#!/usr/bin/env python3
"""Prerequisite validation for Protocol 21 Continuous Maintenance & Support Planning."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

WORKSPACE_ROOT = Path(".artifacts/protocol-21")
RELATED_DIRECTORIES = [
    WORKSPACE_ROOT,
    Path(".artifacts/maintenance"),
    Path(".artifacts/support"),
]
RELATED_SCRIPTS = [
    "scripts/validate_gate_21_backlog.py",
    "scripts/validate_gate_21_approvals.py",
    "scripts/validate_gate_21_governance.py",
    "scripts/aggregate_evidence_21.py",
]
ARTIFACT_TEMPLATES: Dict[str, str] = {
    ".artifacts/protocol-21/maintenance-backlog.csv": (
        "item,severity,owner,due_date,status\n"
    ),
    ".artifacts/protocol-21/technical-debt-log.json": json.dumps(
        {"items": [], "total_score": 0}, indent=2
    )
    + "\n",
    ".artifacts/protocol-21/support-plan.md": (
        "# Support Plan\n\n## Coverage\n\nPlanning pending.\n"
    ),
    ".artifacts/protocol-21/approval-log.csv": (
        "stakeholder,role,status,approval_date,comments\n"
    ),
    ".artifacts/protocol-21/governance-cadence-checklist.json": json.dumps(
        {"reporting": "pending", "dashboards": "pending", "alerts": "pending"}, indent=2
    )
    + "\n",
    ".artifacts/protocol-21/automation-candidates.json": json.dumps(
        {"candidates": [], "prioritization": "pending"}, indent=2
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
        "protocol": "21",
        "protocol_name": "Continuous Maintenance & Support Planning",
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
