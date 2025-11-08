#!/usr/bin/env python3
"""
Script: validate_data_sources.py
Protocol: 08-ai-data-collection-ingestion
Purpose: Validate data source connections and accessibility
Author: AI Workflow System
Created: 2025-11-08
"""

import json
import logging
import argparse
import requests
import sqlite3
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataSourceValidator:
    """Main class for data source validation"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts"
        self.protocol_08_dir = self.artifacts_dir / "protocol-08-ai-data-collection-ingestion"
        
    def execute(self, config_file: str, output_file: str) -> Dict:
        """
        Main execution method
        
        Args:
            config_file: Path to source configuration file
            output_file: Path for validation report
            
        Returns:
            Dict: Execution results with status and validation
        """
        try:
            # Load source configuration
            config = self._load_config(config_file)
            
            # Validate all data sources
            results = self._validate_all_sources(config)
            
            # Generate validation report
            self._generate_report(results, output_file)
            
            return {
                "status": "success",
                "results": results,
                "connectivity_score": results.get("connectivity_score", 0.0),
                "all_sources_accessible": results.get("all_sources_accessible", False)
            }
            
        except Exception as e:
            logger.error(f"Validation failed: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "connectivity_score": 0.0,
                "all_sources_accessible": False
            }
    
    def _load_config(self, config_file: str) -> Dict:
        """Load source configuration from JSON file"""
        config_path = Path(config_file)
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_file}")
        
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def _validate_all_sources(self, config: Dict) -> Dict:
        """Validate all configured data sources"""
        results = {
            "total_sources": 0,
            "successful_connections": 0,
            "failed_connections": 0,
            "source_details": [],
            "all_sources_accessible": True,
            "connectivity_score": 0.0
        }
        
        sources = config.get("data_sources", [])
        results["total_sources"] = len(sources)
        
        for source in sources:
            validation_result = self._validate_single_source(source)
            results["source_details"].append(validation_result)
            
            if validation_result["status"] == "success":
                results["successful_connections"] += 1
            else:
                results["failed_connections"] += 1
                results["all_sources_accessible"] = False
        
        # Calculate connectivity score
        if results["total_sources"] > 0:
            results["connectivity_score"] = results["successful_connections"] / results["total_sources"]
        
        return results
    
    def _validate_single_source(self, source: Dict) -> Dict:
        """Validate a single data source connection"""
        source_type = source.get("type", "unknown")
        source_name = source.get("name", "unnamed")
        
        result = {
            "name": source_name,
            "type": source_type,
            "status": "error",
            "message": "",
            "response_time_ms": 0,
            "timestamp": ""
        }
        
        try:
            if source_type == "api":
                result.update(self._validate_api_source(source))
            elif source_type == "database":
                result.update(self._validate_database_source(source))
            elif source_type == "file":
                result.update(self._validate_file_source(source))
            else:
                result["message"] = f"Unsupported source type: {source_type}"
                
        except Exception as e:
            result["message"] = f"Validation error: {str(e)}"
        
        return result
    
    def _validate_api_source(self, source: Dict) -> Dict:
        """Validate API data source"""
        import time
        start_time = time.time()
        
        url = source.get("url")
        headers = source.get("headers", {})
        auth = source.get("auth", {})
        
        try:
            # Make test request
            response = requests.get(url, headers=headers, timeout=30)
            response_time = (time.time() - start_time) * 1000
            
            if response.status_code == 200:
                return {
                    "status": "success",
                    "message": f"API accessible (Status: {response.status_code})",
                    "response_time_ms": round(response_time, 2),
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                }
            else:
                return {
                    "status": "error",
                    "message": f"API returned status {response.status_code}",
                    "response_time_ms": round(response_time, 2),
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "message": f"API connection failed: {str(e)}",
                "response_time_ms": round((time.time() - start_time) * 1000, 2),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
    
    def _validate_database_source(self, source: Dict) -> Dict:
        """Validate database data source"""
        import time
        start_time = time.time()
        
        connection_string = source.get("connection_string")
        query = source.get("test_query", "SELECT 1")
        
        try:
            conn = sqlite3.connect(connection_string)
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            conn.close()
            
            response_time = (time.time() - start_time) * 1000
            return {
                "status": "success",
                "message": f"Database connection successful (Test query: {query})",
                "response_time_ms": round(response_time, 2),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"Database connection failed: {str(e)}",
                "response_time_ms": round((time.time() - start_time) * 1000, 2),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
    
    def _validate_file_source(self, source: Dict) -> Dict:
        """Validate file data source"""
        import time
        start_time = time.time()
        
        file_path = Path(source.get("path"))
        
        try:
            if file_path.exists() and file_path.is_file():
                size_mb = file_path.stat().st_size / (1024 * 1024)
                response_time = (time.time() - start_time) * 1000
                
                return {
                    "status": "success",
                    "message": f"File accessible (Size: {size_mb:.2f} MB)",
                    "response_time_ms": round(response_time, 2),
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                }
            else:
                return {
                    "status": "error",
                    "message": f"File not found: {file_path}",
                    "response_time_ms": round((time.time() - start_time) * 1000, 2),
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                
        except Exception as e:
            return {
                "status": "error",
                "message": f"File access error: {str(e)}",
                "response_time_ms": round((time.time() - start_time) * 1000, 2),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
    
    def _generate_report(self, results: Dict, output_file: str):
        """Generate validation report"""
        # Ensure output directory exists
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Add summary
        report = {
            "validation_summary": {
                "total_sources": results["total_sources"],
                "successful_connections": results["successful_connections"],
                "failed_connections": results["failed_connections"],
                "connectivity_score": results["connectivity_score"],
                "all_sources_accessible": results["all_sources_accessible"],
                "validation_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            },
            "detailed_results": results
        }
        
        # Write report
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Validation report generated: {output_file}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Validate data source connections")
    parser.add_argument("--config", required=True, help="Source configuration file path")
    parser.add_argument("--output", required=True, help="Output validation report file path")
    
    args = parser.parse_args()
    
    # Initialize validator
    workspace_path = Path.cwd()
    validator = DataSourceValidator(str(workspace_path))
    
    # Execute validation
    result = validator.execute(args.config, args.output)
    
    # Exit with appropriate code
    if result["status"] == "success" and result["all_sources_accessible"]:
        exit(0)  # Success
    elif result["status"] == "success":
        exit(1)  # Warning - some sources failed
    else:
        exit(2)  # Error - validation failed

if __name__ == "__main__":
    main()
