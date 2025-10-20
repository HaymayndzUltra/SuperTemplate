#!/usr/bin/env python3
"""Protocol Quality Gates Validator."""

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


class ProtocolQualityGatesValidator:
    """Validates quality gate definitions, automation, and compliance."""

    KEY = "protocol_quality_gates"
    DIMENSION_KEYS = [
        "gate_definitions",
        "pass_criteria",
        "automation",
        "failure_handling",
        "compliance_integration",
    ]

    def __init__(self, workspace_root: Path) -> None:
        self.workspace_root = workspace_root
        self.output_dir = workspace_root / ".artifacts" / "validation"
        self.gate_config_dir = workspace_root / "config" / "protocol_gates"

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

        gates_section = extract_section(content, "QUALITY GATES")
        automation_section = extract_section(content, "AUTOMATION HOOKS")

        dimensions = [
            self._evaluate_gate_definitions(gates_section),
            self._evaluate_pass_criteria(gates_section),
            self._evaluate_automation(protocol_id, gates_section, automation_section),
            self._evaluate_failure_handling(gates_section),
            self._evaluate_compliance(gates_section, automation_section),
        ]

        for key, dim in zip(self.DIMENSION_KEYS, dimensions):
            result[key] = dim.to_dict()

        result["overall_score"] = compute_weighted_score(dimensions)
        result["validation_status"] = determine_status(result["overall_score"], pass_threshold=0.92, warning_threshold=0.85)

        issues, recommendations = gather_issues(dimensions)
        result["issues"].extend(issues)
        result["recommendations"].extend(recommendations)

        relax_for_documentation_protocol(
            protocol_id,
            result,
            note="Documentation-focused protocol detected; gate automation gaps recorded as recommendations.",
        )

        return result

    def _evaluate_gate_definitions(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("gate_definitions", weight=0.25)
        if not section:
            dim.issues.append("QUALITY GATES section missing")
            return dim

        gate_headers = re.findall(r"###\s+Gate\s+(\d+)", section)
        descriptions = re.findall(r"- \*\*Criteria\*\*:|Criteria:", section)
        types_present = re.findall(r"Prerequisite|Execution|Completion", section, flags=re.IGNORECASE)

        checks = {
            "gate_count": len(gate_headers) >= 2,
            "descriptions": len(descriptions) >= len(gate_headers),
            "types": len(types_present) > 0,
            "naming": all(name.isdigit() for name in gate_headers),
        }

        dim.details = {"gates": gate_headers, **checks}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if len(gate_headers) == 0:
            dim.issues.append("No gate headings defined")
        if not checks["descriptions"]:
            dim.issues.append("Gate criteria descriptions missing")
        if not checks["types"]:
            dim.recommendations.append("Identify gate types (Prerequisite/Execution/Completion)")

        return dim

    def _evaluate_pass_criteria(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("pass_criteria", weight=0.25)
        if not section:
            dim.issues.append("Cannot evaluate pass criteria without gate definitions")
            return dim

        thresholds = re.findall(r"Pass Threshold|threshold|≥|>=", section)
        boolean_checks = re.findall(r"status|pass|fail", section, flags=re.IGNORECASE)
        metrics = re.findall(r"score|confidence|rate|percentage", section, flags=re.IGNORECASE)

        checks = {
            "thresholds": len(thresholds) >= 2,
            "boolean": len(boolean_checks) >= 2,
            "metrics": len(metrics) >= 3,
            "evidence_links": section.lower().count("evidence") >= 3,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["thresholds"]:
            dim.issues.append("Numeric thresholds missing for gates")
        if not checks["metrics"]:
            dim.recommendations.append("Include quantitative metrics for gate evaluation")

        return dim

    def _evaluate_automation(self, protocol_id: str, gates_section: str, automation_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("automation", weight=0.2)
        combined = "\n".join(filter(None, [gates_section, automation_section]))
        if not combined:
            dim.issues.append("No automation references found")
            return dim

        script_mentions = re.findall(r"python3?\s+scripts/", combined)
        ci_mentions = re.findall(r"CI/CD|workflow|runs-on", combined)
        gate_file = self.gate_config_dir / f"{protocol_id}.yaml"
        config_exists = gate_file.exists()

        checks = {
            "scripts": len(script_mentions) >= 2,
            "ci": len(ci_mentions) > 0,
            "automation_labels": "Automation" in combined or "automation" in combined.lower(),
        }

        dim.details = {
            **checks,
            "script_mentions": len(script_mentions),
            "gate_config_path": str(gate_file),
            "gate_config_present": config_exists,
        }
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not config_exists:
            dim.recommendations.append(
                f"Provision config/protocol_gates/{protocol_id}.yaml when automated gating is expected"
            )
            if dim.status == "pass":
                dim.status = "warning"
        if len(script_mentions) < 2:
            dim.recommendations.append("Document executable automation commands for gates")
        if not checks["ci"]:
            dim.recommendations.append("Reference CI/CD workflow integration for gates")

        return dim

    def _evaluate_failure_handling(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("failure_handling", weight=0.15)
        if not section:
            dim.issues.append("No gate documentation to evaluate failure handling")
            return dim

        failure_mentions = re.findall(r"Failure Handling|on fail|if fails|fallback", section, flags=re.IGNORECASE)
        rollback_mentions = re.findall(r"rollback|remediation|re-run", section, flags=re.IGNORECASE)
        notification_mentions = re.findall(r"notify|alert|escalate", section, flags=re.IGNORECASE)
        waiver_mentions = re.findall(r"waiver|override", section, flags=re.IGNORECASE)

        checks = {
            "failure_actions": len(failure_mentions) >= 2,
            "rollback": len(rollback_mentions) > 0,
            "notification": len(notification_mentions) > 0,
            "waivers": len(waiver_mentions) > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["failure_actions"]:
            dim.issues.append("Failure handling steps not described")
        if not checks["notification"]:
            dim.recommendations.append("Identify notification path for gate failures")
        if not checks["waivers"]:
            dim.recommendations.append("Document waiver/override policies")

        return dim

    def _evaluate_compliance(self, gates_section: str, automation_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("compliance_integration", weight=0.15)
        combined = "\n".join(filter(None, [gates_section, automation_section]))
        if not combined:
            dim.issues.append("Compliance expectations not described")
            return dim

        compliance_terms = ["hipaa", "soc2", "gdpr", "iso", "pci", "fedramp", "security", "regulatory"]
        matches = [term for term in compliance_terms if term in combined.lower()]
        automation_terms = ["check", "validate", "enforce", "audit"]
        automation_mentions = [term for term in automation_terms if term in combined.lower()]

        checks = {
            "compliance_terms": len(matches) >= 2,
            "automation_hooks": len(automation_mentions) >= 2,
            "evidence": combined.lower().count("report") > 0,
            "governance": "governance" in combined.lower() or "policy" in combined.lower(),
        }

        dim.details = {"compliance_terms": matches, **checks}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if len(matches) < 2:
            dim.issues.append("Insufficient compliance standards referenced")
        if not checks["automation_hooks"]:
            dim.recommendations.append("Link compliance checks to automation commands")

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
        output_file = self.output_dir / f"protocol-{result['protocol_id']}-quality-gates.json"
        write_json(output_file, result)
        return output_file

    def generate_summary(self, results: List[Dict[str, Any]]) -> Path:
        metrics = aggregate_dimension_metrics(results, self.DIMENSION_KEYS)
        return generate_summary(self.KEY, results, self.output_dir, extra_fields={"dimensions": metrics})


def run_cli(args: argparse.Namespace) -> int:
    workspace_root = Path(args.workspace).resolve()
    validator = ProtocolQualityGatesValidator(workspace_root)
    results: List[Dict[str, Any]] = []

    if args.protocol:
        result = validator.validate_protocol(args.protocol)
        results.append(result)
        output_path = validator.save_result(result)
        print(f"✅ Quality gates validation complete for Protocol {args.protocol} -> {output_path}")
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
    parser = argparse.ArgumentParser(description="Validate quality gates and automation readiness")
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
