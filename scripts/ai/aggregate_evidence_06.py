#!/usr/bin/env python3
"""
Script: aggregate_evidence_06.py
Protocol: 06-ai-use-case-definition
Purpose: Aggregate all evidence artifacts for Protocol 06
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

class EvidenceAggregator:
    """Main class for evidence aggregation"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts" / "protocol-06"
        
    def execute(self, protocol_id: str, output_file: str) -> Dict:
        """
        Main execution method
        
        Args:
            protocol_id: Protocol identifier
            output_file: Path for evidence manifest
            
        Returns:
            Dict: Execution results with status and manifest
        """
        try:
            # Aggregate evidence
            result = self._aggregate_evidence(protocol_id)
            
            # Generate evidence manifest
            self._generate_manifest(result, output_file)
            
            return {
                "status": "success",
                "result": result,
                "artifacts_count": len(result.get("artifacts", []))
            }
            
        except Exception as e:
            logger.error(f"Evidence aggregation failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _aggregate_evidence(self, protocol_id: str) -> Dict:
        """Core evidence aggregation logic"""
        artifacts = []
        
        # Define expected artifact directories
        expected_dirs = [
            "business-analysis",
            "data-assessment", 
            "success-metrics",
            "feasibility"
        ]
        
        # Scan artifacts directory
        if self.artifacts_dir.exists():
            for artifact_dir in self.artifacts_dir.iterdir():
                if artifact_dir.is_dir():
                    for artifact_file in artifact_dir.iterdir():
                        if artifact_file.is_file():
                            artifacts.append({
                                "name": artifact_file.name,
                                "path": str(artifact_file.relative_to(self.workspace)),
                                "size": artifact_file.stat().st_size,
                                "type": artifact_file.suffix,
                                "category": artifact_dir.name
                            })
        
        # Validate completeness
        missing_categories = [cat for cat in expected_dirs 
                            if not any(a["category"] == cat for a in artifacts)]
        
        return {
            "protocol_id": protocol_id,
            "artifacts": artifacts,
            "missing_categories": missing_categories,
            "completeness_score": 1.0 - (len(missing_categories) / len(expected_dirs)),
            "aggregation_timestamp": "2025-01-07T00:00:00Z"
        }
    
    def _generate_manifest(self, result: Dict, output_file: str) -> None:
        """Generate evidence manifest"""
        # Ensure artifacts directory exists
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        # Save manifest
        output_path = self.workspace / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        
        logger.info(f"Evidence manifest saved to: {output_path}")

def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(description="Aggregate evidence for protocol")
    parser.add_argument("--protocol-id", required=True, help="Protocol identifier")
    parser.add_argument("--output", required=True, help="Output manifest file")
    parser.add_argument("--workspace", default=".", help="Workspace path")
    
    args = parser.parse_args()
    
    aggregator = EvidenceAggregator(args.workspace)
    result = aggregator.execute(args.protocol_id, args.output)
    
    print(json.dumps(result, indent=2))
    
    # Exit with error code if aggregation failed
    if result["status"] == "error":
        exit(1)
    elif result.get("completeness_score", 0) < 0.8:
        exit(2)  # Low completeness warning

if __name__ == "__main__":
    main()
