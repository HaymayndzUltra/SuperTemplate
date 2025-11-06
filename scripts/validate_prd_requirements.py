#!/usr/bin/env python3
"""
Script: validate_prd_requirements.py
Protocol: 06-create-prd
Purpose: Validate PRD requirements completeness
Author: AI Workflow System
Created: 2025-01-07
"""

import json
import logging
import argparse
from pathlib import Path
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PRDRequirementsValidator:
    """Main class for PRD requirements validation"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        
    def execute(self, directory: str, output_file: str) -> Dict:
        """
        Main execution method
        
        Args:
            directory: Directory containing PRD artifacts
            output_file: Path for validation report
            
        Returns:
            Dict: Execution results with status and validation
        """
        try:
            # Scan directory for PRD artifacts
            artifacts = self._scan_artifacts(directory)
            
            # Validate requirements
            result = self._validate_requirements(artifacts)
            
            # Generate validation report
            self._generate_report(result, output_file)
            
            return {
                "status": "success",
                "result": result,
                "validation_passed": result.get("overall_score", 0) >= 0.8
            }
            
        except Exception as e:
            logger.error(f"Requirements validation failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _scan_artifacts(self, directory: str) -> Dict:
        """Scan directory for PRD artifacts"""
        dir_path = self.workspace / directory
        
        artifacts = {
            "prd_file": None,
            "functional_requirements": None,
            "user_stories": None,
            "technical_specifications": None,
            "acceptance_criteria": None
        }
        
        if dir_path.exists():
            for file_path in dir_path.rglob("*.md"):
                filename = file_path.name.lower()
                if "prd" in filename and not artifacts["prd_file"]:
                    artifacts["prd_file"] = str(file_path.relative_to(self.workspace))
                elif "functional" in filename and not artifacts["functional_requirements"]:
                    artifacts["functional_requirements"] = str(file_path.relative_to(self.workspace))
                elif "user" in filename and "story" in filename and not artifacts["user_stories"]:
                    artifacts["user_stories"] = str(file_path.relative_to(self.workspace))
                elif "technical" in filename and not artifacts["technical_specifications"]:
                    artifacts["technical_specifications"] = str(file_path.relative_to(self.workspace))
                elif "acceptance" in filename and not artifacts["acceptance_criteria"]:
                    artifacts["acceptance_criteria"] = str(file_path.relative_to(self.workspace))
        
        return artifacts
    
    def _validate_requirements(self, artifacts: Dict) -> Dict:
        """Core requirements validation logic"""
        validations = {
            "prd_document_exists": bool(artifacts["prd_file"]),
            "functional_requirements_defined": bool(artifacts["functional_requirements"]),
            "user_stories_documented": bool(artifacts["user_stories"]),
            "technical_specifications_provided": bool(artifacts["technical_specifications"]),
            "acceptance_criteria_specified": bool(artifacts["acceptance_criteria"])
        }
        
        # Calculate overall score
        passed_count = sum(1 for v in validations.values() if v)
        total_count = len(validations)
        overall_score = passed_count / total_count if total_count > 0 else 0
        
        return {
            "validations": validations,
            "artifacts_found": artifacts,
            "overall_score": overall_score,
            "validation_timestamp": "2025-01-07T00:00:00Z",
            "issues": [k for k, v in validations.items() if not v]
        }
    
    def _generate_report(self, result: Dict, output_file: str) -> None:
        """Generate validation report"""
        output_path = self.workspace / output_file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        
        logger.info(f"Validation report saved to: {output_path}")

def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(description="Validate PRD requirements")
    parser.add_argument("--dir", required=True, help="Directory containing PRD artifacts")
    parser.add_argument("--output", required=True, help="Output validation report")
    parser.add_argument("--workspace", default=".", help="Workspace path")
    
    args = parser.parse_args()
    
    validator = PRDRequirementsValidator(args.workspace)
    result = validator.execute(args.dir, args.output)
    
    print(json.dumps(result, indent=2))
    
    # Exit with error code if validation failed
    if result["status"] == "error":
        exit(1)
    elif not result.get("validation_passed", False):
        exit(2)  # Validation failed

if __name__ == "__main__":
    main()
