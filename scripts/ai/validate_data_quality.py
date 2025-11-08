#!/usr/bin/env python3
"""
Script: validate_data_quality.py
Protocol: 08-ai-data-collection-ingestion
Purpose: Validate quality of ingested data
Author: AI Workflow System
Created: 2025-11-08
"""

import json
import logging
import argparse
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import hashlib

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataQualityValidator:
    """Main class for data quality validation"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts"
        self.protocol_08_dir = self.artifacts_dir / "protocol-08-ai-data-collection-ingestion"
        self.raw_data_dir = self.protocol_08_dir / "raw-data"
        self.profiling_dir = self.protocol_08_dir / "profiling-reports"
        
        # Ensure directories exist
        self.profiling_dir.mkdir(parents=True, exist_ok=True)
        
    def execute(self, input_dir: str, output_file: str, config_file: str = None) -> Dict:
        """
        Main execution method
        
        Args:
            input_dir: Directory containing ingested data files
            output_file: Path for quality metrics file
            config_file: Optional quality configuration file
            
        Returns:
            Dict: Execution results with status and quality scores
        """
        try:
            # Load quality configuration
            quality_config = self._load_quality_config(config_file)
            
            # Validate data quality
            results = self._validate_data_quality(input_dir, quality_config)
            
            # Generate quality metrics
            self._generate_quality_report(results, output_file)
            
            return {
                "status": "success",
                "results": results,
                "overall_quality_score": results.get("overall_quality_score", 0.0),
                "data_quality_acceptable": results.get("data_quality_acceptable", False)
            }
            
        except Exception as e:
            logger.error(f"Quality validation failed: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "overall_quality_score": 0.0,
                "data_quality_acceptable": False
            }
    
    def _load_quality_config(self, config_file: str = None) -> Dict:
        """Load quality configuration from file"""
        if config_file and Path(config_file).exists():
            with open(config_file, 'r') as f:
                return json.load(f)
        
        # Default quality configuration
        return {
            "thresholds": {
                "completeness": 0.95,
                "accuracy": 0.90,
                "consistency": 0.95,
                "timeliness": 0.90,
                "uniqueness": 0.95
            },
            "required_columns": [],
            "pii_columns": [],
            "data_types": {}
        }
    
    def _validate_data_quality(self, input_dir: str, quality_config: Dict) -> Dict:
        """Validate quality of all data files"""
        results = {
            "validation_start": datetime.now().isoformat(),
            "total_files": 0,
            "files_validated": 0,
            "files_failed": 0,
            "total_records": 0,
            "quality_dimensions": {},
            "file_details": [],
            "overall_quality_score": 0.0,
            "data_quality_acceptable": False,
            "validation_end": "",
            "duration_seconds": 0
        }
        
        input_path = Path(input_dir)
        if not input_path.exists():
            raise FileNotFoundError(f"Input directory not found: {input_dir}")
        
        # Find all parquet files
        data_files = list(input_path.glob("*.parquet"))
        results["total_files"] = len(data_files)
        
        logger.info(f"Validating quality for {len(data_files)} data files")
        
        # Initialize quality dimensions
        thresholds = quality_config.get("thresholds", {})
        for dimension in thresholds.keys():
            results["quality_dimensions"][dimension] = {
                "total_score": 0.0,
                "file_scores": [],
                "threshold": thresholds[dimension],
                "passed": False
            }
        
        # Validate each file
        for file_path in data_files:
            file_result = self._validate_single_file(file_path, quality_config)
            results["file_details"].append(file_result)
            
            if file_result["status"] == "success":
                results["files_validated"] += 1
                results["total_records"] += file_result.get("record_count", 0)
                
                # Update dimension scores
                for dimension, score in file_result.get("dimension_scores", {}).items():
                    if dimension in results["quality_dimensions"]:
                        results["quality_dimensions"][dimension]["file_scores"].append(score)
            else:
                results["files_failed"] += 1
        
        # Calculate final scores
        results["validation_end"] = datetime.now().isoformat()
        start_time = datetime.fromisoformat(results["validation_start"])
        end_time = datetime.fromisoformat(results["validation_end"])
        results["duration_seconds"] = (end_time - start_time).total_seconds()
        
        # Calculate dimension averages and overall score
        dimension_scores = []
        for dimension, data in results["quality_dimensions"].items():
            if data["file_scores"]:
                avg_score = np.mean(data["file_scores"])
                data["total_score"] = round(avg_score, 3)
                data["passed"] = avg_score >= data["threshold"]
                dimension_scores.append(avg_score)
        
        # Overall quality score is average of all dimensions
        if dimension_scores:
            results["overall_quality_score"] = round(np.mean(dimension_scores), 3)
        
        # Check if data quality is acceptable
        min_threshold = min(thresholds.values()) if thresholds else 0.9
        results["data_quality_acceptable"] = results["overall_quality_score"] >= min_threshold
        
        logger.info(f"Quality validation completed: {results['overall_quality_score']:.3f} overall score")
        
        return results
    
    def _validate_single_file(self, file_path: Path, quality_config: Dict) -> Dict:
        """Validate quality of a single data file"""
        result = {
            "file_name": file_path.name,
            "file_size_mb": round(file_path.stat().st_size / (1024 * 1024), 2),
            "status": "error",
            "message": "",
            "record_count": 0,
            "column_count": 0,
            "dimension_scores": {},
            "quality_issues": [],
            "checksum": "",
            "validation_timestamp": datetime.now().isoformat()
        }
        
        try:
            # Load data
            df = pd.read_parquet(file_path)
            result["record_count"] = len(df)
            result["column_count"] = len(df.columns)
            
            # Calculate checksum
            result["checksum"] = self._calculate_checksum(file_path)
            
            # Validate each quality dimension
            thresholds = quality_config.get("thresholds", {})
            
            # Completeness
            completeness_score = self._calculate_completeness(df)
            result["dimension_scores"]["completeness"] = completeness_score
            if completeness_score < thresholds.get("completeness", 0.95):
                result["quality_issues"].append(f"Low completeness: {completeness_score:.3f}")
            
            # Accuracy (basic validation)
            accuracy_score = self._calculate_accuracy(df, quality_config)
            result["dimension_scores"]["accuracy"] = accuracy_score
            if accuracy_score < thresholds.get("accuracy", 0.90):
                result["quality_issues"].append(f"Low accuracy: {accuracy_score:.3f}")
            
            # Consistency
            consistency_score = self._calculate_consistency(df)
            result["dimension_scores"]["consistency"] = consistency_score
            if consistency_score < thresholds.get("consistency", 0.95):
                result["quality_issues"].append(f"Low consistency: {consistency_score:.3f}")
            
            # Timeliness (placeholder - would need timestamp columns)
            timeliness_score = self._calculate_timeliness(df)
            result["dimension_scores"]["timeliness"] = timeliness_score
            if timeliness_score < thresholds.get("timeliness", 0.90):
                result["quality_issues"].append(f"Low timeliness: {timeliness_score:.3f}")
            
            # Uniqueness
            uniqueness_score = self._calculate_uniqueness(df)
            result["dimension_scores"]["uniqueness"] = uniqueness_score
            if uniqueness_score < thresholds.get("uniqueness", 0.95):
                result["quality_issues"].append(f"Low uniqueness: {uniqueness_score:.3f}")
            
            result["status"] = "success"
            result["message"] = "Quality validation completed"
            
            # Generate profiling report
            self._generate_profiling_report(df, file_path, result)
            
        except Exception as e:
            result["message"] = f"Validation error: {str(e)}"
        
        return result
    
    def _calculate_completeness(self, df: pd.DataFrame) -> float:
        """Calculate completeness score (non-null values / total values)"""
        total_values = len(df) * len(df.columns)
        non_null_values = df.count().sum()
        return round(non_null_values / total_values, 3) if total_values > 0 else 0.0
    
    def _calculate_accuracy(self, df: pd.DataFrame, quality_config: Dict) -> float:
        """Calculate accuracy score (basic data format validation)"""
        accuracy_issues = 0
        total_checks = 0
        
        # Check data types if specified
        data_types = quality_config.get("data_types", {})
        for column, expected_type in data_types.items():
            if column in df.columns:
                total_checks += 1
                try:
                    if expected_type == "numeric":
                        pd.to_numeric(df[column], errors='coerce')
                    elif expected_type == "datetime":
                        pd.to_datetime(df[column], errors='coerce')
                    # Add more type checks as needed
                except:
                    accuracy_issues += 1
        
        # Check for obvious data quality issues
        for column in df.columns:
            total_checks += 1
            
            # Check for empty strings in object columns
            if df[column].dtype == 'object':
                empty_strings = (df[column] == '').sum()
                if empty_strings > len(df) * 0.1:  # More than 10% empty strings
                    accuracy_issues += 1
            
            # Check for negative values in columns that should be positive
            if 'amount' in column.lower() or 'count' in column.lower() or 'value' in column.lower():
                if df[column].dtype in ['int64', 'float64']:
                    negative_values = (df[column] < 0).sum()
                    if negative_values > len(df) * 0.05:  # More than 5% negative values
                        accuracy_issues += 1
        
        return round(1.0 - (accuracy_issues / total_checks), 3) if total_checks > 0 else 1.0
    
    def _calculate_consistency(self, df: pd.DataFrame) -> float:
        """Calculate consistency score (data format consistency)"""
        consistency_issues = 0
        total_checks = 0
        
        for column in df.columns:
            total_checks += 1
            
            # Check for consistent data types within column
            if df[column].dtype == 'object':
                # Check string length consistency
                str_lengths = df[column].astype(str).str.len()
                if str_lengths.std() > str_lengths.mean() * 0.5:  # High variance in length
                    consistency_issues += 1
            
            # Check for consistent patterns
            if 'id' in column.lower():
                # ID columns should have consistent format
                unique_count = df[column].nunique()
                total_count = len(df)
                if unique_count != total_count:  # IDs should be unique
                    consistency_issues += 1
        
        return round(1.0 - (consistency_issues / total_checks), 3) if total_checks > 0 else 1.0
    
    def _calculate_timeliness(self, df: pd.DataFrame) -> float:
        """Calculate timeliness score (placeholder implementation)"""
        # In a real implementation, this would check timestamp columns
        # For now, return a default score
        return 0.95
    
    def _calculate_uniqueness(self, df: pd.DataFrame) -> float:
        """Calculate uniqueness score (duplicate detection)"""
        total_records = len(df)
        if total_records == 0:
            return 1.0
        
        # Check for exact duplicates
        duplicate_count = df.duplicated().sum()
        uniqueness_score = 1.0 - (duplicate_count / total_records)
        
        return round(uniqueness_score, 3)
    
    def _calculate_checksum(self, file_path: Path) -> str:
        """Calculate SHA-256 checksum of file"""
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    
    def _generate_profiling_report(self, df: pd.DataFrame, file_path: Path, validation_result: Dict):
        """Generate detailed profiling report for the file"""
        profile = {
            "file_info": {
                "name": file_path.name,
                "size_mb": validation_result["file_size_mb"],
                "records": validation_result["record_count"],
                "columns": validation_result["column_count"],
                "checksum": validation_result["checksum"]
            },
            "column_profiles": {},
            "quality_scores": validation_result["dimension_scores"],
            "quality_issues": validation_result["quality_issues"],
            "generated_at": datetime.now().isoformat()
        }
        
        # Profile each column
        for column in df.columns:
            column_profile = {
                "data_type": str(df[column].dtype),
                "non_null_count": df[column].count(),
                "null_count": df[column].isnull().sum(),
                "unique_count": df[column].nunique(),
                "null_percentage": round(df[column].isnull().sum() / len(df) * 100, 2)
            }
            
            # Add statistics for numeric columns
            if df[column].dtype in ['int64', 'float64']:
                column_profile.update({
                    "min": df[column].min(),
                    "max": df[column].max(),
                    "mean": round(df[column].mean(), 3),
                    "std": round(df[column].std(), 3),
                    "quartiles": {
                        "25%": df[column].quantile(0.25),
                        "50%": df[column].quantile(0.50),
                        "75%": df[column].quantile(0.75)
                    }
                })
            
            # Add statistics for string columns
            elif df[column].dtype == 'object':
                str_series = df[column].astype(str)
                column_profile.update({
                    "avg_length": round(str_series.str.len().mean(), 2),
                    "min_length": str_series.str.len().min(),
                    "max_length": str_series.str.len().max(),
                    "most_common": df[column].value_counts().head(5).to_dict()
                })
            
            profile["column_profiles"][column] = column_profile
        
        # Save profiling report
        profile_file = self.profiling_dir / f"{file_path.stem}_profile.json"
        with open(profile_file, 'w') as f:
            json.dump(profile, f, indent=2, default=str)
    
    def _generate_quality_report(self, results: Dict, output_file: str):
        """Generate quality validation report"""
        # Ensure output directory exists
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Add quality summary
        report = {
            "quality_summary": {
                "validation_start": results["validation_start"],
                "validation_end": results["validation_end"],
                "duration_seconds": results["duration_seconds"],
                "total_files": results["total_files"],
                "files_validated": results["files_validated"],
                "files_failed": results["files_failed"],
                "total_records": results["total_records"],
                "overall_quality_score": results["overall_quality_score"],
                "data_quality_acceptable": results["data_quality_acceptable"],
                "status": "pass" if results["data_quality_acceptable"] else "fail"
            },
            "dimension_results": results["quality_dimensions"],
            "detailed_results": results
        }
        
        # Write quality report
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        logger.info(f"Data quality report generated: {output_file}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Validate data quality")
    parser.add_argument("--input", required=True, help="Input directory with data files")
    parser.add_argument("--output", required=True, help="Output quality metrics file path")
    parser.add_argument("--config", help="Optional quality configuration file")
    
    args = parser.parse_args()
    
    # Initialize validator
    workspace_path = Path.cwd()
    validator = DataQualityValidator(str(workspace_path))
    
    # Execute validation
    result = validator.execute(args.input, args.output, args.config)
    
    # Exit with appropriate code
    if result["status"] == "success" and result["data_quality_acceptable"]:
        exit(0)  # Success
    elif result["status"] == "success":
        exit(1)  # Warning - quality issues
    else:
        exit(2)  # Error - validation failed

if __name__ == "__main__":
    main()
