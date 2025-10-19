#!/usr/bin/env python3
"""Evidence aggregation for Protocol 01 (01): Client Proposal Generation.

Collects all gate validation results and artifacts into a consolidated evidence manifest.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from gate_utils import load_manifest_data, write_manifest


def run_gate_validator(validator_script: str) -> dict:
    """Run a gate validator and capture results.
    
    Args:
        validator_script: Path to validator script
        
    Returns:
        Validation result dict
    """
    try:
        result = subprocess.run(
            [sys.executable, validator_script],
            capture_output=True,
            text=True,
            timeout=30,
        )
        
        # Try to parse JSON output
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            return {
                "status": "fail" if result.returncode != 0 else "pass",
                "notes": result.stdout or result.stderr or "No output",
            }
            
    except subprocess.TimeoutExpired:
        return {"status": "fail", "notes": "Validator timeout"}
    except Exception as exc:
        return {"status": "fail", "notes": f"Validator error: {exc}"}


def aggregate_evidence(output_dir: Path, protocol_id: str = "01") -> None:
    """Aggregate evidence from all Protocol 01 gates.
    
    Args:
        output_dir: Output directory for aggregated evidence
        protocol_id: Protocol identifier (default: 01)
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load protocol metadata
    data = load_manifest_data(protocol_id)
    
    # Run all gate validators
    validators = [
        {
            "name": "gate_1_job_post_intake",
            "command": "python3 scripts/validate_gate_01_jobpost.py",
            "script": "scripts/validate_gate_01_jobpost.py",
        },
        {
            "name": "gate_2_tone_strategy",
            "command": "python3 scripts/validate_gate_01_tone.py",
            "script": "scripts/validate_gate_01_tone.py",
        },
        {
            "name": "gate_3_proposal_structure",
            "command": "python3 scripts/validate_gate_01_structure.py",
            "script": "scripts/validate_gate_01_structure.py",
        },
        {
            "name": "gate_4_compliance",
            "command": "python3 scripts/validate_gate_01_compliance.py",
            "script": "scripts/validate_gate_01_compliance.py",
        },
        {
            "name": "gate_5_final_validation",
            "command": "python3 scripts/validate_gate_01_final.py",
            "script": "scripts/validate_gate_01_final.py",
        },
    ]
    
    validator_results = []
    for validator in validators:
        result = run_gate_validator(validator["script"])
        validator_results.append({
            "name": validator["name"],
            "command": validator["command"],
            "status": result.get("status", "not-run"),
            "notes": result.get("notes", ""),
        })
    
    # Check artifact status
    artifacts = [
        {
            "path": ".artifacts/protocol-01/jobpost-analysis.json",
            "description": "Parsed job post objectives, tone, and risks",
        },
        {
            "path": ".artifacts/protocol-01/tone-map.json",
            "description": "Tone classification and strategy mapping",
        },
        {
            "path": ".artifacts/protocol-01/PROPOSAL.md",
            "description": "Client-facing proposal document",
        },
        {
            "path": ".artifacts/protocol-01/humanization-log.json",
            "description": "Humanization filter application log",
        },
        {
            "path": ".artifacts/protocol-01/proposal-validation-report.json",
            "description": "Final validation evidence",
        },
        {
            "path": ".artifacts/protocol-01/compliance-validation-report.json",
            "description": "Compliance check results",
        },
    ]
    
    artifact_results = []
    for artifact in artifacts:
        path = Path(artifact["path"])
        status = "generated" if path.exists() else "missing"
        artifact_results.append({
            "path": artifact["path"],
            "description": artifact["description"],
            "status": status,
        })
    
    # Write manifest
    manifest_path = output_dir / "evidence-manifest.json"
    notes = f"Evidence aggregated at {datetime.utcnow().isoformat()}Z"
    write_manifest(manifest_path, data, artifact_results, validator_results, notes)
    
    print(f"Evidence manifest written to {manifest_path}")
    
    # Print summary
    passed_validators = sum(1 for v in validator_results if v["status"] == "pass")
    print(f"\nValidation Summary:")
    print(f"  Validators: {passed_validators}/{len(validator_results)} passed")
    print(f"  Artifacts: {sum(1 for a in artifact_results if a['status'] == 'generated')}/{len(artifact_results)} generated")


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Aggregate evidence for Protocol 01")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(".artifacts/protocol-01"),
        help="Output directory for evidence manifest",
    )
    parser.add_argument(
        "--protocol-id",
        type=str,
        default="01",
        help="Protocol identifier (default: 01)",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    aggregate_evidence(args.output, args.protocol_id)
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
