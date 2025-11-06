#!/usr/bin/env python3
"""
Script: classify_ai_problem_type.py
Protocol: 06-ai-use-case-definition
Purpose: Classify AI problem type based on business requirements
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

class AIProblemClassifier:
    """Main class for AI problem type classification"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts" / "protocol-06"
        
    def execute(self, input_file: str, output_file: str) -> Dict:
        """
        Main execution method
        
        Args:
            input_file: Path to project brief or requirements
            output_file: Path for classification output
            
        Returns:
            Dict: Execution results with status and classification
        """
        try:
            # Read input
            input_path = self.workspace / input_file
            if not input_path.exists():
                raise FileNotFoundError(f"Input file not found: {input_path}")
            
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Perform classification
            result = self._classify_problem(content)
            
            # Generate evidence
            self._generate_evidence(result, output_file)
            
            return {
                "status": "success",
                "result": result,
                "confidence": result.get("confidence", 0.0)
            }
            
        except Exception as e:
            logger.error(f"Classification failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _classify_problem(self, content: str) -> Dict:
        """Core classification logic"""
        # Simple keyword-based classification
        problem_types = {
            "classification": ["classify", "categorize", "predict category", "label"],
            "regression": ["predict", "forecast", "estimate", "continuous", "numeric"],
            "clustering": ["group", "segment", "cluster", "find patterns"],
            "anomaly_detection": ["detect anomaly", "find outliers", "unusual"],
            "recommendation": ["recommend", "suggest", "personalize"],
            "nlp": ["text", "language", "sentiment", "document"],
            "computer_vision": ["image", "visual", "object detection", "recognition"]
        }
        
        content_lower = content.lower()
        scores = {}
        
        for problem_type, keywords in problem_types.items():
            score = sum(1 for keyword in keywords if keyword in content_lower)
            scores[problem_type] = score / len(keywords)
        
        # Get best match
        best_type = max(scores, key=scores.get)
        confidence = scores[best_type]
        
        return {
            "problem_type": best_type,
            "confidence": confidence,
            "all_scores": scores,
            "classification_method": "keyword_analysis"
        }
    
    def _generate_evidence(self, result: Dict, output_file: str) -> None:
        """Generate evidence artifacts"""
        # Ensure artifacts directory exists
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        # Save classification result
        output_path = self.workspace / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        
        logger.info(f"Classification saved to: {output_path}")

def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(description="Classify AI problem type")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--workspace", default=".", help="Workspace path")
    
    args = parser.parse_args()
    
    classifier = AIProblemClassifier(args.workspace)
    result = classifier.execute(args.input, args.output)
    
    print(json.dumps(result, indent=2))
    
    # Exit with error code if classification failed
    if result["status"] == "error":
        exit(1)
    elif result["confidence"] < 0.8:
        exit(2)  # Low confidence warning

if __name__ == "__main__":
    main()
