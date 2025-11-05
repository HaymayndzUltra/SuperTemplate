#\!/usr/bin/env python3
"""Aggregate evidence for Protocol 22 Implementation Retrospective."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List

PROTOCOL_ID = "22"
PROTOCOL_NAME = "Implementation Retrospective"

VALIDATOR_COMMANDS: List[Dict[str, object]] = [
    {
        "name": "gate_participation",
        "script": "scripts/validate_gate_22_participation.py",
        "args": [
            "--notes",
            ".artifacts/protocol-22/session-notes.md"
        ]
    },
    {
        "name": "gate_action_plan",
        "script": "scripts/validate_gate_22_action_plan.py",
        "args": [
            "--register",
            ".artifacts/protocol-22/action-register.csv"
        ]
    }
]

EXPECTED_ARTIFACTS = [
    {
        "path": ".artifacts/protocol-22/session-notes.md",
        "description": "Retrospective session documentation"
    },
    {
        "path": ".artifacts/protocol-22/action-register.csv",
        "description": "Action items and owners"
    },
    {
        "path": ".artifacts/protocol-22/lessons-learned.json",
        "description": "Lessons learned synthesis"
    }
]


def _run_validator(command: Dict[str, object]) -> Dict[str, str]:
    script = Path(command["script"])
    args = command.get("args", [])
    if isinstance(args, (str, Path)):
        args = [str(args)]
    cmd = [sys.executable, str(script), *map(str, args or [])]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        status = "pass" if result.returncode == 0 else "fail"
        notes = result.stdout.strip() or result.stderr.strip()
        return {
            "name": str(command["name"]),
            "command": " ".join(cmd),
            "status": status,
            "notes": notes[:500],
        }
    except subprocess.TimeoutExpired:
        return {
            "name": str(command["name"]),
            "command": " ".join(cmd),
            "status": "fail",
            "notes": "Validator timeout (30s exceeded)",
        }
    except FileNotFoundError:
        return {
            "name": str(command["name"]),
            "command": " ".join(cmd),
            "status": "skipped",
            "notes": "Validator script not found",
        }


def _collect_artifacts() -> List[Dict[str, str]]:
    artifacts: List[Dict[str, str]] = []
    for artifact in EXPECTED_ARTIFACTS:
        path = Path(artifact["path"])
        status = "exists" if path.exists() else "missing"
        size = path.stat().st_size if path.exists() else 0
        artifacts.append({
            "path": artifact["path"],
            "description": artifact["description"],
            "status": status,
            "size_bytes": size,
        })
    return artifacts


def aggregate(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    
    validator_results = [_run_validator(cmd) for cmd in VALIDATOR_COMMANDS]
    artifact_results = _collect_artifacts()
    
    manifest = {
        "protocol_id": PROTOCOL_ID,
        "protocol_name": PROTOCOL_NAME,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "validators": validator_results,
        "artifacts": artifact_results,
        "summary": {
            "validators_passed": sum(1 for v in validator_results if v["status"] == "pass"),
            "validators_total": len(validator_results),
            "artifacts_present": sum(1 for a in artifact_results if a["status"] == "exists"),
            "artifacts_total": len(artifact_results),
        },
    }
    
    manifest_path = output_dir / "evidence-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=f"Aggregate Protocol {PROTOCOL_ID} evidence")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(".artifacts/protocol-22"),
        help="Output directory for manifest",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    aggregate(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
