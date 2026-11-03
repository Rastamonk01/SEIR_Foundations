# Balerica Legacy Bank on EC2: Modern API, Legacy Core

## Launch → Install → Run COBOL → Serve FastAPI → Repeat ×7

![AWS EC2](https://img.shields.io/badge/AWS-EC2_us--east--1-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Amazon Linux](https://img.shields.io/badge/Amazon_Linux-2023-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![GnuCOBOL](https://img.shields.io/badge/Core-GnuCOBOL-003B57?style=for-the-badge&logo=gnu&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-venv_+_uvicorn-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/Ledger-SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/Git-First_Clone-F05032?style=for-the-badge&logo=git&logoColor=white)

![Runs](https://img.shields.io/badge/Lab_Runs-7_of_7-yellow?style=for-the-badge)
![Return Codes](https://img.shields.io/badge/Return_Codes-0_|_4_|_8_|_12-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

Applied Cloud & Platform Engineering. Lab results: seven hand-built EC2 instances, each running a FastAPI front office over a GnuCOBOL back office.

> **Goal:** Build the bank from scratch on a brand-new instance seven times until the steps are muscle memory. Prove that the COBOL core reports its own result through return codes, and decode a fixed-width ledger by hand.

---

## File Structure

```text
SEIR_Foundations/
├── AWS/
    └── 01module/
        └── lesson1_ec2/
            ├── lab_runs/
            │   ├── BAM_2/
            │   └── screenshots/
            ├── scripts/                    ← User Data startup scripts
            │   ├── BAM_2.2.sh
            │   └── seir_ec2_userdata.sh
            ├── udemy/
            ├── ai_enabled_study_lab1.0.txt 
            ├── ai_review_transcript_Koffi.txt
            ├── lab1_notes.md
            ├── README.md
            └── spotter_Koffi.txt
```

---

### Lesson 1 - Run Log & Evidence

**Person:** KA (Koffi A)
**Week:** 3
**Time zone:** Australia/Adelaide (ACDT, UTC+10:30)
**Region:** us-east-1 (N. Virginia)

Each run is a brand-new EC2 instance where I completed runbook Steps 0–4 by hand: clone the repo, run the installer, run the COBOL core, and start the FastAPI layer with uvicorn.

Every screenshot shows the ID line:

```bash
whoami && TZ='Australia/Adelaide' date && ec2-metadata -i && uptime -s
```

```bash
## Swapped ID
> sudo timedatectl set-timezone Australia/Adelaide
##### set the timezone
> whoami && date && timedatectl show -p Timezone --value && ec2-metadata -i && uptime -s && uptime -p
##### gets all ID and server running period/time
```

---

## Lab runs

| Run | Date       | Time zone          | Instance ID         | Boot time (UTC)                                         | Public IPv4 DNS                                | Screenshot                                                           | Terminated? |
|-----|------------|--------------------|---------------------|---------------------------------------------------------|------------------------------------------------|----------------------------------------------------------------------|-------------|
| 1   | 2026-10-31 | Australia/Adelaide | i-04a3f004ec972e0d3 | swapped `uptime -s` with `uptime -p`                    | ec2-98-89-23-249.compute-1.amazonaws.com       | [lab1_run1.jpg](/AWS/01module/lesson1_ec2/screenshots/lab1_run1.jpg) | Yes         |
| 2   | 2026-10-31 | Australia/Adelaide | i-064f0e898402def08 | 2026-10-31 01:35:48 (shown as 12:05:48 ACDT)            | ec2-13-218-110-252.compute-1.amazonaws.com     | [lab1_run2.jpg](/AWS/01module/lesson1_ec2/screenshots/lab1_run2.jpg) | Yes         |
| 3   | 2026-10-31 | Australia/Adelaide | i-083ad8a12ddd32738 | 2026-10-31 02:03:47 (shown as 12:33:47 ACDT)            | ec2-3-95-62-149.compute-1.amazonaws.com        | [lab1_run3.jpg](/AWS/01module/lesson1_ec2/screenshots/lab1_run3.jpg) | Yes         |
| 4   | 2026-11-01 | Australia/Adelaide | i-0754f23fd7f36b03d | 2026-11-01 01:11:22 (shown as 11:41:22 ACDT)            | ec2-52-91-51-168.compute-1.amazonaws.com       | [lab1_run4.jpg](/AWS/01module/lesson1_ec2/screenshots/lab1_run4.jpg) | Yes         |
| 5   | 2026-11-01 | Australia/Adelaide | i-0d670053a1967c65c | 2026-11-01 01:28:32 (shown as 11:58:32 ACDT)            | ec2-54-146-212-178.compute-1.amazonaws.com     | [lab1_run5.jpg](/AWS/01module/lesson1_ec2/screenshots/lab1_run5.jpg) | Yes         |
| 6   | 2026-11-01 | Australia/Adelaide | i-0374393f4a4010f6f | 2026-11-01 01:45:11 (shown as 12:15:11 ACDT)            | ec2-18-206-236-27.compute-1.amazonaws.com      | [lab1_run6.jpg](/AWS/01module/lesson1_ec2/screenshots/lab1_run6.jpg) | Yes         |
| 7   | 2026-11-03 | Australia/Adelaide | i-0f322fe776c92d324 | 2026-11-02 21:45:49 (shown as 2026-11-03 08:15:49 ACDT) | ec2-54-226-96-241.compute-1.amazonaws.com      | [lab1_run7.jpg](/AWS/01module/lesson1_ec2/screenshots/lab1_run7.jpg) | Yes         |

> **Note on boot time:** on Runs 2–6 I ran `sudo timedatectl set-timezone Australia/Adelaide` before the ID line, so `uptime -s` printed the boot time in ACDT. To get UTC, I subtracted 10 hours 30 minutes. The value printed in each screenshot is shown in brackets.

After each run I terminated the instance and checked EC2 → Volumes and Elastic IPs for leftovers. I kept my launch template.

### Lab-run screenshots

📸 **Screenshot [`Run 1 Console`](lab_runs/screenshots/id_lesson1_ec2_template_01.png) :** Run 1: the ID line for `i-04a3f004ec972e0d3`, then uvicorn reporting **Application startup complete.** on port 8000.

📸 **Screenshot [`Run 2 Console`](lab_runs/screenshots/id_lesson1_ec2_template_02.png) :** Run 2: the ID line for `i-064f0e898402def08` (boot `12:05:48` ACDT), then **Application startup complete.**, and browser requests to `/`, `/docs` and `/openapi.json` returning **200 OK**.

📸 **Screenshot [`Run 3 Console`](lab_runs/screenshots/id_lesson1_ec2_template_03.png) :** Run 3: the ID line for `i-083ad8a12ddd32738` (boot `12:33:47` ACDT), then **Application startup complete.** (server process `36061`).

📸 **Screenshot [`Run 4 Console`](lab_runs/screenshots/id_lesson1_ec2_template_04.png) :** Run 4: the ID line for `i-0754f23fd7f36b03d` (boot `11:41:22` ACDT), then **Application startup complete.** (server process `36278`).

📸 **Screenshot [`Run 5 Console`](lab_runs/screenshots/id_lesson1_ec2_template_05.png) :** Run 5: the ID line for `i-0d670053a1967c65c` (boot `11:58:32` ACDT), then **Application startup complete.** (server process `35859`).

📸 **Screenshot [`Run 6 Console`](lab_runs/screenshots/id_lesson1_ec2_template_06.png) :** Run 6: the ID line for `i-0374393f4a4010f6f` (boot `12:15:11` ACDT), then **Application startup complete.** (server process `36808`).

📸 **Screenshot [`Run 7 Console`](lab_runs/screenshots/id_lesson1_ec2_template_07.png) :** Run 7: the ID line for `i-0f322fe776c92d324` (boot `08:15:49` ACDT), then **Application startup complete.** (server process `37421`), and browser requests to `/`, `/docs` and `/openapi.json` returning **200 OK**.

---

## COBOL core practice

Done on Run 1 (`i-04a3f004ec972e0d3`) in `/opt/balerica-bank`. My TXN IDs start with `TXN-KA-`. Full commands and outputs are in [lab1_notes.md](lab1_notes.md#cobol-practice).

| Return code | Meaning             | How I triggered it                                                            |
|-------------|---------------------|-------------------------------------------------------------------------------|
| 0           | success             | `payment_post TXN-KA-0001 100001 10.00 USD HW-RC0` → POSTED                   |
| 4           | account not found   | `account_lookup 999999`                                                       |
| 8           | business rejection  | `payment_post TXN-KA-0002 100001 0.00 ...` → AMOUNT MUST BE GREATER THAN ZERO |
| 12          | environment failure | ran `account_lookup` from `~` → CANNOT OPEN data/accounts.dat, FILE-STATUS=35 |

📸 **Screenshot [`cobol_rc0.jpg`](lab_runs/screenshots/cobol_rc0.png) :** the ID line, then `payment_post TXN-KA-0001 ... 10.00 USD` returning **STATUS=POSTED**, and `echo $?` printing **0**.

📸 **Screenshot [`cobol_rc4.jpg`](lab_runs/screenshots/cobol_rc4.png) :** the ID line, then `account_lookup 999999` returning **ERROR=ACCOUNT NOT FOUND**, and `echo $?` printing **4**.

📸 **Screenshot [`cobol_rc8.jpg`](lab_runs/screenshots/cobol_rc8.png) :** the ID line, then a zero-amount `payment_post TXN-KA-0002` returning **STATUS=REJECTED / AMOUNT MUST BE GREATER THAN ZERO**, and `echo $?` printing **8**.

📸 **Screenshot [`cobol_rc12.jpg`](lab_runs/screenshots/cobol_rc12.png) :** the ID line, then `account_lookup` run from the home folder returning **ERROR=CANNOT OPEN data/accounts.dat / FILE-STATUS=35**, and `echo $?` printing **12**.

📸 **Screenshot [`cobol_ledger_decode.jpg`](lab_runs/screenshots/cobol_ledger_decode.png) :** the ID line, then `cut -c` slicing `data/accounts.dat` into id / name / status / balance / currency. Alice's raw balance `000000500000` decodes to **5000.00**.

---

## Git

I cloned my HW repo onto an EC2 instance and listed its module1 folder. I only cloned: I didn't push from EC2, and no token was put on the server.

📸 **Screenshot [`git_clone.jpg`](lab_runs/screenshots/git_clone.png) :** the ID line for `i-0495ce968de35c32b` (boot `2026-11-03 08:49:14` ACDT), then `git clone https://github.com/Rastamonk01/SEIR_Foundations.git` into the home folder, and `ls` of `SEIR_Foundations/AWS/01module` showing `00.5lab  00lab  lesson1_ec2  week1_tasks`.

> In my repo, **`AWS/01module`** is my Module 1 folder (the assignment's "module1"). The repo is public, so the clone needed no credentials, and no token was put on the server.

---

## Udemy — Maarek

📸 **Screenshot [`Maarek quiz section 21`](udemy/01_maarek_quiz_section_21.png) :** the completed Section 21 quiz result.

📸 **Screenshot [`Maarek quiz section 23`](udemy/02_maarek_quiz_section_23.png) :** the completed Section 23 quiz result.

📸 **Screenshot [`Maarek quiz section 25`](udemy/03_maarek_quiz_section_25.png) :** the completed Section 25 quiz result.

---

## "Be A Man" extra credit

Details, IDs and full outputs are in the BAM section of [lab1_notes.md](lab1_notes.md#bam-extra-credit).

📸 **Screenshot [`BAM_2.1 SSH`](lab_runs/BAM_2/BAM_2.1_5.png) :** the ID line for `i-09a4d6d2097ec92ed`, then `POST /ask` about my own `TXN-KA-0101` answered with **`"source": "amazon-bedrock"`**, using IAM role `BalericaLegacyBankEC2Role` and inference profile `us.anthropic.claude-haiku-4-5-20251001-v1:0`, with no access keys on the instance.

📸 **Screenshot [`BAM_2.2 Connect`](lab_runs/BAM_2/BAM_2.2_instance_connect_id.png) :** the ID line for `i-05e8c105391b3ecec`, launched from baked template `lt-070a12156a2d7831e` (v1), then `cloud-init status: done`, **`1030:Installation complete.`** found in `/var/log/cloud-init-output.log`, and `account_lookup 100001` returning **0** with no manual install.

📸 **Screenshot [`BAM_2.3 Connect`](lab_runs/BAM_2/BAM_2.3_ami_instance_connect_id_metadata.png) :** the ID line for `i-0fa6fc630cd34f507`, launched from golden AMI `ami-0d4ff01d90546aa7d`, then uvicorn reporting **Application startup complete.** without running the installer.

---

## Files in this folder

| File                          | What it is                                                             |
|-------------------------------|------------------------------------------------------------------------|
| `README.md`                   | this file                                                              |
| `lab1_notes.md`               | per-run notes, COBOL practice, mistakes, commands I know by heart, BAM |
| `screenshots/`                | all `.png` evidence linked above                                       |
| `ai_review_KA.txt`            | AI review of the runbook (TODO: rename with full name)                 |
| `ai_review_transcript_KA.txt` | conversation summary + share link                                      |
| `spotter_KA.txt`              | spotter cross-check                                                    |
| `AI_enabled_study_lab1.0.txt` | research: databases, COBOL, SWIFT/ISO 20022, APIs, intersection        |

---

## Architecture (what each run builds)

```text
Browser / curl / SWIFT generator
        |  HTTP :8000
     FastAPI (app/main.py)
        |  subprocess
   cobol_bridge.py
        |  argv + KEY=VALUE stdout + return code
 account_lookup / payment_post  (GnuCOBOL)
        |  fixed-width records
 accounts.dat / payments.dat  <->  SQLite (bank.db, system of record)

POST /ask -> agents/balerica.py -> Amazon Bedrock (IAM role, us. inference profile)
```
