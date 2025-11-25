#!/usr/bin/env python3
"""
Validate Artifact Completeness
Validates that all required artifacts from prerequisite protocols exist.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

# Required artifacts per protocol
PROTOCOL_REQUIREMENTS = {
    "03": {
        "name": "Project Brief Creation",
        "required_artifacts": [
            "PROJECT-BRIEF.md",
            "project-brief-validation-report.json",
            "BRIEF-APPROVAL-RECORD.json"
        ],
        "optional_artifacts": [
            "technical-baseline.json",
            "context-summary.md"
        ]
    },
    "04": {
        "name": "Project Bootstrap",
        "required_artifacts": [
            "bootstrap-manifest.json",
            "context-kit.json"
        ],
        "optional_artifacts": [
            "architecture-principles.md",
            "tooling-config.json"
        ]
    },
    "05": {
        "name": "Context Engineering",
        "required_artifacts": [
            "architecture-principles.md"
        ],
        "optional_artifacts": [
            "codebase-analysis.json",
            "stack-detection.json"
        ]
    }
}

def check_artifact_exists(workspace: Path, protocol_id: str, artifact_name: str) -> dict:
    """Check if artifact exists in various locations."""
    locations_checked = []
    
    # Check workspace root
    root_path = workspace / artifact_name
    locations_checked.append(str(root_path))
    if root_path.exists():
        return {
            "artifact": artifact_name,
            "exists": True,
            "location": str(root_path),
            "size_bytes": root_path.stat().st_size
        }
    
    # Check .artifacts/protocol-{id}/
    artifacts_path = workspace / '.artifacts' / f'protocol-{protocol_id}' / artifact_name
    locations_checked.append(str(artifacts_path))
    if artifacts_path.exists():
        return {
            "artifact": artifact_name,
            "exists": True,
            "location": str(artifacts_path),
            "size_bytes": artifacts_path.stat().st_size
        }
    
    # Check .artifacts/protocol-{id} updated/
    updated_path = workspace / '.artifacts' / f'protocol-{protocol_id} updated' / artifact_name
    locations_checked.append(str(updated_path))
    if updated_path.exists():
        return {
            "artifact": artifact_name,
            "exists": True,
            "location": str(updated_path),
            "size_bytes": updated_path.stat().st_size
        }
    
    return {
        "artifact": artifact_name,
        "exists": False,
        "locations_checked": locations_checked
    }

def validate_protocol_artifacts(workspace: Path, protocol_id: str) -> dict:
    """Validate artifacts for a specific protocol."""
    if protocol_id not in PROTOCOL_REQUIREMENTS:
        return {
            "protocol": protocol_id,
            "status": "unknown",
            "message": f"No requirements defined for protocol {protocol_id}"
        }
    
    requirements = PROTOCOL_REQUIREMENTS[protocol_id]
    results = {
        "protocol": protocol_id,
        "protocol_name": requirements['name'],
        "required": [],
        "optional": [],
        "required_missing": [],
        "status": "pass"
    }
    
    # Check required artifacts
    for artifact in requirements['required_artifacts']:
        check = check_artifact_exists(workspace, protocol_id, artifact)
        results['required'].append(check)
        if not check['exists']:
            results['required_missing'].append(artifact)
            results['status'] = "fail"
    
    # Check optional artifacts
    for artifact in requirements.get('optional_artifacts', []):
        check = check_artifact_exists(workspace, protocol_id, artifact)
        results['optional'].append(check)
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Validate artifact completeness')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    parser.add_argument('--protocols', default='03,04,05', help='Comma-separated protocol IDs to validate')
    parser.add_argument('--output', help='Output JSON file path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    protocols = [p.strip() for p in args.protocols.split(',')]
    
    print(f"[PROTOCOL 05B | PHASE 1] Validating artifact completeness...")
    
    validation_results = {
        "timestamp": datetime.now().isoformat(),
        "workspace": str(workspace),
        "protocols_validated": protocols,
        "results": [],
        "overall_status": "pass"
    }
    
    for protocol_id in protocols:
        result = validate_protocol_artifacts(workspace, protocol_id)
        validation_results['results'].append(result)
        if result['status'] == 'fail':
            validation_results['overall_status'] = 'fail'
    
    # Summary
    total_required = sum(len(r.get('required', [])) for r in validation_results['results'])
    total_found = sum(len([a for a in r.get('required', []) if a.get('exists')]) for r in validation_results['results'])
    total_missing = sum(len(r.get('required_missing', [])) for r in validation_results['results'])
    
    validation_results['summary'] = {
        "total_required_artifacts": total_required,
        "total_found": total_found,
        "total_missing": total_missing,
        "completeness_percentage": round((total_found / total_required * 100) if total_required > 0 else 100, 2)
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'artifact-completeness-validation.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(validation_results, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 1] Validation complete, output: {output_path}")
    print(f"  - Overall status: {validation_results['overall_status'].upper()}")
    print(f"  - Completeness: {validation_results['summary']['completeness_percentage']}%")
    
    if validation_results['overall_status'] == 'fail':
        print(f"  - Missing artifacts:")
        for result in validation_results['results']:
            for missing in result.get('required_missing', []):
                print(f"    - Protocol {result['protocol']}: {missing}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
