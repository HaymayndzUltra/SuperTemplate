#!/usr/bin/env python3
"""
Estimate Timeline
Estimates execution timeline for protocol sequence.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timedelta

# Base time estimates per protocol (in hours)
PROTOCOL_TIME_ESTIMATES = {
    "01": {"min": 2, "max": 4, "typical": 3},
    "02": {"min": 4, "max": 8, "typical": 6},
    "03": {"min": 4, "max": 8, "typical": 6},
    "04": {"min": 8, "max": 16, "typical": 12},
    "05": {"min": 4, "max": 8, "typical": 6},
    "05b": {"min": 1, "max": 2, "typical": 1.5},
    "06": {"min": 4, "max": 8, "typical": 6},
    "07": {"min": 8, "max": 16, "typical": 12},
    "08": {"min": 8, "max": 24, "typical": 16},
    "09": {"min": 8, "max": 16, "typical": 12},
    "10": {"min": 16, "max": 40, "typical": 24},
    "11": {"min": 8, "max": 16, "typical": 12},
    "12": {"min": 24, "max": 80, "typical": 40},
    "13": {"min": 8, "max": 24, "typical": 16},
    "14": {"min": 8, "max": 24, "typical": 16},
    "15": {"min": 8, "max": 16, "typical": 12},
    "16": {"min": 4, "max": 8, "typical": 6},
    "17": {"min": 8, "max": 16, "typical": 12},
    "18": {"min": 8, "max": 24, "typical": 16},
    "19": {"min": 8, "max": 16, "typical": 12},
    "20": {"min": 4, "max": 8, "typical": 6},
    "21": {"min": 2, "max": 4, "typical": 3},
    "22": {"min": 8, "max": 16, "typical": 12},
    "23": {"min": 4, "max": 8, "typical": 6},
    "AR": {"min": 4, "max": 8, "typical": 6},
    "CR": {"min": 4, "max": 16, "typical": 8},
    "SR": {"min": 8, "max": 24, "typical": 16}
}

def estimate_protocol_time(protocol_id: str, customizations: dict = None) -> dict:
    """Estimate time for a single protocol."""
    
    base_estimate = PROTOCOL_TIME_ESTIMATES.get(protocol_id, {"min": 4, "max": 8, "typical": 6})
    
    # Apply customization multiplier
    multiplier = 1.0
    if customizations:
        num_customizations = len(customizations.get('customizations', []))
        num_adaptations = len(customizations.get('tech_stack_adaptations', []))
        
        # Add 10% per customization, 5% per adaptation
        multiplier += (num_customizations * 0.1) + (num_adaptations * 0.05)
    
    return {
        "min_hours": round(base_estimate['min'] * multiplier, 1),
        "max_hours": round(base_estimate['max'] * multiplier, 1),
        "typical_hours": round(base_estimate['typical'] * multiplier, 1),
        "multiplier": round(multiplier, 2)
    }

def estimate_timeline(sequence_data: dict, customization_data: dict) -> dict:
    """Estimate complete project timeline."""
    
    sequence = sequence_data.get('sequence', [])
    customizations = {c['protocol_id']: c for c in customization_data.get('customizations', [])}
    
    protocol_estimates = []
    total_min = 0
    total_max = 0
    total_typical = 0
    
    for protocol in sequence:
        protocol_id = protocol.get('protocol_id')
        protocol_customizations = customizations.get(protocol_id, {})
        
        estimate = estimate_protocol_time(protocol_id, protocol_customizations)
        
        protocol_estimates.append({
            "protocol_id": protocol_id,
            "protocol_name": protocol.get('protocol_name'),
            "sequence_number": protocol.get('sequence_number'),
            "estimate": estimate
        })
        
        total_min += estimate['min_hours']
        total_max += estimate['max_hours']
        total_typical += estimate['typical_hours']
    
    # Convert to days (assuming 8-hour workdays)
    days_min = total_min / 8
    days_max = total_max / 8
    days_typical = total_typical / 8
    
    # Convert to weeks
    weeks_min = days_min / 5
    weeks_max = days_max / 5
    weeks_typical = days_typical / 5
    
    return {
        "protocol_estimates": protocol_estimates,
        "totals": {
            "hours": {
                "min": round(total_min, 1),
                "max": round(total_max, 1),
                "typical": round(total_typical, 1)
            },
            "days": {
                "min": round(days_min, 1),
                "max": round(days_max, 1),
                "typical": round(days_typical, 1)
            },
            "weeks": {
                "min": round(weeks_min, 1),
                "max": round(weeks_max, 1),
                "typical": round(weeks_typical, 1)
            }
        },
        "assumptions": {
            "hours_per_day": 8,
            "days_per_week": 5,
            "includes_buffer": False
        }
    }

def main():
    parser = argparse.ArgumentParser(description='Estimate protocol execution timeline')
    parser.add_argument('--sequence', required=True, help='Path to protocol-sequence.json')
    parser.add_argument('--customizations', required=True, help='Path to customization-analysis.json')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 5] Estimating timeline...")
    
    # Load sequence data
    sequence_path = Path(args.sequence)
    if not sequence_path.is_absolute():
        sequence_path = workspace / sequence_path
    
    with open(sequence_path, 'r', encoding='utf-8') as f:
        sequence_data = json.load(f)
    
    # Load customization data
    custom_path = Path(args.customizations)
    if not custom_path.is_absolute():
        custom_path = workspace / custom_path
    
    with open(custom_path, 'r', encoding='utf-8') as f:
        customization_data = json.load(f)
    
    # Estimate timeline
    timeline = estimate_timeline(sequence_data, customization_data)
    
    # Build output
    output = {
        "timestamp": datetime.now().isoformat(),
        "timeline": timeline,
        "summary": {
            "total_protocols": len(timeline['protocol_estimates']),
            "estimated_hours": timeline['totals']['hours']['typical'],
            "estimated_days": timeline['totals']['days']['typical'],
            "estimated_weeks": timeline['totals']['weeks']['typical'],
            "range": f"{timeline['totals']['weeks']['min']}-{timeline['totals']['weeks']['max']} weeks"
        },
        "input_files": {
            "sequence": str(sequence_path),
            "customizations": str(custom_path)
        }
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'timeline-estimate.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 5] Timeline estimation complete")
    print(f"  - Total protocols: {output['summary']['total_protocols']}")
    print(f"  - Estimated hours: {output['summary']['estimated_hours']}")
    print(f"  - Estimated weeks: {output['summary']['range']}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
