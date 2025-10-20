"""Utility helpers for protocol validation scripts."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

SECTION_PATTERN = re.compile(r"^##\s+(.+)$", flags=re.MULTILINE)

DEFAULT_PROTOCOL_IDS: List[str] = [f"{i:02d}" for i in range(1, 28)]


def current_timestamp() -> str:
    """Return an ISO-8601 timestamp with UTC designator."""

    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


@dataclass
class DimensionEvaluation:
    """Container for per-dimension validation data."""

    name: str
    weight: float
    score: float = 0.0
    status: str = "fail"
    issues: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    details: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "score": self.score,
            "status": self.status,
            "issues": self.issues,
            "recommendations": self.recommendations,
            "details": self.details,
        }


def get_protocol_file(workspace_root: Path, protocol_id: str) -> Optional[Path]:
    """Return the markdown file for a protocol id."""

    workflow_dir = workspace_root / ".cursor" / "ai-driven-workflow"
    if not workflow_dir.exists():
        return None
    matches = sorted(workflow_dir.glob(f"{protocol_id}-*.md"))
    return matches[0] if matches else None


def read_protocol_content(protocol_file: Path) -> Optional[str]:
    """Read a protocol markdown file and return its text."""

    try:
        return protocol_file.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    except Exception as exc:  # pragma: no cover - defensive guard
        raise RuntimeError(f"Failed to read protocol file {protocol_file}: {exc}")


def _normalise_heading(raw: str) -> str:
    """Return a normalised heading token for flexible lookups."""

    heading = raw.strip()
    heading = re.sub(r"^[\w\-\s]*[.:]\s*", "", heading)
    heading = re.sub(r"\s+", " ", heading)
    return heading.upper()


def extract_section(content: str, section_name: str) -> str:
    """Extract a markdown section by heading name (case-insensitive).

    The helper understands numbered headings such as ``## 01. QUALITY GATES`` or
    prefixed variants like ``## 00-CD. AI ROLE AND MISSION``. If an exact match
    is not found, a fuzzy lookup is attempted that matches on substring to avoid
    overly brittle validators.
    """

    sections: Dict[str, Tuple[str, str]] = {}
    matches = list(SECTION_PATTERN.finditer(content))
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
        heading = match.group(1)
        normalised = _normalise_heading(heading)
        sections[normalised] = (heading, content[start:end].strip())

    target = _normalise_heading(section_name)
    if target in sections:
        return sections[target][1]

    for key, (_, value) in sections.items():
        if target in key or key in target:
            return value

    return ""


def determine_status(score: float, *, pass_threshold: float = 0.9, warning_threshold: float = 0.75) -> str:
    """Convert numeric score into pass/warning/fail label."""

    if score >= pass_threshold:
        return "pass"
    if score >= warning_threshold:
        return "warning"
    return "fail"


def compute_weighted_score(
    dimensions: Iterable[DimensionEvaluation], *, baseline: float = 0.0
) -> float:
    total_weight = sum(dim.weight for dim in dimensions)
    if total_weight == 0:
        return 0.0
    weighted = sum(dim.score * dim.weight for dim in dimensions) / total_weight
    if baseline <= 0:
        return weighted
    baseline = min(max(baseline, 0.0), 0.99)
    return baseline + (1 - baseline) * weighted


def gather_issues(dimensions: Iterable[DimensionEvaluation]) -> Tuple[List[str], List[str]]:
    issues: List[str] = []
    recommendations: List[str] = []
    for dim in dimensions:
        issues.extend(dim.issues)
        recommendations.extend(dim.recommendations)
    return issues, recommendations


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def build_base_result(validator_key: str, protocol_id: str) -> Dict[str, Any]:
    return {
        "validator": validator_key,
        "protocol_id": protocol_id,
        "validation_timestamp": current_timestamp(),
        "overall_score": 0.0,
        "validation_status": "fail",
        "issues": [],
        "recommendations": [],
    }


def generate_summary(
    validator_key: str,
    results: List[Dict[str, Any]],
    output_dir: Path,
    *,
    extra_fields: Optional[Dict[str, Any]] = None,
) -> Path:
    """Create a validator summary report with aggregate statistics."""

    summary = {
        "validator": validator_key,
        "validation_timestamp": current_timestamp(),
        "total_protocols": len(results),
        "pass_count": sum(1 for item in results if item.get("validation_status") == "pass"),
        "warning_count": sum(1 for item in results if item.get("validation_status") == "warning"),
        "fail_count": sum(1 for item in results if item.get("validation_status") == "fail"),
        "average_score": (
            sum(item.get("overall_score", 0.0) for item in results) / len(results)
            if results
            else 0.0
        ),
        "protocols": [
            {
                "protocol_id": item.get("protocol_id"),
                "status": item.get("validation_status"),
                "score": item.get("overall_score"),
            }
            for item in results
        ],
    }

    if extra_fields:
        summary.update(extra_fields)

    output_dir.mkdir(parents=True, exist_ok=True)
    summary_path = output_dir / f"{validator_key}-summary.json"
    write_json(summary_path, summary)
    return summary_path


def aggregate_dimension_metrics(results: List[Dict[str, Any]], dimension_keys: Iterable[str]) -> Dict[str, Any]:
    metrics: Dict[str, Dict[str, Any]] = {}
    for key in dimension_keys:
        values = [item.get(key, {}).get("score") for item in results if key in item]
        metrics[key] = {
            "average_score": (sum(v for v in values if v is not None) / len(values) if values else 0.0),
            "pass_count": sum(1 for item in results if item.get(key, {}).get("status") == "pass"),
            "warning_count": sum(1 for item in results if item.get(key, {}).get("status") == "warning"),
            "fail_count": sum(1 for item in results if item.get(key, {}).get("status") == "fail"),
        }
    return metrics


def status_from_counts(found: int, total: int) -> str:
    """Return pass/warning/fail from discrete checklist completion."""

    if total <= 0:
        return "fail"
    if found >= total:
        return "pass"

    # Allow a generous warning band so partially complete documentation does
    # not immediately fail when the fundamentals are present.
    warning_threshold = total - max(1, total // 2)
    if found >= warning_threshold:
        return "warning"
    return "fail"

