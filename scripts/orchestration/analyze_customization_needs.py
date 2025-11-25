#!/usr/bin/env python3
"""
Analyze Customization Needs
Analyzes project-specific customization requirements for each protocol.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def analyze_customizations(sequence_data: dict, brief_data: dict, characteristics_data: dict) -> list:
    """Analyze customization needs for each protocol in sequence."""
    
    customizations = []
    
    sequence = sequence_data.get('sequence', [])
    tech_stack = brief_data.get('tech_stack', {})
    detected_chars = [c for c in characteristics_data.get('all_characteristics', []) if c.get('detected')]
    
    for protocol in sequence:
        protocol_id = protocol.get('protocol_id')
        protocol_name = protocol.get('protocol_name')
        
        custom = {
            "protocol_id": protocol_id,
            "protocol_name": protocol_name,
            "customizations": [],
            "tech_stack_adaptations": [],
            "skip_sections": [],
            "priority_sections": []
        }
        
        # Analyze based on tech stack
        frontend = tech_stack.get('frontend', [])
        backend = tech_stack.get('backend', [])
        ai_ml = tech_stack.get('ai_ml', [])
        
        # Protocol-specific customizations
        if protocol_id in ['04', '05']:  # Bootstrap/Context
            if frontend:
                custom['tech_stack_adaptations'].append({
                    "component": "frontend",
                    "frameworks": frontend,
                    "adaptation": "Configure frontend tooling and scaffolding"
                })
            if backend:
                custom['tech_stack_adaptations'].append({
                    "component": "backend",
                    "frameworks": backend,
                    "adaptation": "Configure backend environment and dependencies"
                })
        
        elif protocol_id in ['06', '07']:  # AI Use Case / Data Strategy
            if ai_ml:
                custom['priority_sections'].append("AI/ML framework configuration")
                custom['customizations'].append({
                    "type": "framework_specific",
                    "detail": f"Configure for {', '.join(ai_ml)}"
                })
        
        elif protocol_id in ['08', '09', '10', '11']:  # Data protocols
            # Check for vector DB
            vector_char = next((c for c in detected_chars if c.get('id') == 'database_vector'), None)
            if vector_char:
                custom['customizations'].append({
                    "type": "vector_db",
                    "detail": "Include vector database configuration for embeddings"
                })
        
        elif protocol_id in ['18', '19']:  # Performance / Documentation
            infra = tech_stack.get('infrastructure', [])
            if infra:
                custom['tech_stack_adaptations'].append({
                    "component": "infrastructure",
                    "platforms": infra,
                    "adaptation": f"Optimize for {', '.join(infra)}"
                })
        
        # Check compliance requirements
        compliance_chars = [c for c in detected_chars if c.get('category') == 'compliance']
        if compliance_chars:
            custom['priority_sections'].append("Compliance requirements")
            for comp in compliance_chars:
                custom['customizations'].append({
                    "type": "compliance",
                    "detail": f"Address {comp.get('name')}"
                })
        
        customizations.append(custom)
    
    return customizations

def main():
    parser = argparse.ArgumentParser(description='Analyze protocol customization needs')
    parser.add_argument('--sequence', required=True, help='Path to protocol-sequence.json')
    parser.add_argument('--brief', required=True, help='Path to project-brief-parsed.json')
    parser.add_argument('--characteristics', required=True, help='Path to characteristics-detection.json')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 5] Analyzing customization needs...")
    
    # Load sequence data
    sequence_path = Path(args.sequence)
    if not sequence_path.is_absolute():
        sequence_path = workspace / sequence_path
    
    with open(sequence_path, 'r', encoding='utf-8') as f:
        sequence_data = json.load(f)
    
    # Load brief data
    brief_path = Path(args.brief)
    if not brief_path.is_absolute():
        brief_path = workspace / brief_path
    
    with open(brief_path, 'r', encoding='utf-8') as f:
        brief_data = json.load(f)
    
    # Load characteristics data
    char_path = Path(args.characteristics)
    if not char_path.is_absolute():
        char_path = workspace / char_path
    
    with open(char_path, 'r', encoding='utf-8') as f:
        characteristics_data = json.load(f)
    
    # Analyze customizations
    customizations = analyze_customizations(sequence_data, brief_data, characteristics_data)
    
    # Calculate summary
    protocols_with_customizations = len([c for c in customizations if c.get('customizations')])
    total_customizations = sum(len(c.get('customizations', [])) for c in customizations)
    
    # Build output
    output = {
        "timestamp": datetime.now().isoformat(),
        "customizations": customizations,
        "summary": {
            "total_protocols": len(customizations),
            "protocols_with_customizations": protocols_with_customizations,
            "total_customization_items": total_customizations
        },
        "input_files": {
            "sequence": str(sequence_path),
            "brief": str(brief_path),
            "characteristics": str(char_path)
        }
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'customization-analysis.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 5] Customization analysis complete")
    print(f"  - Protocols analyzed: {output['summary']['total_protocols']}")
    print(f"  - With customizations: {output['summary']['protocols_with_customizations']}")
    print(f"  - Total customization items: {output['summary']['total_customization_items']}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
