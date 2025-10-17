"""Unified brief processor adapter."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from importlib import import_module
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Dict, List, Optional, Union

def _load_project_generator_symbol(module_path: str, attribute: str):
    package_name = "project_generator"
    module = sys.modules.get(package_name)
    if module is None or not hasattr(module, "__path__"):
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

    module_obj = import_module(module_path)
    return getattr(module_obj, attribute)


BriefParser = _load_project_generator_symbol("project_generator.core.brief_parser", "BriefParser")
ScaffoldSpec = _load_project_generator_symbol("project_generator.core.brief_parser", "ScaffoldSpec")

from scripts.lifecycle_tasks import build_plan
from scripts.plan_from_brief import render_plan_md


@dataclass(frozen=True)
class ParsedBrief:
    """Structured representation returned from :meth:`UnifiedBriefProcessor.parse`."""

    project_name: str
    industry: str
    project_type: str
    stack: Dict[str, str]
    compliance: List[str]
    features: List[str]
    raw_spec: ScaffoldSpec


class UnifiedBriefProcessor:
    """Parse briefs, extract metadata and generate planning artefacts."""

    def __init__(
        self,
        *,
        brief_path: Optional[Union[str, Path]] = None,
        brief_content: Optional[str] = None,
    ) -> None:
        if not brief_path and not brief_content:
            raise ValueError("Either 'brief_path' or 'brief_content' must be provided.")

        self._brief_path = Path(brief_path) if brief_path else None
        self._brief_content = brief_content
        self._raw_content = brief_content
        self._parsed: Optional[ParsedBrief] = None

    # ------------------------------------------------------------------
    # Public API expected by the validation prompt
    # ------------------------------------------------------------------
    def parse(self) -> ParsedBrief:
        """Parse the brief and cache the resulting specification."""

        if self._parsed is not None:
            return self._parsed

        spec = self._load_spec()
        project_name = self._resolve_project_name(spec)
        spec.name = project_name

        parsed = ParsedBrief(
            project_name=project_name,
            industry=spec.industry,
            project_type=spec.project_type,
            stack={
                "frontend": spec.frontend,
                "backend": spec.backend,
                "database": spec.database,
                "auth": spec.auth,
                "deploy": spec.deploy,
            },
            compliance=[c.upper() for c in spec.compliance],
            features=list(spec.features),
            raw_spec=spec,
        )

        self._parsed = parsed
        return parsed

    def extract_metadata(self) -> Dict[str, Union[str, Dict[str, str], List[str]]]:
        """Return metadata dictionary derived from the parsed brief."""

        parsed = self.parse()
        metadata = {
            "project_name": parsed.project_name,
            "industry": parsed.industry,
            "type": parsed.project_type,
            "stack": parsed.stack,
            "compliance": parsed.compliance,
            "features": parsed.features,
            "complexity": self._infer_complexity(parsed),
        }
        if self._raw_content:
            explicit_type = self._extract_label("Type")
            if explicit_type:
                metadata["type"] = explicit_type
            explicit_complexity = self._extract_label("Complexity")
            if explicit_complexity:
                metadata["complexity"] = explicit_complexity
        return metadata

    def generate_plan(self, *, output_path: Union[str, Path]) -> Path:
        """Write ``PLAN.md`` to ``output_path`` and return the resulting path."""

        parsed = self.parse()
        plan = build_plan(parsed.raw_spec)
        plan_md = render_plan_md(parsed.raw_spec, plan)

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(plan_md, encoding="utf-8")

        return output_path

    def generate_tasks(self, *, output_path: Union[str, Path]) -> Path:
        """Persist ``tasks.json`` derived from the parsed brief."""

        parsed = self.parse()
        plan = build_plan(parsed.raw_spec)

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(plan, indent=2), encoding="utf-8")

        return output_path

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _load_spec(self) -> ScaffoldSpec:
        if self._brief_path:
            self._raw_content = self._brief_path.read_text(encoding="utf-8")
            return BriefParser(self._brief_path).parse()

        assert self._brief_content is not None
        from tempfile import NamedTemporaryFile

        with NamedTemporaryFile(mode="w", suffix=".md", encoding="utf-8", delete=False) as handle:
            handle.write(self._brief_content)
            temp_path = Path(handle.name)

        spec = BriefParser(temp_path).parse()
        temp_path.unlink(missing_ok=True)
        return spec

    def _infer_complexity(self, parsed: ParsedBrief) -> str:
        feature_count = len(parsed.features)
        if feature_count >= 5:
            return "High"
        if feature_count >= 3:
            return "Medium"
        return "Low"

    def _resolve_project_name(self, spec: ScaffoldSpec) -> str:
        if self._raw_content:
            match = re.search(r"^\s*(?:project|title)[:\-]\s*(.+)$", self._raw_content, re.IGNORECASE | re.MULTILINE)
            if match:
                return match.group(1).strip()
        return spec.name.replace("-", " ").title()

    def _extract_label(self, label: str) -> Optional[str]:
        if not self._raw_content:
            return None
        pattern = rf"^\s*{re.escape(label)}[:\-]\s*(.+)$"
        match = re.search(pattern, self._raw_content, re.IGNORECASE | re.MULTILINE)
        if match:
            return match.group(1).strip()
        return None


__all__ = ["UnifiedBriefProcessor", "ParsedBrief"]

