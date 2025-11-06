#!/usr/bin/env python3
"""
Script: validate_prerequisites_1.py
Protocol: 06-create-prd
Purpose: Validate all prerequisites for Protocol 06
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

class PrerequisitesValidator:
    """Main class for prerequisites validation"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts"
        
    def execute(self, log_file: str = None) -> Dict:
        """
        Main execution method
        
        Args:
            log_file: Path for validation log
            
        Returns:
            Dict: Execution results with status and validation
        """
        try:
            # Validate prerequisites
            result = self._validate_prerequisites()
            
            # Generate validation log
            if log_file:
                self._generate_log(result, log_file)
            
            return {
                "status": "success",
                "result": result,
                "all_satisfied": result.get("all_prerequisites_satisfied", False)
            }
            
        except Exception as e:
            logger.error(f"Prerequisites validation failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _validate_prerequisites(self) -> Dict:
        """Core prerequisites validation logic"""
        prerequisites = {
            "artifacts": {
                "PROJECT-BRIEF.md": self._check_file_exists(".artifacts/protocol-03/PROJECT-BRIEF.md"),
                "technical-baseline.json": self._check_file_exists(".artifacts/protocol-03/technical-baseline.json"),
                "project-brief-validation-report.json": self._check_file_exists(".artifacts/protocol-03/project-brief-validation-report.json"),
                "BRIEF-APPROVAL-RECORD.json": self._check_file_exists(".artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json")
            },
            "approvals": {
                "Project Brief approval": self._check_approval_exists("project-brief"),
                "Technical baseline sign-off": self._check_approval_exists("technical-baseline")
            },
            "system_state": {
                "PRD templates": self._check_directory_exists(".templates/prd/"),
                "Automation scripts": self._check_scripts_exist(),
                "Validation tools": self._check_tools_available()
            }
        }
        
        # Calculate overall status
        all_items = {}
        for category in prerequisites.values():
            all_items.update(category)
        
        satisfied_count = sum(1 for item in all_items.values() if item["satisfied"])
        total_count = len(all_items)
        satisfaction_rate = satisfied_count / total_count if total_count > 0 else 0
        
        return {
            "prerequisites": prerequisites,
            "satisfaction_rate": satisfaction_rate,
            "all_prerequisites_satisfied": satisfaction_rate >= 1.0,
            "validation_timestamp": "2025-01-07T00:00:00Z"
        }
    
    def _check_file_exists(self, relative_path: str) -> Dict:
        """Check if required file exists"""
        file_path = self.workspace / relative_path
        return {
            "satisfied": file_path.exists() and file_path.is_file(),
            "path": relative_path,
            "message": "File found" if file_path.exists() else "File missing"
        }
    
    def _check_approval_exists(self, approval_type: str) -> Dict:
        """Check if approval record exists"""
        approval_file = self.workspace / f".artifacts/protocol-03/{approval_type}-approval.json"
        return {
            "satisfied": approval_file.exists(),
            "path": f".artifacts/protocol-03/{approval_type}-approval.json",
            "message": "Approval recorded" if approval_file.exists() else "Approval missing"
        }
    
    def _check_directory_exists(self, relative_path: str) -> Dict:
        """Check if directory exists"""
        dir_path = self.workspace / relative_path
        return {
            "satisfied": dir_path.exists() and dir_path.is_dir(),
            "path": relative_path,
            "message": "Directory found" if dir_path.exists() else "Directory missing"
        }
    
    def _check_scripts_exist(self) -> Dict:
        """Check if automation scripts exist"""
        scripts = [
            "scripts/generate_prd_assets.py",
            "scripts/validate_prd_gate.py", 
            "scripts/validate_prd_context.py",
            "scripts/validate_prd_requirements.py",
            "scripts/aggregate_evidence_1.py"
        ]
        
        missing_scripts = []
        for script in scripts:
            script_path = self.workspace / script
            if not script_path.exists():
                missing_scripts.append(script)
        
        return {
            "satisfied": len(missing_scripts) == 0,
            "path": "scripts/",
            "message": "All scripts found" if len(missing_scripts) == 0 else f"Missing scripts: {missing_scripts}",
            "missing_scripts": missing_scripts
        }
    
    def _check_tools_available(self) -> Dict:
        """Check if validation tools are available"""
        # For now, assume tools are available if directory exists
        tools_dir = self.workspace / "validators-system"
        return {
            "satisfied": tools_dir.exists(),
            "path": "validators-system/",
            "message": "Tools available" if tools_dir.exists() else "Tools missing"
        }
    
    def _generate_log(self, result: Dict, log_file: str) -> None:
        """Generate validation log"""
        log_path = self.workspace / log_file
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        
        logger.info(f"Validation log saved to: {log_path}")

def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(description="Validate protocol prerequisites")
    parser.add_argument("--log", help="Validation log file")
    parser.add_argument("--workspace", default=".", help="Workspace path")
    
    args = parser.parse_args()
    
    validator = PrerequisitesValidator(args.workspace)
    result = validator.execute(args.log)
    
    print(json.dumps(result, indent=2))
    
    # Exit with error code if prerequisites not satisfied
    if result["status"] == "error":
        exit(1)
    elif not result.get("all_satisfied", False):
        exit(2)  # Prerequisites missing

if __name__ == "__main__":
    main()
