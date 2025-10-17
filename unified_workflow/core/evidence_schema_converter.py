"""Compatibility wrapper for the evidence schema converter."""

from __future__ import annotations

from scripts.evidence_schema_converter import (  # noqa: F401
    EvidenceSchemaConverter,
    EvidenceMigrator,
)


def convert_legacy_evidence(*args, **kwargs):  # type: ignore[override]
    """Compatibility helper mirroring the legacy API used in prompts."""

    return EvidenceSchemaConverter.legacy_to_unified(*args, **kwargs)


__all__ = ["EvidenceSchemaConverter", "EvidenceMigrator", "convert_legacy_evidence"]

