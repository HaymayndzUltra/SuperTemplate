#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
from typing import Dict, List, Tuple

WORKFLOWS_DIR = os.path.join("docs", "workflows")
REQUIRED_SECTIONS = [
    "## Overview",
    "## Prerequisites",
    "## Steps",
    "## Evidence",
    "## Failure Modes",
    "## Overall Acceptance",
]

FRONTMATTER_REQUIRED_KEYS = [
    "title",
    "phase",
    "triggers",
    "scope",
    "inputs",
    "outputs",
    "artifacts",
    "gates",
    "owner",
]

YAML_START = re.compile(r"^---\s*$")
YAML_END = re.compile(r"^---\s*$")


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def find_markdown_files(root: str) -> List[str]:
    out: List[str] = []
    for base, _dirs, files in os.walk(root):
        for name in files:
            if name.endswith(".md"):
                out.append(os.path.join(base, name))
    return sorted(out)


def parse_frontmatter(text: str) -> Tuple[Dict, int]:
    lines = text.splitlines()
    if not lines or not YAML_START.match(lines[0]):
        return {}, 0
    # collect until next ---
    fm_lines: List[str] = []
    end_idx = 1
    for i in range(1, len(lines)):
        if YAML_END.match(lines[i]):
            end_idx = i
            break
        fm_lines.append(lines[i])
    # naive YAML parse (key: value, arrays with [] or - list)
    fm: Dict = {}
    buffer_key = None
    for raw in fm_lines:
        line = raw.rstrip()
        if not line:
            continue
        if line.strip().startswith("- ") and buffer_key:
            fm.setdefault(buffer_key, []).append(line.strip()[2:])
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            key = k.strip()
            value = v.strip()
            if value.startswith("[") and value.endswith("]"):
                inner = value[1:-1].strip()
                fm[key] = [s.strip().strip('"\'') for s in inner.split(",")] if inner else []
            else:
                fm[key] = value.strip('"\'')
            buffer_key = key
        else:
            buffer_key = None
    return fm, end_idx + 1


def check_frontmatter(fm: Dict, path: str) -> List[str]:
    errors: List[str] = []
    for key in FRONTMATTER_REQUIRED_KEYS:
        if key not in fm or fm.get(key) in (None, ""):
            errors.append(f"{path}: missing frontmatter key: {key}")
    # basic type sanity
    if "phase" in fm:
        try:
            int(str(fm["phase"]))
        except Exception:
            errors.append(f"{path}: phase must be an integer")
    return errors


def check_sections(text: str, path: str) -> List[str]:
    errors: List[str] = []
    for sec in REQUIRED_SECTIONS:
        if sec not in text:
            errors.append(f"{path}: missing required section: {sec}")
    return errors


def validate(args: argparse.Namespace) -> int:
    files = find_markdown_files(WORKFLOWS_DIR)
    if args.list:
        print(json.dumps(files, indent=2))
        return 0

    failures: List[str] = []
    for p in files:
        text = read_file(p)
        fm, body_idx = parse_frontmatter(text)
        if args.frontmatter or args.all:
            failures.extend(check_frontmatter(fm, p))
        if args.sections or args.all:
            failures.extend(check_sections(text, p))

    if args.dry_run:
        print("[DRY RUN] Validation completed.")
        print(f"Checked files: {len(files)}")
        if failures:
            print("Sample failures:")
            for e in failures[:10]:
                print(f"- {e}")
        return 0

    if failures:
        print("[VALIDATION FAILED]")
        for e in failures:
            print(f"- {e}")
        return 2

    print("[VALIDATION OK]")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Validate workflow docs for frontmatter and required sections.")
    parser.add_argument("--all", action="store_true", help="Run all validations")
    parser.add_argument("--frontmatter", action="store_true", help="Validate YAML frontmatter keys")
    parser.add_argument("--sections", action="store_true", help="Validate required sections presence")
    parser.add_argument("--list", action="store_true", help="List workflow markdown files")
    parser.add_argument("--dry-run", action="store_true", help="Do not fail; print sample results")
    args = parser.parse_args()
    if not (args.all or args.frontmatter or args.sections or args.list or args.dry_run):
        parser.print_help()
        return 0
    sys.exit(validate(args))


if __name__ == "__main__":
    main()