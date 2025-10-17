"""Adapter for project_generator imports.

This adapter ensures proper import resolution for project_generator
components without requiring sys.path manipulation.
"""

from __future__ import annotations

# These imports work when unified_workflow is run from repo root
# project_generator is a top-level package at repo root
from project_generator.core.generator import ProjectGenerator
from project_generator.core.validator import ProjectValidator
from project_generator.core.industry_config import IndustryConfig
from project_generator.core.brief_parser import BriefParser
from project_generator.templates.registry import TemplateRegistry

__all__ = [
    'ProjectGenerator',
    'ProjectValidator',
    'IndustryConfig',
    'BriefParser',
    'TemplateRegistry',
]

