#!/usr/bin/env python3
"""Gate 0 validator for Protocol 02: Pre-Call Readiness Gate.

Ensures all pre-call artifacts exist and outstanding questions are tagged.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_ARTIFACTS = [
    (Path(".artifacts/protocol-02/discovery-brief.md"), "discovery brief"),
    (Path(".artifacts/protocol-02/assumptions-gaps.md"), "assumptions & gaps tracker"),
    (Path(".artifacts/protocol-02/question-bank.md"), "question bank"),
    (Path(".artifacts/protocol-02/integration-inventory.md"), "integration inventory"),
    (Path(".artifacts/protocol-02/call-agenda.md"), "call agenda"),
    (Path(".artifacts/protocol-02/ready-for-call-summary.md"), "ready-for-call summary"),
]

TAGGED_MARKER = "ASK CLIENT"


def validate_pre_call(threshold: float = 1.0) -> dict:
    """Validate pre-call readiness artifacts and tagging coverage."""
    issues: list[str] = []
    artifacts_present = 0

    for path, label in REQUIRED_ARTIFACTS:
        if path.exists():
            artifacts_present += 1
        else:
            issues.append(f"Missing {label}: {path}")

    readiness_score = artifacts_present / len(REQUIRED_ARTIFACTS)

    # Verify that outstanding questions are tagged in assumptions tracker
    tag_coverage = 0.0
    assumptions_path = REQUIRED_ARTIFACTS[1][0]
    if assumptions_path.exists():
        content = assumptions_path.read_text(encoding="utf-8")
        total_lines = sum(1 for line in content.splitlines() if line.strip())
        tagged_lines = sum(1 for line in content.splitlines() if TAGGED_MARKER in line)
        tag_coverage = tagged_lines / total_lines if total_lines else 1.0
        if tag_coverage < 1.0:
            issues.append(
                "Not all outstanding items tagged with 'ASK CLIENT' in assumptions-gaps.md"
            )
    else:
        tag_coverage = 0.0

    status = "pass" if readiness_score >= threshold and tag_coverage >= threshold else "fail"

    return {
        "status": status,
        "readiness_score": round(readiness_score, 3),
        "tag_coverage": round(tag_coverage, 3),
        "issues": issues,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Gate 0: Pre-Call Readiness")
    parser.add_argument(
        "--threshold",
        type=float,
        default=1.0,
        help="Minimum readiness score required (default: 1.0)",
    )
    args = parser.parse_args(argv or sys.argv[1:])

    result = validate_pre_call(args.threshold)
    print(json.dumps(result, indent=2))

    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
