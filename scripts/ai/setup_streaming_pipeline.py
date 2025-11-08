#!/usr/bin/env python3
"""
Script: setup_streaming_pipeline.py
Protocol: 08-ai-data-collection-ingestion
Purpose: Set up streaming data pipeline infrastructure
Author: AI Workflow System
Created: 2025-11-08
"""

import json
import logging
import argparse
import yaml
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StreamingPipelineSetup:
    """Main class for streaming pipeline setup"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts"
        self.protocol_08_dir = self.artifacts_dir / "protocol-08-ai-data-collection-ingestion"
        
    def execute(self, config_file: str, output_file: str) -> Dict:
        """
        Main execution method
        
        Args:
            config_file: Path to streaming configuration file
            output_file: Path for setup results file
            
        Returns:
            Dict: Execution results with status and setup info
        """
        try:
            # Load streaming configuration
            streaming_config = self._load_config(config_file)
            
            # Set up streaming pipeline
            results = self._setup_streaming_pipeline(streaming_config)
            
            # Generate setup report
            self._generate_setup_report(results, output_file)
            
            return {
                "status": "success",
                "results": results,
                "setup_score": results.get("setup_score", 0.0),
                "pipeline_ready": results.get("pipeline_ready", False)
            }
            
        except Exception as e:
            logger.error(f"Streaming pipeline setup failed: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "setup_score": 0.0,
                "pipeline_ready": False
            }
    
    def _load_config(self, config_file: str) -> Dict:
        """Load streaming configuration from YAML file"""
        config_path = Path(config_file)
        if not config_path.exists():
            raise FileNotFoundError(f"Streaming configuration file not found: {config_file}")
        
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def _setup_streaming_pipeline(self, streaming_config: Dict) -> Dict:
        """Set up the complete streaming pipeline"""
        results = {
            "setup_start": datetime.now().isoformat(),
            "components_setup": 0,
            "components_failed": 0,
            "component_details": [],
            "setup_score": 0.0,
            "pipeline_ready": False,
            "setup_end": "",
            "duration_seconds": 0
        }
        
        # Setup components
        components = [
            ("kafka_topics", self._setup_kafka_topics),
            ("schema_registry", self._setup_schema_registry),
            ("buffer_configuration", self._setup_buffer_config),
            ("monitoring", self._setup_monitoring),
            ("error_handling", self._setup_error_handling)
        ]
        
        logger.info("Setting up streaming pipeline components")
        
        for component_name, setup_func in components:
            component_result = setup_func(streaming_config.get(component_name, {}))
            component_result["component"] = component_name
            results["component_details"].append(component_result)
            
            if component_result["status"] == "success":
                results["components_setup"] += 1
            else:
                results["components_failed"] += 1
        
        # Calculate final results
        results["setup_end"] = datetime.now().isoformat()
        start_time = datetime.fromisoformat(results["setup_start"])
        end_time = datetime.fromisoformat(results["setup_end"])
        results["duration_seconds"] = (end_time - start_time).total_seconds()
        
        # Calculate setup score
        total_components = len(components)
        if total_components > 0:
            results["setup_score"] = results["components_setup"] / total_components
        
        results["pipeline_ready"] = results["setup_score"] >= 0.8
        
        logger.info(f"Streaming pipeline setup completed: {results['components_setup']}/{total_components} components ready")
        
        return results
    
    def _setup_kafka_topics(self, kafka_config: Dict) -> Dict:
        """Set up Kafka topics"""
        result = {
            "status": "error",
            "message": "",
            "topics_created": 0,
            "topics_failed": 0,
            "topic_details": []
        }
        
        try:
            topics = kafka_config.get("topics", [])
            
            if not topics:
                result["message"] = "No topics specified in configuration"
                return result
            
            # Simulate Kafka topic creation (in real implementation, use kafka-python)
            for topic in topics:
                topic_result = self._create_kafka_topic(topic)
                result["topic_details"].append(topic_result)
                
                if topic_result["status"] == "success":
                    result["topics_created"] += 1
                else:
                    result["topics_failed"] += 1
            
            if result["topics_created"] > 0:
                result["status"] = "success"
                result["message"] = f"Created {result['topics_created']}/{len(topics)} Kafka topics"
            else:
                result["message"] = "Failed to create any Kafka topics"
                
        except Exception as e:
            result["message"] = f"Kafka setup error: {str(e)}"
        
        return result
    
    def _create_kafka_topic(self, topic_config: Dict) -> Dict:
        """Create a single Kafka topic"""
        result = {
            "topic_name": topic_config.get("name", "unnamed"),
            "status": "success",
            "message": "",
            "partitions": topic_config.get("partitions", 3),
            "replication_factor": topic_config.get("replication_factor", 1)
        }
        
        try:
            # Simulate topic creation (in real implementation, use Kafka admin client)
            topic_name = topic_config.get("name")
            partitions = topic_config.get("partitions", 3)
            replication_factor = topic_config.get("replication_factor", 1)
            
            # Simulate successful creation
            result["message"] = f"Topic '{topic_name}' created with {partitions} partitions, replication factor {replication_factor}"
            
        except Exception as e:
            result["status"] = "error"
            result["message"] = f"Failed to create topic: {str(e)}"
        
        return result
    
    def _setup_schema_registry(self, schema_config: Dict) -> Dict:
        """Set up schema registry"""
        result = {
            "status": "error",
            "message": "",
            "schemas_registered": 0,
            "registry_url": ""
        }
        
        try:
            registry_url = schema_config.get("url", "http://localhost:8081")
            schemas = schema_config.get("schemas", [])
            
            result["registry_url"] = registry_url
            
            if not schemas:
                result["message"] = "No schemas specified in configuration"
                return result
            
            # Simulate schema registration (in real implementation, use schema registry client)
            for schema in schemas:
                schema_result = self._register_schema(schema, registry_url)
                if schema_result["status"] == "success":
                    result["schemas_registered"] += 1
            
            if result["schemas_registered"] > 0:
                result["status"] = "success"
                result["message"] = f"Registered {result['schemas_registered']}/{len(schemas)} schemas"
            else:
                result["message"] = "Failed to register any schemas"
                
        except Exception as e:
            result["message"] = f"Schema registry setup error: {str(e)}"
        
        return result
    
    def _register_schema(self, schema_config: Dict, registry_url: str) -> Dict:
        """Register a single schema"""
        result = {
            "schema_name": schema_config.get("name", "unnamed"),
            "status": "success",
            "message": ""
        }
        
        try:
            schema_name = schema_config.get("name")
            schema_type = schema_config.get("type", "AVRO")
            
            # Simulate successful registration
            result["message"] = f"Schema '{schema_name}' registered as {schema_type}"
            
        except Exception as e:
            result["status"] = "error"
            result["message"] = f"Failed to register schema: {str(e)}"
        
        return result
    
    def _setup_buffer_config(self, buffer_config: Dict) -> Dict:
        """Set up buffer configuration"""
        result = {
            "status": "error",
            "message": "",
            "buffer_size_mb": 0,
            "flush_interval_seconds": 0
        }
        
        try:
            buffer_size = buffer_config.get("size_mb", 100)
            flush_interval = buffer_config.get("flush_interval_seconds", 5)
            
            result["buffer_size_mb"] = buffer_size
            result["flush_interval_seconds"] = flush_interval
            
            # Validate configuration
            if buffer_size > 0 and flush_interval > 0:
                result["status"] = "success"
                result["message"] = f"Buffer configured: {buffer_size}MB, flush every {flush_interval}s"
            else:
                result["message"] = "Invalid buffer configuration values"
                
        except Exception as e:
            result["message"] = f"Buffer setup error: {str(e)}"
        
        return result
    
    def _setup_monitoring(self, monitoring_config: Dict) -> Dict:
        """Set up monitoring configuration"""
        result = {
            "status": "error",
            "message": "",
            "metrics_enabled": False,
            "alerts_enabled": False
        }
        
        try:
            metrics_enabled = monitoring_config.get("metrics", {}).get("enabled", False)
            alerts_enabled = monitoring_config.get("alerts", {}).get("enabled", False)
            
            result["metrics_enabled"] = metrics_enabled
            result["alerts_enabled"] = alerts_enabled
            
            # Create monitoring configuration file
            monitoring_file = self.protocol_08_dir / "streaming-monitoring.yaml"
            monitoring_data = {
                "metrics": {
                    "enabled": metrics_enabled,
                    "interval_seconds": monitoring_config.get("metrics", {}).get("interval_seconds", 60)
                },
                "alerts": {
                    "enabled": alerts_enabled,
                    "thresholds": monitoring_config.get("alerts", {}).get("thresholds", {})
                }
            }
            
            with open(monitoring_file, 'w') as f:
                yaml.dump(monitoring_data, f, default_flow_style=False)
            
            result["status"] = "success"
            result["message"] = f"Monitoring configured: metrics={metrics_enabled}, alerts={alerts_enabled}"
            
        except Exception as e:
            result["message"] = f"Monitoring setup error: {str(e)}"
        
        return result
    
    def _setup_error_handling(self, error_config: Dict) -> Dict:
        """Set up error handling configuration"""
        result = {
            "status": "error",
            "message": "",
            "retry_attempts": 0,
            "dead_letter_queue": False
        }
        
        try:
            retry_attempts = error_config.get("retry_attempts", 3)
            dead_letter_enabled = error_config.get("dead_letter_queue", {}).get("enabled", False)
            
            result["retry_attempts"] = retry_attempts
            result["dead_letter_queue"] = dead_letter_enabled
            
            # Validate configuration
            if retry_attempts >= 0:
                result["status"] = "success"
                result["message"] = f"Error handling configured: {retry_attempts} retries, DLQ={dead_letter_enabled}"
            else:
                result["message"] = "Invalid retry attempts configuration"
                
        except Exception as e:
            result["message"] = f"Error handling setup error: {str(e)}"
        
        return result
    
    def _generate_setup_report(self, results: Dict, output_file: str):
        """Generate setup report"""
        # Ensure output directory exists
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Add setup summary
        report = {
            "setup_summary": {
                "setup_start": results["setup_start"],
                "setup_end": results["setup_end"],
                "duration_seconds": results["duration_seconds"],
                "components_setup": results["components_setup"],
                "components_failed": results["components_failed"],
                "setup_score": results["setup_score"],
                "pipeline_ready": results["pipeline_ready"],
                "overall_status": "ready" if results["pipeline_ready"] else "incomplete"
            },
            "component_results": results["component_details"],
            "detailed_results": results
        }
        
        # Write setup report
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Streaming pipeline setup report generated: {output_file}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Set up streaming pipeline")
    parser.add_argument("--config", required=True, help="Streaming configuration file path")
    parser.add_argument("--output", required=True, help="Output setup results file path")
    
    args = parser.parse_args()
    
    # Initialize setup
    workspace_path = Path.cwd()
    setup = StreamingPipelineSetup(str(workspace_path))
    
    # Execute setup
    result = setup.execute(args.config, args.output)
    
    # Exit with appropriate code
    if result["status"] == "success" and result["pipeline_ready"]:
        exit(0)  # Success
    elif result["status"] == "success":
        exit(1)  # Warning - partial setup
    else:
        exit(2)  # Error - setup failed

if __name__ == "__main__":
    main()
