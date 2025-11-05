#!/usr/bin/env python3
"""Prerequisite validation for Protocol 20 Project Closure & Handover."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

WORKSPACE_ROOT = Path(".artifacts/protocol-20")
RELATED_DIRECTORIES = [
    WORKSPACE_ROOT,
    Path(".artifacts/closure"),
    Path(".artifacts/handover"),
]
RELATED_SCRIPTS = [
    "scripts/validate_gate_20_deliverables.py",
    "scripts/validate_gate_20_handover.py",
    "scripts/validate_gate_20_governance.py",
    "scripts/aggregate_evidence_20.py",
]
ARTIFACT_TEMPLATES: Dict[str, str] = {
    ".artifacts/protocol-20/deliverable-audit-log.csv": (
        "deliverable,status,owner,acceptance_date\n"
    ),
    ".artifacts/protocol-20/PROJECT-DELIVERABLE-REGISTER.xlsx": (
        "# Placeholder for Excel file\n"
    ),
    ".artifacts/protocol-20/operational-handover-record.json": json.dumps(
        {"services": [], "slas": [], "escalation_paths": []}, indent=2
    )
    + "\n",
    ".artifacts/protocol-20/governance-closure-report.json": json.dumps(
        {"tasks": [], "archives": [], "status": "pending"}, indent=2
    )
    + "\n",
    ".artifacts/protocol-20/stakeholder-acceptance.md": (
        "# Stakeholder Acceptance\n\n## Sign-offs\n\nAwaiting approvals.\n"
    ),
    ".artifacts/protocol-20/financial-closure-summary.json": json.dumps(
        {"budget": 0, "actual": 0, "variance": 0}, indent=2
    )
    + "\n",
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
        "protocol": "20",
        "protocol_name": "Project Closure & Handover",
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
