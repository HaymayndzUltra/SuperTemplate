#!/usr/bin/env python3
"""Validate PRD gate artifacts before proceeding with generation."""
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys

REQUIRED_SECTIONS = [
    "## 1. Overview",
    "## 2. Functional Specifications",
    "## 3. Technical Specifications",
    "## 4. Out of Scope",
]


class ValidationError(Exception):
    pass


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        raise ValidationError("PRD is missing required YAML front matter for sign-off metadata.")
    end = text.find("\n---", 3)
    if end == -1:
        raise ValidationError("Front matter terminator not found (expected closing ---).")
    block = text[3:end].strip().splitlines()
    metadata: dict[str, str] = {}
    for raw in block:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    body = text[end + len("\n---"):]
    return metadata, body


def validate_timestamp(value: str) -> None:
    candidate = value.replace("Z", "+00:00")
    try:
        datetime.fromisoformat(candidate)
    except ValueError as exc:
        raise ValidationError(f"Invalid ISO-8601 timestamp for sign-off: {value}") from exc


def validate_metadata(metadata: dict[str, str], stage: str) -> None:
    if metadata.get("signoff_stage") != stage:
        raise ValidationError(f"Expected signoff_stage '{stage}', found '{metadata.get('signoff_stage')}'.")
    approver = metadata.get("signoff_approver", "")
    if not approver or approver.strip().lower() in {"", "tbd", "todo", "pending"}:
        raise ValidationError("signoff_approver must be populated with the approving agent or user.")
    timestamp = metadata.get("signoff_timestamp")
    if not timestamp:
        raise ValidationError("signoff_timestamp is required in the PRD front matter.")
    validate_timestamp(timestamp)


def validate_sections(body: str) -> None:
    for section in REQUIRED_SECTIONS:
        if section not in body:
            raise ValidationError(f"PRD is missing required section: {section}")


def validate_architecture(path: Path) -> None:
    if not path.exists():
        raise ValidationError(f"Architecture summary missing: {path}")
    text = path.read_text(encoding="utf-8", errors="ignore")
    required_snippets = ["# Architecture Summary", "## Primary Components", "## Integration Flows"]
    for snippet in required_snippets:
        if snippet not in text:
            raise ValidationError(f"Architecture summary missing required content: {snippet}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate PRD sign-off metadata and supporting architecture notes.")
    parser.add_argument("--prd", required=True)
    parser.add_argument("--architecture")
    parser.add_argument("--required-stage", default="PRD + Architecture OK")
    parser.add_argument("--output", help="Optional JSON output path for validation result")
    args = parser.parse_args()

    prd_path = Path(args.prd)
    if not prd_path.exists():
        raise SystemExit("PRD.md not found; run PRD generation before continuing.")
    text = prd_path.read_text(encoding="utf-8", errors="ignore")

    metadata, body = parse_front_matter(text)
    validate_metadata(metadata, args.required_stage)
    validate_sections(body)

    if args.architecture:
        validate_architecture(Path(args.architecture))

    # Emit success message
    print("PRD gate validation passed.")

    # Optionally write a minimal JSON result if an output path is provided
    if args.output:
        out_path = Path(args.output)
        try:
            out_path.parent.mkdir(parents=True, exist_ok=True)
        except Exception:
            pass
        out_path.write_text('{"status": "passed", "required_stage": "' + args.required_stage + '"}', encoding="utf-8")


if __name__ == "__main__":
    try:
        main()
    except ValidationError as exc:
        print(f"[PRD Gate] {exc}", file=sys.stderr)
        raise SystemExit(1)
