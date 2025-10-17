"""Unit tests for evidence schema conversion helpers."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List

import importlib
import sys
from pathlib import Path


def _ensure_project_generator_package() -> None:
    """Ensure the ``project_generator`` package resolves relative to the repository root."""

    repo_root = Path(__file__).resolve().parents[2]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

    for module_name in list(sys.modules):
        if module_name == "project_generator" or module_name.startswith("project_generator."):
            sys.modules.pop(module_name)

    importlib.invalidate_caches()
    importlib.import_module("project_generator")


_ensure_project_generator_package()

from unified_workflow.core.evidence_schema_converter import (
    EvidenceSchemaConverter,
    convert_legacy_evidence,
)


def _build_standard_legacy_records() -> List[Dict[str, Any]]:
    """Create representative legacy evidence entries."""

    return [
        {
            "path": "docs/README.md",
            "category": "documentation",
            "description": "Project overview",
            "checksum": "abc123",
            "created_at": "2025-01-01T00:00:00Z",
        },
        {
            "path": "src/app.py",
            "category": "code",
            "description": "Application module",
            "checksum": "def456",
            "created_at": "2025-01-01T01:00:00Z",
        },
    ]


def _sanitise_dynamic_metadata(evidence: Dict[str, Any]) -> Dict[str, Any]:
    """Return a copy of ``evidence`` with unstable timestamps removed."""

    cleaned = deepcopy(evidence)
    cleaned["manifest"]["metadata"].pop("generated_at", None)
    cleaned["run_log"]["metadata"].pop("last_updated", None)
    cleaned["validation"]["metadata"].pop("last_updated", None)
    if cleaned["run_log"]["entries"]:
        cleaned["run_log"]["entries"][0].pop("timestamp", None)
    if cleaned["validation"]["phases"]:
        cleaned["validation"]["phases"][0].pop("validated_at", None)
    return cleaned


def test_convert_legacy_evidence_matches_converter() -> None:
    """Compatibility helper should delegate to the converter implementation."""

    legacy = _build_standard_legacy_records()
    helper_output = convert_legacy_evidence(legacy, "demo-project", phase=2)
    direct_output = EvidenceSchemaConverter.legacy_to_unified(legacy, "demo-project", phase=2)

    assert _sanitise_dynamic_metadata(helper_output) == _sanitise_dynamic_metadata(direct_output)
    assert helper_output["manifest"]["metadata"]["project_name"] == "demo-project"
    assert helper_output["validation"]["phases"][0]["phase"] == 2


def test_legacy_to_unified_supports_workflow1_records() -> None:
    """Records using the workflow1 structure should be normalized correctly."""

    legacy = [
        {
            "file": "artifacts/report.md",
            "phase": 3,
            "project": "demo",
            "checksum": "xyz789",
            "timestamp": "2025-02-01T00:00:00Z",
        }
    ]

    unified = EvidenceSchemaConverter.legacy_to_unified(legacy, "demo", phase=3)

    artifact = unified["manifest"]["artifacts"][0]
    assert artifact["path"] == "artifacts/report.md"
    assert artifact["phase"] == 3
    assert artifact["description"].startswith("Phase 3 artifact")


def test_unified_to_legacy_strips_phase_information() -> None:
    """Round-trip conversion should drop phase metadata to match legacy format."""

    legacy = _build_standard_legacy_records()
    unified = EvidenceSchemaConverter.legacy_to_unified(legacy, "demo", phase=1)
    round_tripped = EvidenceSchemaConverter.unified_to_legacy(unified)

    for original, converted in zip(legacy, round_tripped, strict=True):
        assert "phase" not in converted
        assert converted["path"] == original["path"]
        assert converted["category"] == original["category"]
        assert converted["description"] == original["description"]
        assert converted["checksum"] == original["checksum"]
