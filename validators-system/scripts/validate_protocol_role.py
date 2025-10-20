#!/usr/bin/env python3
"""Validator 2 - AI Role and Mission"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict

from validator_utils import (
    BaseProtocolValidator,
    DimensionResult,
    collect_section_text,
    contains_any,
    find_markers,
    normalize_score,
    run_cli,
)


class AIRoleValidator(BaseProtocolValidator):
    slug = "ai-role"
    name = "AI Role Validator"
    dimension_weights = {
        "role_definition": 0.25,
        "mission_statement": 0.25,
        "constraints": 0.20,
        "output_expectations": 0.15,
        "behavioral_guidance": 0.15,
    }
    pass_threshold = 0.92
    warning_threshold = 0.8

    def evaluate_dimensions(self, protocol_id: str, content: str) -> Dict[str, DimensionResult]:
        role_text = collect_section_text(content, ["AI ROLE", "ROLE AND MISSION", "ROLE & MISSION"])
        mission_text = role_text
        communication_text = collect_section_text(content, ["COMMUNICATION", "STATUS", "ANNOUNCEMENT"])
        workflow_text = collect_section_text(content, ["WORKFLOW", "DELIVERABLE", "OUTPUT"])
        evidence_text = collect_section_text(content, ["EVIDENCE", "SUMMARY"])
        combined_output = "\n".join(filter(None, [role_text, workflow_text, evidence_text]))

        dimensions: Dict[str, DimensionResult] = {}

        # Dimension 2.1 - Role Definition
        title_present = contains_any(role_text, ["You are", "Role:", "persona", "You act as"])
        description_present = len(role_text.splitlines()) >= 3
        expertise_present = contains_any(role_text, ["expert", "expertise", "specialist", "domain", "experience"])
        traits_present = contains_any(role_text, ["tone", "empat", "decisive", "collaborative", "proactive", "behavior"])
        findings = {
            "title": title_present,
            "description": description_present,
            "domain_expertise": expertise_present,
            "behavioral_traits": traits_present,
        }
        issues = []
        if not title_present:
            issues.append("Role title not clearly defined.")
        if not description_present:
            issues.append("Role description missing supporting details.")
        if not expertise_present:
            issues.append("Domain expertise not documented.")
        if not traits_present:
            issues.append("Behavioral traits not described.")

        if all(findings.values()):
            status = "pass"
        elif title_present and description_present:
            status = "warning"
        else:
            status = "fail"
        score = normalize_score(status)
        dimensions["role_definition"] = DimensionResult(status, score, findings, issues, [])

        # Dimension 2.2 - Mission Statement
        mission_clarity = contains_any(mission_text, ["mission", "objective", "goal", "charter"])
        scope_boundaries = contains_any(mission_text, ["scope", "out of scope", "boundaries", "within", "outside"])
        success_criteria = contains_any(mission_text, ["success", "definition of done", "complete", "approval"])
        value_proposition = contains_any(mission_text, ["value", "impact", "client benefit", "why this matters"])
        mission_findings = {
            "mission": mission_clarity,
            "scope": scope_boundaries,
            "success": success_criteria,
            "value": value_proposition,
        }
        mission_issues = []
        if not mission_clarity:
            mission_issues.append("Mission statement missing.")
        if not scope_boundaries:
            mission_issues.append("Scope boundaries not defined.")
        if not success_criteria:
            mission_issues.append("Success criteria absent.")
        if not value_proposition:
            mission_issues.append("Value proposition not articulated.")

        mission_score_state = "pass" if sum(mission_findings.values()) >= 3 else "warning" if mission_clarity else "fail"
        mission_score = normalize_score(mission_score_state)
        dimensions["mission_statement"] = DimensionResult(
            mission_score_state,
            mission_score,
            mission_findings,
            mission_issues,
            [],
        )

        # Dimension 2.3 - Constraints & Guidelines
        marker_counts = find_markers(role_text, ["[CRITICAL]", "[MUST]", "[GUIDELINE]", "[SHOULD]", "[WARNING]"])
        critical_present = marker_counts.get("[CRITICAL]", 0) > 0
        must_present = marker_counts.get("[MUST]", 0) > 0
        guideline_present = (marker_counts.get("[GUIDELINE]", 0) + marker_counts.get("[SHOULD]", 0)) > 0
        prohibitions_present = contains_any(role_text, ["never", "do not", "avoid", "prohibit"])
        constraint_findings = {
            "critical_constraints": critical_present,
            "must_rules": must_present,
            "guidelines": guideline_present,
            "prohibitions": prohibitions_present,
        }
        constraint_issues = []
        if not critical_present:
            constraint_issues.append("[CRITICAL] constraint missing.")
        if not must_present:
            constraint_issues.append("[MUST] rules absent.")
        if not guideline_present:
            constraint_issues.append("Guideline markers missing.")
        if not prohibitions_present:
            constraint_issues.append("No explicit prohibitions found.")

        if critical_present and must_present and (guideline_present or prohibitions_present):
            constraint_status = "pass"
        elif must_present or guideline_present:
            constraint_status = "warning"
        else:
            constraint_status = "fail"
        constraint_score = normalize_score(constraint_status)
        dimensions["constraints"] = DimensionResult(
            constraint_status,
            constraint_score,
            constraint_findings,
            constraint_issues,
            [],
        )

        # Dimension 2.4 - Output Expectations
        format_present = contains_any(combined_output, ["markdown", "json", "yaml", "table", "report"])
        structure_present = contains_any(combined_output, ["section", "template", "include", "structured"])
        location_present = contains_any(combined_output, [".artifacts", "store in", "save to", "output:" ])
        validation_present = contains_any(combined_output, ["validate", "quality", "review", "threshold", "score"])
        output_findings = {
            "format": format_present,
            "structure": structure_present,
            "location": location_present,
            "validation": validation_present,
        }
        output_issues = []
        if not format_present:
            output_issues.append("Output format not specified.")
        if not structure_present:
            output_issues.append("Output structure not defined.")
        if not location_present:
            output_issues.append("Output storage location missing.")
        if not validation_present:
            output_issues.append("Output validation criteria absent.")
        satisfied = sum(output_findings.values())
        if satisfied >= 3:
            output_status = "pass"
        elif satisfied >= 2:
            output_status = "warning"
        else:
            output_status = "fail"
        output_score = normalize_score(output_status)
        dimensions["output_expectations"] = DimensionResult(
            output_status,
            output_score,
            output_findings,
            output_issues,
            [],
        )

        # Dimension 2.5 - Behavioral Guidance
        combined_behavior = "\n".join(filter(None, [role_text, communication_text]))
        communication_style = contains_any(combined_behavior, ["tone", "communicate", "announce", "status", "style"])
        decision_making = contains_any(combined_behavior, ["decide", "choose", "prioritize", "decision"])
        error_handling = contains_any(combined_behavior, ["if blocked", "halt", "stop", "error", "escalate"])
        user_interaction = contains_any(combined_behavior, ["ask", "confirm", "request", "clarify", "feedback"])
        behavior_findings = {
            "communication_style": communication_style,
            "decision_making": decision_making,
            "error_handling": error_handling,
            "user_interaction": user_interaction,
        }
        behavior_issues = []
        if not communication_style:
            behavior_issues.append("Communication style not described.")
        if not decision_making:
            behavior_issues.append("Decision-making guidance missing.")
        if not error_handling:
            behavior_issues.append("Error handling behavior absent.")
        if not user_interaction:
            behavior_issues.append("User interaction guidance missing.")
        satisfied_behavior = sum(behavior_findings.values())
        if satisfied_behavior >= 3:
            behavior_status = "pass"
        elif satisfied_behavior >= 2:
            behavior_status = "warning"
        else:
            behavior_status = "fail"
        behavior_score = normalize_score(behavior_status)
        dimensions["behavioral_guidance"] = DimensionResult(
            behavior_status,
            behavior_score,
            behavior_findings,
            behavior_issues,
            [],
        )

        return dimensions


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AI role and mission definition for protocols")
    parser.add_argument("--protocol", help="Protocol ID to validate (e.g., 01)")
    parser.add_argument("--all", action="store_true", help="Validate all protocol files")
    parser.add_argument("--summary", action="store_true", help="Generate aggregated summary")
    parser.add_argument("--workspace", default=".", help="Workspace root path")
    args = parser.parse_args()

    workspace = Path(args.workspace)
    validator = AIRoleValidator(workspace)
    return run_cli(validator, args.protocol, args.all, args.summary)


if __name__ == "__main__":
    raise SystemExit(main())
