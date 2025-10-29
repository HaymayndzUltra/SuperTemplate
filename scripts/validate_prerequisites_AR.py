#!/usr/bin/env python3
"""Prerequisite validation for the Architecture Review (AR) protocol."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

WORKSPACE_ROOT = Path(".artifacts/review-architecture")
RELATED_DIRECTORIES = [
    WORKSPACE_ROOT,
    Path(".artifacts/review-code"),
    Path(".artifacts/review-security"),
]
RELATED_SCRIPTS = [
    "scripts/validate_gate_AR_structure.py",
    "scripts/validate_gate_AR_quality.py",
    "scripts/validate_gate_AR_traceability.py",
    "scripts/run_protocol_AR_gates.py",
    "scripts/aggregate_evidence_AR.py",
]
ARTIFACT_TEMPLATES: Dict[str, str] = {
    ".artifacts/review-architecture/input-validation.json": json.dumps(
        {
            "artifacts": [],
            "status": "pending",
        },
        indent=2,
    )
    + "\n",
    ".artifacts/review-architecture/quality-attribute-matrix.csv": (
        "attribute,priority,acceptance_criteria,status\n"
    ),
    ".artifacts/review-architecture/boundary-analysis.md": (
        "# Modular Boundary Analysis\n\n"
        "Document boundary checks, coupling observations, and remediation"
        " items.\n"
    ),
    ".artifacts/review-architecture/quality-scenarios.json": json.dumps(
        {
            "scenarios": [],
        },
        indent=2,
    )
    + "\n",
    ".artifacts/review-architecture/findings-register.csv": (
        "finding_id,severity,owner,status,notes\n"
    ),
    ".artifacts/review-architecture/decision-record.md": (
        "# Architecture Review Decision\n\n"
        "Record the approval decision, conditions, and follow-up actions.\n"
    ),
    ".artifacts/review-architecture/architecture-review-findings.csv": (
        "finding_id,category,severity,status,notes\n"
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
        "protocol": "AR",
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
