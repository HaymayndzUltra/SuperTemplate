#!/usr/bin/env python3
"""Prerequisite validation for Protocol 19 Documentation & Knowledge Transfer."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

WORKSPACE_ROOT = Path(".artifacts/protocol-19")
RELATED_DIRECTORIES = [
    WORKSPACE_ROOT,
    Path(".artifacts/documentation"),
    Path(".artifacts/knowledge-transfer"),
]
RELATED_SCRIPTS = [
    "scripts/validate_gate_19_completeness.py",
    "scripts/validate_gate_19_enablement.py",
    "scripts/validate_gate_19_publication.py",
    "scripts/aggregate_evidence_19.py",
]
ARTIFACT_TEMPLATES: Dict[str, str] = {
    ".artifacts/protocol-19/documentation-plan.json": json.dumps(
        {"personas": [], "deliverables": [], "status": "pending"}, indent=2
    )
    + "\n",
    ".artifacts/protocol-19/review-tracker.csv": (
        "deliverable,reviewer,status,feedback\n"
    ),
    ".artifacts/protocol-19/draft-index.json": json.dumps(
        {"drafts": [], "completion": 0}, indent=2
    )
    + "\n",
    ".artifacts/protocol-19/enablement-summary.md": (
        "# Knowledge Transfer Enablement Summary\n\n## Sessions\n\nScheduling pending.\n"
    ),
    ".artifacts/protocol-19/knowledge-gap-log.json": json.dumps(
        {"gaps": [], "critical_questions": []}, indent=2
    )
    + "\n",
    ".artifacts/protocol-19/publication-manifest.json": json.dumps(
        {"documents": [], "accessibility": "pending"}, indent=2
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
        "protocol": "19",
        "protocol_name": "Documentation & Knowledge Transfer",
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
