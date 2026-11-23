# Lesson 2 Homework Notes: Seven Alerts, Seven Wins

**Person:** KA (Koffi A)
**Time zone:** Australia/Adelaide (ACDT, UTC+10:30)
**Region:** us-east-1 (N. Virginia)

The overview and screenshots are in [README.md](README.md). To redo this homework, use [runbook.md](runbook.md).

---

## Instance

| Field            | Value                                                    |
|------------------|----------------------------------------------------------|
| Instance ID      | `i-0dd5a5ab6d189b4fe`                                    |
| Name tag         | `GTA-KA-middle-jira-complete-19-11-2026`                 |
| Type / AZ        | t2.small (1 vCPU) / us-east-1d                           |
| Boot time        | `2026-11-21 07:28:56` ACDT (= `2026-11-20 20:58:56` UTC) |
| User / directory | `ec2-user` / `/opt/balerica-bank` (venv active)          |
| Slack channel    | `#balerica-alerts-01` (where my Incoming Webhook posts)  |

**ID line:** like Lesson 1, I set the server timezone first, so `date` prints ACDT:

```bash
sudo timedatectl set-timezone Australia/Adelaide
whoami && date && timedatectl show -p Timezone --value && ec2-metadata -i && uptime -s && uptime -p
```

This shows the same facts as the required `whoami && TZ='Australia/Adelaide' date && ec2-metadata -i`: user, local date and instance ID.

---

## Setup

```bash
python3 slack.py --test                       # SUCCESS: Chewbacca approves!
ls hw*.py                                     # all 7 scripts present
sed -i 's/^SLACK_ALERT_SEVERITY=.*/SLACK_ALERT_SEVERITY=INFO/' .env
grep -E '^SLACK_ALERT(S_ENABLED|_SEVERITY)=' .env
```

```text
SLACK_ALERTS_ENABLED=true
SLACK_ALERT_SEVERITY=INFO
```

---

## Run log

| # | Script                   | Slack time (ACDT) | Severity                       | Incident                           | Result                                                                    |
|---|--------------------------|-------------------|--------------------------------|------------------------------------|---------------------------------------------------------------------------|
| 1 | hw1_hello_slack.py       | 8:01 AM           | INFO                           | HW-001                             | "Hello from Koffi A! I sent this alert myself, from my own EC2 instance." |
| 2 | hw2_severity_tour.py     | 8:10 AM           | INFO, WARNING, ERROR, CRITICAL | HW-002                             | All 4 delivered                                                           |
| 3 | hw3_server_time.py       | ~8:15 AM          | INFO                           | HW-003                             | "Friday November 20, 2026 at 21:45:02 UTC"                                |
| 4 | hw4_disk_watch.py        | 8:25 AM           | INFO                           | HW-004                             | 25.8% used, 5.9 GB free                                                   |
| 5 | hw5_load_check.py        | —                 | INFO                           | HW-005                             | Load 0.00 / 0.01 / 0.00 on 1 CPU                                          |
| 6 | hw6_incident_drill.py ×3 | —                 | ERROR, ERROR, INFO             | DRILL-5050, DRILL-4041, DRILL-9922 | All 3 delivered                                                           |
| 7 | hw7_morning_report.py    | 08:33 ACDT        | INFO                           | HW-007                             | Multi-line morning report delivered                                       |

**hw7 output:**

```text
MORNING REPORT — Balerica AI server
- Time: 2026-11-20 22:03:43 UTC
- Host: ip-172-31-43-116.ec2.internal (Linux x86_64)
- Python: 3.9.25
- Disk on / : 25.8% used
- Load (1m): 0.00
- Status: all checks ran. The bank greets the day.

Delivered!
```

---

## Answers to the "In your notes:" questions

### hw2: Which severities arrived, and why those?

**All four arrived: INFO, WARNING, ERROR and CRITICAL.** My `.env` had `SLACK_ALERT_SEVERITY=INFO`, and INFO is the lowest level, so every severity is equal to or above the threshold. `slack.py` ranks the levels INFO 0, WARNING 1, ERROR 2, CRITICAL 3 and skips anything below the minimum *before* calling the webhook. With the class setting (`ERROR`), only ERROR and CRITICAL would have arrived.

### hw3: How many hours apart are server time and your wall clock?

**10 hours 30 minutes.** The script reported `Friday November 20, 2026 at 21:45:02 UTC`, and `date` on the server (set to my timezone) showed `Sat Nov 21 08:18:04 ACDT 2026` a few minutes later. 21:45 UTC + 10:30 = 08:15 ACDT on the next day, so the server is still on Friday while I'm already on Saturday. The script asks for UTC explicitly (`datetime.now(timezone.utc)`), so it reports UTC even though I changed the server timezone with `timedatectl`. Servers use UTC so logs from every region and team line up on one timeline.

### hw4: Why is a quiet INFO here good design, not a failure?

