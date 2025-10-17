"""Unified project generator adapter.

This module exposes a small adapter that wires the legacy
``project_generator`` package into the Week 2 unified workflow.  The
adapter normalises configuration, ensures the unified template registry
is always used, and returns light-weight dataclasses that are convenient
for validation prompts and tests.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from importlib import import_module
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Union
from unified_workflow.core.template_registry import (
    TemplateMetadata,
    UnifiedTemplateRegistry,
)


@dataclass(frozen=True)
class ProjectGenerationResult:
    """Result returned after calling :meth:`UnifiedProjectGenerator.generate`."""

    success: bool
    project_path: Optional[Path]
    details: Dict[str, Any]
    error: Optional[str] = None


@dataclass(frozen=True)
class ProjectValidationResult:
    """Result returned from :meth:`UnifiedProjectGenerator.validate`."""

    is_valid: bool
    errors: Sequence[str]
    warnings: Sequence[str]


@dataclass(frozen=True)
class AvailableTemplate:
    """Small wrapper exposing template metadata via simple attributes."""

    name: str
    type: str
    path: Path
    variants: Sequence[str]
    engines: Optional[Sequence[str]]


class UnifiedProjectGenerator:
    """Bridge between the unified workflow and the legacy generator."""

    def __init__(
        self,
        project_name: str,
        industry: str,
        stack_config: Dict[str, str],
        *,
        project_type: str = "fullstack",
        template_registry: Optional[UnifiedTemplateRegistry] = None,
    ) -> None:
        self.project_name = project_name
        self.industry = industry
        self.stack_config = stack_config
        self.project_type = project_type

        self._template_registry = template_registry or UnifiedTemplateRegistry()
        self._template_registry.initialize()

        self._generator_cls = None
        self._validator_cls = None
        self._industry_config_cls = None
        self._last_generation: Optional[ProjectGenerationResult] = None

    # ------------------------------------------------------------------
    # Public API expected by validation prompt
    # ------------------------------------------------------------------
    def generate(self, output_dir: Optional[Union[str, Path]] = None) -> ProjectGenerationResult:
        """Generate a project using the unified configuration interface."""

        target_root = Path(output_dir) if output_dir else Path.cwd() / self.project_name
        target_root = target_root.resolve()
        target_root.parent.mkdir(parents=True, exist_ok=True)

        args = self._build_args(target_root)
        generator = self._get_generator_class()(
            args=args,
            config=self._create_industry_config(),
            template_registry=self._template_registry,
        )

        generation_details = generator.generate()
        project_path = Path(generation_details.get("project_path", "")).resolve() if generation_details.get("project_path") else None

        if generation_details.get("success"):
            # The legacy generator always nests the project name under
            # ``args.output_dir``.  Ensure the directory matches the
            # caller expectation (``target_root``).
            expected_path = target_root
            if project_path and project_path != expected_path:
                if expected_path.exists():
                    project_path = expected_path
                elif project_path.exists():
                    project_path.rename(expected_path)
                    project_path = expected_path

            result = ProjectGenerationResult(True, project_path, generation_details)
        else:
            result = ProjectGenerationResult(
                False,
                project_path,
                generation_details,
                error=generation_details.get("error"),
            )

        self._last_generation = result
        return result

    def validate(self) -> ProjectValidationResult:
        """Validate the stack configuration against the legacy validator."""

        args = self._build_args(Path.cwd() / self.project_name)
        validator = self._get_validator_class()()
        validation = validator.validate_configuration(args)

        return ProjectValidationResult(
            is_valid=bool(validation.get("valid")),
            errors=tuple(validation.get("errors", [])),
            warnings=tuple(validation.get("warnings", [])),
        )

    def get_templates(self) -> List[AvailableTemplate]:
        """Expose templates from the unified registry as simple objects."""

        templates: List[TemplateMetadata] = self._template_registry.list_templates()
        return [
            AvailableTemplate(
                name=template.name,
                type=template.type.value,
                path=template.path,
                variants=tuple(template.variants),
                engines=tuple(template.engines) if template.engines else None,
            )
            for template in templates
        ]

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _build_args(self, target_root: Path):
        """Create an ``argparse.Namespace`` mirroring CLI inputs."""

        from argparse import Namespace

        resolved_root = target_root.resolve()
        output_dir = resolved_root.parent
        project_name = resolved_root.name

        stack = {
            "frontend": self.stack_config.get("frontend", "none"),
            "backend": self.stack_config.get("backend", "none"),
            "database": self.stack_config.get("database", "none"),
            "auth": self.stack_config.get("auth", "auth0"),
            "deploy": self.stack_config.get("deploy", "aws"),
        }

        compliance = self.stack_config.get("compliance", [])
        if isinstance(compliance, str):
            compliance_str = compliance
        else:
            compliance_str = ",".join(compliance)

        features = self.stack_config.get("features", [])
        if isinstance(features, str):
            features_str = features
        else:
            features_str = ",".join(features)

        return Namespace(
            name=project_name,
            industry=self.industry,
            project_type=self.project_type,
            frontend=stack["frontend"],
            backend=stack["backend"],
            database=stack["database"],
            auth=stack["auth"],
            deploy=stack["deploy"],
            compliance=compliance_str,
            features=features_str,
            output_dir=str(output_dir),
            no_git=True,
            no_install=True,
            workers=2,
            force=True,
            no_cursor_assets=True,
            minimal_cursor=False,
            rules_manifest=None,
            nestjs_orm="typeorm",
        )

    def _get_generator_class(self):
        if self._generator_cls is None:
            self._generator_cls = self._load_symbol(
                "project_generator.core.generator",
                "ProjectGenerator",
            )
        return self._generator_cls

    def _get_validator_class(self):
        if self._validator_cls is None:
            self._validator_cls = self._load_symbol(
                "project_generator.core.validator",
                "ProjectValidator",
            )
        return self._validator_cls

    def _create_industry_config(self):
        if self._industry_config_cls is None:
            self._industry_config_cls = self._load_symbol(
                "project_generator.core.industry_config",
                "IndustryConfig",
            )
        return self._industry_config_cls(self.industry)

    def _load_symbol(self, module_path: str, attribute: str):
        self._ensure_project_generator_package()
        module = import_module(module_path)
        return getattr(module, attribute)

    def _ensure_project_generator_package(self) -> None:
        package_name = "project_generator"
        module = sys.modules.get(package_name)
        if module is not None and hasattr(module, "__path__"):
            return

        repo_root = Path(__file__).resolve().parent.parent / package_name
        spec = spec_from_file_location(
            package_name,
            repo_root / "__init__.py",
            submodule_search_locations=[str(repo_root)],
        )
        if spec is None or spec.loader is None:
            raise ImportError(f"Unable to load package {package_name}")

        module = module_from_spec(spec)
        sys.modules[package_name] = module
        spec.loader.exec_module(module)


__all__ = [
    "UnifiedProjectGenerator",
    "ProjectGenerationResult",
    "ProjectValidationResult",
    "AvailableTemplate",
]

