# A Day in My Shoes: Jira Scrum Space

## Epic → Stories → Tasks → Story Points

![Jira](https://img.shields.io/badge/Jira-Cloud_Free-0052CC?style=for-the-badge&logo=jira&logoColor=white)
![Scrum](https://img.shields.io/badge/Template-Scrum_(team--managed)-6554C0?style=for-the-badge)
![Agile](https://img.shields.io/badge/Reading-Head_First_Agile_Ch._1–3-36B37E?style=for-the-badge)

![Items](https://img.shields.io/badge/Work_Items-1_Epic_|_6_Stories_|_24_Tasks-yellow?style=for-the-badge)
![Points](https://img.shields.io/badge/Story_Points-69-blueviolet?style=for-the-badge)
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
            │   ├── jira_estimation_on.jpg
            │   ├── jira_epic.jpg
            │   ├── jira_story.jpg
            │   ├── jira_task.jpg
            │   └── jira_backlog.jpg
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

## What I learned

- An **epic** is the big goal, **stories** are the blocks of value under it, and **tasks** are the individual steps.
- Story points measure **relative** size, effort and uncertainty, not hours. What matters most is using the scale consistently.
- Even an ordinary day contains a lot of small, unseen work. Writing it all down shows why mundane tasks need to be tracked too.
