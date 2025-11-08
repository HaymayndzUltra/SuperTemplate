#!/usr/bin/env python3
"""
Protocol 08 Gate 5: Documentation Validator
Validates completeness of documentation, artifacts, and audit trail.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any, List


def validate_documentation(
    protocol_dir: Path,
    protocol_number: str = "08"
) -> Dict[str, Any]:
    """
    Validate documentation completeness for protocol execution.
    
    Args:
        protocol_dir: Path to protocol artifacts directory
        protocol_number: Protocol number (default: "08")
    
    Returns:
        Dictionary with validation results
    """
    results = {
        "validator": "documentation",
        "protocol": protocol_number,
        "protocol_dir": str(protocol_dir),
        "passed": False,
        "coverage_score": 0.0,
        "artifacts": {},
        "missing": [],
        "warnings": []
    }
    
    if not protocol_dir.exists():
        results["missing"].append(f"Protocol directory does not exist: {protocol_dir}")
        return results
    
    # Define required artifacts based on protocol
    required_artifacts = {
        "source-config.yaml": "Data source configuration",
        "etl-config.yaml": "ETL pipeline configuration",
        "ingestion-log.json": "Execution audit trail",
        "quality-metrics.json": "Data quality metrics",
        "data-lineage.json": "Data lineage documentation",
        "handoff-package.zip": "Handoff package for next protocol",
        "evidence-manifest.json": "Evidence package manifest"
    }
    
    optional_artifacts = {
        "profiling-reports/": "Data profiling reports",
        "compliance-docs/": "Compliance documentation",
        "error-logs/": "Error and exception logs"
    }
    
    artifacts_found = 0
    total_required = len(required_artifacts)
    
    # Check required artifacts
    for artifact_name, description in required_artifacts.items():
        artifact_path = protocol_dir / artifact_name
        
        if artifact_path.exists():
            artifacts_found += 1
            
            # Get file size or item count
            if artifact_path.is_file():
                size = artifact_path.stat().st_size
                results["artifacts"][artifact_name] = {
                    "status": "✅ Present",
                    "description": description,
                    "size_bytes": size
                }
            else:
                item_count = len(list(artifact_path.iterdir()))
                results["artifacts"][artifact_name] = {
                    "status": "✅ Present",
                    "description": description,
                    "item_count": item_count
                }
        else:
            results["missing"].append(f"{artifact_name}: {description}")
            results["artifacts"][artifact_name] = {
                "status": "❌ Missing",
                "description": description
            }
    
    # Check optional artifacts (warnings only)
    for artifact_name, description in optional_artifacts.items():
        artifact_path = protocol_dir / artifact_name
        
        if artifact_path.exists():
            results["artifacts"][artifact_name] = {
                "status": "✅ Present (optional)",
                "description": description
            }
        else:
            results["warnings"].append(f"Optional artifact missing: {artifact_name}")
            results["artifacts"][artifact_name] = {
                "status": "⚠️ Missing (optional)",
                "description": description
            }
    
    # Validate evidence manifest if present
    manifest_path = protocol_dir / "evidence-manifest.json"
    if manifest_path.exists():
        try:
            with open(manifest_path, 'r') as f:
                manifest = json.load(f)
            
            # Check manifest structure
            required_fields = ["protocol", "execution_id", "timestamp", "artifacts"]
            missing_fields = [f for f in required_fields if f not in manifest]
            
            if missing_fields:
                results["warnings"].append(
                    f"Evidence manifest missing fields: {', '.join(missing_fields)}"
                )
            
            # Verify artifacts listed in manifest exist
            if "artifacts" in manifest:
                for artifact_entry in manifest["artifacts"]:
                    artifact_path = Path(artifact_entry.get("path", ""))
                    if not (protocol_dir / artifact_path).exists():
                        results["warnings"].append(
                            f"Manifest references missing artifact: {artifact_path}"
                        )
        except json.JSONDecodeError as e:
            results["warnings"].append(f"Failed to parse evidence manifest: {e}")
        except Exception as e:
            results["warnings"].append(f"Error validating evidence manifest: {e}")
    
    # Calculate coverage score
    results["coverage_score"] = artifacts_found / total_required if total_required > 0 else 0.0
    
    # Pass if 100% coverage (all required artifacts present)
    results["passed"] = results["coverage_score"] >= 1.0
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Validate documentation completeness for Protocol 08 Gate 5"
    )
    parser.add_argument(
        "--protocol-dir",
        type=Path,
        required=True,
        help="Path to protocol artifacts directory"
    )
    parser.add_argument(
        "--protocol",
        type=str,
        default="08",
        help="Protocol number (default: 08)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Path to save validation report JSON"
    )
    
    args = parser.parse_args()
    
    # Run validation
    results = validate_documentation(args.protocol_dir, args.protocol)
    
    # Save results if output specified
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"✅ Validation report saved to: {args.output}")
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"DOCUMENTATION VALIDATION - PROTOCOL {args.protocol}")
    print(f"{'='*60}")
    print(f"Protocol Directory: {args.protocol_dir}")
    print(f"Documentation Coverage: {results['coverage_score']:.2%}")
    print(f"Status: {'✅ PASS' if results['passed'] else '❌ FAIL'}")
    
    if results['artifacts']:
        print(f"\nArtifacts ({len(results['artifacts'])}):")
        for artifact_name, info in results['artifacts'].items():
            status = info['status']
            desc = info['description']
            
            extra_info = ""
            if 'size_bytes' in info:
                extra_info = f" ({info['size_bytes']:,} bytes)"
            elif 'item_count' in info:
                extra_info = f" ({info['item_count']} items)"
            
            print(f"  {status} {artifact_name}{extra_info}")
            print(f"      {desc}")
    
    if results['missing']:
        print(f"\n❌ MISSING REQUIRED ARTIFACTS ({len(results['missing'])}):")
        for missing in results['missing']:
            print(f"  ❌ {missing}")
    
    if results['warnings']:
        print(f"\n⚠️  WARNINGS ({len(results['warnings'])}):")
        for warning in results['warnings']:
            print(f"  ⚠️  {warning}")
    
    print(f"{'='*60}\n")
    
    # Exit with appropriate code
    sys.exit(0 if results['passed'] else 1)


if __name__ == "__main__":
    main()
