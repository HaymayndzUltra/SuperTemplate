"""Focused unit tests for the unified template registry."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List

from unified_workflow.core.template_registry import TemplateMetadata, UnifiedTemplateRegistry


def _write_file(path: Path, content: str) -> None:
    """Create a file with UTF-8 encoded content."""

    path.write_text(content, encoding="utf-8")


def _create_template(
    base_path: Path,
    template_type: str,
    directory_name: str,
    *,
    manifest_name: str | None = None,
    variants: Iterable[str] | None = None,
) -> Path:
    """Create a fake template directory structure for testing."""

    variant_list: List[str] = list(variants or ("base",))
    template_dir = base_path / template_type / directory_name
    template_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = template_dir / "template.manifest.json"
    manifest_payload = {
        "name": manifest_name or directory_name,
        "type": template_type,
        "variants": variant_list,
        "description": f"Mock template {directory_name}",
    }
    _write_file(manifest_path, json.dumps(manifest_payload))

    for variant in variant_list:
        variant_dir = template_dir / variant
        variant_dir.mkdir(parents=True, exist_ok=True)
        _write_file(variant_dir / "README.md", f"# {directory_name} ({variant})\n")
        if template_type == "frontend":
            _write_file(variant_dir / "package.json", "{}")
        else:
            _write_file(variant_dir / "requirements.txt", "flask\n")

    return template_dir


def test_registry_discovers_primary_templates(tmp_path: Path) -> None:
    """Registry should enumerate templates located in the primary search path."""

    primary_base = tmp_path / "template-packs"
    _create_template(primary_base, "frontend", "react_app", variants=("base", "minimal"))

    registry = UnifiedTemplateRegistry(root_path=tmp_path)
    registry.initialize()

    templates = registry.list_templates()
    assert len(templates) == 1

    metadata: TemplateMetadata = templates[0]
    assert metadata.name == "react_app"
    assert metadata.type.value == "frontend"
    assert metadata.variants == ["base", "minimal"]
    assert registry.get_template_path("frontend", "react_app", "minimal") == metadata.path / "minimal"


def test_registry_prefers_higher_priority_paths(tmp_path: Path) -> None:
    """Higher-priority search paths should override legacy duplicates."""

    legacy_base = tmp_path / "project_generator" / "template-packs"
    primary_base = tmp_path / "template-packs"

    legacy_template = _create_template(legacy_base, "backend", "service_legacy", manifest_name="service")
    primary_template = _create_template(primary_base, "backend", "service_primary", manifest_name="service")

    registry = UnifiedTemplateRegistry(root_path=tmp_path)
    registry.initialize()

    metadata = registry.get_template("backend", "service")
    assert metadata is not None
    assert metadata.path == primary_template

    manifest = registry.export_manifest()
    manifest_entry = manifest["templates"]["backend/service"]
    assert Path(manifest_entry["path"]) == primary_template


def test_add_template_location_discovers_templates(tmp_path: Path) -> None:
    """Adding a custom template location should trigger discovery on reinitialization."""

    registry = UnifiedTemplateRegistry(root_path=tmp_path)
    registry.initialize()

    custom_base = tmp_path / "custom_templates"
    _create_template(custom_base, "database", "analytics")

    registry.add_template_location(custom_base, priority=0)

    metadata = registry.get_template("database", "analytics")
    assert metadata is not None
    assert metadata.path == custom_base / "database" / "analytics"

    manifest = registry.export_manifest()
    assert any(path_str.endswith("custom_templates") for path_str in manifest["search_paths"])
