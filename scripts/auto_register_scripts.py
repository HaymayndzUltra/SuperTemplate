#!/usr/bin/env python3
"""
Auto-Register Scripts - Phase 3 Governance Tool

Automatically categorizes and registers orphaned scripts into script-registry.json
based on naming conventions, imports, and docstrings.
"""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set


def analyze_script(script_path: Path) -> Dict[str, any]:
    """Analyze a Python script to determine its category."""
    try:
        content = script_path.read_text()
        tree = ast.parse(content)
        
        # Extract docstring
        docstring = ast.get_docstring(tree) or ""
        
        # Extract imports
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
        
        # Extract function names
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        
        return {
            "docstring": docstring.lower(),
            "imports": imports,
            "functions": functions,
            "content": content.lower()
        }
    except:
        return {
            "docstring": "",
            "imports": [],
            "functions": [],
            "content": script_path.read_text().lower() if script_path.exists() else ""
        }


def categorize_script(script_path: Path) -> str:
    """Determine the category of a script based on its content and name."""
    name = script_path.stem.lower()
    analysis = analyze_script(script_path)
    
    # Category patterns
    patterns = {
        "protocol-gates": [
            "validate_gate", "aggregate_evidence", "gate_utils", "run_protocol_gates"
        ],
        "telemetry": [
            "inventory", "generate_protocol_scorecard", "generate_evidence_manifest",
            "protocol_script_inventory"
        ],
        "bootstrap": [
            "bootstrap", "init_client", "generate_client_project", "classify_domain",
            "normalize_project_rules", "optimize_project_rules", "analyze_project_rules"
        ],
        "prd": [
            "prd", "validate_prd", "generate_prd"
        ],
        "task-generation": [
            "task", "enrich_tasks", "lifecycle_tasks", "pre_lifecycle", "plan_from_brief"
        ],
        "execution": [
            "run_workflow", "lane_executor", "ai_executor", "ai_orchestrator",
            "project_generator_orchestration"
        ],
        "quality": [
            "quality_gates", "collect_coverage", "aggregate_coverage",
            "check_hipaa", "enforce_gates", "compliance", "doctor"
        ],
        "evidence": [
            "evidence_manager", "evidence_report", "evidence_schema",
            "migrate_evidence", "collect_perf"
        ],
        "retrospective": [
            "retrospective", "improvement", "trigger_plan", "compare_pull"
        ],
        "discovery": [
            "analyze_jobpost", "analyze_brief", "brief_processor", "tone_mapper"
        ],
        "monitoring": [
            "monitoring", "dashboard", "real_monitoring", "external_services",
            "real_external_validation"
        ],
        "testing": [
            "test_", "validate_script_registry", "integration_test"
        ],
        "utilities": [
            "backup", "benchmark", "detect_", "generate_consistency",
            "generate_protocol_sequence", "update_", "setup_"
        ]
    }
    
    # Check patterns
    for category, keywords in patterns.items():
        if any(keyword in name for keyword in keywords):
            return category
    
    # Check docstring
    docstring = analysis["docstring"]
    if "gate" in docstring or "validator" in docstring:
        return "protocol-gates"
    elif "evidence" in docstring:
        return "evidence"
    elif "quality" in docstring or "audit" in docstring:
        return "quality"
    elif "bootstrap" in docstring or "init" in docstring:
        return "bootstrap"
    elif "task" in docstring:
        return "task-generation"
    
    # Default to utilities
    return "utilities"


def update_registry(
    registry_path: Path,
    orphaned_scripts: List[str],
    dry_run: bool = False
) -> Dict:
    """Update the registry with orphaned scripts."""
    
    # Load current registry
    with open(registry_path) as f:
        registry = json.load(f)
    
    # Categorize orphaned scripts
    categorized = {}
    for script_str in orphaned_scripts:
        script_path = Path(script_str)
        category = categorize_script(script_path)
        
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(script_str)
    
    # Update registry
    updates_made = {}
    for category, scripts in categorized.items():
        if category not in registry:
            registry[category] = {}
        
        # Add scripts to category
        for script in sorted(scripts):
            script_name = Path(script).stem.replace("_", "-")
            
            # Skip if already registered
            if script in str(registry):
                continue
            
            # Find appropriate subcategory or create new one
            if category == "protocol-gates":
                # Already organized by protocol
                continue
            elif len(scripts) == 1:
                registry[category][script_name] = script
            else:
                # Group similar scripts
                if script_name not in registry[category]:
                    if isinstance(registry[category], dict):
                        registry[category][script_name] = script
                    updates_made[script] = category
    
    # Write updated registry
    if not dry_run:
        with open(registry_path, 'w') as f:
            json.dump(registry, f, indent=2)
        print(f"✅ Updated registry: {registry_path}")
    else:
        print("🔍 DRY RUN - No changes made")
    
    return {
        "categorized": categorized,
        "updates_made": updates_made,
        "total_categorized": sum(len(scripts) for scripts in categorized.values())
    }


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Automatically register orphaned scripts"
    )
    parser.add_argument(
        "--registry",
        type=Path,
        default=Path("scripts/script-registry.json"),
        help="Path to script-registry.json"
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path(".artifacts/validation/script-registry-report.json"),
        help="Path to validation report with orphaned scripts"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes"
    )
    
    args = parser.parse_args()
    
    # Load validation report
    if not args.report.exists():
        print(f"ERROR: Validation report not found: {args.report}", file=sys.stderr)
        print("Run validate_script_registry.py first to generate the report", file=sys.stderr)
        return 1
    
    with open(args.report) as f:
        report = json.load(f)
    
    orphaned_scripts = report.get("orphaned_scripts", [])
    
    if not orphaned_scripts:
        print("✅ No orphaned scripts found!")
        return 0
    
    print(f"📋 Found {len(orphaned_scripts)} orphaned scripts")
    print(f"🔄 Categorizing and registering...\n")
    
    # Update registry
    result = update_registry(args.registry, orphaned_scripts, args.dry_run)
    
    # Print summary
    print("\n=== Auto-Registration Summary ===\n")
    print(f"Total Scripts Categorized: {result['total_categorized']}")
    print("\nCategories:")
    for category, scripts in sorted(result['categorized'].items()):
        print(f"  {category}: {len(scripts)} scripts")
    
    if args.dry_run:
        print("\n🔍 This was a DRY RUN - re-run without --dry-run to apply changes")
    else:
        print("\n✅ Registry updated successfully!")
        print("   Run validate_script_registry.py to verify coverage")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
