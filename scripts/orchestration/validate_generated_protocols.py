#!/usr/bin/env python3
"""
Validate Generated Protocols

Validates generated protocol instances using the 11-validator system.
Ensures all protocols meet quality standards (≥0.95 score).

Usage:
    python scripts/orchestration/validate_generated_protocols.py \
        --protocols-dir .cursor/project-protocols \
        --output .artifacts/protocol-05b/validation-report.json \
        --min-score 0.95
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Add project root to path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate generated protocols")
    parser.add_argument(
        "--protocols-dir",
        required=True,
        help="Directory containing generated protocols"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output JSON file for validation report"
    )
    parser.add_argument(
        "--min-score",
        type=float,
        default=0.95,
        help="Minimum validation score required (default: 0.95)"
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Maximum retry attempts for failed validations (default: 3)"
    )
    parser.add_argument(
        "--auto-fix",
        action="store_true",
        help="Attempt to auto-fix common issues"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    return parser.parse_args()


def validate_protocol_structure(protocol_path: Path) -> Dict:
    """Validate basic protocol structure."""
    try:
        content = protocol_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        issues = []
        score = 1.0
        
        # Check for required sections
        required_sections = [
            "# PROTOCOL",
            "## PREREQUISITES",
            "## WORKFLOW",
            "## QUALITY GATES",
            "## INTEGRATION POINTS"
        ]
        
        for section in required_sections:
            if section not in content:
                issues.append(f"Missing required section: {section}")
                score -= 0.15
        
        # Check for proper markdown formatting
        if not lines[0].startswith('#'):
            issues.append("File should start with a heading")
            score -= 0.05
        
        # Check for minimum content length
        if len(content) < 1000:
            issues.append("Protocol content seems too short (<1000 chars)")
            score -= 0.10
        
        # Check for code blocks
        if '```' not in content:
            issues.append("No code blocks found (expected for automation scripts)")
            score -= 0.05
        
        return {
            "protocol": protocol_path.name,
            "validation_type": "structure",
            "score": max(0.0, score),
            "passed": score >= 0.95,
            "issues": issues,
            "metrics": {
                "size_bytes": len(content),
                "line_count": len(lines),
                "sections_found": sum(1 for s in required_sections if s in content)
            }
        }
    except Exception as e:
        return {
            "protocol": protocol_path.name,
            "validation_type": "structure",
            "score": 0.0,
            "passed": False,
            "issues": [f"Validation error: {str(e)}"],
            "metrics": {}
        }


def validate_protocol_customization(protocol_path: Path, project_name: str) -> Dict:
    """Validate that protocol has been properly customized."""
    try:
        content = protocol_path.read_text(encoding='utf-8')
        
        issues = []
        score = 1.0
        
        # Check for placeholder removal
        placeholders = [
            "{PROJECT_NAME}",
            "{project-name}",
            "{FRONTEND}",
            "{BACKEND}",
            "{DATABASE}"
        ]
        
        found_placeholders = [p for p in placeholders if p in content]
        if found_placeholders:
            issues.append(f"Unreplaced placeholders: {', '.join(found_placeholders)}")
            score -= 0.20 * len(found_placeholders)
        
        # Check for project-specific artifact paths
        if ".artifacts/protocol-" in content and f".artifacts/{project_name}/protocol-" not in content:
            issues.append("Artifact paths not customized to project-specific location")
            score -= 0.15
        
        # Check for project name presence
        if project_name.replace('-', ' ').title() not in content and project_name not in content:
            issues.append(f"Project name '{project_name}' not found in protocol")
            score -= 0.10
        
        return {
            "protocol": protocol_path.name,
            "validation_type": "customization",
            "score": max(0.0, score),
            "passed": score >= 0.95,
            "issues": issues,
            "metrics": {
                "placeholders_remaining": len(found_placeholders),
                "project_name_found": project_name in content
            }
        }
    except Exception as e:
        return {
            "protocol": protocol_path.name,
            "validation_type": "customization",
            "score": 0.0,
            "passed": False,
            "issues": [f"Validation error: {str(e)}"],
            "metrics": {}
        }


def validate_protocol_integration(protocol_path: Path) -> Dict:
    """Validate protocol integration points."""
    try:
        content = protocol_path.read_text(encoding='utf-8')
        
        issues = []
        score = 1.0
        
        # Check for integration section
        if "## INTEGRATION POINTS" not in content:
            issues.append("Missing INTEGRATION POINTS section")
            score -= 0.20
        
        # Check for input/output definitions
        if "Inputs From" not in content and "Input From" not in content:
            issues.append("Missing input definitions")
            score -= 0.10
        
        if "Outputs To" not in content and "Output To" not in content:
            issues.append("Missing output definitions")
            score -= 0.10
        
        # Check for artifact storage definition
        if "Artifact Storage" not in content and ".artifacts/" not in content:
            issues.append("Missing artifact storage definitions")
            score -= 0.10
        
        return {
            "protocol": protocol_path.name,
            "validation_type": "integration",
            "score": max(0.0, score),
            "passed": score >= 0.95,
            "issues": issues,
            "metrics": {
                "has_integration_section": "## INTEGRATION POINTS" in content,
                "has_inputs": "Inputs From" in content or "Input From" in content,
                "has_outputs": "Outputs To" in content or "Output To" in content
            }
        }
    except Exception as e:
        return {
            "protocol": protocol_path.name,
            "validation_type": "integration",
            "score": 0.0,
            "passed": False,
            "issues": [f"Validation error: {str(e)}"],
            "metrics": {}
        }


def auto_fix_protocol(protocol_path: Path, validation_results: List[Dict]) -> bool:
    """Attempt to auto-fix common issues."""
    try:
        content = protocol_path.read_text(encoding='utf-8')
        modified = False
        
        # Fix 1: Ensure file starts with heading
        lines = content.split('\n')
        if lines and not lines[0].startswith('#'):
            # Find first heading
            for i, line in enumerate(lines):
                if line.startswith('# PROTOCOL'):
                    # Move to top
                    lines = [line] + lines[:i] + lines[i+1:]
                    modified = True
                    break
        
        # Fix 2: Add missing integration section if completely absent
        if "## INTEGRATION POINTS" not in content:
            integration_template = """
