#!/usr/bin/env python3
"""
Script: package_handoff.py
Protocol: 08-ai-data-collection-ingestion
Purpose: Package all artifacts for handoff to next protocol
Author: AI Workflow System
Created: 2025-11-08
"""

import json
import logging
import argparse
import zipfile
import shutil
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
import hashlib

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HandoffPackager:
    """Main class for packaging handoff materials"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts"
        self.protocol_08_dir = self.artifacts_dir / "protocol-08-ai-data-collection-ingestion"
        
    def execute(self, protocol_id: str, output_file: str) -> Dict:
        """
        Main execution method
        
        Args:
            protocol_id: Protocol identifier (e.g., "08")
            output_file: Path for handoff package file
            
        Returns:
            Dict: Execution results with status and package info
        """
        try:
            # Package handoff materials
            results = self._package_handoff_materials(protocol_id, output_file)
            
            # Generate package manifest
            self._generate_package_manifest(results, output_file)
            
            return {
                "status": "success",
                "results": results,
                "package_size_mb": results.get("package_size_mb", 0.0),
                "artifacts_packaged": results.get("artifacts_count", 0)
            }
            
        except Exception as e:
            logger.error(f"Handoff packaging failed: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "package_size_mb": 0.0,
                "artifacts_count": 0
            }
    
    def _package_handoff_materials(self, protocol_id: str, output_file: str) -> Dict:
        """Package all required artifacts for handoff"""
        results = {
            "packaging_start": datetime.now().isoformat(),
            "protocol_id": protocol_id,
            "output_package": output_file,
            "artifacts_found": 0,
            "artifacts_packaged": 0,
            "artifacts_failed": 0,
            "package_size_mb": 0.0,
            "artifact_details": [],
            "packaging_end": "",
            "duration_seconds": 0
        }
        
        # Define required artifacts
        required_artifacts = [
            "source-connections.json",
            "etl-configuration.yaml", 
            "ingestion-log.json",
            "quality-metrics.json",
            "raw-data/",
            "profiling-reports/"
        ]
        
        logger.info(f"Packaging handoff for Protocol {protocol_id}")
        
        # Create handoff package
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for artifact in required_artifacts:
                artifact_result = self._package_single_artifact(artifact, zipf)
                results["artifact_details"].append(artifact_result)
                
                if artifact_result["status"] == "success":
                    results["artifacts_packaged"] += 1
                else:
                    results["artifacts_failed"] += 1
                
                results["artifacts_found"] += 1
        
        # Calculate package size
        results["packaging_end"] = datetime.now().isoformat()
        start_time = datetime.fromisoformat(results["packaging_start"])
        end_time = datetime.fromisoformat(results["packaging_end"])
        results["duration_seconds"] = (end_time - start_time).total_seconds()
        
        package_path = Path(output_file)
        results["package_size_mb"] = round(package_path.stat().st_size / (1024 * 1024), 2)
        
        logger.info(f"Handoff package created: {output_file} ({results['package_size_mb']} MB)")
        
        return results
    
    def _package_single_artifact(self, artifact: str, zipf: zipfile.ZipFile) -> Dict:
        """Package a single artifact"""
        result = {
            "artifact": artifact,
            "status": "error",
            "message": "",
            "size_mb": 0.0,
            "checksum": ""
        }
        
        try:
            source_path = self.protocol_08_dir / artifact
            
            if not source_path.exists():
                result["message"] = f"Artifact not found: {artifact}"
                return result
            
            if source_path.is_file():
                # Package single file
                zipf.write(source_path, f"protocol-08-artifacts/{artifact}")
                result["size_mb"] = round(source_path.stat().st_size / (1024 * 1024), 2)
                result["checksum"] = self._calculate_checksum(source_path)
                result["status"] = "success"
                result["message"] = "File packaged successfully"
                
            elif source_path.is_dir():
                # Package directory
                for file_path in source_path.rglob('*'):
                    if file_path.is_file():
                        arcname = f"protocol-08-artifacts/{artifact}/{file_path.relative_to(source_path)}"
                        zipf.write(file_path, arcname)
                
                # Calculate directory size
                total_size = sum(f.stat().st_size for f in source_path.rglob('*') if f.is_file())
                result["size_mb"] = round(total_size / (1024 * 1024), 2)
                result["status"] = "success"
                result["message"] = f"Directory packaged successfully ({len(list(source_path.rglob('*')))} files)"
            
        except Exception as e:
            result["message"] = f"Packaging error: {str(e)}"
        
        return result
    
    def _calculate_checksum(self, file_path: Path) -> str:
        """Calculate SHA-256 checksum of file"""
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    
    def _generate_package_manifest(self, results: Dict, output_file: str):
        """Generate package manifest"""
        manifest = {
            "handoff_package": {
                "protocol": "08",
                "protocol_name": "AI Data Collection & Ingestion",
                "target_protocol": "09",
                "target_name": "AI Data Cleaning & Validation",
                "package_file": output_file,
                "package_size_mb": results["package_size_mb"],
                "artifacts_count": results["artifacts_packaged"],
                "packaging_timestamp": results["packaging_end"],
                "packaging_duration_seconds": results["duration_seconds"],
                "status": "success" if results["artifacts_failed"] == 0 else "partial"
            },
            "package_contents": results["artifact_details"],
            "handoff_instructions": {
                "extract_to": "AI-project-workflow/.artifacts/protocol-09-ai-data-cleaning-validation/",
                "required_artifacts": [
                    "raw-data/",
                    "quality-metrics.json",
                    "source-connections.json"
                ],
                "optional_artifacts": [
                    "etl-configuration.yaml",
                    "ingestion-log.json",
                    "profiling-reports/"
                ],
                "validation_steps": [
                    "Verify raw data files are accessible",
                    "Check quality metrics meet thresholds",
                    "Validate source configurations",
                    "Review profiling reports"
                ]
            }
        }
        
        # Save manifest alongside package
        manifest_file = Path(output_file).with_suffix('.json')
        with open(manifest_file, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        logger.info(f"Package manifest generated: {manifest_file}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Package handoff materials")
    parser.add_argument("--protocol", required=True, help="Protocol identifier")
    parser.add_argument("--output", required=True, help="Output handoff package file path")
    
    args = parser.parse_args()
    
    # Initialize packager
    workspace_path = Path.cwd()
    packager = HandoffPackager(str(workspace_path))
    
    # Execute packaging
    result = packager.execute(args.protocol, args.output)
    
    # Exit with appropriate code
    if result["status"] == "success":
        exit(0)  # Success
    else:
        exit(2)  # Error - packaging failed

if __name__ == "__main__":
    main()
