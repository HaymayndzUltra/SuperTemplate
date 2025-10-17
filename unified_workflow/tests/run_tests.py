#!/usr/bin/env python3
"""
Test runner for Unified Developer Workflow

Runs all test suites and generates comprehensive test report.
"""

import pytest
import sys
import os
from pathlib import Path
import json
from datetime import datetime


def run_all_tests():
    """Run all test suites"""
    
    # Get test directory
    test_dir = Path(__file__).parent
    
    # Test files
    test_files = [
        "test_evidence_manager.py",
        "test_ai_executor.py", 
        "test_quality_gates.py",
        "test_validation_gates.py",
        "test_integration.py"
    ]
    
    # Run tests
    print("🧪 Running Unified Developer Workflow Tests")
    print("=" * 60)
    
    results = {}
    
    for test_file in test_files:
        test_path = test_dir / test_file
        
        if test_path.exists():
            print(f"\n📋 Running {test_file}")
            print("-" * 40)
            
            # Run pytest
            exit_code = pytest.main([
                str(test_path),
                "-v",
                "--tb=short",
                "--capture=no"
            ])
            
            results[test_file] = {
                "exit_code": exit_code,
                "status": "passed" if exit_code == 0 else "failed"
            }
            
            if exit_code == 0:
                print(f"✅ {test_file} - PASSED")
            else:
                print(f"❌ {test_file} - FAILED")
        else:
            print(f"⚠️  {test_file} - NOT FOUND")
            results[test_file] = {
                "exit_code": 1,
                "status": "not_found"
            }
    
    # Generate test report
    report = {
        "metadata": {
            "test_run_date": datetime.utcnow().isoformat() + "Z",
            "total_tests": len(test_files),
            "passed": len([r for r in results.values() if r["status"] == "passed"]),
            "failed": len([r for r in results.values() if r["status"] == "failed"]),
            "not_found": len([r for r in results.values() if r["status"] == "not_found"])
        },
        "results": results
    }
    
    # Save report
    report_path = test_dir / "test-report.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Print summary
    print("\n" + "=" * 60)
    print("🎉 Test Run Complete!")
    print(f"📊 Total Tests: {report['metadata']['total_tests']}")
    print(f"✅ Passed: {report['metadata']['passed']}")
    print(f"❌ Failed: {report['metadata']['failed']}")
    print(f"⚠️  Not Found: {report['metadata']['not_found']}")
    print(f"📋 Report saved: {report_path}")
    
    # Return overall status
    return 0 if report['metadata']['failed'] == 0 else 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
