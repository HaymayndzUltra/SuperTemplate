#!/usr/bin/env python3
"""
Protocol 23 Artifact Generator - Automated Script Governance

Generates required artifacts for Protocol 23 (Script Governance):
1. Complete script index with metadata
2. Documentation audit report
3. Remediation backlog with prioritized actions
"""

from __future__ import annotations

import ast
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


def extract_script_metadata(script_path: Path) -> Dict:
    """Extract metadata from a Python script."""
    try:
        content = script_path.read_text()
        tree = ast.parse(content)
        
        # Extract docstring
        docstring = ast.get_docstring(tree) or "No description available"
        
        # Extract functions and classes
        functions = []
        classes = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_doc = ast.get_docstring(node) or ""
                functions.append({
                    "name": node.name,
                    "docstring": func_doc,
                    "is_public": not node.name.startswith("_")
                })
            elif isinstance(node, ast.ClassDef):
                class_doc = ast.get_docstring(node) or ""
                classes.append({
                    "name": node.name,
                    "docstring": class_doc
                })
        
        # Count lines
        lines = content.splitlines()
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith("#")]
        
        # Check for main guard
        has_main_guard = "if __name__ ==" in content
        
        # Check for shebang
        has_shebang = content.startswith("#!")
        
        return {
            "description": docstring.split("\n")[0] if docstring else "No description",
            "full_docstring": docstring,
            "functions": functions,
            "classes": classes,
            "total_lines": len(lines),
            "code_lines": len(code_lines),
            "has_main_guard": has_main_guard,
            "has_shebang": has_shebang,
            "is_executable": script_path.stat().st_mode & 0o111 != 0
        }
    except Exception as e:
        return {
            "description": f"Error parsing script: {e}",
            "full_docstring": "",
            "functions": [],
            "classes": [],
            "total_lines": 0,
            "code_lines": 0,
            "has_main_guard": False,
            "has_shebang": False,
            "is_executable": False
        }


def generate_script_index(scripts_dir: Path, output_path: Path):
    """Generate complete script index with metadata."""
    print("📋 Generating script index...")
    
    index = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "scripts_directory": str(scripts_dir),
        "total_scripts": 0,
        "scripts": {}
    }
    
    # Find all Python scripts
    for script_path in sorted(scripts_dir.glob("*.py")):
        if script_path.name.startswith("_") or script_path.name == "__init__.py":
            continue
        
        metadata = extract_script_metadata(script_path)
        relative_path = script_path.relative_to(scripts_dir.parent)
        
        index["scripts"][str(relative_path)] = {
            "name": script_path.stem,
            "path": str(relative_path),
            "size_bytes": script_path.stat().st_size,
            "last_modified": datetime.fromtimestamp(script_path.stat().st_mtime).isoformat(),
            **metadata
        }
        
        index["total_scripts"] += 1
    
    # Write index
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(index, f, indent=2)
    
    print(f"✅ Script index generated: {output_path}")
    print(f"   Total scripts indexed: {index['total_scripts']}")
    
    return index


def audit_documentation(index: Dict, output_path: Path):
    """Audit script documentation completeness."""
    print("\n📚 Auditing documentation...")
    
    audit = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "total_scripts": len(index["scripts"]),
        "documented": 0,
        "undocumented": 0,
        "partially_documented": 0,
        "documentation_score": 0.0,
        "issues": []
    }
    
    for script_path, metadata in index["scripts"].items():
        score = 0
        max_score = 5
        issues_for_script = []
        
        # Check docstring
        if metadata["full_docstring"] and len(metadata["full_docstring"]) > 20:
            score += 1
        else:
            issues_for_script.append("Missing or inadequate module docstring")
        
        # Check functions documentation
        if metadata["functions"]:
            documented_functions = sum(
                1 for f in metadata["functions"]
                if f["docstring"] and len(f["docstring"]) > 10
            )
            if documented_functions == len(metadata["functions"]):
                score += 1
            elif documented_functions > 0:
                score += 0.5
                issues_for_script.append(
                    f"Only {documented_functions}/{len(metadata['functions'])} functions documented"
                )
            else:
                issues_for_script.append("No function docstrings")
        else:
            score += 0.5  # No functions to document
        
        # Check main guard
        if metadata["has_main_guard"]:
            score += 1
        else:
            issues_for_script.append("Missing main guard (if __name__ == '__main__')")
        
        # Check shebang
        if metadata["has_shebang"]:
            score += 1
        else:
            issues_for_script.append("Missing shebang (#!)")
        
        # Check executable permission
        if metadata["is_executable"]:
            score += 1
        else:
            issues_for_script.append("Not executable (chmod +x needed)")
        
        # Categorize
        score_percent = (score / max_score) * 100
        if score_percent >= 80:
            audit["documented"] += 1
        elif score_percent >= 40:
            audit["partially_documented"] += 1
        else:
            audit["undocumented"] += 1
        
        if issues_for_script:
            audit["issues"].append({
                "script": script_path,
                "score": round(score_percent, 1),
                "issues": issues_for_script
            })
    
    # Calculate overall score
    if audit["total_scripts"] > 0:
        audit["documentation_score"] = round(
            (audit["documented"] / audit["total_scripts"]) * 100, 2
        )
    
    # Write audit
    with open(output_path, 'w') as f:
        json.dump(audit, f, indent=2)
    
    print(f"✅ Documentation audit generated: {output_path}")
    print(f"   Documentation score: {audit['documentation_score']}%")
    print(f"   Fully documented: {audit['documented']}")
    print(f"   Partially documented: {audit['partially_documented']}")
    print(f"   Undocumented: {audit['undocumented']}")
    
    return audit


