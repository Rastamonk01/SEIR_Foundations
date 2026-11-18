# Runbook: Redeploy the Balerica AI Incident Integration (EC2 + Slack + Jira)

This runbook takes you from a **brand-new EC2 instance** to a working incident flow:

```text
incident.py ──► jira.py ──► Jira issue (the incident record)
            └─► slack.py ──► #balerica-alerts (the alert, with a Jira link)
```

**Time needed:** about 30 minutes.
**Run commands one at a time.** Read each result before moving on.

---

## 0. One-time setup (skip if already done)

You only do these once. On a redeploy you just reuse the values.

| What                         | Where                                                                               | Value to keep                                         |
|------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------|
| Slack workspace              | slack.com                                                                           | Workspace URL, e.g. `https://YOUR-WS.slack.com`       |
| Alert channel                | Slack                                                                               | `#balerica-alerts`                                    |
| Slack app + Incoming Webhook | api.slack.com/apps → Incoming Webhooks                                              | Webhook URL (**secret**)                              |
| Jira Cloud site              | atlassian.com (Free plan)                                                           | `https://YOUR-SITE.atlassian.net`                     |
| Jira incident project        | Jira → Create space → Kanban                                                        | Name `Balerica AI Incident Management`, key **`BAI`** |
| Atlassian API token          | id.atlassian.com → Security → API tokens → **Create API token** (not "with scopes") | Token (**secret**)                                    |

Keep **secrets** (webhook URL, API token) in a password manager or private note only.

> ⚠️ **Use the incident project (`BAI`) for `jira.py`, not your SEIR-Saga day-planning space.** If `JIRA_PROJECT_KEY` points at the SEIR-Saga space, incident tickets end up in your sprint.

---

## 1. Launch and connect

1. Go to **EC2 → Launch instance** (or launch from your launch template).
   - AMI: Amazon Linux 2023
   - Type: t2.micro or t2.small
   - Region: us-east-1
   - Security group: SSH (22) from **My IP**, and 8000 from My IP if you want the API.
2. Connect with EC2 Instance Connect or SSH.
3. Set the timezone and run the ID line. Run the ID line again before every screenshot.

   ```bash
   #ID
   whoami && TZ='Your/Zone' date && ec2-metadata -i && uptime -s

   #OR
   #You can set your timezone 
   sudo timedatectl set-timezone 'Your/Zone'
   whoami && date && timedatectl show -p Timezone --value && ec2-metadata -i && uptime -s && uptime -p
   ```

4. Write down the **instance ID**.

---

## 2. Install the bank (Lesson 1)

```bash
sudo dnf install -y git sqlite
cd ~
git clone https://github.com/BalericaAI/SEIR-Foundations.git
bash SEIR-Foundations/module1/lesson1_ec2/API/install/install.sh
```

✅ The output should end with `Installation complete.`

Check that it worked:

```bash
cd /opt/balerica-bank
./cobol/bin/account_lookup 100001; echo "rc=$?"
```

✅ You should see `rc=0`.

> If you launched from a golden AMI that already has the bank, skip the installer and just run the check.

---

## 3. Add Slack (Lesson 2)

**1. Copy the files into the bank folder.**

```bash
cd /opt/balerica-bank
cp ~/SEIR-Foundations/module1/lesson2_slack/slack.py .
cp -n ~/SEIR-Foundations/module1/lesson2_slack/slack.env.example .env
chmod 600 .env
```

**2. Set your workspace URL in `slack.py`.** This is the workspace URL, **not** the webhook.

```bash
sed -i 's#https://chewbacca.slack.com#https://YOUR-WS.slack.com#' slack.py
grep -n "SLACK_WORKSPACE_URL =" slack.py
```

**3. Put the webhook in `.env`.**

```bash
nano .env
```

```dotenv
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/PASTE/REAL/WEBHOOK
SLACK_ALERTS_ENABLED=true
SLACK_ALERT_SEVERITY=ERROR
SLACK_ALERT_CHANNEL=balerica-alerts
```

Save and exit: `Ctrl+O`, `Enter`, `Ctrl+X`.

**4. Install the dependencies and test.**

```bash
source venv/bin/activate
python3 -m pip install requests python-dotenv
python3 slack.py --test
```

✅ You should see `SUCCESS: Chewbacca approves!`, and the message should appear in Slack.

🛑 **Don't continue until Slack works on its own.**

---

## 4. Add Jira (Lesson 3)

**1. Copy the files.**

```bash
cd /opt/balerica-bank
cp ~/SEIR-Foundations/module1/lesson3_Jira/jira.py ~/SEIR-Foundations/module1/lesson3_Jira/incident.py .
```

**2. Add the Jira variables to the end of `.env`.** Open it with nano. **Don't delete the Slack lines.**

```bash
nano .env
```

```dotenv
JIRA_SITE_URL=https://YOUR-SITE.atlassian.net
JIRA_EMAIL=you@example.com
JIRA_API_TOKEN=PASTE-TOKEN
JIRA_PROJECT_KEY=BAI
JIRA_ISSUE_TYPE=Task
JIRA_ENABLED=true
INCIDENT_STATE_DB=data/incident_state.db
```

`JIRA_ISSUE_TYPE` must be a work type that exists in that project, such as `Task` or `Bug`.

