#!/usr/bin/env python3
"""Balerica AI x Vice City: GTA 6-themed synthetic incidents.

Fires themed test incidents through the existing incident.py coordinator
(Jira ticket first, Slack alert second). Every scenario is SYNTHETIC and
contains no real customer data.

Wanted level -> severity:
    1 star  -> INFO       (Jira only; Slack filters it at SLACK_ALERT_SEVERITY=ERROR)
    2 stars -> WARNING    (Jira only at ERROR threshold)
    3 stars -> ERROR      (Jira + Slack)
    4-5     -> CRITICAL   (Jira + Slack)

Settings: loaded from .env2 first (override with --env-file). Values in .env2
win; anything .env2 leaves out falls back to .env.

Usage (run from /opt/balerica-bank, venv active):
    python3 gta6_incidents.py --list
    python3 gta6_incidents.py --dry-run --scenario vice-bank-heist
    python3 gta6_incidents.py --scenario vice-bank-heist
    python3 gta6_incidents.py --random
    python3 gta6_incidents.py --all --yes          # creates one Jira issue per scenario
    python3 gta6_incidents.py --scenario cobol-core-down --run-id 002   # new incident
"""
import argparse
import json
import os
import random
import sys
from pathlib import Path

# Settings for this script live in .env2 (separate from the main .env).
# Any variable missing from .env2 falls back to the value in .env.
ENV_FILE = ".env2"

# Each scenario has a STABLE incident ID (GTA6-<CODE>-<run_id>).
# Re-running the same scenario + run-id reuses the same Jira ticket.
SCENARIOS = {
    "vice-bank-heist": {
        "code": "HEIST",
        "agent": "heist_watch.py",
        "stars": 5,
        "message": "Vice City branch vault breach: vault door opened outside business hours",
        "evidence": "Synthetic: vault sensor OPEN at 03:12, no scheduled access, 2 badges unrecognised",
        "recommendation": "Lock down branch access, review badge logs and CCTV, freeze vault-linked accounts",
    },
    "leonida-atm-drain": {
        "code": "ATM",
        "agent": "atm_monitor.py",
        "stars": 4,
        "message": "Leonida Keys ATMs dispensing cash far above normal rate",
        "evidence": "Synthetic: 6 ATMs, 412 withdrawals in 10 minutes (baseline 20)",
        "recommendation": "Disable affected ATMs remotely and check for jackpotting malware",
    },
    "offshore-wire-spree": {
        "code": "SWIFT",
        "agent": "swift_watch.py",
        "stars": 4,
        "message": "Burst of SWIFT MT103 wires to new offshore beneficiaries",
        "evidence": "Synthetic: 37 MT103 messages in 5 minutes, all to first-time beneficiaries",
        "recommendation": "Hold outbound wires, verify initiating operator, contact compliance",
    },
    "card-club-spree": {
        "code": "CARD",
        "agent": "fraud_watch.py",
        "stars": 4,
        "message": "Same card used at multiple Vice City nightclubs within minutes",
        "evidence": "Synthetic: 9 card-present transactions at 9 venues in 14 minutes",
        "recommendation": "Block card, notify cardholder, flag merchants for review",
    },
    "scanner-flood": {
        "code": "DDOS",
        "agent": "telemetry.py",
        "stars": 4,
        "message": "Request flood on the FastAPI front office from thousands of IPs",
        "evidence": "Synthetic: 18k req/s on /docs and /, normal is 40 req/s",
        "recommendation": "Enable rate limiting / WAF rules and check security group exposure",
    },
    "cobol-core-down": {
        "code": "COBOL",
        "agent": "cobol.py",
        "stars": 3,
        "message": "Port Gellhorn branch: COBOL core cannot open accounts.dat (rc=12)",
        "evidence": "Synthetic: account_lookup returned FILE-STATUS=35, return code 12",
        "recommendation": "Confirm working directory is /opt/balerica-bank and data/accounts.dat exists",
    },
    "rush-hour-latency": {
        "code": "LATENCY",
        "agent": "health.py",
        "stars": 3,
        "message": "Vice City rush hour: API p95 latency above 3 seconds",
        "evidence": "Synthetic: p95 3.4s for 10 minutes, threshold 800ms",
        "recommendation": "Check uvicorn workers, CPU credits and slow COBOL subprocess calls",
    },
    "safehouse-disk-full": {
        "code": "DISK",
        "agent": "health.py",
        "stars": 3,
        "message": "Safehouse stash overflowing: EC2 root disk at 95 percent",
        "evidence": "Synthetic: / at 95% used, logs/ grew 3 GB in 1 hour",
        "recommendation": "Rotate and compress logs, check for runaway writers, extend EBS volume",
    },
    "pay-n-spray-ledger": {
        "code": "LEDGER",
        "agent": "auditor.py",
        "stars": 3,
        "message": "Ledger repaint: SQLite balances do not match fixed-width accounts.dat",
        "evidence": "Synthetic: 3 accounts differ, largest gap 250.00 USD",
        "recommendation": "Freeze postings, re-run reconciliation, compare payments.dat to bank.db",
    },
    "inside-crew-login": {
        "code": "LOGIN",
        "agent": "analyze_logs.py",
        "stars": 3,
        "message": "Staff account logged in from Leonida and offshore within 5 minutes",
        "evidence": "Synthetic: impossible-travel alert for operator account OPS-117",
        "recommendation": "Force password reset, revoke sessions, review recent actions",
    },
    "patrol-spotted": {
        "code": "AUTHFAIL",
        "agent": "analyze_logs.py",
        "stars": 2,
        "message": "Patrol spotted: failed logins rising on the admin page",
        "evidence": "Synthetic: 45 failed logins in 15 minutes from 3 IPs",
        "recommendation": "Watch the trend; block IPs if it continues",
    },
    "radio-check": {
        "code": "RADIO",
        "agent": "health.py",
        "stars": 1,
        "message": "Radio check: nightly health check completed with notes",
        "evidence": "Synthetic: all services up, one slow response logged",
        "recommendation": "No action needed; informational only",
    },
}


