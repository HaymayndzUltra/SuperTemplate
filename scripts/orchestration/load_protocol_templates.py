#!/usr/bin/env python3
"""
Load Protocol Templates

Loads foundation protocol templates from .cursor/ai-driven-workflow/
for transformation into project-specific instances.

Usage:
    python scripts/orchestration/load_protocol_templates.py \
        --protocol-ids 06,07,08,09,10,11,12,13,14,15 \
        --output .artifacts/protocol-05b/loaded-templates.json
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Add project root to path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Load protocol templates")
    parser.add_argument(
        "--protocol-ids",
        required=True,
        help="Comma-separated protocol IDs to load (e.g., 06,07,08)"
    )
    parser.add_argument(
        "--templates-dir",
        default=".cursor/ai-driven-workflow",
        help="Directory containing foundation templates"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output JSON file path"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    return parser.parse_args()


def find_template_file(protocol_id: str, templates_dir: Path) -> Optional[Path]:
    """Find template file for given protocol ID."""
    # Try common naming patterns
    patterns = [
        f"{protocol_id}-*.md",
        f"protocol-{protocol_id}-*.md",
        f"{protocol_id.lstrip('0')}-*.md",  # Try without leading zero
    ]
    
    for pattern in patterns:
        matches = list(templates_dir.glob(pattern))
        if matches:
            return matches[0]
    
    return None


def load_template(template_path: Path, verbose: bool = False) -> Dict:
    """Load a single protocol template."""
    if verbose:
        print(f"[INFO] Loading template: {template_path}")
    
    try:
        content = template_path.read_text(encoding='utf-8')
        
        # Extract basic metadata
        lines = content.split('\n')
        title = ""
        for line in lines[:20]:  # Check first 20 lines for title
            if line.startswith('# PROTOCOL'):
                title = line.strip('# ').strip()
                break
        
        return {
            "protocol_id": template_path.stem.split('-')[0],
            "template_path": str(template_path),
            "template_name": template_path.name,
            "title": title,
            "content": content,
            "size_bytes": len(content),
            "line_count": len(lines)
        }
    except Exception as e:
        print(f"[ERROR] Failed to load {template_path}: {e}", file=sys.stderr)
        return None


def main() -> int:
    args = parse_args()
    
    # Resolve paths
    templates_dir = ROOT / args.templates_dir
    output_path = ROOT / args.output
    
    if not templates_dir.exists():
        print(f"[ERROR] Templates directory not found: {templates_dir}", file=sys.stderr)
        return 1
    
    # Parse protocol IDs
    protocol_ids = [pid.strip() for pid in args.protocol_ids.split(',')]
    
    if args.verbose:
        print(f"[INFO] Loading {len(protocol_ids)} protocol templates")
        print(f"[INFO] Templates directory: {templates_dir}")
    
    # Load templates
    loaded_templates = []
    missing_templates = []
    
    for protocol_id in protocol_ids:
        template_path = find_template_file(protocol_id, templates_dir)
        
        if not template_path:
            missing_templates.append(protocol_id)
            print(f"[WARN] Template not found for protocol {protocol_id}", file=sys.stderr)
            continue
        
        template_data = load_template(template_path, args.verbose)
        if template_data:
            loaded_templates.append(template_data)
    
    # Create output
    output_data = {
        "loaded_count": len(loaded_templates),
        "missing_count": len(missing_templates),
        "missing_protocols": missing_templates,
        "templates": loaded_templates,
        "metadata": {
            "templates_dir": str(templates_dir),
            "protocol_ids_requested": protocol_ids,
            "total_size_bytes": sum(t["size_bytes"] for t in loaded_templates),
            "total_lines": sum(t["line_count"] for t in loaded_templates)
        }
    }
    
    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output_data, indent=2), encoding='utf-8')
    
    if args.verbose:
        print(f"[INFO] Loaded {len(loaded_templates)} templates")
        print(f"[INFO] Output written to: {output_path}")
    
    # Summary
    print(f"[OK] Loaded {len(loaded_templates)}/{len(protocol_ids)} templates")
    if missing_templates:
        print(f"[WARN] Missing templates: {', '.join(missing_templates)}")
        return 2
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
