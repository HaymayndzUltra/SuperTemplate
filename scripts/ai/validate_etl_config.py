#!/usr/bin/env python3
"""
Script: validate_etl_config.py
Protocol: 08-ai-data-collection-ingestion
Purpose: Validate ETL configuration against data strategy requirements
Author: AI Workflow System
Created: 2025-11-08
"""

import json
import logging
import argparse
import yaml
from pathlib import Path
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ETLConfigValidator:
    """Main class for ETL configuration validation"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts"
        self.protocol_08_dir = self.artifacts_dir / "protocol-08-ai-data-collection-ingestion"
        
    def execute(self, config_file: str, strategy_file: str, output_file: str) -> Dict:
        """
        Main execution method
        
        Args:
            config_file: Path to ETL configuration file
            strategy_file: Path to data strategy file
            output_file: Path for validation report
            
        Returns:
            Dict: Execution results with status and validation
        """
        try:
            # Load configuration and strategy
            etl_config = self._load_config(config_file)
            data_strategy = self._load_strategy(strategy_file)
            
            # Validate ETL configuration
            results = self._validate_etl_configuration(etl_config, data_strategy)
            
            # Generate validation report
            self._generate_report(results, output_file)
            
            return {
                "status": "success",
                "results": results,
                "compliance_score": results.get("compliance_score", 0.0),
                "strategy_compliant": results.get("strategy_compliant", False)
            }
            
        except Exception as e:
            logger.error(f"Validation failed: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "compliance_score": 0.0,
                "strategy_compliant": False
            }
    
    def _load_config(self, config_file: str) -> Dict:
        """Load ETL configuration from YAML file"""
        config_path = Path(config_file)
        if not config_path.exists():
            raise FileNotFoundError(f"ETL configuration file not found: {config_file}")
        
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def _load_strategy(self, strategy_file: str) -> Dict:
        """Load data strategy from JSON file"""
        strategy_path = Path(strategy_file)
        if not strategy_path.exists():
            raise FileNotFoundError(f"Data strategy file not found: {strategy_file}")
        
        with open(strategy_path, 'r') as f:
            return json.load(f)
    
    def _validate_etl_configuration(self, etl_config: Dict, data_strategy: Dict) -> Dict:
        """Validate ETL configuration against strategy requirements"""
        results = {
            "total_requirements": 0,
            "satisfied_requirements": 0,
            "violated_requirements": 0,
            "validation_details": [],
            "strategy_compliant": True,
            "compliance_score": 0.0
        }
        
        # Validate data sources
        source_validation = self._validate_data_sources(etl_config, data_strategy)
        results["validation_details"].append(source_validation)
        
        # Validate extraction methods
        extraction_validation = self._validate_extraction_methods(etl_config, data_strategy)
        results["validation_details"].append(extraction_validation)
        
        # Validate quality requirements
        quality_validation = self._validate_quality_requirements(etl_config, data_strategy)
        results["validation_details"].append(quality_validation)
        
        # Validate compliance requirements
        compliance_validation = self._validate_compliance_requirements(etl_config, data_strategy)
        results["validation_details"].append(compliance_validation)
        
        # Calculate totals and score
        for validation in results["validation_details"]:
            results["total_requirements"] += validation["total_checks"]
            results["satisfied_requirements"] += validation["passed_checks"]
            results["violated_requirements"] += validation["failed_checks"]
        
        if results["total_requirements"] > 0:
            results["compliance_score"] = results["satisfied_requirements"] / results["total_requirements"]
            results["strategy_compliant"] = results["compliance_score"] >= 0.95
        
        return results
    
    def _validate_data_sources(self, etl_config: Dict, data_strategy: Dict) -> Dict:
        """Validate data source configuration"""
        validation = {
            "category": "Data Sources",
            "total_checks": 0,
            "passed_checks": 0,
            "failed_checks": 0,
            "details": []
        }
        
        # Check if all strategy sources are configured
        strategy_sources = data_strategy.get("data_sources", [])
        etl_sources = etl_config.get("sources", [])
        
        validation["total_checks"] += 1
        if len(etl_sources) >= len(strategy_sources):
            validation["passed_checks"] += 1
            validation["details"].append({
                "check": "Source Coverage",
                "status": "PASS",
                "message": f"All {len(strategy_sources)} strategy sources configured"
            })
        else:
            validation["failed_checks"] += 1
            validation["details"].append({
                "check": "Source Coverage",
                "status": "FAIL",
                "message": f"Missing sources: {len(strategy_sources) - len(etl_sources)} not configured"
            })
        
        # Check source authentication
        validation["total_checks"] += 1
        auth_configured = all(source.get("auth") for source in etl_sources)
        if auth_configured:
            validation["passed_checks"] += 1
            validation["details"].append({
                "check": "Authentication Configuration",
                "status": "PASS",
                "message": "All sources have authentication configured"
            })
        else:
            validation["failed_checks"] += 1
            validation["details"].append({
                "check": "Authentication Configuration",
                "status": "FAIL",
                "message": "Some sources missing authentication configuration"
            })
        
        return validation
    
    def _validate_extraction_methods(self, etl_config: Dict, data_strategy: Dict) -> Dict:
        """Validate extraction method configuration"""
        validation = {
            "category": "Extraction Methods",
            "total_checks": 0,
            "passed_checks": 0,
            "failed_checks": 0,
            "details": []
        }
        
        # Check extraction type compliance
        strategy_latency = data_strategy.get("requirements", {}).get("latency", "batch")
        etl_extraction = etl_config.get("extraction", {}).get("type", "batch")
        
        validation["total_checks"] += 1
        if self._extraction_type_compliant(strategy_latency, etl_extraction):
            validation["passed_checks"] += 1
            validation["details"].append({
                "check": "Extraction Type Compliance",
                "status": "PASS",
                "message": f"Extraction type '{etl_extraction}' meets latency requirements '{strategy_latency}'"
            })
        else:
            validation["failed_checks"] += 1
            validation["details"].append({
                "check": "Extraction Type Compliance",
                "status": "FAIL",
                "message": f"Extraction type '{etl_extraction}' doesn't meet latency requirements '{strategy_latency}'"
            })
        
        # Check streaming configuration if required
        if strategy_latency == "streaming":
            validation["total_checks"] += 1
            streaming_config = etl_config.get("streaming", {})
            required_streaming_fields = ["kafka_topics", "schema_registry", "buffer_size"]
            
            if all(field in streaming_config for field in required_streaming_fields):
                validation["passed_checks"] += 1
                validation["details"].append({
                    "check": "Streaming Configuration",
                    "status": "PASS",
                    "message": "All required streaming components configured"
                })
            else:
                validation["failed_checks"] += 1
                validation["details"].append({
                    "check": "Streaming Configuration",
                    "status": "FAIL",
                    "message": f"Missing streaming components: {required_streaming_fields}"
                })
        
        return validation
    
    def _validate_quality_requirements(self, etl_config: Dict, data_strategy: Dict) -> Dict:
        """Validate quality requirement configuration"""
        validation = {
            "category": "Quality Requirements",
            "total_checks": 0,
            "passed_checks": 0,
            "failed_checks": 0,
            "details": []
        }
        
        # Check quality thresholds
        strategy_quality = data_strategy.get("requirements", {}).get("quality", {})
        etl_quality = etl_config.get("quality", {})
        
        quality_checks = [
            ("completeness_threshold", "completeness"),
            ("accuracy_threshold", "accuracy"),
            ("timeliness_threshold", "timeliness")
        ]
        
        for strategy_field, etl_field in quality_checks:
            validation["total_checks"] += 1
            strategy_value = strategy_quality.get(strategy_field, 0.9)
            etl_value = etl_quality.get(etl_field, 0.9)
            
            if etl_value >= strategy_value:
                validation["passed_checks"] += 1
                validation["details"].append({
                    "check": f"Quality Threshold - {etl_field.title()}",
                    "status": "PASS",
                    "message": f"ETL threshold {etl_value} >= strategy requirement {strategy_value}"
                })
            else:
                validation["failed_checks"] += 1
                validation["details"].append({
                    "check": f"Quality Threshold - {etl_field.title()}",
                    "status": "FAIL",
                    "message": f"ETL threshold {etl_value} < strategy requirement {strategy_value}"
                })
        
        return validation
    
    def _validate_compliance_requirements(self, etl_config: Dict, data_strategy: Dict) -> Dict:
        """Validate compliance requirement configuration"""
        validation = {
            "category": "Compliance Requirements",
            "total_checks": 0,
            "passed_checks": 0,
            "failed_checks": 0,
            "details": []
        }
        
        # Check GDPR compliance
        validation["total_checks"] += 1
        gdpr_config = etl_config.get("compliance", {}).get("gdpr", {})
        required_gdpr_fields = ["data_masking", "consent_tracking", "right_to_deletion"]
        
        if all(field in gdpr_config for field in required_gdpr_fields):
            validation["passed_checks"] += 1
            validation["details"].append({
                "check": "GDPR Compliance",
                "status": "PASS",
                "message": "All required GDPR components configured"
            })
        else:
            validation["failed_checks"] += 1
            validation["details"].append({
                "check": "GDPR Compliance",
                "status": "FAIL",
                "message": f"Missing GDPR components: {required_gdpr_fields}"
            })
        
        # Check audit logging
        validation["total_checks"] += 1
        audit_config = etl_config.get("audit", {})
        if audit_config.get("enabled", False):
            validation["passed_checks"] += 1
            validation["details"].append({
                "check": "Audit Logging",
                "status": "PASS",
                "message": "Audit logging is enabled and configured"
            })
        else:
            validation["failed_checks"] += 1
            validation["details"].append({
                "check": "Audit Logging",
                "status": "FAIL",
                "message": "Audit logging is not enabled"
            })
        
        return validation
    
    def _extraction_type_compliant(self, strategy_latency: str, etl_extraction: str) -> bool:
        """Check if extraction type meets latency requirements"""
        compliance_map = {
            "realtime": ["streaming", "realtime"],
            "streaming": ["streaming", "realtime"],
            "batch": ["batch", "streaming", "realtime"]
        }
        
        return etl_extraction in compliance_map.get(strategy_latency, [])
    
    def _generate_report(self, results: Dict, output_file: str):
        """Generate validation report"""
        # Ensure output directory exists
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Add summary
        report = {
            "validation_summary": {
                "total_requirements": results["total_requirements"],
                "satisfied_requirements": results["satisfied_requirements"],
                "violated_requirements": results["violated_requirements"],
                "compliance_score": results["compliance_score"],
                "strategy_compliant": results["strategy_compliant"],
                "validation_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            },
            "detailed_results": results
        }
        
        # Write report
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"ETL validation report generated: {output_file}")

def main():
    """Main entry point"""
    import time
    parser = argparse.ArgumentParser(description="Validate ETL configuration")
    parser.add_argument("--config", required=True, help="ETL configuration file path")
    parser.add_argument("--strategy", required=True, help="Data strategy file path")
    parser.add_argument("--output", required=True, help="Output validation report file path")
    
    args = parser.parse_args()
    
    # Initialize validator
    workspace_path = Path.cwd()
    validator = ETLConfigValidator(str(workspace_path))
    
    # Execute validation
    result = validator.execute(args.config, args.strategy, args.output)
    
    # Exit with appropriate code
    if result["status"] == "success" and result["strategy_compliant"]:
        exit(0)  # Success
    elif result["status"] == "success":
        exit(1)  # Warning - partial compliance
    else:
        exit(2)  # Error - validation failed

if __name__ == "__main__":
    main()
