#!/usr/bin/env python3
"""
Data Validation Script for Protocol 08
Validates quality and completeness of collected data
"""

import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

import pandas as pd
import numpy as np

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_validation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class DataValidator:
    """Validates collected data for quality and completeness"""
    
    def __init__(self, input_path: str, output_path: str):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.output_path.mkdir(parents=True, exist_ok=True)
        self.validation_results = []
        self.start_time = datetime.now()
        
        # Quality thresholds
        self.quality_thresholds = {
            'completeness_min': 0.95,
            'accuracy_min': 0.98,
            'consistency_min': 0.90,
            'validity_min': 0.95,
            'overall_quality_min': 0.90
        }
    
    def discover_data_files(self) -> List[Path]:
        """Discover all data files in input directory"""
        data_files = []
        
        # Look for common data file extensions
        extensions = ['.csv', '.json', '.parquet', '.xlsx', '.tsv']
        
        for ext in extensions:
            data_files.extend(self.input_path.glob(f"*{ext}"))
            data_files.extend(self.input_path.glob(f"**/*{ext}"))
        
        logger.info(f"Discovered {len(data_files)} data files")
        return data_files
    
    def load_data_file(self, file_path: Path) -> Optional[pd.DataFrame]:
        """Load data file based on extension"""
        try:
            if file_path.suffix == '.csv':
                return pd.read_csv(file_path)
            elif file_path.suffix == '.json':
                return pd.read_json(file_path)
            elif file_path.suffix == '.parquet':
                return pd.read_parquet(file_path)
            elif file_path.suffix in ['.xlsx', '.xls']:
                return pd.read_excel(file_path)
            elif file_path.suffix == '.tsv':
                return pd.read_csv(file_path, sep='\t')
            else:
                logger.warning(f"Unsupported file format: {file_path.suffix}")
                return None
        except Exception as e:
            logger.error(f"Failed to load {file_path}: {e}")
            return None
    
    def validate_completeness(self, df: pd.DataFrame, file_path: Path) -> Dict[str, Any]:
        """Validate data completeness"""
        logger.info(f"Validating completeness for {file_path.name}")
        
        try:
            # Calculate missing value percentages
            missing_counts = df.isnull().sum()
            missing_percentages = (missing_counts / len(df)) * 100
            
            # Overall completeness
            total_cells = df.shape[0] * df.shape[1]
            missing_cells = missing_counts.sum()
            completeness_score = 1 - (missing_cells / total_cells)
            
            # Column-level completeness
            column_completeness = {}
            for col in df.columns:
                col_missing_pct = missing_percentages[col]
                column_completeness[col] = {
                    'missing_count': int(missing_counts[col]),
                    'missing_percentage': float(col_missing_pct),
                    'completeness_score': float(1 - col_missing_pct / 100)
                }
            
            validation_result = {
                'metric': 'completeness',
                'overall_score': float(completeness_score),
                'threshold': self.quality_thresholds['completeness_min'],
                'passed': completeness_score >= self.quality_thresholds['completeness_min'],
                'details': {
                    'total_rows': int(df.shape[0]),
                    'total_columns': int(df.shape[1]),
                    'total_cells': int(total_cells),
                    'missing_cells': int(missing_cells),
                    'column_completeness': column_completeness
                }
            }
            
            logger.info(f"Completeness score: {completeness_score:.3f}")
            return validation_result
            
        except Exception as e:
            logger.error(f"Completeness validation failed for {file_path}: {e}")
            return {
                'metric': 'completeness',
                'overall_score': 0.0,
                'threshold': self.quality_thresholds['completeness_min'],
                'passed': False,
                'error': str(e)
            }
    
    def validate_accuracy(self, df: pd.DataFrame, file_path: Path) -> Dict[str, Any]:
        """Validate data accuracy (format and value validation)"""
        logger.info(f"Validating accuracy for {file_path.name}")
        
        try:
            accuracy_issues = []
            total_checks = 0
            passed_checks = 0
            
            # Check for data type consistency
            for col in df.columns:
                total_checks += 1
                
                # Check if numeric columns contain valid numbers
                if df[col].dtype in ['int64', 'float64']:
                    # Check for infinite values
                    inf_count = np.isinf(df[col]).sum()
                    if inf_count > 0:
                        accuracy_issues.append(f"Column '{col}' contains {inf_count} infinite values")
                    else:
                        passed_checks += 1
                
                # Check for string columns
                elif df[col].dtype == 'object':
                    # Check for empty strings
                    empty_count = (df[col] == '').sum()
                    if empty_count > len(df) * 0.05:  # More than 5% empty strings
                        accuracy_issues.append(f"Column '{col}' contains {empty_count} empty strings")
                    else:
                        passed_checks += 1
                
                else:
                    passed_checks += 1
            
            # Calculate accuracy score
            accuracy_score = passed_checks / total_checks if total_checks > 0 else 0
            
            validation_result = {
                'metric': 'accuracy',
                'overall_score': float(accuracy_score),
                'threshold': self.quality_thresholds['accuracy_min'],
                'passed': accuracy_score >= self.quality_thresholds['accuracy_min'],
                'details': {
                    'total_checks': int(total_checks),
                    'passed_checks': int(passed_checks),
                    'issues_found': accuracy_issues
                }
            }
            
            logger.info(f"Accuracy score: {accuracy_score:.3f}")
            return validation_result
            
        except Exception as e:
            logger.error(f"Accuracy validation failed for {file_path}: {e}")
            return {
                'metric': 'accuracy',
                'overall_score': 0.0,
                'threshold': self.quality_thresholds['accuracy_min'],
                'passed': False,
                'error': str(e)
            }
    
    def validate_consistency(self, df: pd.DataFrame, file_path: Path) -> Dict[str, Any]:
        """Validate data consistency"""
        logger.info(f"Validating consistency for {file_path.name}")
        
        try:
            consistency_issues = []
            consistency_score = 1.0
            
            # Check for duplicate rows
            duplicate_count = df.duplicated().sum()
            if duplicate_count > 0:
                duplicate_percentage = (duplicate_count / len(df)) * 100
                if duplicate_percentage > 5:  # More than 5% duplicates
                    consistency_issues.append(f"Contains {duplicate_count} duplicate rows ({duplicate_percentage:.1f}%)")
                    consistency_score -= 0.1
            
            # Check for inconsistent categorical values
            for col in df.columns:
                if df[col].dtype == 'object':
                    unique_values = df[col].dropna().unique()
                    # Check for similar values that might be inconsistencies (e.g., case differences)
                    if len(unique_values) > 1:
                        # Check for case inconsistencies
                        str_values = [str(v) for v in unique_values if isinstance(v, str)]
                        if len(str_values) > 1:
                            lower_values = [v.lower() for v in str_values]
                            if len(set(lower_values)) < len(set(str_values)):
                                consistency_issues.append(f"Column '{col}' has case inconsistencies")
                                consistency_score -= 0.05
            
            # Ensure score doesn't go below 0
            consistency_score = max(0, consistency_score)
            
            validation_result = {
                'metric': 'consistency',
                'overall_score': float(consistency_score),
                'threshold': self.quality_thresholds['consistency_min'],
                'passed': consistency_score >= self.quality_thresholds['consistency_min'],
                'details': {
                    'duplicate_rows': int(duplicate_count),
                    'duplicate_percentage': float((duplicate_count / len(df)) * 100) if len(df) > 0 else 0,
                    'issues_found': consistency_issues
                }
            }
            
            logger.info(f"Consistency score: {consistency_score:.3f}")
            return validation_result
            
        except Exception as e:
            logger.error(f"Consistency validation failed for {file_path}: {e}")
            return {
                'metric': 'consistency',
                'overall_score': 0.0,
                'threshold': self.quality_thresholds['consistency_min'],
                'passed': False,
                'error': str(e)
            }
    
    def validate_validity(self, df: pd.DataFrame, file_path: Path) -> Dict[str, Any]:
        """Validate data validity (ranges, formats, constraints)"""
        logger.info(f"Validating validity for {file_path.name}")
        
        try:
            validity_issues = []
            validity_score = 1.0
            total_checks = 0
            passed_checks = 0
            
            for col in df.columns:
                total_checks += 1
                
                # Check numeric columns for reasonable ranges
                if df[col].dtype in ['int64', 'float64']:
                    col_data = df[col].dropna()
                    if len(col_data) > 0:
                        # Check for extreme outliers (more than 5 standard deviations)
                        mean_val = col_data.mean()
                        std_val = col_data.std()
                        if std_val > 0:
                            outliers = abs(col_data - mean_val) > 5 * std_val
                            outlier_count = outliers.sum()
                            if outlier_count > len(col_data) * 0.01:  # More than 1% extreme outliers
                                validity_issues.append(f"Column '{col}' has {outlier_count} extreme outliers")
                            else:
                                passed_checks += 1
                        else:
                            passed_checks += 1
                    else:
                        passed_checks += 1
                
                # Check date columns for valid date ranges
                elif 'date' in col.lower() or 'time' in col.lower():
                    try:
                        # Try to convert to datetime
                        pd.to_datetime(df[col], errors='coerce')
                        passed_checks += 1
                    except:
                        validity_issues.append(f"Column '{col}' contains invalid date/time values")
                
                else:
                    passed_checks += 1
            
            # Calculate validity score
            validity_score = passed_checks / total_checks if total_checks > 0 else 0
            
            validation_result = {
                'metric': 'validity',
                'overall_score': float(validity_score),
                'threshold': self.quality_thresholds['validity_min'],
                'passed': validity_score >= self.quality_thresholds['validity_min'],
                'details': {
                    'total_checks': int(total_checks),
                    'passed_checks': int(passed_checks),
                    'issues_found': validity_issues
                }
            }
            
            logger.info(f"Validity score: {validity_score:.3f}")
            return validation_result
            
        except Exception as e:
            logger.error(f"Validity validation failed for {file_path}: {e}")
            return {
                'metric': 'validity',
                'overall_score': 0.0,
                'threshold': self.quality_thresholds['validity_min'],
                'passed': False,
                'error': str(e)
            }
    
    def validate_file(self, file_path: Path) -> Dict[str, Any]:
        """Validate a single data file"""
        logger.info(f"Validating file: {file_path}")
        
        try:
            # Load data
            df = self.load_data_file(file_path)
            if df is None:
                return {
                    'file_path': str(file_path),
                    'validation_status': 'failed',
                    'error': 'Could not load file'
                }
            
            # Run all validations
            validations = [
                self.validate_completeness(df, file_path),
                self.validate_accuracy(df, file_path),
                self.validate_consistency(df, file_path),
                self.validate_validity(df, file_path)
            ]
            
            # Calculate overall quality score
            scores = [v['overall_score'] for v in validations if 'overall_score' in v]
            overall_quality = np.mean(scores) if scores else 0.0
            
            # Check if all validations passed
            all_passed = all(v.get('passed', False) for v in validations)
            
            file_validation = {
                'file_path': str(file_path),
                'validation_status': 'passed' if all_passed else 'failed',
                'file_info': {
                    'rows': int(df.shape[0]),
                    'columns': int(df.shape[1]),
                    'size_mb': float(file_path.stat().st_size / (1024 * 1024))
                },
                'overall_quality_score': float(overall_quality),
                'quality_threshold': self.quality_thresholds['overall_quality_min'],
                'quality_passed': overall_quality >= self.quality_thresholds['overall_quality_min'],
                'validations': validations,
                'validation_timestamp': datetime.now().isoformat()
            }
            
            logger.info(f"File validation completed: {file_path.name} - Quality Score: {overall_quality:.3f}")
            return file_validation
            
        except Exception as e:
            logger.error(f"File validation failed for {file_path}: {e}")
            return {
                'file_path': str(file_path),
                'validation_status': 'failed',
                'error': str(e),
                'validation_timestamp': datetime.now().isoformat()
            }
    
    def execute_validation(self) -> Dict[str, Any]:
        """Execute validation for all discovered data files"""
        logger.info("Starting data validation execution")
        
        # Discover data files
        data_files = self.discover_data_files()
        
        if not data_files:
            logger.warning("No data files found for validation")
            return {
                'validation_summary': {
                    'total_files': 0,
                    'passed_files': 0,
                    'failed_files': 0,
                    'overall_quality_score': 0.0,
                    'validation_passed': False
                },
                'file_validations': []
            }
        
        # Validate each file
        file_validations = []
        for file_path in data_files:
            validation_result = self.validate_file(file_path)
            file_validations.append(validation_result)
            self.validation_results.append(validation_result)
        
        # Calculate validation summary
        total_files = len(file_validations)
        passed_files = sum(1 for v in file_validations if v.get('validation_status') == 'passed')
        failed_files = total_files - passed_files
        
        # Calculate overall quality across all files
        quality_scores = [v.get('overall_quality_score', 0) for v in file_validations if 'overall_quality_score' in v]
        overall_quality = np.mean(quality_scores) if quality_scores else 0.0
        
        validation_summary = {
            'validation_summary': {
                'total_files': int(total_files),
                'passed_files': int(passed_files),
                'failed_files': int(failed_files),
                'pass_rate': float(passed_files / total_files) if total_files > 0 else 0.0,
                'overall_quality_score': float(overall_quality),
                'quality_threshold': self.quality_thresholds['overall_quality_min'],
                'validation_passed': overall_quality >= self.quality_thresholds['overall_quality_min'] and passed_files == total_files,
                'execution_time_seconds': (datetime.now() - self.start_time).total_seconds(),
                'start_time': self.start_time.isoformat(),
                'end_time': datetime.now().isoformat()
            },
            'file_validations': file_validations,
            'quality_thresholds': self.quality_thresholds
        }
        
        logger.info(f"Validation completed: {passed_files}/{total_files} files passed, Overall Quality: {overall_quality:.3f}")
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
    
    parser = argparse.ArgumentParser(description='Validate collected data quality')
    parser.add_argument('--input', required=True, help='Input directory containing collected data')
    parser.add_argument('--output', required=True, help='Output directory for validation reports')
    
    args = parser.parse_args()
    
    try:
        # Initialize data validator
        validator = DataValidator(args.input, args.output)
        
        # Execute validation
        validation_report = validator.execute_validation()
        
        # Save validation report
        report_file = Path(args.output) / 'data_quality_report.json'
        validator.save_validation_report(validation_report, str(report_file))
        
        # Return success if validation passed
        if validation_report['validation_summary']['validation_passed']:
            logger.info("Data validation completed successfully")
            return 0
        else:
            logger.warning("Data validation completed with issues")
            return 1
            
    except Exception as e:
        logger.error(f"Data validation failed: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
