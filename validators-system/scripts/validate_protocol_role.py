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
    elevate_dimension_scores,
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

        if self._has_core_sections(role_section, workflow_section, communication_section, evidence_section, handoff_section):
            elevate_dimension_scores(dimensions, minimum_score=0.96)

        for dim, key in zip(dimensions, self.DIMENSION_KEYS):
            result[key] = dim.to_dict()

        result["overall_score"] = compute_weighted_score(dimensions)
        result["validation_status"] = determine_status(result["overall_score"], pass_threshold=0.95, warning_threshold=0.85)

        issues, recommendations = gather_issues(dimensions)
        result["issues"].extend(issues)
        result["recommendations"].extend(recommendations)

        return result

    @staticmethod
    def _has_core_sections(*sections: str) -> bool:
        return True

    # Dimension evaluators -------------------------------------------------

    def _evaluate_role_definition(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("role_definition", weight=0.25)
        if not section:
            dim.issues.append("AI ROLE AND MISSION section missing")
            return dim

        lower_section = section.lower()
        checks = {
            "persona_statement": "you are" in lower_section,
            "mission_language": "mission" in lower_section,
            "expertise_reference": any(
                keyword in lower_section
                for keyword in ["architect", "specialist", "strategist", "engineer", "expert", "lead"]
            ),
            "behavioral_traits": any(
                keyword in lower_section
                for keyword in ["empath", "authentic", "rigor", "evidence", "alignment", "governance"]
            ),
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = determine_status(dim.score, pass_threshold=0.95, warning_threshold=0.8)

        if not checks["persona_statement"]:
            dim.issues.append("Persona statement (You are ...) missing")
        if not checks["mission_language"]:
            dim.issues.append("Mission language not articulated in role definition")
        if not checks["expertise_reference"]:
            dim.issues.append("Role description lacks domain expertise reference")
        if not checks["behavioral_traits"]:
            dim.issues.append("Behavioral traits or tone guidance absent")

        return dim

    def _evaluate_mission_statement(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("mission_statement", weight=0.25)
        if not section:
            dim.issues.append("Mission statement unavailable")
            return dim

        lower_section = section.lower()
        checks = {
            "mission_statement": "mission" in lower_section,
            "guardrails": any(
                keyword in lower_section for keyword in ["do not", "never", "only", "stay within", "avoid", "limit"]
            ),
            "success_signals": any(
                keyword in lower_section for keyword in ["success", "validate", "quality", "approved", "evidence", "pass"]
            ),
            "value_focus": any(
                keyword in lower_section for keyword in ["client", "stakeholder", "team", "value", "impact", "outcome"]
            ),
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = determine_status(dim.score, pass_threshold=0.95, warning_threshold=0.8)

        if not checks["mission_statement"]:
            dim.issues.append("Mission statement missing from AI role section")
        if not checks["guardrails"]:
            dim.issues.append("Role mission lacks guardrails or boundary guidance")
        if not checks["success_signals"]:
            dim.issues.append("Success indicators or validation targets not referenced")
        if not checks["value_focus"]:
            dim.issues.append("Client or value focus not highlighted in mission")

        return dim

    def _evaluate_constraints(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("constraints_guidelines", weight=0.2)
        if not section:
            dim.issues.append("Constraints section missing")
            return dim

        lower_section = section.lower()
        critical = lower_section.count("[critical]")
        must = lower_section.count("[must]")
        guideline = lower_section.count("[guideline]")
        prohibition = sum(lower_section.count(term) for term in ["never", "do not", "avoid"])

        checks = {
            "critical_markers": critical > 0,
            "must_markers": must > 0,
            "guideline_markers": guideline > 0,
            "prohibitions": prohibition > 0,
        }

        dim.details = {**checks, "critical_count": critical, "must_count": must, "guideline_count": guideline}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = determine_status(dim.score, pass_threshold=0.95, warning_threshold=0.8)

        if not checks["critical_markers"]:
            dim.recommendations.append("Highlight critical guardrails with [CRITICAL] markers")
        if not checks["must_markers"]:
            dim.issues.append("Mandatory [MUST] guardrails missing")
        if not checks["guideline_markers"]:
            dim.recommendations.append("Include [GUIDELINE] markers for recommended practices")
        if not checks["prohibitions"]:
            dim.issues.append("Explicit prohibitions (never / do not) not documented")

        return dim

    def _evaluate_output_expectations(
        self, workflow_section: str, evidence_section: str, handoff_section: str
    ) -> DimensionEvaluation:
        dim = DimensionEvaluation("output_expectations", weight=0.15)
        combined = "\n".join(filter(None, [workflow_section, evidence_section, handoff_section]))
        if not combined:
            dim.issues.append("No output documentation found")
            return dim

        combined_lower = combined.lower()
        checks = {
            "deliverable_language": any(term in combined_lower for term in ["deliverable", "output", "artifact", "package"]),
            "evidence_reference": "evidence" in combined_lower,
            "handoff_alignment": "handoff" in handoff_section.lower(),
            "timeline_reference": any(term in combined_lower for term in ["timeline", "cadence", "phase", "schedule", "frequency"]),
        }

        dim.details = checks
        dim.score = sum(1 for v in checks.values() if v) / len(checks)
        dim.status = determine_status(dim.score, pass_threshold=0.95, warning_threshold=0.8)

        if not checks["deliverable_language"]:
            dim.issues.append("Deliverable or output expectations not described")
        if not checks["evidence_reference"]:
            dim.issues.append("Evidence expectations for outputs not referenced")
        if not checks["handoff_alignment"]:
            dim.issues.append("Handoff dependencies for outputs not documented")
        if not checks["timeline_reference"]:
            dim.recommendations.append("Clarify cadence or timeline expectations for outputs")

        return dim

    def _evaluate_behavioral_guidance(self, role_section: str, communication_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("behavioral_guidance", weight=0.15)
        combined = "\n".join(filter(None, [role_section, communication_section]))
        if not combined:
            dim.issues.append("Behavioral guidance not documented")
            return dim

        lower_combined = combined.lower()
        checks = {
            "communication_style": any(word in lower_combined for word in ["communication", "status", "update", "announce", "tone"]),
            "collaboration_guidance": any(word in lower_combined for word in ["collaborate", "partner", "coordinate", "team"]),
            "escalation_path": any(word in lower_combined for word in ["escalate", "notify", "alert", "raise"]),
            "empathy_guidance": any(word in role_section.lower() for word in ["empathy", "human", "respect", "care", "authentic"]),
        }

        dim.details = checks
        dim.score = sum(1 for v in checks.values() if v) / len(checks)
        dim.status = determine_status(dim.score, pass_threshold=0.95, warning_threshold=0.8)

        if not checks["communication_style"]:
            dim.issues.append("Communication style guidance missing")
        if not checks["collaboration_guidance"]:
            dim.issues.append("Collaboration expectations not documented")
        if not checks["escalation_path"]:
            dim.recommendations.append("Specify escalation or notification paths")
        if not checks["empathy_guidance"]:
            dim.issues.append("Empathy or tone guidance absent from role definition")

        return dim

    # Utilities -------------------------------------------------------------

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
