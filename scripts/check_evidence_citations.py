#!/usr/bin/env python3
"""Lint verification reports for evidence citation formatting.

The validator scans Markdown files for inline citations in the
`【F:path†Lx-Ly】` format and ensures each citation:

1. Starts with the `F:` file prefix rather than a chunk identifier
2. Matches the `F:<relative-path>†L<start>(-L<end>)?` pattern
3. Points to an existing file within the repository
4. Uses non-decreasing line spans (if an end line is provided)

Usage:
    python scripts/check_evidence_citations.py [paths...]

If no paths are provided the script defaults to scanning
`documentation/pr-reviews/`.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TARGET = REPO_ROOT / "documentation" / "pr-reviews"

CODE_FENCE_PATTERN = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_PATTERN = re.compile(r"`[^`]*`")
CITATION_PATTERN = re.compile(r"【([^】]+)】")
VALID_CITATION_PATTERN = re.compile(r"^F:([^†]+)†L(\d+)(?:-L(\d+))?$")


@dataclass
class CitationError:
    file_path: Path
    line: int
    citation: str
    message: str

    def format(self) -> str:
        rel_path = self.file_path.relative_to(REPO_ROOT)
        return f"{rel_path}:{self.line}: {self.message} -> 【{self.citation}】"


def iter_markdown_files(targets: Sequence[Path]) -> Iterable[Path]:
    """Yield Markdown files from the provided targets."""
    for target in targets:
        if target.is_dir():
            yield from sorted(p for p in target.rglob("*.md") if p.is_file())
        elif target.is_file():
            if target.suffix.lower() == ".md":
                yield target
        else:
            continue


def _code_spans(text: str) -> List[tuple[int, int]]:
    """Return start/end positions for fenced and inline code segments."""
    spans: List[tuple[int, int]] = []
    for match in CODE_FENCE_PATTERN.finditer(text):
        spans.append((match.start(), match.end()))

    for match in INLINE_CODE_PATTERN.finditer(text):
        # Skip inline code captured inside fenced blocks
        if any(start <= match.start() < end for start, end in spans):
            continue
        spans.append((match.start(), match.end()))

    spans.sort()
    return spans


def _is_within_spans(index: int, spans: Sequence[tuple[int, int]]) -> bool:
    return any(start <= index < end for start, end in spans)


def validate_citations(markdown_file: Path) -> List[CitationError]:
    """Validate all citations within a Markdown file."""
    try:
        text = markdown_file.read_text(encoding="utf-8")
    except Exception as exc:  # pragma: no cover - I/O failure
        return [
            CitationError(
                file_path=markdown_file,
                line=0,
                citation="",
                message=f"Failed to read file: {exc}",
            )
        ]

    errors: List[CitationError] = []
    spans = _code_spans(text)

    for match in CITATION_PATTERN.finditer(text):
        citation = match.group(1)
        line_no = text.count("\n", 0, match.start()) + 1

        if _is_within_spans(match.start(), spans):
            continue

        if not citation.startswith("F:"):
            errors.append(
                CitationError(
                    file_path=markdown_file,
                    line=line_no,
                    citation=citation,
                    message="citation must start with 'F:' file reference",
                )
            )
            continue

        match_components = VALID_CITATION_PATTERN.match(citation)
        if not match_components:
            errors.append(
                CitationError(
                    file_path=markdown_file,
                    line=line_no,
                    citation=citation,
                    message="citation must match format F:path†Lx(-Ly)",
                )
            )
            continue

        relative_path_str, start_line, end_line = (
            match_components.group(1),
            int(match_components.group(2)),
            match_components.group(3),
        )

        try:
            citation_path = (REPO_ROOT / relative_path_str).resolve(strict=False)
        except Exception:  # pragma: no cover - path resolution errors
            errors.append(
                CitationError(
                    file_path=markdown_file,
                    line=line_no,
                    citation=citation,
                    message="unable to resolve citation path",
                )
            )
            continue

        try:
            citation_path.relative_to(REPO_ROOT)
        except ValueError:
            errors.append(
                CitationError(
                    file_path=markdown_file,
                    line=line_no,
                    citation=citation,
                    message="citation path must remain inside repository",
                )
            )
            continue

        if not citation_path.exists():
            errors.append(
                CitationError(
                    file_path=markdown_file,
                    line=line_no,
                    citation=citation,
                    message="referenced file does not exist",
                )
            )
            continue

        if end_line is not None and int(end_line) < int(start_line):
            errors.append(
                CitationError(
                    file_path=markdown_file,
                    line=line_no,
                    citation=citation,
                    message="line span end must be >= start",
                )
            )

    return errors


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate evidence citation formatting")
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Markdown files or directories to scan. Defaults to documentation/pr-reviews/",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    targets = [path.resolve() for path in args.paths] if args.paths else [DEFAULT_TARGET]

    markdown_files = list(iter_markdown_files(targets))
    if not markdown_files:
        print("No Markdown files found to validate.")
        return 0

    all_errors: List[CitationError] = []
    for md_file in markdown_files:
        all_errors.extend(validate_citations(md_file))

    if all_errors:
        print("Evidence citation validation failed:")
        for error in all_errors:
            print(f"  - {error.format()}")
        print(f"Total violations: {len(all_errors)}")
        return 1

    print(f"Validated {len(markdown_files)} Markdown files with no citation issues.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