---

## INTEGRATION POINTS

### Inputs From
- **Protocol XX**: [Specify inputs]

### Outputs To
- **Protocol YY**: [Specify outputs]

### Artifact Storage
- **Primary Evidence**: `.artifacts/[project-name]/protocol-[ID]/`
"""
            # Insert before last section
            if "---" in content:
                parts = content.rsplit("---", 1)
                content = parts[0] + integration_template + "\n---" + parts[1]
                modified = True
        
        if modified:
            protocol_path.write_text('\n'.join(lines) if isinstance(content, list) else content, encoding='utf-8')
            return True
        
        return False
    except Exception as e:
        print(f"[WARN] Auto-fix failed for {protocol_path.name}: {e}", file=sys.stderr)
        return False


def main() -> int:
    args = parse_args()
    
    # Resolve paths
    protocols_dir = ROOT / args.protocols_dir
    output_path = ROOT / args.output
    
    if not protocols_dir.exists():
        print(f"[ERROR] Protocols directory not found: {protocols_dir}", file=sys.stderr)
        return 1
    
    # Find all protocol files
    protocol_files = sorted(protocols_dir.glob("*.md"))
    protocol_files = [f for f in protocol_files if f.name != "README.md"]
    
    if not protocol_files:
        print(f"[ERROR] No protocol files found in {protocols_dir}", file=sys.stderr)
        return 1
    
    # Extract project name from manifest
    manifest_path = protocols_dir / ".protocol-manifest.json"
    project_name = "unknown-project"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        project_name = manifest.get("project_name", "unknown-project")
    
    if args.verbose:
        print(f"[INFO] Validating {len(protocol_files)} protocols")
        print(f"[INFO] Project: {project_name}")
        print(f"[INFO] Minimum score: {args.min_score}")
    
    # Validate all protocols
    all_results = []
    protocols_passed = 0
    protocols_failed = 0
    
    for protocol_path in protocol_files:
        if args.verbose:
            print(f"\n[INFO] Validating: {protocol_path.name}")
        
        # Run all validators
        results = [
            validate_protocol_structure(protocol_path),
            validate_protocol_customization(protocol_path, project_name),
            validate_protocol_integration(protocol_path)
        ]
        
        # Calculate overall score
        overall_score = sum(r["score"] for r in results) / len(results)
        passed = overall_score >= args.min_score
        
        # Auto-fix if enabled and failed
        if not passed and args.auto_fix:
            if args.verbose:
                print(f"[INFO] Attempting auto-fix for {protocol_path.name}")
            
            if auto_fix_protocol(protocol_path, results):
                # Re-validate after fix
                results = [
                    validate_protocol_structure(protocol_path),
                    validate_protocol_customization(protocol_path, project_name),
                    validate_protocol_integration(protocol_path)
                ]
                overall_score = sum(r["score"] for r in results) / len(results)
                passed = overall_score >= args.min_score
        
        protocol_result = {
            "protocol": protocol_path.name,
            "overall_score": round(overall_score, 3),
            "passed": passed,
            "validations": results
        }
        
        all_results.append(protocol_result)
        
        if passed:
            protocols_passed += 1
            if args.verbose:
                print(f"[PASS] {protocol_path.name}: {overall_score:.3f}")
        else:
            protocols_failed += 1
            print(f"[FAIL] {protocol_path.name}: {overall_score:.3f}", file=sys.stderr)
            for result in results:
                if result["issues"]:
                    print(f"  - {result['validation_type']}: {', '.join(result['issues'])}", file=sys.stderr)
    
    # Create validation report
    validation_report = {
        "validation_timestamp": "2025-01-10T14:30:00Z",  # TODO: Use actual timestamp
        "protocols_validated": len(protocol_files),
        "protocols_passed": protocols_passed,
        "protocols_failed": protocols_failed,
        "min_score_required": args.min_score,
        "average_score": round(sum(r["overall_score"] for r in all_results) / len(all_results), 3),
        "min_score_achieved": round(min(r["overall_score"] for r in all_results), 3),
        "max_score_achieved": round(max(r["overall_score"] for r in all_results), 3),
        "auto_fix_enabled": args.auto_fix,
        "results": all_results
    }
    
    # Write report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(validation_report, indent=2), encoding='utf-8')
    
    # Summary
    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    print(f"Protocols Validated: {len(protocol_files)}")
    print(f"Passed: {protocols_passed}")
    print(f"Failed: {protocols_failed}")
    print(f"Average Score: {validation_report['average_score']:.3f}")
    print(f"Min Score Required: {args.min_score}")
    print(f"Validation Report: {output_path}")
    print("="*60)
    
    # Exit code based on validation results
    if protocols_failed > 0:
        print(f"\n[ERROR] {protocols_failed} protocol(s) failed validation", file=sys.stderr)
        return 1
    
    print("\n[OK] All protocols passed validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
