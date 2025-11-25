#!/usr/bin/env python3
"""
Register New Protocol
Registers a newly generated protocol in the script registry.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def load_registry(workspace: Path) -> dict:
    """Load existing script registry."""
    registry_path = workspace / 'scripts' / 'script-registry.json'
    if registry_path.exists():
        with open(registry_path, 'r', encoding='utf-8') as f:
            registry = json.load(f)
            # Ensure protocols key exists
            if 'protocols' not in registry:
                registry['protocols'] = {}
            return registry
    return {"protocols": {}, "scripts": {}, "registry_version": "1.0.0"}

def save_registry(workspace: Path, registry: dict) -> None:
    """Save script registry."""
    registry_path = workspace / 'scripts' / 'script-registry.json'
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2)

def register_protocol(registry: dict, protocol_info: dict) -> dict:
    """Register a new protocol in the registry."""
    
    protocol_id = protocol_info['protocol_id']
    
    registry['protocols'][protocol_id] = {
        "id": protocol_id,
        "name": protocol_info['protocol_name'],
        "track": protocol_info.get('track', 'generic'),
        "path": protocol_info['protocol_path'],
        "generated": True,
        "generated_at": protocol_info.get('generated_at', datetime.now().isoformat()),
        "gap_spec": protocol_info.get('gap_spec_path'),
        "validation_score": protocol_info.get('validation_score'),
        "status": "active"
    }
    
    return registry

def main():
    parser = argparse.ArgumentParser(description='Register new protocol in registry')
    parser.add_argument('--protocol-id', required=True, help='Protocol ID')
    parser.add_argument('--protocol-name', required=True, help='Protocol name')
    parser.add_argument('--protocol-path', required=True, help='Path to protocol file')
    parser.add_argument('--track', default='generic', help='Protocol track')
    parser.add_argument('--gap-spec', help='Path to gap specification used')
    parser.add_argument('--validation-score', type=float, help='Validation score')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 0] Registering new protocol...")
    
    # Load registry
    registry = load_registry(workspace)
    
    # Check if protocol already exists
    if args.protocol_id in registry.get('protocols', {}):
        print(f"[WARNING] Protocol {args.protocol_id} already registered, updating...")
    
    # Register protocol
    protocol_info = {
        "protocol_id": args.protocol_id,
        "protocol_name": args.protocol_name,
        "protocol_path": args.protocol_path,
        "track": args.track,
        "gap_spec_path": args.gap_spec,
        "validation_score": args.validation_score,
        "generated_at": datetime.now().isoformat()
    }
    
    registry = register_protocol(registry, protocol_info)
    
    # Save registry
    save_registry(workspace, registry)
    
    print(f"[PROTOCOL 0] Protocol registered successfully")
    print(f"  - Protocol ID: {args.protocol_id}")
    print(f"  - Protocol Name: {args.protocol_name}")
    print(f"  - Track: {args.track}")
    print(f"  - Registry updated: scripts/script-registry.json")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
