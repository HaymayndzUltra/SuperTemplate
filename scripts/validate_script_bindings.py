#!/usr/bin/env python3
"""Validate automation script bindings for unified protocols."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List

SCRIPT_PATTERN = re.compile(r"\{SCRIPT:\s*([^}]+)\}")


def load_registry(path: Path) -> Dict[str, Dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Script registry not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def extract_scripts_from_markdown(path: Path) -> List[str]:
    content = path.read_text(encoding="utf-8")
    return [match.strip() for match in SCRIPT_PATTERN.findall(content)]


def validate_script_path(script: str) -> bool:
    command = script.split()[0]
    return Path(command).exists()


def validate_registry(registry: Dict[str, Dict[str, str]]) -> List[Dict[str, str]]:
    issues: List[Dict[str, str]] = []
    for phase, scripts in registry.items():
        for name, script in scripts.items():
            if not validate_script_path(script):
                issues.append({
                    "severity": "critical",
                    "phase": phase,
                    "script": script,
                    "message": f"Registry entry '{name}' points to missing script: {script}",
                })
    return issues


def validate_markdown_scripts(markdown_files: List[Path]) -> List[Dict[str, str]]:
    issues: List[Dict[str, str]] = []
    for path in markdown_files:
        for script in extract_scripts_from_markdown(path):
            if not validate_script_path(script):
                issues.append({
                    "severity": "warning",
                    "file": str(path),
                    "script": script,
                    "message": f"Script reference missing executable: {script}",
                })
    return issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate automation script bindings")
    parser.add_argument("--registry", default="scripts/script-registry.json", help="Path to script registry JSON")
    parser.add_argument("--protocol-dir", default="unified_workflow/phases", help="Directory containing protocol markdown files")
    parser.add_argument("--commands-dir", default=".cursor/commands/generated", help="Directory containing generated command files")
    parser.add_argument("--summary", action="store_true", help="Print summary JSON")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    registry_path = Path(args.registry)
    protocol_dir = Path(args.protocol_dir)
    commands_dir = Path(args.commands_dir)

    registry = load_registry(registry_path)
    issues = validate_registry(registry)

    markdown_files: List[Path] = []
    if protocol_dir.exists():
        markdown_files.extend(protocol_dir.glob("*.md"))
    if commands_dir.exists():
        markdown_files.extend(commands_dir.glob("*.md"))

    issues.extend(validate_markdown_scripts(markdown_files))

    summary = {
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "checked_files": [str(path) for path in markdown_files],
    }

    if args.summary or summary["status"] == "fail":
        print(json.dumps(summary, indent=2))

    if issues:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
