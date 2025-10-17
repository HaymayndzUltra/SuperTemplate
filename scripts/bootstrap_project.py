#!/usr/bin/env python3
"""One-command bootstrap that prepares docs and runs the end-to-end generator."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = REPO_ROOT / "workflow.config.json"
REQUIRED_FIELDS = ("name", "industry", "project_type", "frontend", "backend", "database")
FIELD_ENV_MAPPING: Tuple[Tuple[str, str], ...] = (
    ("name", "NAME"),
    ("industry", "INDUSTRY"),
    ("project_type", "PROJECT_TYPE"),
    ("frontend", "FE"),
    ("backend", "BE"),
    ("database", "DB"),
    ("auth", "AUTH"),
    ("deploy", "DEPLOY"),
    ("compliance", "COMPLIANCE"),
)


def load_config(path: Path) -> Dict[str, str]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return {k: str(v) for k, v in data.items() if isinstance(v, (str, int, float))}
    except Exception:
        pass
    return {}


def resolve_settings(args: argparse.Namespace, config: Dict[str, str]) -> Dict[str, str]:
    env = os.environ
    resolved: Dict[str, str] = {}
    for field, env_key in FIELD_ENV_MAPPING:
        value = getattr(args, field, None)
        if value is None:
            value = env.get(env_key)
        if value is None:
            value = config.get(field)
        if isinstance(value, str):
            value = value.strip()
        if value is not None and value != "":
            resolved[field] = str(value)

    missing = [key for key in REQUIRED_FIELDS if not resolved.get(key)]
    if missing:
        joined = ", ".join(missing)
        raise SystemExit(f"Missing required settings: {joined}. Provide flags, environment variables, or update {args.config_file}.")

    return resolved


def maybe_update_config(path: Path, config: Dict[str, str], updates: Dict[str, str]) -> None:
    merged = dict(config)
    merged.update({k: v for k, v in updates.items() if v})
    path.write_text(json.dumps(merged, indent=2) + "\n", encoding="utf-8")


def run_command(cmd: list[str], *, env: Dict[str, str] | None = None, cwd: Path | None = None) -> None:
    proc = subprocess.run(cmd, cwd=str(cwd) if cwd else None, env=env, check=False)
    if proc.returncode != 0:
        display = " ".join(cmd)
        raise SystemExit(f"Command failed ({proc.returncode}): {display}")


def bootstrap(args: argparse.Namespace) -> None:
    config_path = (Path(args.config_file).resolve() if args.config_file else DEFAULT_CONFIG)
    config_data = load_config(config_path)
    settings = resolve_settings(args, config_data)

    if args.update_config:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        maybe_update_config(config_path, config_data, settings)

    brief_dir = REPO_ROOT / "docs" / "briefs" / settings["name"]
    brief_dir.mkdir(parents=True, exist_ok=True)
    run_command([sys.executable, str(REPO_ROOT / "scripts" / "scaffold_briefs.py"), settings["name"]])

    env = os.environ.copy()
    env.update({key.upper(): value for key, value in settings.items()})
    env.setdefault("CONFIG_FILE", str(config_path))
    if args.output_root:
        env["OUTPUT_ROOT"] = args.output_root
    if args.force:
        env["FORCE_OUTPUT"] = "1"

    project_dir = Path(env.get("OUTPUT_ROOT", str(REPO_ROOT / "../_generated"))).expanduser().resolve() / settings["name"]
    print(f"[bootstrap] Running e2e pipeline for {settings['name']} → {project_dir}")
    run_command([str(REPO_ROOT / "scripts" / "e2e_from_brief.sh")], env=env, cwd=REPO_ROOT)
    print(f"[bootstrap] Completed. Project artifacts available at {project_dir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare brief scaffolding and run the generator pipeline")
    parser.add_argument("--name", help="Project/client name (defaults to NAME env or config)")
    parser.add_argument("--industry", help="Industry override")
    parser.add_argument("--project-type", dest="project_type", help="Project type override")
    parser.add_argument("--frontend", help="Frontend stack override")
    parser.add_argument("--backend", help="Backend stack override")
    parser.add_argument("--database", help="Database selection override")
    parser.add_argument("--auth", help="Authentication provider override")
    parser.add_argument("--deploy", help="Deployment target override")
    parser.add_argument("--compliance", help="Comma-separated compliance regimes")
    parser.add_argument("--output-root", help="Override OUTPUT_ROOT for generator outputs")
    parser.add_argument("--config-file", default=str(DEFAULT_CONFIG), help="Path to workflow config JSON")
    parser.add_argument("--update-config", action="store_true", help="Write resolved settings back to the config file")
    parser.add_argument("--force", action="store_true", help="Overwrite existing generated project outputs")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bootstrap(args)


if __name__ == "__main__":
    main()
