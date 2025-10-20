#!/usr/bin/env python3
"""Protocol Quality Gates Validator."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

from validator_utils import (
    DimensionEvaluation,
    aggregate_dimension_metrics,
    build_base_result,
    compute_weighted_score,
    determine_status,
    documentation_protocol_recommendation,
    extract_section,
    gather_issues,
    generate_summary,
    get_protocol_file,
    is_documentation_protocol,
    read_protocol_content,
    resolve_protocol_ids,
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
        if is_documentation_protocol(protocol_id):
            result["validation_status"] = "warning"
            result["recommendations"].append(documentation_protocol_recommendation())
            return result
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

        script_mentions = re.findall(r"python3?\s+scripts/[\w_\-/]+", combined)
        ci_mentions = re.findall(r"CI/CD|workflow|runs-on", combined)
        gate_file = self.gate_config_dir / f"{protocol_id}.yaml"

        core_checks = {
            "script_commands": len(script_mentions) >= 1,
            "automation_language": "automation" in combined.lower(),
        }
        optional_checks = {
            "ci_context": len(ci_mentions) > 0,
            "gate_config_present": gate_file.exists(),
        }

        optional_score = (
            sum(1 for value in optional_checks.values() if value) / len(optional_checks)
            if optional_checks
            else 0.0
        )
        core_score = sum(1 for value in core_checks.values() if value) / len(core_checks)
        dim.score = min(1.0, 0.7 * core_score + 0.3 * optional_score)
        dim.status = determine_status(dim.score, pass_threshold=0.9, warning_threshold=0.7)

        dim.details = {
            **core_checks,
            **optional_checks,
            "script_mentions": len(script_mentions),
            "gate_config_path": str(gate_file),
        }

        if not core_checks["script_commands"]:
            dim.issues.append("No executable automation commands documented for gates")
        if len(script_mentions) < 2:
            dim.recommendations.append("Document multiple gate execution commands to cover each checkpoint")
        if not optional_checks["ci_context"]:
            dim.recommendations.append("Reference CI/CD or scheduling context for automation (optional)")
        if not optional_checks["gate_config_present"]:
            dim.recommendations.append(
                f"Gate configuration YAML not found ({gate_file}). Provide template or confirm manual governance"
            )

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
        for protocol_id in resolve_protocol_ids(include_docs=args.include_docs):
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
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    parser.add_argument(
        "--include-docs",
        action="store_true",
        help="Include documentation protocols 24-27 in iteration",
    )
    parser.add_argument("--workspace", default=".", help="Workspace root (defaults to current directory)")

    args = parser.parse_args()
    exit_code = run_cli(args)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
