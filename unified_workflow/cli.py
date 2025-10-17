#!/usr/bin/env python3
"""Unified Workflow CLI - Compatibility layer for legacy scripts with telemetry.

This CLI provides a unified entry point while maintaining backward compatibility
with legacy scripts. It tracks usage to inform deprecation decisions.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Telemetry file location
TELEMETRY_FILE = Path.home() / ".unified-workflow" / "telemetry.json"


class TelemetryTracker:
    """Tracks CLI usage for deprecation decisions."""
    
    def __init__(self, telemetry_file: Path = TELEMETRY_FILE):
        """Initialize telemetry tracker.
        
        Args:
            telemetry_file: Path to store telemetry data
        """
        self.telemetry_file = telemetry_file
        self.telemetry_file.parent.mkdir(parents=True, exist_ok=True)
        self._load_data()
    
    def _load_data(self) -> None:
        """Load existing telemetry data."""
        if self.telemetry_file.exists():
            try:
                self.data = json.loads(self.telemetry_file.read_text())
            except Exception as e:
                logger.warning(f"Failed to load telemetry: {e}")
                self.data = {"commands": {}, "migrations": {}}
        else:
            self.data = {"commands": {}, "migrations": {}}
    
    def _save_data(self) -> None:
        """Save telemetry data."""
        try:
            self.telemetry_file.write_text(
                json.dumps(self.data, indent=2),
                encoding="utf-8"
            )
        except Exception as e:
            logger.warning(f"Failed to save telemetry: {e}")
    
    def track_command(
        self,
        command: str,
        args: List[str],
        *,
        source: str,
        exit_code: Optional[int] = None,
        fallback: bool = False,
        attempted_sources: Optional[Sequence[str]] = None,
    ) -> None:
        """Track a command execution.

        Args:
            command: Command name
            args: Command arguments
            source: Execution source (``"unified"`` or ``"legacy"``)
            exit_code: Optional exit code returned by the command
            fallback: Whether the execution required a legacy fallback
            attempted_sources: Optional sequence describing all routing attempts
        """
        timestamp = datetime.utcnow().isoformat() + "Z"

        if command not in self.data["commands"]:
            self.data["commands"][command] = {
                "count": 0,
                "legacy_count": 0,
                "unified_count": 0,
                "first_seen": timestamp,
                "last_seen": timestamp,
                "args_patterns": {},
                "last_exit_code": None,
                "last_source": None,
                "fallback_count": 0,
                "attempt_counts": {"unified": 0, "legacy": 0},
                "last_attempts": [],
            }

        cmd_data = self.data["commands"][command]
        cmd_data.setdefault("unified_count", 0)
        cmd_data.setdefault("legacy_count", 0)
        cmd_data.setdefault("args_patterns", {})
        cmd_data.setdefault("last_exit_code", None)
        cmd_data.setdefault("last_source", None)
        cmd_data.setdefault("fallback_count", 0)
        cmd_data.setdefault("attempt_counts", {"unified": 0, "legacy": 0})
        cmd_data.setdefault("last_attempts", [])

        cmd_data["count"] += 1
        if source == "legacy":
            cmd_data["legacy_count"] += 1
        else:
            cmd_data["unified_count"] += 1
        cmd_data["last_seen"] = timestamp
        cmd_data["last_source"] = source
        if exit_code is not None:
            cmd_data["last_exit_code"] = exit_code
        if fallback:
            cmd_data["fallback_count"] += 1

        attempts = list(attempted_sources) if attempted_sources else [source]
        deduped_attempts = []
        for attempt in attempts:
            if attempt not in deduped_attempts:
                deduped_attempts.append(attempt)
            if attempt not in cmd_data["attempt_counts"]:
                cmd_data["attempt_counts"][attempt] = 0
            cmd_data["attempt_counts"][attempt] += 1
        cmd_data["last_attempts"] = deduped_attempts

        # Track argument patterns
        args_key = " ".join(args[:2]) if args else "no_args"
        if args_key not in cmd_data["args_patterns"]:
            cmd_data["args_patterns"][args_key] = 0
        cmd_data["args_patterns"][args_key] += 1

        self._save_data()
    
    def get_deprecation_candidates(self, days: int = 14) -> List[str]:
        """Get commands that haven't been used in N days via legacy path.
        
        Args:
            days: Number of days to check
            
        Returns:
            List of command names that are deprecation candidates
        """
        candidates = []
        cutoff = datetime.utcnow().timestamp() - (days * 86400)
        
        for cmd, data in self.data["commands"].items():
            if data["legacy_count"] > 0:
                last_seen = datetime.fromisoformat(
                    data["last_seen"].replace("Z", "+00:00")
                ).timestamp()
                if last_seen < cutoff:
                    candidates.append(cmd)
        
        return candidates


class LegacyCommandRouter:
    """Routes legacy commands to their implementations."""

    def __init__(
        self,
        project_root: Optional[Path] = None,
        tracker: Optional[TelemetryTracker] = None,
    ):
        """Initialize the legacy command router.

        Args:
            project_root: Root directory of the project
            tracker: Optional shared telemetry tracker instance
        """
        self.project_root = project_root or self._find_project_root()
        self.scripts_dir = self.project_root / "scripts"
        self.unified_automation = self.project_root / "scripts"
        self.tracker = tracker or TelemetryTracker()
        
        # Define command mappings
        self.command_map = {
            # Project generation commands
            "generate-project": {
                "script": "generate_client_project.py",
                "unified": "project_generator_orchestration.py",
                "description": "Generate a new project from templates"
            },
            "generate-from-brief": {
                "script": "generate_from_brief.py",
                "unified": "brief_processor.py",
                "description": "Generate project from a brief file"
            },
            "bootstrap": {
                "script": "bootstrap_project.py",
                "unified": "project_generator_orchestration.py",
                "description": "Bootstrap a new project"
            },
            
            # Planning commands
            "plan-from-brief": {
                "script": "plan_from_brief.py",
                "unified": "brief_processor.py",
                "description": "Generate plan from brief"
            },
            "pre-lifecycle-plan": {
                "script": "pre_lifecycle_plan.py",
                "unified": "plan_manager.py",
                "description": "Create pre-lifecycle plan"
            },
            
            # Workflow commands
            "run-workflow": {
                "script": "run_workflow.py",
                "unified": "ai_orchestrator.py",
                "description": "Execute workflow automation"
            },
            
            # Validation commands
            "validate-compliance": {
                "script": "validate_compliance_assets.py",
                "unified": "compliance_validator.py",
                "description": "Validate compliance documentation"
            },
            "validate-prd": {
                "script": "validate_prd_gate.py",
                "unified": "validation_gates.py",
                "description": "Validate PRD gate"
            },
            "validate-tasks": {
                "script": "validate_tasks.py",
                "unified": "validation_gates.py",
                "description": "Validate task definitions"
            },
            
            # Utility commands
            "doctor": {
                "script": "doctor.py",
                "unified": None,  # Keep as standalone
                "description": "Check environment health"
            },
            "analyze-rules": {
                "script": "analyze_project_rules.py",
                "unified": None,  # Keep as standalone
                "description": "Analyze project rules"
            }
        }
    
    def _find_project_root(self) -> Path:
        """Find the project root directory."""
        current = Path.cwd()
        while current.parent != current:
            if (current / "scripts").exists() and (current / "unified-workflow").exists():
                return current
            current = current.parent
        return Path.cwd()
    
    def list_commands(self) -> List[Tuple[str, str]]:
        """List all available commands.
        
        Returns:
            List of (command, description) tuples
        """
        return [(cmd, info["description"]) for cmd, info in self.command_map.items()]
    
    def route_command(self, command: str, args: List[str], use_legacy: bool = False) -> int:
        """Route a command to its implementation.

        Args:
            command: Command name
            args: Command arguments
            use_legacy: Force use of legacy implementation

        Returns:
            Exit code
        """
        if command not in self.command_map:
            logger.error(f"Unknown command: {command}")
            return 1

        cmd_info = self.command_map[command]
        attempted_sources: List[str] = []
        fallback_used = False
        exit_code: Optional[int] = None
        final_source = "legacy" if use_legacy else "unified"

        if use_legacy or cmd_info["unified"] is None:
            attempted_sources.append("legacy")
            script_name = cmd_info.get("script")
            if not script_name:
                logger.error("Legacy path requested but no legacy script is defined for %s", command)
                exit_code = 1
            else:
                script_path = self.scripts_dir / script_name
                if not script_path.exists():
                    logger.error(f"Legacy script not found: {script_path}")
                    exit_code = 1
                else:
                    logger.info(f"Running legacy command: {command}")
                    exit_code = self._run_legacy_script(script_path, args)
            final_source = "legacy"
        else:
            unified_path = self.unified_automation / cmd_info["unified"]
            if unified_path.exists():
                attempted_sources.append("unified")
                logger.info(f"Running unified command: {command}")
                exit_code = self._run_unified_module(unified_path, args)
                final_source = "unified"

                if exit_code != 0 and cmd_info.get("script"):
                    logger.warning(
                        "Unified command '%s' exited with %s, attempting legacy fallback",
                        command,
                        exit_code,
                    )
                    fallback_used = True
                    attempted_sources.append("legacy")
                    script_path = self.scripts_dir / cmd_info["script"]
                    if script_path.exists():
                        final_source = "legacy"
                        exit_code = self._run_legacy_script(script_path, args)
                    else:
                        logger.error(f"Legacy script not found for fallback: {script_path}")
            else:
                logger.warning("Unified implementation not found for '%s', falling back to legacy", command)
                fallback_used = True
                attempted_sources.extend(["unified", "legacy"])
                script_name = cmd_info.get("script")
                if not script_name:
                    logger.error("No legacy script available for command %s", command)
                    exit_code = 1
                else:
                    script_path = self.scripts_dir / script_name
                    if not script_path.exists():
                        logger.error(f"Legacy script not found: {script_path}")
                        exit_code = 1
                    else:
                        final_source = "legacy"
                        exit_code = self._run_legacy_script(script_path, args)

        self.tracker.track_command(
            command,
            args,
            source=final_source,
            exit_code=exit_code,
            fallback=fallback_used,
            attempted_sources=attempted_sources,
        )

        return exit_code if exit_code is not None else 1
    
    def _run_legacy_script(self, script_path: Path, args: List[str]) -> int:
        """Run a legacy Python script.
        
        Args:
            script_path: Path to the script
            args: Script arguments
            
        Returns:
            Exit code
        """
        cmd = [sys.executable, str(script_path)] + args
        logger.debug(f"Executing: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, cwd=self.project_root)
            return result.returncode
        except Exception as e:
            logger.error(f"Failed to run legacy script: {e}")
            return 1
    
    def _run_unified_module(self, module_path: Path, args: List[str]) -> int:
        """Run a unified workflow module.
        
        Args:
            module_path: Path to the module
            args: Module arguments
            
        Returns:
            Exit code
        """
        # For now, run as subprocess - later can import and call directly
        cmd = [sys.executable, str(module_path)] + args
        logger.debug(f"Executing: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, cwd=self.project_root)
            return result.returncode
        except Exception as e:
            logger.error(f"Failed to run unified module: {e}")
            return 1


def create_parser(router: Optional[LegacyCommandRouter] = None) -> argparse.ArgumentParser:
    """Create the CLI argument parser.

    Returns:
        Configured argument parser
    """
    parser = argparse.ArgumentParser(
        description="Unified Developer Workflow CLI with legacy compatibility",
        epilog="Use 'unified <command> --help' for command-specific help"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="Unified Workflow CLI v1.0.0"
    )
    
    parser.add_argument(
        "--legacy",
        action="store_true",
        help="Force use of legacy script implementation"
    )
    
    parser.add_argument(
        "--show-telemetry",
        action="store_true",
        help="Show telemetry data and exit"
    )
    
    parser.add_argument(
        "--list-deprecation-candidates",
        action="store_true",
        help="List commands that are candidates for deprecation"
    )
    
    router = router or LegacyCommandRouter()

    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add subcommands dynamically from router
    for cmd, desc in router.list_commands():
        subparser = subparsers.add_parser(cmd, help=desc)
        # Add a catch-all for arguments to pass through
        subparser.add_argument(
            "args",
            nargs="*",
            help="Arguments to pass to the command"
        )
    
    return parser


def show_telemetry() -> None:
    """Display telemetry data."""
    tracker = TelemetryTracker()
    
    print("\n=== Unified Workflow Telemetry ===\n")
    
    if not tracker.data["commands"]:
        print("No telemetry data collected yet.")
        return
    
    # Sort commands by usage
    commands = sorted(
        tracker.data["commands"].items(),
        key=lambda x: x[1]["count"],
        reverse=True
    )
    
    header = (
        f"{'Command':<25} {'Total':<8} {'Unified':<8} {'Legacy':<8} "
        f"{'Fallbacks':<10} {'Last Used':<20} {'Exit':<5} {'Source':<8}"
    )
    print(header)
    print("-" * len(header))

    for cmd, data in commands:
        last_used = data["last_seen"][:19].replace("T", " ")
        unified_count = data.get("unified_count", 0)
        legacy_count = data.get("legacy_count", 0)
        fallback_count = data.get("fallback_count", 0)
        exit_code = data.get("last_exit_code")
        last_source = (data.get("last_source") or "-").upper()
        print(
            f"{cmd:<25} {data['count']:<8} {unified_count:<8} {legacy_count:<8} "
            f"{fallback_count:<10} {last_used:<20} {str(exit_code if exit_code is not None else '-'): <5} {last_source:<8}"
        )

    print(f"\nTotal unique commands: {len(commands)}")
    total_calls = sum(d["count"] for _, d in commands)
    total_unified = sum(d.get("unified_count", 0) for _, d in commands)
    total_legacy = sum(d.get("legacy_count", 0) for _, d in commands)
    total_fallbacks = sum(d.get("fallback_count", 0) for _, d in commands)
    print(f"Total command calls: {total_calls}")
    if total_calls:
        print(f"Unified command calls: {total_unified} ({total_unified/total_calls*100:.1f}%)")
        print(f"Legacy command calls: {total_legacy} ({total_legacy/total_calls*100:.1f}%)")
    else:
        print("Unified command calls: 0")
        print("Legacy command calls: 0")
    print(f"Legacy fallbacks: {total_fallbacks}")


class UnifiedCLI:
    """High-level interface bridging the parser and command router."""

    def __init__(self, router: Optional[LegacyCommandRouter] = None) -> None:
        """Create a unified CLI wrapper.

        Args:
            router: Optional pre-configured command router instance.
        """

        self.router = router or LegacyCommandRouter()
        self.parser = create_parser(self.router)
        self.tracker = self.router.tracker

    def run(self, argv: Optional[Sequence[str]] = None) -> int:
        """Execute the CLI using the provided arguments."""

        args = self.parser.parse_args(argv)

        if getattr(args, "show_telemetry", False):
            show_telemetry()
            return 0

        if getattr(args, "list_deprecation_candidates", False):
            candidates = self.tracker.get_deprecation_candidates()
            if candidates:
                print("\nDeprecation candidates (unused for 14+ days via legacy):")
                for cmd in candidates:
                    print(f"  - {cmd}")
            else:
                print("\nNo deprecation candidates found.")
            return 0

        if not getattr(args, "command", None):
            self.parser.print_help()
            return 0

        command_args = getattr(args, "args", []) or []
        return self.router.route_command(args.command, command_args, use_legacy=getattr(args, "legacy", False))


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main CLI entry point."""

    cli = UnifiedCLI()
    return cli.run(argv)


if __name__ == "__main__":
    raise SystemExit(main())
