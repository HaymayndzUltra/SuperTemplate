#!/usr/bin/env python3
"""
Script: calculate_feasibility_score.py
Protocol: 06-ai-use-case-definition
Purpose: Calculate Problem-AI Fit Score for feasibility assessment
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

class FeasibilityCalculator:
    """Main class for feasibility score calculation"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts" / "protocol-06"
        
    def execute(self, input_file: str, output_file: str) -> Dict:
        """
        Main execution method
        
        Args:
            input_file: Path to data assessment or requirements
            output_file: Path for feasibility report
            
        Returns:
            Dict: Execution results with status and feasibility score
        """
        try:
            # Read input
            input_path = self.workspace / input_file
            if not input_path.exists():
                raise FileNotFoundError(f"Input file not found: {input_path}")
            
            with open(input_path, 'r', encoding='utf-8') as f:
                data = json.load(f) if input_path.suffix == '.json' else {"content": f.read()}
            
            # Calculate feasibility
            result = self._calculate_feasibility(data)
            
            # Generate evidence
            self._generate_evidence(result, output_file)
            
            return {
                "status": "success",
                "result": result,
                "feasibility_score": result.get("overall_score", 0.0)
            }
            
        except Exception as e:
            logger.error(f"Feasibility calculation failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _calculate_feasibility(self, data: Dict) -> Dict:
        """Core feasibility calculation logic"""
        # Feasibility factors
        factors = {
            "data_availability": self._assess_data_availability(data),
            "technical_complexity": self._assess_technical_complexity(data),
            "business_impact": self._assess_business_impact(data),
            "resource_requirements": self._assess_resources(data),
            "timeline_realism": self._assess_timeline(data)
        }
        
        # Calculate weighted score
        weights = {
            "data_availability": 0.3,
            "technical_complexity": 0.25,
            "business_impact": 0.2,
            "resource_requirements": 0.15,
            "timeline_realism": 0.1
        }
        
        overall_score = sum(factors[factor] * weights[factor] for factor in factors)
        
        # Determine recommendation
        if overall_score >= 0.8:
            recommendation = "PROCEED"
        elif overall_score >= 0.6:
            recommendation = "PROCEED_WITH_MITIGATION"
        else:
            recommendation = "RECONSIDER"
        
        return {
            "overall_score": overall_score,
            "recommendation": recommendation,
            "factors": factors,
            "weights": weights,
            "threshold_met": overall_score >= 0.8
        }
    
    def _assess_data_availability(self, data: Dict) -> float:
        """Assess data availability (0-1 scale)"""
        # Simple heuristic based on content analysis
        content = data.get("content", "").lower()
        
        positive_indicators = ["data available", "sufficient data", "data sources", "database"]
        negative_indicators = ["no data", "missing data", "data collection needed", "insufficient"]
        
        positive_score = sum(1 for indicator in positive_indicators if indicator in content)
        negative_score = sum(1 for indicator in negative_indicators if indicator in content)
        
        # Base score with some randomness for simulation
        base_score = 0.7
        adjustment = (positive_score - negative_score) * 0.1
        return max(0.0, min(1.0, base_score + adjustment))
    
    def _assess_technical_complexity(self, data: Dict) -> float:
        """Assess technical complexity (0-1 scale, higher is better)"""
        content = data.get("content", "").lower()
        
        complex_indicators = ["deep learning", "neural network", "complex", "advanced"]
        simple_indicators = ["simple", "basic", "straightforward", "linear"]
        
        complex_score = sum(1 for indicator in complex_indicators if indicator in content)
        simple_score = sum(1 for indicator in simple_indicators if indicator in content)
        
        # Higher complexity score means more challenging (lower feasibility)
        base_score = 0.8
        complexity_penalty = complex_score * 0.15
        simplicity_bonus = simple_score * 0.1
        
        return max(0.0, min(1.0, base_score - complexity_penalty + simplicity_bonus))
    
    def _assess_business_impact(self, data: Dict) -> float:
        """Assess business impact (0-1 scale)"""
        content = data.get("content", "").lower()
        
        impact_indicators = ["high impact", "critical", "important", "valuable", "roi"]
        
        impact_score = sum(1 for indicator in impact_indicators if indicator in content)
        base_score = 0.6
        impact_bonus = impact_score * 0.08
        
        return max(0.0, min(1.0, base_score + impact_bonus))
    
    def _assess_resources(self, data: Dict) -> float:
        """Assess resource requirements (0-1 scale)"""
        # Default to good resource availability
        return 0.75
    
    def _assess_timeline(self, data: Dict) -> float:
        """Assess timeline realism (0-1 scale)"""
        # Default to realistic timeline
        return 0.8
    
    def _generate_evidence(self, result: Dict, output_file: str) -> None:
        """Generate evidence artifacts"""
        # Ensure artifacts directory exists
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        # Save feasibility result
        output_path = self.workspace / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        
        logger.info(f"Feasibility report saved to: {output_path}")

def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(description="Calculate feasibility score")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--workspace", default=".", help="Workspace path")
    
    args = parser.parse_args()
    
    calculator = FeasibilityCalculator(args.workspace)
    result = calculator.execute(args.input, args.output)
    
    print(json.dumps(result, indent=2))
    
    # Exit with error code if feasibility is low
    if result["status"] == "error":
        exit(1)
    elif result["feasibility_score"] < 0.8:
        exit(2)  # Below threshold warning

if __name__ == "__main__":
    main()
