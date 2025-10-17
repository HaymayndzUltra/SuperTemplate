#!/usr/bin/env python3
"""
Protocol Validation Script
Validates all protocols in the AI-driven workflow system
"""

import os
import sys
import json
import argparse
from pathlib import Path

def validate_protocol_structure(protocol_path):
    """Validate a single protocol file structure"""
    required_sections = [
        "AI ROLE AND MISSION",
        "INTEGRATION POINTS", 
        "QUALITY GATES",
        "COMMUNICATION PROTOCOLS",
        "HANDOFF CHECKLIST"
    ]
    
    try:
        with open(protocol_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        missing_sections = []
        for section in required_sections:
            if section not in content:
                missing_sections.append(section)
                
        return {
            "file": str(protocol_path),
            "valid": len(missing_sections) == 0,
            "missing_sections": missing_sections,
            "has_must_markers": "[MUST]" in content,
            "has_guideline_markers": "[GUIDELINE]" in content,
            "has_critical_markers": "[CRITICAL]" in content
        }
    except Exception as e:
        return {
            "file": str(protocol_path),
            "valid": False,
            "error": str(e)
        }

def main():
    parser = argparse.ArgumentParser(description="Validate AI-driven workflow protocols")
    parser.add_argument("--all", action="store_true", help="Validate all protocols")
    parser.add_argument("--protocols", nargs="+", help="Specific protocol numbers to validate")
    parser.add_argument("--output", help="Output file for validation results")
    
    args = parser.parse_args()
    
    workflow_dir = Path(".cursor/ai-driven-workflow")
    results = []
    
    if args.all:
        # Find all protocol files
        protocol_files = list(workflow_dir.glob("*.md"))
        protocol_files = [f for f in protocol_files if f.name[0].isdigit()]
        
        for protocol_file in sorted(protocol_files):
            result = validate_protocol_structure(protocol_file)
            results.append(result)
    
    elif args.protocols:
        for protocol_num in args.protocols:
            pattern = f"{protocol_num}-*.md"
            protocol_files = list(workflow_dir.glob(pattern))
            
            for protocol_file in protocol_files:
                result = validate_protocol_structure(protocol_file)
                results.append(result)
    
    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Validation results saved to {args.output}")
    else:
        for result in results:
            status = "✅ VALID" if result["valid"] else "❌ INVALID"
            print(f"{status}: {result['file']}")
            if not result["valid"] and "missing_sections" in result:
                print(f"  Missing sections: {', '.join(result['missing_sections'])}")

if __name__ == "__main__":
    main()