**3. Check that the variable names are all there.** This prints names only, never values.

```bash
grep -o '^[A-Z_]*=' .env
```

✅ You should see 11 names: 4 `SLACK_`, 6 `JIRA_` and `INCIDENT_STATE_DB`.

**4. Verify Jira access.** This doesn't create a ticket.

```bash
python3 jira.py --verify
```

✅ You should see `Connected to Jira project: BAI (Balerica AI Incident Management)`.

---

## 5. Run the full chain

```bash
mkdir -p data
python3 slack.py --test
python3 jira.py --verify
python3 incident.py --dry-run
python3 incident.py --test      # ONCE: each run creates a new Jira ticket
```

✅ The output should end with:

```json
{ "jira_key": "BAI-…", "jira_created": true, "slack_status": "sent" }
```

**Check both systems yourself.** Terminal output alone isn't proof.

- [ ] In Slack, the alert in `#balerica-alerts` has a clickable `Jira: …/browse/BAI-…` link.
- [ ] Clicking the link opens the matching issue in the **BAI** project.

---

## 6. Duplicate-detection test

```bash
cat > bam_dup.py <<'EOF'
from incident import report_incident
r = report_incident(agent='bam_dup.py', severity='ERROR',
                    message='BAM duplicate-detection test',
                    incident_id='BAM-DUP-XX-001',   # XX = your initials
                    evidence='Synthetic test only',
                    recommendation='Confirm the second run reuses the same Jira key.')
print(r)
EOF
python3 bam_dup.py
python3 bam_dup.py
sqlite3 data/incident_state.db "SELECT incident_id, jira_key, slack_sent FROM incidents;"
```

✅ What you should see:

- Both runs show the **same `jira_key`**.
- Run 1 shows `jira_created: True` and `sent`.
- Run 2 shows `jira_created: False` and `already_sent`.

**Where the ID lives:** in `data/incident_state.db`, table `incidents`, where `incident_id` is the PRIMARY KEY.

> On a **new instance** the database is empty, so the same ID creates a new ticket. To reuse old state, copy `data/incident_state.db` from the old instance before terminating it.

---

## 7. Troubleshooting

| Symptom                              | Fix                                                                     |
|--------------------------------------|-------------------------------------------------------------------------|
| `CHOMP!!!` from slack.py             | `SLACK_WORKSPACE_URL` in `slack.py` is still the placeholder            |
| Slack test fails                     | Wrong or revoked webhook, or `SLACK_ALERTS_ENABLED` isn't `true`        |
| Slack worked, now doesn't            | `.env` was overwritten; check with `grep -o '^[A-Z_]*=' .env`           |
| `slack_status: filtered_or_disabled` | `SLACK_ALERT_SEVERITY=ERROR`, `SLACK_ALERTS_ENABLED=true`               |
| `Jira HTTP 401`                      | Wrong email or token, or you used a token "with scopes"                 |
| `Jira HTTP 403`                      | Your account can't create issues in that project                        |
| `Jira HTTP 404`                      | Wrong `JIRA_SITE_URL` or `JIRA_PROJECT_KEY`                             |
| `Jira HTTP 400`                      | `JIRA_ISSUE_TYPE` doesn't exist in the project                          |
| `ModuleNotFoundError`                | `source venv/bin/activate`, then `pip install requests python-dotenv`   |
| SQLite error                         | Run `mkdir -p data` inside `/opt/balerica-bank`                         |
| Duplicate tickets                    | The incident ID changed, or the DB was deleted                          |
| Jira ticket made, Slack failed       | Fix Slack, then rerun with the **same** incident ID; only Slack retries |

---

## 8. Security rules

- Never put the webhook URL, API token or `.env` contents in screenshots, GitHub, Slack, Jira or AI prompts.
- Keep `.env` at `chmod 600`. Don't commit `.env` or `data/`.
- If a secret leaks, revoke it straight away (Slack app → regenerate webhook; Atlassian → revoke token) and update `.env`.

---

## 9. Teardown

1. Back up anything you need, such as `data/incident_state.db` and your screenshots.
2. Go to **EC2 → Instances → Terminate instance**.
3. Check **EC2 → Volumes** and **Elastic IPs** for anything left behind.
4. Keep your launch template, and your Slack and Jira settings, for the next redeploy.

---

## Quick redeploy (copy-paste summary)

```bash
# 1. ID line
whoami && TZ='Your/Zone' date && ec2-metadata -i && uptime -s

# 2. Bank
sudo dnf install -y git sqlite && cd ~
git clone https://github.com/BalericaAI/SEIR-Foundations.git
bash SEIR-Foundations/module1/lesson1_ec2/API/install/install.sh

# 3–4. Integrations
cd /opt/balerica-bank
cp ~/SEIR-Foundations/module1/lesson2_slack/slack.py .
cp ~/SEIR-Foundations/module1/lesson3_Jira/{jira.py,incident.py} .
sed -i 's#https://chewbacca.slack.com#https://YOUR-WS.slack.com#' slack.py
touch .env && chmod 600 .env && nano .env      # paste SLACK_ + JIRA_ variables
source venv/bin/activate
python3 -m pip install requests python-dotenv

# 5. Verify
mkdir -p data
python3 slack.py --test && python3 jira.py --verify && python3 incident.py --dry-run
python3 incident.py --test
```
