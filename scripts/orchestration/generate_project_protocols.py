#!/usr/bin/env python3
"""
Generate Project-Specific Protocols

Master orchestration script that coordinates the complete protocol generation pipeline:
1. Load foundation templates
2. Transform templates with project-specific customizations
3. Write generated protocols to disk
4. Create generation manifest

This script is called from Protocol 05b PHASE 7.

Usage:
    python scripts/orchestration/generate_project_protocols.py \
        --protocol-ids 06,07,08,09,10,11,12,13,14,15 \
        --project-brief PROJECT-BRIEF.md \
        --execution-plan PROTOCOL-EXECUTION-PLAN.md \
        --output-dir .cursor/project-protocols \
        --artifacts-dir .artifacts/protocol-05b
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List

# Add project root to path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate project-specific protocols")
    parser.add_argument(
        "--protocol-ids",
        required=True,
        help="Comma-separated protocol IDs to generate (e.g., 06,07,08)"
    )
    parser.add_argument(
        "--project-brief",
        required=True,
        help="Path to PROJECT-BRIEF.md"
    )
    parser.add_argument(
        "--execution-plan",
        required=True,
        help="Path to PROTOCOL-EXECUTION-PLAN.md"
    )
    parser.add_argument(
        "--output-dir",
        default=".cursor/project-protocols",
        help="Output directory for generated protocols"
    )
    parser.add_argument(
        "--artifacts-dir",
        default=".artifacts/protocol-05b",
        help="Directory for intermediate artifacts"
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


def run_script(script_path: str, args_list: List[str], verbose: bool = False) -> int:
    """Run a Python script and return exit code."""
    cmd = [sys.executable, script_path] + args_list
    
    if verbose:
        print(f"[INFO] Running: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=False, capture_output=not verbose)
        return result.returncode
    except Exception as e:
        print(f"[ERROR] Script execution failed: {e}", file=sys.stderr)
        return 1


def main() -> int:
    args = parse_args()
    
    # Resolve paths
    artifacts_dir = ROOT / args.artifacts_dir
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    
    # Define intermediate artifact paths
    loaded_templates_path = artifacts_dir / "loaded-templates.json"
    transformed_protocols_path = artifacts_dir / "transformed-protocols.json"
    
    # Start time
    start_time = datetime.utcnow()
    
    print("[MASTER RAY™ | PROTOCOL GENERATION START]")
    print(f"[INFO] Generating protocols: {args.protocol_ids}")
    print(f"[INFO] Project brief: {args.project_brief}")
    print(f"[INFO] Output directory: {args.output_dir}")
    
    # STEP 1: Load foundation templates
    print("\n[STEP 7.2] Loading foundation templates...")
    
    load_args = [
        "--protocol-ids", args.protocol_ids,
        "--templates-dir", ".cursor/ai-driven-workflow",
        "--output", str(loaded_templates_path)
    ]
    
    if args.verbose:
        load_args.append("--verbose")
    
    exit_code = run_script(
        "scripts/orchestration/load_protocol_templates.py",
        load_args,
        args.verbose
    )
    
    if exit_code != 0:
        print(f"[ERROR] Template loading failed with exit code {exit_code}", file=sys.stderr)
        return exit_code
    
    print("[OK] Templates loaded successfully")
    
    # STEP 2: Transform templates
    print("\n[STEP 7.3] Applying transformations...")
    
    transform_args = [
        "--templates", str(loaded_templates_path),
        "--project-brief", args.project_brief,
        "--execution-plan", args.execution_plan,
        "--output", str(transformed_protocols_path)
    ]
    
    if args.verbose:
        transform_args.append("--verbose")
    
    exit_code = run_script(
        "scripts/orchestration/transform_protocols.py",
        transform_args,
        args.verbose
    )
    
    if exit_code != 0:
        print(f"[ERROR] Transformation failed with exit code {exit_code}", file=sys.stderr)
        return exit_code
    
    print("[OK] Transformations applied successfully")
    
    # STEP 3: Write generated protocols
    print("\n[STEP 7.5] Writing generated protocols to disk...")
    
    write_args = [
        "--transformed", str(transformed_protocols_path),
        "--output-dir", args.output_dir,
        "--manifest", f"{args.output_dir}/.protocol-manifest.json"
    ]
    
    if args.force:
        write_args.append("--force")
    
    if args.verbose:
        write_args.append("--verbose")
    
    exit_code = run_script(
        "scripts/orchestration/write_generated_protocols.py",
        write_args,
        args.verbose
    )
    
    if exit_code != 0:
        print(f"[ERROR] Writing protocols failed with exit code {exit_code}", file=sys.stderr)
        return exit_code
    
    print("[OK] Protocols written successfully")
    
    # STEP 4: Validate generated protocols
    print("\n[STEP 7.4] Validating generated protocols...")
    
    validation_report_path = artifacts_dir / "validation-report.json"
    
    validate_args = [
        "--protocols-dir", args.output_dir,
        "--output", str(validation_report_path),
        "--min-score", "0.95",
        "--auto-fix"
    ]
    
    if args.verbose:
        validate_args.append("--verbose")
    
    exit_code = run_script(
        "scripts/orchestration/validate_generated_protocols.py",
        validate_args,
        args.verbose
    )
    
    if exit_code != 0:
        print(f"[WARN] Validation completed with issues (exit code {exit_code})", file=sys.stderr)
        # Don't fail the entire process, just warn
    else:
        print("[OK] All protocols passed validation")
    
    # STEP 5: Generate comprehensive report
    print("\n[STEP 7.7] Generating protocol generation report...")
    
    report_path = artifacts_dir / "PROTOCOL-GENERATION-REPORT.md"
    manifest_path = Path(args.output_dir) / ".protocol-manifest.json"
    
    report_args = [
        "--manifest", str(manifest_path),
        "--validation", str(validation_report_path),
        "--output", str(report_path)
    ]
    
    if args.verbose:
        report_args.append("--verbose")
    
    exit_code = run_script(
        "scripts/orchestration/generate_protocol_report.py",
        report_args,
        args.verbose
    )
    
    if exit_code != 0:
        print(f"[WARN] Report generation failed (exit code {exit_code})", file=sys.stderr)
    else:
        print(f"[OK] Report generated: {report_path}")
    
    # Generate summary
    end_time = datetime.utcnow()
    duration_ms = int((end_time - start_time).total_seconds() * 1000)
    
    # Load manifest for summary
    manifest_path = Path(args.output_dir) / ".protocol-manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        
        print("\n" + "="*60)
        print("PROTOCOL GENERATION SUMMARY")
        print("="*60)
        print(f"Project: {manifest.get('project_name', 'unknown')}")
        print(f"Protocols Generated: {manifest.get('total_protocols', 0)}")
        print(f"Customizations Applied: {manifest.get('total_customizations', 0)}")
        print(f"Total Size: {manifest.get('total_size_bytes', 0) / 1024:.2f} KB")
        print(f"Duration: {duration_ms} ms")
        print(f"Output Directory: {args.output_dir}")
        print(f"Manifest: {manifest_path}")
        print("="*60)
    
    print("\n[MASTER RAY™ | PROTOCOL GENERATION COMPLETE]")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
