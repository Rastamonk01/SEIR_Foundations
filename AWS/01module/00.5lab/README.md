# SEIR Foundations - Module 1, Lab 0.5

## EC2 Hardening & Custom Website: My IP SSH, Dashboard, User Data Web App

![AWS](https://img.shields.io/badge/AWS-EC2-orange?style=for-the-badge&logo=amazonaws&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-Bash_Script-green?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Python](https://img.shields.io/badge/Python-3_stdlib-blue?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Amazon_Linux_2023-yellow?style=for-the-badge&logo=linux&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-Git_Bash-blue?style=for-the-badge&logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

Systems Engineering and Infrastructure Integration

Applied Cloud & Platform Engineering - Lab Results: My IP SSH, SEIR Dashboard & Custom Website

---
This lab picked up the **Next Challenge** from Lab 0 and used the **AWS Management Console** to:

1. Restrict **SSH (port 22)** in the security group from `0.0.0.0/0` to **My IP** only.
2. Launch **`00.5lab_MyIP_EC2_01`** with the SEIR dashboard User Data and connect over **SSH** from Git Bash.
3. Show the **SEIR dashboard** and run basic identity checks (`pwd`, `whoami`, `date`).
4. Launch **`00.5lab_MyIP_EC2_02`** with a **custom website** User Data script (`website_userdata_v3.sh`).
5. Browse the **live website** over HTTP and confirm the server details on the **Server Info** page.
6. Capture **screenshots** as evidence.
7. **Terminate** both instances.
8. Complete the **EC2 knowledge checks**.

---

## File Structure

```text
SEIR_Foundations/
└── AWS/
    └── 01module/
        └── 00.5lab/
            ├── screenshots/
            │   ├── BAM_1.1/
            │   ├── BAM_1.2/
            │   └── BAM_1.3/
            ├── script/                    ← User Data startup scripts
            │   ├── seir_ec2_userdata.sh
            │   └── website_userdata_v3.sh
            ├── udemy/
            ├── group_TODS.txt
            └── README.md
```

---

## Naming Conventions Used

| Resource           | Name                                                |
|--------------------|-----------------------------------------------------|
| Region             | `us-west-2` (Oregon)                                |
| Key pair           | `Wakanda_EC2_Instance` (`Wakanda_EC2_Instance.pem`) |
| Instance 1         | `00.5lab_MyIP_EC2_01` (SEIR dashboard)              |
| Instance 2         | `00.5lab_MyIP_EC2_02` (custom website)              |
| Website service    | `seir_foundations` (systemd)                        |
| Screenshots folder | `screenshots/`                                      |
| Script folder      | `script/`                                           |

## Team

| Field          | Detail                        |
|----------------|-------------------------------|
| Group          | Troll Ops                     |
| Spotter        | Tim's Group                   |
| Teammates      | Tim, Carlos, Emonie, Marvin   |
| Meeting times  | Mon, Wed & Fri, 8:00 PM EST   |

## Environment

- **Region:** `us-west-2`, Availability Zone `us-west-2a` for both instances.
- **AMI:** Amazon Linux 2023.
- **Instance type:** `t3.micro` (2 vCPU, 913 MiB memory as reported by `free -h`).
- **Root volume:** 8 GiB.
- **Local SSH client:** Git Bash (MSYS2 UCRT64) on Windows, run from `~/.../Wakanda_EC2_Key_pair` *(location you have saved the key pair file)*

---

## Task 1 : Restrict SSH to My IP

1. In **EC2 → Security Groups**, edited the inbound rules used by this lab's instances.
2. Changed the **SSH** rule source from **Anywhere-IPv4** (`0.0.0.0/0`) to **My IP**, which the console fills in as my current public address with a `/32` mask.
3. Kept **HTTP** open so the website in Task 4 can be reached from a browser:

   | # | Type | Protocol | Port range | Source               |
   |---|------|----------|------------|----------------------|
   | 1 | SSH  | TCP      | 22         | My IP (`<my-ip>/32`) |
   | 2 | HTTP | TCP      | 80         | `0.0.0.0/0`          |

   Outbound was left at the default (All traffic → `0.0.0.0/0`).
4. Chose **Save rules**.

---

## Task 2 : Launch and Connect to `00.5lab_MyIP_EC2_01`

1. Launched an Amazon Linux 2023 `t3.micro` instance with key pair `Wakanda_EC2_Instance` and the My IP security group.
2. **Advanced details → User data:** pasted the full contents of `seir_ec2_userdata.sh` (same script as Lab 0).
3. Named it `00.5lab_MyIP_EC2_01` and waited for **Running** and **3/3 checks passed**.

| Name                  | Instance ID           | State   | Type       | Status check      | Public IPv4     | AZ           |
|-----------------------|-----------------------|---------|------------|-------------------|-----------------|--------------|
| `00.5lab_MyIP_EC2_01` | `i-01b18a4eba968d6bc` | Running | `t3.micro` | 3/3 checks passed | `44.244.248.66` | `us-west-2a` |

📸 **Screenshot [`01_BAM_1.1_MyIP_EC2_01_summary.png`](screenshots/BAM_1.1/01_BAM_1.1_MyIP_EC2_01_summary.png):** Instance summary for `i-01b18a4eba968d6bc` (`00.5lab_MyIP_EC2_01`) showing Public IPv4 `44.244.248.66` and state **Running**.

📸 **Screenshot [`02_BAM_1.1_MyIP_EC2_01_running.png`](screenshots/BAM_1.1/02_BAM_1.1_MyIP_EC2_01_running.png):** Instances list with `00.5lab_MyIP_EC2_01` **Running**, `t3.micro`, **3/3 checks passed**.

### 2.1 SSH from Git Bash

1. Opened Git Bash in the folder holding the key:

   ```bash
   cd ~/Documents/Wakanda_EC2_Key_pair
   chmod 400 Wakanda_EC2_Instance.pem
   ```

2. Connected with the public DNS name from **Connect → SSH client**:

   ```bash
   ssh -i "Wakanda_EC2_Instance.pem" ec2-user@ec2-44-244-248-66.us-west-2.compute.amazonaws.com
   ```

3. The session opened on `ip-172-31-35-56`, which proves my IP was allowed through the tightened SSH rule.

📸 **Screenshot [`03_BAM_1.1_MyIP_EC2_01_ssh.png`](screenshots/BAM_1.1/03_BAM_1.1_MyIP_EC2_01_ssh.png):** Git Bash SSH session to `ec2-44-244-248-66.us-west-2.compute.amazonaws.com` showing the post-quantum warning and the Amazon Linux 2023 banner.

---

## Task 3 : Show the SEIR Dashboard

The dashboard displayed automatically at login. I then ran three quick checks:

```bash
pwd      # /home/ec2-user
whoami   # ec2-user
date     # Sat Oct 24 00:41:21 UTC 2026
```

| Instance              | Hostname          | Uptime | CPU busy | vCPUs | Load (1/5/15)  | Memory         | Root disk         |
|-----------------------|-------------------|--------|----------|-------|----------------|----------------|-------------------|
| `00.5lab_MyIP_EC2_01` | `ip-172-31-35-56` | 4 min  | 0%       | 2     | 0.00 0.01 0.00 | 146Mi / 913Mi  | 1.6G / 8.0G (20%) |

The instance ID (`i-01b18a4eba968d6bc`), type (`t3.micro`) and AZ (`us-west-2a`) came back through IMDSv2 and matched the console. Total memory dropped from 1.9 GiB in Lab 0 to 913 MiB here because `t3.micro` has half the memory of `t3.small`; usage stayed around 150 MiB.

📸 **Screenshot [`04_BAM_1.1_MyIP_EC2_01_dashboard.png`](screenshots/BAM_1.1/04_BAM_1.1_MyIP_EC2_01_dashboard.png):** the full SEIR Foundations dashboard, Cost Reality Check, and the `pwd`, `whoami` and `date` output.

### Observations during connection

| Observation                                                              | What it means                                                                                                                                                              |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SSH connected after the rule change                                      | The My IP rule matched my current public address. If my home IP changes, SSH will time out until the rule is updated.                                                      |
| `WARNING: connection is not using a post-quantum key exchange algorithm` | My newer OpenSSH client prefers post-quantum key exchange and the server's defaults don't offer it yet. The session is still encrypted; a warning to track, not a failure. |
| Dashboard appeared without typing anything                               | The `/etc/profile.d/` hook from User data worked on first login.                                                                                                           |

---

## Task 4 : Launch the Custom Website `00.5lab_MyIP_EC2_02`

1. Launched a second Amazon Linux 2023 `t3.micro` instance with the same key pair and security group.
2. **Advanced details → User data:** pasted the full contents of `website_userdata_v3.sh`, from `#!/bin/bash` to `echo "SEIR website installed. Visit http://<public-ip>/"`.
3. Named it `00.5lab_MyIP_EC2_02` and waited for **Running** and **3/3 checks passed**.

📸 **Screenshot [`01_BAM_1.3_website_userdata_v3_script.png`](screenshots/BAM_1.3/01_BAM_1.3_website_userdata_v3_script.png):** `cat website_userdata_v3.sh` in Git Bash showing the script header, the Python imports and the CSS block.

### What the User Data script does

| Step | Action                                                                                                                                                                |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | Runs with `set -euo pipefail` so the script stops on the first error                                                                                                  |
| 2    | Creates `/opt/seir_foundations` and writes `app.py` with a quoted heredoc so the Python code is stored literally                                                      |
| 3    | `app.py` serves four pages with only the Python standard library (`ThreadingHTTPServer`): `/`, `/about`, `/calculator`, `/server`                                     |
| 4    | `/calculator` is dynamic: the server does the maths on a POST and handles invalid numbers and divide-by-zero, with the request body capped at 10,000 bytes            |
| 5    | `/server` is dynamic: hostname, UTC time and uptime from `/proc/uptime`, plus instance ID, type, AZ and public IPv4 from **IMDSv2** with 1 s timeouts                 |
| 6    | Every page carries a thank-you note and a **Vision Board** of GIFs loaded from GIPHY in the visitor's browser, so nothing is uploaded to the server                   |
| 7    | Writes `/etc/systemd/system/seir_foundations.service` with `Restart=always`, `DynamicUser=yes` and `CAP_NET_BIND_SERVICE` so it binds port 80 without running as root |
| 8    | Runs `systemctl daemon-reload` and `systemctl enable --now` so the site starts now and on every reboot                                                                |

| Name                  | Instance ID           | State                       | Type       | Status check      | Public IPv4    | AZ           |
|-----------------------|-----------------------|-----------------------------|------------|-------------------|----------------|--------------|
| `00.5lab_MyIP_EC2_02` | `i-073c32986ab4e95d8` | Running                     | `t3.micro` | 3/3 checks passed | `32.190.51.47` | `us-west-2a` |
| `00.5lab_MyIP_EC2_02` | `i-0e84a1285ea5f1891` | Terminated (earlier launch) | `t3.micro` | –                 | –              | –            |

📸 **Screenshot [`01_BAM_1.2_MyIP_EC2_02_summary.png`](screenshots/BAM_1.2/01_BAM_1.2_MyIP_EC2_02_summary.png):** Instance summary for `i-073c32986ab4e95d8` (`00.5lab_MyIP_EC2_02`) showing Public IPv4 `32.190.51.47` and state **Running**.

📸 **Screenshot [`02_BAM_1.2_MyIP_EC2_02_running.png`](screenshots/BAM_1.2/02_BAM_1.2_MyIP_EC2_02_running.png):** Instances list with `i-073c32986ab4e95d8` **Running** with **3/3 checks passed**, and an earlier launch with the same name (`i-0e84a1285ea5f1891`) already **Terminated**.

---

## Task 5 : Browse the Live Website

1. Chose **open address** on the instance summary, which opened `http://32.190.51.47/`.
2. Navigated to **Server Info** and refreshed to confirm the page is generated live.

| Field              | Value shown on `/server`                        | Matches console |
|--------------------|-------------------------------------------------|-----------------|
| Hostname           | `ip-172-31-36-29.us-west-2.compute.internal`    | Yes             |
| Instance ID        | `i-073c32986ab4e95d8`                           | Yes             |
| Instance type      | `t3.micro`                                      | Yes             |
| Availability Zone  | `us-west-2a`                                    | Yes             |
| Public IPv4        | `32.190.51.47`                                  | Yes             |
| Server time (UTC)  | `2026-10-25 00:14:50`                           | –               |
| Uptime             | `0h 6m`                                         | –               |

The page loaded over plain HTTP from my browser, which confirms the port 80 rule and the `seir_foundations` service were both working without me logging in to install anything.

📸 **Screenshot [`03_BAM_1.2_MyIP_EC2_02_website.png`](screenshots/BAM_1.2/03_BAM_1.2_MyIP_EC2_02_website.png):** "Koffi EC2 Site" Server Info page with the live instance details, the thank-you note to Theo and Tim's group, the four-GIF Vision Board and the footer naming `ip-172-31-36-29.us-west-2.compute.internal`.

---

## Task 6 : Evidence Summary

| Instance              | Instance ID           | Public IPv4     | Private IPv4    | Access method                                  | Screenshot                                                                                             | Instance Terminated |
|-----------------------|-----------------------|-----------------|-----------------|------------------------------------------------|--------------------------------------------------------------------------------------------------------|---------------------|
| `00.5lab_MyIP_EC2_01` | `i-01b18a4eba968d6bc` | 44.244.248.66   | 172.31.35.56    | SSH from Git Bash (`Wakanda_EC2_Instance.pem`) | [`04_BAM_1.1_MyIP_EC2_01_dashboard.png`](screenshots/BAM_1.1/04_BAM_1.1_MyIP_EC2_01_dashboard.png)     | Yes                 |
| `00.5lab_MyIP_EC2_02` | `i-073c32986ab4e95d8` | 32.190.51.47    | 172.31.36.29    | HTTP in browser (port 80)                      | [`03_BAM_1.2_MyIP_EC2_02_website.png`](screenshots/BAM_1.2/03_BAM_1.2_MyIP_EC2_02_website.png)         | Yes                 |

---

## Task 7 : Terminate the Instances

1. Typed `exit` in the SSH session and closed the website tab.
2. **EC2 → Instances**, selected each `00.5lab_MyIP` instance.
3. **Instance state → Terminate (delete) instance** → confirm.
4. Refreshed until both showed **Terminated**.

📸 **Screenshot [`05_BAM_1.1_MyIP_EC2_01_terminated.png`](screenshots/BAM_1.1/05_BAM_1.1_MyIP_EC2_01_terminated.png):** "Successfully initiated termination (deletion) of i-01b18a4eba968d6bc" with `00.5lab_MyIP_EC2_01` **Terminated**.

📸 **Screenshot [`04_BAM_1.2_MyIP_EC2_02_terminated.png`](screenshots/BAM_1.2/04_BAM_1.2_MyIP_EC2_02_terminated.png):** "Successfully initiated termination (deletion) of i-073c32986ab4e95d8" with both `00.5lab_MyIP_EC2_02` entries **Terminated**.

---

## Task 8 : EC2 Knowledge Checks

| Quiz                 | Score   | Topics covered                                                                                                |
|----------------------|---------|---------------------------------------------------------------------------------------------------------------|
| EC2 quiz section 5   | 12 / 12 | Spot Fleet, purchasing options, Reserved Instance terms, instance types, security groups, migration scenarios |
| EC2 quiz section 6   | 5 / 5   | EC2 Hibernate, Elastic Network Interfaces across AZs, fleets of instances, hosting a Node.js application      |

📸 **Screenshot [`01_maarek_quiz_section_5.png`](udemy/01_maarek_quiz_section_5.png):** "Great job! You are ready to move on to the next lecture. You got 12 out of 12 correct."

📸 **Screenshot [`02_maarek_quiz_section_6.png`](udemy/02_maarek_quiz_section_6.png):** "Great job! You are ready to move on to the next lecture. You got 5 out of 5 correct."

---

## Challange

Inserted images in the body section to reflect on a running website, was able to fix the issue and displayed images on a running website.
Hence the terminated attempt on;

 📸 **Screenshot [`02_BAM_1.2_MyIP_EC2_02_running.png`](screenshots/BAM_1.2/02_BAM_1.2_MyIP_EC2_02_running.png) with an earlier launch with the same name (`i-0e84a1285ea5f1891`) already Terminated.

---

## Lab 0.5 Completion Checklist

- [x] SSH inbound rule changed from `0.0.0.0/0` to **My IP** *(security group screenshot to add)*
- [x] `00.5lab_MyIP_EC2_01` launched, `t3.micro`, Running, 3/3 checks passed
- [x] `00.5lab_MyIP_EC2_01` connected via SSH with `Wakanda_EC2_Instance.pem`
- [x] `seir-dashboard` shown, plus `pwd`, `whoami` and `date`
- [x] `00.5lab_MyIP_EC2_02` launched with `website_userdata_v3.sh`, Running, 3/3 checks passed
- [x] Custom website reached over HTTP and Server Info matched the console
- [x] All screenshots saved in `screenshots/`
- [x] Both instances terminated
- [x] EC2 knowledge checks passed (12/12 and 5/5)

> ⚠️ **Security note:** SSH is now limited to my own IP (`/32`), which removes the internet-wide exposure from Lab 0. HTTP on port 80 stays open to `0.0.0.0/0` because the website is meant to be public; it serves plain HTTP, so nothing sensitive should be submitted through it. The `.pem` key is kept out of Git with a `*.pem` entry in `.gitignore`.
