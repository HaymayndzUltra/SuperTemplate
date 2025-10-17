"""Compatibility wrapper around the unified template registry.

This module exposes the legacy :class:`TemplateRegistry` interface used by the
``project_generator`` package while delegating all functionality to the
``UnifiedTemplateRegistry`` located in ``unified_workflow.core``.  The wrapper
ensures the project generator and the unified workflow consume an identical
view of available templates without duplicating discovery logic.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional

from unified_workflow.core.template_registry import (
    TemplateMetadata,
    UnifiedTemplateRegistry,
)


class TemplateRegistry:
    """Legacy template registry facade.

    The original project generator expected a lightweight registry capable of
    returning dictionaries.  The unified registry already exposes all required
    metadata, so the facade converts modern ``TemplateMetadata`` instances into
    the legacy structures on demand.
    """

    def __init__(self, root: Optional[Path] = None):
        """Initialize the registry facade.

        Args:
            root: Optional project root. When provided, template discovery is
                limited to the supplied directory.  If omitted the unified
                registry performs automatic root detection.
        """

        self._registry = UnifiedTemplateRegistry(root_path=root)
        self._registry.initialize()

    # ------------------------------------------------------------------
    # Legacy interface
    # ------------------------------------------------------------------
    def list_all(self) -> List[Dict[str, object]]:
        """Return all templates in the legacy dictionary format."""

        templates = self._registry.list_templates()
        return [self._to_legacy_dict(template) for template in templates]

    def get_template(
        self, template_type: str, template_name: str
    ) -> Optional[Dict[str, object]]:
        """Retrieve metadata for a specific template.

        Args:
            template_type: Template category (backend, frontend, etc.).
            template_name: Template identifier within the category.

        Returns:
            Legacy dictionary describing the template, or ``None`` when the
            template is not present in the unified registry.
        """

        metadata = self._registry.get_template(template_type, template_name)
        if metadata is None:
            return None
        return self._to_legacy_dict(metadata)

    def get_template_path(
        self, template_type: str, template_name: str, variant: str = "base"
    ) -> Optional[Path]:
        """Return the path to a template variant.

        Args:
            template_type: Template category.
            template_name: Template identifier.
            variant: Optional variant name (``"base"`` by default).

        Returns:
            Path to the template variant if it exists, otherwise ``None``.
        """

        return self._registry.get_template_path(template_type, template_name, variant)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _to_legacy_dict(metadata: TemplateMetadata) -> Dict[str, object]:
        """Convert unified metadata to the legacy dictionary representation."""

        return {
            "type": metadata.type.value,
            "name": metadata.name,
            "variants": list(metadata.variants),
            "engines": list(metadata.engines) if metadata.engines else None,
            "path": str(metadata.path),
        }

