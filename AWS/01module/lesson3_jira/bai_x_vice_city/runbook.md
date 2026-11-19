# Runbook: Deploy and Run the GTA 6 Incident Drills

This runbook deploys `gta6_incidents.py` onto an EC2 instance that already runs the Balerica AI incident flow, then fires the themed incidents and checks the results.

**Time needed:** about 15 minutes.
**Run commands one at a time.** Read each result before moving on.

---

## 0. Before you start

You need an instance where the base incident chain **already works**. If it doesn't, follow the main redeploy `runbook.md` (bank → Slack → Jira) first.

- [ ] `/opt/balerica-bank` contains `incident.py`, `jira.py`, `slack.py` and `.env`
- [ ] `python3 slack.py --test` succeeds
- [ ] `python3 jira.py --verify` succeeds
- [ ] You have a copy of `gta6_incidents.py` (GitHub repo or local file)

---

## 1. Connect and run the ID line

```bash
sudo timedatectl set-timezone Australia/Adelaide
whoami && date && timedatectl show -p Timezone --value && ec2-metadata -i && uptime -s && uptime -p
cd /opt/balerica-bank
source venv/bin/activate
ls incident.py jira.py slack.py .env
```

Write down the **instance ID**.

---

## 2. Put the script on the instance

**Option A: paste it in with nano.**

```bash
nano gta6_incidents.py
```

Paste in the whole file, then save and exit: `Ctrl+O`, `Enter`, `Ctrl+X`.

**Option B: from your GitHub repo.**

```bash
cd ~ && git clone https://github.com/Rastamonk01/SEIR_Foundations.git 2>/dev/null || (cd ~/SEIR_Foundations && git pull)
cp ~.../lesson3_jira/Balerica_AI_X_Vice_City/gta6_incidents.py /opt/balerica-bank/
cd /opt/balerica-bank
```

---

## 3. Create `.env2`

`.env2` holds **only** the settings that should differ for the drills. Anything you leave out, such as the Jira site, email, token and Slack webhook, is read from `.env`.

```bash
touch .env2 && chmod 600 .env2
nano .env2
```

```dotenv
JIRA_PROJECT_KEY=SEIR
JIRA_ISSUE_TYPE=Task
INCIDENT_STATE_DB=data/gta6_state.db
```

> 💡 **Recommended:** set `JIRA_PROJECT_KEY=SEIR` (the incident project) so drill tickets don't fill your SEIR-Saga sprint space. Whatever project you use, `JIRA_ISSUE_TYPE` must exist in it.
>
> **Optional:** to send drill alerts to a different Slack channel, create a second Incoming Webhook and add `SLACK_WEBHOOK_URL=…` to `.env2`.

Check the variable names without printing any values:

```bash
grep -o '^[A-Z_]*=' .env2
```

You should see `JIRA_PROJECT_KEY=`, `JIRA_ISSUE_TYPE=` and `INCIDENT_STATE_DB=`.

---

## 4. Check the script (no API calls)

```bash
python3 -m py_compile gta6_incidents.py && echo OK
python3 gta6_incidents.py --list
python3 gta6_incidents.py --dry-run --scenario vice-bank-heist
```

What you should see:

- `OK`
- A table of 12 scenarios
- A JSON preview ending with `No API calls made. A real run would load .env2 first.`

---

## 5. Fire one incident

```bash
python3 gta6_incidents.py --scenario vice-bank-heist
```

The first line should confirm your settings:

```text
Loaded .env2 | Jira project: SEIR | state DB: data/gta6_state.db
```

Then you should get JSON with `"jira_created": true` and `"slack_status": "sent"`.

**Check both systems:**

- [ ] **Slack:** a CRITICAL alert from `heist_watch.py` with the ★★★★★ bar and a clickable Jira link
- [ ] **Jira:** the ticket title starts `[Balerica AI][CRITICAL] heist_watch.py: [GTA6 ★★★★★] Vice City branch vault breach…`

---

## 6. Prove there are no duplicates

```bash
python3 gta6_incidents.py --scenario vice-bank-heist
sqlite3 data/gta6_state.db "SELECT incident_id, jira_key, slack_sent FROM incidents WHERE incident_id LIKE 'GTA6%';"
```

