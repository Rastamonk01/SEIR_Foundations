# Balerica AI x Vice City: GTA 6-Themed Incident Drills

![GTA6 EDITION](screenshots/bai_x_vice_city.jpg)

*Image Credit: Alexander (Balerica)*

## Wanted Level → Severity → Jira Ticket → Slack Alert

![AWS EC2](https://img.shields.io/badge/AWS-EC2_us--east--1-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3_+_venv-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-Cloud_REST_API-0052CC?style=for-the-badge&logo=jira&logoColor=white)
![Slack](https://img.shields.io/badge/Slack-Incoming_Webhook-4A154B?style=for-the-badge&logo=slack&logoColor=white)
![SQLite](https://img.shields.io/badge/State-SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

![Scenarios](https://img.shields.io/badge/Scenarios-12-yellow?style=for-the-badge)
![Tickets](https://img.shields.io/badge/Jira_Tickets-13-blue?style=for-the-badge)
![Alerts](https://img.shields.io/badge/Slack_Alerts-11-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

Applied Cloud & Platform Engineering, extension of Lesson 3: I added 12 Vice City-themed incident scenarios on top of the course's `incident.py` coordinator. Each scenario has a **wanted level** (1–5 stars) that sets its severity, and every incident goes Jira first, then Slack.

> **Goal:** Exercise the full incident pipeline with realistic, varied, *synthetic* banking incidents. Prove the severity filter, duplicate detection and separate settings (`.env2`) all work, without touching the main `.env`.

All scenarios are fictional test data. No real customer data is used. The GTA 6 theme is a fan-made naming style only.

---

## File Structure

```text
SEIR_Foundations/
└── AWS/
    └── 01module/
        └── lesson3_jira/
            ├── bai_x_vice_city/
            │   ├── screenshots/
            │   │   ├── bai_x_vice_city.jpg
            │   │   ├── gta6_instance_id.png
            │   │   ├── gta6_incidents_test_run.png
            │   │   ├── gta6_instance_incident_run.png
            │   │   ├── gta6_incident_slack.png
            │   │   ├── gta6_incident_jira.png
            │   │   ├── gta6_instance_incident_no_duplicates.png
            │   │   ├── gta6_instance_incident_no_duplicates_02.png
            │   │   ├── gta6_instance_incident_severity_filter.png
            │   │   ├── gta6_instance_incident_severity_filter_jira.png
            │   │   ├── gta6_troubleshoot.png
            │   │   ├── gta6_instance_incident_other_runs_01.png
            │   │   ├── gta6_instance_incident_other_runs_02.png
            │   │   ├── gta6_instance_incident_other_runs_03.png
            │   │   ├── gta6_instance_incident_other_runs_jira.png
            │   │   ├── gta6_instance_incident_other_runs_slack_01.png
            │   │   └── gta6_instance_incident_other_runs_slack_02.png
            │   ├── gta6_incidents.py
            │   ├── README.md
            │   └── runbook.md
            ├── screenshots/
            ├── bam_dup.py
            ├── lesson3_notes.md
            ├── README.md
            └── runbook.md
```

On the EC2 instance, the script sits in `/opt/balerica-bank` next to `incident.py`, `jira.py`, `slack.py`, `.env` and `.env2`.

---

## Architecture

```text
gta6_incidents.py  (12 scenarios, wanted level -> severity)
        |  loads .env2 first (override), then incident.py loads .env for anything missing
        v
   incident.py  report_incident()
        |  checks data/gta6_state.db for the incident ID
        +--> jira.py  --> Jira issue (the incident record)
        +--> slack.py --> Slack alert with the Jira link (ERROR and CRITICAL only)
```

| Stars             | Severity  | Jira | Slack (threshold `ERROR`) |
| ----------------- | --------- | ---- | ------------------------- |
| ★☆☆☆☆             | INFO      | ✅   | filtered                  |
| ★★☆☆☆             | WARNING   | ✅   | filtered                  |
| ★★★☆☆             | ERROR     | ✅   | ✅                        |
| ★★★★☆ / ★★★★★     | CRITICAL  | ✅   | ✅                        |

Each scenario has a **stable incident ID**, `GTA6-<CODE>-<run-id>` (for example `GTA6-HEIST-001`). Running it again reuses the same ticket, and `--run-id 002` opens a new one.

---

## Run log

**Person:** KA (Koffi A)
**Time zone:** Australia/Adelaide (ACDT, UTC+10:30)
**Region:** us-east-1

| Field            | Value                                                    |
|------------------|----------------------------------------------------------|
| Instance ID      | `i-04f4b1b37c819b13d`                                    |
| Name tag         | `pre-GTA-tuesday-class-middle-jira-complete-18-11-2026`  |
| Type / AZ        | t2.small / us-east-1d                                    |
| Boot time        | `2026-11-19 09:59:01` ACDT (= `2026-11-18 23:29:01` UTC) |
| User / directory | `ec2-user` / `/opt/balerica-bank` (venv active)          |

The `.env2` I used contains only these variables. Everything else, such as the Jira site, token and Slack webhook, falls back to `.env`:

```dotenv
JIRA_PROJECT_KEY=SEIR
JIRA_ISSUE_TYPE=Task
INCIDENT_STATE_DB=data/gta6_state.db
```

The script confirms it on every real run:

```text
Loaded .env2 | Jira project: SEIR | state DB: data/gta6_state.db
```

---

## Results

| Scenario                         | Stars   | Severity | Incident ID       | Jira    | Slack                |
|----------------------------------|---------|----------|-------------------|---------|----------------------|
| vice-bank-heist                  | ★★★★★ | CRITICAL | GTA6-HEIST-001    | SEIR-65 | sent                 |
| patrol-spotted                   | ★★☆☆☆ | WARNING  | GTA6-AUTHFAIL-001 | SEIR-66 | filtered_or_disabled |
| rush-hour-latency (`--random`)   | ★★★☆☆ | ERROR    | GTA6-LATENCY-001  | SEIR-67 | sent                 |
| cobol-core-down (`--run-id 002`) | ★★★☆☆ | ERROR    | GTA6-COBOL-002    | SEIR-68 | sent                 |
| card-club-spree                  | ★★★★☆ | CRITICAL | GTA6-CARD-001     | SEIR-69 | sent                 |
| cobol-core-down                  | ★★★☆☆ | ERROR    | GTA6-COBOL-001    | SEIR-70 | sent                 |
| inside-crew-login                | ★★★☆☆ | ERROR    | GTA6-LOGIN-001    | SEIR-71 | sent                 |
| leonida-atm-drain                | ★★★★☆ | CRITICAL | GTA6-ATM-001      | SEIR-72 | sent                 |
| offshore-wire-spree              | ★★★★☆ | CRITICAL | GTA6-SWIFT-001    | SEIR-73 | sent                 |
| pay-n-spray-ledger               | ★★★☆☆ | ERROR    | GTA6-LEDGER-001   | SEIR-74 | sent                 |
| radio-check                      | ★☆☆☆☆ | INFO     | GTA6-RADIO-001    | SEIR-75 | filtered_or_disabled |
| safehouse-disk-full              | ★★★☆☆ | ERROR    | GTA6-DISK-001     | SEIR-76 | sent                 |
| scanner-flood                    | ★★★★☆ | CRITICAL | GTA6-DDOS-001     | SEIR-77 | sent                 |

**Totals:** 12 scenarios plus 1 extra run-id gave **13 Jira tickets** (SEIR-65 to SEIR-77) and **11 Slack alerts**. The WARNING and INFO tickets correctly got no alert.

**Duplicate detection held during `--all --yes`:** `GTA6-HEIST-001` (SEIR-65), `GTA6-LATENCY-001` (SEIR-67) and `GTA6-AUTHFAIL-001` (SEIR-66) had already been fired. All three came back with `jira_created: false` and no new ticket. HEIST and LATENCY showed `already_sent`, and AUTHFAIL stayed `filtered_or_disabled`.

### State database

The SQLite file `data/gta6_state.db` (set by `INCIDENT_STATE_DB` in `.env2`) has **exactly 13 rows**, one per incident ID, and each maps to a single Jira key:

```text
$ sqlite3 data/gta6_state.db "SELECT incident_id, jira_key, slack_sent FROM incidents WHERE incident_id LIKE 'GTA6%';"
GTA6-HEIST-001|SEIR-65|1
GTA6-AUTHFAIL-001|SEIR-66|0
GTA6-LATENCY-001|SEIR-67|1
GTA6-COBOL-002|SEIR-68|1
GTA6-CARD-001|SEIR-69|1
GTA6-COBOL-001|SEIR-70|1
GTA6-LOGIN-001|SEIR-71|1
GTA6-ATM-001|SEIR-72|1
GTA6-SWIFT-001|SEIR-73|1
GTA6-LEDGER-001|SEIR-74|1
GTA6-RADIO-001|SEIR-75|0
GTA6-DISK-001|SEIR-76|1
GTA6-DDOS-001|SEIR-77|1
```

- `incident_id` is the PRIMARY KEY, so one ID can never map to two tickets.
- `slack_sent = 1` for the 11 ERROR/CRITICAL incidents, which matches the 11 Slack alerts.
- `slack_sent = 0` for **AUTHFAIL (WARNING)** and **RADIO (INFO)**. Slack filtered them, so they were never marked as sent. If the threshold were lowered later, rerunning those IDs would send their alerts without creating new tickets.

> **Note:** SEIR-64 (`[INFO] jira.py: SEIR Foundations Jira integration test`) came from a separate `jira.py --test` run and is not part of this drill.

---

## Screenshots

📸 **Screenshot [`gta6_instance_id`](screenshots/gta6_instance_id.png):** the ID line for `i-04f4b1b37c819b13d`, run as `ec2-user` (Thu Nov 19 10:04:01 ACDT 2026, boot `09:59:01`).

📸 **Screenshot [`gta6_incidents_test_run`](screenshots/gta6_incidents_test_run.png):** `py_compile` printing **OK**, `--list` showing all 12 scenarios with wanted level, severity and agent, then `--dry-run --scenario vice-bank-heist` ending with **No API calls made. A real run would load .env2 first.**

📸 **Screenshot [`gta6_instance_incident_run`](screenshots/gta6_instance_incident_run.png):** the first real run. It prints **Loaded .env2 | Jira project: SEIR | state DB: data/gta6_state.db**, then `GTA6-HEIST-001` → **SEIR-65**, `jira_created: true`, `slack_status: sent`.

📸 **Screenshot [`gta6_incident_slack`](screenshots/gta6_incident_slack.png):** the CRITICAL Slack alert from `heist_watch.py` with the **★★★★★** wanted bar and a clickable link to **SEIR-65** (11:02 AM).

📸 **Screenshot [`gta6_incident_jira`](screenshots/gta6_incident_jira.png):** Jira ticket **SEIR-65**, `[Balerica AI][CRITICAL] heist_watch.py: [GTA6 ★★★★★] Vice City branch vault breach…`, with source agent, severity, incident ID, evidence and recommendation.

📸 **Screenshot [`gta6_instance_incident_no_duplicates`](screenshots/gta6_instance_incident_no_duplicates.png):** the same scenario run again. It returned the **same SEIR-65**, with `jira_created: false` and `slack_status: already_sent`.

📸 **Screenshot [`gta6_instance_incident_no_duplicates_02`](screenshots/gta6_instance_incident_no_duplicates_02.png):** `sqlite3 data/gta6_state.db` listing all **13 GTA6 incident IDs**, each with one Jira key (SEIR-65 to SEIR-77). `slack_sent` is `1` for the 11 alerted incidents and `0` for the filtered WARNING (AUTHFAIL) and INFO (RADIO) incidents.

📸 **Screenshot [`gta6_instance_incident_severity_filter`](screenshots/gta6_instance_incident_severity_filter.png):** `patrol-spotted` (★★, WARNING) → **SEIR-66** created, `slack_status: filtered_or_disabled`. Slack correctly ignored it because it's below the `ERROR` threshold.

📸 **Screenshot [`gta6_instance_incident_severity_filter_jira`](screenshots/gta6_instance_incident_severity_filter_jira.png):** the WARNING ticket **SEIR-66** in Jira. The incident is still recorded even though no alert was sent.

📸 **Screenshots [`…_slack_01`](screenshots/gta6_instance_incident_other_runs_slack_01.png) and [`…_slack_02`](screenshots/gta6_instance_incident_other_runs_slack_02.png):** the Slack channel after the batch runs, showing only ERROR and CRITICAL alerts (SEIR-67 to 77). There are **no alerts for SEIR-66 (WARNING) or SEIR-75 (INFO)**.

📸 **Screenshot [`gta6_troubleshoot`](screenshots/gta6_troubleshoot.png):** `grep -o '^[A-Z_]*=' .env2`, listing the three variable **names** in `.env2` (`JIRA_PROJECT_KEY`, `JIRA_ISSUE_TYPE`, `INCIDENT_STATE_DB`) without their values.

📸 **Screenshots [`other_runs_01`](screenshots/gta6_instance_incident_other_runs_01.png), [`_02`](screenshots/gta6_instance_incident_other_runs_02.png), [`_03`](screenshots/gta6_instance_incident_other_runs_03.png):** `--random` (rush-hour-latency → SEIR-67), `--scenario cobol-core-down --run-id 002` (→ SEIR-68), and `--all --yes` covering all 12 scenarios, including the three reused tickets.

📸 **Screenshot [`gta6_instance_incident_other_runs_jira`](screenshots/gta6_instance_incident_other_runs_jira.png):** the Jira backlog showing every GTA6 ticket, **SEIR-65 to SEIR-77**, each titled with its severity, agent and wanted bar.

---

## What I learned

- **A separate settings file is cheap isolation.** Loading `.env2` with `override=True` *before* importing `jira.py` matters, because `jira.py` reads its settings at import time. Anything `.env2` doesn't define falls back to `.env`, so I didn't have to copy any secrets.
- **A separate state DB gives a separate dedup history.** `data/gta6_state.db` keeps the drill's incident IDs apart from `data/incident_state.db`. Querying the wrong file returns nothing.
- **Severity filtering is a feature, not a failure.** WARNING and INFO incidents still get a Jira record, but they don't page anyone in Slack.
- **Stable IDs make bulk runs safe.** `--all` reused the tickets for incidents that already existed instead of creating duplicates.
- **Next improvement:** point `.env2` at the dedicated incident project (`SEIR`), so drill tickets don't land in the SEIR-Saga sprint space.

See [runbook.md](runbook.md) to redeploy it step by step.
