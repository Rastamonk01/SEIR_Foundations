# SEIR Foundations - Module 1, Lab 0

## EC2 Deployment: Launch, Connect, Observe, Repeat

![AWS](https://img.shields.io/badge/AWS-EC2-orange?style=for-the-badge&logo=amazonaws&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-Bash_Script-green?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Amazon_Linux_2023-yellow?style=for-the-badge&logo=linux&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-Git_Bash-blue?style=for-the-badge&logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

Systems Engineering and Infrastructure Integration

Applied Cloud & Platform Engineering - Lab Results: EC2 Instances

---
This lab used the **AWS Management Console** to:

1. Create an EC2 **launch template** with a custom key pair and a custom security group (SSH + HTTP only).
2. Launch **3 EC2 instances** from that template.
3. Connect to **2 instances with EC2 Instance Connect** and **1 instance with SSH**.
4. Show the **SEIR dashboard** (run `seir-dashboard`).
5. Capture **screenshots** as evidence.
6. **Terminate** the instances.

---

## File Structure

```text
SEIR_Foundations/
├── AWS/
└── README.md
    └── 01module/
        └── 00lab/
            ├── screenshots
            ├── script
            └── README.md
```

---

## Naming Conventions Used

| Resource           | Name                                                                                                                      |
|--------------------|---------------------------------------------------------------------------------------------------------------------------|
| Region             | `us-west-2` (Oregon)                                                                                                      |
| Key pair           | `Wakanda_EC2_Instance` (`Wakanda_EC2_Instance.pem`)                                                                       |
| Security group     | `Wakanda_EC2_Instance_SG`                                                                                                 |
| Launch template    | `Wakanda_EC2_Instance_Deployment_05_Template`                                                                             |
| Instances          | `Wakanda_EC2_Instance_ Deployment_05_1`, `Wakanda_EC2_Instance_ Deployment_05_2`, `Wakanda_EC2_Instance_ Deployment_05_3` |
| Screenshots folder | `screenshots/`                                                                                                            |
| Script  folder     | `script/`                                                                                                                 |

## Environment

- **Region:** `us-west-2`, Availability Zone `us-west-2a` for all three instances.
- **AMI:** Amazon Linux 2023.
- **Instance type:** `t3.small` (2 vCPU, 1.9 GiB memory).
- **Root volume:** 8 GiB.
- **Local SSH client:** Git Bash on Windows, run from `~/Documents/Wakanda EC2 Key pair` *(location you have seved the key pair file)*

---

## Task 1 : Create the EC2 Launch Template

1. In **EC2 → Launch Templates**, created a new launch template.
2. **AMI:** Quick Start → **Amazon Linux 2023 AMI**.
3. **Instance type:** `t3.small`.
4. **Key pair:** `Wakanda_EC2_Instance` (RSA, `.pem` format), stored locally in `~/Documents/Wakanda EC2 Key pair/`.
5. **Network settings:** created a custom security group in the default VPC with exactly two inbound rules:

   | # | Type | Protocol | Port range | Source      |
   |---|------|----------|------------|-------------|
   | 1 | SSH  | TCP      | 22         | `0.0.0.0/0` |
   | 2 | HTTP | TCP      | 80         | `0.0.0.0/0` |

   Outbound was left at the default (All traffic → `0.0.0.0/0`).
6. **Storage:** default 8 GiB root volume.
7. **Advanced details → User data:** pasted the full contents of `seir_ec2_userdata.sh`, from `#!/bin/bash` to `echo 'SEIR dashboard installed.'`.
8. Chose **Create launch template**.

### What the User Data script does

| Step | Action                                                                                                                                        |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | Writes `/usr/local/bin/seir-dashboard` using a quoted heredoc so the code is stored literally                                                 |
| 2    | Sets it to `755` so any user can run it                                                                                                       |
| 3    | Writes `/etc/profile.d/seir-dashboard.sh` so the dashboard runs once per interactive login                                                    |
| 4    | Sets the hook to `644` (readable, not executable)                                                                                             |
| 5    | At login, displays hostname, uptime, CPU busy %, load average, memory and root disk usage                                                     |
| 6    | Reads instance ID, instance type and AZ from the metadata service using **IMDSv2 tokens only**, with 1–2 s timeouts so login is never delayed |
| 7    | Prints a **Cost Reality Check** reminder to stop instances and set a budget alert                                                             |

---

## Task 2 : Launch EC2 Instances from the Template

1. From **Launch Templates**, chose **Actions → Launch instance from template**.
2. Launched three instances with the inherited template settings.
3. Named them with the ✏️ pencil icon in the **Name** column.
4. Waited for **Running** and **3/3 checks passed**.

| Name                                    | Instance ID           | State   | Type       | Status check      | AZ           |
|-----------------------------------------|-----------------------|---------|------------|-------------------|--------------|
| `Wakanda_EC2_Instance_ Deployment_05_1` | `i-00a9c0c10a10ffaa0` | Running | `t3.small` | 3/3 checks passed | `us-west-2a` |
| `Wakanda_EC2_Instance_ Deployment_05_2` | `i-0b9cde10e8e27893b` | Running | `t3.small` | 3/3 checks passed | `us-west-2a` |
| `Wakanda_EC2_Instance_ Deployment_05_3` | `i-0b60714addc8bf12a` | Running | `t3.small` | 3/3 checks passed | `us-west-2a` |

📸 **Screenshot [`Deployment_Instances_GUI_05.png`](/AWS/01module/00lab/screenshots/Deployment_Instances_GUI_05.png) :** the Instances list showing all three `Deployment_05` instances **Running** with **3/3 checks passed** in `us-west-2a`.

---

## Task 3 : Connect to the Instances

### 3.1 EC2 Instance Connect - `Deployment_05_1`

1. Selected `Wakanda_EC2_Instance_ Deployment_05_1` → **Connect** → **EC2 Instance Connect** tab.
2. Username `ec2-user`, then **Connect**.
3. The browser terminal opened on `ip-172-31-34-166` and the SEIR dashboard displayed automatically at login.

📸 **Screenshot `Deployment_05_1.png`:** EC2 Instance Connect session on `i-00a9c0c10a10ffaa0` (Public IP `44.255.198.159`, Private IP `172.31.34.166`) showing the SEIR Foundations dashboard at login and again after running `seir-dashboard`.

### 3.2 EC2 Instance Connect - `Deployment_05_2`

Repeated the steps in **3.1** for `Wakanda_EC2_Instance_ Deployment_05_2`. The session opened on `ip-172-31-42-93`.

📸 **Screenshot `Deployment_05_02.png`:** EC2 Instance Connect session on `i-0b9cde10e8e27893b` (Public IP `35.166.152.17`, Private IP `172.31.42.93`) showing two dashboard runs, with uptime advancing from 3 to 4 minutes.

### 3.3 SSH - `Deployment_05_3`

1. Copied the public DNS name from **Connect → SSH client**.
2. Opened Git Bash in the folder holding the key:

   ```bash
   cd ~/Documents/"Wakanda EC2 Key pair"
   chmod 400 Wakanda_EC2_Instance.pem
   ```

3. Connected:

   ```bash
   ssh -i "Wakanda_EC2_Instance.pem" ec2-user@ec2-44-246-165-48.us-west-2.compute.amazonaws.com
   ```

4. The session opened on `ip-172-31-37-128` and the SEIR dashboard displayed automatically at login.

📸 **Screenshot `Deployment_05_03.png`:** Git Bash SSH session on `i-0b60714addc8bf12a` (Public IP `44.246.165.48`, Private IP `172.31.37.128`) showing the post-quantum warning, the Amazon Linux 2023 banner and the full SEIR dashboard.

### Observations during connection

| Observation                                                              |  What it means                                                                                                                                                                      |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `WARNING: connection is not using a post-quantum key exchange algorithm` | My newer OpenSSH client prefers post-quantum key exchange, and the server's defaults don't offer it yet. The session is still encrypted; this is a warning to track, not a failure. |
| Dashboard appeared without typing anything                               | The `/etc/profile.d/` hook from User data worked on first login.                                                                                                                    |
| `seir-dashboard` re-ran on demand                                        | The script is installed on the `PATH` at `/usr/local/bin`.                                                                                                                          |

---

## Task 4 : Show the SEIR Dashboard

The dashboard ran on all three instances. Readings captured:

| Instance          | Hostname           | Uptime    | CPU busy | vCPUs | Load (1/5/15)  | Memory        | Root disk         |
|-------------------|--------------------|-----------|----------|-------|----------------|---------------|-------------------|
| `Deployment_05_1` | `ip-172-31-34-166` | 5 min     | 2%       | 2     | 0.00 0.00 0.00 | 158Mi / 1.9Gi | 1.6G / 8.0G (20%) |
| `Deployment_05_2` | `ip-172-31-42-93`  | 3 → 4 min | 0%       | 2     | 0.01 0.03 0.00 | 159Mi / 1.9Gi | 1.6G / 8.0G (20%) |
| `Deployment_05_3` | `ip-172-31-37-128` | 11 min    | 11%      | 2     | 0.00 0.01 0.00 | 154Mi / 1.9Gi | 1.6G / 8.0G (20%) |

All three instances returned instance ID, type and AZ through IMDSv2, and every value matched the EC2 console. The 11% CPU reading on `Deployment_05_3` is a single 0.2-second sample taken during SSH login; the near-zero load average confirms the instance was idle.

---

## Task 5 : Evidence Summary

| Instance          | Instance ID           | Public IPv4    | Private IPv4  | Connection method                             | Screenshot                                                                               | Instance Terminated |
|-------------------|-----------------------|----------------|---------------|-----------------------------------------------|------------------------------------------------------------------------------------------|---------------------|
| `Deployment_05_1` | `i-00a9c0c10a10ffaa0` | 44.255.198.159 | 172.31.34.166 | EC2 Instance Connect                          | [`screenshots/Deployment_05_1.png`](/AWS/01module/00lab/screenshots/Deployment_05_1.png) | Yes                 |
| `Deployment_05_2` | `i-0b9cde10e8e27893b` | 35.166.152.17  | 172.31.42.93  | EC2 Instance Connect                          | [`screenshots/Deployment_05_2.png`](/AWS/01module/00lab/screenshots/Deployment_05_2.png) | Yes                 |
| `Deployment_05_3` | `i-0b60714addc8bf12a` | 44.246.165.48  | 172.31.37.128 | SSH from Git Bash(`Wakanda_EC2_Instance.pem`) | [`screenshots/Deployment_05_3.png`](/AWS/01module/00lab/screenshots/Deployment_05_3.png) | Yes                 |

---

## Task 6 : Terminate the Instances

1. Exit the sessions: close the Instance Connect tabs, type `exit` in the SSH session.
2. **EC2 → Instances**, select all three `Deployment_05` instances.
3. **Instance state → Terminate (delete) instance** → confirm.
4. Refresh until all three show **Terminated**.

---

## Next Challenge

Changing the SSH IP Address traffic (`0.0.0.0/0`) → to a custom local IP address (`My IP`) and excuting a custom script.

---

## Lab 0 Completion Checklist

- [x] Launch template created with custom key pair `Wakanda_EC2_Instance` *(screenshot to add)*
- [x] Security group has exactly two inbound rules (SSH 22, HTTP 80) and the default outbound rule *(screenshot to add)*
- [x] 3 instances launched, all `t3.small`, Running, 3/3 checks passed
- [x] `Deployment_05_1` and `Deployment_05_2` connected via EC2 Instance Connect
- [x] `Deployment_05_3` connected via SSH with `Wakanda_EC2_Instance.pem`
- [x] `seir-dashboard` shown on each instance
- [x] All screenshots saved in `screenshots/`
- [x] All 3 instances terminated

> ⚠️ **Security note:** `0.0.0.0/0` on port 22 exposes SSH to the entire internet. It's acceptable for this short-lived lab, but in real environments restrict SSH to your own IP (`My IP`) or use Session Manager. The `.pem` key is kept out of Git with a `*.pem` entry in `.gitignore`.
