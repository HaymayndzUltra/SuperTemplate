#!/usr/bin/env python3
"""Prerequisite validation for the Code Review (CR) protocol.

This script prepares the evidence workspace, seeds placeholder artifacts when
necessary, and verifies that all automation hooks referenced by the protocol
are present. It enables pipelines to execute the protocol end-to-end even when
upstream systems have not yet produced their artefacts.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

WORKSPACE_ROOT = Path(".artifacts/review-code")
RELATED_DIRECTORIES = [
    WORKSPACE_ROOT,
    Path(".artifacts/review-security"),
    Path(".artifacts/review-architecture"),
]
RELATED_SCRIPTS = [
    "scripts/validate_gate_CR_standards.py",
    "scripts/validate_gate_CR_tests.py",
    "scripts/validate_gate_CR_feedback.py",
    "scripts/run_protocol_CR_gates.py",
    "scripts/aggregate_evidence_CR.py",
]
ARTIFACT_TEMPLATES: Dict[str, str] = {
    ".artifacts/review-code/context-checklist.json": json.dumps(
        {
            "status": "pending",
            "checks": [
                {"item": "pull-request-link", "status": "pending"},
                {"item": "task-reference", "status": "pending"},
                {"item": "coding-standards.md", "status": "pending"},
            ],
        },
        indent=2,
    )
    + "\n",
    ".artifacts/review-code/change-impact.md": (
        "# Change Impact Summary\n\n"
        "Populate this file with affected modules, risk assessment, and CI"
        " observations before running gate validators.\n"
    ),
    ".artifacts/review-code/design-issues.json": json.dumps([], indent=2) + "\n",
    ".artifacts/review-code/test-validation-report.json": json.dumps(
        {
            "tests": [],
            "coverage": {
                "statements": 0.0,
                "branches": 0.0,
                "threshold": 0.0,
            },
        },
        indent=2,
    )
    + "\n",
    ".artifacts/review-code/feedback-log.csv": (
        "comment_id,author,severity,status,notes\n"
    ),
    ".artifacts/review-code/decision-record.md": (
        "# Code Review Decision\n\n"
        "Summarise the approval outcome, conditions, and follow-up tasks here.\n"
    ),
    ".artifacts/review-security/security-risk-log.csv": (
        "risk_id,category,severity,status,mitigation\n"
    ),
    ".artifacts/review-architecture/architecture-review-findings.csv": (
        "finding_id,area,severity,status,notes\n"
    ),
}


def _ensure_file(path: Path, payload: str) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(payload, encoding="utf-8")
        return "created"
    return "exists"


def _check_scripts(scripts: List[str]) -> List[str]:
    missing: List[str] = []
    for script in scripts:
        if not Path(script).exists():
            missing.append(script)
    return missing


def main() -> int:
    actions: List[Dict[str, str]] = []

    for directory in RELATED_DIRECTORIES:
        directory.mkdir(parents=True, exist_ok=True)

    for path, payload in ARTIFACT_TEMPLATES.items():
        status = _ensure_file(Path(path), payload)
        actions.append({"artifact": path, "status": status})

    missing_scripts = _check_scripts(RELATED_SCRIPTS)

    report = {
        "protocol": "CR",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "workspace": str(WORKSPACE_ROOT),
        "artifacts": actions,
        "missing_scripts": missing_scripts,
        "status": "pass" if not missing_scripts else "warning",
    }

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
