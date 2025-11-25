#!/usr/bin/env python3
"""
Prepare Protocol 0 Inputs
Validates and prepares inputs for Protocol 0 gap-fill generation.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime
import jsonschema

def load_schema(workspace: Path) -> dict:
    """Load gap-specification schema."""
    schema_path = workspace / 'config' / 'schemas' / 'gap-specification.schema.json'
    if schema_path.exists():
        with open(schema_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def validate_gap_spec(gap_spec: dict, schema: dict) -> tuple[bool, list]:
    """Validate gap specification against schema."""
    errors = []
    
    if schema:
        try:
            jsonschema.validate(gap_spec, schema)
        except jsonschema.ValidationError as e:
            errors.append(f"Schema validation error: {e.message}")
        except jsonschema.SchemaError as e:
            errors.append(f"Schema error: {e.message}")
    
    # Additional validation
    if not gap_spec.get('gap_id'):
        errors.append("Missing required field: gap_id")
    
    if not gap_spec.get('gap_name'):
        errors.append("Missing required field: gap_name")
    
    if not gap_spec.get('gap_description') or len(gap_spec.get('gap_description', '')) < 20:
        errors.append("gap_description must be at least 20 characters")
    
    if not gap_spec.get('workflow_steps') or len(gap_spec.get('workflow_steps', [])) < 1:
        errors.append("At least one workflow step is required")
    
    # Validate workflow steps
    for i, step in enumerate(gap_spec.get('workflow_steps', [])):
        if not step.get('name'):
            errors.append(f"Workflow step {i+1} missing name")
        if not step.get('inputs'):
            errors.append(f"Workflow step {i+1} missing inputs")
        if not step.get('outputs'):
            errors.append(f"Workflow step {i+1} missing outputs")
    
    return len(errors) == 0, errors

def prepare_inputs(gap_spec: dict, workspace: Path) -> dict:
    """Prepare and enrich gap specification for generation."""
    
    prepared = gap_spec.copy()
    
    # Ensure required sections has minimum set
    min_sections = ['IDENTITY', 'AI_ROLE', 'PREREQUISITES', 'WORKFLOW', 'QUALITY_GATES', 'EVIDENCE_SUMMARY']
    current_sections = prepared.get('required_sections', [])
    for section in min_sections:
        if section not in current_sections:
            current_sections.append(section)
    prepared['required_sections'] = current_sections
    
    # Ensure quality gates exist
    if not prepared.get('quality_gates'):
        prepared['quality_gates'] = [
            {
                "gate_id": 0,
                "name": "Input Validation",
                "threshold": 1.0,
                "criteria": ["All required inputs present", "Input format valid"]
            },
            {
                "gate_id": 1,
                "name": "Output Validation",
                "threshold": 0.95,
                "criteria": ["All outputs generated", "Output format valid"]
            }
        ]
    
    # Set defaults
    prepared.setdefault('track', 'generic')
    prepared.setdefault('complexity', 'medium')
    prepared.setdefault('integration_points', {'input_from': [], 'output_to': []})
    prepared.setdefault('automation_hooks', [])
    
    return prepared

def main():
    parser = argparse.ArgumentParser(description='Prepare Protocol 0 inputs')
    parser.add_argument('--input', required=True, help='Path to gap-specification.json')
    parser.add_argument('--output', help='Output prepared specification path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 0] Preparing inputs for gap-fill generation...")
    
    # Load gap specification
    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = workspace / input_path
    
    with open(input_path, 'r', encoding='utf-8') as f:
        gap_spec = json.load(f)
    
    # Load schema
    schema = load_schema(workspace)
    
    # Validate
    valid, errors = validate_gap_spec(gap_spec, schema)
    
    if not valid:
        print(f"[PROTOCOL 0] Validation failed:")
        for error in errors:
            print(f"  - {error}")
        
        result = {
            "status": "validation_failed",
            "errors": errors,
            "timestamp": datetime.now().isoformat()
        }
        
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
        
        return 1
    
    # Prepare inputs
    prepared = prepare_inputs(gap_spec, workspace)
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'new-protocols' / 'prepared-gap-spec.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    result = {
        "status": "ready",
        "prepared_spec": prepared,
        "validation": {
            "valid": True,
            "errors": []
        },
        "enrichments": {
            "sections_added": len(prepared['required_sections']) - len(gap_spec.get('required_sections', [])),
            "defaults_applied": True
        },
        "timestamp": datetime.now().isoformat()
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    
    print(f"[PROTOCOL 0] Input preparation complete")
    print(f"  - Status: Ready for generation")
    print(f"  - Protocol ID: {prepared['gap_id']}")
    print(f"  - Workflow steps: {len(prepared['workflow_steps'])}")
    print(f"  - Quality gates: {len(prepared['quality_gates'])}")
    print(f"  - Output: {output_path}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
