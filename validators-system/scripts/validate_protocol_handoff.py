#!/usr/bin/env python3
"""Validator 8 - Handoff Checklist"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict

from validator_utils import (
    BaseProtocolValidator,
    DimensionResult,
    collect_section_text,
    count_checkboxes,
    normalize_score,
    run_cli,
)


class HandoffValidator(BaseProtocolValidator):
    slug = "handoff"
    name = "Handoff Checklist Validator"
    dimension_weights = {
        "checklist_completeness": 0.30,
        "verification_procedures": 0.25,
        "stakeholder_signoff": 0.20,
        "documentation_requirements": 0.15,
        "transition_support": 0.10,
    }
    pass_threshold = 0.9
    warning_threshold = 0.75

    def evaluate_dimensions(self, protocol_id: str, content: str) -> Dict[str, DimensionResult]:
        handoff_text = collect_section_text(content, ["HANDOFF", "CHECKLIST", "TRANSITION"])
        evidence_text = collect_section_text(content, ["EVIDENCE", "SUMMARY"])
        dimensions: Dict[str, DimensionResult] = {}

        # Dimension 8.1 - Checklist Completeness
        checkbox_count = count_checkboxes(handoff_text)
        checklist_findings = {
            "checkbox_count": checkbox_count,
        }
        checklist_issues = []
        if checkbox_count >= 6:
            checklist_status = "pass"
        elif checkbox_count >= 3:
            checklist_status = "warning"
        elif checkbox_count > 0:
            checklist_status = "warning"
            checklist_issues.append("Checklist too short to cover handoff requirements.")
        else:
            checklist_status = "fail"
            checklist_issues.append("No handoff checklist found.")
        checklist_score = normalize_score(checklist_status)
        dimensions["checklist_completeness"] = DimensionResult(
            checklist_status,
            checklist_score,
            checklist_findings,
            checklist_issues,
            [],
        )

        # Dimension 8.2 - Verification Procedures
        verification_keywords = ["verify", "validate", "script", "run", "check", "evidence"]
        verification_lines = [line for line in handoff_text.splitlines() if any(keyword in line.lower() for keyword in verification_keywords)]
        verification_findings = {
            "verification_lines": verification_lines[:10],
            "count": len(verification_lines),
        }
        verification_issues = []
        if len(verification_lines) >= 3:
            verification_status = "pass"
        elif verification_lines:
            verification_status = "warning"
        else:
            verification_status = "fail"
            verification_issues.append("Verification procedures not described.")
        verification_score = normalize_score(verification_status)
        dimensions["verification_procedures"] = DimensionResult(
            verification_status,
            verification_score,
            verification_findings,
            verification_issues,
            [],
        )

        # Dimension 8.3 - Stakeholder Sign-off
        stakeholder_keywords = ["stakeholder", "sign-off", "approval", "reviewer", "client"]
        stakeholder_lines = [line for line in handoff_text.splitlines() if any(keyword in line.lower() for keyword in stakeholder_keywords)]
        stakeholder_findings = {
            "stakeholder_lines": stakeholder_lines[:10],
            "count": len(stakeholder_lines),
        }
        stakeholder_issues = []
        if len(stakeholder_lines) >= 2:
            stakeholder_status = "pass"
        elif stakeholder_lines:
            stakeholder_status = "warning"
        else:
            stakeholder_status = "fail"
            stakeholder_issues.append("Stakeholder approvals not documented.")
        stakeholder_score = normalize_score(stakeholder_status)
        dimensions["stakeholder_signoff"] = DimensionResult(
            stakeholder_status,
            stakeholder_score,
            stakeholder_findings,
            stakeholder_issues,
            [],
        )

        # Dimension 8.4 - Documentation Requirements
        documentation_keywords = ["document", "summary", "report", "artifact", "store", "location"]
        documentation_lines = [line for line in (handoff_text + "\n" + evidence_text).splitlines() if any(keyword in line.lower() for keyword in documentation_keywords)]
        documentation_findings = {
            "documentation_lines": documentation_lines[:10],
            "count": len(documentation_lines),
        }
        documentation_issues = []
        if len(documentation_lines) >= 3:
            documentation_status = "pass"
        elif documentation_lines:
            documentation_status = "warning"
        else:
            documentation_status = "fail"
            documentation_issues.append("Documentation requirements missing from handoff.")
        documentation_score = normalize_score(documentation_status)
        dimensions["documentation_requirements"] = DimensionResult(
            documentation_status,
            documentation_score,
            documentation_findings,
            documentation_issues,
            [],
        )

        # Dimension 8.5 - Transition Support
        support_keywords = ["support", "contact", "escalation", "knowledge transfer", "training", "office hours"]
        support_lines = [line for line in handoff_text.splitlines() if any(keyword in line.lower() for keyword in support_keywords)]
        support_findings = {
            "support_lines": support_lines[:10],
            "count": len(support_lines),
        }
        support_issues = []
        if len(support_lines) >= 2:
            support_status = "pass"
        elif support_lines:
            support_status = "warning"
        else:
            support_status = "fail"
            support_issues.append("Transition support details not provided.")
        support_score = normalize_score(support_status)
        dimensions["transition_support"] = DimensionResult(
            support_status,
            support_score,
            support_findings,
            support_issues,
            [],
        )

        return dimensions


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate protocol handoff checklist")
    parser.add_argument("--protocol", help="Protocol ID to validate")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--summary", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root path")
    args = parser.parse_args()

    validator = HandoffValidator(Path(args.workspace))
    return run_cli(validator, args.protocol, args.all, args.summary)


if __name__ == "__main__":
    raise SystemExit(main())
