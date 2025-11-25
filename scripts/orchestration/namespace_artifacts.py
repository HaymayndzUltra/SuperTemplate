#!/usr/bin/env python3
"""
Namespace Artifacts Module
Generates unique run IDs and namespaces artifact paths for parallel execution.
"""
import argparse
import json
import sys
import uuid
import os
from pathlib import Path
from datetime import datetime

def generate_run_id() -> str:
    """Generate a unique run ID."""
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    short_uuid = str(uuid.uuid4())[:8]
    return f"{timestamp}-{short_uuid}"

def get_namespaced_path(base_path: Path, run_id: str, protocol_id: str) -> Path:
    """Get namespaced artifact path."""
    return base_path / f"protocol-{protocol_id}" / run_id

def create_run_manifest(run_id: str, protocol_id: str, workspace: Path) -> dict:
    """Create a manifest for this run."""
    return {
        "run_id": run_id,
        "protocol_id": protocol_id,
        "workspace": str(workspace),
        "created_at": datetime.now().isoformat(),
        "pid": os.getpid(),
        "status": "initialized"
    }

def main():
    parser = argparse.ArgumentParser(description='Namespace artifacts for parallel execution')
    parser.add_argument('action', choices=['generate', 'create', 'status'],
                       help='Action to perform')
    parser.add_argument('--protocol', default='05b', help='Protocol ID')
    parser.add_argument('--run-id', help='Existing run ID (for status)')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    artifacts_base = workspace / '.artifacts'
    
    if args.action == 'generate':
        run_id = generate_run_id()
        print(f"[NAMESPACE] Generated run ID: {run_id}")
        
        # Output as JSON for scripting
        result = {
            "run_id": run_id,
            "protocol_id": args.protocol,
            "artifacts_path": str(get_namespaced_path(artifacts_base, run_id, args.protocol))
        }
        print(json.dumps(result, indent=2))
        return 0
    
    elif args.action == 'create':
        run_id = args.run_id or generate_run_id()
        namespaced_path = get_namespaced_path(artifacts_base, run_id, args.protocol)
        namespaced_path.mkdir(parents=True, exist_ok=True)
        
        # Create run manifest
        manifest = create_run_manifest(run_id, args.protocol, workspace)
        manifest_path = namespaced_path / 'run-manifest.json'
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"[NAMESPACE] Created namespaced artifacts directory")
        print(f"  - Run ID: {run_id}")
        print(f"  - Path: {namespaced_path}")
        print(f"  - Manifest: {manifest_path}")
        
        result = {
            "run_id": run_id,
            "protocol_id": args.protocol,
            "artifacts_path": str(namespaced_path),
            "manifest_path": str(manifest_path)
        }
        print(json.dumps(result, indent=2))
        return 0
    
    elif args.action == 'status':
        if not args.run_id:
            # List all runs
            runs = []
            protocol_path = artifacts_base / f"protocol-{args.protocol}"
            if protocol_path.exists():
                for run_dir in protocol_path.iterdir():
                    if run_dir.is_dir():
                        manifest_path = run_dir / 'run-manifest.json'
                        if manifest_path.exists():
                            with open(manifest_path, 'r', encoding='utf-8') as f:
                                manifest = json.load(f)
                                runs.append(manifest)
            
            print(json.dumps({"runs": runs}, indent=2))
        else:
            # Get specific run status
            namespaced_path = get_namespaced_path(artifacts_base, args.run_id, args.protocol)
            manifest_path = namespaced_path / 'run-manifest.json'
            
            if manifest_path.exists():
                with open(manifest_path, 'r', encoding='utf-8') as f:
                    manifest = json.load(f)
                
                # Count artifacts
                artifact_count = sum(1 for f in namespaced_path.rglob('*') if f.is_file())
                manifest["artifact_count"] = artifact_count
                
                print(json.dumps(manifest, indent=2))
            else:
                print(f"[ERROR] Run not found: {args.run_id}")
                return 1
        
        return 0
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

