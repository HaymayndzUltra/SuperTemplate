#!/usr/bin/env python3
#!/usr/bin/env python3
"""Common utilities for protocol validators."""

import argparse
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple
import re

PASS_THRESHOLD = 0.95
WARNING_THRESHOLD = 0.80


@dataclass
class DimensionResult:
    """Result for a single validation dimension."""

    name: str
    score: float
    status: str
    issues: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    evidence: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "score": self.score,
            "status": self.status,
            "issues": self.issues,
            "recommendations": self.recommendations,
            "evidence": self.evidence,
        }


class ProtocolValidatorBase:
    """Base class with shared logic for protocol validators."""

    VALIDATOR_NAME: str = "base_validator"
    VALIDATOR_VERSION: str = "1.0.0"
    DIMENSIONS: Tuple[Tuple[str, float, Callable[[str, str], DimensionResult]], ...] = ()

    def __init__(self, workspace_root: Path) -> None:
        self.workspace_root = workspace_root
        self.protocols_dir = workspace_root / ".cursor" / "ai-driven-workflow"
        self.output_dir = workspace_root / ".artifacts" / "validation"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # High-level validation entry points
    # ------------------------------------------------------------------
    def validate_protocol(self, protocol_id: str) -> Dict[str, Any]:
        """Validate a single protocol and return structured results."""
        protocol_id = protocol_id.zfill(2)
        result: Dict[str, Any] = {
            "validator": self.VALIDATOR_NAME,
            "validator_version": self.VALIDATOR_VERSION,
            "protocol_id": protocol_id,
            "validation_timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "dimensions": {},
            "overall_score": 0.0,
            "validation_status": "fail",
            "issues": [],
            "recommendations": [],
        }

        protocol_file = self._find_protocol_file(protocol_id)
        if protocol_file is None or not protocol_file.exists():
            message = f"Protocol file not found for ID {protocol_id}"
            result["issues"].append(message)
            return result

        content = protocol_file.read_text(encoding="utf-8")
        total_weight = sum(weight for _, weight, _ in self.DIMENSIONS)
        if not self.DIMENSIONS or not total_weight:
            raise ValueError("Validator dimensions must be configured with weights")

        weighted_score = 0.0
        for dimension_name, weight, handler in self.DIMENSIONS:
            dimension_result = handler(protocol_id, content)
            result["dimensions"][dimension_name] = dimension_result.to_dict()
            weighted_score += dimension_result.score * weight
            result["issues"].extend(dimension_result.issues)
            result["recommendations"].extend(dimension_result.recommendations)

        result["overall_score"] = round(weighted_score / total_weight, 4)
        result["validation_status"] = self._status_from_score(result["overall_score"])

        self._write_output(protocol_id, result)
        return result

    def validate_all(self) -> Dict[str, Any]:
        """Validate all protocols and return aggregated scores."""
        summary: Dict[str, Any] = {
            "validator": self.VALIDATOR_NAME,
            "validator_version": self.VALIDATOR_VERSION,
            "validation_timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "protocols": {},
            "overall_score": 0.0,
            "validation_status": "fail",
            "issues": [],
        }

        protocol_ids = self._list_protocol_ids()
        if not protocol_ids:
            summary["issues"].append("No protocol files found")
            return summary

        scores: List[float] = []
        statuses: List[str] = []
        for protocol_id in protocol_ids:
            result = self.validate_protocol(protocol_id)
            summary["protocols"][protocol_id] = result
            scores.append(result.get("overall_score", 0.0))
            statuses.append(result.get("validation_status", "fail"))
            summary["issues"].extend(result.get("issues", []))

        if scores:
            summary["overall_score"] = round(sum(scores) / len(scores), 4)
            summary["validation_status"] = self._status_from_score(summary["overall_score"])

        aggregate_path = self.output_dir / f"summary-{self.VALIDATOR_NAME}.json"
        aggregate_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        return summary

    # ------------------------------------------------------------------
    # Helper and utility methods
    # ------------------------------------------------------------------
    def _find_protocol_file(self, protocol_id: str) -> Optional[Path]:
        pattern = f"{protocol_id}-*.md"
        matches = sorted(self.protocols_dir.glob(pattern))
        return matches[0] if matches else None

    def _list_protocol_ids(self) -> List[str]:
        protocol_files = sorted(self.protocols_dir.glob("[0-9][0-9]-*.md"))
        return [f.name.split("-", 1)[0] for f in protocol_files]

    def _write_output(self, protocol_id: str, result: Dict[str, Any]) -> None:
        output_file = self.output_dir / f"protocol-{protocol_id}-{self.VALIDATOR_NAME}.json"
        output_file.write_text(json.dumps(result, indent=2), encoding="utf-8")

    @staticmethod
    def _status_from_score(score: float) -> str:
        if score >= PASS_THRESHOLD:
            return "pass"
        if score >= WARNING_THRESHOLD:
            return "warning"
        return "fail"

    # ------------------------------------------------------------------
    # Content analysis helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _extract_section(content: str, section_name: str) -> str:
        pattern = rf"^##\s+(?:\d+\.\s+)?{re.escape(section_name)}.*?\n(.*?)(?=^##\s+|\Z)"
        match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE | re.DOTALL)
        return match.group(1).strip() if match else ""

    @staticmethod
    def _extract_subsections(section_text: str) -> Dict[str, str]:
        pattern = re.compile(r"^###\s+([^\n]+)\n(.*?)(?=^###\s+|\Z)", re.MULTILINE | re.DOTALL)
        return {title.strip(): body.strip() for title, body in pattern.findall(section_text)}

    @staticmethod
    def _count_markers(text: str) -> Dict[str, int]:
        markers = {
            "critical": text.count("[CRITICAL]"),
            "must": text.count("[MUST]"),
            "guideline": text.count("[GUIDELINE]"),
            "optional": text.count("[OPTIONAL]"),
            "strict": text.count("[STRICT]"),
        }
        return markers

    @staticmethod
    def _score_feature_flags(feature_flags: Dict[str, bool]) -> Tuple[float, List[str]]:
        total = len(feature_flags)
        if total == 0:
            return 0.0, ["No evaluation criteria configured"]
        found = sum(1 for value in feature_flags.values() if value)
        missing = [name for name, present in feature_flags.items() if not present]
        return found / total, missing

    @staticmethod
    def _status_for_features(score: float) -> str:
        if score >= PASS_THRESHOLD:
            return "pass"
        if score >= WARNING_THRESHOLD:
            return "warning"
        return "fail"

    @staticmethod
    def _has_keywords(text: str, keywords: Iterable[str]) -> bool:
        lowered = text.lower()
        return any(keyword.lower() in lowered for keyword in keywords)

    @staticmethod
    def _list_bullet_items(text: str) -> List[str]:
        bullets = re.findall(r"^[\-\*]\s+(.*)$", text, re.MULTILINE)
        numbered = re.findall(r"^\d+\.\s+(.*)$", text, re.MULTILINE)
        return [item.strip() for item in bullets + numbered if item.strip()]

    def _build_dimension_result(
        self,
        name: str,
        feature_flags: Dict[str, bool],
        evidence: Optional[Dict[str, Any]] = None,
        base_recommendations: Optional[List[str]] = None,
    ) -> DimensionResult:
        """Utility helper to convert feature flags into a dimension result."""

        score, missing = self._score_feature_flags(feature_flags)
        status = self._status_from_score(score)
        issues = [f"Missing {label.replace('_', ' ')}" for label in missing]
        recommendations = list(base_recommendations or [])
        for label in missing:
            recommendations.append(f"Add explicit coverage for {label.replace('_', ' ')}")

        return DimensionResult(
            name=name,
            score=round(score, 4),
            status=status,
            issues=issues,
            recommendations=recommendations,
            evidence=evidence or {"checks": feature_flags},
        )

    # ------------------------------------------------------------------
    # CLI
    # ------------------------------------------------------------------
    def run_cli(self, args: Optional[List[str]] = None) -> int:
        parser = argparse.ArgumentParser(description=f"Run the {self.VALIDATOR_NAME} validator")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--protocol", help="Specific protocol ID to validate (e.g., 01)")
        group.add_argument("--all", action="store_true", help="Validate all protocols")
        parsed = parser.parse_args(args=args)

        if parsed.protocol:
            result = self.validate_protocol(parsed.protocol)
            print(json.dumps(result, indent=2))
        else:
            summary = self.validate_all()
            print(json.dumps(summary, indent=2))

        return 0


def run_validator_cli(validator_cls: Callable[[Path], ProtocolValidatorBase]) -> None:
    workspace_root = Path(__file__).resolve().parents[2]
    validator = validator_cls(workspace_root)
    raise SystemExit(validator.run_cli())