def stars_to_severity(stars: int) -> str:
    if stars >= 4:
        return "CRITICAL"
    if stars == 3:
        return "ERROR"
    if stars == 2:
        return "WARNING"
    return "INFO"


def wanted_bar(stars: int) -> str:
    return "★" * stars + "☆" * (5 - stars)


def build(name: str, run_id: str) -> dict:
    s = SCENARIOS[name]
    return {
        "agent": s["agent"],
        "severity": stars_to_severity(s["stars"]),
        "message": f"[GTA6 {wanted_bar(s['stars'])}] {s['message']}",
        "incident_id": f"GTA6-{s['code']}-{run_id}",
        "evidence": s["evidence"],
        "recommendation": s["recommendation"],
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Balerica AI x Vice City synthetic incidents")
    pick = p.add_mutually_exclusive_group()
    pick.add_argument("--scenario", action="append", choices=sorted(SCENARIOS),
                      help="Scenario to fire (repeatable)")
    pick.add_argument("--random", action="store_true", help="Fire one random scenario")
    pick.add_argument("--all", action="store_true", help="Fire every scenario (needs --yes)")
    pick.add_argument("--list", action="store_true", help="List scenarios and exit")
    p.add_argument("--dry-run", action="store_true", help="Show what would be sent; no API calls")
    p.add_argument("--run-id", default="001",
                   help="Suffix for incident IDs (default 001). Change it to open a NEW incident.")
    p.add_argument("--yes", action="store_true", help="Confirm --all (creates many Jira issues)")
    p.add_argument("--env-file", default=ENV_FILE,
                   help=f"Settings file to load first (default {ENV_FILE}); its values win over .env")
    args = p.parse_args()

    if args.list or not (args.scenario or args.random or args.all):
        print(f"{'SCENARIO':<22} {'WANTED':<7} {'SEVERITY':<9} AGENT")
        for name, s in SCENARIOS.items():
            print(f"{name:<22} {wanted_bar(s['stars'])}  {stars_to_severity(s['stars']):<9} {s['agent']}")
        if not args.list:
            print("\nPick one: --scenario NAME | --random | --all --yes  (add --dry-run to preview)")
        return 0

    if not args.run_id.replace("-", "").isalnum():
        print("run-id must be letters, numbers or dashes")
        return 2

    names = sorted(SCENARIOS) if args.all else (
        [random.choice(list(SCENARIOS))] if args.random else args.scenario)

    if args.all and not args.dry_run and not args.yes:
        print(f"--all will create up to {len(names)} Jira issues. Re-run with --yes to confirm.")
        return 2

    payloads = [build(n, args.run_id) for n in names]

    if args.dry_run:
        for n, pl in zip(names, payloads):
            print(f"--- {n} ---")
            print(json.dumps(pl, indent=2, ensure_ascii=False))
        print(f"No API calls made. A real run would load {args.env_file} first.")
        return 0

    # Load .env2 BEFORE importing incident/jira/slack: jira.py reads its settings
    # at import time. override=True makes .env2 win over anything already set.
    # incident.py then calls load_dotenv() for .env, which only fills in
    # variables that .env2 did NOT define (python-dotenv never overrides by default).
    env_path = Path(args.env_file)
    if not env_path.is_file():
        print(f"Settings file {env_path} not found. Create it (chmod 600) or pass --env-file.")
        return 2
    from dotenv import load_dotenv
    load_dotenv(env_path, override=True)
    print(f"Loaded {env_path} | Jira project: {os.getenv('JIRA_PROJECT_KEY', '?')} | "
          f"state DB: {os.getenv('INCIDENT_STATE_DB', 'data/incident_state.db')}")

    # Imported only for real runs, so --list and --dry-run work without any env file.
    from incident import report_incident

    failures = 0
    for n, pl in zip(names, payloads):
        try:
            result = report_incident(**pl)
            result["scenario"] = n
            result["severity"] = pl["severity"]
            print(json.dumps(result, indent=2, ensure_ascii=False))
            ok_status = {"sent", "already_sent"}
            if pl["severity"] in {"INFO", "WARNING"}:
                ok_status.add("filtered_or_disabled")  # below Slack threshold: expected
            if result["slack_status"] not in ok_status:
                failures += 1
        except Exception as exc:  # keep going; never print secrets
            failures += 1
            print(json.dumps({"scenario": n, "incident_id": pl["incident_id"],
                              "error": type(exc).__name__}, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
