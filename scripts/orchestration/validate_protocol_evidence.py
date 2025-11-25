#!/usr/bin/env python3
"""
Validate Protocol Evidence
Validates that all required artifacts from Protocol 05 exist and are valid.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def validate_file_exists(file_path: Path) -> tuple[bool, str]:
    """Check if file exists and is readable."""
    if not file_path.exists():
        return False, f"File not found: {file_path}"
    if not file_path.is_file():
        return False, f"Path is not a file: {file_path}"
    if not file_path.stat().st_size > 0:
        return False, f"File is empty: {file_path}"
    return True, "File exists and is readable"

def validate_json_file(file_path: Path) -> tuple[bool, str, dict]:
    """Validate JSON file format and return parsed data."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return True, "Valid JSON format", data
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {str(e)}", {}
    except Exception as e:
        return False, f"Error reading file: {str(e)}", {}

def validate_markdown_file(file_path: Path) -> tuple[bool, str]:
    """Basic markdown file validation."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if len(content.strip()) == 0:
            return False, "Markdown file is empty"
        # Check for basic markdown structure
        if not any(marker in content for marker in ['#', '*', '-', '`']):
            return False, "File appears to have no markdown content"
        return True, "Valid markdown format"
    except Exception as e:
        return False, f"Error reading file: {str(e)}"

def validate_bootstrap_manifest(data: dict) -> tuple[bool, list]:
    """Validate bootstrap-manifest.json structure."""
    errors = []
    required_fields = ['project_type', 'scaffold_structure', 'tooling_config', 'timestamp']
    
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    
    if 'project_type' in data and not isinstance(data['project_type'], str):
        errors.append("project_type must be a string")
    
    if 'timestamp' in data:
        try:
            datetime.fromisoformat(data['timestamp'].replace('Z', '+00:00'))
        except (ValueError, AttributeError):
            errors.append("timestamp must be valid ISO 8601 format")
    
    return len(errors) == 0, errors

def validate_architecture_principles(content: str) -> tuple[bool, list]:
    """Validate architecture-principles.md has required sections."""
    errors = []
    required_sections = [
        'System Architecture',
        'Technical Constraints',
        'Integration Requirements',
        'Infrastructure Requirements'
    ]
    
    content_lower = content.lower()
    for section in required_sections:
        # Check for section header (markdown format)
        if section.lower() not in content_lower:
            # Also check for common variations
            variations = [
                section.lower().replace(' ', '-'),
                section.lower().replace(' ', '_'),
                section.lower()
            ]
            if not any(var in content_lower for var in variations):
                errors.append(f"Missing required section: {section}")
    
    return len(errors) == 0, errors

def main():
    parser = argparse.ArgumentParser(description='Validate Protocol 05 evidence artifacts')
    parser.add_argument('--protocol', default='05', help='Protocol ID to validate (default: 05)')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    protocol_id = args.protocol
    
    print(f"[PROTOCOL 05B | STEP 1.1] Validating Protocol {protocol_id} completion...")
    
    checks = []
    all_passed = True
    
    # Check bootstrap-manifest.json
    manifest_paths = [
        workspace / 'bootstrap-manifest.json',
        workspace / '.artifacts' / f'protocol-{protocol_id}' / 'bootstrap-manifest.json'
    ]
    
    manifest_found = False
    manifest_data = {}
    
    for manifest_path in manifest_paths:
        exists, msg = validate_file_exists(manifest_path)
        if exists:
            manifest_found = True
            valid_json, json_msg, data = validate_json_file(manifest_path)
            if valid_json:
                manifest_data = data
                valid_structure, structure_errors = validate_bootstrap_manifest(data)
                checks.append({
                    "check": "bootstrap-manifest.json exists",
                    "status": "pass",
                    "path": str(manifest_path)
                })
                checks.append({
                    "check": "bootstrap-manifest.json valid JSON",
                    "status": "pass" if valid_json else "fail",
                    "message": json_msg
                })
                checks.append({
                    "check": "bootstrap-manifest.json structure",
                    "status": "pass" if valid_structure else "fail",
                    "errors": structure_errors if not valid_structure else []
                })
                if not valid_json or not valid_structure:
                    all_passed = False
            else:
                checks.append({
                    "check": "bootstrap-manifest.json",
                    "status": "fail",
                    "message": json_msg
                })
                all_passed = False
            break
    
    if not manifest_found:
        checks.append({
            "check": "bootstrap-manifest.json exists",
            "status": "fail",
            "message": "File not found in workspace root or .artifacts/protocol-05/"
        })
        all_passed = False
    
    # Check architecture-principles.md
    arch_paths = [
        workspace / 'architecture-principles.md',
        workspace / '.artifacts' / f'protocol-{protocol_id}' / 'architecture-principles.md'
    ]
    
    arch_found = False
    
    for arch_path in arch_paths:
        exists, msg = validate_file_exists(arch_path)
        if exists:
            arch_found = True
            valid_md, md_msg = validate_markdown_file(arch_path)
            if valid_md:
                with open(arch_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                valid_sections, section_errors = validate_architecture_principles(content)
                checks.append({
                    "check": "architecture-principles.md exists",
                    "status": "pass",
                    "path": str(arch_path)
                })
                checks.append({
                    "check": "architecture-principles.md valid markdown",
                    "status": "pass" if valid_md else "fail",
                    "message": md_msg
                })
                checks.append({
                    "check": "architecture-principles.md required sections",
                    "status": "pass" if valid_sections else "fail",
                    "errors": section_errors if not valid_sections else []
                })
                if not valid_md or not valid_sections:
                    all_passed = False
            else:
                checks.append({
                    "check": "architecture-principles.md",
                    "status": "fail",
                    "message": md_msg
                })
                all_passed = False
            break
    
    if not arch_found:
        checks.append({
            "check": "architecture-principles.md exists",
            "status": "fail",
            "message": "File not found in workspace root or .artifacts/protocol-05/"
        })
        all_passed = False
    
    # Prepare result
    result = {
        "status": "pass" if all_passed else "fail",
        "protocol": protocol_id,
        "workspace": str(workspace),
        "timestamp": datetime.now().isoformat(),
        "checks_passed": sum(1 for c in checks if c.get("status") == "pass"),
        "checks_total": len(checks),
        "checks": checks
    }
    
    # Write evidence artifact
    output_dir = workspace / '.artifacts' / 'protocol-05b'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / 'phase-00-preflight-check.json'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    
    print(json.dumps(result, indent=2))
    
    if all_passed:
        print("[PROTOCOL 05B | STEP 1.1 COMPLETE] All artifacts validated")
        return 0
    else:
        print("[PROTOCOL 05B | STEP 1.1 FAILED] Some validation checks failed")
        print("[ERROR] Missing or invalid artifacts - return to Protocol 05")
        return 1

if __name__ == "__main__":
    sys.exit(main())
