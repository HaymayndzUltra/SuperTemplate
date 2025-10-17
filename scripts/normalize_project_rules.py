#!/usr/bin/env python3
"""
Normalize frontmatter for project rules under .cursor/rules/project-rules/**.mdc
Rules:
- description: human guidance text; remove TAGS/TRIGGERS/SCOPE patterns
- globs: comma-separated patterns with no quotes, no spaces (e.g., **/*.ts,**/*.tsx)
- alwaysApply: false (enforced)
- Do not touch master/common rules; only project-rules subtree

Usage:
  python scripts/normalize_project_rules.py --dry-run
  python scripts/normalize_project_rules.py --apply
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Tuple

ROOT = Path(__file__).resolve().parents[1]
RULES_DIR = ROOT / ".cursor" / "rules" / "project-rules"

DESC_STANDARD = (
    "The description defines the appropriate scenarios, and the model will evaluate the context "
    "to decide whether the rule should be applied."
)

FM_START = re.compile(r"^---\s*$")
FM_END = re.compile(r"^---\s*$")
HAS_TAGS = re.compile(r"TAGS:\s*\[", re.I)
HAS_TRIGGERS = re.compile(r"TRIGGERS:\s*", re.I)
HAS_SCOPE = re.compile(r"SCOPE:\s*", re.I)


def normalize_frontmatter(text: str) -> Tuple[str, bool]:
    lines = text.splitlines()
    if not lines or not FM_START.match(lines[0]):
        return text, False

    # find end of frontmatter
    end_idx = None
    for i in range(1, min(len(lines), 200)):
        if FM_END.match(lines[i]):
            end_idx = i
            break
    if end_idx is None:
        return text, False

    header = lines[1:end_idx]
    body = lines[end_idx + 1 :]

    changed = False

    # Build normalized header map in order: description, globs, alwaysApply
    desc_line_idx = next((i for i, ln in enumerate(header) if ln.strip().lower().startswith("description:")), None)
    globs_line_idx = next((i for i, ln in enumerate(header) if ln.strip().lower().startswith("globs:")), None)
    always_idx = next((i for i, ln in enumerate(header) if ln.strip().lower().startswith("alwaysapply:")), None)

    # Normalize description
    if desc_line_idx is not None:
        raw = header[desc_line_idx]
        val = raw.split(":", 1)[1].strip()
        # strip surrounding quotes
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        if HAS_TAGS.search(val) or HAS_TRIGGERS.search(val) or HAS_SCOPE.search(val) or not val:
            header[desc_line_idx] = f"description: {DESC_STANDARD}"
            changed = True
    else:
        header.insert(0, f"description: {DESC_STANDARD}")
        changed = True

    # Normalize globs (if present): remove quotes and spaces around commas
    if globs_line_idx is not None:
        raw = header[globs_line_idx]
        val = raw.split(":", 1)[1].strip()
        # remove surrounding quotes if present
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        # remove spaces
        val = val.replace(" ", "")
        header[globs_line_idx] = f"globs: {val}"
        if header[globs_line_idx] != raw:
            changed = True

    # Ensure alwaysApply: false
    if always_idx is not None:
        raw = header[always_idx]
        header[always_idx] = "alwaysApply: false"
        if header[always_idx] != raw:
            changed = True
    else:
        header.append("alwaysApply: false")
        changed = True

    # Rebuild file
    new_text = "\n".join(["---"] + header + ["---"] + body) + ("\n" if text.endswith("\n") else "")
    return (new_text, changed)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not RULES_DIR.exists():
        print(f"[ERR] rules dir not found: {RULES_DIR}")
        return 2

    changed_files = 0
    scanned = 0

    for p in RULES_DIR.rglob("*.mdc"):
        try:
            original = p.read_text(encoding="utf-8")
        except Exception:
            continue
        new_text, changed = normalize_frontmatter(original)
        scanned += 1
        if changed:
            changed_files += 1
            print(f"[CHANGE] {p}")
            if args.apply:
                p.write_text(new_text, encoding="utf-8")
    print(f"[OK] scanned={scanned} changed={changed_files} apply={args.apply}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())