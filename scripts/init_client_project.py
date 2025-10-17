#!/usr/bin/env python3
"""High-level orchestrator entry point for initializing a client project."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import List

from scripts.analyze_brief import analyze_brief
from scripts.generate_protocol_sequence import (
    SCRIPT_REGISTRY_PATH,
    build_commands,
    load_registry,
)


def run_generate_from_brief(brief: Path, output_root: Path) -> None:
    command = [
        "python3",
        str(Path("scripts/generate_from_brief.py")),
        "--brief",
        str(brief),
        "--output-root",
        str(output_root),
        "--yes",
        "--force",
    ]
    subprocess.run(command, check=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Initialize project orchestration from a brief")
    parser.add_argument("--brief", default="PROJECT-BRIEF.md", help="Path to project brief")
    parser.add_argument("--analysis-output", default=".cursor/orchestration/analysis.json", help="Path to write analysis JSON")
    parser.add_argument("--commands-dir", default=".cursor/commands/generated", help="Directory for generated command files")
    parser.add_argument("--generate-scaffold", action="store_true", help="Generate project scaffold via generate_from_brief.py")
    parser.add_argument("--scaffold-output", default="../generated-projects", help="Output root for generated project scaffold")
    parser.add_argument("--summary", action="store_true", help="Print summary of generated artifacts")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    brief_path = Path(args.brief).resolve()
    if not brief_path.exists():
        raise FileNotFoundError(f"Brief not found: {brief_path}")

    analysis = analyze_brief(brief_path)
    analysis_output = Path(args.analysis_output)
    analysis_output.parent.mkdir(parents=True, exist_ok=True)
    analysis_output.write_text(analysis.to_json(), encoding="utf-8")

    registry = load_registry(SCRIPT_REGISTRY_PATH)
    commands_dir = Path(args.commands_dir)
    artifacts = build_commands(json.loads(analysis.to_json()), commands_dir, registry)

    scaffold_location: List[str] = []
    if args.generate_scaffold:
        output_root = Path(args.scaffold_output).resolve()
        output_root.mkdir(parents=True, exist_ok=True)
        run_generate_from_brief(brief_path, output_root)
        scaffold_location.append(str(output_root))

    if args.summary:
        summary = {
            "analysis": str(analysis_output),
            "commands": [str(commands_dir / artifact.filename) for artifact in artifacts],
            "scaffold": scaffold_location,
        }
        print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
