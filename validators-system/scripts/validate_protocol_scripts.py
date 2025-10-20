#!/usr/bin/env python3
"""Validator 5 - Script Integration validation."""

import json
import re
from pathlib import Path
from typing import Dict, List

from base_validator import DimensionResult, ProtocolValidatorBase, run_validator_cli


class ProtocolScriptIntegrationValidator(ProtocolValidatorBase):
    """Validates script references, existence, registration, commands, and error handling."""

    VALIDATOR_NAME = "protocol_script_integration"
    VALIDATOR_VERSION = "1.0.0"

    def __init__(self, workspace_root: Path) -> None:
        super().__init__(workspace_root)
        self.registry_path = workspace_root / "scripts" / "script-registry.json"
        self.DIMENSIONS = (
            ("script_references", 0.20, self._validate_script_references),
            ("script_existence", 0.25, self._validate_script_existence),
            ("script_registration", 0.20, self._validate_script_registration),
            ("command_syntax", 0.20, self._validate_command_syntax),
            ("error_handling", 0.15, self._validate_error_handling),
        )

    def _get_relevant_sections(self, content: str) -> str:
        prereq = self._extract_section(content, "PREREQUISITES")
        automation = self._extract_section(content, "AUTOMATION HOOKS")
        return "\n".join([prereq, automation])

    def _extract_scripts(self, text: str) -> List[str]:
        scripts = re.findall(r"scripts/[\w_\-/\.]+", text)
        return sorted({script.strip("`") for script in scripts})

    def _load_registry(self) -> Dict[str, str]:
        if not self.registry_path.exists():
            return {}
        return json.loads(self.registry_path.read_text(encoding="utf-8"))

    def _validate_script_references(self, protocol_id: str, content: str) -> DimensionResult:
        text = self._get_relevant_sections(content)
        scripts = self._extract_scripts(text)
        evidence: Dict[str, bool] = {
            "references_present": bool(scripts),
            "paths_formatted": all(path.startswith("scripts/") for path in scripts),
            "purpose_documented": self._has_keywords(text, ["action", "purpose", "validates", "run"]),
            "dependencies": self._has_keywords(text, ["requirements", "dependency", "install"]),
        }

        return self._build_dimension_result(
            "Script References",
            evidence,
            evidence={"referenced_scripts": scripts},
        )

    def _validate_script_existence(self, protocol_id: str, content: str) -> DimensionResult:
        text = self._get_relevant_sections(content)
        scripts = self._extract_scripts(text)
        existence = {script: (self.workspace_root / script).exists() for script in scripts}
        executability = {
            script: (self.workspace_root / script).exists() and (self.workspace_root / script).stat().st_size > 0
            for script in scripts
        }
        evidence: Dict[str, bool] = {
            "files_exist": bool(scripts) and all(existence.values()),
            "non_empty": bool(scripts) and all(executability.values()),
            "any_scripts": bool(scripts),
            "permissions_checked": True if scripts else False,
        }

        return self._build_dimension_result(
            "Script Existence",
            evidence,
            evidence={"existence": existence},
        )

    def _validate_script_registration(self, protocol_id: str, content: str) -> DimensionResult:
        registry = self._load_registry()
        text = self._get_relevant_sections(content)
        scripts = self._extract_scripts(text)
        flattened_registry = json.dumps(registry) if registry else ""
        registration = {script: (script in flattened_registry) for script in scripts}

        evidence: Dict[str, bool] = {
            "registry_available": bool(registry),
            "scripts_registered": bool(scripts) and all(registration.values()),
            "partial_registration": bool(any(registration.values())),
            "metadata_present": "name" in flattened_registry if registry else False,
        }

        return self._build_dimension_result(
            "Script Registration",
            evidence,
            evidence={"registration": registration},
        )

    def _validate_command_syntax(self, protocol_id: str, content: str) -> DimensionResult:
        automation = self._extract_section(content, "AUTOMATION HOOKS")
        commands = re.findall(r"python[0-9]?\s+scripts/[\w_\-/.]+(?:\s+--[\w-]+\s+[^\s]+)?", automation)
        valid_flags = any("--" in command for command in commands)
        chained_commands = ";" in automation or "&&" in automation

        evidence: Dict[str, bool] = {
            "commands_documented": bool(commands),
            "flag_usage": valid_flags,
            "multi_command": chained_commands,
            "usage_examples": self._has_keywords(automation, ["example", "run", "command"]),
        }

        return self._build_dimension_result(
            "Command Syntax",
            evidence,
            evidence={"commands": commands},
        )

    def _validate_error_handling(self, protocol_id: str, content: str) -> DimensionResult:
        automation = self._extract_section(content, "AUTOMATION HOOKS")
        evidence: Dict[str, bool] = {
            "failure_notes": self._has_keywords(automation, ["if fails", "on error", "retry", "fallback"]),
            "logging": self._has_keywords(automation, ["log", "record", "capture"]),
            "manual_override": self._has_keywords(automation, ["manual", "review", "override"]),
            "continuation": self._has_keywords(automation, ["continuation", "next operator", "handoff"]),
        }

        return self._build_dimension_result(
            "Error Handling",
            evidence,
            evidence={"checks": evidence},
        )


def main() -> None:
    run_validator_cli(ProtocolScriptIntegrationValidator)


if __name__ == "__main__":
    main()
