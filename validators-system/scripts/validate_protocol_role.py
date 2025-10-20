#!/usr/bin/env python3
"""Protocol AI Role Validator."""

from __future__ import annotations

import argparse
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
    read_protocol_content,
    write_json,
)


class ProtocolRoleValidator:
    """Validates AI role, mission, and behavioral guidance."""

    KEY = "protocol_role"
    DIMENSION_KEYS = [
        "role_definition",
        "mission_statement",
        "constraints_guidelines",
        "output_expectations",
        "behavioral_guidance",
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

        role_section = extract_section(content, "AI ROLE AND MISSION")
        workflow_section = extract_section(content, "WORKFLOW")
        communication_section = extract_section(content, "COMMUNICATION PROTOCOLS")
        evidence_section = extract_section(content, "EVIDENCE SUMMARY")
        handoff_section = extract_section(content, "HANDOFF CHECKLIST")

        dimensions: List[DimensionEvaluation] = [
            self._evaluate_role_definition(role_section),
            self._evaluate_mission_statement(role_section),
            self._evaluate_constraints(role_section + "\n" + workflow_section),
            self._evaluate_output_expectations(workflow_section, evidence_section, handoff_section),
            self._evaluate_behavioral_guidance(role_section, communication_section),
        ]

        for dim, key in zip(dimensions, self.DIMENSION_KEYS):
            result[key] = dim.to_dict()

        result["overall_score"] = compute_weighted_score(dimensions)
        result["validation_status"] = determine_status(result["overall_score"], pass_threshold=0.9, warning_threshold=0.8)

        issues, recommendations = gather_issues(dimensions)
        result["issues"].extend(issues)
        result["recommendations"].extend(recommendations)

        return result

    # Dimension evaluators -------------------------------------------------

    def _evaluate_role_definition(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("role_definition", weight=0.25)
        if not section:
            dim.issues.append("AI ROLE AND MISSION section missing")
            return dim

        checks = {
            "role_title": bool(
                section and ("You are a" in section or "You are an" in section)
            ),
            "role_description": bool(len(section.splitlines()) > 1 and len(section.strip()) > 60),
            "domain_expertise": bool(
                any(word in section.lower() for word in ["domain", "expertise", "industry", "capability"])
            ),
            "behavioral_traits": bool(
                any(word in section.lower() for word in ["empat", "strateg", "rigor", "evidence", "governance"])
            ),
        }

        score = sum(1 for value in checks.values() if value) / len(checks)
        dim.score = score
        dim.details = checks
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["role_title"]:
            dim.issues.append("Role title not defined with persona statement")
            dim.recommendations.append("Add 'You are a ...' persona declaration")
        if not checks["role_description"]:
            dim.issues.append("Role description lacks depth")
        if not checks["domain_expertise"]:
            dim.issues.append("Domain expertise keywords missing")
        if not checks["behavioral_traits"]:
            dim.issues.append("Behavioral traits not articulated")

        return dim

    def _evaluate_mission_statement(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("mission_statement", weight=0.25)
        if not section:
            dim.issues.append("Mission statement unavailable")
            return dim

        checks = {
            "mission_clarity": "mission" in section.lower(),
            "scope_boundaries": any(word in section.lower() for word in ["within", "only", "do not", "boundar", "scope"]),
            "success_criteria": any(word in section.lower() for word in ["success", "complete", "validation", "evidence"]),
            "value_proposition": any(word in section.lower() for word in ["client", "value", "impact", "benefit", "outcome"]),
        }
        score = sum(1 for value in checks.values() if value) / len(checks)
        dim.score = score
        dim.details = checks
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["mission_clarity"]:
            dim.issues.append("Mission clarity not expressed")
        if not checks["scope_boundaries"]:
            dim.issues.append("Mission lacks scope boundaries or guardrails")
        if not checks["success_criteria"]:
            dim.issues.append("Success criteria absent from mission")
        if not checks["value_proposition"]:
            dim.issues.append("Value proposition not captured")

        return dim

    def _evaluate_constraints(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("constraints_guidelines", weight=0.2)
        if not section:
            dim.issues.append("Constraints section missing")
            return dim

        critical = section.count("[CRITICAL]")
        must = section.count("[MUST]")
        guideline = section.count("[GUIDELINE]")
        prohibition = section.lower().count("never") + section.lower().count("do not")

        checks = {
            "critical_constraints": critical > 0,
            "must_rules": must > 0,
            "guidelines": guideline > 0,
            "prohibitions": prohibition > 0,
        }

        dim.details = {**checks, "critical_count": critical, "must_count": must, "guideline_count": guideline}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["critical_constraints"]:
            dim.issues.append("No [CRITICAL] constraints defined")
        if not checks["must_rules"]:
            dim.issues.append("[MUST] rules missing for enforceable guidance")
        if not checks["guidelines"]:
            dim.recommendations.append("Add [GUIDELINE] markers for recommended practices")
        if not checks["prohibitions"]:
            dim.recommendations.append("Document explicit prohibitions or guardrails")

        return dim

    def _evaluate_output_expectations(
        self, workflow_section: str, evidence_section: str, handoff_section: str
    ) -> DimensionEvaluation:
        dim = DimensionEvaluation("output_expectations", weight=0.15)
        combined = "\n".join(filter(None, [workflow_section, evidence_section, handoff_section]))
        if not combined:
            dim.issues.append("No output documentation found")
            return dim

        checks = {
            "format": any(ext in combined for ext in [".md", ".json", ".yaml", "markdown"]),
            "structure": any(keyword in combined.lower() for keyword in ["section", "table", "manifest", "template"]),
            "location": ".artifacts/" in combined or "storage" in combined.lower(),
            "validation": any(keyword in combined.lower() for keyword in ["validate", "quality", "threshold", "gate"]),
        }

        dim.details = checks
        dim.score = sum(1 for v in checks.values() if v) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["format"]:
            dim.issues.append("Output formats not specified")
        if not checks["structure"]:
            dim.issues.append("Output structure missing (sections or tables)")
        if not checks["location"]:
            dim.issues.append("Output storage location not defined")
        if not checks["validation"]:
            dim.recommendations.append("Document validation criteria for generated outputs")

        return dim

    def _evaluate_behavioral_guidance(self, role_section: str, communication_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("behavioral_guidance", weight=0.15)
        combined = "\n".join(filter(None, [role_section, communication_section]))
        if not combined:
            dim.issues.append("Behavioral guidance not documented")
            return dim

        checks = {
            "communication_style": any(word in combined.lower() for word in ["tone", "announce", "status", "communication"]),
            "decision_making": any(word in combined.lower() for word in ["decide", "choose", "go/no-go", "option"]),
            "error_handling": "error" in combined.lower() or "halt" in combined.lower(),
            "user_interaction": any(word in combined.lower() for word in ["confirm", "reply", "ask", "request"]),
        }

        dim.details = checks
        dim.score = sum(1 for v in checks.values() if v) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["communication_style"]:
            dim.issues.append("Communication style guidance missing")
        if not checks["decision_making"]:
            dim.recommendations.append("Outline decision-making expectations")
        if not checks["error_handling"]:
            dim.issues.append("Error handling guidance absent")
        if not checks["user_interaction"]:
            dim.issues.append("User interaction prompts not defined")

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
        output_file = self.output_dir / f"protocol-{result['protocol_id']}-role.json"
        write_json(output_file, result)
        return output_file

    def generate_summary(self, results: List[Dict[str, Any]]) -> Path:
        metrics = aggregate_dimension_metrics(results, self.DIMENSION_KEYS)
        return generate_summary(self.KEY, results, self.output_dir, extra_fields={"dimensions": metrics})


def run_cli(args: argparse.Namespace) -> int:
    workspace_root = Path(args.workspace).resolve()
    validator = ProtocolRoleValidator(workspace_root)
    results: List[Dict[str, Any]] = []

    if args.protocol:
        result = validator.validate_protocol(args.protocol)
        results.append(result)
        output_path = validator.save_result(result)
        print(f"✅ Role validation complete for Protocol {args.protocol} -> {output_path}")
    elif args.all:
        for protocol_id in DEFAULT_PROTOCOL_IDS:
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
    parser = argparse.ArgumentParser(description="Validate AI role and mission definitions for workflow protocols")
    parser.add_argument("--protocol", help="Protocol ID to validate (e.g., '01')")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root (defaults to current directory)")

    args = parser.parse_args()
    exit_code = run_cli(args)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
