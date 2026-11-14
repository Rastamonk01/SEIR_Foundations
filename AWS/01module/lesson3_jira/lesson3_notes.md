# Lesson 3 Notes: Jira

**Person:** KA (Koffi A)
**Week:** 5
**Time zone:** Australia/Adelaide (ACDT, UTC+10:30)
**Region:** us-east-1 (N. Virginia)

The required homework (A Day in My Shoes) is documented in [README.md](README.md). This file only covers the extra credit.

---

## BAM extra credit

### Instance

| Field                          | Value                                                    |
|--------------------------------|----------------------------------------------------------|
| Instance ID                    | `i-0f6250818d1a31d40`                                    |
| Name tag                       | `saturday-slack-complete-07-11-2026`                     |
| Instance type / AZ             | t2.small / us-east-1d                                    |
| Boot time                      | `2026-11-14 13:12:12` ACDT (= `2026-11-14 02:42:12` UTC) |
| Working directory              | `/opt/balerica-bank` (venv active)                       |
| Jira site                      | `https://mburualex04.atlassian.net`                      |
| Jira project used by `jira.py` | `SEIR` (SEIR-Saga_KA)                                    |
| Jira issue type                | `Bug`                                                    |
| Slack channel                  | `#balerica-alerts-01` (where my Incoming Webhook posts)  |

**ID line:** Like Lesson 1, I set the server timezone first and used this version of the ID line, so `date` and `uptime -s` both print in ACDT:

```bash
whoami && TZ='Your/Zone' date && ec2-metadata -i && uptime -s
```

```bash
## Swapped ID
> sudo timedatectl set-timezone Australia/Adelaide
##### set the timezone
> whoami && date && timedatectl show -p Timezone --value && ec2-metadata -i && uptime -s && uptime -p
##### gets all ID and server running period/time
```

### Evidence summary

| BAM       | Where          | Instance ID           | Time (ACDT) | Result                                       | Screenshot                              |
|-----------|----------------|-----------------------|-------------|----------------------------------------------|-----------------------------------------|
| pre-check | Terminal       | `i-0f6250818d1a31d40` | 13:18:25    | `slack.py --test` → SUCCESS                  | `slack_testid.png`                      |
| 5.1       | Notepad + Jira | n/a (browser)         | —           | Config note + test issue SEIR-61             | `BAM_5.1.png`                           |
| 5.2       | Terminal       | `i-0f6250818d1a31d40` | 13:44:18    | `jira.py --verify` → Connected to SEIR       | `BAM_5.2.png`                           |
| 5.3       | Terminal       | `i-0f6250818d1a31d40` | 13:46:06    | `incident.py --test` → SEIR-62, Slack `sent` | `BAM_5.3.png`                           |
| 5.4       | Slack          | n/a (Slack)           | 1:56 PM     | Alert with clickable SEIR-62 link            | `BAM_5.4.png`                           |
| 5.5       | Jira           | n/a (browser)         | 1:58 PM     | SEIR-62 key, title, project                  | `BAM_5.5.png`                           |
| 5.5 check | Terminal       | `i-0f6250818d1a31d40` | —           | `.env` variable names present                | `BAM_5.5_troubleshooting.png`           |
| 5.6       | Terminal       | `i-0f6250818d1a31d40` | 14:13:10    | Two runs, same key SEIR-63                   | `BAM_5.6.png`                           |
| 5.6       | Slack / Jira   | n/a                   | 2:13 PM     | One alert, one issue (SEIR-63)               | `BAM_5.6_slack.png`, `BAM_5.6_jira.png` |
| 5.7       | Jira           | n/a (Jira)            | —           | *pending: one-day sprint*                    | `BAM_5.7.png`                           |

---

### Pre-check: Slack on its own

Before adding Jira I confirmed Slack still worked, so I'd know any later failure was in Jira, not Slack.

```bash
cd /opt/balerica-bank
source venv/bin/activate
python3 slack.py --test
```

