#!/usr/bin/env python3
"""Gate 2 validator for Protocol 02: Recap & Approval Gate.

Ensures discovery recap was delivered, approval logged, and follow-ups tracked.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RECAP_PATH = Path(".artifacts/protocol-02/discovery-recap.md")
APPROVAL_LOG_PATH = Path(".artifacts/protocol-02/discovery-approval-log.json")
READY_SUMMARY_PATH = Path(".artifacts/protocol-02/ready-for-call-summary.md")

REQUIRED_APPROVAL_KEYS = {"status", "approved_at", "approver", "delivery_channel"}
APPROVED_STATUS = {"approved", "signed"}


def _read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"__error__": f"Invalid JSON: {exc}"}


def validate_recap() -> dict:
    issues: list[str] = []
    recap_sent = False
    approval_status = "unknown"

    if not RECAP_PATH.exists():
        issues.append(f"Missing discovery recap: {RECAP_PATH}")
    else:
        recap_content = RECAP_PATH.read_text(encoding="utf-8").lower()
        recap_sent = "sent on" in recap_content or "delivered" in recap_content
        if not recap_sent:
            issues.append("Discovery recap does not document send timestamp")
        if "pending" in recap_content and "approval" in recap_content:
            issues.append("Recap still marked pending approval")

    approval_payload = _read_json(APPROVAL_LOG_PATH)
    if not approval_payload:
        issues.append(f"Missing approval log: {APPROVAL_LOG_PATH}")
    elif "__error__" in approval_payload:
        issues.append(approval_payload["__error__"])
    else:
        missing_keys = REQUIRED_APPROVAL_KEYS.difference(approval_payload.keys())
        if missing_keys:
            issues.append(
                f"Approval log missing fields: {', '.join(sorted(missing_keys))}"
            )
        approval_status = str(approval_payload.get("status", "")).lower()
        if approval_status not in APPROVED_STATUS:
            issues.append(
                "Approval status must be one of: " + ", ".join(sorted(APPROVED_STATUS))
            )

    if READY_SUMMARY_PATH.exists():
        ready_status = ""
        for line in READY_SUMMARY_PATH.read_text(encoding="utf-8").splitlines():
            if line.lower().startswith("status:"):
                ready_status = line.split(":", 1)[-1].strip().lower()
                break
        if ready_status and ready_status != "pre_call_ready":
            issues.append(
                "Ready-for-call summary not marked as pre_call_ready before recap send"
            )

    status = "pass" if not issues else "fail"

    return {
        "status": status,
        "recap_sent": recap_sent,
        "approval_status": approval_status,
        "issues": issues,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Gate 2: Recap & Approval")
    _ = parser.parse_args(argv or sys.argv[1:])

    result = validate_recap()
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
