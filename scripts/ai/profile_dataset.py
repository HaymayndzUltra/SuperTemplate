#!/usr/bin/env python3
"""
Script: profile_dataset.py
Protocol: 08-ai-data-collection-ingestion
Purpose: Generate comprehensive data profiling reports
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
import matplotlib.pyplot as plt
import seaborn as sns

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatasetProfiler:
    """Main class for data profiling"""
    
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.artifacts_dir = self.workspace / ".artifacts"
        self.protocol_08_dir = self.artifacts_dir / "protocol-08-ai-data-collection-ingestion"
        self.profiling_dir = self.protocol_08_dir / "profiling-reports"
        
        # Ensure directories exist
        self.profiling_dir.mkdir(parents=True, exist_ok=True)
        
    def execute(self, input_dir: str, output_dir: str) -> Dict:
        """
        Main execution method
        
        Args:
            input_dir: Directory containing data files to profile
            output_dir: Directory for profiling reports
            
        Returns:
            Dict: Execution results with status and profiling info
        """
        try:
            # Profile all datasets
            results = self._profile_datasets(input_dir, output_dir)
            
            # Generate summary report
            self._generate_summary_report(results, output_dir)
            
            return {
                "status": "success",
                "results": results,
                "datasets_profiled": results.get("datasets_profiled", 0),
                "total_records_analyzed": results.get("total_records_analyzed", 0)
            }
            
        except Exception as e:
            logger.error(f"Data profiling failed: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "datasets_profiled": 0,
                "total_records_analyzed": 0
            }
    
    def _profile_datasets(self, input_dir: str, output_dir: str) -> Dict:
        """Profile all datasets in input directory"""
        results = {
            "profiling_start": datetime.now().isoformat(),
            "input_directory": input_dir,
            "output_directory": output_dir,
            "total_files": 0,
            "datasets_profiled": 0,
            "datasets_failed": 0,
            "total_records_analyzed": 0,
            "total_size_mb": 0.0,
            "dataset_details": [],
            "profiling_end": "",
            "duration_seconds": 0
        }
        
        input_path = Path(input_dir)
        output_path = Path(output_dir)
        
        if not input_path.exists():
            raise FileNotFoundError(f"Input directory not found: {input_dir}")
        
        # Ensure output directory exists
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Find all parquet files
        data_files = list(input_path.glob("*.parquet"))
        results["total_files"] = len(data_files)
        
        logger.info(f"Profiling {len(data_files)} datasets")
        
        # Profile each file
        for file_path in data_files:
            dataset_result = self._profile_single_dataset(file_path, output_path)
            results["dataset_details"].append(dataset_result)
            
            if dataset_result["status"] == "success":
                results["datasets_profiled"] += 1
                results["total_records_analyzed"] += dataset_result.get("record_count", 0)
                results["total_size_mb"] += dataset_result.get("size_mb", 0.0)
            else:
                results["datasets_failed"] += 1
        
        # Calculate final results
        results["profiling_end"] = datetime.now().isoformat()
        start_time = datetime.fromisoformat(results["profiling_start"])
        end_time = datetime.fromisoformat(results["profiling_end"])
        results["duration_seconds"] = (end_time - start_time).total_seconds()
        
        logger.info(f"Profiling completed: {results['datasets_profiled']}/{results['total_files']} datasets profiled")
        
        return results
    
    def _profile_single_dataset(self, file_path: Path, output_dir: Path) -> Dict:
        """Profile a single dataset"""
        result = {
            "file_name": file_path.name,
            "status": "error",
            "message": "",
            "record_count": 0,
            "column_count": 0,
            "size_mb": 0.0,
            "profile_file": "",
            "profiling_timestamp": datetime.now().isoformat()
        }
        
        try:
            # Load data
            df = pd.read_parquet(file_path)
            result["record_count"] = len(df)
            result["column_count"] = len(df.columns)
            result["size_mb"] = round(file_path.stat().st_size / (1024 * 1024), 2)
            
            # Generate profile
            profile = self._generate_dataset_profile(df, file_path)
            
            # Save profile
            profile_file = output_dir / f"{file_path.stem}_profile.json"
            with open(profile_file, 'w') as f:
                json.dump(profile, f, indent=2, default=str)
            
            result["profile_file"] = str(profile_file)
            result["status"] = "success"
            result["message"] = "Dataset profiled successfully"
            
            # Generate visualizations
            self._generate_visualizations(df, output_dir, file_path.stem)
            
        except Exception as e:
            result["message"] = f"Profiling error: {str(e)}"
        
        return result
    
    def _generate_dataset_profile(self, df: pd.DataFrame, file_path: Path) -> Dict:
        """Generate comprehensive dataset profile"""
        profile = {
            "dataset_info": {
                "file_name": file_path.name,
                "file_size_mb": round(file_path.stat().st_size / (1024 * 1024), 2),
                "record_count": len(df),
                "column_count": len(df.columns),
                "memory_usage_mb": round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2),
                "profiled_at": datetime.now().isoformat()
            },
            "data_quality": {
                "completeness": self._calculate_completeness(df),
                "duplicate_rows": df.duplicated().sum(),
                "duplicate_percentage": round(df.duplicated().sum() / len(df) * 100, 2) if len(df) > 0 else 0
            },
            "column_profiles": {},
            "data_types": {},
            "statistical_summary": {},
            "correlation_matrix": {},
            "data_distribution": {}
        }
        
        # Profile each column
        for column in df.columns:
            column_profile = self._profile_column(df[column])
            profile["column_profiles"][column] = column_profile
        
        # Data type summary
        profile["data_types"] = df.dtypes.astype(str).to_dict()
        
        # Statistical summary for numeric columns
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        if len(numeric_columns) > 0:
            profile["statistical_summary"] = df[numeric_columns].describe().to_dict()
            
            # Correlation matrix
            if len(numeric_columns) > 1:
                correlation_matrix = df[numeric_columns].corr()
                profile["correlation_matrix"] = correlation_matrix.round(3).to_dict()
        
        # Data distribution analysis
        profile["data_distribution"] = self._analyze_data_distribution(df)
        
        return profile
    
    def _profile_column(self, series: pd.Series) -> Dict:
        """Profile a single column"""
        profile = {
            "data_type": str(series.dtype),
            "non_null_count": series.count(),
            "null_count": series.isnull().sum(),
            "null_percentage": round(series.isnull().sum() / len(series) * 100, 2) if len(series) > 0 else 0,
            "unique_count": series.nunique(),
            "unique_percentage": round(series.nunique() / len(series) * 100, 2) if len(series) > 0 else 0
        }
        
        # Numeric column statistics
        if pd.api.types.is_numeric_dtype(series):
            profile.update({
                "min": series.min(),
                "max": series.max(),
                "mean": round(series.mean(), 3),
                "median": series.median(),
                "std": round(series.std(), 3),
                "var": round(series.var(), 3),
                "skewness": round(series.skew(), 3),
                "kurtosis": round(series.kurtosis(), 3),
                "quartiles": {
                    "25%": series.quantile(0.25),
                    "50%": series.quantile(0.50),
                    "75%": series.quantile(0.75)
                },
                "outliers": self._detect_outliers(series)
            })
        
        # String column statistics
        elif series.dtype == 'object':
            str_series = series.astype(str)
            profile.update({
                "avg_length": round(str_series.str.len().mean(), 2),
                "min_length": str_series.str.len().min(),
                "max_length": str_series.str.len().max(),
                "empty_strings": (str_series == '').sum(),
                "whitespace_strings": str_series.str.strip().eq('').sum(),
                "most_common": series.value_counts().head(10).to_dict(),
                "pattern_analysis": self._analyze_string_patterns(str_series)
            })
        
        # Datetime column statistics
        elif pd.api.types.is_datetime64_any_dtype(series):
            profile.update({
                "min_date": series.min().isoformat() if pd.notna(series.min()) else None,
                "max_date": series.max().isoformat() if pd.notna(series.max()) else None,
                "date_range_days": (series.max() - series.min()).days if pd.notna(series.min()) and pd.notna(series.max()) else 0,
                "frequency": self._analyze_datetime_frequency(series)
            })
        
        return profile
    
    def _calculate_completeness(self, df: pd.DataFrame) -> Dict:
        """Calculate completeness metrics"""
        completeness = {}
        
        # Overall completeness
        total_values = len(df) * len(df.columns)
        non_null_values = df.count().sum()
        completeness["overall"] = round(non_null_values / total_values, 3) if total_values > 0 else 0.0
        
        # Column-wise completeness
        completeness["by_column"] = {}
        for column in df.columns:
            column_completeness = df[column].count() / len(df)
            completeness["by_column"][column] = round(column_completeness, 3)
        
        # Completeness distribution
        completeness_scores = list(completeness["by_column"].values())
        completeness["distribution"] = {
            "min": min(completeness_scores) if completeness_scores else 0.0,
            "max": max(completeness_scores) if completeness_scores else 0.0,
            "mean": round(np.mean(completeness_scores), 3) if completeness_scores else 0.0,
            "median": round(np.median(completeness_scores), 3) if completeness_scores else 0.0
        }
        
        return completeness
    
    def _detect_outliers(self, series: pd.Series) -> Dict:
        """Detect outliers using IQR method"""
        try:
            Q1 = series.quantile(0.25)
            Q3 = series.quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = series[(series < lower_bound) | (series > upper_bound)]
            
            return {
                "count": len(outliers),
                "percentage": round(len(outliers) / len(series) * 100, 2) if len(series) > 0 else 0,
                "lower_bound": lower_bound,
                "upper_bound": upper_bound,
                "method": "IQR (1.5 * IQR)"
            }
        except:
            return {"count": 0, "percentage": 0, "method": "IQR (1.5 * IQR)", "error": "Calculation failed"}
    
    def _analyze_string_patterns(self, series: pd.Series) -> Dict:
        """Analyze patterns in string data"""
        patterns = {
            "numeric_strings": 0,
            "email_patterns": 0,
            "url_patterns": 0,
            "phone_patterns": 0,
            "date_patterns": 0
        }
        
        try:
            # Numeric strings
            numeric_mask = series.str.match(r'^\d+$', na=False)
            patterns["numeric_strings"] = numeric_mask.sum()
            
            # Email patterns (basic)
            email_mask = series.str.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', na=False)
            patterns["email_patterns"] = email_mask.sum()
            
            # URL patterns (basic)
            url_mask = series.str.match(r'^https?://[^\s/$.?#].[^\s]*$', na=False)
            patterns["url_patterns"] = url_mask.sum()
            
            # Phone patterns (basic)
            phone_mask = series.str.match(r'^\+?[\d\s\-\(\)]{10,}$', na=False)
            patterns["phone_patterns"] = phone_mask.sum()
            
            # Date patterns (basic)
            date_mask = series.str.match(r'^\d{4}-\d{2}-\d{2}$', na=False)
            patterns["date_patterns"] = date_mask.sum()
            
        except Exception as e:
            patterns["error"] = str(e)
        
        return patterns
    
    def _analyze_datetime_frequency(self, series: pd.Series) -> Dict:
        """Analyze frequency patterns in datetime data"""
        try:
            # Remove null values
            clean_series = series.dropna()
            
            if len(clean_series) == 0:
                return {"error": "No valid datetime values"}
            
            # Calculate time differences
            time_diffs = clean_series.sort_values().diff().dropna()
            
            return {
                "avg_interval_hours": round(time_diffs.mean().total_seconds() / 3600, 2),
                "min_interval_hours": round(time_diffs.min().total_seconds() / 3600, 2),
                "max_interval_hours": round(time_diffs.max().total_seconds() / 3600, 2),
                "regular_frequency": time_diffs.std().total_seconds() / 3600 < 1.0  # Less than 1 hour std dev
            }
        except Exception as e:
            return {"error": str(e)}
    
    def _analyze_data_distribution(self, df: pd.DataFrame) -> Dict:
        """Analyze overall data distribution"""
        distribution = {
            "numeric_columns": 0,
            "categorical_columns": 0,
            "datetime_columns": 0,
            "text_columns": 0,
            "mixed_types": False
        }
        
        for column in df.columns:
            dtype = df[column].dtype
            if pd.api.types.is_numeric_dtype(dtype):
                distribution["numeric_columns"] += 1
            elif dtype == 'object':
                distribution["categorical_columns"] += 1
            elif pd.api.types.is_datetime64_any_dtype(dtype):
                distribution["datetime_columns"] += 1
            else:
                distribution["text_columns"] += 1
        
        total_columns = len(df.columns)
        distribution["mixed_types"] = len([v for v in distribution.values() if isinstance(v, int) and v > 0]) > 1
        
        return distribution
    
    def _generate_visualizations(self, df: pd.DataFrame, output_dir: Path, dataset_name: str):
        """Generate visualization plots"""
        try:
            # Set up matplotlib
            plt.style.use('default')
            
            # Create plots directory
            plots_dir = output_dir / "plots"
            plots_dir.mkdir(exist_ok=True)
            
            # Numeric columns histograms
            numeric_columns = df.select_dtypes(include=[np.number]).columns
            
            for column in numeric_columns[:5]:  # Limit to first 5 numeric columns
                plt.figure(figsize=(10, 6))
                df[column].hist(bins=50, alpha=0.7)
                plt.title(f'Distribution of {column}')
                plt.xlabel(column)
                plt.ylabel('Frequency')
                plt.tight_layout()
                plt.savefig(plots_dir / f"{dataset_name}_{column}_histogram.png", dpi=150, bbox_inches='tight')
                plt.close()
            
            # Correlation heatmap
            if len(numeric_columns) > 1:
                plt.figure(figsize=(12, 8))
                correlation_matrix = df[numeric_columns].corr()
                sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
                plt.title('Correlation Matrix')
                plt.tight_layout()
                plt.savefig(plots_dir / f"{dataset_name}_correlation_heatmap.png", dpi=150, bbox_inches='tight')
                plt.close()
            
            logger.info(f"Generated visualizations for {dataset_name}")
            
        except Exception as e:
            logger.warning(f"Failed to generate visualizations for {dataset_name}: {str(e)}")
    
    def _generate_summary_report(self, results: Dict, output_dir: str):
        """Generate profiling summary report"""
        # Ensure output directory exists
        output_path = Path(output_dir)
        
        # Create summary report
        summary = {
            "profiling_summary": {
                "profiling_start": results["profiling_start"],
                "profiling_end": results["profiling_end"],
                "duration_seconds": results["duration_seconds"],
                "input_directory": results["input_directory"],
                "output_directory": results["output_directory"],
                "total_files": results["total_files"],
                "datasets_profiled": results["datasets_profiled"],
                "datasets_failed": results["datasets_failed"],
                "total_records_analyzed": results["total_records_analyzed"],
                "total_size_mb": round(results["total_size_mb"], 2),
                "success_rate": round(results["datasets_profiled"] / results["total_files"] * 100, 2) if results["total_files"] > 0 else 0
            },
            "dataset_results": results["dataset_details"],
            "detailed_results": results
        }
        
        # Write summary report
        summary_file = output_path / "profiling_summary.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        logger.info(f"Profiling summary report generated: {summary_file}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Profile datasets")
    parser.add_argument("--input", required=True, help="Input directory with data files")
    parser.add_argument("--output", required=True, help="Output directory for profiling reports")
    
    args = parser.parse_args()
    
    # Initialize profiler
    workspace_path = Path.cwd()
    profiler = DatasetProfiler(str(workspace_path))
    
    # Execute profiling
    result = profiler.execute(args.input, args.output)
    
    # Exit with appropriate code
    if result["status"] == "success":
        exit(0)  # Success
    else:
        exit(2)  # Error - profiling failed

if __name__ == "__main__":
    main()
