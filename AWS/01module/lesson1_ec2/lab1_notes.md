# Lesson 1 Lab Notes - Balerica Legacy Bank (FastAPI + COBOL core)

**Person:** KA (Koffi A)
**Time zone used in every screenshot:** Australia/Adelaide (ACDT, UTC+10:30)
**Required ID line:** `whoami && TZ='Australia/Adelaide' date && ec2-metadata -i && uptime -s`

```bash
## Swapped ID
> sudo timedatectl set-timezone Australia/Adelaide
##### set the timezone
> whoami && date && timedatectl show -p Timezone --value && ec2-metadata -i && uptime -s && uptime -p
##### gets all ID and server running period/time
```

---

## Run 1 - i-04a3f004ec972e0d3

- **Date:** Sat 31 Oct 2026
- **Name tag:** lesson1_ec2_template_01 (t2.small, us-east-1c)
- **Private / public IP:** 172.31.31.92 / 98.89.23.249
- **Public IPv4 DNS:** ec2-98-89-23-249.compute-1.amazonaws.com
- **Boot time:** My first ID line swapped `uptime -s` with `uptime -p`, which printed `up 18 minutes` at 08:27:16 ACDT. That puts the boot at about 08:09 ACDT (about 21:39 UTC on 30 Oct).

**What I did / what changed:**
This was my first full run of Steps 0–4. I cloned the course repo, ran the installer, ran the COBOL programs by hand, and started uvicorn. From my laptop I opened the home page, `/docs` and `/openapi.json`. Each request showed up in the uvicorn log, and `/favicon.ico` returned a harmless `404 Not Found`.

**Errors and fixes:**
I used `uptime -p` instead of `uptime -s`, so the ID line showed how long the server had been up instead of when it booted. The README table needs the boot time, so this screenshot has to be retaken: Ctrl+C, the correct ID line, then uvicorn again. I also left this instance running for more than 4 hours.

**What I newly understood:**
The uvicorn window doubles as a live access log, showing the caller's IP, path and status code for every request. A return code lets a program report "not found" without crashing.

**Exact output line only this run would have:**

```text
INFO:     Started server process [36530]
```

📸 **Screenshot : [`Run 1 Console`](lab_runs/screenshots/id_lesson1_ec2_template_01.png)** |
📸 **Bank Screenshot : [`Run 1 Bank Website`](lab_runs/screenshots/bank_results_lesson1_ec2_template_01.png)**

---

## Run 2 - i-064f0e898402def08

- **Date:** Sat 31 Oct 2026
- **Name tag:** lesson1_ec2_template_02 (t2.small, us-east-1c)
- **Private / public IP:** 172.31.22.67 / 13.218.110.252
- **Public IPv4 DNS:** ec2-13-218-110-252.compute-1.amazonaws.com
- **Boot time (as shown):** `2026-10-31 12:05:48` (ACDT) = **2026-10-31 01:35:48 UTC**
- **ID line run at:** Sat Oct 31 12:22:50 ACDT 2026, `up 17 minutes`

**What changed:**
I fixed the boot time by adding `uptime -s`. I also added `timedatectl show -p Timezone --value`, which printed `Australia/Adelaide`. That showed me the instance's own clock is set to Adelaide, not UTC. I opened the home page, `/docs` and the port-80 instance-details page in the browser, and the bank's Swagger page listed all seven endpoints, including `/chewbacca`.

**Errors and fixes:**
Because the system time zone is Australia/Adelaide, `uptime -s` prints the boot time in ACDT. For the README I had to convert it to UTC by subtracting 10 hours 30 minutes. My ID line was also not the exact one the assignment asks for: I wrote `date` plus `timedatectl` instead of `TZ='Australia/Adelaide' date`, and added `uptime -p` at the end. From Run 4 on, I'll use the exact required line.

**What I newly understood:**
Setting `TZ=` in front of a command only changes that one command. `timedatectl` shows the time zone of the whole machine. Two times can look the same and still be in different zones, so I always need to know which zone I'm reading.

**Exact output line only this run would have:**

```text
INFO:     Started server process [36428]
```

📸 **Screenshot : [`Run 2 Console`](lab_runs/screenshots/id_lesson1_ec2_template_02.png)** |
📸 **Bank Screenshot : [`Run 2 Bank Website`](lab_runs/screenshots/bank_results_lesson1_ec2_template_02.png)**

