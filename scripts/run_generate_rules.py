#!/usr/bin/env python3
"""
Lightweight rules generator that follows .cursor/ai-driven-workflow/00-generate-rules.md Generation Phase.

- Detect basic stack signals in the generated project directory
- Emit focused project rules under <project>/.cursor/rules/project-rules/
  without overwriting existing files unless --overwrite is passed
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import List


def detect_stack(project_dir: Path) -> dict:
    pkg = project_dir / "package.json"
    py = project_dir / "pyproject.toml"
    req = project_dir / "requirements.txt"
    stack = {"frontend": None, "backend": None}

    if pkg.exists():
        try:
            data = json.loads(pkg.read_text(encoding="utf-8"))
        except Exception:
            data = {}
        deps = {**(data.get("dependencies") or {}), **(data.get("devDependencies") or {})}
        if any(k in deps for k in ["next", "react-dom"]):
            stack["frontend"] = "nextjs"
        elif "@angular/core" in deps:
            stack["frontend"] = "angular"
        elif "nuxt" in deps:
            stack["frontend"] = "nuxt"
        elif "expo" in deps or "react-native" in deps:
            stack["frontend"] = "expo"

    if py.exists() or req.exists():
        text = (py.read_text(encoding="utf-8") if py.exists() else "") + "\n" + (req.read_text(encoding="utf-8") if req.exists() else "")
        low = text.lower()
        if "fastapi" in low:
            stack["backend"] = "fastapi"
        elif "django" in low:
            stack["backend"] = "django"

    # fallback: look for nestjs/go markers
    if (project_dir / "nest-cli.json").exists():
        stack["backend"] = stack["backend"] or "nestjs"
    if any((project_dir / n).exists() for n in ["go.mod", "main.go"]):
        stack["backend"] = stack["backend"] or "go"

    return stack


def ensure_rule(path: Path, content: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    if not content.endswith("\n"):
        content += "\n"
    path.write_text(content, encoding="utf-8")


def build_rule(name: str, description: str) -> str:
    return (
        "---\n"
        f"description: \"{description}\"\n"
        "alwaysApply: false\n"
        "---\n"
        "## Guidance\n\n"
        "Follow framework best practices, enforce testing and a11y, and document decisions.\n"
    )


def generate_rules(project_dir: Path, overwrite: bool) -> List[str]:
    emitted: List[str] = []
    rules_root = project_dir / ".cursor" / "rules" / "project-rules"
    stack = detect_stack(project_dir)

    if stack.get("frontend") == "nextjs":
        p = rules_root / "nextjs-app-structure.mdc"
        ensure_rule(p, build_rule("nextjs-app-structure.mdc", "Project-specific Next.js conventions and structure"), overwrite)
        emitted.append(str(p))
    if stack.get("frontend") == "angular":
        p = rules_root / "angular-app-structure.mdc"
        ensure_rule(p, build_rule("angular-app-structure.mdc", "Project-specific Angular conventions and structure"), overwrite)
        emitted.append(str(p))
    if stack.get("frontend") == "nuxt":
        p = rules_root / "vue-app-structure.mdc"
        ensure_rule(p, build_rule("vue-app-structure.mdc", "Project-specific Vue/Nuxt conventions and structure"), overwrite)
        emitted.append(str(p))
    if stack.get("frontend") == "expo":
        p = rules_root / "react-native-app-structure.mdc"
        ensure_rule(p, build_rule("react-native-app-structure.mdc", "Project-specific React Native/Expo guidelines"), overwrite)
        emitted.append(str(p))

    if stack.get("backend") == "fastapi":
        p = rules_root / "fastapi-backend-architecture.mdc"
        ensure_rule(p, build_rule("fastapi-backend-architecture.mdc", "FastAPI backend architecture and conventions"), overwrite)
        emitted.append(str(p))
    if stack.get("backend") == "django":
        p = rules_root / "django-backend-architecture.mdc"
        ensure_rule(p, build_rule("django-backend-architecture.mdc", "Django backend architecture and conventions"), overwrite)
        emitted.append(str(p))
    if stack.get("backend") == "nestjs":
        p = rules_root / "nestjs-backend-architecture.mdc"
        ensure_rule(p, build_rule("nestjs-backend-architecture.mdc", "NestJS backend architecture and conventions"), overwrite)
        emitted.append(str(p))
    if stack.get("backend") == "go":
        p = rules_root / "golang-backend-architecture.mdc"
        ensure_rule(p, build_rule("golang-backend-architecture.mdc", "Golang backend architecture and conventions"), overwrite)
        emitted.append(str(p))

    # Fullstack integration rule if both fronts detected in same project
    if stack.get("frontend") and stack.get("backend"):
        p = rules_root / "fullstack-integration-conventions.mdc"
        ensure_rule(p, build_rule("fullstack-integration-conventions.mdc", "Fullstack integration contracts and conventions"), overwrite)
        emitted.append(str(p))

    return emitted


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project-dir", required=True, help="Path to generated project root")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing project rules if they exist")
    args = ap.parse_args()

    project_dir = Path(args.project_dir).resolve()
    files = generate_rules(project_dir, overwrite=bool(args.overwrite))
    print(json.dumps({"generated": files}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