You should get the **same** `jira_key`, with `jira_created: false` and `slack_status: already_sent`. The query should show `GTA6-HEIST-001|<KEY>|1`.

> ⚠️ Query **`data/gta6_state.db`**, not `data/incident_state.db`. The drills use the state DB set in `.env2`, so the main DB has no GTA6 rows.

---

## 7. Test the severity filter

```bash
python3 gta6_incidents.py --scenario patrol-spotted
```

 A Jira ticket should be created with `slack_status: filtered_or_disabled`, and no Slack message should appear. That's correct, because WARNING is below `SLACK_ALERT_SEVERITY=ERROR`.

---

## 8. More runs

```bash
python3 gta6_incidents.py --random                                   # one random scenario
python3 gta6_incidents.py --scenario cobol-core-down --run-id 002    # a NEW incident
python3 gta6_incidents.py --all --yes                                # all 12 scenarios
```

`--all --yes` creates up to 12 tickets and about 10 Slack alerts. Scenarios you've already fired are reused, not duplicated.

| Scenario            | Stars    | Severity | Agent           |
| --------------------|----------|--------- |-----------------|
| vice-bank-heist     | ★★★★★ | CRITICAL | heist_watch.py  |
| leonida-atm-drain   | ★★★★☆ | CRITICAL | atm_monitor.py  |
| offshore-wire-spree | ★★★★☆ | CRITICAL | swift_watch.py  |
| card-club-spree     | ★★★★☆ | CRITICAL | fraud_watch.py  |
| scanner-flood       | ★★★★☆ | CRITICAL | telemetry.py    |
| cobol-core-down     | ★★★☆☆ | ERROR    | cobol.py        |
| rush-hour-latency   | ★★★☆☆ | ERROR    | health.py       |
| safehouse-disk-full | ★★★☆☆ | ERROR    | health.py       |
| pay-n-spray-ledger  | ★★★☆☆ | ERROR    | auditor.py      |
| inside-crew-login   | ★★★☆☆ | ERROR    | analyze_logs.py |
| patrol-spotted      | ★★☆☆☆ | WARNING  | analyze_logs.py |
| radio-check         | ★☆☆☆☆ | INFO     | health.py       |

---

## 9. Troubleshooting

| Symptom                                                   | Fix                                                                                            |
|-----------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `Settings file .env2 not found`                           | Create `.env2` in `/opt/balerica-bank`, or pass `--env-file PATH`                              |
| `Loaded .env2 \| Jira project: …` shows the wrong project | Fix `JIRA_PROJECT_KEY` in `.env2`, which takes priority over `.env`                            |
| SQLite query prints nothing                               | You queried `incident_state.db`; use `data/gta6_state.db`                                      |
| `"error": "JiraError"`                                    | Run `python3 jira.py --verify`; see the main runbook's error table (401/403/404/400)           |
| `Jira HTTP 400`                                           | `JIRA_ISSUE_TYPE` in `.env2` doesn't exist in that project                                     |
| `slack_status: filtered_or_disabled` on ERROR/CRITICAL    | `SLACK_ALERTS_ENABLED=true`, `SLACK_ALERT_SEVERITY=ERROR`                                      |
| `slack_status: failed_…`                                  | Run `python3 slack.py --test`; check the webhook. Rerun the same scenario to retry Slack only. |
| `ModuleNotFoundError`                                     | `source venv/bin/activate`, then `pip install requests python-dotenv`                          |
| `--all` refuses to run                                    | Add `--yes` to confirm                                                                         |
| Want to fire a scenario fresh                             | Use a new `--run-id` (e.g. `002`)                                                              |

---

## 10. Cleanup

1. **Jira:** find the drill tickets by searching for `GTA6`, then delete or close them.
2. **Reset the drill state** if you want to start the IDs again from scratch:

   ```bash
   rm data/gta6_state.db
   ```

3. **Teardown:** terminate the instance, then check **Volumes** and **Elastic IPs** for anything left behind.

---

## Security

- `.env` and `.env2` stay at `chmod 600` and are **never** committed. Add both to `.gitignore`.
- Never show token, webhook or `.env`/`.env2` contents in screenshots. Use `grep -o '^[A-Z_]*='` to show names only.
- All scenarios are synthetic. Don't put real customer data in incident messages.