---

## Run 3 - i-083ad8a12ddd32738

- **Date:** Sat 31 Oct 2026
- **Name tag:** lesson1_ec2_template_03 (t2.small, us-east-1c)
- **Private / public IP:** 172.31.19.115 / 3.95.62.149
- **Public IPv4 DNS:** ec2-3-95-62-149.compute-1.amazonaws.com
- **Boot time (as shown):** `2026-10-31 12:33:47` (ACDT) = **2026-10-31 02:03:47 UTC**
- **ID line run at:** Sat Oct 31 12:46:55 ACDT 2026, `up 13 minutes`

**What changed:**
This run was my fastest yet: 13 minutes from boot to uvicorn, compared with 17 minutes for Run 2 and 18 for Run 1. I knew the order of the steps without reading ahead. The return codes matched every time: `0` for Alice and `4` for 999999.

**Errors and fixes:**
I still typed `echo $?` on its own line after `account_lookup 999999`. It worked only because I typed nothing in between. Next time I'll put `; echo $?` on the same line. I also had three instances running at the same time (Runs 1–3), which costs money.

**What I newly understood:**
Every new instance gets a new private IP, public IP, DNS name and instance ID, and uvicorn gets a new process ID. That's why each run can be proven unique. The journal on each new instance starts empty, because each instance has its own disk.

**Exact output line only this run would have:**

```text
INFO:     Started server process [36061]
```

📸 **Screenshot : [`Run 3 Console`](lab_runs/screenshots/id_lesson1_ec2_template_03.png)** |
📸 **Bank Screenshot : [`Run 3 Bank Website`](lab_runs/screenshots/bank_results_lesson1_ec2_template_03.png)**

---

## Run 4 - i-0754f23fd7f36b03d

- **Date:** Sun 1 Nov 2026
- **Name tag:** lesson1_ec2_template_04 (t2.small, us-east-1c)
- **Private / public IP:** 172.31.20.37 / 52.91.51.168
- **Public IPv4 DNS:** ec2-52-91-51-168.compute-1.amazonaws.com
- **Boot time (as shown):** `2026-11-01 11:41:22` (ACDT) = **2026-11-01 01:11:22 UTC**
- **ID line run at:** Sun Nov 1 11:52:25 ACDT 2026, `up 11 minutes`

**What changed:** This was my first run of the day. I noticed that the system time zone isn't set by my template: I set it myself with `sudo timedatectl set-timezone Australia/Adelaide`. The login banner showed `Last login: Sun Nov 1 01:15:02`, which is UTC, because it was printed *before* I changed the time zone. Steps 0–4 went through without me looking at the runbook.

**Errors and fixes:** I still typed `echo $?` on its own line after `account_lookup 999999`, and I used my modified ID line instead of the exact required one. No new errors. The installer and the COBOL compile worked the first time.

**What I newly understood:** `timedatectl set-timezone` changes the whole machine's clock display, including `uptime -s` and the login message. `TZ='...' date` changes only that single command. If I hadn't changed the system time zone, `uptime -s` would already print UTC, which is what the README table wants.

**Exact output line only this run would have:**

```text
INFO:     Started server process [36278]
```

📸 **Screenshot : [`Run 4 Console`](lab_runs/screenshots/id_lesson1_ec2_template_04.png)** |
📸 **Bank Screenshot : [`Run 4 Bank Website`](lab_runs/screenshots/bank_results_lesson1_ec2_template_04.png)**

---

## Run 5 - i-0d670053a1967c65c

- **Date:** Sun 1 Nov 2026
- **Name tag:** lesson1_ec2_template_05 (t2.small, us-east-1c)
- **Private / public IP:** 172.31.31.97 / 54.146.212.178
- **Public IPv4 DNS:** ec2-54-146-212-178.compute-1.amazonaws.com
- **Boot time (as shown):** `2026-11-01 11:58:32` (ACDT) = **2026-11-01 01:28:32 UTC**
- **ID line run at:** Sun Nov 1 12:08:29 ACDT 2026, `up 9 minutes`

**What changed:** This was my fastest run: about 10 minutes from boot to uvicorn. I had the installer path and the commands memorised. The browser pages (`/`, `/docs`, `/openapi.json`) loaded straight away because my security group already allows port 8000.

