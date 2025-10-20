#!/usr/bin/env python3
"""Protocol Script Integration Validator."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Set

from validator_utils import (
    DimensionEvaluation,
    aggregate_dimension_metrics,
    build_base_result,
    compute_weighted_score,
    determine_status,
    extract_section,
    gather_issues,
    generate_summary,
    get_protocol_file,
    get_protocol_id_list,
    is_documentation_protocol,
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
        self.registry_data = self._load_registry()
        self.registry_entries = self._flatten_registry(self.registry_data)

    def _load_registry(self) -> Dict[str, Any]:
        if not self.registry_file.exists():
            return {}
        try:
            return json.loads(self.registry_file.read_text(encoding="utf-8"))
        except Exception:
            return {}

    @staticmethod
    def _flatten_registry(data: Any) -> Set[str]:
        entries: Set[str] = set()
        if isinstance(data, dict):
            for value in data.values():
                entries.update(ProtocolScriptIntegrationValidator._flatten_registry(value))
        elif isinstance(data, list):
            for item in data:
                entries.update(ProtocolScriptIntegrationValidator._flatten_registry(item))
        elif isinstance(data, str):
            entries.add(data)
        return entries

    def validate_protocol(self, protocol_id: str) -> Dict[str, Any]:
        result = build_base_result(self.KEY, protocol_id)
        protocol_file = get_protocol_file(self.workspace_root, protocol_id)
        if not protocol_file:
            result["issues"].append(f"Protocol file not found for ID {protocol_id}")
            return result

        if is_documentation_protocol(protocol_id):
            result["overall_score"] = 1.0
            result["validation_status"] = "warning"
            result["recommendations"].append(
                "Documentation protocols (24-27) capture references; script integration validation skipped."
            )
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

        return result

    def _evaluate_inventory(self, section: str) -> DimensionEvaluation:
        dim = DimensionEvaluation("script_inventory", weight=0.25)
        if not section:
            dim.issues.append("AUTOMATION HOOKS section missing")
            return dim

        script_commands = re.findall(r"python3?\s+scripts/[\w_\-/]+\.py", section)
        shell_commands = re.findall(r"bash\s+scripts/|./scripts/", section)
        aggregate_commands = script_commands + shell_commands

        command_paths: List[str] = []
        for command in script_commands:
            match = re.search(r"python3?\s+(scripts/[\w_\-/]+\.(?:py|sh))", command)
            if match:
                command_paths.append(match.group(1))
        for command in shell_commands:
            match = re.search(r"(?:bash|./)\s*(scripts/[\w_\-/]+(?:\.[\w]+)?)", command)
            if match:
                command_paths.append(match.group(1))

        unique_paths = sorted(set(command_paths))
        unregistered: List[str] = []
        if self.registry_entries:
            unregistered = [path for path in unique_paths if path not in self.registry_entries]

        dim.details = {
            "script_count": len(script_commands),
            "shell_count": len(shell_commands),
            "commands": aggregate_commands[:10],
            "command_paths": unique_paths,
            "unregistered_commands": unregistered,
            "registry_entries_checked": len(self.registry_entries),
        }
        coverage = min(1.0, len(aggregate_commands) / 5)
        dim.score = coverage
        dim.status = determine_status(dim.score, pass_threshold=0.95, warning_threshold=0.7)

        if len(aggregate_commands) < 3:
            dim.issues.append("Insufficient automation commands listed")
            dim.recommendations.append("Document end-to-end automation steps for the protocol")
        if self.registry_entries and unregistered:
            dim.issues.append(
                "Unregistered automation commands detected: " + ", ".join(unregistered[:5])
            )
        elif not self.registry_entries:
            dim.recommendations.append("Script registry unavailable; run governance sync to register automation")

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
            "ownership": any(term in combined.lower() for term in ["owner", "responsible", "team"]),
        }

        dim.details = {
            **checks,
            "registry_file": str(self.registry_file),
            "registered_entries": len(self.registry_entries),
        }
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not mention_present:
            dim.recommendations.append("Reference the script registry or governance source for automation mapping")
        if not has_registry_file:
            dim.issues.append(f"Registry file not found: {self.registry_file}")
        elif has_registry_file and not self.registry_entries:
            dim.issues.append("Script registry file could not be parsed")
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

        optional_fields = {
            "ci_context": ci_context,
            "scheduling": scheduling,
            "permissions": permissions,
        }

        dim.details = {"environment": environment, **optional_fields}
        optional_count = sum(1 for value in optional_fields.values() if value)

        if environment:
            dim.score = min(1.0, 0.6 + (optional_count / max(len(optional_fields), 1)) * 0.4)
        else:
            dim.score = (optional_count / max(len(optional_fields), 1)) * 0.4

        dim.status = determine_status(dim.score, pass_threshold=0.85, warning_threshold=0.6)

        if not environment:
            dim.issues.append("Document environment/dependency expectations")

        if not ci_context:
            dim.recommendations.append("Reference CI/CD or workflow execution context (optional)")
        if not scheduling:
            dim.recommendations.append("Outline scheduling or trigger conditions for automation (optional)")
        if not permissions:
            dim.recommendations.append("Clarify access and credential requirements (optional)")

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
            "flag_usage": flag_usage >= max(1, len(commands) // 3),
            "output_redirection": output_redirection > 0,
            "parameterization": parameterized > 0,
            "documentation": "```" in section,
        }

        dim.details = {"command_count": len(commands), **checks}
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

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
            "logging": logging >= 2,
            "manual_paths": manual_paths > 0,
        }

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not checks["exit_codes"]:
            dim.issues.append("Exit code handling not described")
        if not checks["fallback"]:
            dim.recommendations.append("Document fallback or retry sequences for failures")
        if logging < 2:
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
        protocol_ids = get_protocol_id_list(include_docs=args.include_docs)
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
    parser = argparse.ArgumentParser(description="Validate automation script integration for protocols")
    parser.add_argument("--protocol", help="Protocol ID to validate (e.g., '01')")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root (defaults to current directory)")
    parser.add_argument(
        "--include-docs",
        action="store_true",
        help="Include documentation protocols (24-27) during --all runs",
    )

    args = parser.parse_args()
    exit_code = run_cli(args)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
