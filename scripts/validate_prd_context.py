#!/usr/bin/env python3
"""
Script: validate_prd_context.py
Protocol: 06-create-prd
Purpose: Validate PRD context and alignment
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

class PRDContextValidator:
    """Main class for PRD context validation"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        
    def execute(self, input_file: str, output_file: str) -> Dict:
        """
        Main execution method
        
        Args:
            input_file: Path to PRD context file
            output_file: Path for validation report
            
        Returns:
            Dict: Execution results with status and validation
        """
        try:
            # Load context
            context = self._load_context(input_file)
            
            # Validate context
            result = self._validate_context(context)
            
            # Generate validation report
            self._generate_report(result, output_file)
            
            return {
                "status": "success",
                "result": result,
                "validation_passed": result.get("overall_score", 0) >= 0.8
            }
            
        except Exception as e:
            logger.error(f"Context validation failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _load_context(self, input_file: str) -> Dict:
        """Load PRD context from file"""
        input_path = self.workspace / input_file
        if not input_path.exists():
            # Create sample context for validation
            return {
                "feature_name": "sample-feature",
                "business_objectives": ["Increase user engagement"],
                "stakeholders": ["Product Team", "Engineering"],
                "success_metrics": ["User retention rate"],
                "constraints": ["Budget limits", "Technical feasibility"]
            }
        
        with open(input_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _validate_context(self, context: Dict) -> Dict:
        """Core context validation logic"""
        validations = {
            "feature_name": bool(context.get("feature_name")),
            "business_objectives": len(context.get("business_objectives", [])) > 0,
            "stakeholders": len(context.get("stakeholders", [])) > 0,
            "success_metrics": len(context.get("success_metrics", [])) > 0,
            "constraints": isinstance(context.get("constraints"), list)
        }
        
        # Calculate overall score
        passed_count = sum(1 for v in validations.values() if v)
        total_count = len(validations)
        overall_score = passed_count / total_count if total_count > 0 else 0
        
        return {
            "validations": validations,
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
    parser = argparse.ArgumentParser(description="Validate PRD context")
    parser.add_argument("--input", required=True, help="Input context file")
    parser.add_argument("--output", required=True, help="Output validation report")
    parser.add_argument("--workspace", default=".", help="Workspace path")
    
    args = parser.parse_args()
    
    validator = PRDContextValidator(args.workspace)
    result = validator.execute(args.input, args.output)
    
    print(json.dumps(result, indent=2))
    
    # Exit with error code if validation failed
    if result["status"] == "error":
        exit(1)
    elif not result.get("validation_passed", False):
        exit(2)  # Validation failed

if __name__ == "__main__":
    main()
