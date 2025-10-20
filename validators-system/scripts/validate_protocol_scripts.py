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
        self.registry_index = self._flatten_registry_entries(self.registry_data)

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
        command_entries = self._extract_command_entries(
            [automation_section, workflow_section]
        )

        dimensions = [
            self._evaluate_inventory(automation_section, command_entries),
            self._evaluate_registry_alignment(automation_section, workflow_section, command_entries),
            self._evaluate_execution_context(automation_section),
            self._evaluate_command_syntax(command_entries, automation_section),
            self._evaluate_error_handling(automation_section, workflow_section, evidence_section),
        ]

        for key, dim in zip(self.DIMENSION_KEYS, dimensions):
            result[key] = dim.to_dict()

        result["overall_score"] = compute_weighted_score(dimensions)
        result["validation_status"] = determine_status(result["overall_score"], pass_threshold=0.9, warning_threshold=0.8)

        issues, recommendations = gather_issues(dimensions)
        result["issues"].extend(issues)
        result["recommendations"].extend(recommendations)

        relax_for_documentation_protocol(
            protocol_id,
            result,
            note="Documentation-focused protocol detected; script integration gaps tracked as recommendations.",
        )

        return result

    def _evaluate_inventory(
        self, section: str, command_entries: List[Dict[str, Any]]
    ) -> DimensionEvaluation:
        dim = DimensionEvaluation("script_inventory", weight=0.25)
        if not section:
            dim.issues.append("AUTOMATION HOOKS section missing")
            return dim

        commands = [entry for entry in command_entries if entry["command"]]
        command_count = len(commands)
        missing_paths = [entry["script_path"] for entry in commands if entry["script_path"] and not entry["exists"]]

        dim.details = {
            "command_count": command_count,
            "commands": [entry["command"] for entry in commands[:10]],
            "missing_scripts": missing_paths,
        }
        coverage = min(1.0, command_count / 5)
        dim.score = coverage
        dim.status = determine_status(dim.score, pass_threshold=0.95, warning_threshold=0.7)

        if command_count < 3:
            dim.issues.append("Insufficient automation commands listed")
            dim.recommendations.append("Document end-to-end automation steps for the protocol")
        if missing_paths:
            dim.issues.append(
                "Referenced command paths not found: " + ", ".join(sorted(set(missing_paths)))
            )

        return dim

    def _evaluate_registry_alignment(
        self,
        automation_section: str,
        workflow_section: str,
        command_entries: List[Dict[str, Any]],
    ) -> DimensionEvaluation:
        dim = DimensionEvaluation("registry_alignment", weight=0.2)
        combined = "\n".join(filter(None, [automation_section, workflow_section]))
        if not combined:
            dim.issues.append("Unable to evaluate registry alignment without documentation")
            return dim

        mention_terms = ["script-registry", "registry", "register", "orchestrator"]
        mention_present = any(term in combined.lower() for term in mention_terms)
        has_registry_file = self.registry_file.exists()
        cross_links = combined.lower().count("scripts/") >= max(1, len(command_entries) // 2)
        ownership = any(term in combined.lower() for term in ["owner", "responsible", "team"])

        registered = [entry for entry in command_entries if entry["registered"]]
        total_commands = len(command_entries)
        registration_ratio = (
            len(registered) / total_commands if total_commands else 0.0
        )
        unregistered = [
            entry["script_path"]
            for entry in command_entries
            if entry["script_path"] and not entry["registered"] and entry["exists"]
        ]

        score_components = [registration_ratio]
        score_components.append(1.0 if mention_present else 0.0)
        score_components.append(1.0 if cross_links else 0.0)
        score_components.append(1.0 if ownership else 0.0)
        dim.score = sum(score_components) / len(score_components)
        dim.status = determine_status(dim.score, pass_threshold=0.9, warning_threshold=0.7)

        dim.details = {
            "registry_file": str(self.registry_file),
            "registry_available": has_registry_file,
            "registry_reference": mention_present,
            "workflow_mapping": cross_links,
            "ownership": ownership,
            "total_commands": total_commands,
            "registered_commands": len(registered),
            "registration_ratio": registration_ratio,
            "unregistered_commands": sorted(set(unregistered)),
        }

        if not has_registry_file:
            dim.issues.append(f"Registry file not found: {self.registry_file}")
        if not mention_present:
            dim.recommendations.append("Reference scripts/script-registry.json for governance context")
        if not cross_links:
            dim.recommendations.append("Map automation hooks back to workflow steps or phases")
        if unregistered:
            dim.recommendations.append(
                "Register automation commands in scripts/script-registry.json: "
                + ", ".join(sorted(set(unregistered)))
            )

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

        dim.details = checks
        dim.score = sum(1 for value in checks.values() if value) / len(checks)
        dim.status = self._status_from_counts(sum(checks.values()), len(checks))

        if not ci_context:
            dim.recommendations.append("Describe CI/CD context (workflow name, runner, or trigger)")
        if not environment:
            dim.recommendations.append("Document environment/dependency expectations")
        if not permissions:
            dim.recommendations.append("Clarify access and credential requirements")

        return dim

    def _evaluate_command_syntax(
        self, command_entries: List[Dict[str, Any]], section: str
    ) -> DimensionEvaluation:
        dim = DimensionEvaluation("command_syntax", weight=0.2)
        if not section:
            dim.issues.append("No automation commands available for syntax validation")
            return dim

        commands = [entry["command"] for entry in command_entries]
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

    def _load_registry(self) -> Dict[str, Any]:
        if not self.registry_file.exists():
            return {}
        try:
            return json.loads(self.registry_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}

    def _flatten_registry_entries(self, data: Any) -> List[str]:
        entries: List[str] = []

        def _collect(node: Any) -> None:
            if isinstance(node, str):
                entries.append(node.lstrip("./"))
            elif isinstance(node, list):
                for item in node:
                    _collect(item)
            elif isinstance(node, dict):
                for item in node.values():
                    _collect(item)

        _collect(data)
        return entries

    def _extract_command_entries(
        self, sections: List[str]
    ) -> List[Dict[str, Any]]:
        text = "\n".join(filter(None, sections))
        if not text:
            return []

        command_pattern = re.compile(r"(?:python3?|bash)\s+[^`\n]+")
        script_pattern = re.compile(r"(?:\./)?scripts/[\w\-/\.]+")
        entries: List[Dict[str, Any]] = []
        seen: Set[str] = set()

        for match in command_pattern.findall(text):
            command = match.strip()
            if command in seen:
                continue
            seen.add(command)
            script_match = script_pattern.search(command)
            script_path = script_match.group(0).lstrip("./") if script_match else ""
            script_path = script_path.rstrip(".,)")
            path_obj = self.workspace_root / script_path if script_path else None
            exists = bool(path_obj and path_obj.exists())
            registered = script_path in self.registry_index if script_path else False
            entries.append(
                {
                    "command": command,
                    "script_path": script_path,
                    "exists": exists,
                    "registered": registered,
                }
            )

        return entries

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
    parser = argparse.ArgumentParser(description="Validate automation script integration for protocols")
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
