#!/usr/bin/env python3
"""Validator 3 - Workflow Algorithm"""
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


class WorkflowValidator(BaseProtocolValidator):
    slug = "workflow"
    name = "Workflow Algorithm Validator"
    dimension_weights = {
        "workflow_structure": 0.20,
        "step_definitions": 0.25,
        "action_markers": 0.15,
        "halt_conditions": 0.20,
        "evidence_tracking": 0.20,
    }
    pass_threshold = 0.92
    warning_threshold = 0.8

    def evaluate_dimensions(self, protocol_id: str, content: str) -> Dict[str, DimensionResult]:
        workflow_text = collect_section_text(content, ["WORKFLOW"])
        if not workflow_text:
            workflow_text = ""
        dimensions: Dict[str, DimensionResult] = {}

        # Dimension 3.1 - Workflow Structure
        step_headings = len([line for line in workflow_text.splitlines() if line.strip().startswith("### STEP")])
        numbered_steps = len(set(find.strip().split(":")[0] for find in workflow_text.split("### ") if find.startswith("STEP")))
        has_structure = step_headings >= 3
        has_phases = contains_any(workflow_text, ["PHASE", "Stage", "Sprint"])
        structure_findings = {
            "step_headings": step_headings,
            "distinct_steps": numbered_steps,
            "phase_markers": has_phases,
        }
        structure_issues = []
        if not workflow_text:
            structure_issues.append("Workflow section missing.")
        if step_headings < 1:
            structure_issues.append("Workflow steps not defined with headings.")
        if not has_phases:
            structure_issues.append("No phase markers or context transitions found.")
        if has_structure and has_phases:
            structure_status = "pass"
        elif workflow_text:
            structure_status = "warning"
        else:
            structure_status = "fail"
        structure_score = normalize_score(structure_status)
        dimensions["workflow_structure"] = DimensionResult(
            structure_status,
            structure_score,
            structure_findings,
            structure_issues,
            [],
        )

        # Dimension 3.2 - Step Definitions
        action_lines = [line for line in workflow_text.splitlines() if "Action:" in line or line.strip().startswith("- ")]
        output_lines = [line for line in workflow_text.splitlines() if "Evidence:" in line or "Output" in line]
        numbering_ok = step_headings == numbered_steps and step_headings > 0
        definitions_findings = {
            "action_lines": len(action_lines),
            "output_lines": len(output_lines),
            "numbering_consistent": numbering_ok,
        }
        definition_issues = []
        if len(action_lines) < step_headings:
            definition_issues.append("Some steps missing action descriptions.")
        if len(output_lines) < step_headings:
            definition_issues.append("Some steps missing evidence/output definitions.")
        if not numbering_ok:
            definition_issues.append("Step numbering inconsistent.")
        if numbering_ok and len(action_lines) >= step_headings and len(output_lines) >= step_headings:
            definition_status = "pass"
        elif workflow_text:
            definition_status = "warning"
        else:
            definition_status = "fail"
        definition_score = normalize_score(definition_status)
        dimensions["step_definitions"] = DimensionResult(
            definition_status,
            definition_score,
            definitions_findings,
            definition_issues,
            [],
        )

        # Dimension 3.3 - Action Markers
        marker_counts = find_markers(workflow_text, ["[CRITICAL]", "[MUST]", "[GUIDELINE]", "[OPTIONAL]", "[STRICT]"])
        total_markers = sum(marker_counts.values())
        marker_findings = {"counts": marker_counts, "total": total_markers}
        marker_issues = []
        if marker_counts.get("[CRITICAL]", 0) == 0:
            marker_issues.append("No [CRITICAL] markers found.")
        if marker_counts.get("[MUST]", 0) == 0:
            marker_issues.append("No [MUST] markers present.")
        if total_markers == 0:
            marker_status = "fail"
        elif marker_counts.get("[CRITICAL]", 0) > 0 and marker_counts.get("[MUST]", 0) > 0:
            marker_status = "pass"
        else:
            marker_status = "warning"
        marker_score = normalize_score(marker_status)
        dimensions["action_markers"] = DimensionResult(
            marker_status,
            marker_score,
            marker_findings,
            marker_issues,
            [],
        )

        # Dimension 3.4 - Halt Conditions
        halt_keywords = ["halt", "stop", "pause", "block", "do not proceed", "if missing", "validation gate"]
        halt_matches = [line for line in workflow_text.splitlines() if any(word in line.lower() for word in halt_keywords)]
        halt_findings = {
            "halt_conditions": len(halt_matches),
            "examples": halt_matches[:5],
        }
        halt_issues = []
        if not halt_matches:
            halt_issues.append("Workflow lacks explicit halt conditions.")
        if len(halt_matches) >= max(1, step_headings // 2):
            halt_status = "pass"
        elif halt_matches:
            halt_status = "warning"
        else:
            halt_status = "fail"
        halt_score = normalize_score(halt_status)
        dimensions["halt_conditions"] = DimensionResult(
            halt_status,
            halt_score,
            halt_findings,
            halt_issues,
            [],
        )

        # Dimension 3.5 - Evidence Tracking
        evidence_lines = [line for line in workflow_text.splitlines() if ".artifacts" in line or "Evidence:" in line]
        tracking_findings = {
            "evidence_references": len(evidence_lines),
            "examples": evidence_lines[:5],
        }
        tracking_issues = []
        if not evidence_lines:
            tracking_issues.append("No evidence tracking references found in workflow.")
        elif len(evidence_lines) < step_headings:
            tracking_issues.append("Evidence tracking not defined for every step.")
        if evidence_lines and len(evidence_lines) >= step_headings:
            tracking_status = "pass"
        elif evidence_lines:
            tracking_status = "warning"
        else:
            tracking_status = "fail"
        tracking_score = normalize_score(tracking_status)
        dimensions["evidence_tracking"] = DimensionResult(
            tracking_status,
            tracking_score,
            tracking_findings,
            tracking_issues,
            [],
        )

        return dimensions


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate workflow algorithm structure")
    parser.add_argument("--protocol", help="Protocol ID to validate")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--summary", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root path")
    args = parser.parse_args()

    validator = WorkflowValidator(Path(args.workspace))
    return run_cli(validator, args.protocol, args.all, args.summary)


if __name__ == "__main__":
    raise SystemExit(main())
