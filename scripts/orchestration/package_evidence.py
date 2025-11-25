#!/usr/bin/env python3
"""
Package Evidence
Packages all Protocol 05b artifacts into a handoff package with manifest and checksums.
"""
import argparse
import json
import sys
import hashlib
import zipfile
from pathlib import Path
from datetime import datetime

def calculate_file_hash(file_path: Path) -> str:
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return "error"

def collect_artifacts(artifacts_dir: Path) -> list:
    """Collect all artifacts from the protocol-05b directory."""
    artifacts = []
    
    if not artifacts_dir.exists():
        return artifacts
    
    for file_path in artifacts_dir.rglob('*'):
        if file_path.is_file():
            artifacts.append({
                "name": file_path.name,
                "path": str(file_path.relative_to(artifacts_dir)),
                "full_path": str(file_path),
                "size_bytes": file_path.stat().st_size,
                "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                "hash": calculate_file_hash(file_path)
            })
    
    return artifacts

def generate_manifest(artifacts: list, workspace: Path) -> dict:
    """Generate evidence manifest."""
    
    manifest = {
        "manifest_version": "1.0.0",
        "protocol": "05b",
        "protocol_name": "Project Protocol Orchestration",
        "generated": datetime.now().isoformat(),
        "workspace": str(workspace),
        "artifacts": artifacts,
        "summary": {
            "total_artifacts": len(artifacts),
            "total_size_bytes": sum(a['size_bytes'] for a in artifacts),
            "artifact_types": {}
        },
        "integrity": {
            "hash_algorithm": "SHA-256",
            "verified": True
        }
    }
    
    # Count artifact types
    for artifact in artifacts:
        ext = Path(artifact['name']).suffix.lstrip('.') or 'unknown'
        if ext not in manifest['summary']['artifact_types']:
            manifest['summary']['artifact_types'][ext] = 0
        manifest['summary']['artifact_types'][ext] += 1
    
    return manifest

def generate_checksums(artifacts: list) -> str:
    """Generate checksums.sha256 content."""
    lines = []
    for artifact in sorted(artifacts, key=lambda x: x['path']):
        lines.append(f"{artifact['hash']}  {artifact['path']}")
    return '\n'.join(lines)

def create_handoff_package(artifacts_dir: Path, output_path: Path, manifest: dict) -> None:
    """Create ZIP handoff package."""
    
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add all artifacts
        for artifact in manifest['artifacts']:
            file_path = Path(artifact['full_path'])
            if file_path.exists():
                arcname = artifact['path']
                zf.write(file_path, arcname)
        
        # Add manifest
        manifest_json = json.dumps(manifest, indent=2)
        zf.writestr('evidence-manifest.json', manifest_json)
        
        # Add checksums
        checksums = generate_checksums(manifest['artifacts'])
        zf.writestr('checksums.sha256', checksums)

def main():
    parser = argparse.ArgumentParser(description='Package Protocol 05b evidence')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    parser.add_argument('--output', help='Output ZIP file path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    artifacts_dir = workspace / '.artifacts' / 'protocol-05b'
    
    print(f"[PROTOCOL 05B | PHASE 6] Packaging evidence...")
    
    # Collect artifacts
    artifacts = collect_artifacts(artifacts_dir)
    
    if not artifacts:
        print(f"[WARNING] No artifacts found in {artifacts_dir}")
    
    # Generate manifest
    manifest = generate_manifest(artifacts, workspace)
    
    # Write manifest to artifacts directory
    manifest_path = artifacts_dir / 'evidence-manifest.json'
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    
    # Write checksums to artifacts directory
    checksums = generate_checksums(artifacts)
    checksums_path = artifacts_dir / 'checksums.sha256'
    with open(checksums_path, 'w', encoding='utf-8') as f:
        f.write(checksums)
    
    # Re-collect to include manifest and checksums
    artifacts = collect_artifacts(artifacts_dir)
    manifest = generate_manifest(artifacts, workspace)
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = artifacts_dir / 'handoff-package.zip'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Create handoff package
    create_handoff_package(artifacts_dir, output_path, manifest)
    
    print(f"[PROTOCOL 05B | PHASE 6] Evidence packaging complete")
    print(f"  - Total artifacts: {manifest['summary']['total_artifacts']}")
    print(f"  - Total size: {manifest['summary']['total_size_bytes']} bytes")
    print(f"  - Manifest: {manifest_path}")
    print(f"  - Checksums: {checksums_path}")
    print(f"  - Package: {output_path}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
