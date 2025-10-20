#!/usr/bin/env python3
"""Protocol Script Integration Validator."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

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
    status_icon,
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
        self._registry_data: Optional[Dict[str, Any]] = None
        self._registry_flat: Optional[Set[str]] = None

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

        commands = self._extract_commands(section)
        script_paths = self._extract_script_paths(commands)
        python_commands = [cmd for cmd in commands if cmd.strip().startswith(("python", "python3"))]
        shell_commands = [cmd for cmd in commands if cmd.strip().startswith("bash") or cmd.strip().startswith("./")]
        missing_files = [
            path for path in script_paths if not (self.workspace_root / path).exists()
        ]

        dim.details = {
            "command_count": len(commands),
            "python_commands": python_commands[:5],
            "shell_commands": shell_commands[:5],
            "script_paths": script_paths,
            "missing_files": missing_files,
        }

        coverage = min(1.0, len(commands) / 5)
        dim.score = coverage
        dim.status = determine_status(dim.score, pass_threshold=0.95, warning_threshold=0.7)

        if len(commands) < 3:
            dim.issues.append("Insufficient automation commands listed")
            dim.recommendations.append("Document end-to-end automation steps for the protocol")
        if missing_files:
            dim.issues.append(
                "Referenced automation scripts not found: " + ", ".join(sorted(set(missing_files)))
            )

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
        ownership_callout = any(term in combined.lower() for term in ["owner", "responsible", "team"])

        commands = self._extract_commands(automation_section)
        script_paths = self._extract_script_paths(commands)
        registered_paths = self._registered_scripts() if has_registry_file else set()
        unregistered = [path for path in script_paths if path not in registered_paths]

        commands_registered = True if not script_paths else len(unregistered) == 0

        core_checks = {
            "registry_file": has_registry_file,
            "commands_registered": commands_registered,
        }
        optional_checks = {
            "registry_reference": mention_present,
            "workflow_mapping": cross_links,
            "ownership_documented": ownership_callout,
        }

        optional_score = (
            sum(1 for value in optional_checks.values() if value) / len(optional_checks)
            if optional_checks
            else 0.0
        )
        core_score = sum(1 for value in core_checks.values() if value) / len(core_checks)
        dim.score = min(1.0, 0.6 * core_score + 0.4 * optional_score)
        dim.status = determine_status(dim.score, pass_threshold=0.9, warning_threshold=0.75)

        dim.details = {
            **core_checks,
            **optional_checks,
            "documented_commands": script_paths,
            "unregistered_commands": unregistered,
            "registry_file_path": str(self.registry_file),
        }

        if not has_registry_file:
            dim.issues.append(f"Registry file not found: {self.registry_file}")
        if unregistered:
            dim.issues.append(
                "Commands missing from registry: " + ", ".join(sorted(set(unregistered)))
            )
        if not mention_present:
            dim.recommendations.append(
                "Reference script registry guidance so operators know where commands are cataloged"
            )
        if not cross_links:
            dim.recommendations.append("Map automation hooks back to workflow steps")
        if not ownership_callout:
            dim.recommendations.append("Note automation owners or reviewers for governance clarity")

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

        core_checks = {"environment": environment}
        optional_checks = {
            "ci_context": ci_context,
            "scheduling": scheduling,
            "permissions": permissions,
        }

        optional_score = (
            sum(1 for value in optional_checks.values() if value) / len(optional_checks)
            if optional_checks
            else 0.0
        )
        core_score = sum(1 for value in core_checks.values() if value) / len(core_checks)
        dim.score = min(1.0, 0.65 * core_score + 0.35 * optional_score)
        dim.status = determine_status(dim.score, pass_threshold=0.9, warning_threshold=0.7)

        dim.details = {**core_checks, **optional_checks}

        if not environment:
            dim.issues.append("Document runtime environment or dependency prerequisites")
        if not ci_context:
            dim.recommendations.append("Reference CI/CD pipelines or automation triggers (optional)")
        if not scheduling:
            dim.recommendations.append("Mention scheduling or triggers for recurring automation (optional)")
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

    def _extract_commands(self, section: str) -> List[str]:
        if not section:
            return []
        return re.findall(r"(?:python3?|bash|\./)\s+[^`\n]+", section)

    def _extract_script_paths(self, commands: List[str]) -> List[str]:
        paths: List[str] = []
        for command in commands:
            match = re.search(r"scripts/[\w_\-/\.]+", command)
            if match:
                normalized = match.group(0).replace("./", "").lstrip("./")
                paths.append(normalized)
        return paths

    def _registered_scripts(self) -> Set[str]:
        if self._registry_flat is not None:
            return self._registry_flat

        data = self._load_registry_data()
        collected: Set[str] = set()

        def _collect(value: Any) -> None:
            if isinstance(value, str):
                collected.add(value)
            elif isinstance(value, list):
                for item in value:
                    _collect(item)
            elif isinstance(value, dict):
                for item in value.values():
                    _collect(item)

        _collect(data)
        self._registry_flat = collected
        return self._registry_flat

    def _load_registry_data(self) -> Dict[str, Any]:
        if self._registry_data is not None:
            return self._registry_data

        if not self.registry_file.exists():
            self._registry_data = {}
            return self._registry_data

        try:
            self._registry_data = json.loads(self.registry_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            self._registry_data = {}
        return self._registry_data

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
        status = result.get("validation_status")
        icon = status_icon(status)
        score = result.get("overall_score")
        score_text = (
            f" (score: {score:.3f})" if isinstance(score, (int, float)) else ""
        )
        print(
            f"{icon} Script integration validation complete for Protocol {args.protocol} -> {output_path}{score_text}"
        )
        if status:
            print(f"   Status: {status.upper()}")
    elif args.all:
        for protocol_id in resolve_protocol_ids(include_docs=args.include_docs):
            result = validator.validate_protocol(protocol_id)
            results.append(result)
            validator.save_result(result)
            icon = status_icon(result.get("validation_status"))
            print(
                f"{icon} Protocol {protocol_id}: {result['validation_status'].upper()} (score: {result['overall_score']:.3f})"
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
