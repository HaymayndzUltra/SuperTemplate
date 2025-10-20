#!/usr/bin/env python3
"""Protocol Cognitive Reasoning Validator."""

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


class ProtocolReasoningValidator:
    """Validates reasoning patterns, decision logic, and learning mechanisms."""

    KEY = "protocol_reasoning"
    DIMENSION_KEYS = [
        "reasoning_patterns",
        "decision_trees",
        "problem_solving_logic",
        "learning_mechanisms",
        "meta_cognition",
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

        workflow_section = extract_section(content, "WORKFLOW")
        gates_section = extract_section(content, "QUALITY GATES")
        evidence_section = extract_section(content, "EVIDENCE SUMMARY")
        handoff_section = extract_section(content, "HANDOFF CHECKLIST")

        combined = "\n".join(filter(None, [workflow_section, gates_section, evidence_section, handoff_section]))

        dimensions = [
            self._evaluate_reasoning_patterns(workflow_section),
            self._evaluate_decision_trees(workflow_section, gates_section),
            self._evaluate_problem_solving(workflow_section, gates_section),
            self._evaluate_learning_mechanisms(evidence_section, handoff_section),
            self._evaluate_meta_cognition(combined),
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
            note="Documentation-focused protocol detected; reasoning prompts treated as optional guidance.",
        )

        return result

    def _evaluate_reasoning_patterns(self, workflow_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("reasoning_patterns", weight=0.25)
        if not workflow_section:
            dim.issues.append("Workflow section missing; cannot evaluate reasoning patterns")
            return dim

        pattern_terms = ["pattern", "heuristic", "strategy", "playbook", "framework"]
        matches = [term for term in pattern_terms if term in workflow_section.lower()]
        explanation_mentions = re.findall(r"because|so that|therefore|why", workflow_section, flags=re.IGNORECASE)
        improvement_mentions = re.findall(r"improve|refine|adjust", workflow_section, flags=re.IGNORECASE)

        checks = {
            "pattern_terms": len(matches) >= 2,
            "explanations": len(explanation_mentions) >= 2,
            "improvement": len(improvement_mentions) > 0,
            "example_references": workflow_section.lower().count("example") > 0,
        }

        dim.details = {"matches": matches, **checks}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if len(matches) < 2:
            dim.issues.append("Reasoning patterns not explicitly named")

        return dim

    def _evaluate_decision_trees(self, workflow_section: str, gates_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("decision_trees", weight=0.25)
        combined = "\n".join(filter(None, [workflow_section, gates_section]))
        if not combined:
            dim.issues.append("Decision logic not documented")
            return dim

        decision_terms = re.findall(r"decision|option|choose|select|branch", combined, flags=re.IGNORECASE)
        criteria_terms = re.findall(r"criteria|if|when|threshold", combined, flags=re.IGNORECASE)
        outcome_terms = re.findall(r"outcome|result|path", combined, flags=re.IGNORECASE)
        logging_terms = re.findall(r"log|record|document", combined, flags=re.IGNORECASE)

        checks = {
            "decision_points": len(decision_terms) >= 3,
            "criteria": len(criteria_terms) >= 4,
            "outcomes": len(outcome_terms) >= 2,
            "logging": len(logging_terms) >= 2,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if len(decision_terms) < 3:
            dim.issues.append("Decision points insufficiently described")

        return dim

    def _evaluate_problem_solving(self, workflow_section: str, gates_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("problem_solving_logic", weight=0.2)
        combined = "\n".join(filter(None, [workflow_section, gates_section]))
        if not combined:
            dim.issues.append("Problem-solving guidance missing")
            return dim

        problem_terms = re.findall(r"issue|problem|risk|blocker", combined, flags=re.IGNORECASE)
        root_cause_terms = re.findall(r"root cause|analysis|diagnose", combined, flags=re.IGNORECASE)
        solution_terms = re.findall(r"mitigate|resolve|fix", combined, flags=re.IGNORECASE)
        validation_terms = re.findall(r"validate|confirm|re-run|test", combined, flags=re.IGNORECASE)

        checks = {
            "problem_identification": len(problem_terms) >= 3,
            "root_cause": len(root_cause_terms) >= 1,
            "solutions": len(solution_terms) >= 2,
            "validation": len(validation_terms) >= 2,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if len(root_cause_terms) == 0:
            dim.recommendations.append("Include root-cause analysis guidance")

        return dim

    def _evaluate_learning_mechanisms(self, evidence_section: str, handoff_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("learning_mechanisms", weight=0.15)
        combined = "\n".join(filter(None, [evidence_section, handoff_section]))
        if not combined:
            dim.issues.append("Learning mechanisms not referenced")
            return dim

        feedback_terms = re.findall(r"feedback|lessons|retro|retrospective|continuous", combined, flags=re.IGNORECASE)
        improvement_terms = re.findall(r"improvement|enhancement|refine", combined, flags=re.IGNORECASE)
        knowledge_terms = re.findall(r"knowledge|catalog|library|index", combined, flags=re.IGNORECASE)
        adaptation_terms = re.findall(r"adapt|update|evolve", combined, flags=re.IGNORECASE)

        checks = {
            "feedback": len(feedback_terms) > 0,
            "improvement_tracking": len(improvement_terms) > 0,
            "knowledge_base": len(knowledge_terms) > 0,
            "adaptation": len(adaptation_terms) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        missing = [name for name, ok in checks.items() if not ok]
        if missing:
            dim.issues.append(f"Learning mechanisms incomplete: {', '.join(missing)}")

        return dim

    def _evaluate_meta_cognition(self, combined: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("meta_cognition", weight=0.15)
        if not combined:
            dim.issues.append("Meta-cognitive guidance missing")
            return dim

        awareness_terms = re.findall(r"aware|limitations|capacity", combined, flags=re.IGNORECASE)
        monitoring_terms = re.findall(r"monitor|track|inspect", combined, flags=re.IGNORECASE)
        correction_terms = re.findall(r"correct|adjust|calibrate", combined, flags=re.IGNORECASE)
        improvement_terms = re.findall(r"improve|mature|evolve", combined, flags=re.IGNORECASE)

        checks = {
            "awareness": len(awareness_terms) > 0,
            "monitoring": len(monitoring_terms) > 0,
            "correction": len(correction_terms) > 0,
            "improvement": len(improvement_terms) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if len(awareness_terms) == 0:
            dim.issues.append("Self-awareness statements missing")

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
        output_file = self.output_dir / f"protocol-{result['protocol_id']}-reasoning.json"
        write_json(output_file, result)
        return output_file

    def generate_summary(self, results: List[Dict[str, Any]]) -> Path:
        metrics = aggregate_dimension_metrics(results, self.DIMENSION_KEYS)
        return generate_summary(self.KEY, results, self.output_dir, extra_fields={"dimensions": metrics})


def run_cli(args: argparse.Namespace) -> int:
    workspace_root = Path(args.workspace).resolve()
    validator = ProtocolReasoningValidator(workspace_root)
    results: List[Dict[str, Any]] = []

    if args.protocol:
        result = validator.validate_protocol(args.protocol)
        results.append(result)
        output_path = validator.save_result(result)
        print(f"✅ Reasoning validation complete for Protocol {args.protocol} -> {output_path}")
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
    parser = argparse.ArgumentParser(description="Validate cognitive reasoning coverage for AI workflow protocols")
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
