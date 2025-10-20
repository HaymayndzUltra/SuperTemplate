#!/usr/bin/env python3
"""Validator 4 - Quality Gates"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict

import yaml

from validator_utils import (
    BaseProtocolValidator,
    DimensionResult,
    collect_section_text,
    contains_any,
    extract_paths,
    find_markers,
    normalize_score,
    run_cli,
)


class QualityGatesValidator(BaseProtocolValidator):
    slug = "quality-gates"
    name = "Quality Gates Validator"
    dimension_weights = {
        "gate_definitions": 0.25,
        "pass_criteria": 0.25,
        "automation": 0.20,
        "failure_handling": 0.15,
        "compliance": 0.15,
    }
    pass_threshold = 0.92
    warning_threshold = 0.8

    def evaluate_dimensions(self, protocol_id: str, content: str) -> Dict[str, DimensionResult]:
        gates_text = collect_section_text(content, ["QUALITY GATES", "GATE"])
        config_path = self.workspace_root / "config" / "protocol_gates" / f"{protocol_id}.yaml"
        config_data = {}
        if config_path.exists():
            try:
                config_data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
            except yaml.YAMLError:
                config_data = {"error": "Failed to parse YAML"}
        dimensions: Dict[str, DimensionResult] = {}

        # Dimension 4.1 - Gate Definitions
        gate_mentions = [line for line in gates_text.splitlines() if line.lower().startswith("### gate")]
        config_gates = config_data.get("gates") if isinstance(config_data, dict) else None
        defined_in_config = isinstance(config_gates, list) and len(config_gates) > 0
        findings = {
            "gate_mentions": len(gate_mentions),
            "config_entries": len(config_gates) if isinstance(config_gates, list) else 0,
            "config_loaded": bool(config_data),
        }
        issues = []
        if not gates_text:
            issues.append("Quality gates section missing.")
        if len(gate_mentions) == 0:
            issues.append("No gate definitions documented in protocol.")
        if not defined_in_config:
            issues.append("No structured gate configuration found.")
        if len(gate_mentions) >= 2 and defined_in_config:
            status = "pass"
        elif gates_text or defined_in_config:
            status = "warning"
        else:
            status = "fail"
        score = normalize_score(status)
        dimensions["gate_definitions"] = DimensionResult(status, score, findings, issues, [])

        # Dimension 4.2 - Pass Criteria
        pass_lines = [line for line in gates_text.splitlines() if "Pass" in line or "Threshold" in line]
        criteria_from_config = []
        if isinstance(config_gates, list):
            for gate in config_gates:
                if isinstance(gate, dict) and gate.get("pass_criteria"):
                    criteria_from_config.append(gate["pass_criteria"])
        criteria_findings = {
            "protocol_criteria": len(pass_lines),
            "config_criteria": len(criteria_from_config),
        }
        criteria_issues = []
        if len(pass_lines) == 0:
            criteria_issues.append("No pass criteria in protocol text.")
        if len(criteria_from_config) == 0:
            criteria_issues.append("No pass criteria defined in configuration.")
        if pass_lines and criteria_from_config:
            criteria_status = "pass"
        elif pass_lines or criteria_from_config:
            criteria_status = "warning"
        else:
            criteria_status = "fail"
        criteria_score = normalize_score(criteria_status)
        dimensions["pass_criteria"] = DimensionResult(
            criteria_status,
            criteria_score,
            criteria_findings,
            criteria_issues,
            [],
        )

        # Dimension 4.3 - Automation
        automation_lines = [line for line in gates_text.splitlines() if "python" in line or "script" in line]
        referenced_paths = extract_paths("\n".join(automation_lines))
        existing_paths = [path for path in referenced_paths if (self.workspace_root / path).exists()]
        automation_findings = {
            "automation_references": len(automation_lines),
            "referenced_scripts": referenced_paths,
            "existing_scripts": existing_paths,
        }
        automation_issues = []
        if not automation_lines:
            automation_issues.append("No automation commands documented.")
        if len(existing_paths) < len(referenced_paths):
            automation_issues.append("Some referenced scripts missing in repository.")
        if automation_lines and existing_paths:
            automation_status = "pass"
        elif automation_lines:
            automation_status = "warning"
        else:
            automation_status = "fail"
        automation_score = normalize_score(automation_status)
        dimensions["automation"] = DimensionResult(
            automation_status,
            automation_score,
            automation_findings,
            automation_issues,
            [],
        )

        # Dimension 4.4 - Failure Handling
        failure_keywords = ["failure", "rollback", "retry", "notify", "escalate", "if gate fails"]
        failure_lines = [line for line in gates_text.splitlines() if any(word in line.lower() for word in failure_keywords)]
        failure_findings = {
            "failure_handling": len(failure_lines),
            "examples": failure_lines[:5],
        }
        failure_issues = []
        if not failure_lines:
            failure_issues.append("Failure handling not described.")
        if len(failure_lines) >= max(1, len(gate_mentions)):
            failure_status = "pass"
        elif failure_lines:
            failure_status = "warning"
        else:
            failure_status = "fail"
        failure_score = normalize_score(failure_status)
        dimensions["failure_handling"] = DimensionResult(
            failure_status,
            failure_score,
            failure_findings,
            failure_issues,
            [],
        )

        # Dimension 4.5 - Compliance Integration
        compliance_keywords = ["hipaa", "soc2", "gdpr", "iso", "regulatory", "compliance"]
        compliance_lines = [line for line in gates_text.splitlines() if any(word in line.lower() for word in compliance_keywords)]
        compliance_findings = {
            "compliance_references": len(compliance_lines),
            "examples": compliance_lines[:5],
        }
        compliance_issues = []
        if not compliance_lines:
            compliance_issues.append("Compliance integration not referenced in quality gates.")
        markers = find_markers(gates_text, ["[CRITICAL]", "[MUST]"])
        has_compliance_marker = markers.get("[CRITICAL]", 0) > 0 or markers.get("[MUST]", 0) > 0
        if compliance_lines and has_compliance_marker:
            compliance_status = "pass"
        elif compliance_lines:
            compliance_status = "warning"
        else:
            compliance_status = "fail"
        compliance_score = normalize_score(compliance_status)
        dimensions["compliance"] = DimensionResult(
            compliance_status,
            compliance_score,
            compliance_findings,
            compliance_issues,
            [],
        )

        return dimensions


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate protocol quality gates")
    parser.add_argument("--protocol", help="Protocol ID to validate")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--summary", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root path")
    args = parser.parse_args()

    validator = QualityGatesValidator(Path(args.workspace))
    return run_cli(validator, args.protocol, args.all, args.summary)


if __name__ == "__main__":
    raise SystemExit(main())
