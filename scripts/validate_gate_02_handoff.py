#!/usr/bin/env python3
"""Gate 3 validator for Protocol 02: Protocol 03 Handoff Readiness.

Verifies that required artifacts are complete, approvals logged, and
no unresolved discovery blockers remain before initiating Protocol 03.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HANDOFF_ARTIFACTS = {
    "client-discovery-form": Path(".artifacts/protocol-02/client-discovery-form.md"),
    "scope-clarification": Path(".artifacts/protocol-02/scope-clarification.md"),
    "timeline-discussion": Path(".artifacts/protocol-02/timeline-discussion.md"),
    "communication-plan": Path(".artifacts/protocol-02/communication-plan.md"),
    "discovery-recap": Path(".artifacts/protocol-02/discovery-recap.md"),
}

ASSUMPTIONS_PATH = Path(".artifacts/protocol-02/assumptions-gaps.md")
APPROVAL_LOG_PATH = Path(".artifacts/protocol-02/discovery-approval-log.json")
HANDOFF_BLOCKERS_PATH = Path(".artifacts/protocol-02/handoff-blockers.md")

APPROVED_STATUS = {"approved", "signed"}


def _load_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").lower()


def _load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"__error__": f"Invalid JSON: {exc}"}


def validate_handoff() -> dict:
    """Validate handoff readiness to Protocol 03."""
    issues: list[str] = []

    # Ensure core artifacts exist
    missing = [label for label, path in HANDOFF_ARTIFACTS.items() if not path.exists()]
    if missing:
        issues.append("Missing artifacts: " + ", ".join(sorted(missing)))

    # Assumptions tracker must have no unresolved ASK CLIENT tags
    assumptions_content = _load_text(ASSUMPTIONS_PATH)
    outstanding = [
        line.strip()
        for line in assumptions_content.splitlines()
        if "ask client" in line.lower()
    ]
    if outstanding:
        issues.append("Outstanding ASK CLIENT items remain in assumptions-gaps.md")

    # Approval log must show approved status
    approval_payload = _load_json(APPROVAL_LOG_PATH)
    approval_status = "unknown"
    if not approval_payload:
        issues.append(f"Missing approval log: {APPROVAL_LOG_PATH}")
    elif "__error__" in approval_payload:
        issues.append(approval_payload["__error__"])
    else:
        approval_status = str(approval_payload.get("status", ""))
        if approval_status.lower() not in APPROVED_STATUS:
            issues.append(
                "Approval log status must be one of: " + ", ".join(sorted(APPROVED_STATUS))
            )

    # No open handoff blockers
    if HANDOFF_BLOCKERS_PATH.exists():
        blockers = [line for line in HANDOFF_BLOCKERS_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
        if blockers:
            issues.append("handoff-blockers.md contains unresolved items")

    status = "pass" if not issues else "fail"

    return {
        "status": status,
        "approval_status": approval_status,
        "outstanding_questions": outstanding,
        "issues": issues,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Gate 3: Protocol 03 Handoff Readiness")
    _ = parser.parse_args(argv or sys.argv[1:])

    result = validate_handoff()
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
