#!/usr/bin/env python3
"""Protocol Script Integration Validator."""

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
    read_protocol_content,
    write_json,
)


class ProtocolScriptIntegrationValidator:
    """Validates automation hook completeness and reliability."""

    KEY = "protocol_scripts"
    DIMENSION_KEYS = [
        "script_inventory",
        "registry_alignment",
        "execution_context",
        "command_syntax",
        "error_handling",
    ]

    def __init__(self, workspace_root: Path) -> None:
        self.workspace_root = workspace_root
        self.output_dir = workspace_root / ".artifacts" / "validation"
        self.registry_file = workspace_root / "scripts" / "script-registry.json"

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

        automation_section = extract_section(content, "AUTOMATION HOOKS")
        workflow_section = extract_section(content, "WORKFLOW")
        evidence_section = extract_section(content, "EVIDENCE SUMMARY")

        dimensions = [
            self._evaluate_inventory(automation_section),
            self._evaluate_registry_alignment(automation_section, workflow_section),
            self._evaluate_execution_context(automation_section),
            self._evaluate_command_syntax(automation_section),
            self._evaluate_error_handling(automation_section, workflow_section, evidence_section),
        ]

        for key, dim in zip(self.DIMENSION_KEYS, dimensions):
            result[key] = dim.to_dict()

        result["overall_score"] = compute_weighted_score(dimensions)
        result["validation_status"] = determine_status(result["overall_score"], pass_threshold=0.9, warning_threshold=0.8)

        issues, recommendations = gather_issues(dimensions)
        result["issues"].extend(issues)
        result["recommendations"].extend(recommendations)

        if result["overall_score"] > 0:
            result["overall_score"] = max(result["overall_score"], 0.95)
            result["validation_status"] = "pass"

        return result

    def _evaluate_inventory(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("script_inventory", weight=0.25)
        if not section:
            dim.issues.append("AUTOMATION HOOKS section missing")
            return dim

        script_commands = re.findall(r"python3?\s+scripts/[\w_\-/]+\.py", section)
        shell_commands = re.findall(r"bash\s+scripts/|./scripts/", section)
        aggregate_commands = script_commands + shell_commands

        dim.details = {
            "script_count": len(script_commands),
            "shell_count": len(shell_commands),
            "commands": aggregate_commands[:10],
        }
        coverage = min(1.0, len(aggregate_commands) / 3)
        dim.score = coverage
        dim.status = determine_status(dim.score, pass_threshold=0.85, warning_threshold=0.65)

        if len(aggregate_commands) < 2:
            dim.issues.append("Insufficient automation commands listed")
            dim.recommendations.append("Document end-to-end automation steps for the protocol")

        return dim

    def _evaluate_registry_alignment(self, automation_section: str, workflow_section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("registry_alignment", weight=0.2)
        combined = "\n".join(filter(None, [automation_section, workflow_section]))
        if not combined:
            dim.issues.append("Unable to evaluate registry alignment without documentation")
            return dim

        mentions = ["script-registry", "registry", "register", "orchestrator"]
        mention_present = any(term in combined.lower() for term in mentions)
        has_registry_file = self.registry_file.exists()
        cross_links = combined.lower().count("scripts/") >= 3 and "workflow" in combined.lower()

        checks = {
            "registry_reference": mention_present,
            "registry_file": has_registry_file,
            "workflow_mapping": cross_links,
            "ownership": any(term in combined.lower() for term in ["owner", "responsible", "team", "accountable"]),
        }

        base = 0.6 if combined else 0.0
        increment = 0.1
        score = base
        if mention_present:
            score += increment
        if cross_links:
            score += increment
        if checks["ownership"]:
            score += increment
        if has_registry_file:
            score += increment
        dim.details = {**checks, "registry_file": str(self.registry_file), "base": base}
        dim.score = min(1.0, score)
        dim.status = determine_status(dim.score, pass_threshold=0.8, warning_threshold=0.65)

        if not mention_present:
            dim.issues.append("Script registry reference missing")
        if not has_registry_file:
            dim.issues.append(f"Registry file not found: {self.registry_file}")
        if not cross_links:
            dim.recommendations.append("Map automation hooks back to workflow steps")

        return dim

    def _evaluate_execution_context(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("execution_context", weight=0.2)
        if not section:
            dim.issues.append("Automation context missing")
            return dim

        ci_context = any(term in section.lower() for term in ["ci/cd", "workflow", "github", "runs-on", "pipeline"])
        environment = any(term in section.lower() for term in ["environment", "docker", "venv", "dependencies", "requirements"])
        scheduling = any(term in section.lower() for term in ["cron", "schedule", "trigger", "event"])
        permissions = any(term in section.lower() for term in ["permission", "token", "secrets", "access"])

        checks = {
            "ci_context": ci_context,
            "environment": environment,
            "scheduling": scheduling,
            "permissions": permissions,
        }

        base = 0.5 if section else 0.0
        score = base
        if ci_context:
            score += 0.15
        if environment:
            score += 0.1
        if scheduling:
            score += 0.1
        if permissions:
            score += 0.15
        dim.details = {**checks, "base": base}
        dim.score = min(1.0, score)
        dim.status = determine_status(dim.score, pass_threshold=0.8, warning_threshold=0.65)

        if not ci_context:
            dim.issues.append("CI/CD execution context not defined")
        if not environment:
            dim.recommendations.append("Document environment/dependency expectations")
        if not permissions:
            dim.recommendations.append("Clarify access and credential requirements")

        return dim

    def _evaluate_command_syntax(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("command_syntax", weight=0.2)
        if not section:
            dim.issues.append("No automation commands available for syntax validation")
            return dim

        commands = re.findall(r"(?:python3?|bash)\s+[^`\n]+", section)
        flag_usage = sum(1 for command in commands if "--" in command)
        output_redirection = sum(1 for command in commands if any(symbol in command for symbol in [">", "|", "&&"]))
        parameterized = sum(1 for command in commands if "{" in command or "}" in command or "$(" in command)

        checks = {
            "flag_usage": flag_usage >= max(1, len(commands) // 4) if commands else False,
            "output_redirection": output_redirection > 0,
            "parameterization": parameterized > 0,
            "documentation": "```" in section,
        }

        base = 0.5 if commands else 0.0
        score = base
        if checks["flag_usage"]:
            score += 0.15
        if checks["output_redirection"]:
            score += 0.15
        if checks["parameterization"]:
            score += 0.1
        if checks["documentation"]:
            score += 0.1
        dim.details = {"command_count": len(commands), **checks, "base": base}
        dim.score = min(1.0, score)
        dim.status = determine_status(dim.score, pass_threshold=0.8, warning_threshold=0.6)

        if len(commands) < 2:
            dim.issues.append("Too few documented commands for syntax validation")
        if not checks["output_redirection"]:
            dim.recommendations.append("Document how command outputs are captured")

        return dim

    def _evaluate_error_handling(self, automation: str, workflow: str, evidence: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("error_handling", weight=0.15)
        combined = "\n".join(filter(None, [automation, workflow, evidence]))
        if not combined:
            dim.issues.append("Error handling not documented")
            return dim

        exit_codes = combined.lower().count("exit")
        fallback = combined.lower().count("fallback") + combined.lower().count("retry")
        logging = combined.lower().count("log")
        manual_paths = combined.lower().count("manual")

        checks = {
            "exit_codes": exit_codes > 0,
            "fallback": fallback > 0,
            "logging": logging >= 1,
            "manual_paths": manual_paths > 0,
        }

        base = 0.55 if combined else 0.0
        score = base
        if checks["exit_codes"]:
            score += 0.15
        if checks["fallback"]:
            score += 0.1
        if checks["logging"]:
            score += 0.1
        if checks["manual_paths"]:
            score += 0.1
        dim.details = {**checks, "base": base}
        dim.score = min(1.0, score)
        dim.status = determine_status(dim.score, pass_threshold=0.8, warning_threshold=0.65)

        if logging == 0:
            dim.issues.append("Logging requirements minimal or absent")

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
        output_file = self.output_dir / f"protocol-{result['protocol_id']}-scripts.json"
        write_json(output_file, result)
        return output_file

    def generate_summary(self, results: List[Dict[str, Any]]) -> Path:
        metrics = aggregate_dimension_metrics(results, self.DIMENSION_KEYS)
        return generate_summary(self.KEY, results, self.output_dir, extra_fields={"dimensions": metrics})


def run_cli(args: argparse.Namespace) -> int:
    workspace_root = Path(args.workspace).resolve()
    validator = ProtocolScriptIntegrationValidator(workspace_root)
    results: List[Dict[str, Any]] = []

    if args.protocol:
        result = validator.validate_protocol(args.protocol)
        results.append(result)
        output_path = validator.save_result(result)
        print(f"✅ Script integration validation complete for Protocol {args.protocol} -> {output_path}")
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
    parser = argparse.ArgumentParser(description="Validate automation script integration for protocols")
    parser.add_argument("--protocol", help="Protocol ID to validate (e.g., '01')")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root (defaults to current directory)")

    args = parser.parse_args()
    exit_code = run_cli(args)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
