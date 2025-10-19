#!/usr/bin/env python3
"""Gate 4 validator for Protocol 01: Real Compliance Validation.

Validates HIPAA compliance checks and quality gates enforcement.
This script delegates to existing compliance validators.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run_compliance_checks(scripts_dir: Path = Path("scripts")) -> dict:
    """Run compliance validation scripts.
    
    Args:
        scripts_dir: Directory containing compliance scripts
        
    Returns:
        Validation result with status and notes
    """
    compliance_scripts = [
        "check_hipaa.py",
        "enforce_gates.py",
        "validate_compliance_assets.py",
    ]
    
    results = []
    all_passed = True
    
    for script in compliance_scripts:
        script_path = scripts_dir / script
        
        if not script_path.exists():
            results.append(f"Missing script: {script}")
            all_passed = False
            continue
        
        try:
            completed = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True,
                timeout=30,
            )
            
            if completed.returncode == 0:
                results.append(f"{script}: PASS")
            else:
                results.append(f"{script}: FAIL - {completed.stderr[:100]}")
                all_passed = False
                
        except subprocess.TimeoutExpired:
            results.append(f"{script}: TIMEOUT")
            all_passed = False
        except Exception as exc:
            results.append(f"{script}: ERROR - {exc}")
            all_passed = False
    
    status = "pass" if all_passed else "fail"
    notes = "; ".join(results)
    
    return {
        "status": status,
        "checks_run": len(compliance_scripts),
        "notes": notes,
    }


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate Gate 4: Compliance")
    parser.add_argument(
        "--scripts-dir",
        type=Path,
        default=Path("scripts"),
        help="Directory containing compliance scripts",
    )
    args = parser.parse_args(argv or sys.argv[1:])
    
    result = run_compliance_checks(args.scripts_dir)
    
    print(json.dumps(result, indent=2))
    
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
