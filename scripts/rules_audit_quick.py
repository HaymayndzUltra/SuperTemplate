#!/usr/bin/env python3
"""Lightweight quality audit for project rule documents."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable, Sequence

import yaml

DEFAULT_ROOT = Path(".cursor/rules/project-rules")
FRONTMATTER_SPLIT = re.compile(r"^---\s*$", re.MULTILINE)
REQUIRED_SECTIONS = ["AI Persona", "Core Principle"]
PROTO_SECTIONS = ["Protocol", "Requirements", "Rules"]
EXAMPLE_SECTIONS = ["Examples", "Example"]
VALIDATION_SECTIONS = ["Validation", "Checks", "Acceptance"]
UNWANTED_COPY = ["Liquid Development Guidelines"]


@dataclass(frozen=True)
class RuleIssue:
    code: str
    path: Path
    detail: str | None = None


@dataclass(frozen=True)
class GlobOverlap:
    glob: str
    paths: list[Path]


@dataclass(frozen=True)
class AuditSummary:
    total_rules: int
    issues: list[RuleIssue]
    overlaps: list[GlobOverlap]


def _read_rule(path: Path) -> tuple[dict[str, object] | None, str | None]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    parts = FRONTMATTER_SPLIT.split(text, maxsplit=2)
    if len(parts) < 3:
        return None, None
    try:
        frontmatter = yaml.safe_load(parts[1]) or {}
    except Exception:
        frontmatter = {}
    body = parts[2]
    return frontmatter, body


def _check_body_sections(body: str, issues: list[RuleIssue], path: Path, min_lines: int) -> None:
    if not body or len(body.splitlines()) < min_lines:
        issues.append(RuleIssue("WEAK_BODY", path))
        return

    lowered = body.lower()
    for section in REQUIRED_SECTIONS:
        if section.lower() not in lowered:
            issues.append(RuleIssue(f"MISSING_SECTION:{section}", path))
    if not any(section.lower() in lowered for section in PROTO_SECTIONS):
        issues.append(RuleIssue("MISSING_SECTION:Protocol", path))
    if not any(section.lower() in lowered for section in EXAMPLE_SECTIONS):
        issues.append(RuleIssue("SUGGEST_ADD:Examples", path))
    if not any(section.lower() in lowered for section in VALIDATION_SECTIONS):
        issues.append(RuleIssue("SUGGEST_ADD:Validation", path))
    for copy in UNWANTED_COPY:
        if copy.lower() in lowered:
            issues.append(RuleIssue("CROSS_CONTENT:LIQUID", path))


def _collect_glob_overlaps(by_globs: dict[str, list[Path]]) -> list[GlobOverlap]:
    overlaps: list[GlobOverlap] = []
    for glob, paths in sorted(by_globs.items()):
        if glob != "None" and len(paths) > 1:
            overlaps.append(GlobOverlap(glob=glob, paths=sorted(paths)))
    return overlaps


def audit_rules(root: Path, min_body_lines: int) -> AuditSummary:
    issues: list[RuleIssue] = []
    by_globs: dict[str, list[Path]] = {}
    total = 0

    for rule_path in sorted(root.rglob("*.mdc")):
        total += 1
        frontmatter, body = _read_rule(rule_path)
        if frontmatter is None or body is None:
            issues.append(RuleIssue("MALFORMED_FRONTMATTER", rule_path))
            continue

        description = str(frontmatter.get("description") or "")
        globs = frontmatter.get("globs")
        if not globs:
            issues.append(RuleIssue("MISSING_GLOBS", rule_path))
        if "TAGS:" not in description or "TRIGGERS:" not in description or "SCOPE:" not in description:
            issues.append(RuleIssue("DESCRIPTION_FORMAT", rule_path))
        if "alwaysApply" not in frontmatter:
            issues.append(RuleIssue("MISSING_ALWAYS_APPLY", rule_path))

        scope = frontmatter.get("scope")
        if scope and scope != "project-rules":
            issues.append(RuleIssue("SCOPE_NOT_PROJECT_RULES", rule_path, detail=str(scope)))

        if globs is not None:
            key = str(globs)
            by_globs.setdefault(key, []).append(rule_path)

        _check_body_sections(body, issues, rule_path, min_body_lines)

    overlaps = _collect_glob_overlaps(by_globs)
    return AuditSummary(total_rules=total, issues=issues, overlaps=overlaps)


def write_report(summary: AuditSummary, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as handle:
        handle.write("# Project Rules Audit\n\n")
        handle.write(f"Total rules: {summary.total_rules}\n")
        handle.write(f"Issues: {len(summary.issues)}\n")
        handle.write(f"Potential overlaps: {len(summary.overlaps)}\n\n")

        handle.write("## Issues\n")
        for issue in summary.issues:
            if issue.detail:
                handle.write(f"- {issue.code}: {issue.path} ({issue.detail})\n")
            else:
                handle.write(f"- {issue.code}: {issue.path}\n")

        handle.write("\n## Overlaps by globs\n")
        for overlap in summary.overlaps:
            handle.write(f"- {overlap.glob}\n")
            for path in overlap.paths:
                handle.write(f"  - {path}\n")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run heuristic checks across .cursor/rules/project-rules/*.mdc files.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help="Directory that contains the project rule markdown files.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional path for the generated markdown report (defaults to <root>/AUDIT_REPORT.md).",
    )
    parser.add_argument(
        "--min-body-lines",
        type=int,
        default=3,
        help="Minimum number of body lines required before a rule is considered substantive.",
    )
    parser.add_argument(
        "--fail-on-issues",
        action="store_true",
        help="Return exit code 2 when any issues are detected.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    output = (args.output or (root / "AUDIT_REPORT.md")).resolve()

    if not root.exists():  # pragma: no cover - CLI guard
        raise SystemExit(f"Project rules directory not found: {root}")

    summary = audit_rules(root=root, min_body_lines=args.min_body_lines)
    write_report(summary, output)

    print("SUMMARY:")
    print(
        f"rules={summary.total_rules} issues={len(summary.issues)} overlaps={len(summary.overlaps)}"
    )
    for issue in summary.issues[:20]:
        detail = f" ({issue.detail})" if issue.detail else ""
        print(f"- {issue.code}: {issue.path}{detail}")

    if args.fail_on_issues and summary.issues:
        return 2
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
