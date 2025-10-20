#!/usr/bin/env python3
"""Protocol Meta-Reflection Validator."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

from validator_utils import (
    DEFAULT_PROTOCOL_IDS,
    DimensionEvaluation,
    aggregate_dimension_metrics,
    build_base_result,
    compute_weighted_score,
    determine_status,
    extract_section,
    gather_issues,
    generate_summary,
    get_protocol_file,
    include_documentation_protocols,
    relax_for_documentation_protocol,
    read_protocol_content,
    write_json,
)


class ProtocolReflectionValidator:
    """Validates retrospective analysis, improvement loops, and planning."""

    KEY = "protocol_reflection"
    DIMENSION_KEYS = [
        "retrospective_analysis",
        "continuous_improvement",
        "system_evolution",
        "knowledge_capture",
        "future_planning",
    ]

    def __init__(self, workspace_root: Path) -> None:
        self.workspace_root = workspace_root
        self.output_dir = workspace_root / ".artifacts" / "validation"

    def validate_protocol(self, protocol_id: str) -> Dict[str, Any]:
        result = build_base_result(self.KEY, protocol_id)
        protocol_file = get_protocol_file(self.workspace_root, protocol_id)
        if not protocol_file:
            result["issues"].append(f"Protocol file not found for ID {protocol_id}")
            return result

        content = read_protocol_content(protocol_file)
        if not content:
            result["issues"].append("Protocol content could not be read")
            return result

        evidence_section = extract_section(content, "EVIDENCE SUMMARY")
        handoff_section = extract_section(content, "HANDOFF CHECKLIST")
        workflow_section = extract_section(content, "WORKFLOW")
        quality_section = extract_section(content, "QUALITY GATES")

        combined = "\n".join(filter(None, [evidence_section, handoff_section, workflow_section, quality_section]))

        dimensions = [
            self._evaluate_retrospective(workflow_section, handoff_section),
            self._evaluate_improvement(combined),
            self._evaluate_evolution(content),
            self._evaluate_knowledge_capture(combined),
            self._evaluate_future_planning(combined),
        ]

        for key, dim in zip(self.DIMENSION_KEYS, dimensions):
            result[key] = dim.to_dict()

        result["overall_score"] = compute_weighted_score(dimensions)
        result["validation_status"] = determine_status(result["overall_score"], pass_threshold=0.85, warning_threshold=0.7)

        issues, recommendations = gather_issues(dimensions)
        result["issues"].extend(issues)
        result["recommendations"].extend(recommendations)

        relax_for_documentation_protocol(
            protocol_id,
            result,
            note="Documentation-focused protocol detected; reflection outputs considered advisory.",
        )

        return result

    def _evaluate_retrospective(self, workflow_section: str, handoff_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("retrospective_analysis", weight=0.3)
        combined = "\n".join(filter(None, [workflow_section, handoff_section]))
        if not combined:
            dim.issues.append("Retrospective guidance not present")
            return dim

        review_terms = re.findall(r"retrospective|review|analysis|postmortem", combined, flags=re.IGNORECASE)
        performance_terms = re.findall(r"performance|metric|score", combined, flags=re.IGNORECASE)
        issue_terms = re.findall(r"issue|problem|risk", combined, flags=re.IGNORECASE)
        success_terms = re.findall(r"success|win|effective", combined, flags=re.IGNORECASE)

        checks = {
            "review": len(review_terms) > 0,
            "performance": len(performance_terms) > 0,
            "issues": len(issue_terms) > 0,
            "success": len(success_terms) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["review"]:
            dim.issues.append("Retrospective analysis not documented")

        return dim

    def _evaluate_improvement(self, combined: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("continuous_improvement", weight=0.25)
        if not combined:
            dim.issues.append("Improvement loops not described")
            return dim

        opportunity_terms = re.findall(r"improvement|optimize|enhance", combined, flags=re.IGNORECASE)
        plan_terms = re.findall(r"plan|roadmap|task", combined, flags=re.IGNORECASE)
        tracking_terms = re.findall(r"track|monitor|measure", combined, flags=re.IGNORECASE)
        evidence_terms = re.findall(r"evidence|proof|report", combined, flags=re.IGNORECASE)

        checks = {
            "opportunities": len(opportunity_terms) > 0,
            "plans": len(plan_terms) > 0,
            "tracking": len(tracking_terms) > 0,
            "evidence": len(evidence_terms) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        missing = [name for name, ok in checks.items() if not ok]
        if missing:
            dim.issues.append(f"Continuous improvement gaps: {', '.join(missing)}")

        return dim

    def _evaluate_evolution(self, content: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("system_evolution", weight=0.2)
        if not content:
            dim.issues.append("Protocol content missing for evolution evaluation")
            return dim

        version_terms = re.findall(r"version|v\d+\.\d+\.\d+", content, flags=re.IGNORECASE)
        rationale_terms = re.findall(r"rationale|because|why", content, flags=re.IGNORECASE)
        impact_terms = re.findall(r"impact|effect|change", content, flags=re.IGNORECASE)
        rollback_terms = re.findall(r"rollback|revert|undo", content, flags=re.IGNORECASE)

        checks = {
            "version_history": len(version_terms) > 0,
            "rationale": len(rationale_terms) > 0,
            "impact": len(impact_terms) > 0,
            "rollback": len(rollback_terms) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["rollback"]:
            dim.recommendations.append("Document rollback or recovery approach for changes")

        return dim

    def _evaluate_knowledge_capture(self, combined: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("knowledge_capture", weight=0.15)
        if not combined:
            dim.issues.append("Knowledge capture not described")
            return dim

        lessons_terms = re.findall(r"lessons|best practice|anti-pattern", combined, flags=re.IGNORECASE)
        knowledge_terms = re.findall(r"knowledge|wiki|repository|catalog", combined, flags=re.IGNORECASE)
        storage_terms = re.findall(r"store|archive|record", combined, flags=re.IGNORECASE)
        sharing_terms = re.findall(r"share|broadcast|publish", combined, flags=re.IGNORECASE)

        checks = {
            "lessons": len(lessons_terms) > 0,
            "knowledge_base": len(knowledge_terms) > 0,
            "storage": len(storage_terms) > 0,
            "sharing": len(sharing_terms) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        missing = [name for name, ok in checks.items() if not ok]
        if missing:
            dim.issues.append(f"Knowledge capture gaps: {', '.join(missing)}")

        return dim

    def _evaluate_future_planning(self, combined: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("future_planning", weight=0.1)
        if not combined:
            dim.issues.append("Future planning not mentioned")
            return dim

        roadmap_terms = re.findall(r"roadmap|future|next phase|upcoming", combined, flags=re.IGNORECASE)
        priority_terms = re.findall(r"priority|prioritize", combined, flags=re.IGNORECASE)
        resource_terms = re.findall(r"resource|budget|team", combined, flags=re.IGNORECASE)
        timeline_terms = re.findall(r"timeline|schedule|when", combined, flags=re.IGNORECASE)

        checks = {
            "roadmap": len(roadmap_terms) > 0,
            "priorities": len(priority_terms) > 0,
            "resources": len(resource_terms) > 0,
            "timeline": len(timeline_terms) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if len(roadmap_terms) == 0:
            dim.issues.append("Roadmap or future direction not documented")

        return dim

    # Utilities -------------------------------------------------------------

    @staticmethod
    def _status_from_counts(found: int, total: int) -> str:
        if found == total:
            return "pass"
        if found >= total - 1:
            return "warning"
        return "fail"

    def save_result(self, result: Dict[str, Any]) -> Path:
        output_file = self.output_dir / f"protocol-{result['protocol_id']}-reflection.json"
        write_json(output_file, result)
        return output_file

    def generate_summary(self, results: List[Dict[str, Any]]) -> Path:
        metrics = aggregate_dimension_metrics(results, self.DIMENSION_KEYS)
        return generate_summary(self.KEY, results, self.output_dir, extra_fields={"dimensions": metrics})


def run_cli(args: argparse.Namespace) -> int:
    workspace_root = Path(args.workspace).resolve()
    validator = ProtocolReflectionValidator(workspace_root)
    results: List[Dict[str, Any]] = []

    if args.protocol:
        result = validator.validate_protocol(args.protocol)
        results.append(result)
        output_path = validator.save_result(result)
        print(f"✅ Reflection validation complete for Protocol {args.protocol} -> {output_path}")
    elif args.all:
        protocol_ids = include_documentation_protocols(
            DEFAULT_PROTOCOL_IDS, include_docs=args.include_docs
        )
        for protocol_id in protocol_ids:
            result = validator.validate_protocol(protocol_id)
            results.append(result)
            validator.save_result(result)
            status_icon = "✅" if result["validation_status"] == "pass" else "⚠️" if result["validation_status"] == "warning" else "❌"
            print(
                f"{status_icon} Protocol {protocol_id}: {result['validation_status'].upper()} (score: {result['overall_score']:.3f})"
            )
    else:
        raise SystemExit("Either --protocol or --all must be supplied")

    if args.report or args.all:
        summary_path = validator.generate_summary(results)
        print(f"\n📊 Summary report: {summary_path}")

    if any(item["validation_status"] == "fail" for item in results):
        return 1
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate meta-reflection readiness for AI workflow protocols")
    parser.add_argument("--protocol", help="Protocol ID to validate (e.g., '01')")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument(
        "--include-docs",
        action="store_true",
        help="Include documentation protocols (24-27) when running with --all",
    )
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root (defaults to current directory)")

    args = parser.parse_args()
    exit_code = run_cli(args)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
