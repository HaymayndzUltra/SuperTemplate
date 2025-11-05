#!/usr/bin/env python3
"""Prerequisite validation for Protocol 23 Script Governance."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

WORKSPACE_ROOT = Path(".artifacts/scripts")
RELATED_DIRECTORIES = [
    WORKSPACE_ROOT,
    Path(".artifacts/governance"),
    Path("scripts"),
]
RELATED_SCRIPTS = [
    "scripts/validate_gate_23_inventory.py",
    "scripts/validate_gate_23_static.py",
    "scripts/validate_gate_23_artifacts.py",
    "scripts/validate_gate_23_reporting.py",
    "scripts/aggregate_evidence_23.py",
    "scripts/validate_script_registry.py",
    "scripts/auto_register_scripts.py",
]
ARTIFACT_TEMPLATES: Dict[str, str] = {
    ".artifacts/scripts/script-index.json": json.dumps(
        {"scripts": [], "completeness": 0}, indent=2
    )
    + "\n",
    ".artifacts/scripts/inventory-validation-report.json": json.dumps(
        {"status": "pending", "coverage": 0}, indent=2
    )
    + "\n",
    ".artifacts/scripts/documentation-audit.csv": (
        "script,has_docstring,has_usage,has_examples,score\n"
    ),
    ".artifacts/scripts/static-analysis-report.json": json.dumps(
        {"findings": [], "blocker_count": 0}, indent=2
    )
    + "\n",
    ".artifacts/scripts/artifact-compliance-report.json": json.dumps(
        {"scripts": [], "compliance_score": 0}, indent=2
    )
    + "\n",
    ".artifacts/scripts/script-compliance.json": json.dumps(
        {"scorecard": {}, "status": "pending"}, indent=2
    )
    + "\n",
    ".artifacts/scripts/remediation-backlog.csv": (
        "script,issue,severity,owner,status\n"
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
        "protocol": "23",
        "protocol_name": "Script Governance",
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
