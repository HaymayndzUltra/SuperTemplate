#!/usr/bin/env python3
"""Validator 7 - Evidence Package validation."""

import json
import os
import re
from pathlib import Path
from typing import Dict

from base_validator import DimensionResult, ProtocolValidatorBase, run_validator_cli


class ProtocolEvidenceValidator(ProtocolValidatorBase):
    """Validates evidence generation, storage, manifest, traceability, and archival."""

    VALIDATOR_NAME = "protocol_evidence"
    VALIDATOR_VERSION = "1.0.0"

    def __init__(self, workspace_root: Path) -> None:
        super().__init__(workspace_root)
        self.artifacts_root = workspace_root / ".artifacts"
        self.DIMENSIONS = (
            ("artifact_generation", 0.30, self._validate_artifact_generation),
            ("storage_structure", 0.20, self._validate_storage_structure),
            ("manifest_completeness", 0.20, self._validate_manifest),
            ("traceability", 0.15, self._validate_traceability),
            ("archival", 0.15, self._validate_archival),
        )

    def _protocol_artifact_dir(self, protocol_id: str) -> Path:
        return self.artifacts_root / f"protocol-{protocol_id}"

    def _get_evidence_section(self, content: str) -> str:
        return self._extract_section(content, "EVIDENCE SUMMARY")

    def _validate_artifact_generation(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_evidence_section(content)
        artifact_entries = re.findall(r"`([^`]+)`\s*\|\s*`?([^`|]+)`?", section)
        evidence: Dict[str, bool] = {
            "artifact_list": bool(artifact_entries),
            "location_column": any(".artifacts" in entry[1] for entry in artifact_entries),
            "format_mentions": self._has_keywords(section, ["json", "markdown", "yaml", "report"]),
            "status_metrics": self._has_keywords(section, ["status", "target", "actual", "metric"]),
        }

        return self._build_dimension_result(
            "Artifact Generation",
            evidence,
            evidence={"artifacts": artifact_entries[:10]},
        )

    def _validate_storage_structure(self, protocol_id: str, content: str) -> DimensionResult:
        artifact_dir = self._protocol_artifact_dir(protocol_id)
        evidence: Dict[str, bool] = {
            "directory_exists": artifact_dir.exists(),
            "naming_convention": artifact_dir.name == f"protocol-{protocol_id}",
            "contains_files": any(artifact_dir.iterdir()) if artifact_dir.exists() else False,
            "write_access": os.access(artifact_dir, os.W_OK) if artifact_dir.exists() else False,
        }

        return self._build_dimension_result(
            "Storage Structure",
            evidence,
            evidence={"path": str(artifact_dir), "files": [child.name for child in artifact_dir.iterdir()] if artifact_dir.exists() else []},
        )

    def _validate_manifest(self, protocol_id: str, content: str) -> DimensionResult:
        artifact_dir = self._protocol_artifact_dir(protocol_id)
        manifest_path = artifact_dir / "evidence-manifest.json"
        manifest_data = {}
        if manifest_path.exists():
            try:
                manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                manifest_data = {}
        evidence: Dict[str, bool] = {
            "manifest_exists": manifest_path.exists(),
            "artifact_inventory": bool(manifest_data.get("artifacts")) if isinstance(manifest_data, dict) else False,
            "metadata_present": any("timestamp" in str(manifest_data) for _ in [0]) if manifest_data else False,
            "dependency_links": "dependencies" in manifest_data if isinstance(manifest_data, dict) else False,
        }

        return self._build_dimension_result(
            "Manifest Completeness",
            evidence,
            evidence={"manifest_path": str(manifest_path), "manifest_keys": list(manifest_data.keys()) if isinstance(manifest_data, dict) else []},
        )

    def _validate_traceability(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_evidence_section(content)
        evidence: Dict[str, bool] = {
            "input_tracking": self._has_keywords(section, ["input", "source", "origin"]),
            "output_tracking": self._has_keywords(section, ["output", "consumer", "downstream"]),
            "transformation_log": self._has_keywords(section, ["transformation", "log", "change", "derivation"]),
            "audit_trail": self._has_keywords(section, ["audit", "timestamp", "record", "trace"]),
        }

        return self._build_dimension_result(
            "Traceability",
            evidence,
            evidence={"checks": evidence},
        )

    def _validate_archival(self, protocol_id: str, content: str) -> DimensionResult:
        section = self._get_evidence_section(content)
        evidence: Dict[str, bool] = {
            "compression": self._has_keywords(section, ["zip", "archive", "compress"]),
            "retention": self._has_keywords(section, ["retention", "duration", "store for"]),
            "retrieval": self._has_keywords(section, ["retrieve", "access", "request"]),
            "cleanup": self._has_keywords(section, ["cleanup", "delete", "purge"]),
        }

        return self._build_dimension_result(
            "Archival",
            evidence,
            evidence={"checks": evidence},
        )


def main() -> None:
    run_validator_cli(ProtocolEvidenceValidator)


if __name__ == "__main__":
    main()
