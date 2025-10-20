#!/usr/bin/env python3
"""Validator 5 - Script Integration"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Set

from validator_utils import (
    BaseProtocolValidator,
    DimensionResult,
    collect_section_text,
    contains_any,
    extract_paths,
    find_commands,
    normalize_score,
    run_cli,
)


class ScriptIntegrationValidator(BaseProtocolValidator):
    slug = "scripts"
    name = "Script Integration Validator"
    dimension_weights = {
        "script_references": 0.20,
        "script_existence": 0.25,
        "script_registration": 0.20,
        "command_syntax": 0.20,
        "error_handling": 0.15,
    }
    pass_threshold = 0.9
    warning_threshold = 0.75

    def __init__(self, workspace_root: Path):
        super().__init__(workspace_root)
        self.registry_path = self.workspace_root / "scripts" / "script-registry.json"
        self.registry_data = self._load_registry()

    def _load_registry(self) -> Dict[str, object]:
        if not self.registry_path.exists():
            return {}
        try:
            return json.loads(self.registry_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {"error": "invalid-json"}

    def evaluate_dimensions(self, protocol_id: str, content: str) -> Dict[str, DimensionResult]:
        automation_text = collect_section_text(content, ["AUTOMATION", "SCRIPT", "WORKFLOW", "PREREQUISITES"])
        dimensions: Dict[str, DimensionResult] = {}

        # Dimension 5.1 - Script References
        referenced_paths = [path for path in extract_paths(automation_text) if path.startswith("scripts/")]
        unique_references = sorted(set(referenced_paths))
        reference_findings = {
            "references": unique_references,
            "count": len(unique_references),
        }
        reference_issues = []
        if not unique_references:
            reference_issues.append("No script references documented in protocol.")
        if len(unique_references) >= 2:
            reference_status = "pass"
        elif unique_references:
            reference_status = "warning"
        else:
            reference_status = "fail"
        reference_score = normalize_score(reference_status)
        dimensions["script_references"] = DimensionResult(
            reference_status,
            reference_score,
            reference_findings,
            reference_issues,
            [],
        )

        # Dimension 5.2 - Script Existence
        existing_scripts = [path for path in unique_references if (self.workspace_root / path).exists()]
        existence_findings = {
            "existing_scripts": existing_scripts,
            "missing_scripts": [path for path in unique_references if path not in existing_scripts],
        }
        existence_issues = []
        if not unique_references:
            existence_status = "fail"
            existence_issues.append("Cannot validate script existence without references.")
        elif len(existing_scripts) == len(unique_references):
            existence_status = "pass"
        elif existing_scripts:
            existence_status = "warning"
            existence_issues.append("Some referenced scripts missing in repository.")
        else:
            existence_status = "fail"
            existence_issues.append("Referenced scripts not found in repository.")
        existence_score = normalize_score(existence_status)
        dimensions["script_existence"] = DimensionResult(
            existence_status,
            existence_score,
            existence_findings,
            existence_issues,
            [],
        )

        # Dimension 5.3 - Script Registration
        registered_scripts: Set[str] = set()
        if isinstance(self.registry_data, dict):
            def collect_paths(node):
                if isinstance(node, dict):
                    for value in node.values():
                        collect_paths(value)
                elif isinstance(node, list):
                    for item in node:
                        collect_paths(item)
                elif isinstance(node, str):
                    registered_scripts.add(node)

            collect_paths(self.registry_data)
        registration_matches = [path for path in unique_references if path in registered_scripts]
        registration_findings = {
            "registered": registration_matches,
            "unregistered": [path for path in unique_references if path not in registration_matches],
            "registry_loaded": bool(self.registry_data),
        }
        registration_issues = []
        if not self.registry_data:
            registration_issues.append("Script registry missing or invalid.")
        if unique_references and not registration_matches:
            registration_issues.append("Referenced scripts not registered.")
        if unique_references and registration_matches and len(registration_matches) == len(unique_references):
            registration_status = "pass"
        elif registration_matches:
            registration_status = "warning"
        else:
            registration_status = "fail"
        registration_score = normalize_score(registration_status)
        dimensions["script_registration"] = DimensionResult(
            registration_status,
            registration_score,
            registration_findings,
            registration_issues,
            [],
        )

        # Dimension 5.4 - Command Syntax
        commands = find_commands(automation_text)
        valid_commands = [cmd for cmd in commands if "scripts/" in cmd]
        command_findings = {
            "commands": commands,
            "valid_commands": valid_commands,
        }
        command_issues = []
        if not commands:
            command_issues.append("No execution commands documented.")
        elif not valid_commands:
            command_issues.append("Commands missing script execution details.")
        if valid_commands:
            command_status = "pass"
        elif commands:
            command_status = "warning"
        else:
            command_status = "fail"
        command_score = normalize_score(command_status)
        dimensions["command_syntax"] = DimensionResult(
            command_status,
            command_score,
            command_findings,
            command_issues,
            [],
        )

        # Dimension 5.5 - Error Handling
        error_keywords = ["stop", "halt", "retry", "if fails", "on failure", "exit code", "log"]
        error_lines = [line for line in automation_text.splitlines() if any(keyword in line.lower() for keyword in error_keywords)]
        error_findings = {
            "error_lines": error_lines,
            "count": len(error_lines),
        }
        error_issues = []
        if not error_lines:
            error_issues.append("No error handling guidance for scripts.")
        if len(error_lines) >= 2:
            error_status = "pass"
        elif error_lines:
            error_status = "warning"
        else:
            error_status = "fail"
        error_score = normalize_score(error_status)
        dimensions["error_handling"] = DimensionResult(
            error_status,
            error_score,
            error_findings,
            error_issues,
            [],
        )

        return dimensions


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate script integration references")
    parser.add_argument("--protocol", help="Protocol ID to validate")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--summary", action="store_true", help="Generate summary report")
    parser.add_argument("--workspace", default=".", help="Workspace root path")
    args = parser.parse_args()

    validator = ScriptIntegrationValidator(Path(args.workspace))
    return run_cli(validator, args.protocol, args.all, args.summary)


if __name__ == "__main__":
    raise SystemExit(main())
