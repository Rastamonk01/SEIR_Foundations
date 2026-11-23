# Runbook: Lesson 2 Homework, Seven Alerts, Seven Wins

This runbook runs the seven Slack homework scripts and the three experiments on an EC2 instance where `slack.py` already works.

**Time needed:** about 30 minutes.
**Run commands one at a time.** Read each result before moving on.

---

## 0. Before you start

- [ ] `/opt/balerica-bank` exists with `slack.py`, `.env` and `venv/` (Lesson 1 install + Lesson 2 lab)
- [ ] `SLACK_WORKSPACE_URL` in `slack.py` is your real workspace, not `chewbacca.slack.com`
- [ ] `.env` has a working `SLACK_WEBHOOK_URL`

If any of these are missing, follow the main redeploy runbook (bank → Slack) first.

---

## 1. Connect, ID line, Slack check

```bash
sudo timedatectl set-timezone Your/Zone
cd /opt/balerica-bank
source venv/bin/activate                 # every new SSH session
whoami && TZ='Your/Zone' date && ec2-metadata -i
python3 slack.py --test
```

✅ You should see `SUCCESS: Chewbacca approves!`, and the message in your alerts channel. 📸 Take a screenshot.

---

## 2. One-time setup

```bash
cd ~ && (git -C SEIR-Foundations pull || git clone https://github.com/BalericaAI/SEIR-Foundations.git)
cp ~/SEIR-Foundations/module1/lesson2_slack/homework/hw*.py /opt/balerica-bank/
cd /opt/balerica-bank
ls hw*.py
```

✅ You should see seven files, `hw1_…` to `hw7_…`.

Lower the threshold so INFO alerts get through:

```bash
sed -i 's/^SLACK_ALERT_SEVERITY=.*/SLACK_ALERT_SEVERITY=INFO/' .env
grep -E '^SLACK_ALERT(S_ENABLED|_SEVERITY)=' .env
```

✅ You should see `SLACK_ALERTS_ENABLED=true` and `SLACK_ALERT_SEVERITY=INFO`. Never print the webhook line. 📸 Take a screenshot.

---

## 3. Run the seven scripts

Read each one first with `cat hwN_*.py`. For each script, take two screenshots: the terminal and the Slack alert.

| Step | Command                                                                      | Expected                                                                 |
|------|------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| hw1  | `nano hw1_hello_slack.py` → set `MY_NAME`, then `python3 hw1_hello_slack.py` | `Delivered!`; "Hello from `<name>`!" in Slack                            |
| hw2  | `python3 hw2_severity_tour.py`                                               | All 4 severities `DELIVERED to Slack`                                    |
| hw3  | `python3 hw3_server_time.py` then `date`                                     | Server time in **UTC**; compare with local `date`                        |
| hw4  | `python3 hw4_disk_watch.py`                                                  | `Disk is NN.N% used -> severity INFO` (under 75%). **Write down the %.** |
| hw5  | `python3 hw5_load_check.py`                                                  | `Load: x / x / x on 1 CPU(s) -> INFO`                                    |
| hw6  | `python3 hw6_incident_drill.py` (run 2–3 times)                              | Random `DRILL-####` incidents. Note which you got.                       |
| hw7  | see below                                                                    | Multi-line MORNING REPORT, `Delivered!`                                  |

For hw7, include the ID line in the same screenshot:

```bash
clear
whoami && TZ='Your/Zone' date && ec2-metadata -i
python3 hw7_morning_report.py
```

📸 **Required:** this terminal screenshot.

📸 **Required:** one screenshot of the alerts channel showing **at least 5 different hw alerts** (hw1 to hw7). Scroll or zoom out so they fit, and blur anything sensitive.

---

## 4. Experiments

### Experiment 1: CRITICAL only

**Write your prediction in your notes before you run it.**

```bash
sed -i 's/^SLACK_ALERT_SEVERITY=.*/SLACK_ALERT_SEVERITY=CRITICAL/' .env
python3 hw2_severity_tour.py
```

