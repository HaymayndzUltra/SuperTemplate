#!/usr/bin/env python3
"""Gate 1 validator for Protocol 02: Post-Call Data Capture.

Checks that post-call artifacts are present and updated with required details.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

POST_CALL_ARTIFACTS = {
    "client-discovery-form": Path(".artifacts/protocol-02/client-discovery-form.md"),
    "scope-clarification": Path(".artifacts/protocol-02/scope-clarification.md"),
    "integration-inventory": Path(".artifacts/protocol-02/integration-inventory.md"),
    "timeline-discussion": Path(".artifacts/protocol-02/timeline-discussion.md"),
    "communication-plan": Path(".artifacts/protocol-02/communication-plan.md"),
}

ASSUMPTIONS_PATH = Path(".artifacts/protocol-02/assumptions-gaps.md")
FOLLOW_UP_MARKER = "follow-up"

REQUIRED_PATTERNS = {
    "client-discovery-form": [r"priority", r"owner", r"acceptance"],
    "scope-clarification": [r"stack|technology", r"constraint", r"integration"],
    "integration-inventory": [r"system", r"owner", r"risk"],
    "timeline-discussion": [r"milestone", r"checkpoint|decision", r"timeline|schedule"],
    "communication-plan": [r"cadence|frequency", r"tool|channel", r"escalation|sla"],
}


def _load_content(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").lower()


def validate_data_capture(threshold: float = 0.95) -> dict:
    """Validate that post-call artifacts are updated and cohesive."""
    coverage_checks = []
    issues: list[str] = []

    for key, path in POST_CALL_ARTIFACTS.items():
        content = _load_content(path)
        if not content:
            issues.append(f"Missing artifact: {path}")
            coverage_checks.append(False)
            continue

        patterns = REQUIRED_PATTERNS[key]
        matched = [bool(re.search(pattern, content)) for pattern in patterns]
        if not all(matched):
            missing_tokens = ", ".join(
                token for token, ok in zip(patterns, matched) if not ok
            )
            issues.append(f"{key.replace('-', ' ').title()} missing: {missing_tokens}")
            coverage_checks.append(False)
        else:
            coverage_checks.append(True)

    coverage_score = sum(coverage_checks) / len(POST_CALL_ARTIFACTS)

    # Ensure outstanding assumptions are tagged with follow-up owner
    follow_up_compliance = 1.0
    if ASSUMPTIONS_PATH.exists():
        content = ASSUMPTIONS_PATH.read_text(encoding="utf-8").lower()
        if FOLLOW_UP_MARKER in content:
            lines = [line for line in content.splitlines() if line.strip()]
            flagged = [line for line in lines if FOLLOW_UP_MARKER in line]
            valid = [line for line in flagged if "owner" in line and "due" in line]
            follow_up_compliance = len(valid) / len(flagged) if flagged else 1.0
            if follow_up_compliance < 1.0:
                issues.append(
                    "Not all follow-up items in assumptions-gaps.md specify owner and due date"
                )

    status = (
        "pass"
        if coverage_score >= threshold and follow_up_compliance >= threshold
        else "fail"
    )

    return {
        "status": status,
        "data_capture_score": round(coverage_score, 3),
        "follow_up_compliance": round(follow_up_compliance, 3),
        "issues": issues,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Gate 1: Post-Call Data Capture")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.95,
        help="Minimum coverage score required (default: 0.95)",
    )
    args = parser.parse_args(argv or sys.argv[1:])

    result = validate_data_capture(args.threshold)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
