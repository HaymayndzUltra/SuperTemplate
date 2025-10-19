#!/usr/bin/env python3
"""Evidence aggregation for Protocol 02 (02): Client Discovery Initiation.

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
    """Run a gate validator and capture results."""
    try:
        result = subprocess.run(
            [sys.executable, validator_script],
            capture_output=True,
            text=True,
            timeout=30,
        )
        
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


def aggregate_evidence(output_dir: Path, protocol_id: str = "02") -> None:
    """Aggregate evidence from all Protocol 02 gates."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    data = load_manifest_data(protocol_id)
    
    validators = [
        {
            "name": "gate_1_objective_alignment",
            "command": "python3 scripts/validate_gate_02_objectives.py",
            "script": "scripts/validate_gate_02_objectives.py",
        },
        {
            "name": "gate_2_requirement_completeness",
            "command": "python3 scripts/validate_gate_02_requirements.py",
            "script": "scripts/validate_gate_02_requirements.py",
        },
        {
            "name": "gate_3_expectation_alignment",
            "command": "python3 scripts/validate_gate_02_expectations.py",
            "script": "scripts/validate_gate_02_expectations.py",
        },
        {
            "name": "gate_4_discovery_confirmation",
            "command": "python3 scripts/validate_gate_02_confirmation.py",
            "script": "scripts/validate_gate_02_confirmation.py",
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
    
    artifacts = [
        {
            "path": ".artifacts/protocol-02/client-context-notes.md",
            "description": "Business objectives and user goals",
        },
        {
            "path": ".artifacts/protocol-02/client-discovery-form.md",
            "description": "Structured feature list and requirements",
        },
        {
            "path": ".artifacts/protocol-02/scope-clarification.md",
            "description": "Technical preferences and constraints",
        },
        {
            "path": ".artifacts/protocol-02/timeline-discussion.md",
            "description": "Delivery expectations and milestones",
        },
        {
            "path": ".artifacts/protocol-02/communication-plan.md",
            "description": "Collaboration blueprint",
        },
        {
            "path": ".artifacts/protocol-02/discovery-recap.md",
            "description": "Client-approved discovery summary",
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
    
    manifest_path = output_dir / "evidence-manifest.json"
    notes = f"Evidence aggregated at {datetime.utcnow().isoformat()}Z"
    write_manifest(manifest_path, data, artifact_results, validator_results, notes)
    
    print(f"Evidence manifest written to {manifest_path}")
    
    passed_validators = sum(1 for v in validator_results if v["status"] == "pass")
    print(f"\nValidation Summary:")
    print(f"  Validators: {passed_validators}/{len(validator_results)} passed")
    print(f"  Artifacts: {sum(1 for a in artifact_results if a['status'] == 'generated')}/{len(artifact_results)} generated")


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Aggregate evidence for Protocol 02")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(".artifacts/protocol-02"),
        help="Output directory for evidence manifest",
    )
    parser.add_argument(
        "--protocol-id",
        type=str,
        default="02",
        help="Protocol identifier (default: 02)",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    aggregate_evidence(args.output, args.protocol_id)
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
