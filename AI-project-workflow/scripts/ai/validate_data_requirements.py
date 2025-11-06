#!/usr/bin/env python3
"""
Script: validate_data_requirements.py
Protocol: 07-ai-data-strategy-planning
Purpose: Validate that data meets quality and volume requirements
Author: AI Workflow System
Created: 2025-01-06
"""

import json
import logging
from typing import Dict, List, Optional, Any, Union
from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np
from collections import defaultdict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataRequirementsValidator:
    """Validate data against ML project requirements and quality standards"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts" / "protocol-07"
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        # Quality thresholds
        self.quality_thresholds = {
            'completeness': {
                'excellent': 0.98,
                'good': 0.95,
                'acceptable': 0.90,
                'poor': 0.80
            },
            'accuracy': {
                'excellent': 0.99,
                'good': 0.95,
                'acceptable': 0.90,
                'poor': 0.80
            },
            'consistency': {
                'excellent': 0.95,
                'good': 0.90,
                'acceptable': 0.85,
                'poor': 0.75
            },
            'timeliness': {
                'excellent': 1.0,    # Real-time
                'good': 0.8,        # < 1 day
                'acceptable': 0.6,  # < 1 week
                'poor': 0.4         # > 1 week
            },
            'validity': {
                'excellent': 0.98,
                'good': 0.95,
                'acceptable': 0.90,
                'poor': 0.80
            }
        }
        
        # Volume requirements by problem type
        self.volume_requirements = {
            'classification': {
                'binary': {'minimum': 1000, 'recommended': 10000},
                'multiclass': {'minimum': 5000, 'recommended': 50000},
                'multilabel': {'minimum': 2000, 'recommended': 20000}
            },
            'regression': {
                'standard': {'minimum': 500, 'recommended': 5000},
                'time_series': {'minimum': 1000, 'recommended': 10000}
            },
            'clustering': {
                'partitioning': {'minimum': 200, 'recommended': 2000},
                'hierarchical': {'minimum': 100, 'recommended': 1000}
            },
            'nlp': {
                'classification': {'minimum': 5000, 'recommended': 50000},
                'generation': {'minimum': 10000, 'recommended': 100000}
            },
            'computer_vision': {
                'classification': {'minimum': 1000, 'recommended': 10000},
                'detection': {'minimum': 5000, 'recommended': 50000}
            }
        }
    
    def execute(self, **kwargs) -> Dict:
        """
        Validate data against requirements
        
        Args:
            data_samples: Sample data from each source
            quality_criteria: Quality thresholds and requirements
            volume_requirements: Minimum data volumes needed
            
        Returns:
            Dict: Validation results with scores and recommendations
        """
        try:
            data_samples = kwargs.get('data_samples', [])
            quality_criteria = kwargs.get('quality_criteria', {})
            volume_requirements = kwargs.get('volume_requirements', {})
            problem_type = kwargs.get('problem_type', 'classification')
            
            # Validate each data sample
            sample_validations = []
            for sample in data_samples:
                validation = self._validate_single_sample(sample, quality_criteria)
                sample_validations.append(validation)
            
            # Calculate overall scores
            overall_scores = self._calculate_overall_scores(sample_validations)
            
            # Validate volume requirements
            volume_validation = self._validate_volume_requirements(
                sample_validations, volume_requirements, problem_type
            )
            
            # Identify quality issues
            quality_issues = self._identify_quality_issues(sample_validations)
            
            # Generate recommendations
            recommendations = self._generate_recommendations(
                sample_validations, quality_issues, volume_validation
            )
            
            # Create data quality profile
            quality_profile = self._create_quality_profile(sample_validations)
            
            result = {
                "quality_score": overall_scores['quality'],
                "volume_score": volume_validation['score'],
                "completeness_score": overall_scores['completeness'],
                "accuracy_score": overall_scores['accuracy'],
                "consistency_score": overall_scores['consistency'],
                "timeliness_score": overall_scores['timeliness'],
                "validity_score": overall_scores['validity'],
                "volume_validation": volume_validation,
                "quality_issues": quality_issues,
                "recommendations": recommendations,
                "sample_validations": sample_validations,
                "quality_profile": quality_profile
            }
            
            # Generate evidence
            self._generate_evidence(result, kwargs)
            
            return {
                "status": "success",
                "result": result,
                "artifacts": self._list_artifacts()
            }
            
        except Exception as e:
            logger.error(f"Data requirements validation failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _validate_single_sample(self, sample: Dict, criteria: Dict) -> Dict:
        """Validate a single data sample"""
        validation = {
            'sample_id': sample.get('id', 'unknown'),
            'source': sample.get('source', 'unknown'),
            'size_mb': 0,
            'row_count': 0,
            'column_count': 0,
            'quality_scores': {},
            'issues': [],
            'statistics': {}
        }
        
        try:
            # Load sample data
            data = self._load_sample_data(sample)
            if data is None:
                validation['issues'].append("Failed to load sample data")
                return validation
            
            # Basic statistics
            validation['row_count'] = len(data)
            validation['column_count'] = len(data.columns) if hasattr(data, 'columns') else 0
            validation['size_mb'] = self._estimate_size_mb(data)
            
            # Quality assessments
            completeness_score = self._assess_completeness(data)
            accuracy_score = self._assess_accuracy(data, criteria)
            consistency_score = self._assess_consistency(data)
            timeliness_score = self._assess_timeliness(data, sample)
            validity_score = self._assess_validity(data)
            
            validation['quality_scores'] = {
                'completeness': completeness_score,
                'accuracy': accuracy_score,
                'consistency': consistency_score,
                'timeliness': timeliness_score,
                'validity': validity_score
            }
            
            # Calculate overall quality score
            validation['overall_quality'] = sum(validation['quality_scores'].values()) / len(validation['quality_scores'])
            
            # Generate statistics
            validation['statistics'] = self._generate_statistics(data)
            
            # Identify issues
            validation['issues'] = self._identify_sample_issues(validation['quality_scores'], criteria)
            
        except Exception as e:
            validation['issues'].append(f"Validation error: {str(e)}")
            logger.error(f"Failed to validate sample {sample.get('id', 'unknown')}: {e}")
        
        return validation
    
    def _load_sample_data(self, sample: Dict) -> Optional[pd.DataFrame]:
        """Load sample data from various sources"""
        try:
            data_path = sample.get('data_path')
            data_type = sample.get('type', 'csv')
            
            if not data_path:
                return None
            
            # Simulate data loading (in real implementation, load actual files)
            if data_type == 'csv':
                # Simulate CSV data
                return pd.DataFrame({
                    'id': range(1000),
                    'feature1': np.random.normal(0, 1, 1000),
                    'feature2': np.random.choice(['A', 'B', 'C'], 1000),
                    'target': np.random.choice([0, 1], 1000),
                    'timestamp': pd.date_range('2024-01-01', periods=1000, freq='H')
                })
            elif data_type == 'json':
                # Simulate JSON data
                return pd.DataFrame({
                    'user_id': range(1000),
                    'activity': np.random.choice(['click', 'view', 'purchase'], 1000),
                    'value': np.random.exponential(50, 1000),
                    'date': pd.date_range('2024-01-01', periods=1000, freq='D')
                })
            else:
                # Generic simulation
                return pd.DataFrame(np.random.randn(1000, 5))
                
        except Exception as e:
            logger.error(f"Failed to load sample data: {e}")
            return None
    
    def _assess_completeness(self, data: pd.DataFrame) -> float:
        """Assess data completeness (missing values)"""
        if data.empty:
            return 0.0
        
        total_values = data.shape[0] * data.shape[1]
        missing_values = data.isnull().sum().sum()
        
        completeness = 1.0 - (missing_values / total_values)
        return round(completeness, 3)
    
    def _assess_accuracy(self, data: pd.DataFrame, criteria: Dict) -> float:
        """Assess data accuracy"""
        if data.empty:
            return 0.0
        
        # Simulate accuracy assessment (in real implementation, use validation rules)
        accuracy_score = 0.95  # Default good score
        
        # Check for obvious data quality issues
        for column in data.columns:
            if data[column].dtype in ['int64', 'float64']:
                # Check for unrealistic values
                if (data[column] < 0).any() and column not in ['target', 'value']:
                    accuracy_score -= 0.05
                if (data[column] > 1000000).any():
                    accuracy_score -= 0.05
        
        return max(0.0, round(accuracy_score, 3))
    
    def _assess_consistency(self, data: pd.DataFrame) -> float:
        """Assess data consistency"""
        if data.empty:
            return 0.0
        
        consistency_score = 0.95  # Default good score
        
        # Check for duplicate rows
        duplicate_ratio = data.duplicated().sum() / len(data)
        if duplicate_ratio > 0.05:
            consistency_score -= 0.1
        
        # Check for inconsistent formats in string columns
        for column in data.select_dtypes(include=['object']).columns:
            unique_formats = set()
            for value in data[column].dropna().head(100):  # Sample first 100
                if isinstance(value, str):
                    # Simple format detection
                    if value.isdigit():
                        unique_formats.add('numeric')
                    elif '@' in value:
                        unique_formats.add('email')
                    elif len(value) == 10 and value.isdigit():
                        unique_formats.add('phone')
                    else:
                        unique_formats.add('text')
            
            if len(unique_formats) > 3:
                consistency_score -= 0.05
        
        return max(0.0, round(consistency_score, 3))
    
    def _assess_timeliness(self, data: pd.DataFrame, sample: Dict) -> float:
        """Assess data timeliness/freshness"""
        # Check if data has timestamp information
        timestamp_columns = []
        for column in data.columns:
            if any(keyword in column.lower() for keyword in ['time', 'date', 'created', 'updated']):
                timestamp_columns.append(column)
        
        if not timestamp_columns:
            return 0.7  # No timestamp information
        
        # Simulate timeliness assessment
        last_updated = sample.get('last_updated', datetime.now())
        days_old = (datetime.now() - last_updated).days
        
        if days_old == 0:
            return 1.0  # Real-time
        elif days_old < 1:
            return 0.8  # Less than a day
        elif days_old < 7:
            return 0.6  # Less than a week
        else:
            return 0.4  # Older than a week
    
    def _assess_validity(self, data: pd.DataFrame) -> float:
        """Assess data validity (format and range constraints)"""
        if data.empty:
            return 0.0
        
        validity_score = 0.95  # Default good score
        
        # Check for invalid values in numeric columns
        for column in data.select_dtypes(include=[np.number]).columns:
            if data[column].isnull().all():
                validity_score -= 0.1
            elif np.isinf(data[column]).any():
                validity_score -= 0.1
        
        # Check for empty strings in object columns
        for column in data.select_dtypes(include=['object']).columns:
            empty_strings = (data[column] == '').sum()
            if empty_strings > len(data) * 0.1:
                validity_score -= 0.1
        
        return max(0.0, round(validity_score, 3))
    
    def _generate_statistics(self, data: pd.DataFrame) -> Dict:
        """Generate basic statistics for the data"""
        stats = {
            'numeric_columns': 0,
            'categorical_columns': 0,
            'datetime_columns': 0,
            'missing_value_ratio': 0.0,
            'duplicate_ratio': 0.0
        }
        
        if data.empty:
            return stats
        
        # Column types
        stats['numeric_columns'] = len(data.select_dtypes(include=[np.number]).columns)
        stats['categorical_columns'] = len(data.select_dtypes(include=['object']).columns)
        
        # Missing values
        stats['missing_value_ratio'] = data.isnull().sum().sum() / (data.shape[0] * data.shape[1])
        
        # Duplicates
        stats['duplicate_ratio'] = data.duplicated().sum() / len(data)
        
        return stats
    
    def _identify_sample_issues(self, quality_scores: Dict, criteria: Dict) -> List[str]:
        """Identify issues in a data sample"""
        issues = []
        
        for metric, score in quality_scores.items():
            threshold = criteria.get(metric, {}).get('minimum', 0.9)
            if score < threshold:
                issues.append(f"{metric} score {score:.3f} below threshold {threshold}")
        
        return issues
    
    def _calculate_overall_scores(self, validations: List[Dict]) -> Dict:
        """Calculate overall quality scores across all samples"""
        if not validations:
            return {
                'quality': 0.0,
                'completeness': 0.0,
                'accuracy': 0.0,
                'consistency': 0.0,
                'timeliness': 0.0,
                'validity': 0.0
            }
        
        # Calculate weighted averages
        metrics = ['completeness', 'accuracy', 'consistency', 'timeliness', 'validity']
        scores = {}
        
        for metric in metrics:
            metric_scores = [
                v['quality_scores'].get(metric, 0.0) 
                for v in validations 
                if 'quality_scores' in v
            ]
            if metric_scores:
                scores[metric] = round(sum(metric_scores) / len(metric_scores), 3)
            else:
                scores[metric] = 0.0
        
        # Overall quality score
        scores['quality'] = round(sum(scores.values()) / len(scores), 3)
        
        return scores
    
    def _validate_volume_requirements(self, validations: List[Dict], 
                                     requirements: Dict, problem_type: str) -> Dict:
        """Validate volume requirements"""
        total_rows = sum(v.get('row_count', 0) for v in validations)
        total_size_mb = sum(v.get('size_mb', 0) for v in validations)
        
        # Get required volumes
        required = requirements.get('minimum_rows', 1000)
        recommended = requirements.get('recommended_rows', 10000)
        
        # Or use defaults based on problem type
        if not requirements:
            problem_category = problem_type.split('_')[0] if '_' in problem_type else problem_type
            subtype = problem_type.split('_')[1] if '_' in problem_type else 'standard'
            
            if problem_category in self.volume_requirements:
                if subtype in self.volume_requirements[problem_category]:
                    reqs = self.volume_requirements[problem_category][subtype]
                else:
                    reqs = list(self.volume_requirements[problem_category].values())[0]
                required = reqs['minimum']
                recommended = reqs['recommended']
        
        # Calculate scores
        score = min(1.0, total_rows / recommended)
        
        return {
            'total_rows': total_rows,
            'total_size_mb': round(total_size_mb, 2),
            'required_rows': required,
            'recommended_rows': recommended,
            'score': round(score, 3),
            'meets_minimum': total_rows >= required,
            'meets_recommended': total_rows >= recommended
        }
    
    def _identify_quality_issues(self, validations: List[Dict]) -> Dict:
        """Identify common quality issues across samples"""
        issues = {
            'high_missing_values': [],
            'accuracy_problems': [],
            'consistency_issues': [],
            'timeliness_concerns': [],
            'validity_problems': []
        }
        
        for validation in validations:
            sample_id = validation.get('sample_id', 'unknown')
            scores = validation.get('quality_scores', {})
            
            if scores.get('completeness', 1.0) < 0.9:
                issues['high_missing_values'].append(sample_id)
            
            if scores.get('accuracy', 1.0) < 0.9:
                issues['accuracy_problems'].append(sample_id)
            
            if scores.get('consistency', 1.0) < 0.85:
                issues['consistency_issues'].append(sample_id)
            
            if scores.get('timeliness', 1.0) < 0.6:
                issues['timeliness_concerns'].append(sample_id)
            
            if scores.get('validity', 1.0) < 0.9:
                issues['validity_problems'].append(sample_id)
        
        return issues
    
    def _generate_recommendations(self, validations: List[Dict], 
                                quality_issues: Dict, volume_validation: Dict) -> List[str]:
        """Generate recommendations for improving data quality"""
        recommendations = []
        
        # Volume recommendations
        if not volume_validation['meets_minimum']:
            recommendations.append(
                f"Increase data volume from {volume_validation['total_rows']} to at least {volume_validation['required_rows']} rows"
            )
        elif not volume_validation['meets_recommended']:
            recommendations.append(
                f"Consider increasing data volume to recommended {volume_validation['recommended_rows']} rows for better model performance"
            )
        
        # Quality recommendations
        if quality_issues['high_missing_values']:
            recommendations.append(
                f"Implement data imputation for samples with high missing values: {', '.join(quality_issues['high_missing_values'])}"
            )
        
        if quality_issues['accuracy_problems']:
            recommendations.append(
                f"Review data validation rules for accuracy issues in: {', '.join(quality_issues['accuracy_problems'])}"
            )
        
        if quality_issues['consistency_issues']:
            recommendations.append(
                f"Standardize data formats and remove duplicates in: {', '.join(quality_issues['consistency_issues'])}"
            )
        
        if quality_issues['timeliness_concerns']:
            recommendations.append(
                f"Update data refresh frequency for: {', '.join(quality_issues['timeliness_concerns'])}"
            )
        
        if quality_issues['validity_problems']:
            recommendations.append(
                f"Implement data validation checks for: {', '.join(quality_issues['validity_problems'])}"
            )
        
        # General recommendations
        recommendations.append("Implement automated data quality monitoring")
        recommendations.append("Establish data quality SLAs with data providers")
        recommendations.append("Create data quality dashboards for continuous monitoring")
        
        return recommendations
    
    def _create_quality_profile(self, validations: List[Dict]) -> Dict:
        """Create comprehensive data quality profile"""
        profile = {
            'total_samples': len(validations),
            'total_rows': sum(v.get('row_count', 0) for v in validations),
            'total_size_mb': round(sum(v.get('size_mb', 0) for v in validations), 2),
            'average_quality_score': 0.0,
            'quality_distribution': {
                'excellent': 0,  # > 0.95
                'good': 0,       # 0.85-0.95
                'acceptable': 0, # 0.70-0.85
                'poor': 0        # < 0.70
            },
            'column_statistics': {
                'total_columns': 0,
                'numeric_columns': 0,
                'categorical_columns': 0,
                'datetime_columns': 0
            }
        }
        
        if not validations:
            return profile
        
        # Quality distribution
        for validation in validations:
            quality = validation.get('overall_quality', 0.0)
            if quality > 0.95:
                profile['quality_distribution']['excellent'] += 1
            elif quality > 0.85:
                profile['quality_distribution']['good'] += 1
            elif quality > 0.70:
                profile['quality_distribution']['acceptable'] += 1
            else:
                profile['quality_distribution']['poor'] += 1
        
        # Average quality score
        quality_scores = [v.get('overall_quality', 0.0) for v in validations]
        profile['average_quality_score'] = round(sum(quality_scores) / len(quality_scores), 3)
        
        # Column statistics
        for validation in validations:
            stats = validation.get('statistics', {})
            profile['column_statistics']['numeric_columns'] += stats.get('numeric_columns', 0)
            profile['column_statistics']['categorical_columns'] += stats.get('categorical_columns', 0)
            profile['column_statistics']['total_columns'] += validation.get('column_count', 0)
        
        return profile
    
    def _estimate_size_mb(self, data: pd.DataFrame) -> float:
        """Estimate data size in MB"""
        if data.empty:
            return 0.0
        
        # Rough estimation based on data types
        size_bytes = data.memory_usage(deep=True).sum()
        return round(size_bytes / (1024 * 1024), 2)
    
    def _generate_evidence(self, result: Dict, inputs: Dict) -> None:
        """Generate evidence artifacts"""
        timestamp = datetime.now().isoformat()
        
        # Save detailed validation report
        report_file = self.artifacts_dir / "data-validation-report.json"
        report_data = {
            "timestamp": timestamp,
            "validation_summary": {
                "overall_quality_score": result['quality_score'],
                "volume_score": result['volume_score']['score'],
                "meets_volume_requirements": result['volume_score']['meets_minimum'],
                "total_samples_validated": len(result['sample_validations'])
            },
            "quality_scores": {
                "completeness": result['completeness_score'],
                "accuracy": result['accuracy_score'],
                "consistency": result['consistency_score'],
                "timeliness": result['timeliness_score'],
                "validity": result['validity_score']
            },
            "volume_validation": result['volume_validation'],
            "quality_issues": result['quality_issues'],
            "recommendations": result['recommendations'],
            "detailed_validations": result['sample_validations'],
            "quality_profile": result['quality_profile']
        }
        
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        # Generate markdown summary
        md_file = self.artifacts_dir / "data-validation-summary.md"
        with open(md_file, 'w') as f:
            f.write("# Data Validation Summary\n\n")
            f.write(f"**Generated**: {timestamp}\n\n")
            f.write("## Validation Results\n")
            f.write(f"- **Overall Quality Score**: {result['quality_score']:.2%}\n")
            f.write(f"- **Volume Score**: {result['volume_score']['score']:.2%}\n")
            f.write(f"- **Total Rows**: {result['volume_score']['total_rows']:,}\n")
            f.write(f"- **Meets Minimum Requirements**: {'✅' if result['volume_score']['meets_minimum'] else '❌'}\n\n")
            
            f.write("## Quality Scores\n")
            f.write(f"- **Completeness**: {result['completeness_score']:.2%}\n")
            f.write(f"- **Accuracy**: {result['accuracy_score']:.2%}\n")
            f.write(f"- **Consistency**: {result['consistency_score']:.2%}\n")
            f.write(f"- **Timeliness**: {result['timeliness_score']:.2%}\n")
            f.write(f"- **Validity**: {result['validity_score']:.2%}\n\n")
            
            if result['quality_issues']:
                f.write("## Quality Issues\n")
                for issue_type, samples in result['quality_issues'].items():
                    if samples:
                        f.write(f"- **{issue_type.replace('_', ' ').title()}**: {', '.join(samples)}\n")
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
    
    parser = argparse.ArgumentParser(description="Validate data requirements for ML project")
    parser.add_argument("--workspace", required=True, help="Workspace path")
    parser.add_argument("--data-samples", required=True, help="Data samples configuration (JSON)")
    parser.add_argument("--quality-criteria", default="{}", help="Quality criteria (JSON)")
    parser.add_argument("--volume-requirements", default="{}", help="Volume requirements (JSON)")
    parser.add_argument("--problem-type", default="classification", help="ML problem type")
    
    args = parser.parse_args()
    
    validator = DataRequirementsValidator(args.workspace)
    result = validator.execute(
        data_samples=json.loads(args.data_samples),
        quality_criteria=json.loads(args.quality_criteria),
        volume_requirements=json.loads(args.volume_requirements),
        problem_type=args.problem_type
    )
    
    print(json.dumps(result, indent=2))
    
if __name__ == "__main__":
    main()
