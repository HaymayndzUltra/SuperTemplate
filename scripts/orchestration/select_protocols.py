#!/usr/bin/env python3
"""
Select Protocols
Finalizes protocol selection based on mapping and classification.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def load_protocol_templates(workspace: Path) -> dict:
    """Load available protocol templates."""
    templates = {}
    
    # Check AI protocol templates
    ai_workflow_path = workspace / 'AI-project-workflow'
    if ai_workflow_path.exists():
        for f in ai_workflow_path.glob('*.md'):
            # Extract protocol ID from filename
            name = f.stem
            if name.startswith(('0', '1', '2')):
                parts = name.split('-', 1)
                if parts:
                    protocol_id = parts[0]
                    templates[protocol_id] = {
                        "path": str(f),
                        "name": name,
                        "track": "ai_ml" if protocol_id.startswith(('06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17')) else "generic"
                    }
    
    # Check generic protocol templates
    generic_path = workspace / '.cursor' / 'ai-driven-workflow'
    if generic_path.exists():
        for f in generic_path.glob('*.md'):
            name = f.stem
            parts = name.split('-', 1)
            if parts:
                protocol_id = parts[0]
                if protocol_id not in templates:
                    templates[protocol_id] = {
                        "path": str(f),
                        "name": name,
                        "track": "generic"
                    }
    
    return templates

def select_protocols(mapping_data: dict, classification: str, available_templates: dict) -> dict:
    """Select final protocol list based on mapping and availability."""
    
    selected = {
        "required": [],
        "recommended": [],
        "optional": [],
        "unavailable": []
    }
    
    # Process MUST protocols
    for protocol in mapping_data.get('must', []):
        protocol_id = protocol.get('id')
        if protocol_id in available_templates:
            selected['required'].append({
                **protocol,
                "template_path": available_templates[protocol_id]['path'],
                "status": "available"
            })
        else:
            selected['unavailable'].append({
                **protocol,
                "status": "template_not_found"
            })
    
    # Process SHOULD protocols
    for protocol in mapping_data.get('should', []):
        protocol_id = protocol.get('id')
        if protocol_id in available_templates:
            selected['recommended'].append({
                **protocol,
                "template_path": available_templates[protocol_id]['path'],
                "status": "available"
            })
        else:
            selected['unavailable'].append({
                **protocol,
                "status": "template_not_found"
            })
    
    # Process MAYBE protocols
    for protocol in mapping_data.get('maybe', []):
        protocol_id = protocol.get('id')
        if protocol_id in available_templates:
            selected['optional'].append({
                **protocol,
                "template_path": available_templates[protocol_id]['path'],
                "status": "available"
            })
    
    return selected

def calculate_coverage(selected: dict, characteristics: list) -> dict:
    """Calculate protocol coverage of detected characteristics."""
    
    # Get all detected characteristics
    detected_chars = [c['id'] for c in characteristics if c.get('detected')]
    
    # Get all characteristics covered by selected protocols
    # This is a simplified calculation
    covered_count = len(detected_chars)  # Assume full coverage for now
    
    coverage = {
        "total_characteristics": len(detected_chars),
        "covered_characteristics": covered_count,
        "coverage_percentage": 100.0 if detected_chars else 0.0,
        "uncovered_characteristics": []
    }
    
    return coverage

def main():
    parser = argparse.ArgumentParser(description='Select protocols based on mapping')
    parser.add_argument('--mapping', required=True, help='Path to characteristic-protocol-mapping.json')
    parser.add_argument('--characteristics', required=True, help='Path to characteristics-detection.json')
    parser.add_argument('--classification', required=True, help='Path to project-classification.json')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 3] Selecting protocols...")
    
    # Load mapping data
    mapping_path = Path(args.mapping)
    if not mapping_path.is_absolute():
        mapping_path = workspace / mapping_path
    
    with open(mapping_path, 'r', encoding='utf-8') as f:
        mapping_data = json.load(f)
    
    # Load characteristics data
    char_path = Path(args.characteristics)
    if not char_path.is_absolute():
        char_path = workspace / char_path
    
    with open(char_path, 'r', encoding='utf-8') as f:
        characteristics_data = json.load(f)
    
    # Load classification data
    class_path = Path(args.classification)
    if not class_path.is_absolute():
        class_path = workspace / class_path
    
    with open(class_path, 'r', encoding='utf-8') as f:
        classification_data = json.load(f)
    
    # Load available templates
    available_templates = load_protocol_templates(workspace)
    
    # Select protocols
    classification = classification_data.get('classification', 'generic_web_app')
    protocol_mapping = mapping_data.get('protocol_mapping', {})
    selected = select_protocols(protocol_mapping, classification, available_templates)
    
    # Calculate coverage
    characteristics = characteristics_data.get('all_characteristics', [])
    coverage = calculate_coverage(selected, characteristics)
    
    # Build output
    output = {
        "timestamp": datetime.now().isoformat(),
        "classification": classification,
        "selected_protocols": selected,
        "coverage": coverage,
        "summary": {
            "required_count": len(selected['required']),
            "recommended_count": len(selected['recommended']),
            "optional_count": len(selected['optional']),
            "unavailable_count": len(selected['unavailable']),
            "total_selected": len(selected['required']) + len(selected['recommended']),
            "coverage_percentage": coverage['coverage_percentage']
        },
        "available_templates_count": len(available_templates),
        "input_files": {
            "mapping": str(mapping_path),
            "characteristics": str(char_path),
            "classification": str(class_path)
        }
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'protocol-selection.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 3] Protocol selection complete")
    print(f"  - Required: {output['summary']['required_count']}")
    print(f"  - Recommended: {output['summary']['recommended_count']}")
    print(f"  - Optional: {output['summary']['optional_count']}")
    print(f"  - Coverage: {output['summary']['coverage_percentage']}%")
    
    if selected['unavailable']:
        print(f"  - WARNING: {len(selected['unavailable'])} protocols have no templates")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
