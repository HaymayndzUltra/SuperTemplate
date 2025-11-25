#!/usr/bin/env python3
"""
Validate Protocol Coverage
Validates that selected protocols provide adequate coverage (>=95%).
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def validate_coverage(selection_data: dict, gap_data: dict) -> dict:
    """Validate protocol coverage meets threshold."""
    
    coverage_percentage = selection_data.get('coverage', {}).get('coverage_percentage', 0)
    total_gaps = gap_data.get('summary', {}).get('total_gaps', 0)
    high_severity_gaps = gap_data.get('summary', {}).get('high_severity', 0)
    
    # Coverage threshold from spec
    COVERAGE_THRESHOLD = 95.0
    
    # Calculate effective coverage considering gaps
    effective_coverage = coverage_percentage
    if total_gaps > 0:
        # Reduce coverage based on gap severity
        gap_penalty = (high_severity_gaps * 10) + ((total_gaps - high_severity_gaps) * 5)
        effective_coverage = max(0, coverage_percentage - gap_penalty)
    
    # Determine pass/fail
    passes_threshold = effective_coverage >= COVERAGE_THRESHOLD
    
    validation_result = {
        "raw_coverage": coverage_percentage,
        "effective_coverage": round(effective_coverage, 2),
        "threshold": COVERAGE_THRESHOLD,
        "passes_threshold": passes_threshold,
        "gap_penalty": round(coverage_percentage - effective_coverage, 2),
        "status": "PASS" if passes_threshold else "FAIL"
    }
    
    # Generate recommendations if failing
    recommendations = []
    if not passes_threshold:
        if high_severity_gaps > 0:
            recommendations.append("Address high-severity gaps before proceeding")
        if total_gaps > 0:
            recommendations.append("Consider using Protocol 0 to generate missing protocols")
        recommendations.append("Review protocol selection for completeness")
    
    validation_result['recommendations'] = recommendations
    
    return validation_result

def main():
    parser = argparse.ArgumentParser(description='Validate protocol coverage')
    parser.add_argument('--selection', required=True, help='Path to protocol-selection.json')
    parser.add_argument('--gaps', required=True, help='Path to gap-analysis.json')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 3] Validating protocol coverage...")
    
    # Load selection data
    selection_path = Path(args.selection)
    if not selection_path.is_absolute():
        selection_path = workspace / selection_path
    
    with open(selection_path, 'r', encoding='utf-8') as f:
        selection_data = json.load(f)
    
    # Load gap data
    gap_path = Path(args.gaps)
    if not gap_path.is_absolute():
        gap_path = workspace / gap_path
    
    with open(gap_path, 'r', encoding='utf-8') as f:
        gap_data = json.load(f)
    
    # Validate coverage
    validation = validate_coverage(selection_data, gap_data)
    
    # Build output
    output = {
        "timestamp": datetime.now().isoformat(),
        "validation": validation,
        "gate_3_status": validation['status'],
        "input_files": {
            "selection": str(selection_path),
            "gaps": str(gap_path)
        }
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'coverage-validation.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 3] Coverage validation complete")
    print(f"  - Raw coverage: {validation['raw_coverage']}%")
    print(f"  - Effective coverage: {validation['effective_coverage']}%")
    print(f"  - Threshold: {validation['threshold']}%")
    print(f"  - Gate 3 Status: {validation['status']}")
    
    if not validation['passes_threshold']:
        print(f"[WARNING] Coverage below threshold - review recommendations")
        for rec in validation['recommendations']:
            print(f"  - {rec}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