```text
SUCCESS: Chewbacca approves!
```

---

### BAM_5.1: Private config (jira_install.md Steps 4–5)

I saved my non-secret Jira config in a private note on my laptop. The API token is **not** in this note.

```text
JIRA_SITE_URL=https://mburualex04.atlassian.net/
JIRA_EMAIL=(blurred)
JIRA_PROJECT_KEY=SEIR
JIRA_TEST_ISSUE_KEY=SEIR-61
JIRA_DEFAULT_ISSUE_TYPE=Bug
```

Manual test incident: **SEIR-61 "TEST - EC2 application error"** (type Bug), with the description from `jira_install.md` Step 3.

Step 5 checklist:

- [x] I created my own Atlassian account.
- [x] I can open my Jira Cloud site.
- [x] I selected or confirmed the Free plan.
- [x] I created the Balerica AI Incident Management project.
- [x] I know my **actual** project key.
- [x] I created and opened a manual test incident.
- [x] I saved the site URL, email, project key, and test issue key privately.
- [x] I have **not** shared any passwords or API tokens.

---

### BAM_5.2: API token and `jira.py --verify`

1. I created a classic Atlassian API token at id.atlassian.com → Security → API tokens and stored it only in my private note and in `.env`.
2. I copied `jira.py` and `incident.py` from the class repo into `/opt/balerica-bank`, next to `slack.py`.
3. I **appended** the Jira variables to my existing `.env` with nano, so the Slack settings stayed in place.

```bash
python3 -m pip install requests python-dotenv
python3 jira.py --verify
```

```text
Requirement already satisfied: requests ... python-dotenv ...
Connected to Jira project: SEIR (SEIR-Saga_KA)
```

---

### BAM_5.3: Full chain test

```bash
mkdir -p data
python3 slack.py --test
python3 jira.py --verify
python3 incident.py --dry-run
python3 incident.py --test
```

```text
SUCCESS: Chewbacca approves!
Connected to Jira project: SEIR (SEIR-Saga_KA)
EC2 agent -> incident.py -> Jira ticket -> Slack alert (includes Jira link)
No API calls made. Run --test when .env is configured.
{
  "incident_id": "SEIR-TEST-20261114T031607764025",
  "jira_key": "SEIR-62",
  "jira_url": "https://mburualex04.atlassian.net/browse/SEIR-62",
  "jira_created": true,
  "slack_status": "sent"
}
```

I ran `--test` **once only**, as instructed.

---

### BAM_5.4 and 5.5: Verifying both systems

- **Slack (5.4):** `#balerica-alerts-01` received a `BALERICA AI ALERT` from agent `incident.py` for incident `SEIR-TEST-20261114T031607764025`, with the clickable link `https://mburualex04.atlassian.net/browse/SEIR-62`. I clicked it and it opened the right issue.
- **Jira (5.5):** issue **SEIR-62** in **SEIR-Saga_KA**, titled `[Balerica AI][ERROR] incident.py: SEIR Foundations integration test: simulated application failure`. Its description has the source agent, severity, incident ID, problem, evidence and recommended investigation.

#### How the flow works

When I run `incident.py --test`, it creates a test incident with a unique ID and passes it to `report_incident()`. That function first checks the local SQLite database to see whether this incident ID already has a Jira ticket. If not, it calls `jira.create_incident()`, which uses the Jira REST API (with my email and API token from `.env`) to create an issue and get back its key and URL, here SEIR-62. The key and URL are saved to SQLite, and then `slack.send_alert()` posts a short alert through my Incoming Webhook to `#balerica-alerts-01`, ending with the Jira link. Jira is called before Slack because Jira is the permanent incident record, and the Slack alert needs that ticket URL so the engineer can click straight through to the details. Slack is only the notification, so if Slack fails the ticket still exists, and re-running with the same incident ID retries only the Slack message. I didn't trust the terminal output alone: I confirmed the alert in Slack, clicked the link, and checked that SEIR-62 described the same incident.

