#!/usr/bin/env python3
"""
Inventory Artifacts
Scans workspace and catalogs all existing artifacts from previous protocols.
"""
import argparse
import json
import sys
import hashlib
from pathlib import Path
from datetime import datetime

def calculate_file_hash(file_path: Path) -> str:
    """Calculate SHA-256 hash of file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return "error"

def scan_artifacts_directory(artifacts_dir: Path) -> dict:
    """Scan .artifacts directory and catalog contents."""
    inventory = {
        "protocols": {},
        "total_files": 0,
        "total_size_bytes": 0
    }
    
    if not artifacts_dir.exists():
        return inventory
    
    for protocol_dir in artifacts_dir.iterdir():
        if protocol_dir.is_dir() and protocol_dir.name.startswith('protocol-'):
            protocol_id = protocol_dir.name.replace('protocol-', '')
            protocol_artifacts = []
            
            for artifact in protocol_dir.rglob('*'):
                if artifact.is_file():
                    file_info = {
                        "name": artifact.name,
                        "path": str(artifact.relative_to(artifacts_dir)),
                        "size_bytes": artifact.stat().st_size,
                        "modified": datetime.fromtimestamp(artifact.stat().st_mtime).isoformat(),
                        "type": artifact.suffix.lstrip('.') or 'unknown'
                    }
                    protocol_artifacts.append(file_info)
                    inventory['total_files'] += 1
                    inventory['total_size_bytes'] += file_info['size_bytes']
            
            inventory['protocols'][protocol_id] = {
                "artifact_count": len(protocol_artifacts),
                "artifacts": protocol_artifacts
            }
    
    return inventory

def scan_workspace_artifacts(workspace: Path) -> dict:
    """Scan workspace root for key artifacts."""
    root_artifacts = []
    
    key_files = [
        'PROJECT-BRIEF.md',
        'architecture-principles.md',
        'bootstrap-manifest.json',
        'PROTOCOL-EXECUTION-PLAN.md',
        'PROTOCOL-CHECKLIST.md'
    ]
    
    for filename in key_files:
        file_path = workspace / filename
        if file_path.exists():
            root_artifacts.append({
                "name": filename,
                "path": filename,
                "size_bytes": file_path.stat().st_size,
                "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                "exists": True
            })
        else:
            root_artifacts.append({
                "name": filename,
                "path": filename,
                "exists": False
            })
    
    return root_artifacts

def main():
    parser = argparse.ArgumentParser(description='Inventory all artifacts in workspace')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--include-hashes', action='store_true', help='Include file hashes')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    artifacts_dir = workspace / '.artifacts'
    
    print(f"[PROTOCOL 05B | PHASE 1] Inventorying artifacts...")
    
    # Scan .artifacts directory
    artifact_inventory = scan_artifacts_directory(artifacts_dir)
    
    # Scan workspace root
    root_artifacts = scan_workspace_artifacts(workspace)
    
    # Build complete inventory
    inventory = {
        "timestamp": datetime.now().isoformat(),
        "workspace": str(workspace),
        "root_artifacts": root_artifacts,
        "protocol_artifacts": artifact_inventory['protocols'],
        "summary": {
            "total_protocols_with_artifacts": len(artifact_inventory['protocols']),
            "total_artifact_files": artifact_inventory['total_files'],
            "total_size_bytes": artifact_inventory['total_size_bytes'],
            "root_artifacts_found": sum(1 for a in root_artifacts if a.get('exists', False))
        }
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'artifact-inventory.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 1] Artifact inventory complete, output: {output_path}")
    print(f"  - Protocols with artifacts: {inventory['summary']['total_protocols_with_artifacts']}")
    print(f"  - Total artifact files: {inventory['summary']['total_artifact_files']}")
    print(f"  - Root artifacts found: {inventory['summary']['root_artifacts_found']}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
