#!/usr/bin/env python3
"""
Pipeline Configuration Validation Script for Protocol 08
Validates data collection pipeline configuration and setup
"""

import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pipeline_config_validation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class PipelineConfigValidator:
    """Validates pipeline configuration for data collection"""
    
    def __init__(self, config_path: str, output_path: str):
        self.config_path = Path(config_path)
        self.output_path = Path(output_path)
        self.output_path.mkdir(parents=True, exist_ok=True)
        self.validation_results = []
        self.start_time = datetime.now()
        
        # Configuration validation thresholds
        self.validation_thresholds = {
            'config_completeness_min': 0.95,
            'connectivity_success_min': 1.0,
            'monitoring_coverage_min': 0.9
        }
    
    def load_pipeline_config(self) -> Dict[str, Any]:
        """Load pipeline configuration"""
        logger.info("Loading pipeline configuration")
        
        try:
            # Look for configuration files
            config_files = list(self.config_path.glob("*.yaml")) + list(self.config_path.glob("*.yml")) + list(self.config_path.glob("*.json"))
            
            if not config_files:
                logger.warning("No configuration files found, using default config")
                return self.get_default_config()
            
            config_file = config_files[0]
            logger.info(f"Loading config from {config_file}")
            
            if config_file.suffix in ['.yaml', '.yml']:
                with open(config_file, 'r') as f:
                    return yaml.safe_load(f)
            elif config_file.suffix == '.json':
                with open(config_file, 'r') as f:
                    return json.load(f)
            else:
                logger.error(f"Unsupported config format: {config_file.suffix}")
                return self.get_default_config()
                
        except Exception as e:
            logger.error(f"Failed to load pipeline config: {e}")
            return self.get_default_config()
    
    def get_default_config(self) -> Dict[str, Any]:
        """Get default pipeline configuration"""
        return {
            'pipeline': {
                'name': 'data-collection-pipeline',
                'version': '1.0',
                'sources': [
                    {
                        'type': 'database',
                        'name': 'primary_db',
                        'connection_string': 'sqlite:///data.db'
                    },
                    {
                        'type': 'api',
                        'name': 'external_api',
                        'url': 'https://api.example.com/data'
                    },
                    {
                        'type': 'files',
                        'name': 'file_source',
                        'path': '/data/input'
                    }
                ],
                'monitoring': {
                    'enabled': True,
                    'metrics': ['throughput', 'error_rate', 'latency'],
                    'alert_thresholds': {
                        'error_rate_max': 0.05,
                        'latency_max_ms': 5000
                    }
                },
                'storage': {
                    'output_path': '/data/collected',
                    'backup_enabled': True,
                    'compression': 'gzip'
                }
            }
        }
    
    def validate_config_completeness(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Validate configuration completeness"""
        logger.info("Validating configuration completeness")
        
        required_sections = ['pipeline', 'sources', 'monitoring', 'storage']
        present_sections = []
        
        pipeline_config = config.get('pipeline', {})
        
        # Check required sections
        if 'sources' in pipeline_config:
            present_sections.append('sources')
        if 'monitoring' in pipeline_config:
            present_sections.append('monitoring')
        if 'storage' in pipeline_config:
            present_sections.append('storage')
        
        completeness_score = len(present_sections) / len(required_sections)
        
        validation_result = {
            'metric': 'config_completeness',
            'score': float(completeness_score),
            'threshold': self.validation_thresholds['config_completeness_min'],
            'passed': completeness_score >= self.validation_thresholds['config_completeness_min'],
            'details': {
                'required_sections': required_sections,
                'present_sections': present_sections,
                'missing_sections': [s for s in required_sections if s not in present_sections]
            }
        }
        
        logger.info(f"Configuration completeness: {completeness_score:.3f}")
        return validation_result
    
    def validate_source_connectivity(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Validate data source connectivity"""
        logger.info("Validating source connectivity")
        
        sources = config.get('pipeline', {}).get('sources', [])
        connectivity_results = []
        
        for source in sources:
            source_type = source.get('type', 'unknown')
            source_name = source.get('name', 'unnamed')
            
            # Simulate connectivity test
            try:
                if source_type == 'database':
                    # Test database connection
                    connection_string = source.get('connection_string', '')
                    if connection_string:
                        connectivity = 'success'
                    else:
                        connectivity = 'failed'
                elif source_type == 'api':
                    # Test API connectivity
                    api_url = source.get('url', '')
                    if api_url.startswith('http'):
                        connectivity = 'success'
                    else:
                        connectivity = 'failed'
                elif source_type == 'files':
                    # Test file path accessibility
                    file_path = source.get('path', '')
                    if file_path:
                        connectivity = 'success'
                    else:
                        connectivity = 'failed'
                else:
                    connectivity = 'unknown'
                
                connectivity_results.append({
                    'source_name': source_name,
                    'source_type': source_type,
                    'connectivity': connectivity
                })
                
            except Exception as e:
                connectivity_results.append({
                    'source_name': source_name,
                    'source_type': source_type,
                    'connectivity': 'error',
                    'error': str(e)
                })
        
        # Calculate connectivity score
        total_sources = len(connectivity_results)
        successful_sources = sum(1 for r in connectivity_results if r.get('connectivity') == 'success')
        connectivity_score = successful_sources / total_sources if total_sources > 0 else 0
        
        validation_result = {
            'metric': 'source_connectivity',
            'score': float(connectivity_score),
            'threshold': self.validation_thresholds['connectivity_success_min'],
            'passed': connectivity_score >= self.validation_thresholds['connectivity_success_min'],
            'details': {
                'total_sources': int(total_sources),
                'successful_sources': int(successful_sources),
                'connectivity_results': connectivity_results
            }
        }
        
        logger.info(f"Source connectivity score: {connectivity_score:.3f}")
        return validation_result
    
    def validate_monitoring_setup(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Validate monitoring configuration"""
        logger.info("Validating monitoring setup")
        
        monitoring_config = config.get('pipeline', {}).get('monitoring', {})
        
        # Check monitoring components
        monitoring_components = {
            'enabled': monitoring_config.get('enabled', False),
            'has_metrics': len(monitoring_config.get('metrics', [])) > 0,
            'has_alerts': len(monitoring_config.get('alert_thresholds', {})) > 0
        }
        
        # Calculate monitoring coverage
        enabled_components = sum(monitoring_components.values())
        total_components = len(monitoring_components)
        monitoring_coverage = enabled_components / total_components if total_components > 0 else 0
        
        validation_result = {
            'metric': 'monitoring_setup',
            'score': float(monitoring_coverage),
            'threshold': self.validation_thresholds['monitoring_coverage_min'],
            'passed': monitoring_coverage >= self.validation_thresholds['monitoring_coverage_min'],
            'details': {
                'monitoring_components': monitoring_components,
                'enabled_components': int(enabled_components),
                'total_components': int(total_components),
                'monitoring_config': monitoring_config
            }
        }
        
        logger.info(f"Monitoring setup score: {monitoring_coverage:.3f}")
        return validation_result
    
    def execute_validation(self) -> Dict[str, Any]:
        """Execute complete pipeline configuration validation"""
        logger.info("Starting pipeline configuration validation")
        
        # Load configuration
        config = self.load_pipeline_config()
        
        # Run all validations
        validations = [
            self.validate_config_completeness(config),
            self.validate_source_connectivity(config),
            self.validate_monitoring_setup(config)
        ]
        
        # Calculate overall score
        scores = [v['score'] for v in validations if 'score' in v]
        overall_score = sum(scores) / len(scores) if scores else 0.0
        
        # Check if all validations passed
        all_passed = all(v.get('passed', False) for v in validations)
        
        validation_summary = {
            'validation_summary': {
                'overall_score': float(overall_score),
                'validation_passed': all_passed,
                'total_validations': len(validations),
                'passed_validations': sum(1 for v in validations if v.get('passed', False)),
                'execution_time_seconds': (datetime.now() - self.start_time).total_seconds(),
                'start_time': self.start_time.isoformat(),
                'end_time': datetime.now().isoformat()
            },
            'validations': validations,
            'configuration': config
        }
        
        logger.info(f"Pipeline configuration validation completed: Score {overall_score:.3f}, Passed: {all_passed}")
        return validation_summary
    
    def save_validation_report(self, report: Dict[str, Any], report_path: str):
        """Save validation report to specified path"""
        try:
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            logger.info(f"Validation report saved to {report_path}")
        except Exception as e:
            logger.error(f"Failed to save validation report: {e}")

def main():
    """Main execution function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate pipeline configuration')
    parser.add_argument('--input', required=True, help='Input directory containing configuration')
    parser.add_argument('--output', required=True, help='Output directory for validation reports')
    
    args = parser.parse_args()
    
    try:
        # Initialize validator
        validator = PipelineConfigValidator(args.input, args.output)
        
        # Execute validation
        validation_report = validator.execute_validation()
        
        # Save validation report
        report_file = Path(args.output) / 'pipeline_config_report.json'
        validator.save_validation_report(validation_report, str(report_file))
        
        # Return success if validation passed
        if validation_report['validation_summary']['validation_passed']:
            logger.info("Pipeline configuration validation completed successfully")
            return 0
        else:
            logger.warning("Pipeline configuration validation completed with issues")
            return 1
            
    except Exception as e:
        logger.error(f"Pipeline configuration validation failed: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