def generate_remediation_backlog(
    audit: Dict,
    registry_report_path: Path,
    output_path: Path
):
    """Generate prioritized remediation backlog."""
    print("\n🔧 Generating remediation backlog...")
    
    backlog = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "total_issues": 0,
        "critical_issues": 0,
        "high_priority_issues": 0,
        "medium_priority_issues": 0,
        "remediation_items": []
    }
    
    # Add registry coverage issues
    if registry_report_path.exists():
        with open(registry_report_path) as f:
            registry_report = json.load(f)
        
        if registry_report["coverage_percent"] < 95:
            backlog["remediation_items"].append({
                "priority": "critical",
                "category": "governance",
                "issue": f"Script registry coverage is {registry_report['coverage_percent']}% (target: ≥95%)",
                "affected_items": registry_report["orphaned_scripts"][:5],
                "action": "Register all orphaned scripts in script-registry.json",
                "estimated_effort": "2-4 hours",
                "automation": "python3 scripts/auto_register_scripts.py"
            })
            backlog["critical_issues"] += 1
    
    # Add documentation issues
    for issue_record in audit.get("issues", []):
        if issue_record["score"] < 40:
            priority = "high"
            backlog["high_priority_issues"] += 1
        else:
            priority = "medium"
            backlog["medium_priority_issues"] += 1
        
        backlog["remediation_items"].append({
            "priority": priority,
            "category": "documentation",
            "issue": f"Script {issue_record['script']} has documentation score of {issue_record['score']}%",
            "affected_items": [issue_record['script']],
            "action": "\n".join([
                "Fix the following:",
                *[f"  - {issue}" for issue in issue_record["issues"]]
            ]),
            "estimated_effort": "15-30 minutes per script"
        })
    
    backlog["total_issues"] = len(backlog["remediation_items"])
    
    # Write backlog
    with open(output_path, 'w') as f:
        json.dump(backlog, f, indent=2)
    
    print(f"✅ Remediation backlog generated: {output_path}")
    print(f"   Total issues: {backlog['total_issues']}")
    print(f"   Critical: {backlog['critical_issues']}")
    print(f"   High: {backlog['high_priority_issues']}")
    print(f"   Medium: {backlog['medium_priority_issues']}")
    
    return backlog


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Generate Protocol 23 governance artifacts"
    )
    parser.add_argument(
        "--scripts-dir",
        type=Path,
        default=Path("scripts"),
        help="Path to scripts directory"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(".artifacts/protocol-23"),
        help="Output directory for artifacts"
    )
    parser.add_argument(
        "--registry-report",
        type=Path,
        default=Path(".artifacts/validation/script-registry-report.json"),
        help="Path to script registry validation report"
    )
    
    args = parser.parse_args()
    
    print("=== Protocol 23 Artifact Generation ===\n")
    
    # Generate script index
    script_index_path = args.output_dir / "script-index.json"
    index = generate_script_index(args.scripts_dir, script_index_path)
    
    # Audit documentation
    doc_audit_path = args.output_dir / "documentation-audit.json"
    audit = audit_documentation(index, doc_audit_path)
    
    # Generate remediation backlog
    remediation_path = args.output_dir / "remediation-backlog.json"
    backlog = generate_remediation_backlog(audit, args.registry_report, remediation_path)
    
    print("\n" + "=" * 42)
    print("✅ Protocol 23 artifacts generated successfully!")
    print(f"\nArtifacts location: {args.output_dir}")
    print("  - script-index.json: Complete script inventory")
    print("  - documentation-audit.json: Documentation completeness audit")
    print("  - remediation-backlog.json: Prioritized action items")
    
    # Exit with failure if critical issues found
    if backlog["critical_issues"] > 0:
        print(f"\n⚠️  WARNING: {backlog['critical_issues']} critical issues require attention")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