**Errors and fixes:** No errors. The only repeat was the separate-line `echo $?`.

**What I newly understood:** The fresh instance had a brand-new ledger (Alice at 5000.00, and `payments.dat` holding only `TXN0001`). Each instance has its own disk, so nothing carries over unless I bake an AMI, which I did in BAM 2.3.

**Exact output line only this run would have:**

```text
INFO:     Started server process [35859]
```

📸 **Screenshot : [`Run 5 Console`](lab_runs/screenshots/id_lesson1_ec2_template_05.png)** |
📸 **Bank Screenshot : [`Run 5 Bank Website`](lab_runs/screenshots/bank_results_lesson1_ec2_template_05.png)**

---

## Run 6 - i-0374393f4a4010f6f

- **Date:** Sun 1 Nov 2026
- **Name tag:** lesson1_ec2_template_06 (t2.small, us-east-1c)
- **Private / public IP:** 172.31.25.125 / 18.206.236.27
- **Public IPv4 DNS:** ec2-18-206-236-27.compute-1.amazonaws.com
- **Boot time (as shown):** `2026-11-01 12:15:11` (ACDT) = **2026-11-01 01:45:11 UTC**
- **ID line run at:** Sun Nov 1 12:36:41 ACDT 2026, `up 21 minutes`

**What changed:** This run took longer (21 minutes from boot to uvicorn) because I was working on Runs 4–6 in parallel. After the screenshots I terminated all three instances in one action.

**Errors and fixes:** No errors. The uvicorn log showed a different client IP this time (`187.13.204.246` instead of `.248`). My home connection's public IP changed. If my security group allowed only "My IP", the browser could have been blocked, and I'd have needed to update the rule.

**What I newly understood:** Terminating several instances at once is quick, but I still need to check Volumes afterwards. The private IPs (172.31.x.x) all come from the same default VPC `vpc-0b755df40fcd9c5cc`, while each public IP and DNS name is new every time.

**Exact output line only this run would have:**

```text
INFO:     Started server process [36808]
```

📸 **Screenshot : [`Run 6 Console`](lab_runs/screenshots/id_lesson1_ec2_template_06.png)** |
📸 **Bank Screenshot : [`Run 6 Bank Website`](lab_runs/screenshots/bank_results_lesson1_ec2_template_06.png)**

---

## Run 7 - i-0f322fe776c92d324

- **Date:** Tue 3 Nov 2026
- **Name tag:** lesson1_ec2_template_07 (t2.small, us-east-1c)
- **Private / public IP:** 172.31.18.77 / 54.226.96.241
- **Public IPv4 DNS:** ec2-54-226-96-241.compute-1.amazonaws.com
- **Boot time (as shown):** `2026-11-03 08:15:49` (ACDT) = **2026-11-02 21:45:49 UTC**. The UTC date is the day before, because 08:15 in Adelaide is still the previous evening in UTC.
- **ID line run at:** Tue Nov 3 08:41:20 ACDT 2026, `up 25 minutes`

**What changed:** This was the final run. I did Steps 0–4 from memory and browsed `/`, `/docs` and `/openapi.json` from my laptop, and all returned 200. In a separate session I also completed the git clone task (see Git below).

**Errors and fixes:** No errors. Converting the boot time to UTC crossed midnight, so I had to change the date as well as the hour. It's an easy mistake to make in the README table.

**What I newly understood:** After seven runs, what used to take me 18 minutes is routine. BAM 2.2 showed me that a launch template with User Data can do all of it with no typing at all. Repeating something by hand is how you learn exactly what to automate.

**Exact output line only this run would have:**

```text
INFO:     Started server process [37421]
```

📸 **Screenshot : [`Run 7 Console`](lab_runs/screenshots/id_lesson1_ec2_template_07.png)** |
📸 **Bank Screenshot : [`Run 7 Bank Website`](lab_runs/screenshots/bank_results_lesson1_ec2_template_07.png)**

---

## Git - clone my repo on EC2

