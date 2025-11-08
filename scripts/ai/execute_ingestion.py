#!/usr/bin/env python3
"""
Script: execute_ingestion.py
Protocol: 08-ai-data-collection-ingestion
Purpose: Execute data ingestion from configured sources
Author: AI Workflow System
Created: 2025-11-08
"""

import json
import logging
import argparse
import yaml
import pandas as pd
import sqlite3
import requests
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataIngestionExecutor:
    """Main class for data ingestion execution"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts"
        self.protocol_08_dir = self.artifacts_dir / "protocol-08-ai-data-collection-ingestion"
        self.raw_data_dir = self.protocol_08_dir / "raw-data"
        
        # Ensure directories exist
        self.protocol_08_dir.mkdir(parents=True, exist_ok=True)
        self.raw_data_dir.mkdir(parents=True, exist_ok=True)
        
    def execute(self, config_file: str, output_file: str) -> Dict:
        """
        Main execution method
        
        Args:
            config_file: Path to ETL configuration file
            output_file: Path for execution log file
            
        Returns:
            Dict: Execution results with status and metrics
        """
        try:
            # Load ETL configuration
            etl_config = self._load_config(config_file)
            
            # Execute ingestion
            results = self._execute_ingestion_pipeline(etl_config)
            
            # Generate execution log
            self._generate_execution_log(results, output_file)
            
            return {
                "status": "success",
                "results": results,
                "ingestion_score": results.get("ingestion_score", 0.0),
                "data_volume_mb": results.get("total_data_volume_mb", 0.0),
                "records_processed": results.get("total_records_processed", 0)
            }
            
        except Exception as e:
            logger.error(f"Ingestion failed: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "ingestion_score": 0.0,
                "data_volume_mb": 0.0,
                "records_processed": 0
            }
    
    def _load_config(self, config_file: str) -> Dict:
        """Load ETL configuration from YAML file"""
        config_path = Path(config_file)
        if not config_path.exists():
            raise FileNotFoundError(f"ETL configuration file not found: {config_file}")
        
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def _execute_ingestion_pipeline(self, etl_config: Dict) -> Dict:
        """Execute the complete ingestion pipeline"""
        results = {
            "execution_start": datetime.now().isoformat(),
            "sources_processed": 0,
            "sources_failed": 0,
            "total_records_processed": 0,
            "total_data_volume_mb": 0.0,
            "source_details": [],
            "ingestion_score": 0.0,
            "execution_end": "",
            "duration_seconds": 0
        }
        
        sources = etl_config.get("sources", [])
        extraction_type = etl_config.get("extraction", {}).get("type", "batch")
        
        logger.info(f"Starting {extraction_type} ingestion for {len(sources)} sources")
        
        for source in sources:
            source_result = self._process_single_source(source, extraction_type)
            results["source_details"].append(source_result)
            
            if source_result["status"] == "success":
                results["sources_processed"] += 1
                results["total_records_processed"] += source_result.get("records_processed", 0)
                results["total_data_volume_mb"] += source_result.get("data_volume_mb", 0.0)
            else:
                results["sources_failed"] += 1
        
        # Calculate final metrics
        results["execution_end"] = datetime.now().isoformat()
        start_time = datetime.fromisoformat(results["execution_start"])
        end_time = datetime.fromisoformat(results["execution_end"])
        results["duration_seconds"] = (end_time - start_time).total_seconds()
        
        # Calculate ingestion score
        total_sources = len(sources)
        if total_sources > 0:
            results["ingestion_score"] = results["sources_processed"] / total_sources
        
        logger.info(f"Ingestion completed: {results['sources_processed']}/{total_sources} sources successful")
        
        return results
    
    def _process_single_source(self, source: Dict, extraction_type: str) -> Dict:
        """Process a single data source"""
        source_name = source.get("name", "unnamed")
        source_type = source.get("type", "unknown")
        
        result = {
            "name": source_name,
            "type": source_type,
            "status": "error",
            "message": "",
            "records_processed": 0,
            "data_volume_mb": 0.0,
            "output_file": "",
            "processing_time_seconds": 0,
            "timestamp": datetime.now().isoformat()
        }
        
        start_time = time.time()
        
        try:
            if source_type == "api":
                result.update(self._process_api_source(source))
            elif source_type == "database":
                result.update(self._process_database_source(source))
            elif source_type == "file":
                result.update(self._process_file_source(source))
            else:
                result["message"] = f"Unsupported source type: {source_type}"
                
        except Exception as e:
            result["message"] = f"Processing error: {str(e)}"
        
        result["processing_time_seconds"] = round(time.time() - start_time, 2)
        return result
    
    def _process_api_source(self, source: Dict) -> Dict:
        """Process API data source"""
        url = source.get("url")
        headers = source.get("headers", {})
        params = source.get("params", {})
        output_format = source.get("output_format", "json")
        
        # Make API request
        response = requests.get(url, headers=headers, params=params, timeout=300)
        response.raise_for_status()
        
        # Process data based on format
        if output_format == "json":
            data = response.json()
            df = pd.DataFrame(data)
        else:
            # Handle other formats (CSV, XML, etc.)
            df = pd.DataFrame()  # Placeholder
        
        # Save to parquet file
        source_name = source.get("name", "api_source").replace(" ", "_").lower()
        output_file = self.raw_data_dir / f"{source_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        df.to_parquet(output_file, index=False)
        
        # Calculate metrics
        records_processed = len(df)
        data_volume_mb = output_file.stat().st_size / (1024 * 1024)
        
        return {
            "status": "success",
            "message": f"API data ingested successfully",
            "records_processed": records_processed,
            "data_volume_mb": round(data_volume_mb, 2),
            "output_file": str(output_file)
        }
    
    def _process_database_source(self, source: Dict) -> Dict:
        """Process database data source"""
        connection_string = source.get("connection_string")
        query = source.get("query", "SELECT * FROM data LIMIT 1000")
        
        # Connect and query database
        conn = sqlite3.connect(connection_string)
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        # Save to parquet file
        source_name = source.get("name", "db_source").replace(" ", "_").lower()
        output_file = self.raw_data_dir / f"{source_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        df.to_parquet(output_file, index=False)
        
        # Calculate metrics
        records_processed = len(df)
        data_volume_mb = output_file.stat().st_size / (1024 * 1024)
        
        return {
            "status": "success",
            "message": f"Database data ingested successfully",
            "records_processed": records_processed,
            "data_volume_mb": round(data_volume_mb, 2),
            "output_file": str(output_file)
        }
    
    def _process_file_source(self, source: Dict) -> Dict:
        """Process file data source"""
        file_path = Path(source.get("path"))
        file_format = source.get("format", "csv")
        
        # Read file based on format
        if file_format == "csv":
            df = pd.read_csv(file_path)
        elif file_format == "json":
            df = pd.read_json(file_path)
        elif file_format == "parquet":
            df = pd.read_parquet(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")
        
        # Save to parquet file
        source_name = source.get("name", "file_source").replace(" ", "_").lower()
        output_file = self.raw_data_dir / f"{source_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.parquet"
        df.to_parquet(output_file, index=False)
        
        # Calculate metrics
        records_processed = len(df)
        data_volume_mb = output_file.stat().st_size / (1024 * 1024)
        
        return {
            "status": "success",
            "message": f"File data ingested successfully",
            "records_processed": records_processed,
            "data_volume_mb": round(data_volume_mb, 2),
            "output_file": str(output_file)
        }
    
    def _generate_execution_log(self, results: Dict, output_file: str):
        """Generate execution log"""
        # Ensure output directory exists
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Add execution summary
        log = {
            "execution_summary": {
                "execution_start": results["execution_start"],
                "execution_end": results["execution_end"],
                "duration_seconds": results["duration_seconds"],
                "total_sources": results["sources_processed"] + results["sources_failed"],
                "sources_processed": results["sources_processed"],
                "sources_failed": results["sources_failed"],
                "total_records_processed": results["total_records_processed"],
                "total_data_volume_mb": round(results["total_data_volume_mb"], 2),
                "ingestion_score": results["ingestion_score"],
                "status": "success" if results["ingestion_score"] >= 0.9 else "partial"
            },
            "detailed_results": results
        }
        
        # Write execution log
        with open(output_file, 'w') as f:
            json.dump(log, f, indent=2)
        
        logger.info(f"Ingestion execution log generated: {output_file}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Execute data ingestion")
    parser.add_argument("--config", required=True, help="ETL configuration file path")
    parser.add_argument("--output", required=True, help="Output execution log file path")
    
    args = parser.parse_args()
    
    # Initialize executor
    workspace_path = Path.cwd()
    executor = DataIngestionExecutor(str(workspace_path))
    
    # Execute ingestion
    result = executor.execute(args.config, args.output)
    
    # Exit with appropriate code
    if result["status"] == "success" and result["ingestion_score"] >= 0.9:
        exit(0)  # Success
    elif result["status"] == "success":
        exit(1)  # Warning - partial success
    else:
        exit(2)  # Error - ingestion failed

if __name__ == "__main__":
    main()
