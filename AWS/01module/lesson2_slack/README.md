# Seven Alerts, Seven Wins: Lesson 2 Slack Homework

## Measure → Decide → Alert, from my own EC2 instance

![AWS EC2](https://img.shields.io/badge/AWS-EC2_us--east--1-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9_+_venv-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Slack](https://img.shields.io/badge/Slack-Incoming_Webhook-4A154B?style=for-the-badge&logo=slack&logoColor=white)

![Scripts](https://img.shields.io/badge/Scripts-7_of_7-yellow?style=for-the-badge)
![Experiments](https://img.shields.io/badge/Experiments-3_of_3-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

Applied Cloud & Platform Engineering, Lesson 2 homework: seven Python scripts that call `send_alert()` from `slack.py`, going from a hello message to a real disk and load monitor and a full morning report. Then three experiments on the `.env` controls.

> **Goal:** Prove, with my own evidence, that a script on EC2 can measure something, choose a severity, and deliver an alert to Slack, and that `.env` settings control what gets through without touching code.

---

## File Structure

```text
SEIR_Foundations/
└── AWS/
    └── 01module/
        └── lesson2_slack/
            ├── screenshots/
            │   ├── slack_instance_id_n_check.png
            │   ├── slack_setup_n_check.png
            │   ├── slack_hw1.png            slack_hw1_instance.png
            │   ├── slack_hw2.png            slack_hw2_instance.png
            │   ├── slack_hw3.png            slack_hw3_instance.png
            │   ├── slack_hw4.png            slack_hw4_instance.png
            │   ├── slack_hw5.png            slack_hw5_instance.png
            │   ├── slack_hw6.png            slack_hw6_instance.png
            │   ├── slack_hw7.png            slack_hw7_instance.png
            │   ├── slack_experiment1.png    slack_experiment1_instance.png
            │   ├── slack_experiment2.png    slack_experiment2_instance.png
            │   ├── slack_experiment3.png    slack_experiment3_instance.png
            │   └── slack_experiment_back_to_original.png
            ├── lesson2_notes.md
            ├── README.md
            └── runbook.md
```

---

## Run summary

**Person:** KA (Koffi A)
**Time zone:** Australia/Adelaide (ACDT, UTC+10:30)
**Instance:** `i-0dd5a5ab6d189b4fe` (t2.small, us-east-1d, boot `2026-11-21 07:28:56` ACDT)
**Channel:** `#balerica-alerts-01`
**Threshold during homework:** `SLACK_ALERT_SEVERITY=INFO`

| Script                   | What it does              | Result                                              |
|--------------------------|---------------------------|-----------------------------------------------------|
| hw1_hello_slack.py       | My own first alert        | INFO, "Hello from Koffi A!"                         |
| hw2_severity_tour.py     | Sends all four severities | All 4 delivered                                     |
| hw3_server_time.py       | Reports server time       | 21:45:02 **UTC**, 10h30m behind my ACDT clock       |
| hw4_disk_watch.py        | Disk usage → severity     | 25.8% used, 5.9 GB free → INFO                      |
| hw5_load_check.py        | Load average vs CPU count | 0.00 / 0.01 / 0.00 on 1 CPU → INFO                  |
| hw6_incident_drill.py ×3 | Random fake bank incident | DRILL-5050 ERROR, DRILL-4041 ERROR, DRILL-9922 INFO |
| hw7_morning_report.py    | Combined status report    | Time, host, Python 3.9.25, disk 25.8%, load 0.00    |

| Experiment | Change                                     | Result                                           |
|------------|--------------------------------------------|--------------------------------------------------|
| 1          | `SLACK_ALERT_SEVERITY=CRITICAL`, rerun hw2 | Predicted 1 of 4, got **1 of 4** (CRITICAL only) |
| 2          | `SLACK_ALERTS_ENABLED=false`, run hw1      | **Skipped**, nothing sent: the kill switch works |
| 3          | hw4 WARNING threshold 75 → 20              | Same 25.8% disk went **INFO → WARNING**          |

Afterwards I put everything back: `SLACK_ALERT_SEVERITY=INFO`, `SLACK_ALERTS_ENABLED=true`, and the original `hw4_disk_watch.py`. The answers to all five "In your notes:" questions are in [lesson2_notes.md](lesson2_notes.md).

---

## Screenshots

### Setup

📸 **[`slack_instance_id_n_check`](screenshots/slack_instance_id_n_check.png):** the ID line for `i-0dd5a5ab6d189b4fe` (Sat Nov 21 07:33:34 ACDT 2026, boot `07:28:56`), then `python3 slack.py --test` returning **SUCCESS: Chewbacca approves!**

📸 **[`slack_setup_n_check`](screenshots/slack_setup_n_check.png):** `ls hw*.py` listing all seven scripts, then `SLACK_ALERT_SEVERITY` set to **INFO** and checked with `grep` (non-secret values only).

### The seven scripts

📸 **[`slack_hw1`](screenshots/slack_hw1.png) / [`_instance`](screenshots/slack_hw1_instance.png):** `MY_NAME` edited in nano, then **"Hello from Koffi A! I sent this alert myself, from my own EC2 instance."** (INFO, HW-001, 8:01 AM).

📸 **[`slack_hw2`](screenshots/slack_hw2.png) / [`_instance`](screenshots/slack_hw2_instance.png):** **INFO, WARNING, ERROR and CRITICAL** all delivered (HW-002, 8:10 AM).

📸 **[`slack_hw3`](screenshots/slack_hw3.png) / [`_instance`](screenshots/slack_hw3_instance.png):** server time **Friday November 20, 2026 at 21:45:02 UTC**, and `date` showing **Sat Nov 21 08:18:04 ACDT 2026**, about 10.5 hours apart.

📸 **[`slack_hw4`](screenshots/slack_hw4.png) / [`_instance`](screenshots/slack_hw4_instance.png):** **Disk 25.8% used, 5.9 GB free → INFO** (HW-004, 8:25 AM).

📸 **[`slack_hw5`](screenshots/slack_hw5.png) / [`_instance`](screenshots/slack_hw5_instance.png):** **Load 0.00 (1m), 0.01 (5m), 0.00 (15m) on 1 CPU → INFO** (HW-005).

📸 **[`slack_hw6`](screenshots/slack_hw6.png) / [`_instance`](screenshots/slack_hw6_instance.png):** three drills, **DRILL-5050** and **DRILL-4041** (ERROR, `/payments` 500s) and **DRILL-9922** (INFO, nightly backup OK).

📸 **[`slack_hw7`](screenshots/slack_hw7.png) / [`_instance`](screenshots/slack_hw7_instance.png):** the ID line (Sat Nov 21 08:33:42 ACDT 2026, `i-0dd5a5ab6d189b4fe`), then the **MORNING REPORT**: `2026-11-20 22:03:43 UTC`, host `ip-172-31-43-116.ec2.internal (Linux x86_64)`, Python 3.9.25, disk 25.8%, load 0.00. It was delivered to Slack as HW-007.

### Experiments

📸 **[`slack_experiment1`](screenshots/slack_experiment1.png) / [`_instance`](screenshots/slack_experiment1_instance.png):** threshold **CRITICAL**: INFO, WARNING and ERROR skipped, **only CRITICAL delivered** (8:45 AM).

📸 **[`slack_experiment2`](screenshots/slack_experiment2.png) / [`_instance`](screenshots/slack_experiment2_instance.png):** `SLACK_ALERTS_ENABLED=false`, and hw1 printed **Skipped**. The channel's latest message is still the 8:45 AM CRITICAL from Experiment 1, so no new alert arrived.

📸 **[`slack_experiment3`](screenshots/slack_experiment3.png) / [`_instance`](screenshots/slack_experiment3_instance.png):** hw4 threshold changed to `elif percent_used >= 20`, and the same **25.8% disk became WARNING** (HW-004, 8:53 AM).

📸 **[`slack_experiment_back_to_original`](screenshots/slack_experiment_back_to_original.png):** `hw4_disk_watch.py` restored from the backup, with `SLACK_ALERTS_ENABLED=true` and `SLACK_ALERT_SEVERITY=INFO` confirmed.

---

## What I learned

- **Configuration changes behaviour without touching code.** One `.env` line decided whether 4, 1 or 0 alerts arrived.
- **Monitors follow measure → decide → alert.** hw4 and hw5 measure real numbers, and the `if/else` thresholds decide how much they matter.
- **Quiet is a valid result.** INFO on a healthy box is correct, and noisy thresholds create alert fatigue.
- **Servers use UTC.** My server was still on Friday while I was already on Saturday in Adelaide.
- **Kill switches are for maintenance windows.** Silence everything with one setting, and put switching it back on in the checklist.

To redo this homework on a new instance, follow [runbook.md](runbook.md).
