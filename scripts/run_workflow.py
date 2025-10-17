#!/usr/bin/env python3
"""CLI entry point for executing the workflow automation pipeline."""
from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
import sys

# Import via proper package path (scripts should be run from repo root)
# If running from elsewhere, use: python -m scripts.run_workflow
from scripts.workflow_automation import WorkflowConfig, WorkflowOrchestrator
from scripts.workflow_automation.exceptions import GateFailedError, WorkflowError


def configure_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )


def load_config(path: Path) -> WorkflowConfig:
    return WorkflowConfig.load(path)


def run(args: argparse.Namespace) -> int:
    configure_logging(args.verbose)
    try:
        config = load_config(args.config)
        orchestrator = WorkflowOrchestrator(config, project_root=args.project_root)
        orchestrator.run()
    except GateFailedError as exc:
        logging.error("Workflow failed: %s", exc)
        return 2
    except WorkflowError as exc:
        logging.error("Workflow configuration error: %s", exc)
        return 3
    except Exception as exc:  # pragma: no cover - defensive catch
        logging.exception("Unexpected error running workflow")
        return 4
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("workflow/gate_controller.yaml"),
        help="Path to workflow configuration file",
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path("."),
        help="Directory containing project artifacts",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging",
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    sys.exit(run(parse_args(sys.argv[1:])))
