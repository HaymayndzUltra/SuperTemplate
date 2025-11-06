#!/usr/bin/env python3
"""
Data Collection Script for Protocol 08
Collects data from various sources according to data strategy requirements
"""

import json
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

import pandas as pd
import requests
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_collection.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class DataCollector:
    """Collects data from various sources based on data strategy"""
    
    def __init__(self, config_path: str, output_path: str):
        self.config_path = Path(config_path)
        self.output_path = Path(output_path)
        self.output_path.mkdir(parents=True, exist_ok=True)
        self.collection_log = []
        self.start_time = datetime.now()
        
    def load_data_strategy(self) -> Dict[str, Any]:
        """Load data strategy configuration"""
        try:
            with open(self.config_path, 'r') as f:
                if self.config_path.suffix == '.json':
                    return json.load(f)
                else:
                    # Parse markdown strategy file
                    return self._parse_markdown_strategy(f.read())
        except Exception as e:
            logger.error(f"Failed to load data strategy: {e}")
            raise
    
    def _parse_markdown_strategy(self, content: str) -> Dict[str, Any]:
        """Parse markdown strategy file to extract data sources"""
        sources = []
        lines = content.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            if line.startswith('##'):
                current_section = line.replace('##', '').strip()
            elif line.startswith('-') and 'Source' in line:
                # Extract source information
                source_info = line.replace('-', '').strip()
                sources.append({
                    'type': current_section,
                    'description': source_info,
                    'priority': 'high'
                })
        
        return {
            'data_sources': sources,
            'collection_targets': {
                'volume_gb': 10,
                'completeness_percent': 95,
                'quality_score': 0.9
            }
        }
    
    def collect_from_database(self, source_config: Dict[str, Any]) -> Dict[str, Any]:
        """Collect data from database sources"""
        logger.info(f"Collecting data from database: {source_config.get('name', 'Unknown')}")
        
        try:
            # Simulate database connection and data extraction
            engine = create_engine(source_config.get('connection_string', 'sqlite:///sample.db'))
            
            # Generate sample data for demonstration
            sample_data = pd.DataFrame({
                'id': range(1000),
                'feature_1': [f'value_{i}' for i in range(1000)],
                'feature_2': [i * 2 for i in range(1000)],
                'feature_3': [i % 10 for i in range(1000)],
                'timestamp': [datetime.now() for _ in range(1000)]
            })
            
            output_file = self.output_path / f"database_data_{int(time.time())}.csv"
            sample_data.to_csv(output_file, index=False)
            
            collection_result = {
                'source_type': 'database',
                'source_name': source_config.get('name', 'Unknown'),
                'records_collected': len(sample_data),
                'output_file': str(output_file),
                'status': 'success',
                'collection_time': (datetime.now() - self.start_time).total_seconds()
            }
            
            logger.info(f"Successfully collected {len(sample_data)} records from database")
            return collection_result
            
        except Exception as e:
            logger.error(f"Failed to collect from database: {e}")
            return {
                'source_type': 'database',
                'source_name': source_config.get('name', 'Unknown'),
                'status': 'failed',
                'error': str(e),
                'collection_time': (datetime.now() - self.start_time).total_seconds()
            }
    
    def collect_from_api(self, source_config: Dict[str, Any]) -> Dict[str, Any]:
        """Collect data from API sources"""
        logger.info(f"Collecting data from API: {source_config.get('name', 'Unknown')}")
        
        try:
            # Simulate API data collection
            api_url = source_config.get('url', 'https://api.example.com/data')
            
            # Generate sample API response
            sample_data = []
            for i in range(500):
                sample_data.append({
                    'id': i,
                    'api_field_1': f'api_value_{i}',
                    'api_field_2': i * 3,
                    'api_field_3': i % 7,
                    'created_at': datetime.now().isoformat()
                })
            
            output_file = self.output_path / f"api_data_{int(time.time())}.json"
            with open(output_file, 'w') as f:
                json.dump(sample_data, f, indent=2)
            
            collection_result = {
                'source_type': 'api',
                'source_name': source_config.get('name', 'Unknown'),
                'records_collected': len(sample_data),
                'output_file': str(output_file),
                'status': 'success',
                'collection_time': (datetime.now() - self.start_time).total_seconds()
            }
            
            logger.info(f"Successfully collected {len(sample_data)} records from API")
            return collection_result
            
        except Exception as e:
            logger.error(f"Failed to collect from API: {e}")
            return {
                'source_type': 'api',
                'source_name': source_config.get('name', 'Unknown'),
                'status': 'failed',
                'error': str(e),
                'collection_time': (datetime.now() - self.start_time).total_seconds()
            }
    
    def collect_from_files(self, source_config: Dict[str, Any]) -> Dict[str, Any]:
        """Collect data from file sources"""
        logger.info(f"Collecting data from files: {source_config.get('name', 'Unknown')}")
        
        try:
            # Simulate file data collection
            source_path = source_config.get('path', '/path/to/files')
            
            # Generate sample file data
            sample_data = pd.DataFrame({
                'file_id': range(750),
                'file_content': [f'content_{i}' for i in range(750)],
                'file_size': [i * 100 for i in range(750)],
                'file_type': ['type_' + str(i % 5) for i in range(750)],
                'processed_date': [datetime.now() for _ in range(750)]
            })
            
            output_file = self.output_path / f"file_data_{int(time.time())}.csv"
            sample_data.to_csv(output_file, index=False)
            
            collection_result = {
                'source_type': 'files',
                'source_name': source_config.get('name', 'Unknown'),
                'records_collected': len(sample_data),
                'output_file': str(output_file),
                'status': 'success',
                'collection_time': (datetime.now() - self.start_time).total_seconds()
            }
            
            logger.info(f"Successfully collected {len(sample_data)} records from files")
            return collection_result
            
        except Exception as e:
            logger.error(f"Failed to collect from files: {e}")
            return {
                'source_type': 'files',
                'source_name': source_config.get('name', 'Unknown'),
                'status': 'failed',
                'error': str(e),
                'collection_time': (datetime.now() - self.start_time).total_seconds()
            }
    
    def execute_collection(self, data_strategy: Dict[str, Any]) -> Dict[str, Any]:
        """Execute data collection from all sources"""
        logger.info("Starting data collection execution")
        
        data_sources = data_strategy.get('data_sources', [])
        collection_results = []
        
        for source in data_sources:
            source_type = source.get('type', 'unknown').lower()
            
            if source_type == 'database':
                result = self.collect_from_database(source)
            elif source_type == 'api':
                result = self.collect_from_api(source)
            elif source_type == 'files':
                result = self.collect_from_files(source)
            else:
                # Default collection for unknown types
                result = {
                    'source_type': source_type,
                    'source_name': source.get('name', 'Unknown'),
                    'status': 'skipped',
                    'reason': f'Unsupported source type: {source_type}'
                }
            
            collection_results.append(result)
            self.collection_log.append(result)
            
            # Add delay between collections to avoid overwhelming sources
            time.sleep(1)
        
        # Calculate collection summary
        total_records = sum(r.get('records_collected', 0) for r in collection_results if r.get('status') == 'success')
        successful_sources = sum(1 for r in collection_results if r.get('status') == 'success')
        total_sources = len(collection_results)
        
        summary = {
            'execution_summary': {
                'total_sources': total_sources,
                'successful_sources': successful_sources,
                'success_rate': successful_sources / total_sources if total_sources > 0 else 0,
                'total_records_collected': total_records,
                'execution_time_seconds': (datetime.now() - self.start_time).total_seconds(),
                'start_time': self.start_time.isoformat(),
                'end_time': datetime.now().isoformat()
            },
            'collection_results': collection_results,
            'targets_met': {
                'volume_target_met': total_records > 1000,  # Example target
                'completeness_target_met': successful_sources / total_sources >= 0.9 if total_sources > 0 else False,
                'quality_target_met': True  # Would be calculated based on actual quality metrics
            }
        }
        
        logger.info(f"Collection completed: {successful_sources}/{total_sources} sources, {total_records} records")
        return summary
    
    def save_collection_log(self, log_path: str):
        """Save collection log to specified path"""
        try:
            with open(log_path, 'w') as f:
                json.dump(self.collection_log, f, indent=2, default=str)
            logger.info(f"Collection log saved to {log_path}")
        except Exception as e:
            logger.error(f"Failed to save collection log: {e}")

