#!/usr/bin/env python3
"""
Workflow Completeness Validation Script
Validates complete SDLC coverage across all protocols
"""

import os
import sys
import json
import argparse
from pathlib import Path

def analyze_workflow_completeness():
    """Analyze workflow completeness across SDLC phases"""
    
    workflow_dir = Path(".cursor/ai-driven-workflow")
    
    # Expected SDLC phases and their protocol coverage
    sdlc_phases = {
        "project_initiation": {
            "protocols": ["01", "02", "01", "00"],
            "coverage": 0,
            "total_needed": 4
        },
        "planning_design": {
            "protocols": ["1", "2", "6"],
            "coverage": 0,
            "total_needed": 3
        },
        "development": {
            "protocols": ["3", "7"],
            "coverage": 0,
            "total_needed": 2
        },
        "integration_testing": {
            "protocols": ["9", "4", "15"],
            "coverage": 0,
            "total_needed": 3
        },
        "deployment": {
            "protocols": ["10", "11"],
            "coverage": 0,
            "total_needed": 2
        },
        "maintenance_support": {
            "protocols": ["12", "13", "14"],
            "coverage": 0,
            "total_needed": 3
        },
        "project_closure": {
            "protocols": ["16", "17", "18", "5"],
            "coverage": 0,
            "total_needed": 4
        }
    }
    
    # Find existing protocols
    existing_protocols = []
    for protocol_file in workflow_dir.glob("*.md"):
        if protocol_file.name[0].isdigit():
            protocol_num = protocol_file.name.split('-')[0]
            existing_protocols.append(protocol_num)
    
    # Calculate coverage for each phase
    for phase, data in sdlc_phases.items():
        existing_in_phase = [p for p in data["protocols"] if p in existing_protocols]
        data["coverage"] = len(existing_in_phase)
        data["existing_protocols"] = existing_in_phase
        data["missing_protocols"] = [p for p in data["protocols"] if p not in existing_protocols]
        data["coverage_percentage"] = (data["coverage"] / data["total_needed"]) * 100
    
    # Overall completeness
    total_existing = len(existing_protocols)
    total_needed = sum(data["total_needed"] for data in sdlc_phases.values())
    overall_coverage = (total_existing / total_needed) * 100
    
    return {
        "sdlc_phases": sdlc_phases,
        "overall_coverage": overall_coverage,
        "total_existing_protocols": total_existing,
        "total_needed_protocols": total_needed,
        "existing_protocols": sorted(existing_protocols),
        "workflow_complete": overall_coverage >= 100
    }

def main():
    parser = argparse.ArgumentParser(description="Validate workflow completeness")
    parser.add_argument("--output", help="Output file for completeness analysis")
    
    args = parser.parse_args()
    
    results = analyze_workflow_completeness()
    
    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Workflow completeness analysis saved to {args.output}")
    else:
        print(f"Overall Coverage: {results['overall_coverage']:.1f}%")
        print(f"Existing Protocols: {results['total_existing_protocols']}/{results['total_needed_protocols']}")
        print(f"Workflow Complete: {'✅ YES' if results['workflow_complete'] else '❌ NO'}")
        print("\nPhase Coverage:")
        
        for phase, data in results["sdlc_phases"].items():
            status = "✅" if data["coverage_percentage"] >= 100 else "⚠️" if data["coverage_percentage"] >= 50 else "❌"
            print(f"  {status} {phase.replace('_', ' ').title()}: {data['coverage']}/{data['total_needed']} ({data['coverage_percentage']:.1f}%)")
            if data["missing_protocols"]:
                print(f"    Missing: {', '.join(data['missing_protocols'])}")

if __name__ == "__main__":
    main()
