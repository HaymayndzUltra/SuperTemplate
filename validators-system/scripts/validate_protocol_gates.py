#!/usr/bin/env python3
"""Validator 4 - Quality Gates validation."""

import json
import re
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

from base_validator import DimensionResult, ProtocolValidatorBase, run_validator_cli


class ProtocolQualityGatesValidator(ProtocolValidatorBase):
    """Validates quality gate definitions, criteria, automation, and compliance."""

    VALIDATOR_NAME = "protocol_quality_gates"
    VALIDATOR_VERSION = "1.0.0"

    def __init__(self, workspace_root: Path) -> None:
        super().__init__(workspace_root)
        self.gates_config_dir = workspace_root / "config" / "protocol_gates"
        self.DIMENSIONS = (
            ("gate_definitions", 0.25, self._validate_gate_definitions),
            ("pass_criteria", 0.25, self._validate_pass_criteria),
            ("automation", 0.20, self._validate_automation),
            ("failure_handling", 0.15, self._validate_failure_handling),
            ("compliance_integration", 0.15, self._validate_compliance),
        )

    def _load_gate_config(self, protocol_id: str) -> Optional[Dict[str, Any]]:
        config_path = self.gates_config_dir / f"{protocol_id}.yaml"
        if not config_path.exists():
            return None
        return yaml.safe_load(config_path.read_text(encoding="utf-8"))

    def _get_quality_section(self, content: str) -> str:
        return self._extract_section(content, "QUALITY GATES")

    def _validate_gate_definitions(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_quality_section(content)
        config = self._load_gate_config(protocol_id)
        gate_titles = re.findall(r"^###\s+Gate\s+\d+", section, re.MULTILINE)
        evidence: Dict[str, bool] = {
            "section_present": bool(section),
            "gate_headings": bool(gate_titles),
            "gate_descriptions": self._has_keywords(section, ["criteria", "evidence", "pass threshold"]),
            "config_exists": config is not None,
        }
        evidence_details = {
            "gate_count_markdown": len(gate_titles),
            "config_present": config is not None,
            "config_gate_count": len(config.get("validators", [])) if config else 0,
        }

        return self._build_dimension_result("Gate Definitions", evidence, evidence=evidence_details)

    def _validate_pass_criteria(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_quality_section(content)
        config = self._load_gate_config(protocol_id)
        numeric_thresholds = re.findall(r"\b\d+\.?\d*\b", section)
        criteria_keywords = self._has_keywords(section, ["threshold", "score", ">=", "pass"])
        config_thresholds = bool(config and config.get("quality_thresholds"))

        evidence: Dict[str, bool] = {
            "numeric_thresholds": bool(numeric_thresholds),
            "criteria_keywords": criteria_keywords,
            "config_thresholds": config_thresholds,
            "success_metrics": self._has_keywords(section, ["metric", "validation", "measurement"]),
        }

        return self._build_dimension_result(
            "Pass Criteria",
            evidence,
            evidence={"detected_thresholds": numeric_thresholds[:10], "config_thresholds": config.get("quality_thresholds", {}) if config else {}},
        )

    def _validate_automation(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_quality_section(content)
        config = self._load_gate_config(protocol_id)
        automation_commands = re.findall(r"python[0-9]?\s+scripts/[\w_\-/.]+", section)
        registry_path = self.workspace_root / "scripts" / "script-registry.json"
        registry_entries = {}
        if registry_path.exists():
            registry_entries = json.loads(registry_path.read_text(encoding="utf-8"))

        referenced_scripts = {cmd.split()[1] for cmd in automation_commands}
        config_scripts = {item.get("command", "") for item in config.get("validators", [])} if config else set()
        scripts_to_check = referenced_scripts.union(config_scripts)

        registered = {
            script: any(script in str(value) for value in registry_entries.values()) if registry_entries else False
            for script in scripts_to_check
        }

        evidence: Dict[str, bool] = {
            "automation_commands": bool(automation_commands),
            "config_scripts": bool(config_scripts),
            "registry_coverage": all(registered.values()) if registered else False,
            "ci_signals": self._has_keywords(section, ["ci", "pipeline", "automation"]),
        }

        return self._build_dimension_result(
            "Automation",
            evidence,
            evidence={
                "commands": sorted(automation_commands),
                "config_scripts": sorted(config_scripts),
                "registered": registered,
            },
        )

    def _validate_failure_handling(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_quality_section(content)
        evidence: Dict[str, bool] = {
            "failure_actions": self._has_keywords(section, ["failure handling", "if fails", "on failure"]),
            "rollback": self._has_keywords(section, ["rollback", "retry", "re-run"]),
            "notification": self._has_keywords(section, ["notify", "alert", "escalate"]),
            "recovery": self._has_keywords(section, ["remediate", "fix", "address"]),
        }

        return self._build_dimension_result(
            "Failure Handling",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_compliance(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_quality_section(content)
        config = self._load_gate_config(protocol_id)
        compliance_keywords = ["hipaa", "soc2", "gdpr", "pci", "iso"]
        evidence: Dict[str, bool] = {
            "hipaa": self._has_keywords(section, ["hipaa"]),
            "soc2": self._has_keywords(section, ["soc2", "soc 2"]),
            "gdpr": self._has_keywords(section, ["gdpr"]),
            "other": self._has_keywords(section, ["regulatory", "compliance", "standards"]),
        }

        config_compliance = False
        if config:
            serialized = json.dumps(config).lower()
            config_compliance = any(keyword in serialized for keyword in compliance_keywords)

        evidence["config_checks"] = config_compliance

        return self._build_dimension_result(
            "Compliance Integration",
            evidence,
            evidence={"config_present": bool(config), "checks": evidence},
        )


def main() -> None:
    run_validator_cli(ProtocolQualityGatesValidator)


if __name__ == "__main__":
    main()
