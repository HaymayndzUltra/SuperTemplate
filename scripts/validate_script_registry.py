#!/usr/bin/env python3
"""
Script Registry Validator - Phase 3 Governance Tool

Validates that all scripts in the repository are properly registered
in script-registry.json and identifies orphaned or undocumented scripts.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple


def load_registry(registry_path: Path) -> Dict:
    """Load the script registry."""
    if not registry_path.exists():
        print(f"ERROR: Registry not found at {registry_path}", file=sys.stderr)
        sys.exit(1)
    
    with open(registry_path) as f:
        return json.load(f)


def collect_registered_scripts(registry: Dict) -> Set[str]:
    """Collect all scripts mentioned in the registry."""
    registered = set()
    
    def _collect_recursive(obj):
        if isinstance(obj, str) and obj.startswith("scripts/"):
            registered.add(obj)
        elif isinstance(obj, dict):
            for value in obj.values():
                _collect_recursive(value)
        elif isinstance(obj, list):
            for item in obj:
                _collect_recursive(item)
    
    _collect_recursive(registry)
    return registered


def find_all_scripts(scripts_dir: Path) -> Set[str]:
    """Find all Python and shell scripts in the scripts directory."""
    all_scripts = set()
    
    for script_path in scripts_dir.rglob("*"):
        if script_path.is_file() and script_path.suffix in {".py", ".sh"}:
            # Normalize to registry format
            relative_path = script_path.relative_to(scripts_dir.parent)
            all_scripts.add(str(relative_path))
    
    return all_scripts


def categorize_scripts(
    all_scripts: Set[str],
    registered: Set[str]
) -> Tuple[Set[str], Set[str], Set[str]]:
    """
    Categorize scripts into:
    - orphaned: exist but not registered
    - phantom: registered but don't exist
    - valid: registered and exist
    """
    orphaned = all_scripts - registered
    phantom = registered - all_scripts
    valid = all_scripts & registered
    
    # Filter out known exceptions
    exceptions = {
        "scripts/__init__.py",
        "scripts/__pycache__",
        "scripts/test.py",
        "scripts/tmp",
    }
    
    orphaned = {s for s in orphaned if not any(exc in s for exc in exceptions)}
    
    return orphaned, phantom, valid


def calculate_coverage(registered: Set[str], all_scripts: Set[str]) -> float:
    """Calculate registration coverage percentage."""
    if not all_scripts:
        return 0.0
    
    # Exclude test files and internal modules
    countable_scripts = {
        s for s in all_scripts 
        if not s.endswith("__init__.py") 
        and not s.startswith("scripts/test_")
        and "__pycache__" not in s
    }
    
    if not countable_scripts:
        return 100.0
    
    registered_countable = registered & countable_scripts
    return (len(registered_countable) / len(countable_scripts)) * 100


def generate_report(
    orphaned: Set[str],
    phantom: Set[str],
    valid: Set[str],
    coverage: float,
    output_path: Path | None = None
) -> Dict:
    """Generate a validation report."""
    report = {
        "status": "pass" if coverage >= 95.0 and not phantom else "fail",
        "coverage_percent": round(coverage, 2),
        "total_scripts": len(valid) + len(orphaned),
        "registered_scripts": len(valid),
        "orphaned_scripts": sorted(list(orphaned)),
        "phantom_scripts": sorted(list(phantom)),
        "valid_scripts": sorted(list(valid)),
        "recommendations": []
    }
    
    # Generate recommendations
    if orphaned:
        report["recommendations"].append({
            "type": "orphaned_scripts",
            "severity": "high",
            "message": f"Found {len(orphaned)} unregistered scripts",
            "action": "Add these scripts to script-registry.json under appropriate categories"
        })
    
    if phantom:
        report["recommendations"].append({
            "type": "phantom_scripts",
            "severity": "critical",
            "message": f"Found {len(phantom)} registered scripts that don't exist",
            "action": "Remove these entries from script-registry.json or create the missing scripts"
        })
    
    if coverage < 95.0:
        report["recommendations"].append({
            "type": "low_coverage",
            "severity": "high",
            "message": f"Script registration coverage is {coverage:.1f}% (target: ≥95%)",
            "action": "Register all production scripts in script-registry.json"
        })
    
    # Write report to file if requested
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"Report written to {output_path}")
    
    return report


def print_summary(report: Dict):
    """Print a human-readable summary."""
    print("\n=== Script Registry Validation Report ===\n")
    print(f"Status: {report['status'].upper()}")
    print(f"Coverage: {report['coverage_percent']}%")
    print(f"Total Scripts: {report['total_scripts']}")
    print(f"Registered: {report['registered_scripts']}")
    print(f"Orphaned: {len(report['orphaned_scripts'])}")
    print(f"Phantom: {len(report['phantom_scripts'])}")
    
    if report['orphaned_scripts']:
        print(f"\n⚠️  Orphaned Scripts ({len(report['orphaned_scripts'])}):")
        for script in report['orphaned_scripts'][:10]:  # Show first 10
            print(f"  - {script}")
        if len(report['orphaned_scripts']) > 10:
            print(f"  ... and {len(report['orphaned_scripts']) - 10} more")
    
    if report['phantom_scripts']:
        print(f"\n❌ Phantom Scripts ({len(report['phantom_scripts'])}):")
        for script in report['phantom_scripts']:
            print(f"  - {script}")
    
    if report['recommendations']:
        print("\n📋 Recommendations:")
        for rec in report['recommendations']:
            severity_icon = {"critical": "🚨", "high": "⚠️", "medium": "ℹ️"}.get(rec['severity'], "•")
            print(f"  {severity_icon} [{rec['severity'].upper()}] {rec['message']}")
            print(f"     Action: {rec['action']}")
    
    print("\n" + "=" * 42)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate script registry coverage and identify orphaned scripts"
    )
    parser.add_argument(
        "--registry",
        type=Path,
        default=Path("scripts/script-registry.json"),
        help="Path to script-registry.json"
    )
    parser.add_argument(
        "--scripts-dir",
        type=Path,
        default=Path("scripts"),
        help="Path to scripts directory"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output path for JSON report (default: stdout only)"
    )
    parser.add_argument(
        "--fail-on-orphans",
        action="store_true",
        help="Exit with code 1 if orphaned scripts are found"
    )
    parser.add_argument(
        "--min-coverage",
        type=float,
        default=95.0,
        help="Minimum required coverage percentage (default: 95.0)"
    )
    
    args = parser.parse_args()
    
    # Load registry
    registry = load_registry(args.registry)
    
    # Collect scripts
    registered = collect_registered_scripts(registry)
    all_scripts = find_all_scripts(args.scripts_dir)
    
    # Categorize
    orphaned, phantom, valid = categorize_scripts(all_scripts, registered)
    
    # Calculate coverage
    coverage = calculate_coverage(registered, all_scripts)
    
    # Generate report
    report = generate_report(orphaned, phantom, valid, coverage, args.output)
    
    # Print summary
    print_summary(report)
    
    # Determine exit code
    exit_code = 0
    if coverage < args.min_coverage:
        print(f"\n❌ Coverage {coverage:.1f}% is below minimum {args.min_coverage}%", file=sys.stderr)
        exit_code = 1
    
    if phantom:
        print(f"\n❌ Found {len(phantom)} phantom scripts (registered but don't exist)", file=sys.stderr)
        exit_code = 1
    
    if args.fail_on_orphans and orphaned:
        print(f"\n❌ Found {len(orphaned)} orphaned scripts (exist but not registered)", file=sys.stderr)
        exit_code = 1
    
    if exit_code == 0:
        print("\n✅ Script registry validation PASSED")
    else:
        print("\n❌ Script registry validation FAILED")
    
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
