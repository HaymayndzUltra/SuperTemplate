#!/usr/bin/env python3
"""Prerequisite validation for the Security Review (SR) protocol."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

WORKSPACE_ROOT = Path(".artifacts/review-security")
RELATED_DIRECTORIES = [
    WORKSPACE_ROOT,
    Path(".artifacts/review-code"),
    Path(".artifacts/review-architecture"),
]
RELATED_SCRIPTS = [
    "scripts/validate_gate_SR_scans.py",
    "scripts/validate_gate_SR_controls.py",
    "scripts/validate_gate_SR_disposition.py",
    "scripts/run_protocol_SR_gates.py",
    "scripts/aggregate_evidence_SR.py",
]
ARTIFACT_TEMPLATES: Dict[str, str] = {
    ".artifacts/review-security/scope-register.json": json.dumps(
        {
            "assets": [],
            "regulatory_scope": [],
            "status": "pending",
        },
        indent=2,
    )
    + "\n",
    ".artifacts/review-security/risk-baseline-report.md": (
        "# Security Risk Baseline\n\n"
        "Document the current risk posture, unresolved vulnerabilities, and"
        " priority areas for the review.\n"
    ),
    ".artifacts/review-security/scan-results.json": json.dumps(
        {
            "summary": {"critical": 0, "high": 0, "medium": 0, "low": 0},
            "tools": [],
        },
        indent=2,
    )
    + "\n",
    ".artifacts/review-security/manual-assessment.md": (
        "# Manual Security Assessment\n\n"
        "Capture manual review findings, affected controls, and remediation"
        " notes.\n"
    ),
    ".artifacts/review-security/findings-register.csv": (
        "finding_id,severity,status,owner,notes\n"
    ),
    ".artifacts/review-security/disposition-record.md": (
        "# Security Review Disposition\n\n"
        "Record approval outcome, conditions, and risk acceptances.\n"
    ),
    ".artifacts/review-security/security-risk-log.csv": (
        "risk_id,severity,status,mitigation\n"
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
    artifacts: List[Dict[str, str]] = []

    for directory in RELATED_DIRECTORIES:
        directory.mkdir(parents=True, exist_ok=True)

    for path, payload in ARTIFACT_TEMPLATES.items():
        status = _ensure_file(Path(path), payload)
        artifacts.append({"artifact": path, "status": status})

    missing_scripts = _check_scripts(RELATED_SCRIPTS)
    report = {
        "protocol": "SR",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "workspace": str(WORKSPACE_ROOT),
        "artifacts": artifacts,
        "missing_scripts": missing_scripts,
        "status": "pass" if not missing_scripts else "warning",
    }

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
