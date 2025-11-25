#!/usr/bin/env python3
"""
Parse bootstrap-manifest.json and extract bootstrap context.
Extracts project type, scaffold structure, tooling config, and other bootstrap information.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def validate_manifest_structure(data: dict) -> tuple[bool, list]:
    """Validate bootstrap manifest has required fields."""
    errors = []
    required_fields = ['project_type', 'scaffold_structure', 'tooling_config']
    
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    
    return len(errors) == 0, errors

def extract_project_type(data: dict) -> str:
    """Extract project type from manifest."""
    return data.get('project_type', 'unknown')

def extract_scaffold_structure(data: dict) -> dict:
    """Extract scaffold structure information."""
    scaffold = data.get('scaffold_structure', {})
    return {
        "directories": scaffold.get('directories', []),
        "files": scaffold.get('files', []),
        "template_used": scaffold.get('template', 'default')
    }

def extract_tooling_config(data: dict) -> dict:
    """Extract tooling configuration."""
    tooling = data.get('tooling_config', {})
    return {
        "package_manager": tooling.get('package_manager', 'npm'),
        "linter": tooling.get('linter'),
        "formatter": tooling.get('formatter'),
        "test_framework": tooling.get('test_framework'),
        "build_tool": tooling.get('build_tool')
    }

def extract_environment_config(data: dict) -> dict:
    """Extract environment configuration."""
    env = data.get('environment', {})
    return {
        "node_version": env.get('node_version'),
        "python_version": env.get('python_version'),
        "runtime": env.get('runtime'),
        "env_vars_required": env.get('env_vars', [])
    }

def main():
    parser = argparse.ArgumentParser(description='Parse bootstrap-manifest.json')
    parser.add_argument('--input', default='bootstrap-manifest.json', help='Input manifest file')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    input_path = workspace / args.input
    
    # Also check .artifacts location
    if not input_path.exists():
        alt_path = workspace / '.artifacts' / 'protocol-05' / 'bootstrap-manifest.json'
        if alt_path.exists():
            input_path = alt_path
    
    if not input_path.exists():
        print(f"[WARNING] bootstrap-manifest.json not found: {input_path}")
        parsed_data = {
            "status": "not_found",
            "project_type": "unknown",
            "scaffold_structure": {},
            "tooling_config": {},
            "environment_config": {},
            "validation_errors": ["File not found"]
        }
    else:
        print(f"[PROTOCOL 05B | PHASE 1] Parsing bootstrap-manifest.json...")
        
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[ERROR] Invalid JSON: {e}")
            parsed_data = {
                "status": "error",
                "validation_errors": [f"Invalid JSON: {str(e)}"]
            }
            if args.output:
                output_path = Path(args.output)
            else:
                output_path = workspace / '.artifacts' / 'protocol-05b' / 'bootstrap-manifest-parsed.json'
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(parsed_data, f, indent=2)
            return 1
        
        valid, errors = validate_manifest_structure(data)
        
        parsed_data = {
            "status": "parsed" if valid else "incomplete",
            "project_type": extract_project_type(data),
            "scaffold_structure": extract_scaffold_structure(data),
            "tooling_config": extract_tooling_config(data),
            "environment_config": extract_environment_config(data),
            "validation_errors": errors if not valid else [],
            "raw_fields": list(data.keys())
        }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'bootstrap-manifest-parsed.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(parsed_data, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 1] Bootstrap manifest parsed, output: {output_path}")
    print(json.dumps(parsed_data, indent=2))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