#### Troubleshooting check I performed

After adding the Jira settings, I checked that I hadn't overwritten my Slack settings, and I checked it without printing any secrets:

```bash
chmod 600 .env
grep -o '^[A-Z_]*=' .env
```

```text
SLACK_WEBHOOK_URL=
SLACK_ALERT_CHANNEL=
SLACK_ALERTS_ENABLED=
SLACK_ALERT_SEVERITY=
JIRA_SITE_URL=
JIRA_EMAIL=
JIRA_API_TOKEN=
JIRA_PROJECT_KEY=
JIRA_ISSUE_TYPE=
JIRA_ENABLED=
INCIDENT_STATE_DB=
```

All 11 variable names were present with the exact spellings the scripts expect. `chmod 600` means only the owner can read the file. This is the first check on the "Slack worked yesterday, not today" row of the failure map.

---

### BAM_5.6: Duplicate detection

[`bam_dup.py`](bam_dup.py), in `/opt/balerica-bank`:

```python

## change 'KA' to your initials
from incident import report_incident

r = report_incident(agent='bam_dup.py', severity='ERROR',
                    message='BAM duplicate-detection test',
                    incident_id='BAM-DUP-KA-001',
                    evidence='Synthetic test only',
                    recommendation='Confirm the second run reuses the same Jira key.')
print(r)
```

```bash
python3 bam_dup.py
python3 bam_dup.py
sqlite3 data/incident_state.db "SELECT incident_id, jira_key, slack_sent FROM incidents;"
```

```text
{'incident_id': 'BAM-DUP-KA-001', 'jira_key': 'SEIR-63', ..., 'jira_created': True,  'slack_status': 'sent'}
{'incident_id': 'BAM-DUP-KA-001', 'jira_key': 'SEIR-63', ..., 'jira_created': False, 'slack_status': 'already_sent'}
SEIR-TEST-20261114T031607764025|SEIR-62|1
BAM-DUP-KA-001|SEIR-63|1
```

| Run | jira_key | jira_created | slack_status     |
|-----|----------|--------------|------------------|
| 1   | SEIR-63  | True         | sent             |
| 2   | SEIR-63  | **False**    | **already_sent** |

Both runs returned the same key, Jira has only one issue (SEIR-63), and Slack received only one alert.

#### Where the incident ID is stored

The ID is stored on the EC2 instance in the SQLite database **`/opt/balerica-bank/data/incident_state.db`** (the path comes from `INCIDENT_STATE_DB` in `.env`), in the **`incidents`** table. `incident_id` is the table's **PRIMARY KEY**, and each row also stores `jira_key`, `jira_url`, `slack_sent` and `created_at`. On the second run, `report_incident()` found the existing `BAM-DUP-KA-001` row, so it returned SEIR-63 without calling Jira. Because `slack_sent` was already `1`, it skipped Slack too. This works only while the incident ID stays the same and the database file isn't deleted. A new ID, or a deleted `data/` folder, would create a second ticket.

---

### BAM_5.7: One-day sprint in SEIR-Saga_KA

*(To be filled in after the sprint.)*

|                  | Value                     |
|------------------|---------------------------|
| Sprint           | SEIR Sprint 1             |
| Date             | 2026-11-__                |
| Points committed | 69 (6 stories + 24 tasks) |
| Points completed | __                        |
| Completion       | __%                       |

**What didn't get done:**

- [item (points): reason]

**Unplanned work added mid-sprint:**

- [item (points): why it came up]

**Reflection:** [1–2 sentences on what the burndown showed, e.g. a flat line during the deep work block, then a drop in the evening.]

---

## Security

- The Jira API token and Slack webhook URL exist only in `/opt/balerica-bank/.env` (`chmod 600`) and my private note. They are not in any screenshot, file or commit.
- My email is blurred in `BAM_5.1.png`.
- `.env` and `data/incident_state.db` stay on the instance and are not committed.