My disk was **25.8% used with 5.9 GB free**, which is healthy, so INFO is the honest answer. If a healthy check fired WARNING or ERROR, people would learn to ignore alerts (alert fatigue) and miss the one that matters. Under the class threshold of `ERROR`, this INFO wouldn't reach Slack at all, and "skipped" there means nothing needs a human. The monitor still ran and measured. It just didn't make noise.

### hw5: What would make this number spike on the Balerica bank?

My load was **0.00 / 0.01 / 0.00 on 1 CPU**, an idle box. It would spike when a lot of work queues at once, for example:

- the end-of-day COBOL batch (`BATCH-EOD`) processing every account
- a burst of SWIFT messages from the traffic generator
- many FastAPI `/payments` requests, each starting a COBOL subprocess
- slow disk I/O on `accounts.dat` / `payments.dat`, which keeps processes waiting
- a runaway script or a request flood or DDoS

On a 1-vCPU t2.small, a 5-minute load above **1.0** means work is waiting in line, which is the script's WARNING rule. Running out of CPU credits on this burstable instance would make it worse.

### hw6: Which fake incident deserves to wake a human at 3 AM?

**The CRITICAL one: `account_lookup returned code 12: ledger file not reachable.`** If the ledger can't be read, the bank can't look up accounts or post payments, so every customer is affected right away. The ERROR `/payments` 500s are a close second. My drills drew that one **twice** (DRILL-5050, DRILL-4041), and if it keeps happening, payments are failing for real customers, so it would justify a page. The rest can wait until morning: the slow batch, queue depth and rejection rate (WARNING/ERROR), and the INFO `Nightly ledger backup completed successfully` I drew as DRILL-9922.

---

## Experiments

### Experiment 1: `SLACK_ALERT_SEVERITY=CRITICAL`, rerun hw2

|                | Messages                                                          |
|----------------|-------------------------------------------------------------------|
| **Prediction** | **1 of 4** (CRITICAL only)                                        |
| **Actual**     | **1 of 4**: CRITICAL delivered (8:45 AM), the other three skipped |

```text
INFO     -> skipped by your threshold
WARNING  -> skipped by your threshold
ERROR    -> skipped by your threshold
CRITICAL -> DELIVERED to Slack
```

The prediction matched. CRITICAL is the highest rank (3), so it's the only level that meets a CRITICAL threshold.

### Experiment 2: `SLACK_ALERTS_ENABLED=false`, run hw1

```text
Skipped. Check .env: SLACK_ALERTS_ENABLED must be true and SLACK_ALERT_SEVERITY=INFO (see homework README).
```

Nothing reached Slack. The channel's last message stayed the 8:45 AM CRITICAL from Experiment 1. `send_alert()` checks `SLACK_ALERTS_ENABLED` **first**, before severity, and returns `False` without contacting the webhook.

**Why a kill switch helps during maintenance windows:** planned work such as patching, restarts, redeploys or a bank batch rerun makes healthy systems look broken for a while. Without a switch, every monitor would page the on-call team with false alarms, and those alarms train people to ignore alerts. One `.env` setting silences everything at once without editing or redeploying code, and switching it back afterwards restores alerting instantly. The risk is forgetting to switch it back on, so it belongs on the maintenance checklist.

### Experiment 3: lower the hw4 WARNING threshold

```bash
cp hw4_disk_watch.py hw4_disk_watch.py.bak
sed -i 's/percent_used >= 75/percent_used >= 20/' hw4_disk_watch.py
python3 hw4_disk_watch.py
```

```text
16:if percent_used >= 90:
18:elif percent_used >= 20:
Disk is 25.8% used -> severity WARNING.
Delivered!
```

**Yes, the severity changed: INFO → WARNING**, with the same 25.8% disk (Slack, 8:53 AM). The data didn't change, only the rule. Thresholds are engineering decisions written in code, and setting them too low causes exactly the alert fatigue described in hw4.

### Everything put back

```bash
mv hw4_disk_watch.py.bak hw4_disk_watch.py
sed -i 's/^SLACK_ALERT_SEVERITY=.*/SLACK_ALERT_SEVERITY=INFO/' .env
sed -i 's/^SLACK_ALERTS_ENABLED=.*/SLACK_ALERTS_ENABLED=true/' .env
grep -E '^SLACK_ALERT(S_ENABLED|_SEVERITY)=' .env
```

```text
SLACK_ALERTS_ENABLED=true
SLACK_ALERT_SEVERITY=INFO
```

---

## Rules followed

- Every message was synthetic. No passwords, keys, customer data or `.env` contents were sent.
- No spam: each script ran once (hw6 three times, hw2 twice), and nothing ran in a loop.
- All scripts still call `send_alert(agent, severity, message, incident_id)` exactly as written. My only edits were `MY_NAME` in hw1 and the temporary threshold in hw4, which I put back.
- Only the variable **names** and the two non-secret values from `.env` were printed. The webhook URL never appears.
