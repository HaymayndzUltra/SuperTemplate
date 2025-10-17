"""Utilities for loading and parsing review protocol playbooks."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


@dataclass(frozen=True)
class ReviewProtocol:
    """Structured representation of a review protocol markdown file."""

    slug: str
    path: Path
    title: str
    checklist: List[str]
    sections: Dict[str, List[str]]
    raw_content: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert the protocol into a serialisable dictionary."""
        return {
            "slug": self.slug,
            "path": str(self.path),
            "title": self.title,
            "checklist": list(self.checklist),
            "sections": {key: list(value) for key, value in self.sections.items()},
            "content": self.raw_content,
        }


class ReviewProtocolLoader:
    """Load review protocol markdown files from the workflow repository."""

    def __init__(self, repository_root: Optional[Path] = None):
        self.repository_root = Path(repository_root or Path(__file__).resolve().parents[2])
        self.protocol_root = (
            self.repository_root
            / ".cursor"
            / "ai-driven-workflow"
            / "review-protocols"
        )
        if not self.protocol_root.exists():
            raise FileNotFoundError(
                f"Review protocol directory not found: {self.protocol_root}"
            )

    def available_protocols(self) -> List[str]:
        """List available protocol slugs without file extensions."""
        return sorted(
            file.stem
            for file in self.protocol_root.glob("*.md")
            if file.is_file()
        )

    def load(self, protocol_name: str) -> ReviewProtocol:
        """Load a review protocol by slug or filename."""
        slug = protocol_name.replace(".md", "")
        protocol_path = self.protocol_root / f"{slug}.md"
        if not protocol_path.exists():
            raise FileNotFoundError(f"Protocol not found: {slug}")

        content = protocol_path.read_text(encoding="utf-8")
        title = self._extract_title(content, fallback=slug)
        sections = self._parse_sections(content)
        checklist = self._extract_checklist(sections.values())

        return ReviewProtocol(
            slug=slug,
            path=protocol_path,
            title=title,
            checklist=checklist,
            sections=sections,
            raw_content=content,
        )

    @staticmethod
    def _extract_title(content: str, fallback: str) -> str:
        """Extract the main title from markdown content."""
        for line in content.splitlines():
            if line.startswith("# "):
                return line[2:].strip()
        return fallback

    @staticmethod
    def _parse_sections(content: str) -> Dict[str, List[str]]:
        """Parse markdown into sections grouped by headings."""
        sections: Dict[str, List[str]] = {}
        current_section = "Overview"
        sections[current_section] = []

        for line in content.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                heading = stripped.lstrip("#").strip()
                current_section = heading or current_section
                sections.setdefault(current_section, [])
                continue
            sections.setdefault(current_section, []).append(stripped)

        return sections

    @staticmethod
    def _extract_checklist(sections: Iterable[List[str]]) -> List[str]:
        """Extract checklist items from section content."""
        checklist: List[str] = []
        pattern = re.compile(r"^- (?:\[(?: |x|X)\]\s*)?(?P<item>.+)")
        for lines in sections:
            for line in lines:
                match = pattern.match(line)
                if match:
                    checklist.append(match.group("item").strip())
        return checklist


__all__ = ["ReviewProtocol", "ReviewProtocolLoader"]
