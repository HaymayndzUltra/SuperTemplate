#!/usr/bin/env python3
"""
Circular Validation Test Script
Tests protocol → meta-analysis → validation circular flow
"""

import os
import sys
import json
import argparse
from pathlib import Path

def test_circular_validation(protocol_path):
    """Test circular validation for a single protocol"""
    try:
        with open(protocol_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if protocol has required structure for meta-analysis
        required_elements = [
            "AI ROLE AND MISSION",
            "QUALITY GATES", 
            "COMMUNICATION PROTOCOLS",
            "[MUST]",
            "[GUIDELINE]"
        ]
        
        has_all_elements = all(element in content for element in required_elements)
        
        # Simulate meta-analysis validation
        meta_analysis_layers = {
            "layer_1_system_decisions": "AI ROLE AND MISSION" in content,
            "layer_2_behavioral_control": "QUALITY GATES" in content,
            "layer_3_procedural_logic": "[MUST]" in content and "[GUIDELINE]" in content,
            "layer_4_communication": "COMMUNICATION PROTOCOLS" in content
        }
        
        all_layers_present = all(meta_analysis_layers.values())
        
        return {
            "file": str(protocol_path),
            "circular_validation_passed": has_all_elements and all_layers_present,
            "has_required_structure": has_all_elements,
            "meta_analysis_layers": meta_analysis_layers,
            "all_layers_present": all_layers_present
        }
        
    except Exception as e:
        return {
            "file": str(protocol_path),
            "circular_validation_passed": False,
            "error": str(e)
        }

def main():
    parser = argparse.ArgumentParser(description="Test circular validation for protocols")
    parser.add_argument("--protocols", nargs="+", help="Protocol numbers to test")
    parser.add_argument("--output", help="Output file for test results")
    
    args = parser.parse_args()
    
    workflow_dir = Path(".cursor/ai-driven-workflow")
    results = []
    
    if args.protocols:
        for protocol_num in args.protocols:
            pattern = f"{protocol_num}-*.md"
            protocol_files = list(workflow_dir.glob(pattern))
            
            for protocol_file in protocol_files:
                result = test_circular_validation(protocol_file)
                results.append(result)
    
    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Circular validation test results saved to {args.output}")
    else:
        for result in results:
            status = "✅ PASSED" if result["circular_validation_passed"] else "❌ FAILED"
            print(f"{status}: {result['file']}")
            if not result["circular_validation_passed"] and "meta_analysis_layers" in result:
                failed_layers = [k for k, v in result["meta_analysis_layers"].items() if not v]
                if failed_layers:
                    print(f"  Failed layers: {', '.join(failed_layers)}")

if __name__ == "__main__":
    main()
