#!/usr/bin/env python3
"""Prerequisite validation for Protocol 22 Implementation Retrospective."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

WORKSPACE_ROOT = Path(".artifacts/protocol-22")
RELATED_DIRECTORIES = [
    WORKSPACE_ROOT,
    Path(".artifacts/retrospective"),
    Path(".artifacts/improvement"),
]
RELATED_SCRIPTS = [
    "scripts/validate_gate_22_participation.py",
    "scripts/validate_gate_22_action_plan.py",
    "scripts/validate_gate_22_integration.py",
    "scripts/aggregate_evidence_22.py",
]
ARTIFACT_TEMPLATES: Dict[str, str] = {
    ".artifacts/protocol-22/session-notes.md": (
        "# Retrospective Session Notes\n\n## Attendees\n\nSession pending.\n"
    ),
    ".artifacts/protocol-22/theme-matrix.csv": (
        "theme,evidence_count,priority,status\n"
    ),
    ".artifacts/protocol-22/action-register.csv": (
        "action,owner,due_date,protocol,priority,status\n"
    ),
    ".artifacts/protocol-22/integration-confirmation-log.json": json.dumps(
        {"actions": [], "acknowledgements": []}, indent=2
    )
    + "\n",
    ".artifacts/protocol-22/improvement-plan.md": (
        "# Continuous Improvement Plan\n\n## Actions\n\nPlanning pending.\n"
    ),
    ".artifacts/protocol-22/lessons-learned.json": json.dumps(
        {"wins": [], "challenges": [], "recommendations": []}, indent=2
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
        "protocol": "22",
        "protocol_name": "Implementation Retrospective",
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