- **Instance:** `i-0495ce968de35c32b` (name `git_clone`), private 172.31.19.136, public 54.221.82.102
- **ID line:** Tue Nov 3 08:57:09 ACDT 2026, boot `2026-11-03 08:49:14` (ACDT) = 2026-11-02 22:19:14 UTC
- **Commands:** `sudo dnf install -y git`, then `git clone https://github.com/Rastamonk01/SEIR_Foundations.git`, then `cd SEIR_Foundations/AWS/01module`, then `ls`
- **Output:** `Receiving objects: 100% (187/187), 7.13 MiB` and `00.5lab  00lab  lesson1_ec2  week1_tasks`
- **Notes:** `AWS/01module` is my Module 1 folder. I only cloned: I didn't push from EC2, and I didn't put a token on the server. The repo is public, so no credentials were needed. A fresh Amazon Linux 2023 instance doesn't include git, so I installed it first (`git-2.50.1`).
- **Cleanup:** Terminated `i-0495ce968de35c32b`.

📸 **Screenshot : [`My Repo Clone`](lab_runs/screenshots/git_clone.png)** |
📸 **Instance Screenshot : [`Repo Instance Terminated`](lab_runs/screenshots/git_clone_terminated.png)**

---

## COBOL practice

**Run and instance used:** Run 1, `i-04a3f004ec972e0d3`, in `/opt/balerica-bank`
**My TXN prefix:** `TXN-KA-`

### Return code 0 - success (`cobol_rc0.jpg`)

```text
$ ./cobol/bin/payment_post TXN-KA-0001 100001 10.00 USD HW-RC0; echo $?
TXN=TXN-KA-0001
ACCOUNT=100001
AMOUNT=10.00
CURRENCY=USD
STATUS=POSTED
REASON=APPROVED
0
```

📸 **Screenshot : [`Return Code 0`](lab_runs/screenshots/cobol_rc0.png)**

### Return code 4 - account not found (`cobol_rc4.jpg`)

```text
$ ./cobol/bin/account_lookup 999999; echo $?
ERROR=ACCOUNT NOT FOUND
ACCOUNT=999999
4
```

📸 **Screenshot : [`Return Code 4`](lab_runs/screenshots/cobol_rc4.png)**

### Return code 8 - business rejection (`cobol_rc8.jpg`)

```text
$ ./cobol/bin/payment_post TXN-KA-0002 100001 0.00 USD HW-RC8; echo $?
TXN=TXN-KA-0002
ACCOUNT=100001
AMOUNT=0.00
CURRENCY=USD
STATUS=REJECTED
REASON=AMOUNT MUST BE GREATER THAN ZERO
8
```

📸 **Screenshot : [`Return Code 8`](lab_runs/screenshots/cobol_rc8.png)**

### Return code 12 - environment failure (`cobol_rc12.jpg`)

```text
$ cd ~ && /opt/balerica-bank/cobol/bin/account_lookup 100001; echo $?
ERROR=CANNOT OPEN data/accounts.dat
FILE-STATUS=35
12
```

The program opens `data/accounts.dat` relative to the current folder. From my home folder that path doesn't exist, so COBOL reports file status 35 ("file not found") and exits with 12.

📸 **Screenshot : [`Return Code 12`](lab_runs/screenshots/cobol_rc12.png)**

### Ledger decoded by hand with `cut -c` (`cobol_ledger_decode.jpg`)

| Columns | Field             | 100001        | 100002       | 100003       |
|---------|-------------------|---------------|--------------|--------------|
| 1–6     | account id        | 100001        | 100002       | 100003       |
| 7–36    | name              | Alice Johnson | Robert Smith | Maria Garcia |
| 37–44   | status            | ACTIVE        | ACTIVE       | ACTIVE       |
| 45–56   | balance (raw)     | 000000500000  | 000000275000 | 000000810000 |
| 45–56   | balance (decoded) | 5000.00       | 2750.00      | 8100.00      |
| 57–59   | currency          | USD           | USD          | USD          |

**Alice's balance, decoded:** the raw field is `000000500000`. Its layout is `PIC 9(10)V99`: 10 digits for whole dollars, then 2 digits for cents. The `V` marks where the decimal point goes, but the point itself is never stored in the file. The first 10 digits, `0000005000`, give 5000. The last 2, `00`, give 00 cents. So the balance is **5000.00**, which matches `BALANCE=5000.00` from `account_lookup`.

