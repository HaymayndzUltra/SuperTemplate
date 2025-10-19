#!/usr/bin/env python3
"""Validate proposal structure for Protocol 01 artifacts."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict

REQUIRED_SECTIONS = [
    "Greeting",
    "Understanding",
    "Proposed Approach",
    "Deliverables & Timeline",
    "Collaboration Model",
    "Next Steps",
]

MIN_WORDS_PER_SECTION = 120


def parse_sections(markdown: str) -> Dict[str, str]:
    sections: Dict[str, str] = {}
    current_title: str | None = None
    current_lines: list[str] = []

    import re

    heading_pattern = re.compile(r'^#{1,6}\s+(.*)')

    for line in markdown.splitlines():
        match = heading_pattern.match(line)
        if match:
            if current_title is not None:
                sections[current_title] = "\n".join(current_lines).strip()
            current_title = match.group(1).strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_title is not None:
        sections[current_title] = "\n".join(current_lines).strip()
    return sections


def validate_sections(sections: Dict[str, str]) -> list[str]:
    errors: list[str] = []
    for required in REQUIRED_SECTIONS:
        if required not in sections:
            errors.append(f"Missing required section: {required}")
            continue
        word_count = len(sections[required].split())
        if word_count < MIN_WORDS_PER_SECTION:
            errors.append(
                f"Section '{required}' contains {word_count} words; minimum is {MIN_WORDS_PER_SECTION}."
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Protocol 01 proposal structure.")
    parser.add_argument("--input", required=True, help="Path to PROPOSAL.md")
    args = parser.parse_args()

    proposal_path = Path(args.input)
    if not proposal_path.exists():
        print(f"Input file not found: {proposal_path}", file=sys.stderr)
        return 1

    sections = parse_sections(proposal_path.read_text(encoding="utf-8"))
    errors = validate_sections(sections)

    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        return 1

    print("Proposal structure validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
