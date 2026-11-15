# A Day in My Shoes: Jira Scrum Space

## Epic → Stories → Tasks → Story Points

![Jira](https://img.shields.io/badge/Jira-Cloud_Free-0052CC?style=for-the-badge&logo=jira&logoColor=white)
![Scrum](https://img.shields.io/badge/Template-Scrum_(team--managed)-6554C0?style=for-the-badge)
![Agile](https://img.shields.io/badge/Reading-Head_First_Agile_Ch._1–3-36B37E?style=for-the-badge)

![Items](https://img.shields.io/badge/Work_Items-1_Epic_|_6_Stories_|_24_Tasks-yellow?style=for-the-badge)
![Points](https://img.shields.io/badge/Story_Points-69-blueviolet?style=for-the-badge)
![BAM](https://img.shields.io/badge/BAM-5.1–5.7_done-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

Applied Cloud & Platform Engineering, Lesson 3: I broke one ordinary day into a Jira epic, stories and tasks, and estimated each one in story points.

> **Goal:** Learn how Agile work is structured by modelling a real day from alarm to sleep, mundane tasks included, as an epic with stories and tasks.

---

## File Structure

```text
SEIR_Foundations/
├── AWS/
    └── 01module/
        └── lesson3_jira/
            ├── screenshots/
            │   ├── jira_estimation_on.png
            │   ├── jira_epic.png
            │   ├── jira_story.png
            │   ├── jira_task.png
            │   ├── jira_backlog.png
            │   └── BAM_5/                 
            │       ├── slack_test_id.png
            │       ├── BAM_5.1.png
            │       ├── BAM_5.2.png
            │       ├── BAM_5.3.png
            │       ├── BAM_5.4.png
            │       ├── BAM_5.5.png
            │       ├── BAM_5.5_troubleshooting.png
            │       ├── BAM_5.6.png
            │       ├── BAM_5.6_slack.png
            │       ├── BAM_5.6_jira.png
            │       └── BAM_5.7.png         ← one-day sprint burndown
            ├── bam_dup.py
            ├── lesson3_notes.md
            └── README.md
```

---

## Space

**Person:** KA (Koffi A)
**Week:** 5
**Time zone:** Australia/Adelaide (ACDT, UTC+10:30)

| Field       | Value                                             |
|-------------|---------------------------------------------------|
| Space name  | `SEIR-Saga_KA`                                    |
| Space key   | `SEIR`                                            |
| Template    | Scrum, team-managed                               |
| Estimation  | ON, Story points                                  |
| Point scale | 1 trivial · 2 small · 3 moderate · 5 big · 8 huge |

Every story and task has the epic **SEIR-31** as its Parent, a Story point estimate, and a description of at least two sentences (when, where, how long, with whom, and what "done" looks like). The epic is the overall goal, so it has no points.

---

## Evidence table

### Epic and stories

| Key     | Type  | Summary              | Story Points |
|---------|-------|----------------------|--------------|
| SEIR-31 | Epic  | A day in my shoes    | -            |
| SEIR-1  | Story | Morning routine      | 5            |
| SEIR-2  | Story | Breakfast            | 3            |
| SEIR-3  | Story | Commute / Errands    | 3            |
| SEIR-4  | Story | Work / Study         | 8            |
| SEIR-5  | Story | Evening              | 5            |
| SEIR-6  | Story | Bedtime              | 2            |
|         |       | **Stories subtotal** | **26**       |

### Tasks

| Key     | Type | Summary                            | Story Points |
|---------|------|------------------------------------|--------------|
| SEIR-37 | Task | [Morning] Alarm & get up           | 1            |
| SEIR-38 | Task | [Morning] Bathroom/shower          | 2            |
| SEIR-39 | Task | [Morning] Brush teeth              | 1            |
| SEIR-40 | Task | [Morning] Get dressed              | 1            |
| SEIR-41 | Task | [Morning] Check phone              | 1            |
| SEIR-42 | Task | [Breakfast] Make coffee            | 1            |
| SEIR-43 | Task | [Breakfast] Cook breakfast         | 2            |
| SEIR-44 | Task | [Breakfast] Wash dishes            | 1            |
| SEIR-45 | Task | [Commute] Drive to work            | 3            |
| SEIR-46 | Task | [Commute] Wait in traffic/line     | 1            |
| SEIR-47 | Task | [Commute] Drive home               | 3            |
| SEIR-48 | Task | [Work] Check email                 | 2            |
| SEIR-49 | Task | [Work] Standup/meetings            | 3            |
| SEIR-50 | Task | [Work] Deep work block             | 5            |
| SEIR-51 | Task | [Work] Lunch - healthy             | 2            |
| SEIR-52 | Task | [Work] Bathroom break              | 1            |
| SEIR-53 | Task | [Evening] Groceries                | 2            |
| SEIR-54 | Task | [Evening] Cook dinner              | 3            |
| SEIR-55 | Task | [Evening] Eat dinner               | 2            |
| SEIR-56 | Task | [Evening] Talk with family/friends | 2            |
| SEIR-57 | Task | [Bedtime] Prep tomorrow's clothes  | 1            |
| SEIR-58 | Task | [Bedtime] Brush teeth              | 1            |
| SEIR-59 | Task | [Bedtime] Scroll phone/read        | 1            |
| SEIR-60 | Task | [Bedtime] Sleep                    | 1            |
|         |      | **Tasks subtotal**                 | **43**       |

### Total

|           | Items  | Story Points |
|-----------|--------|--------------|
| Epic      | 1      | -            |
| Stories   | 6      | 26           |
| Tasks     | 24     | 43           |
| **Total** | **31** | **69**       |

These totals match the backlog view: the sprint header shows **26** points (stories) and the backlog header shows **43** points (tasks).

---

## Biggest task

**SEIR-50 [Work] Deep work block (5 points)** is my biggest task. It's the longest stretch of my day, about five hours of focused work or SEIR coursework. It also takes the most mental effort and has the most uncertainty, since interruptions or a hard problem can stop it finishing on time. Size, effort and risk together make it worth more than a routine task like driving to work (3).

---

## Screenshots

📸 **Screenshot [`jira_estimation_on.jpg`](screenshots/jira_estimation_on.png):** `SEIR-Saga_KA` Space settings → Features, with **Estimation ON** and **Story points** selected.

📸 **Screenshot [`jira_epic.jpg`](screenshots/jira_epic.png):** epic **SEIR-31 A day in my shoes** opened, with its child stories and tasks listed and the **Story point estimate** column showing each child's points. The epic itself has no story points.

📸 **Screenshot [`jira_story.jpg`](screenshots/jira_story.png):** story **SEIR-1 Morning routine** opened, showing Parent **SEIR-31**, its description, and **Story point estimate 5**.

📸 **Screenshot [`jira_task.jpg`](screenshots/jira_task.png):** task **SEIR-37 [Morning] Alarm & get up** opened, showing Parent **SEIR-31**, its description, and **Story point estimate 1**.

📸 **Screenshot [`jira_backlog.jpg`](screenshots/jira_backlog.png):** backlog showing all 6 stories in **SEIR Sprint 1** (26 points) and all 24 tasks in the backlog (43 points), each with its points and epic.

---

## "Be A Man" Challenge

Details, IDs, commands, outputs and written answers are in the BAM section of [lesson3_notes.md](lesson3_notes.md#bam-challenge).

All terminal work was done on **`i-0f6250818d1a31d40`** (t2.small, us-east-1d, boot `2026-11-14 13:12:12` ACDT) in `/opt/balerica-bank`, with `jira.py` and `incident.py` copied next to `slack.py`. Every terminal screenshot starts with my ID line. Browser and Slack screenshots show the Windows clock with the date.

📸 **Screenshot [`slack_testid`](screenshots/BAM_5/slack_test_id.png):** the ID line for `i-0f6250818d1a31d40` (13:18:25 ACDT), then `python3 slack.py --test` returning **SUCCESS: Chewbacca approves!**. Slack was working on its own before I added Jira.

📸 **Screenshot [`BAM_5.1`](screenshots/BAM_5/BAM_5.1.png):** my private config note (email blurred) next to the manual test incident **SEIR-61 "TEST - EC2 application error"** opened in Jira.

📸 **Screenshot [`BAM_5.2`](screenshots/BAM_5/BAM_5.2.png):** the ID line (13:44:18 ACDT), then `python3 jira.py --verify` returning **Connected to Jira project: SEIR (SEIR-Saga_KA)**.

📸 **Screenshot [`BAM_5.3`](screenshots/BAM_5/BAM_5.3.png):** the ID line (13:46:06 ACDT), then `slack.py --test` → `jira.py --verify` → `incident.py --dry-run` → `incident.py --test`, which returned **`"jira_key": "SEIR-62"`**, **`"jira_created": true`** and **`"slack_status": "sent"`**.

📸 **Screenshot [`BAM_5.4`](screenshots/BAM_5/BAM_5.4.png):** the Slack alert in **#balerica-alerts-01** for incident `SEIR-TEST-20261114T031607764025`, with the clickable link **`…/browse/SEIR-62`** (clock 1:56 PM, 14/11/2026).

📸 **Screenshot [`BAM_5.5`](screenshots/BAM_5/BAM_5.5.png):** Jira issue **SEIR-62** opened, with the title **`[Balerica AI][ERROR] incident.py: SEIR Foundations integration test: simulated application failure`**, shown in the **SEIR-Saga_KA** space (clock 1:58 PM, 14/11/2026).

📸 **Screenshot [`BAM_5.5_troubleshooting`](screenshots/BAM_5/BAM_5.5_troubleshooting.png):** `chmod 600 .env` then `grep -o '^[A-Z_]*=' .env`, listing all the `SLACK_` and `JIRA_` variable **names** without their values.

📸 **Screenshot [`BAM_5.6`](screenshots/BAM_5/BAM_5.6.png):** the ID line (14:13:10 ACDT), then [`bam_dup.py`](bam_dup.py) run twice with incident ID **`BAM-DUP-KA-001`**. Both runs returned **SEIR-63**: the first with `jira_created: True` / `sent`, the second with `jira_created: False` / `already_sent`. The SQLite query shows the stored row `BAM-DUP-KA-001|SEIR-63|1`.

📸 **Screenshot [`BAM_5.6_slack`](screenshots/BAM_5/BAM_5.6_slack.png):** the single Slack alert for `BAM-DUP-KA-001` linking to **SEIR-63**. The second run didn't send a second alert.

📸 **Screenshot [`BAM_5.6_jira`](screenshots/BAM_5/BAM_5.6_jira.png):** the one Jira issue **SEIR-63** created for `BAM-DUP-KA-001`.

📸 **Screenshot [`BAM_5.7`](screenshots/BAM_5/BAM_5.7.png):** Sprint burndown chart and report for **SEIR Sprint 1** (15 Nov 2026, Story points). **69** points were committed and all 30 day items show as Done. **46** points burned down during the day, and the last **23** (drive home, evening, bedtime) were closed when I completed the sprint at about 4:00 PM. There were no scope changes. The three 0-point incident Bugs (SEIR-61/62/63) were left incomplete. Full breakdown in [lesson3_notes.md](lesson3_notes.md#bam_57-one-day-sprint-in-seir-saga_ka).

---

## What I learned

- An **epic** is the big goal, **stories** are the blocks of value under it, and **tasks** are the individual steps.
- Story points measure **relative** size, effort and uncertainty, not hours. What matters most is using the scale consistently.
- Even an ordinary day contains a lot of small, unseen work. Writing it all down shows why mundane tasks need to be tracked too.