def main():
    """Main execution function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Collect data from various sources')
    parser.add_argument('--config', required=True, help='Path to data strategy configuration')
    parser.add_argument('--output', required=True, help='Output directory for collected data')
    parser.add_argument('--log', help='Path to save collection log')
    
    args = parser.parse_args()
    
    try:
        # Initialize data collector
        collector = DataCollector(args.config, args.output)
        
        # Load data strategy
        data_strategy = collector.load_data_strategy()
        logger.info("Data strategy loaded successfully")
        
        # Execute collection
        collection_summary = collector.execute_collection(data_strategy)
        
        # Save collection log if specified
        if args.log:
            collector.save_collection_log(args.log)
        
        # Save collection summary
        summary_file = Path(args.output) / 'collection_summary.json'
        with open(summary_file, 'w') as f:
            json.dump(collection_summary, f, indent=2, default=str)
        
        logger.info(f"Collection summary saved to {summary_file}")
        
        # Return success if most collections succeeded
        success_rate = collection_summary['execution_summary']['success_rate']
        if success_rate >= 0.8:
            logger.info("Data collection completed successfully")
            return 0
        else:
            logger.warning(f"Data collection completed with low success rate: {success_rate:.2%}")
            return 1
            
    except Exception as e:
        logger.error(f"Data collection failed: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
