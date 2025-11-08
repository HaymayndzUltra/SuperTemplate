#!/usr/bin/env python3
"""
Script: test_storage_access.py
Protocol: 08-ai-data-collection-ingestion
Purpose: Test data lake storage access and permissions
Author: AI Workflow System
Created: 2025-11-08
"""

import json
import logging
import argparse
import os
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StorageAccessTester:
    """Main class for storage access testing"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts"
        self.protocol_08_dir = self.artifacts_dir / "protocol-08-ai-data-collection-ingestion"
        
    def execute(self, storage_path: str, output_file: str) -> Dict:
        """
        Main execution method
        
        Args:
            storage_path: Path to test storage access
            output_file: Path for test results file
            
        Returns:
            Dict: Execution results with status and access info
        """
        try:
            # Test storage access
            results = self._test_storage_access(storage_path)
            
            # Generate test report
            self._generate_test_report(results, output_file)
            
            return {
                "status": "success",
                "results": results,
                "access_score": results.get("access_score", 0.0),
                "storage_accessible": results.get("storage_accessible", False)
            }
            
        except Exception as e:
            logger.error(f"Storage access test failed: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "access_score": 0.0,
                "storage_accessible": False
            }
    
    def _test_storage_access(self, storage_path: str) -> Dict:
        """Test storage access and permissions"""
        results = {
            "test_start": datetime.now().isoformat(),
            "storage_path": storage_path,
            "tests_performed": 0,
            "tests_passed": 0,
            "tests_failed": 0,
            "test_details": [],
            "access_score": 0.0,
            "storage_accessible": False,
            "test_end": "",
            "duration_seconds": 0
        }
        
        storage_dir = Path(storage_path)
        
        # Test 1: Directory exists
        test_result = self._test_directory_exists(storage_dir)
        results["test_details"].append(test_result)
        results["tests_performed"] += 1
        
        if test_result["status"] == "pass":
            results["tests_passed"] += 1
        else:
            results["tests_failed"] += 1
        
        # Test 2: Read permissions
        test_result = self._test_read_permissions(storage_dir)
        results["test_details"].append(test_result)
        results["tests_performed"] += 1
        
        if test_result["status"] == "pass":
            results["tests_passed"] += 1
        else:
            results["tests_failed"] += 1
        
        # Test 3: Write permissions
        test_result = self._test_write_permissions(storage_dir)
        results["test_details"].append(test_result)
        results["tests_performed"] += 1
        
        if test_result["status"] == "pass":
            results["tests_passed"] += 1
        else:
            results["tests_failed"] += 1
        
        # Test 4: Directory creation
        test_result = self._test_directory_creation(storage_dir)
        results["test_details"].append(test_result)
        results["tests_performed"] += 1
        
        if test_result["status"] == "pass":
            results["tests_passed"] += 1
        else:
            results["tests_failed"] += 1
        
        # Test 5: File operations
        test_result = self._test_file_operations(storage_dir)
        results["test_details"].append(test_result)
        results["tests_performed"] += 1
        
        if test_result["status"] == "pass":
            results["tests_passed"] += 1
        else:
            results["tests_failed"] += 1
        
        # Calculate final results
        results["test_end"] = datetime.now().isoformat()
        start_time = datetime.fromisoformat(results["test_start"])
        end_time = datetime.fromisoformat(results["test_end"])
        results["duration_seconds"] = (end_time - start_time).total_seconds()
        
        # Calculate access score
        if results["tests_performed"] > 0:
            results["access_score"] = results["tests_passed"] / results["tests_performed"]
        
        results["storage_accessible"] = results["access_score"] >= 0.8
        
        logger.info(f"Storage access test completed: {results['tests_passed']}/{results['tests_performed']} tests passed")
        
        return results
    
    def _test_directory_exists(self, storage_dir: Path) -> Dict:
        """Test if storage directory exists"""
        result = {
            "test_name": "Directory Exists",
            "status": "fail",
            "message": "",
            "details": {}
        }
        
        try:
            if storage_dir.exists():
                result["status"] = "pass"
                result["message"] = f"Directory exists: {storage_dir}"
                result["details"] = {
                    "absolute_path": str(storage_dir.absolute()),
                    "is_directory": storage_dir.is_dir(),
                    "parent_exists": storage_dir.parent.exists()
                }
            else:
                result["message"] = f"Directory does not exist: {storage_dir}"
                result["details"] = {
                    "absolute_path": str(storage_dir.absolute()),
                    "parent_exists": storage_dir.parent.exists(),
                    "suggestion": "Create the directory or check the path"
                }
        except Exception as e:
            result["message"] = f"Error checking directory: {str(e)}"
        
        return result
    
    def _test_read_permissions(self, storage_dir: Path) -> Dict:
        """Test read permissions on storage directory"""
        result = {
            "test_name": "Read Permissions",
            "status": "fail",
            "message": "",
            "details": {}
        }
        
        try:
            if not storage_dir.exists():
                result["message"] = "Directory does not exist"
                return result
            
            # Try to list directory contents
            contents = list(storage_dir.iterdir())
            result["status"] = "pass"
            result["message"] = f"Read permissions OK (found {len(contents)} items)"
            result["details"] = {
                "items_count": len(contents),
                "can_list": True,
                "subdirectories": len([item for item in contents if item.is_dir()]),
                "files": len([item for item in contents if item.is_file()])
            }
            
        except PermissionError:
            result["message"] = "Permission denied - cannot read directory"
        except Exception as e:
            result["message"] = f"Error testing read permissions: {str(e)}"
        
        return result
    
    def _test_write_permissions(self, storage_dir: Path) -> Dict:
        """Test write permissions on storage directory"""
        result = {
            "test_name": "Write Permissions",
            "status": "fail",
            "message": "",
            "details": {}
        }
        
        try:
            if not storage_dir.exists():
                result["message"] = "Directory does not exist"
                return result
            
            # Try to create a test file
            test_file = storage_dir / ".storage_access_test"
            test_file.write_text("test")
            
            # Clean up test file
            test_file.unlink()
            
            result["status"] = "pass"
            result["message"] = "Write permissions OK"
            result["details"] = {
                "can_create_files": True,
                "can_delete_files": True,
                "test_file_created": str(test_file)
            }
            
        except PermissionError:
            result["message"] = "Permission denied - cannot write to directory"
        except Exception as e:
            result["message"] = f"Error testing write permissions: {str(e)}"
        
        return result
    
    def _test_directory_creation(self, storage_dir: Path) -> Dict:
        """Test directory creation permissions"""
        result = {
            "test_name": "Directory Creation",
            "status": "fail",
            "message": "",
            "details": {}
        }
        
        try:
            if not storage_dir.exists():
                result["message"] = "Directory does not exist"
                return result
            
            # Try to create a test subdirectory
            test_dir = storage_dir / ".test_subdir"
            test_dir.mkdir(exist_ok=True)
            
            # Clean up test directory
            test_dir.rmdir()
            
            result["status"] = "pass"
            result["message"] = "Directory creation permissions OK"
            result["details"] = {
                "can_create_directories": True,
                "can_delete_directories": True,
                "test_directory_created": str(test_dir)
            }
            
        except PermissionError:
            result["message"] = "Permission denied - cannot create subdirectories"
        except Exception as e:
            result["message"] = f"Error testing directory creation: {str(e)}"
        
        return result
    
    def _test_file_operations(self, storage_dir: Path) -> Dict:
        """Test comprehensive file operations"""
        result = {
            "test_name": "File Operations",
            "status": "fail",
            "message": "",
            "details": {}
        }
        
        try:
            if not storage_dir.exists():
                result["message"] = "Directory does not exist"
                return result
            
            # Test file creation, writing, reading, and deletion
            test_file = storage_dir / ".comprehensive_test.txt"
            
            # Create and write
            test_content = "Storage access test content\nLine 2\nLine 3"
            test_file.write_text(test_content)
            
            # Read back
            read_content = test_file.read_text()
            
            # Verify content
            content_match = read_content == test_content
            
            # Get file info
            file_stats = test_file.stat()
            
            # Clean up
            test_file.unlink()
            
            if content_match:
                result["status"] = "pass"
                result["message"] = "File operations OK"
                result["details"] = {
                    "can_create_files": True,
                    "can_write_files": True,
                    "can_read_files": True,
                    "can_delete_files": True,
                    "content_integrity": content_match,
                    "file_size_bytes": file_stats.st_size,
                    "test_file": str(test_file)
                }
            else:
                result["message"] = "File content integrity check failed"
                result["details"] = {
                    "content_match": content_match,
                    "expected_length": len(test_content),
                    "actual_length": len(read_content)
                }
            
        except Exception as e:
            result["message"] = f"Error testing file operations: {str(e)}"
        
        return result
    
    def _generate_test_report(self, results: Dict, output_file: str):
        """Generate storage access test report"""
        # Ensure output directory exists
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Add test summary
        report = {
            "test_summary": {
                "storage_path": results["storage_path"],
                "test_start": results["test_start"],
                "test_end": results["test_end"],
                "duration_seconds": results["duration_seconds"],
                "tests_performed": results["tests_performed"],
                "tests_passed": results["tests_passed"],
                "tests_failed": results["tests_failed"],
                "access_score": results["access_score"],
                "storage_accessible": results["storage_accessible"],
                "overall_status": "pass" if results["storage_accessible"] else "fail"
            },
            "detailed_results": results
        }
        
        # Write test report
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Storage access test report generated: {output_file}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Test storage access")
    parser.add_argument("--path", required=True, help="Storage path to test")
    parser.add_argument("--output", required=True, help="Output test results file path")
    
    args = parser.parse_args()
    
    # Initialize tester
    workspace_path = Path.cwd()
    tester = StorageAccessTester(str(workspace_path))
    
    # Execute test
    result = tester.execute(args.path, args.output)
    
    # Exit with appropriate code
    if result["status"] == "success" and result["storage_accessible"]:
        exit(0)  # Success
    elif result["status"] == "success":
        exit(1)  # Warning - partial access
    else:
        exit(2)  # Error - test failed

if __name__ == "__main__":
    main()
