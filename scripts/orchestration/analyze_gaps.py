#!/usr/bin/env python3
"""
Analyze Gaps
Identifies gaps in protocol coverage that may require Protocol 0 generation.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def identify_coverage_gaps(selection_data: dict, characteristics_data: dict) -> list:
    """Identify gaps where characteristics aren't covered by selected protocols."""
    
    gaps = []
    
    # Get detected characteristics
    detected = [c for c in characteristics_data.get('all_characteristics', []) if c.get('detected')]
    
    # Get selected protocol IDs
    selected = selection_data.get('selected_protocols', {})
    all_selected_ids = []
    for category in ['required', 'recommended']:
        for protocol in selected.get(category, []):
            all_selected_ids.append(protocol.get('id'))
    
    # Check unavailable protocols for gaps
    unavailable = selected.get('unavailable', [])
    for protocol in unavailable:
        gaps.append({
            "type": "missing_template",
            "protocol_id": protocol.get('id'),
            "protocol_name": protocol.get('name'),
            "severity": "high" if protocol.get('id') in ['06', '07', '08'] else "medium",
            "reason": "Protocol template not found in workspace",
            "recommendation": "Use Protocol 0 to generate template or acquire from repository"
        })
    
    # Check for characteristic gaps (characteristics without protocol coverage)
    # This is a simplified check - in production, would have detailed mapping
    uncovered_categories = set()
    for char in detected:
        category = char.get('category')
        # Check if any protocol covers this category
        has_coverage = False
        for protocol in selected.get('required', []) + selected.get('recommended', []):
            # Simplified check - assume protocols cover their track
            if protocol.get('track') == 'ai_ml' and category == 'ai_ml':
                has_coverage = True
            elif protocol.get('track') == 'generic' and category in ['application', 'infrastructure', 'data']:
                has_coverage = True
        
        if not has_coverage and category not in uncovered_categories:
            uncovered_categories.add(category)
    
    for category in uncovered_categories:
        gaps.append({
            "type": "uncovered_category",
            "category": category,
            "severity": "medium",
            "reason": f"Characteristics in '{category}' category may not be fully covered",
            "recommendation": "Review protocol selection or generate custom protocol"
        })
    
    return gaps

def generate_gap_specifications(gaps: list) -> list:
    """Generate gap specifications for Protocol 0."""
    
    gap_specs = []
    
    for i, gap in enumerate(gaps):
        if gap['type'] == 'missing_template':
            gap_specs.append({
                "gap_id": f"GAP-{i+1:03d}",
                "gap_type": "missing_protocol",
                "protocol_id": gap.get('protocol_id'),
                "protocol_name": gap.get('protocol_name'),
                "severity": gap.get('severity'),
                "requires_protocol_0": True,
                "suggested_action": "Generate protocol template using Protocol 0"
            })
    
    return gap_specs

def main():
    parser = argparse.ArgumentParser(description='Analyze protocol coverage gaps')
    parser.add_argument('--selection', required=True, help='Path to protocol-selection.json')
    parser.add_argument('--characteristics', required=True, help='Path to characteristics-detection.json')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 3] Analyzing protocol coverage gaps...")
    
    # Load selection data
    selection_path = Path(args.selection)
    if not selection_path.is_absolute():
        selection_path = workspace / selection_path
    
    with open(selection_path, 'r', encoding='utf-8') as f:
        selection_data = json.load(f)
    
    # Load characteristics data
    char_path = Path(args.characteristics)
    if not char_path.is_absolute():
        char_path = workspace / char_path
    
    with open(char_path, 'r', encoding='utf-8') as f:
        characteristics_data = json.load(f)
    
    # Identify gaps
    gaps = identify_coverage_gaps(selection_data, characteristics_data)
    
    # Generate gap specifications
    gap_specs = generate_gap_specifications(gaps)
    
    # Calculate gap severity summary
    high_severity = len([g for g in gaps if g.get('severity') == 'high'])
    medium_severity = len([g for g in gaps if g.get('severity') == 'medium'])
    low_severity = len([g for g in gaps if g.get('severity') == 'low'])
    
    # Build output
    output = {
        "timestamp": datetime.now().isoformat(),
        "gaps": gaps,
        "gap_specifications": gap_specs,
        "summary": {
            "total_gaps": len(gaps),
            "high_severity": high_severity,
            "medium_severity": medium_severity,
            "low_severity": low_severity,
            "requires_protocol_0": any(g.get('requires_protocol_0') for g in gap_specs),
            "coverage_status": "complete" if len(gaps) == 0 else "gaps_identified"
        },
        "input_files": {
            "selection": str(selection_path),
            "characteristics": str(char_path)
        }
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'gap-analysis.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 3] Gap analysis complete")
    print(f"  - Total gaps: {output['summary']['total_gaps']}")
    print(f"  - High severity: {output['summary']['high_severity']}")
    print(f"  - Requires Protocol 0: {output['summary']['requires_protocol_0']}")
    
    if output['summary']['requires_protocol_0']:
        print(f"[WARNING] Protocol 0 generation may be required to fill gaps")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
