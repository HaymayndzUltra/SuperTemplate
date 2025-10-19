#!/usr/bin/env python3
"""Configuration-driven protocol gate runner.

This prototype loads a YAML descriptor mapping validation steps for a protocol,
executes available scripts, captures results, and writes an evidence manifest
following ``documentation/evidence-manifest.schema.json``.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

import yaml

from gate_utils import load_manifest_data, write_manifest

CONFIG_DIR = Path("config/protocol_gates")
MANIFEST_ROOT = Path(".artifacts")


def _run_command(command: str) -> Dict[str, str]:
    try:
        completed = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
        )
        status = "pass"
        notes = completed.stdout.strip()
    except subprocess.CalledProcessError as exc:
        status = "fail"
        notes = (exc.stdout or "") + (exc.stderr or "")
    return {
        "command": command,
        "status": status,
        "notes": notes.strip(),
    }


def _load_protocol_config(protocol_id: str, config_dir: Path) -> Dict[str, object]:
    config_path = config_dir / f"{protocol_id}.yaml"
    if not config_path.exists():
        raise SystemExit(f"Missing gate config: {config_path}")
    return yaml.safe_load(config_path.read_text(encoding="utf-8"))


def _execute_protocol(protocol_id: str, config: Dict[str, object]) -> None:
    data = load_manifest_data(protocol_id)
    validators: List[dict] = []
    artifacts: List[dict] = []

    for validator in config.get("validators", []):
        command = validator["command"]
        result = _run_command(command)
        validators.append(
            {
                "name": validator.get("name", command),
                "command": command,
                "status": result["status"],
                "notes": result["notes"],
            }
        )

    for artifact in config.get("artifacts", []):
        artifacts.append(
            {
                "path": artifact.get("path"),
                "status": artifact.get("status", "pending"),
                "description": artifact.get("description", ""),
            }
        )

    manifest_dir = MANIFEST_ROOT / f"protocol-{protocol_id}"
    manifest_path = manifest_dir / "gate-manifest.json"
    write_manifest(manifest_path, data, artifacts, validators, notes=config.get("notes", ""))
    print(f"Manifest written to {manifest_path}")


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run protocol gate validations.")
    parser.add_argument("protocol", help="Protocol identifier (e.g., 01, 02)")
    parser.add_argument(
        "--config-dir",
        type=Path,
        default=CONFIG_DIR,
        help=f"Directory containing protocol gate configs (default: {CONFIG_DIR})",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    config = _load_protocol_config(args.protocol, args.config_dir)
    _execute_protocol(args.protocol, config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
