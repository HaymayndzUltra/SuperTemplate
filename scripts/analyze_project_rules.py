#!/usr/bin/env python3
import os
import re
import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

PROJECT_RULES_DIR = Path("/workspace/.cursor/rules/project-rules")
ROOT_INDEX = PROJECT_RULES_DIR / "INDEX.mdc"
UTILS_INDEX = PROJECT_RULES_DIR / "utilities" / "INDEX.mdc"
REPORT_PATH = PROJECT_RULES_DIR / "VALIDATION_REPORT.md"


def read_file(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def parse_index(index_text: str) -> Dict[str, str]:
    """
    Parse INDEX.mdc into mapping of file base name -> category label.
    Categories: languages, frameworks, compliance, infrastructure, utilities
    """
    category = None
    mapping: Dict[str, str] = {}
    for line in index_text.splitlines():
        line_strip = line.strip()
        if line_strip.startswith("## "):
            title = line_strip[3:].strip().lower()
            if title in {"languages", "frameworks", "compliance", "infrastructure", "utilities"}:
                category = title
            else:
                category = None
            continue
        if category and line_strip.startswith("-"):
            # extract filename token
            token = line_strip.lstrip("- ").strip()
            if token.endswith(".mdc"):
                mapping[token] = category
    return mapping


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    fm: Dict[str, str] = {}
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            header = text[4:end].strip()
            body = text[end + 4 :].lstrip("\n")
            # naive YAML-ish parse for simple key: value pairs
            for line in header.splitlines():
                if ":" in line:
                    key, val = line.split(":", 1)
                    fm[key.strip()] = val.strip()
    return fm, body


KEYWORD_MAP: List[Tuple[str, str]] = [
    # (keyword, normalized topic)
    ("laravel", "laravel"),
    ("drupal", "drupal"),
    ("wordpress", "wordpress"),
    ("swiftui", "swift"),
    ("swift 6", "swift"),
    ("python", "python"),
    ("fastapi", "fastapi"),
    ("flask", "flask"),
    ("django", "django"),
    ("rails", "rails"),
    ("spring", "spring"),
    ("react", "react"),
    ("next.js", "nextjs"),
    ("nextjs", "nextjs"),
    ("sveltekit", "sveltekit"),
    ("svelte", "svelte"),
    ("vue", "vue"),
    ("angular", "angular"),
    ("expo", "expo"),
    ("react native", "react-native"),
    ("ionic", "ionic"),
    ("flutter", "flutter"),
    ("android", "android"),
    ("golang", "golang"),
    ("go ", "golang"),
    ("typescript", "typescript"),
    ("javascript", "javascript"),
    ("julia", "julia"),
    ("kotlin", "kotlin"),
    ("rust", "rust"),
    ("cpp", "cpp"),
    ("c++", "cpp"),
    ("lua", "lua"),
    ("pci", "pci-compliance"),
    ("sox", "sox-compliance"),
    ("accessibility", "accessibility"),
    ("terraform", "terraform"),
    ("azure", "azure"),
    ("manifest", "manifest-backend"),
    ("chain-of-thought", "swift-cot"),
    ("cot", "swift-cot"),
]


RENAMES: Dict[str, str] = {
    # current -> correct base name
    "franework": "laravel",
    "cot": "swift-cot",
    "manifest": "manifest-backend",
}


def detect_topic(body: str) -> Optional[str]:
    text = body.lower()
    for kw, topic in KEYWORD_MAP:
        if kw in text:
            return topic
    return None


def main() -> None:
    root_index = parse_index(read_file(ROOT_INDEX)) if ROOT_INDEX.exists() else {}
    utils_index = parse_index(read_file(UTILS_INDEX)) if UTILS_INDEX.exists() else {}
    index_map: Dict[str, str] = {}
    index_map.update(root_index)
    index_map.update(utils_index)

    rows: List[Dict[str, str]] = []
    all_files: List[Path] = sorted(PROJECT_RULES_DIR.rglob("*.mdc"))
    for p in all_files:
        rel = p.relative_to(PROJECT_RULES_DIR).as_posix()
        if rel.lower().endswith("/index.mdc"):
            continue
        text = read_file(p)
        fm, body = parse_frontmatter(text)
        base = p.name
        base_no_ext = base[:-4]
        # Prefer base filename match; if not found, try relative path (handles nested entries like review/behavior.mdc)
        index_cat = index_map.get(base)
        if not index_cat:
            index_cat = index_map.get(rel, "(not in index)")
        detected = detect_topic(text)
        proposed_base = RENAMES.get(base_no_ext, base_no_ext)
        proposed_category = index_cat
        # If not present in index, infer a category from topic heuristics
        if proposed_category == "(not in index)":
            if detected in {"python", "typescript", "javascript", "swift", "php", "java", "kotlin", "rust", "cpp", "golang", "lua", "julia"}:
                proposed_category = "languages"
            elif detected in {"nextjs", "react", "angular", "svelte", "sveltekit", "vue", "react-native", "expo", "flutter", "android", "ionic", "django", "fastapi", "flask", "rails", "spring", "laravel"}:
                proposed_category = "frameworks"
            elif detected in {"pci-compliance", "sox-compliance", "accessibility"}:
                proposed_category = "compliance"
            elif detected in {"azure", "terraform"}:
                proposed_category = "infrastructure"
            else:
                proposed_category = "utilities"

        needs_rename = (proposed_base + ".mdc") != base
        fm_desc = fm.get("description", "").strip().strip('"')
        fm_globs = fm.get("globs", "").strip()
        fm_apply = fm.get("alwaysApply", "").strip()
        # basic frontmatter sanity
        fm_ok = bool(fm_desc) and fm_apply in {"true", "false", "True", "False"}

        rows.append({
            "current": rel,
            "index_category": index_cat,
            "detected_topic": detected or "unknown",
            "proposed_filename": (p.parent / (proposed_base + ".mdc")).relative_to(PROJECT_RULES_DIR).as_posix(),
            "proposed_category": proposed_category,
            "frontmatter_ok": "yes" if fm_ok else "no",
            "frontmatter_desc": fm_desc,
            "frontmatter_globs": fm_globs,
            "frontmatter_alwaysApply": fm_apply,
            "needs_change": "yes" if needs_rename or proposed_category != index_cat or not fm_ok else "no",
        })

    # Generate report
    lines: List[str] = []
    lines.append("# Project Rules Validation Report")
    lines.append("")
    lines.append(f"Scanned files: {len(rows)}")
    lines.append("")
    lines.append("## Mapping (Current → Detected → Proposed Filename → Proposed Category)")
    lines.append("")
    lines.append("| Current Filename | Detected Topic | Index Category | Proposed Filename | Proposed Category | Frontmatter OK | Needs Change |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in rows:
        lines.append("| {current} | {detected_topic} | {index_category} | {proposed_filename} | {proposed_category} | {frontmatter_ok} | {needs_change} |".format(**r))

    # Detailed changes only for needs_change
    lines.append("")
    lines.append("## Detailed Changes (only files needing changes)")
    lines.append("")
    for r in rows:
        if r["needs_change"] != "yes":
            continue
        lines.append(f"### {r['current']}")
        lines.append("")
        lines.append(f"- Current State: index_category={r['index_category']}, detected_topic={r['detected_topic']}, frontmatter_ok={r['frontmatter_ok']}")
        lines.append(f"- Proposed Changes: new filename={r['proposed_filename']}, proposed_category={r['proposed_category']}")
        reason_bits = []
        if r["current"].endswith("franework.mdc"):
            reason_bits.append("misspelled Laravel rule")
        if r["current"].endswith("cot.mdc"):
            reason_bits.append("Swift Chain-of-Thought content")
        if r["current"].endswith("manifest.mdc"):
            reason_bits.append("Manifest backend guidelines")
        if r["frontmatter_ok"] != "yes":
            reason_bits.append("frontmatter needs normalization")
        if not reason_bits:
            reason_bits.append("categorization/rename alignment based on detected topic and index")
        lines.append(f"- Reasoning: {', '.join(reason_bits)}")
        lines.append("- Content Modifications: none planned (rename and frontmatter normalization only)")
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote report to {REPORT_PATH}")


if __name__ == "__main__":
    main()

