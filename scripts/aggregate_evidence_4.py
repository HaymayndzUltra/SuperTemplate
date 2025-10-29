#!/usr/bin/env python3
"""Aggregate evidence for Protocol 12 Quality Audit (Gate 4)."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from gate_utils import ManifestData, load_manifest_data, write_manifest

PROTOCOL_ID = "12"
VALIDATOR_COMMANDS: List[Dict[str, object]] = [
    {
        "name": "gate_pre_audit",
        "script": "scripts/validate_gate_4_pre_audit.py",
        "args": ["--threshold", "0.80"],
    },
    {
        "name": "gate_reporting",
        "script": "scripts/validate_gate_4_reporting.py",
        "args": ["--threshold", "0.95"],
    },
]
REFERENCE_SCRIPTS = [
    "scripts/validate_prerequisites_4.py",
    "scripts/validate_gate_4_pre_audit.py",
    "scripts/validate_gate_4_reporting.py",
    "scripts/aggregate_evidence_4.py",
    "scripts/run_protocol_4_gates.py",
]
EXPECTED_ARTIFACTS = [
    {
        "path": ".artifacts/quality-audit/ci-test-results.json",
        "description": "CI test workflow summary",
    },
    {
        "path": ".artifacts/quality-audit/ci-lint-results.json",
        "description": "CI lint workflow summary",
    },
    {
        "path": ".artifacts/quality-audit/ci-workflow-log.txt",
        "description": "Combined CI workflow log",
    },
    {
        "path": ".artifacts/quality-audit/coverage-report.json",
        "description": "Aggregated coverage metrics",
    },
    {
        "path": ".artifacts/quality-audit/coverage-metadata.yaml",
        "description": "Coverage metadata snapshot",
    },
    {
        "path": ".artifacts/quality-audit/change-context.json",
        "description": "Git change context snapshot",
    },
    {
        "path": ".artifacts/quality-audit/mode-resolution.json",
        "description": "Router mode resolution evidence",
    },
    {
        "path": ".artifacts/quality-audit/protocol-manifest.json",
        "description": "Specialized protocol manifest",
    },
    {
        "path": ".artifacts/quality-audit/execution-log.md",
        "description": "Specialized protocol execution log",
    },
    {
        "path": ".artifacts/quality-audit/audit-findings.json",
        "description": "Consolidated audit findings",
    },
    {
        "path": ".artifacts/quality-audit/finding-summary.csv",
        "description": "Findings severity summary",
    },
    {
        "path": ".artifacts/quality-audit/quality-audit-manifest.json",
        "description": "Quality audit package manifest",
    },
    {
        "path": ".artifacts/quality-audit/QUALITY-AUDIT-PACKAGE.zip",
        "description": "Packaged audit deliverable",
    },
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
        try:
            parsed = json.loads(result.stdout)
            status = parsed.get("status", status)
            notes = parsed.get("notes", notes)
        except json.JSONDecodeError:
            pass
        return {
            "name": str(command["name"]),
            "command": " ".join(cmd),
            "status": status,
            "notes": notes,
        }
    except subprocess.TimeoutExpired:
        return {
            "name": str(command["name"]),
            "command": " ".join(cmd),
            "status": "fail",
            "notes": "Validator timeout",
        }
    except FileNotFoundError:
        return {
            "name": str(command["name"]),
            "command": " ".join(cmd),
            "status": "fail",
            "notes": "Validator script missing",
        }


def _collect_artifacts() -> List[Dict[str, str]]:
    artifacts: List[Dict[str, str]] = []
    for artifact in EXPECTED_ARTIFACTS:
        path = Path(artifact["path"])
        status = "generated" if path.exists() else "missing"
        artifacts.append(
            {
                "path": artifact["path"],
                "description": artifact["description"],
                "status": status,
            }
        )
    return artifacts


def _build_manifest_data() -> ManifestData:
    data = load_manifest_data(PROTOCOL_ID)
    referenced = sorted(set(data.referenced_scripts + REFERENCE_SCRIPTS))
    missing = [script for script in referenced if not Path(script).exists()]
    coverage = 1.0
    if referenced:
        coverage = (len(referenced) - len(missing)) / len(referenced)
    return ManifestData(
        protocol_id=data.protocol_id,
        protocol_title=data.protocol_title,
        coverage=coverage,
        referenced_scripts=referenced,
        missing_scripts=missing,
    )


def aggregate(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    validator_results = [_run_validator(command) for command in VALIDATOR_COMMANDS]
    artifact_results = _collect_artifacts()
    data = _build_manifest_data()
    manifest_path = output_dir / "evidence-manifest.json"
    notes = f"Evidence aggregated at {datetime.utcnow().isoformat()}Z"
    write_manifest(manifest_path, data, artifact_results, validator_results, notes)
    print(f"Evidence manifest written to {manifest_path}")


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Aggregate Quality Audit evidence")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(".artifacts/quality-audit"),
        help="Output directory for manifest",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    aggregate(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
