#!/usr/bin/env python3
"""Aggregate evidence for the Security Review (SR) protocol."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from gate_utils import ManifestData, write_manifest

PROTOCOL_ID = "SR"
PROTOCOL_TITLE = "Security Review Validation"
VALIDATOR_COMMANDS: List[Dict[str, object]] = [
    {
        "name": "gate_scans",
        "script": "scripts/validate_gate_SR_scans.py",
        "args": ["--input", ".artifacts/review-security/scan-results.json"],
    },
    {
        "name": "gate_controls",
        "script": "scripts/validate_gate_SR_controls.py",
        "args": ["--report", ".artifacts/review-security/manual-assessment.md"],
    },
    {
        "name": "gate_disposition",
        "script": "scripts/validate_gate_SR_disposition.py",
        "args": ["--register", ".artifacts/review-security/findings-register.csv"],
    },
]
REFERENCE_SCRIPTS = [
    "scripts/validate_prerequisites_SR.py",
    "scripts/validate_gate_SR_scans.py",
    "scripts/validate_gate_SR_controls.py",
    "scripts/validate_gate_SR_disposition.py",
    "scripts/run_protocol_SR_gates.py",
]
EXPECTED_ARTIFACTS = [
    {
        "path": ".artifacts/review-security/scope-register.json",
        "description": "Defined security review scope and assets",
    },
    {
        "path": ".artifacts/review-security/risk-baseline-report.md",
        "description": "Risk baseline summary",
    },
    {
        "path": ".artifacts/review-security/scan-results.json",
        "description": "Aggregated automated scan results",
    },
    {
        "path": ".artifacts/review-security/manual-assessment.md",
        "description": "Manual security assessment notes",
    },
    {
        "path": ".artifacts/review-security/findings-register.csv",
        "description": "Consolidated findings register",
    },
    {
        "path": ".artifacts/review-security/disposition-record.md",
        "description": "Final disposition record",
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
    referenced = sorted(set(REFERENCE_SCRIPTS))
    missing = [script for script in referenced if not Path(script).exists()]
    coverage = 1.0
    if referenced:
        coverage = (len(referenced) - len(missing)) / len(referenced)
    return ManifestData(
        protocol_id=PROTOCOL_ID,
        protocol_title=PROTOCOL_TITLE,
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
    parser = argparse.ArgumentParser(description="Aggregate Security Review evidence")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(".artifacts/review-security"),
        help="Output directory for manifest",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    aggregate(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
