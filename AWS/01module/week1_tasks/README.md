# SEIR Foundations: Week 1 Tasks: SSH & EC2 User Data Website

![AWS](https://img.shields.io/badge/AWS-EC2-orange?style=for-the-badge&logo=amazonaws&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-Bash_Script-green?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Amazon_Linux_2023-yellow?style=for-the-badge&logo=linux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-Git_Bash-blue?style=for-the-badge&logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

Systems Engineering and Infrastructure Integration

Applied Cloud & Platform Engineering - Lab Results: Server Info & Calculator Website

---

## What the Lab Does

The lab is split into two tasks, both run against the same EC2 instance launched from a launch template.

1. Launch a `t3.micro` Amazon Linux 2023 instance (`Week1_tasks_Instance_01`) in `us-west-2` from the `Week1_tasks` launch template.
2. Attach a User Data startup script that writes a small Python web app and registers it as a systemd service called `seir_foundations`.
3. Connect to the instance from Git Bash on Windows using `ssh` and a `.pem` key pair (not EC2 Instance Connect).
4. Run the tasks practice commands: create and read a text file, make and enter a folder, print the working directory and list the home directory.
5. Run extra commands of my own to check memory, disk, uptime, hostname and current user.
6. Open the instance's public IP in a browser and test all four pages, including the dynamic calculator.
7. Terminate the instance once testing is done to avoid ongoing charges.

---

## File Structure

```text
SEIR_Foundations/
├── AWS/
    └── 01module/
        └── week1_tasks
            ├── screenshots
            ├── script     ← Website User Data startup script
            └── README.md
```

---

## Linux Commands Used

### 1. `ssh -i`

**Definition:** Opens a secure shell session to a remote host, with `-i` pointing to the private key file used to authenticate.
**Why I used it:** It was the required way to connect for Task 1, using `Wakanda_EC2_Instance.pem` to log in as `ec2-user` from Git Bash.

### 2. `echo "Hello, World!" > hello.txt`

**Definition:** Prints text and, with `>`, redirects it into a file, creating or overwriting it.
**Why I used it:** To create a simple text file on the server as the first CPG exercise.

### 3. `cat`

**Definition:** Prints the contents of a file to the terminal.
**Why I used it:** To confirm `hello.txt` contained `Hello, World!`.

### 4. `mkdir new_project && cd new_project`

**Definition:** Creates a directory, and `&&` runs `cd` into it only if `mkdir` succeeded.
**Why I used it:** To make a project folder and move into it in one line.

### 5. `pwd`

**Definition:** Prints the full path of the current working directory.
**Why I used it:** To confirm I was inside `/home/ec2-user/new_project`.

### 6. `ls -l ~`

**Definition:** Lists the home directory (`~`) in long format (`-l`), showing permissions, owner, size and date.
**Why I used it:** To see both `hello.txt` and the `new_project` directory I had created.

### 7. `free -h`

**Definition:** Shows memory and swap usage, with `-h` for human-readable units.
**Why I used it:** To check how much RAM a `t3.micro` has (about 913 MiB) and how much the web service was using.

### 8. `df -h`

**Definition:** Shows disk space usage per mounted filesystem in human-readable units.
**Why I used it:** To confirm the 8 GB root volume was only 20% used.

### 9. `uptime`

**Definition:** Shows how long the system has been running, logged-in users and load averages.
**Why I used it:** To check the instance was healthy and idle (load average near zero).

### 10. `hostname`

**Definition:** Prints the system's host name.
**Why I used it:** To match the server name shown in the website footer and Server Info page.

### 11. `whoami`

**Definition:** Prints the user name of the current session.
**Why I used it:** To confirm I was logged in as `ec2-user`.

---

## EC2 Instance Details

| Field           | Detail                                 |
|-----------------|----------------------------------------|
| Name            | `Week1_tasks_Instance_01`              |
| Instance ID     | `i-050002597ad1e2064`                  |
| Launch template | `Week1_tasks` (`lt-0265a9de419b1e41f`) |
| Instance type   | `t3.micro`                             |
| AMI             | Amazon Linux 2023                      |
| Region / AZ     | US West (Oregon) / `us-west-2a`        |
| Public IPv4     | `35.86.131.142`                        |
| Private IPv4    | `172.31.35.25`                         |
| Final state     | Terminated after testing               |

---

## Web Page Requirements

| Requirement         | How it was met                                                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| At least 3 pages    | 4 pages: Home `/`, About `/about`, Calculator `/calculator`, Server Info `/server`                                                  |
| One dynamic page    | Calculator sends two numbers and an operator (+ − × ÷) to the server, which returns the result (e.g. `88 + 15 = 103`, `7 × 7 = 49`) |
| Extra dynamic page  | Server Info shows live hostname, instance ID, type, AZ, public IP, UTC time and uptime                                              |
| Set up by User Data | Script ran at first boot; no manual install over SSH                                                                                |
| Web server          | Python 3 standard library (no extra packages)                                                                                       |
| Kept running        | systemd service `seir_foundations`                                                                                                  |
| Shared public IP    | `http://35.86.131.142`                                                                                                              |

---

## How to Deploy

1. In the EC2 console, launch an instance from the `Week1_tasks` launch template (or choose Amazon Linux 2023 and `t3.micro`).
2. Make sure the security group allows inbound SSH (port 22) from your IP and HTTP (port 80).
3. Under **Advanced details → User data**, paste the script from the `script` folder.
4. Launch the instance and wait for the status checks to pass.
5. Copy the public IPv4 address and open `http://<public-ip>` in a browser.
6. Connect over SSH from Git Bash:

```bash
cd ~/Documents/Wakanda_EC2_Key_pair
ssh -i "Wakanda_EC2_Instance.pem" ec2-user@ec2-35-86-131-142.us-west-2.compute.amazonaws.com
```

7. When finished, select the instance and choose **Instance state → Terminate**.

---

## Screenshots

| Screenshot                                                                                       | Description                                                                                  |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [`01_launch_template.png`](/AWS/01module/Week1_tasks/screenshots/01_launch_template.png)         | Launch templates list in US West (Oregon) showing the `Week1_tasks` template                 |
| [`02_instance_running.png`](/AWS/01module/Week1_tasks/screenshots/02_instance_running.png)       | `Week1_tasks_Instance_01` running as `t3.micro` with public IP `35.86.131.142`               |
| [`03_ssh_tasks_commands.png`](/AWS/01module/week1_tasks/screenshots/03_ssh_tasks_commands.png)   | Git Bash SSH login, then `echo`, `cat`, `mkdir && cd`, `pwd` and `ls -l ~` output            |
| [`04_ssh_extra_commands.png`](/AWS/01module/week1_tasks/screenshots/04_ssh_extra_commands.png)   | Second SSH session running `free -h`, `df -h`, `uptime`, `hostname` and `whoami`             |
| [`05_home_page.png`](/AWS/01module/week1_tasks/screenshots/05_home_page.png)                     | Home page "Hello from the cloud!" with links to the other pages                              |
| [`06_about_page.png`](/AWS/01module/week1_tasks/screenshots/06_about_page.png)                   | About page listing Amazon Linux 2023, Python 3, the `seir_foundations` service and User Data |
| [`07_calculator_dropdown.png`](/AWS/01module/week1_tasks/screenshots/07_calculator_dropdown.png) | Calculator with the operator dropdown open showing + − × ÷                                   |
| [`08_calculator_add.png`](/AWS/01module/week1_tasks/screenshots/08_calculator_add.png)           | Calculator result `88 + 15 = 103`                                                            |
| [`09_calculator_multiply.png`](/AWS/01module/week1_tasks/screenshots/09_calculator_multiply.png) | Calculator result `7 × 7 = 49`                                                               |
| [`10_server_info.png`](/AWS/01module/week1_tasks/screenshots/10_server_info.png)                 | Server Info page with instance ID, type, AZ, public IP, UTC time and uptime                  |
| [`11_instance_terminated.png`](/AWS/01module/week1_tasks/screenshots/11_instance_terminated.png) | Console banner confirming termination of `i-050002597ad1e2064`                               |

---

## Git Workflow Used

```bash
# Move into the lab folder
cd SEIR_Foundations/AWS/01module/00lab

# Stage the README, script and screenshots
git add README.md script screenshots

# Commit with a clear message
git commit -m "Add Module 1 Lab 00: SSH and EC2 User Data website"

# Push to GitHub
git push origin main
```
