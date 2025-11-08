#!/usr/bin/env python3
"""
Protocol 08 Gate 3: Ingestion Quality Validator
Validates data completeness, schema compliance, and quality metrics for ingested data.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any


def validate_ingestion_quality(input_path: Path, threshold: float = 0.90) -> Dict[str, Any]:
    """
    Validate ingestion quality metrics.
    
    Args:
        input_path: Path to ingested data directory
        threshold: Minimum quality score (default: 0.90)
    
    Returns:
        Dictionary with validation results
    """
    results = {
        "validator": "ingestion_quality",
        "input_path": str(input_path),
        "threshold": threshold,
        "passed": False,
        "quality_score": 0.0,
        "metrics": {},
        "issues": []
    }
    
    if not input_path.exists():
        results["issues"].append(f"Input path does not exist: {input_path}")
        return results
    
    # Check for required files/directories
    required_items = ["raw-data", "metadata", "quality-metrics.json"]
    missing_items = [item for item in required_items if not (input_path / item).exists()]
    
    if missing_items:
        results["issues"].append(f"Missing required items: {', '.join(missing_items)}")
    
    # Load quality metrics if available
    quality_file = input_path / "quality-metrics.json"
    if quality_file.exists():
        try:
            with open(quality_file, 'r') as f:
                quality_data = json.load(f)
            
            # Extract quality metrics
            completeness = quality_data.get("completeness", 0.0)
            schema_compliance = quality_data.get("schema_compliance", 0.0)
            volume_match = quality_data.get("volume_match", 0.0)
            timeliness = quality_data.get("timeliness", 1.0)
            
            results["metrics"] = {
                "completeness": completeness,
                "schema_compliance": schema_compliance,
                "volume_match": volume_match,
                "timeliness": timeliness
            }
            
            # Calculate overall quality score (weighted average)
            quality_score = (
                completeness * 0.35 +
                schema_compliance * 0.35 +
                volume_match * 0.20 +
                timeliness * 0.10
            )
            
            results["quality_score"] = quality_score
            
            # Validate against threshold
            if quality_score >= threshold:
                results["passed"] = True
            else:
                results["issues"].append(
                    f"Quality score {quality_score:.2f} below threshold {threshold}"
                )
            
            # Individual metric checks
            if completeness < 0.95:
                results["issues"].append(f"Completeness {completeness:.2%} below 95%")
            if schema_compliance < 0.90:
                results["issues"].append(f"Schema compliance {schema_compliance:.2%} below 90%")
                
        except json.JSONDecodeError as e:
            results["issues"].append(f"Failed to parse quality metrics: {e}")
        except Exception as e:
            results["issues"].append(f"Error reading quality metrics: {e}")
    else:
        results["issues"].append("Quality metrics file not found")
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Validate data ingestion quality for Protocol 08 Gate 3"
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to ingested data directory"
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.90,
        help="Minimum quality score threshold (default: 0.90)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Path to save validation report JSON"
    )
    
    args = parser.parse_args()
    
    # Run validation
    results = validate_ingestion_quality(args.input, args.threshold)
    
    # Save results if output specified
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"✅ Validation report saved to: {args.output}")
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"INGESTION QUALITY VALIDATION")
    print(f"{'='*60}")
    print(f"Input: {args.input}")
    print(f"Quality Score: {results['quality_score']:.2%}")
    print(f"Threshold: {args.threshold:.2%}")
    print(f"Status: {'✅ PASS' if results['passed'] else '❌ FAIL'}")
    
    if results['metrics']:
        print(f"\nMetrics:")
        for metric, value in results['metrics'].items():
            print(f"  - {metric}: {value:.2%}")
    
    if results['issues']:
        print(f"\nIssues:")
        for issue in results['issues']:
            print(f"  ⚠️  {issue}")
    
    print(f"{'='*60}\n")
    
    # Exit with appropriate code
    sys.exit(0 if results['passed'] else 1)


if __name__ == "__main__":
    main()
