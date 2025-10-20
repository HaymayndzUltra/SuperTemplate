"""Utility helpers for protocol validators."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

PROTOCOL_FILE_PATTERN = re.compile(r"^(?P<id>\d{2})-.*\.md$")


def discover_protocol_files(protocols_dir: Path) -> List[Path]:
    """Return all protocol markdown files sorted by numeric id."""
    protocol_files: List[Tuple[int, Path]] = []
    for path in protocols_dir.glob("*.md"):
        match = PROTOCOL_FILE_PATTERN.match(path.name)
        if not match:
            continue
        protocol_files.append((int(match.group("id")), path))
    protocol_files.sort(key=lambda item: item[0])
    return [p for _, p in protocol_files]


def extract_sections(content: str) -> List[Tuple[str, str]]:
    """Split markdown content into (heading, body) tuples for level-2 headings."""
    sections: List[Tuple[str, str]] = []
    current_heading: Optional[str] = None
    current_lines: List[str] = []

    for line in content.splitlines():
        if line.startswith("## "):
            if current_heading is not None:
                sections.append((current_heading, "\n".join(current_lines).strip()))
                current_lines = []
            current_heading = line[3:].strip()
        elif current_heading is not None:
            current_lines.append(line)

    if current_heading is not None:
        sections.append((current_heading, "\n".join(current_lines).strip()))

    return sections


def collect_section_text(content: str, keywords: Iterable[str]) -> str:
    """Return concatenated text of sections whose heading contains any keyword."""
    keywords_lower = [kw.lower() for kw in keywords]
    collected: List[str] = []
    for heading, body in extract_sections(content):
        heading_lower = heading.lower()
        if any(kw in heading_lower for kw in keywords_lower):
            collected.append(body)
    return "\n\n".join(collected).strip()


def find_markers(text: str, markers: Iterable[str]) -> Dict[str, int]:
    """Count validation markers like [CRITICAL], [MUST], etc."""
    counts: Dict[str, int] = {}
    for marker in markers:
        counts[marker] = len(re.findall(re.escape(marker), text))
    return counts


def contains_any(text: str, keywords: Iterable[str]) -> bool:
    return any(re.search(re.escape(keyword), text, re.IGNORECASE) for keyword in keywords)


def contains_all(text: str, keywords: Iterable[str]) -> bool:
    return all(re.search(re.escape(keyword), text, re.IGNORECASE) for keyword in keywords)


def count_checkboxes(text: str) -> int:
    return len(re.findall(r"- \[[ xX]?\]", text))


def find_commands(text: str) -> List[str]:
    pattern = re.compile(r"(```(?:bash|shell)?\n[\s\S]*?```|`[^`\n]+`)")
    matches: List[str] = []
    for block in pattern.findall(text):
        block_clean = block.strip("`\n")
        for line in block_clean.splitlines():
            stripped = line.strip()
            if stripped.startswith("python") or stripped.startswith("./") or stripped.startswith("bash"):
                matches.append(stripped)
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("python ") or stripped.startswith("python3 "):
            matches.append(stripped)
    return matches


def extract_paths(text: str) -> List[str]:
    pattern = re.compile(r"([./]?[\w\-./]+\.(?:py|sh|json|md|yaml|yml))")
    return list({match.group(1) for match in pattern.finditer(text)})


def normalize_score(status: str, pass_value: float = 1.0, warning_value: float = 0.6, fail_value: float = 0.0) -> float:
    if status == "pass":
        return pass_value
    if status == "warning":
        return warning_value
    return fail_value


def status_from_ratio(ratio: float, pass_threshold: float, warning_threshold: float) -> str:
    if ratio >= pass_threshold:
        return "pass"
    if ratio >= warning_threshold:
        return "warning"
    return "fail"


def timestamp() -> str:
    return datetime.utcnow().isoformat() + "Z"


@dataclass
class DimensionResult:
    status: str
    score: float
    findings: Dict[str, object]
    issues: List[str]
    recommendations: List[str]

    def as_dict(self) -> Dict[str, object]:
        return {
            "status": self.status,
            "score": self.score,
            "findings": self.findings,
            "issues": self.issues,
            "recommendations": self.recommendations,
        }


class BaseProtocolValidator:
    slug: str = "base"
    name: str = "Base Validator"
    dimension_weights: Dict[str, float] = {}
    pass_threshold: float = 0.9
    warning_threshold: float = 0.75

    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root.resolve()
        self.protocols_dir = self.workspace_root / ".cursor" / "ai-driven-workflow"
        self.output_dir = self.workspace_root / ".artifacts" / "validation" / self.slug
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def list_protocol_ids(self) -> List[str]:
        ids: List[str] = []
        for path in discover_protocol_files(self.protocols_dir):
            match = PROTOCOL_FILE_PATTERN.match(path.name)
            if match:
                ids.append(match.group("id"))
        return ids

    def load_protocol_content(self, protocol_id: str) -> Tuple[Path, str]:
        target: Optional[Path] = None
        for path in discover_protocol_files(self.protocols_dir):
            if path.name.startswith(f"{protocol_id}-"):
                target = path
                break
        if target is None:
            raise FileNotFoundError(f"Protocol file not found for ID {protocol_id}")
        return target, target.read_text(encoding="utf-8")

    def evaluate_dimensions(self, protocol_id: str, content: str) -> Dict[str, DimensionResult]:
        raise NotImplementedError

    def aggregate_score(self, dimension_results: Dict[str, DimensionResult]) -> float:
        total = 0.0
        for key, result in dimension_results.items():
            weight = self.dimension_weights.get(key, 0.0)
            total += weight * result.score
        return total

    def status_for_score(self, score: float) -> str:
        if score >= self.pass_threshold:
            return "pass"
        if score >= self.warning_threshold:
            return "warning"
        return "fail"

    def compile_result(self, protocol_id: str, dimension_results: Dict[str, DimensionResult]) -> Dict[str, object]:
        overall_score = self.aggregate_score(dimension_results)
        status = self.status_for_score(overall_score)
        issues: List[str] = []
        recommendations: List[str] = []
        for result in dimension_results.values():
            issues.extend(result.issues)
            recommendations.extend(result.recommendations)
        return {
            "validator": self.slug,
            "validator_name": self.name,
            "protocol_id": protocol_id,
            "validation_timestamp": timestamp(),
            "dimensions": {key: value.as_dict() for key, value in dimension_results.items()},
            "overall_score": round(overall_score, 3),
            "validation_status": status,
            "issues": issues,
            "recommendations": recommendations,
        }

    def validate_protocol(self, protocol_id: str) -> Dict[str, object]:
        _, content = self.load_protocol_content(protocol_id)
        dimension_results = self.evaluate_dimensions(protocol_id, content)
        return self.compile_result(protocol_id, dimension_results)

    def save_protocol_result(self, protocol_id: str, result: Dict[str, object]) -> Path:
        output_path = self.output_dir / f"protocol-{protocol_id}-{self.slug}.json"
        with output_path.open("w", encoding="utf-8") as handle:
            json.dump(result, handle, indent=2)
        return output_path

    def generate_summary(self, all_results: List[Dict[str, object]]) -> Path:
        summary = {
            "validator": self.slug,
            "validator_name": self.name,
            "generated_at": timestamp(),
            "total_protocols": len(all_results),
            "status_counts": {
                "pass": sum(1 for r in all_results if r["validation_status"] == "pass"),
                "warning": sum(1 for r in all_results if r["validation_status"] == "warning"),
                "fail": sum(1 for r in all_results if r["validation_status"] == "fail"),
            },
            "average_score": round(sum(r["overall_score"] for r in all_results) / len(all_results), 3)
            if all_results
            else 0,
            "protocols": [
                {
                    "protocol_id": r["protocol_id"],
                    "status": r["validation_status"],
                    "score": r["overall_score"],
                }
                for r in all_results
            ],
        }
        summary_path = self.output_dir / f"{self.slug}-summary.json"
        with summary_path.open("w", encoding="utf-8") as handle:
            json.dump(summary, handle, indent=2)
        return summary_path


def run_cli(validator: BaseProtocolValidator, protocol: Optional[str], run_all: bool, generate_summary_flag: bool) -> int:
    all_results: List[Dict[str, object]] = []

    if protocol:
        try:
            result = validator.validate_protocol(protocol)
        except FileNotFoundError as exc:
            print(f"❌ {exc}")
            return 1
        validator.save_protocol_result(protocol, result)
        all_results.append(result)
        status_icon = "✅" if result["validation_status"] == "pass" else "⚠️" if result["validation_status"] == "warning" else "❌"
        print(f"{status_icon} Protocol {protocol}: {result['validation_status'].upper()} (score={result['overall_score']:.3f})")
    elif run_all:
        for protocol_id in validator.list_protocol_ids():
            try:
                result = validator.validate_protocol(protocol_id)
            except FileNotFoundError as exc:
                print(f"❌ {exc}")
                continue
            validator.save_protocol_result(protocol_id, result)
            all_results.append(result)
            status_icon = "✅" if result["validation_status"] == "pass" else "⚠️" if result["validation_status"] == "warning" else "❌"
            print(f"{status_icon} Protocol {protocol_id}: {result['validation_status'].upper()} (score={result['overall_score']:.3f})")
    else:
        print("⚠️ No protocol specified. Use --protocol XX or --all.")
        return 1

    if all_results and (run_all or generate_summary_flag):
        summary_path = validator.generate_summary(all_results)
        print(f"📄 Summary written to {summary_path}")

    fail_count = sum(1 for result in all_results if result["validation_status"] == "fail")
    return 1 if fail_count else 0