📸 **Screenshot : [`Ledger Decode`](lab_runs/screenshots/cobol_ledger_decode.png)**

### Journal lines for my TXN IDs

```text
$ grep 'TXN-KA' data/payments.dat
TXN-KA-0001         100001000000001000USDPOSTED  HW-RC0
TXN-KA-0002         100001000000000000USDREJECTEDHW-RC8
```

- `000000001000` is 10.00 and `000000000000` is 0.00, decoded with the same implied-decimal rule.
- `REJECTED` is exactly 8 characters, so it fills the whole status field and runs straight into the memo. `POSTED` is 6 characters, so it gets 2 spaces of padding.
- The rejected payment was still written to the journal. A bank keeps a record of what it refused, not just what it approved.

### Did the balance change?

**No.** After posting `TXN0001` (125.50) and `TXN-KA-0001` (10.00), Alice still showed:

```text
BALANCE=5000.00
000000500000
```

📸 **Screenshot : [`Balance Verdit`](lab_runs/screenshots/cobol_balance_verdict.png)**

My understanding is that `payment_post` run from the command line only adds a line to the journal (`payments.dat`). It does not update `accounts.dat`, which is an export from SQLite, the system of record. (One can retest with uvicorn running, post through `POST /payments`, and check whether `/transactions` or the balance changes. My `curl -s .../transactions` printed nothing, probably because uvicorn wasn't running at that moment, and `-s` hides the connection error.)

---

## Mistakes I made

1. I used `uptime -p` instead of `uptime -s` in the Run 1 ID line.
2. In Runs 2–3 I changed the required ID line instead of using it exactly as given.
3. I didn't notice at first that the instance clock is set to Australia/Adelaide, so `uptime -s` shows ACDT, not UTC.
4. I took the COBOL screenshots without the ID line above the commands.
5. I posted `TXN0001` without my initials. That was fine for the runbook step, but not for the practice.
6. I typed `echo $?` on a separate line instead of using `; echo $?`.
7. I pasted several commands at once, so their outputs bunched together.
8. I left Run 1 running for more than 4 hours, and had three instances running at once.

## Commands I now know by heart

- `whoami`, `pwd`, `ls`, `cd /opt/balerica-bank`
- `sudo dnf install -y git`, `git clone <url>`
- `source venv/bin/activate`
- `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- `./cobol/bin/account_lookup <id>; echo $?`
- `./cobol/bin/payment_post <txn> <acct> <amt> USD <memo>; echo $?`
- `cat data/payments.dat`, `grep 'TXN-KA' data/payments.dat`
- `cut -c45-56 data/accounts.dat`
- `curl http://127.0.0.1:8000/status`
- `timedatectl show -p Timezone --value`
- `whoami && TZ='Australia/Adelaide' date && ec2-metadata -i && uptime -s`

---

## BAM (extra credit)

### BAM_2.1 - `/ask` answers from Amazon Bedrock ✅

- **Instance ID:** i-09a4d6d2097ec92ed (ip-172-31-24-131)
- **ID line:** Sun Nov 1 09:19:21 ACDT 2026, boot `2026-11-01 07:18:06` (ACDT) = 2026-10-31 20:48:06 UTC
- **IAM role / instance profile:** `BalericaLegacyBankEC2Role`, with the inline policy `BedrockInvokeModel` (`bedrock:InvokeModel` only, `Resource: "*"`). I created it in AWS CloudShell from the repo's `ec2-trust-policy.json` and `bedrock-invoke-policy.json`.
- **AWS_REGION:** us-east-1
- **Inference profile ID:** `us.anthropic.claude-haiku-4-5-20251001-v1:0`
- **Proof there are no access keys:** `aws sts get-caller-identity` returned `arn:aws:sts::<account>:assumed-role/BalericaLegacyBankEC2Role/i-09a4d6d2097ec92ed`. `~/.aws` holds only the CLI's `cli` cache folder, with no `credentials` or `config` file. The instance gets short-lived credentials from its role through the instance metadata service.

**Question (only my ledger can answer):**

```text
What is the status and amount of TXN-KA-0101, and what is Alice Johnson's current balance?
```

**Full response:**

```json
{
    "question": "What is the status and amount of TXN-KA-0101, and what is Alice Johnson's current balance?",
    "response": "Based on the live system context:\n\n**TXN-KA-0101:**\n- Status: **POSTED**\n- Amount: **$42.00**\n- Transaction ID: TXN93486699113563656\n\n**Alice Johnson (Account 100001):**\n- Current Balance: **$2,870.81 USD**\n- Account Status: **ACTIVE**\n\nThe transaction has been successfully posted to her account.",
    "source": "amazon-bedrock"
}
```

📸 **Screenshot : [`BAM_2.1`](lab_runs/BAM_2/BAM_2.1.png)** |
📸 **Screenshot : [`BAM_2.1 SSH`](lab_runs/BAM_2/BAM_2.1_5.png)**

**How I checked it:** Compare against `curl -s http://127.0.0.1:8000/accounts/100001` (balance 2,870.81?) and `curl -s http://127.0.0.1:8000/transactions` (does `TXN-KA-0101` appear, and where does the `TXN9348...` ID come from?).

**Errors hit and fixes:**

1. In CloudShell, pasting several commands at once merged them into one line, giving "Unknown options" errors. `add-role-to-instance-profile` never ran, so the instance profile was empty (`"Roles": []`). Fix: one command per Enter.
2. A `\` line continuation broke during the paste, giving `ParamValidation: --iam-instance-profile required`. Fix: run the command on a single line.
3. The model ID had two prefixes (`us.anthropic.global.anthropic...`), giving `ValidationException: model identifier is invalid`.
4. Claude Haiku 5.5 and Opus 4.7 gave `AccessDeniedException ... not available for this account`, in both the instance and the Playground. That is account-level model access, not IAM: an IAM denial says "not authorized to perform bedrock:InvokeModel". Claude Haiku 4.5 worked in the Playground, so I used its `us.` profile.

**What I learned:** `/ask` falls back to the offline answers silently, so I tested each layer separately: role (`sts get-caller-identity`), then model access (Playground), then the model ID (`bedrock-runtime converse`), and only then the app. The exact wording of an AccessDenied message tells you which layer refused.

📸 **Screenshot : [`BAM_2.1 sts caller`](lab_runs/BAM_2/BAM_2.1_2.png)**

### BAM_2.2 - Baked launch template

- **Launch template:** `balerica-bank-baked`, ID **`lt-070a12156a2d7831e`**, **version 1** (default), created 2026-11-01T02:51:12Z. This is a new template.
- **Template settings:** AMI `ami-0c230065b91270bc6` (Amazon Linux 2023), t2.small, key pair `lesson1_ec2_keypair`, security group `sg-07e77e9cf11a520d9` (lesson1_ec2_sg), IAM role `BalericaLegacyBankEC2Role`
- **Instance launched from it:** `i-05e8c105391b3ecec` (`lesson1_BAM_2.2_baked`), private 172.31.26.25, public 100.27.199.189, DNS ec2-100-27-199-189.compute-1.amazonaws.com
- **Final User Data:**

```bash
#!/bin/bash
set -x
export HOME=/root
dnf install -y git
cd /home/ec2-user
git clone https://github.com/BalericaAI/SEIR-Foundations.git
bash SEIR-Foundations/module1/lesson1_ec2/API/install/install.sh
chown -R ec2-user:ec2-user /home/ec2-user/SEIR-Foundations /opt/balerica-bank
echo "BALERICA USER DATA FINISHED"
```

**Script : [`BAM_2.2 Baked User Data`](scripts/BAM_2.2.sh)**

- 📸 **Screenshot : [`BAM_2.2 Connect`](lab_runs/BAM_2/BAM_2.2_instance_connect_id.png):** `sudo cloud-init status --wait` printed `status: done`. On the instance clock, which was still UTC, the ID line showed `Sun Nov 1 03:04:09 UTC 2026`, `instance-id: i-05e8c105391b3ecec`, and boot `2026-11-01 02:52:02` (UTC), `up 12 minutes`. `sudo grep -n "Installation complete" /var/log/cloud-init-output.log` returned **`1030:Installation complete.`** (line 1030 of the log). `./cobol/bin/account_lookup 100001; echo $?` returned Alice Johnson, ACTIVE, 5000.00 USD, then **`0`**. I typed no install commands.
- **Time zone check:** I then ran `sudo timedatectl set-timezone Australia/Adelaide` and the same ID line again. The boot time now printed as `2026-11-01 13:22:02` (ACDT), which is the **same moment** as 02:52:02 UTC, plus 10 hours 30 minutes. This proves `uptime -s` uses the system time zone, and that on Runs 2–6 my boot times were ACDT only because I had changed it myself.
- **Cleanup:** instance `i-05e8c105391b3ecec` terminated ✅. Launch template `lt-070a12156a2d7831e` kept, as the assignment asks.
- **Mistake:** I was already logged in to the instance through EC2 Instance Connect, and then ran the `ssh` command *from inside the instance*. The `.pem` file only exists on my laptop, so it failed: "Identity file not accessible" and then "Permission denied (publickey)". The prompt `ec2-user@ip-172-31-26-25` showed I was already on the target machine.

### BAM_2.3 - Golden AMI

- **Source instance ID:** i-09a4d6d2097ec92ed (the configured BAM 2.1 instance)
- **AMI:** `ami-0d4ff01d90546aa7d` (name `lesson1_ec2_template_04_image`, created 2026-10-31T22:56:31Z, status Available)
- **Snapshot:** `snap-0d9bc7af9ba2848f7` (8 GiB root volume `vol-0997b11e3becdda94`; full snapshot size 2 GiB). The description, "Created by CreateImage(i-09a4d6d2097ec92ed) for ami-0d4ff01d90546aa7d", links the snapshot, the AMI and the source instance.
- **AMI-launched instance ID:** i-0fa6fc630cd34f507 (`lesson1_BAM_2.3_from_ami`, t3.micro, private 172.31.31.34, public 54.234.197.139, DNS ec2-54-234-197-139.compute-1.amazonaws.com)
- **Boot time:** `2026-11-01 09:57:39` (ACDT) = 2026-10-31 23:27:39 UTC
- **Proof:** On the new instance I only ran `cd /opt/balerica-bank`, `source venv/bin/activate`, the ID line and `uvicorn`, with no installer, and still got `Application startup complete.` (server process [2922] on my first attempt). `/`, `/docs` and `/openapi.json` all returned 200 from my browser.
- **Surprise:** the port-80 "AWS Instance Details" page on the new instance still said `ip-172-31-24-131`, which is the **source** instance's hostname. The page was generated once, at the source's first boot, and the AMI copied that file as-is. An AMI freezes everything on the disk, including stale per-instance data. That's why golden images often regenerate instance-specific files at boot.
- **Mistakes:** In Git Bash I tried `ssh root@...`. Amazon Linux refuses root logins ("Please login as the user ec2-user"), so the connection closed and my next commands ran on my laptop instead (`cd: /opt/balerica-bank: No such file or directory`). In EC2 Instance Connect I was logged in as `root`, so `whoami` printed `root`.
- **Cleanup (Sun 1 Nov 2026, about 10:45 ACDT):** AMI-launched instance `i-0fa6fc630cd34f507` terminated ✅, AMI `ami-0d4ff01d90546aa7d` deregistered ✅, snapshot `snap-0d9bc7af9ba2848f7` deleted ✅, source instance `i-09a4d6d2097ec92ed` terminated ✅ (about 11:07 ACDT). Order matters: the snapshot can only be deleted after the AMI that uses it is deregistered.

📸 **Screenshot : [`BAM_2.3 Connect`](lab_runs/BAM_2/BAM_2.3_ami_instance_connect_id_metadata.png)** |
📸 **Screenshot : [`BAM_2.3 Git Bash`](lab_runs/BAM_2/BAM_2.3_ami_instance_gitbash_id_metadata.png)** |
📸 **Screenshot : [`BAM_2.3 Bank Website`](lab_runs/BAM_2/BAM_2.3_ami_instance_bank_results.png)** |
📸 **Screenshot : [`BAM_2.3 Instance Terminated`](lab_runs/BAM_2/BAM_2.3_ami_instance_terminated.png)**

**What I learned:** an AMI is a pointer to an EBS snapshot plus launch metadata. The 8 GiB volume only needed 2 GiB of snapshot storage, because snapshots store only the blocks that are actually used. The AMI captures the disk (the installed bank, venv, compiled COBOL, `bank.db`, even the time zone setting). It doesn't capture the IAM role, the security group or the key pair, which are chosen again at launch.
