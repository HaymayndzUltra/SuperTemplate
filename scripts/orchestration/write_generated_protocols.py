#!/usr/bin/env python3
"""
Write Generated Protocols

Writes transformed protocol instances to .cursor/project-protocols/ directory
and creates generation manifest for tracking and audit.

Usage:
    python scripts/orchestration/write_generated_protocols.py \
        --transformed .artifacts/protocol-05b/transformed-protocols.json \
        --output-dir .cursor/project-protocols \
        --manifest .cursor/project-protocols/.protocol-manifest.json
"""

import argparse
import json
import sys
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List

# Add project root to path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Write generated protocols to disk")
    parser.add_argument(
        "--transformed",
        required=True,
        help="Path to transformed-protocols.json"
    )
    parser.add_argument(
        "--output-dir",
        default=".cursor/project-protocols",
        help="Output directory for generated protocols"
    )
    parser.add_argument(
        "--manifest",
        help="Path to generation manifest file (default: <output-dir>/.protocol-manifest.json)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing protocol files"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    return parser.parse_args()


def calculate_checksum(content: str) -> str:
    """Calculate SHA-256 checksum of content."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def generate_protocol_filename(protocol_id: str, project_name: str) -> str:
    """Generate filename for protocol instance."""
    # Extract protocol name from ID (e.g., "06" -> "create-prd")
    protocol_names = {
        "06": "create-prd",
        "07": "technical-design",
        "08": "task-generation",
        "09": "environment-setup",
        "10": "execute-tasks",
        "11": "integration-testing",
        "12": "quality-audit",
        "13": "uat-coordination",
        "14": "pre-deployment",
        "15": "production-deployment",
        "16": "monitoring-observability",
        "17": "incident-response",
        "18": "performance-optimization"
    }
    
    protocol_name = protocol_names.get(protocol_id, f"protocol-{protocol_id}")
    return f"{protocol_id}-{protocol_name}-{project_name}.md"


def write_protocol_file(
    protocol_data: Dict,
    output_dir: Path,
    project_name: str,
    force: bool,
    verbose: bool
) -> Dict:
    """Write a single protocol file to disk."""
    protocol_id = protocol_data["protocol_id"]
    content = protocol_data["transformed_content"]
    
    # Generate filename
    filename = generate_protocol_filename(protocol_id, project_name)
    output_path = output_dir / filename
    
    # Check if file exists
    if output_path.exists() and not force:
        print(f"[WARN] File exists, skipping: {output_path}", file=sys.stderr)
        return None
    
    # Write file
    try:
        output_path.write_text(content, encoding='utf-8')
        
        if verbose:
            print(f"[INFO] Written: {output_path}")
        
        # Calculate checksum
        checksum = calculate_checksum(content)
        
        return {
            "protocol_id": protocol_id,
            "filename": filename,
            "path": str(output_path),
            "size_bytes": len(content),
            "line_count": len(content.split('\n')),
            "checksum_sha256": checksum,
            "source_template": protocol_data.get("source_template", "unknown"),
            "customizations_applied": protocol_data.get("customizations_applied", 0)
        }
    except Exception as e:
        print(f"[ERROR] Failed to write {output_path}: {e}", file=sys.stderr)
        return None


def create_readme(output_dir: Path, project_info: Dict, protocols_written: List[Dict]) -> None:
    """Create README.md in output directory."""
    project_name = project_info.get("project_name", "unknown-project")
    tech_stack = project_info.get("tech_stack", {})
    
    readme_content = f"""# Project-Specific Protocols: {project_name.replace('-', ' ').title()}

**Generated**: {datetime.utcnow().isoformat()}Z  
**Project**: {project_name}  
**Protocols**: {len(protocols_written)}

## Overview

This directory contains customized protocol instances generated specifically for the **{project_name}** project. These protocols are derived from foundation templates in `.cursor/ai-driven-workflow/` with project-specific customizations applied.

## Tech Stack

- **Frontend**: {tech_stack.get('frontend', 'Not specified')}
- **Backend**: {tech_stack.get('backend', 'Not specified')}
- **Database**: {tech_stack.get('database', 'Not specified')}

## Protocols Generated

"""
    
    for protocol in sorted(protocols_written, key=lambda p: p["protocol_id"]):
        readme_content += f"- **Protocol {protocol['protocol_id']}**: `{protocol['filename']}`\n"
    
    readme_content += f"""
## Usage

Execute protocols in the order specified in `PROTOCOL-EXECUTION-PLAN.md`. Each protocol file contains:
- Project-specific workflow steps
- Customized validation gates
- Tech stack-specific automation scripts
- Project-specific artifact paths

## Customizations Applied

Total customizations: {sum(p.get('customizations_applied', 0) for p in protocols_written)}

## Regeneration

To regenerate protocols (e.g., after foundation template updates):

```bash
python scripts/orchestration/regenerate_protocols.py \\
  --project-root . \\
  --force
```

## Maintenance

- **DO NOT** manually edit generated protocols (changes will be lost on regeneration)
- **DO** update foundation templates in `.cursor/ai-driven-workflow/` and regenerate
- **DO** update PROJECT-BRIEF.md if project requirements change, then regenerate

## Manifest

See `.protocol-manifest.json` for complete generation details and traceability.
"""
    
    readme_path = output_dir / "README.md"
    readme_path.write_text(readme_content, encoding='utf-8')


def create_manifest(
    output_dir: Path,
    project_info: Dict,
    protocols_written: List[Dict],
    transformed_data: Dict
) -> Dict:
    """Create generation manifest."""
    manifest = {
        "generation_timestamp": datetime.utcnow().isoformat() + "Z",
        "project_name": project_info.get("project_name", "unknown-project"),
        "project_type": "Web Application",  # TODO: Extract from brief
        "foundation_version": "1.0.0",
        "transformation_engine_version": "1.0.0",
        "protocols_generated": protocols_written,
        "total_protocols": len(protocols_written),
        "total_customizations": transformed_data.get("total_customizations", 0),
        "total_size_bytes": sum(p["size_bytes"] for p in protocols_written),
        "total_lines": sum(p["line_count"] for p in protocols_written),
        "project_info": project_info
    }
    
    return manifest


def main() -> int:
    args = parse_args()
    
    # Resolve paths
    transformed_path = ROOT / args.transformed
    output_dir = ROOT / args.output_dir
    
    if args.manifest:
        manifest_path = ROOT / args.manifest
    else:
        manifest_path = output_dir / ".protocol-manifest.json"
    
    # Validate inputs
    if not transformed_path.exists():
        print(f"[ERROR] Transformed protocols file not found: {transformed_path}", file=sys.stderr)
        return 1
    
    # Load transformed protocols
    if args.verbose:
        print(f"[INFO] Loading transformed protocols from: {transformed_path}")
    
    transformed_data = json.loads(transformed_path.read_text(encoding='utf-8'))
    protocols = transformed_data.get("protocols", [])
    project_info = transformed_data.get("project_info", {})
    
    if not protocols:
        print("[ERROR] No protocols found in input file", file=sys.stderr)
        return 1
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if args.verbose:
        print(f"[INFO] Output directory: {output_dir}")
        print(f"[INFO] Writing {len(protocols)} protocol files")
    
    # Write protocol files
    protocols_written = []
    project_name = project_info.get("project_name", "unknown-project")
    
    for protocol_data in protocols:
        result = write_protocol_file(
            protocol_data,
            output_dir,
            project_name,
            args.force,
            args.verbose
        )
        
        if result:
            protocols_written.append(result)
    
    if not protocols_written:
        print("[ERROR] No protocols were written", file=sys.stderr)
        return 1
    
    # Create README
    if args.verbose:
        print(f"[INFO] Creating README.md")
    
    create_readme(output_dir, project_info, protocols_written)
    
    # Create manifest
    if args.verbose:
        print(f"[INFO] Creating generation manifest")
    
    manifest = create_manifest(output_dir, project_info, protocols_written, transformed_data)
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    
    # Summary
    print(f"[OK] Written {len(protocols_written)} protocol files to {output_dir}")
    print(f"[OK] Generation manifest: {manifest_path}")
    
    if args.verbose:
        total_size_kb = sum(p["size_bytes"] for p in protocols_written) / 1024
        print(f"[INFO] Total size: {total_size_kb:.2f} KB")
        print(f"[INFO] Total customizations: {transformed_data.get('total_customizations', 0)}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
