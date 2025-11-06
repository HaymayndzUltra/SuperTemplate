#!/usr/bin/env python3
"""
Script: assess_data_availability.py
Protocol: 07-ai-data-strategy-planning
Purpose: Automatically assess data source availability and accessibility
Author: AI Workflow System
Created: 2025-01-06
"""

import json
import logging
from typing import Dict, List, Optional, Any
from pathlib import Path
from datetime import datetime
import time
import requests
from urllib.parse import urlparse
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataAvailabilityAssessor:
    """Assess data source availability and accessibility for ML projects"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts" / "protocol-07"
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        # Data source types and their assessment methods
        self.source_types = {
            'database': self._assess_database,
            'api': self._assess_api,
            'file_system': self._assess_file_system,
            'data_lake': self._assess_data_lake,
            'stream': self._assess_stream,
            'third_party': self._assess_third_party
        }
        
        # Scoring weights
        self.weights = {
            'accessibility': 0.4,
            'volume': 0.25,
            'type_coverage': 0.2,
            'freshness': 0.15
        }
    
    def execute(self, **kwargs) -> Dict:
        """
        Assess data availability across multiple sources
        
        Args:
            data_sources: List of data source configurations
            requirements: Data volume and type requirements
            access_credentials: Authentication credentials
            
        Returns:
            Dict: Availability assessment results
        """
        try:
            data_sources = kwargs.get('data_sources', [])
            requirements = kwargs.get('requirements', {})
            access_credentials = kwargs.get('access_credentials', {})
            
            # Assess each data source
            source_assessments = []
            for source in data_sources:
                assessment = self._assess_single_source(source, access_credentials)
                source_assessments.append(assessment)
            
            # Calculate overall availability scores
            overall_scores = self._calculate_overall_scores(source_assessments, requirements)
            
            # Identify issues and recommendations
            issues = self._identify_issues(source_assessments)
            recommendations = self._generate_recommendations(source_assessments, requirements)
            
            # Generate data source inventory
            inventory = self._create_inventory(source_assessments)
            
            result = {
                "availability_score": overall_scores['overall'],
                "accessibility_score": overall_scores['accessibility'],
                "volume_score": overall_scores['volume'],
                "type_score": overall_scores['type'],
                "freshness_score": overall_scores['freshness'],
                "accessible_sources": overall_scores['accessible_count'],
                "total_sources": len(data_sources),
                "volume_coverage": overall_scores['volume_coverage'],
                "type_coverage": overall_scores['type_coverage'],
                "accessibility_issues": issues['accessibility'],
                "volume_issues": issues['volume'],
                "recommendations": recommendations,
                "source_assessments": source_assessments,
                "data_inventory": inventory
            }
            
            # Generate evidence
            self._generate_evidence(result, kwargs)
            
            return {
                "status": "success",
                "result": result,
                "artifacts": self._list_artifacts()
            }
            
        except Exception as e:
            logger.error(f"Data availability assessment failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _assess_single_source(self, source: Dict, credentials: Dict) -> Dict:
        """Assess a single data source"""
        source_type = source.get('type', 'unknown')
        source_id = source.get('id', 'unknown')
        
        assessment = {
            'source_id': source_id,
            'type': source_type,
            'name': source.get('name', 'Unknown'),
            'accessible': False,
            'accessibility_score': 0.0,
            'volume_score': 0.0,
            'type_score': 0.0,
            'freshness_score': 0.0,
            'overall_score': 0.0,
            'issues': [],
            'sample_data': None,
            'metadata': {}
        }
        
        # Get assessment function for source type
        assessor = self.source_types.get(source_type, self._assess_generic)
        
        try:
            # Perform source-specific assessment
            source_result = assessor(source, credentials)
            assessment.update(source_result)
            
            # Calculate overall score for this source
            assessment['overall_score'] = (
                assessment['accessibility_score'] * self.weights['accessibility'] +
                assessment['volume_score'] * self.weights['volume'] +
                assessment['type_score'] * self.weights['type_coverage'] +
                assessment['freshness_score'] * self.weights['freshness']
            )
            
        except Exception as e:
            assessment['issues'].append(f"Assessment failed: {str(e)}")
            logger.error(f"Failed to assess source {source_id}: {e}")
        
        return assessment
    
    def _assess_database(self, source: Dict, credentials: Dict) -> Dict:
        """Assess database data source"""
        result = {
            'accessible': False,
            'accessibility_score': 0.0,
            'volume_score': 0.0,
            'type_score': 0.0,
            'freshness_score': 0.0,
            'issues': []
        }
        
        try:
            # Test database connection
            connection_string = source.get('connection_string')
            if not connection_string:
                result['issues'].append("Missing connection string")
                return result
            
            # Simulate connection test (in real implementation, use actual DB driver)
            connection_test = self._test_database_connection(connection_string, credentials)
            
            if connection_test['success']:
                result['accessible'] = True
                result['accessibility_score'] = 1.0
                
                # Assess volume
                table_info = connection_test.get('tables', [])
                total_rows = sum(table.get('row_count', 0) for table in table_info)
                result['volume_score'] = min(1.0, total_rows / 1000000)  # Normalize to 1M rows
                
                # Assess data types
                data_types = set()
                for table in table_info:
                    data_types.update(table.get('data_types', []))
                result['type_score'] = min(1.0, len(data_types) / 10)  # Normalize to 10 types
                
                # Assess freshness
                last_updated = connection_test.get('last_updated')
                if last_updated:
                    days_old = (datetime.now() - last_updated).days
                    result['freshness_score'] = max(0.0, 1.0 - (days_old / 365))  # Decay over year
                
                result['metadata'] = {
                    'tables': len(table_info),
                    'total_rows': total_rows,
                    'data_types': list(data_types),
                    'last_updated': last_updated.isoformat() if last_updated else None
                }
            else:
                result['issues'].append(connection_test.get('error', 'Connection failed'))
                
        except Exception as e:
            result['issues'].append(f"Database assessment error: {str(e)}")
        
        return result
    
    def _assess_api(self, source: Dict, credentials: Dict) -> Dict:
        """Assess API data source"""
        result = {
            'accessible': False,
            'accessibility_score': 0.0,
            'volume_score': 0.0,
            'type_score': 0.0,
            'freshness_score': 0.0,
            'issues': []
        }
        
        try:
            api_url = source.get('url')
            if not api_url:
                result['issues'].append("Missing API URL")
                return result
            
            # Test API accessibility
            api_test = self._test_api_accessibility(api_url, credentials)
            
            if api_test['success']:
                result['accessible'] = True
                result['accessibility_score'] = 1.0
                
                # Assess rate limits and volume
                rate_limit = api_test.get('rate_limit', 1000)  # requests per hour
                result['volume_score'] = min(1.0, rate_limit / 10000)  # Normalize to 10k/hour
                
                # Assess data types from API response
                sample_response = api_test.get('sample_response', {})
                data_types = self._infer_data_types_from_json(sample_response)
                result['type_score'] = min(1.0, len(data_types) / 8)  # Normalize to 8 types
                
                # Assess freshness
                last_updated = api_test.get('last_updated')
                if last_updated:
                    hours_old = (datetime.now() - last_updated).total_seconds() / 3600
                    result['freshness_score'] = max(0.0, 1.0 - (hours_old / 168))  # Decay over week
                
                result['metadata'] = {
                    'endpoint': api_url,
                    'rate_limit': rate_limit,
                    'data_types': list(data_types),
                    'response_format': api_test.get('format', 'json'),
                    'last_updated': last_updated.isoformat() if last_updated else None
                }
            else:
                result['issues'].append(api_test.get('error', 'API access failed'))
                
        except Exception as e:
            result['issues'].append(f"API assessment error: {str(e)}")
        
        return result
    
    def _assess_file_system(self, source: Dict, credentials: Dict) -> Dict:
        """Assess file system data source"""
        result = {
            'accessible': False,
            'accessibility_score': 0.0,
            'volume_score': 0.0,
            'type_score': 0.0,
            'freshness_score': 0.0,
            'issues': []
        }
        
        try:
            file_path = source.get('path')
            if not file_path:
                result['issues'].append("Missing file path")
                return result
            
            # Test file system access
            fs_test = self._test_file_system_access(file_path, credentials)
            
            if fs_test['success']:
                result['accessible'] = True
                result['accessibility_score'] = 1.0
                
                # Assess volume
                total_size = fs_test.get('total_size_mb', 0)
                result['volume_score'] = min(1.0, total_size / 10000)  # Normalize to 10GB
                
                # Assess file types
                file_types = fs_test.get('file_types', [])
                result['type_score'] = min(1.0, len(file_types) / 6)  # Normalize to 6 types
                
                # Assess freshness
                latest_file = fs_test.get('latest_file_date')
                if latest_file:
                    days_old = (datetime.now() - latest_file).days
                    result['freshness_score'] = max(0.0, 1.0 - (days_old / 30))  # Decay over month
                
                result['metadata'] = {
                    'path': file_path,
                    'total_size_mb': total_size,
                    'file_count': fs_test.get('file_count', 0),
                    'file_types': file_types,
                    'latest_file_date': latest_file.isoformat() if latest_file else None
                }
            else:
                result['issues'].append(fs_test.get('error', 'File system access failed'))
                
        except Exception as e:
            result['issues'].append(f"File system assessment error: {str(e)}")
        
        return result
    
    def _assess_data_lake(self, source: Dict, credentials: Dict) -> Dict:
        """Assess data lake data source"""
        # Similar to file system but with additional considerations
        return self._assess_file_system(source, credentials)
    
    def _assess_stream(self, source: Dict, credentials: Dict) -> Dict:
        """Assess streaming data source"""
        result = {
            'accessible': False,
            'accessibility_score': 0.0,
            'volume_score': 0.0,
            'type_score': 0.0,
            'freshness_score': 0.0,
            'issues': []
        }
        
        try:
            stream_config = source.get('stream_config', {})
            if not stream_config:
                result['issues'].append("Missing stream configuration")
                return result
            
            # Test stream accessibility
            stream_test = self._test_stream_accessibility(stream_config, credentials)
            
            if stream_test['success']:
                result['accessible'] = True
                result['accessibility_score'] = 1.0
                
                # Assess throughput
                throughput = stream_test.get('events_per_second', 0)
                result['volume_score'] = min(1.0, throughput / 1000)  # Normalize to 1k events/sec
                
                # Assess data types
                data_types = stream_test.get('data_types', [])
                result['type_score'] = min(1.0, len(data_types) / 5)  # Normalize to 5 types
                
                # Streams are inherently fresh
                result['freshness_score'] = 1.0
                
                result['metadata'] = {
                    'stream_type': stream_config.get('type', 'unknown'),
                    'throughput': throughput,
                    'data_types': data_types,
                    'latency_ms': stream_test.get('latency_ms', 0)
                }
            else:
                result['issues'].append(stream_test.get('error', 'Stream access failed'))
                
        except Exception as e:
            result['issues'].append(f"Stream assessment error: {str(e)}")
        
        return result
    
    def _assess_third_party(self, source: Dict, credentials: Dict) -> Dict:
        """Assess third-party data provider"""
        # Similar to API but with additional considerations
        return self._assess_api(source, credentials)
    
    def _assess_generic(self, source: Dict, credentials: Dict) -> Dict:
        """Generic assessment for unknown source types"""
        return {
            'accessible': False,
            'accessibility_score': 0.0,
            'volume_score': 0.0,
            'type_score': 0.0,
            'freshness_score': 0.0,
            'issues': [f"Unknown source type: {source.get('type', 'unknown')}"]
        }
    
    def _calculate_overall_scores(self, assessments: List[Dict], requirements: Dict) -> Dict:
        """Calculate overall availability scores"""
        if not assessments:
            return {
                'overall': 0.0,
                'accessibility': 0.0,
                'volume': 0.0,
                'type': 0.0,
                'freshness': 0.0,
                'accessible_count': 0,
                'volume_coverage': 0.0,
                'type_coverage': 0.0
            }
        
        # Calculate weighted averages
        accessible_sources = [a for a in assessments if a['accessible']]
        
        if not accessible_sources:
            return {
                'overall': 0.0,
                'accessibility': 0.0,
                'volume': 0.0,
                'type': 0.0,
                'freshness': 0.0,
                'accessible_count': 0,
                'volume_coverage': 0.0,
                'type_coverage': 0.0
            }
        
        # Calculate component scores
        accessibility_score = len(accessible_sources) / len(assessments)
        volume_score = sum(a['volume_score'] for a in accessible_sources) / len(accessible_sources)
        type_score = sum(a['type_score'] for a in accessible_sources) / len(accessible_sources)
        freshness_score = sum(a['freshness_score'] for a in accessible_sources) / len(accessible_sources)
        
        # Calculate overall score
        overall_score = (
            accessibility_score * self.weights['accessibility'] +
            volume_score * self.weights['volume'] +
            type_score * self.weights['type_coverage'] +
            freshness_score * self.weights['freshness']
        )
        
        # Calculate coverage against requirements
        required_volume = requirements.get('min_volume_gb', 100)
        actual_volume = sum(a['metadata'].get('total_size_mb', 0) for a in accessible_sources) / 1024  # Convert to GB
        volume_coverage = min(1.0, actual_volume / required_volume)
        
        required_types = set(requirements.get('required_data_types', []))
        available_types = set()
        for a in accessible_sources:
            available_types.update(a['metadata'].get('data_types', []))
        type_coverage = len(required_types.intersection(available_types)) / len(required_types) if required_types else 1.0
        
        return {
            'overall': round(overall_score, 3),
            'accessibility': round(accessibility_score, 3),
            'volume': round(volume_score, 3),
            'type': round(type_score, 3),
            'freshness': round(freshness_score, 3),
            'accessible_count': len(accessible_sources),
            'volume_coverage': round(volume_coverage, 3),
            'type_coverage': round(type_coverage, 3)
        }
    
    def _identify_issues(self, assessments: List[Dict]) -> Dict:
        """Identify common issues across data sources"""
        issues = {
            'accessibility': [],
            'volume': [],
            'type': [],
            'freshness': []
        }
        
        for assessment in assessments:
            if not assessment['accessible']:
                issues['accessibility'].append(assessment['source_id'])
            
            if assessment['volume_score'] < 0.5:
                issues['volume'].append(assessment['source_id'])
            
            if assessment['type_score'] < 0.5:
                issues['type'].append(assessment['source_id'])
            
            if assessment['freshness_score'] < 0.5:
                issues['freshness'].append(assessment['source_id'])
        
        return issues
    
    def _generate_recommendations(self, assessments: List[Dict], requirements: Dict) -> List[str]:
        """Generate recommendations for improving data availability"""
        recommendations = []
        
        # Count accessible vs total sources
        accessible_count = sum(1 for a in assessments if a['accessible'])
        total_count = len(assessments)
        
        if accessible_count < total_count:
            recommendations.append(f"Fix {total_count - accessible_count} inaccessible data sources")
        
        # Check volume issues
        low_volume_sources = [a['source_id'] for a in assessments if a['volume_score'] < 0.5]
        if low_volume_sources:
            recommendations.append(f"Increase data volume for sources: {', '.join(low_volume_sources)}")
        
        # Check type coverage
        recommendations.append("Consider data augmentation for insufficient data types")
        
        # Check freshness
        stale_sources = [a['source_id'] for a in assessments if a['freshness_score'] < 0.5]
        if stale_sources:
            recommendations.append(f"Update data freshness for sources: {', '.join(stale_sources)}")
        
        # General recommendations
        if accessible_count / total_count < 0.9:
            recommendations.append("Implement data source monitoring and alerting")
        
        recommendations.append("Establish data quality monitoring framework")
        
        return recommendations
    
    def _create_inventory(self, assessments: List[Dict]) -> Dict:
        """Create data source inventory"""
        inventory = {
            'total_sources': len(assessments),
            'accessible_sources': sum(1 for a in assessments if a['accessible']),
            'source_types': {},
            'total_size_gb': 0,
            'data_types': set(),
            'quality_distribution': {
                'high': 0,  # > 0.8
                'medium': 0,  # 0.5-0.8
                'low': 0  # < 0.5
            }
        }
        
        for assessment in assessments:
            # Count by type
            source_type = assessment['type']
            inventory['source_types'][source_type] = inventory['source_types'].get(source_type, 0) + 1
            
            # Add size
            size_mb = assessment['metadata'].get('total_size_mb', 0)
            inventory['total_size_gb'] += size_mb / 1024
            
            # Add data types
            inventory['data_types'].update(assessment['metadata'].get('data_types', []))
            
            # Quality distribution
            score = assessment['overall_score']
            if score > 0.8:
                inventory['quality_distribution']['high'] += 1
            elif score > 0.5:
                inventory['quality_distribution']['medium'] += 1
            else:
                inventory['quality_distribution']['low'] += 1
        
        inventory['data_types'] = list(inventory['data_types'])
        inventory['total_size_gb'] = round(inventory['total_size_gb'], 2)
        
        return inventory
    
    # Helper methods (simplified implementations)
    def _test_database_connection(self, connection_string: str, credentials: Dict) -> Dict:
        """Test database connection (simplified)"""
        # In real implementation, use appropriate database driver
        return {
            'success': True,
            'tables': [
                {'name': 'users', 'row_count': 50000, 'data_types': ['string', 'integer', 'datetime']},
                {'name': 'transactions', 'row_count': 200000, 'data_types': ['float', 'integer', 'datetime']}
            ],
            'last_updated': datetime.now()
        }
    
    def _test_api_accessibility(self, url: str, credentials: Dict) -> Dict:
        """Test API accessibility (simplified)"""
        try:
            response = requests.get(url, timeout=10, headers=credentials.get('headers', {}))
            if response.status_code == 200:
                return {
                    'success': True,
                    'rate_limit': 1000,
                    'sample_response': response.json() if response.headers.get('content-type', '').startswith('application/json') else {},
                    'format': 'json',
                    'last_updated': datetime.now()
                }
        except:
            pass
        return {'success': False, 'error': 'API request failed'}
    
    def _test_file_system_access(self, path: str, credentials: Dict) -> Dict:
        """Test file system access (simplified)"""
        # In real implementation, check actual file system
        return {
            'success': True,
            'total_size_mb': 5000,
            'file_count': 100,
            'file_types': ['csv', 'json', 'parquet'],
            'latest_file_date': datetime.now()
        }
    
    def _test_stream_accessibility(self, config: Dict, credentials: Dict) -> Dict:
        """Test stream accessibility (simplified)"""
        return {
            'success': True,
            'events_per_second': 500,
            'data_types': ['json', 'avro'],
            'latency_ms': 50
        }
    
    def _infer_data_types_from_json(self, data: Dict) -> List[str]:
        """Infer data types from JSON structure"""
        types = set()
        for value in data.values():
            if isinstance(value, str):
                types.add('string')
            elif isinstance(value, int):
                types.add('integer')
            elif isinstance(value, float):
                types.add('float')
            elif isinstance(value, bool):
                types.add('boolean')
            elif isinstance(value, list):
                types.add('array')
            elif isinstance(value, dict):
                types.add('object')
        return list(types)
    
    def _generate_evidence(self, result: Dict, inputs: Dict) -> None:
        """Generate evidence artifacts"""
        timestamp = datetime.now().isoformat()
        
        # Save detailed assessment report
        report_file = self.artifacts_dir / "data-availability-report.json"
        report_data = {
            "timestamp": timestamp,
            "assessment_summary": {
                "overall_score": result['availability_score'],
                "accessible_sources": result['accessible_sources'],
                "total_sources": result['total_sources'],
                "volume_coverage": result['volume_coverage'],
                "type_coverage": result['type_coverage']
            },
            "detailed_assessments": result['source_assessments'],
            "issues": {
                "accessibility_issues": result['accessibility_issues'],
                "recommendations": result['recommendations']
            },
            "data_inventory": result['data_inventory']
        }
        
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        # Generate markdown summary
        md_file = self.artifacts_dir / "data-availability-summary.md"
        with open(md_file, 'w') as f:
            f.write("# Data Availability Assessment\n\n")
            f.write(f"**Generated**: {timestamp}\n\n")
            f.write("## Executive Summary\n")
            f.write(f"- **Overall Availability Score**: {result['availability_score']:.2%}\n")
            f.write(f"- **Accessible Sources**: {result['accessible_sources']}/{result['total_sources']}\n")
            f.write(f"- **Volume Coverage**: {result['volume_coverage']:.2%}\n")
            f.write(f"- **Type Coverage**: {result['type_coverage']:.2%}\n\n")
            
            if result['accessibility_issues']:
                f.write("## Accessibility Issues\n")
                for issue in result['accessibility_issues']:
                    f.write(f"- {issue}\n")
                f.write("\n")
            
            if result['recommendations']:
                f.write("## Recommendations\n")
                for rec in result['recommendations']:
                    f.write(f"- {rec}\n")
    
    def _list_artifacts(self) -> List[str]:
        """List generated artifacts"""
        artifacts = []
        for file in self.artifacts_dir.glob("*"):
            artifacts.append(str(file.relative_to(self.workspace)))
        return artifacts


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Assess data availability for ML project")
    parser.add_argument("--workspace", required=True, help="Workspace path")
    parser.add_argument("--data-sources", required=True, help="Data sources configuration (JSON)")
    parser.add_argument("--requirements", default="{}", help="Data requirements (JSON)")
    parser.add_argument("--credentials", default="{}", help="Access credentials (JSON)")
    
    args = parser.parse_args()
    
    assessor = DataAvailabilityAssessor(args.workspace)
    result = assessor.execute(
        data_sources=json.loads(args.data_sources),
        requirements=json.loads(args.requirements),
        access_credentials=json.loads(args.credentials)
    )
    
    print(json.dumps(result, indent=2))
    
if __name__ == "__main__":
    main()
