#!/usr/bin/env python3
"""
Script: validate_handoff.py
Protocol: 08-ai-data-collection-ingestion
Purpose: Validate handoff package completeness and integrity
Author: AI Workflow System
Created: 2025-11-08
"""

import json
import logging
import argparse
import zipfile
import hashlib
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HandoffValidator:
    """Main class for handoff package validation"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts"
        
    def execute(self, package_file: str, output_file: str) -> Dict:
        """
        Main execution method
        
        Args:
            package_file: Path to handoff package file
            output_file: Path for validation report file
            
        Returns:
            Dict: Execution results with status and validation info
        """
        try:
            # Validate handoff package
            results = self._validate_handoff_package(package_file)
            
            # Generate validation report
            self._generate_validation_report(results, output_file)
            
            return {
                "status": "success",
                "results": results,
                "validation_score": results.get("validation_score", 0.0),
                "handoff_valid": results.get("handoff_valid", False)
            }
            
        except Exception as e:
            logger.error(f"Handoff validation failed: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "validation_score": 0.0,
                "handoff_valid": False
            }
    
    def _validate_handoff_package(self, package_file: str) -> Dict:
        """Validate handoff package completeness and integrity"""
        results = {
            "validation_start": datetime.now().isoformat(),
            "package_file": package_file,
            "package_size_mb": 0.0,
            "total_files": 0,
            "valid_files": 0,
            "invalid_files": 0,
            "missing_required": 0,
            "validation_details": [],
            "validation_score": 0.0,
            "handoff_valid": False,
            "validation_end": "",
            "duration_seconds": 0
        }
        
        package_path = Path(package_file)
        
        # Check if package exists
        if not package_path.exists():
            raise FileNotFoundError(f"Handoff package not found: {package_file}")
        
        # Get package size
        results["package_size_mb"] = round(package_path.stat().st_size / (1024 * 1024), 2)
        
        # Define required artifacts
        required_artifacts = [
            "protocol-08-artifacts/source-connections.json",
            "protocol-08-artifacts/etl-configuration.yaml",
            "protocol-08-artifacts/ingestion-log.json",
            "protocol-08-artifacts/quality-metrics.json",
            "protocol-08-artifacts/raw-data/",  # Directory
            "protocol-08-artifacts/profiling-reports/"  # Directory
        ]
        
        optional_artifacts = [
            "protocol-08-artifacts/handoff-manifest.json",
            "protocol-08-artifacts/validation-summary.json"
        ]
        
        logger.info(f"Validating handoff package: {package_file}")
        
        # Extract and validate package contents
        with zipfile.ZipFile(package_file, 'r') as zipf:
            file_list = zipf.namelist()
            results["total_files"] = len(file_list)
            
            # Validate required artifacts
            for required_artifact in required_artifacts:
                validation_result = self._validate_artifact(zipf, required_artifact, required=True)
                results["validation_details"].append(validation_result)
                
                if validation_result["status"] == "success":
                    results["valid_files"] += 1
                else:
                    results["invalid_files"] += 1
                    if validation_result.get("required", False):
                        results["missing_required"] += 1
            
            # Validate optional artifacts
            for optional_artifact in optional_artifacts:
                validation_result = self._validate_artifact(zipf, optional_artifact, required=False)
                results["validation_details"].append(validation_result)
                
                if validation_result["status"] == "success":
                    results["valid_files"] += 1
                else:
                    results["invalid_files"] += 1
        
        # Calculate final results
        results["validation_end"] = datetime.now().isoformat()
        start_time = datetime.fromisoformat(results["validation_start"])
        end_time = datetime.fromisoformat(results["validation_end"])
        results["duration_seconds"] = (end_time - start_time).total_seconds()
        
        # Calculate validation score
        total_required = len(required_artifacts)
        total_optional = len(optional_artifacts)
        
        if total_required > 0:
            required_score = (total_required - results["missing_required"]) / total_required
            optional_score = results["valid_files"] / (total_required + total_optional)
            results["validation_score"] = round((required_score * 0.8 + optional_score * 0.2), 3)
        
        results["handoff_valid"] = results["validation_score"] >= 0.9 and results["missing_required"] == 0
        
        logger.info(f"Handoff validation completed: {results['validation_score']:.3f} score")
        
        return results
    
    def _validate_artifact(self, zipf: zipfile.ZipFile, artifact_path: str, required: bool) -> Dict:
        """Validate a single artifact in the package"""
        result = {
            "artifact": artifact_path,
            "required": required,
            "status": "error",
            "message": "",
            "size_bytes": 0,
            "checksum": ""
        }
        
        try:
            # Check if artifact exists in package
            if artifact_path.endswith('/'):
                # Directory check
                dir_prefix = artifact_path
                matching_files = [f for f in zipf.namelist() if f.startswith(dir_prefix)]
                
                if matching_files:
                    result["status"] = "success"
                    result["message"] = f"Directory found with {len(matching_files)} files"
                    result["size_bytes"] = sum(zipf.getinfo(f).file_size for f in matching_files)
                else:
                    result["status"] = "error"
                    result["message"] = f"Directory not found: {artifact_path}"
            else:
                # File check
                if artifact_path in zipf.namelist():
                    file_info = zipf.getinfo(artifact_path)
                    result["status"] = "success"
                    result["message"] = "File found and accessible"
                    result["size_bytes"] = file_info.file_size
                    result["checksum"] = self._calculate_file_checksum(zipf, artifact_path)
                    
                    # Additional validation for specific file types
                    if artifact_path.endswith('.json'):
                        self._validate_json_content(zipf, artifact_path, result)
                    elif artifact_path.endswith('.yaml') or artifact_path.endswith('.yml'):
                        self._validate_yaml_content(zipf, artifact_path, result)
                else:
                    result["status"] = "error"
                    result["message"] = f"File not found: {artifact_path}"
            
        except Exception as e:
            result["message"] = f"Validation error: {str(e)}"
        
        return result
    
    def _calculate_file_checksum(self, zipf: zipfile.ZipFile, file_path: str) -> str:
        """Calculate SHA-256 checksum of file in zip"""
        hash_sha256 = hashlib.sha256()
        with zipf.open(file_path) as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    
    def _validate_json_content(self, zipf: zipfile.ZipFile, file_path: str, result: Dict):
        """Validate JSON file content"""
        try:
            with zipf.open(file_path) as f:
                json.load(f)
            result["message"] += " (Valid JSON)"
        except json.JSONDecodeError as e:
            result["status"] = "warning"
            result["message"] += f" (Invalid JSON: {str(e)})"
    
    def _validate_yaml_content(self, zipf: zipfile.ZipFile, file_path: str, result: Dict):
        """Validate YAML file content"""
        try:
            import yaml
            with zipf.open(file_path) as f:
                yaml.safe_load(f)
            result["message"] += " (Valid YAML)"
        except Exception as e:
            result["status"] = "warning"
            result["message"] += f" (Invalid YAML: {str(e)})"
    
    def _generate_validation_report(self, results: Dict, output_file: str):
        """Generate handoff validation report"""
        # Ensure output directory exists
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Add validation summary
        report = {
            "validation_summary": {
                "package_file": results["package_file"],
                "validation_start": results["validation_start"],
                "validation_end": results["validation_end"],
                "duration_seconds": results["duration_seconds"],
                "package_size_mb": results["package_size_mb"],
                "total_files": results["total_files"],
                "valid_files": results["valid_files"],
                "invalid_files": results["invalid_files"],
                "missing_required": results["missing_required"],
                "validation_score": results["validation_score"],
                "handoff_valid": results["handoff_valid"],
                "overall_status": "pass" if results["handoff_valid"] else "fail"
            },
            "artifact_results": results["validation_details"],
            "detailed_results": results
        }
        
        # Write validation report
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Handoff validation report generated: {output_file}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Validate handoff package")
    parser.add_argument("--package", required=True, help="Handoff package file path")
    parser.add_argument("--output", required=True, help="Output validation report file path")
    
    args = parser.parse_args()
    
    # Initialize validator
    workspace_path = Path.cwd()
    validator = HandoffValidator(str(workspace_path))
    
    # Execute validation
    result = validator.execute(args.package, args.output)
    
    # Exit with appropriate code
    if result["status"] == "success" and result["handoff_valid"]:
        exit(0)  # Success
    elif result["status"] == "success":
        exit(1)  # Warning - validation issues
    else:
        exit(2)  # Error - validation failed

if __name__ == "__main__":
    main()
