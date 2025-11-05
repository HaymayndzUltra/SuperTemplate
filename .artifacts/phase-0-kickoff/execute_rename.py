#!/usr/bin/env python3
"""
Atomic rename execution for Protocol 18-23 script corrections
Based on 01-RENAMING-MANIFEST.md
"""

import os
import sys
import json
import shutil
from pathlib import Path
from datetime import datetime

# Base paths
PROJECT_ROOT = Path("/home/haymayndz/SuperTemplate")
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
BACKUP_DIR = PROJECT_ROOT / ".artifacts/phase-0-kickoff/backup"

# Rename mapping based on manifest
RENAME_MAP = {
    # Protocol 18 (14 → 18)
    "validate_gate_14_baseline.py": "validate_gate_18_baseline.py",
    "validate_gate_14_optimization.py": "validate_gate_18_optimization.py",
    "validate_gate_14_diagnostics.py": "validate_gate_18_diagnostics.py",
    "validate_gate_14_governance.py": "validate_gate_18_governance.py",
    
    # Protocol 19 (16 → 19)
    "validate_gate_16_completeness.py": "validate_gate_19_completeness.py",
    "validate_gate_16_enablement.py": "validate_gate_19_enablement.py",
    "validate_gate_16_publication.py": "validate_gate_19_publication.py",
    
    # Protocol 20 (17 → 20)
    "validate_gate_17_deliverables.py": "validate_gate_20_deliverables.py",
    "validate_gate_17_handover.py": "validate_gate_20_handover.py",
    "validate_gate_17_governance.py": "validate_gate_20_governance.py",
    
    # Protocol 21 (18 → 21)
    "validate_gate_18_backlog.py": "validate_gate_21_backlog.py",
    "validate_gate_18_approvals.py": "validate_gate_21_approvals.py",
    "validate_gate_18_governance.py": "validate_gate_21_governance.py",
}

def create_backup():
    """Create backup of scripts directory"""
    print(f"Creating backup in {BACKUP_DIR}...")
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = BACKUP_DIR / f"scripts_backup_{timestamp}.tar.gz"
    
    os.system(f"cd {PROJECT_ROOT} && tar -czf {backup_file} scripts/")
    print(f"✓ Backup created: {backup_file}")
    return backup_file

def execute_renames():
    """Execute all rename operations"""
    results = {
        "success": [],
        "errors": [],
        "skipped": [],
        "timestamp": datetime.now().isoformat()
    }
    
    print("\n=== EXECUTING RENAME OPERATIONS ===\n")
    
    for old_name, new_name in RENAME_MAP.items():
        old_path = SCRIPTS_DIR / old_name
        new_path = SCRIPTS_DIR / new_name
        
        print(f"Processing: {old_name} → {new_name}")
        
        if not old_path.exists():
            msg = f"  ⚠ Source not found: {old_path}"
            print(msg)
            results["skipped"].append({
                "file": old_name,
                "reason": "Source file does not exist"
            })
            continue
        
        if new_path.exists():
            msg = f"  ⚠ Target already exists: {new_path}"
            print(msg)
            results["skipped"].append({
                "file": old_name,
                "reason": "Target file already exists"
            })
            continue
        
        try:
            shutil.move(str(old_path), str(new_path))
            msg = f"  ✓ Renamed successfully"
            print(msg)
            results["success"].append({
                "old": old_name,
                "new": new_name,
                "path": str(new_path)
            })
        except Exception as e:
            msg = f"  ✗ Error: {str(e)}"
            print(msg)
            results["errors"].append({
                "file": old_name,
                "error": str(e)
            })
    
    return results

def save_results(results, backup_file):
    """Save execution results"""
    results_file = BACKUP_DIR / "rename_results.json"
    
    results["backup_location"] = str(backup_file)
    results["summary"] = {
        "total_operations": len(RENAME_MAP),
        "successful": len(results["success"]),
        "errors": len(results["errors"]),
        "skipped": len(results["skipped"])
    }
    
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✓ Results saved to: {results_file}")
    return results_file

def print_summary(results):
    """Print execution summary"""
    print("\n" + "="*60)
    print("RENAME OPERATION SUMMARY")
    print("="*60)
    print(f"Total operations: {results['summary']['total_operations']}")
    print(f"✓ Successful:     {results['summary']['successful']}")
    print(f"⚠ Skipped:        {results['summary']['skipped']}")
    print(f"✗ Errors:         {results['summary']['errors']}")
    print("="*60)
    
    if results['summary']['errors'] > 0:
        print("\n⚠ ERRORS ENCOUNTERED:")
        for error in results['errors']:
            print(f"  - {error['file']}: {error['error']}")
    
    if results['summary']['skipped'] > 0:
        print("\n⚠ SKIPPED FILES:")
        for skip in results['skipped']:
            print(f"  - {skip['file']}: {skip['reason']}")

def main():
    print("="*60)
    print("PHASE 1 - ATOMIC SCRIPT RENAME EXECUTION")
    print("="*60)
    print(f"Project: {PROJECT_ROOT}")
    print(f"Scripts: {SCRIPTS_DIR}")
    print(f"Operations: {len(RENAME_MAP)}")
    print("="*60)
    
    # Step 1: Create backup
    backup_file = create_backup()
    
    # Step 2: Execute renames
    results = execute_renames()
    
    # Step 3: Save results
    results_file = save_results(results, backup_file)
    
    # Step 4: Print summary
    print_summary(results)
    
    # Exit code based on errors
    if results['summary']['errors'] > 0:
        print("\n⚠ Some operations failed. Check results file for details.")
        sys.exit(1)
    else:
        print("\n✓ All operations completed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