✅ You should see INFO, WARNING and ERROR `skipped by your threshold`, and `CRITICAL -> DELIVERED to Slack`.

### Experiment 2: the kill switch

```bash
sed -i 's/^SLACK_ALERT_SEVERITY=.*/SLACK_ALERT_SEVERITY=INFO/' .env
sed -i 's/^SLACK_ALERTS_ENABLED=.*/SLACK_ALERTS_ENABLED=false/' .env
python3 hw1_hello_slack.py
```

✅ You should see `Skipped. Check .env: SLACK_ALERTS_ENABLED must be true…`, and nothing new in Slack.

### Experiment 3: the disk threshold

Choose a number **below** your hw4 disk %. For example, use 20 if you're at about 26%.

```bash
sed -i 's/^SLACK_ALERTS_ENABLED=.*/SLACK_ALERTS_ENABLED=true/' .env
cp hw4_disk_watch.py hw4_disk_watch.py.bak
sed -i 's/percent_used >= 75/percent_used >= 20/' hw4_disk_watch.py
grep -n "percent_used >=" hw4_disk_watch.py
python3 hw4_disk_watch.py
```

✅ The same disk % should now show `-> severity WARNING`.

### Put everything back

```bash
mv hw4_disk_watch.py.bak hw4_disk_watch.py
sed -i 's/^SLACK_ALERT_SEVERITY=.*/SLACK_ALERT_SEVERITY=INFO/' .env
sed -i 's/^SLACK_ALERTS_ENABLED=.*/SLACK_ALERTS_ENABLED=true/' .env
grep -E '^SLACK_ALERT(S_ENABLED|_SEVERITY)=' .env
grep -n "percent_used >=" hw4_disk_watch.py      # should show 90 and 75 again
```

📸 Take a screenshot.

> For normal class work, and the Jira and GTA drills, you can set `SLACK_ALERT_SEVERITY=ERROR` again afterwards, so only ERROR and CRITICAL page Slack.

---

## 5. Notes and submission

In `lesson2_notes.md`, record:

- [ ] Experiment 1: your prediction vs the actual result
- [ ] hw2: which severities arrived, and why
- [ ] hw3: hours between server time (UTC) and your clock (Adelaide: **10.5 h**)
- [ ] hw4: why a quiet INFO is good design
- [ ] hw5: what would make the load spike on the Balerica bank
- [ ] hw6: which fake incident deserves a 3 AM page
- [ ] Experiments 2 and 3: what happened and why

Then push to your repo:

```bash
git add AWS/01module/lesson2_slack
git commit -m "Lesson 2 homework: seven alerts, seven wins"
git push
```

Send Theo the link.

---

## Troubleshooting

| Symptom                                | Fix                                                                             |
|----------------------------------------|---------------------------------------------------------------------------------|
| `CHOMP! Edit MY_NAME…`                 | Edit `MY_NAME` in `hw1_hello_slack.py`                                          |
| `ModuleNotFoundError: slack`           | The script isn't next to `slack.py`. Run from `/opt/balerica-bank`.             |
| `ModuleNotFoundError: dotenv/requests` | `source venv/bin/activate`                                                      |
| Script prints `Skipped`                | Check `SLACK_ALERTS_ENABLED=true` and that `SLACK_ALERT_SEVERITY` is low enough |
| `ValueError: Fix SLACK_WORKSPACE_URL`  | Set your real workspace URL in `slack.py`                                       |
| Nothing in Slack but `Delivered!`      | You're looking at the wrong channel; check which channel the webhook posts to   |
| Wrong `.env` value after experiments   | Run the "Put everything back" commands                                          |

---

## Rules

- Synthetic messages only: no passwords, keys, customer data or `.env` contents.
- No spam: no loops, and run each script only a few times.
- Keep `send_alert(agent, severity, message, incident_id)` calls exactly as written.
- Never screenshot or print `SLACK_WEBHOOK_URL`.
