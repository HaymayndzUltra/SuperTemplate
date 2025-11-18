#!/usr/bin/env python3
"""
Script: check_data_leakage.py
Protocol: 11 - AI Dataset Preparation & Splitting
Purpose: Detect data leakage between train/validation/test sets
"""

import json
import logging
import argparse
from pathlib import Path
from typing import Dict, Any, List, Tuple
import pandas as pd
import numpy as np
from scipy.stats import spearmanr, pearsonr
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_datasets(train_path: str, val_path: str, test_path: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load train/validation/test datasets."""
    logger.info("Loading datasets for leakage detection")
    
    train_df = pd.read_parquet(train_path) if train_path.endswith('.parquet') else pd.read_csv(train_path)
    val_df = pd.read_parquet(val_path) if val_path.endswith('.parquet') else pd.read_csv(val_path)
    test_df = pd.read_parquet(test_path) if test_path.endswith('.parquet') else pd.read_csv(test_path)
    
    logger.info(f"Datasets loaded: train={len(train_df)}, val={len(val_df)}, test={len(test_df)}")
    
    return train_df, val_df, test_df


def check_row_overlap(df1: pd.DataFrame, df2: pd.DataFrame, name1: str, name2: str) -> Dict[str, Any]:
    """Check for row overlap between two datasets."""
    logger.info(f"Checking row overlap between {name1} and {name2}")
    
    # Convert to tuples for comparison
    df1_rows = set(map(tuple, df1.values))
    df2_rows = set(map(tuple, df2.values))
    
    overlap = df1_rows & df2_rows
    overlap_count = len(overlap)
    overlap_ratio = overlap_count / len(df1) if len(df1) > 0 else 0
    
    result = {
        "comparison": f"{name1} vs {name2}",
        "overlap_count": overlap_count,
        "overlap_ratio": overlap_ratio,
        "leakage_detected": overlap_count > 0
    }
    
    if overlap_count > 0:
        logger.warning(f"Row overlap detected: {overlap_count} rows ({overlap_ratio:.2%})")
    else:
        logger.info(f"No row overlap detected between {name1} and {name2}")
    
    return result


def check_feature_target_correlation(
    df: pd.DataFrame,
    target_column: str,
    name: str,
    correlation_threshold: float = 0.95
) -> Dict[str, Any]:
    """Check for suspicious feature-target correlations indicating leakage."""
    logger.info(f"Checking feature-target correlations in {name}")
    
    if target_column not in df.columns:
        logger.warning(f"Target column '{target_column}' not found in {name}")
        return {"error": f"Target column '{target_column}' not found"}
    
    target = df[target_column]
    suspicious_features = []
    
    for col in df.columns:
        if col == target_column:
            continue
        
        try:
            # Skip non-numeric columns
            if not pd.api.types.is_numeric_dtype(df[col]):
                continue
            
            # Calculate correlation
            correlation, _ = pearsonr(df[col].fillna(0), target.fillna(0))
            
            # Flag suspicious correlations
            if abs(correlation) > correlation_threshold:
                suspicious_features.append({
                    "feature": col,
                    "correlation": correlation,
                    "suspicious": True
                })
                logger.warning(f"Suspicious correlation in {name}: {col} = {correlation:.4f}")
        
        except Exception as e:
            logger.debug(f"Could not calculate correlation for {col}: {e}")
            continue
    
    result = {
        "dataset": name,
        "target_column": target_column,
        "suspicious_features": suspicious_features,
        "leakage_detected": len(suspicious_features) > 0,
        "correlation_threshold": correlation_threshold
    }
    
    return result


def check_temporal_leakage(
    train_df: pd.DataFrame,
    val_df: pd.DataFrame,
    test_df: pd.DataFrame,
    time_column: str = None
) -> Dict[str, Any]:
    """Check for temporal leakage (future information in training data)."""
    logger.info("Checking for temporal leakage")
    
    if time_column is None or time_column not in train_df.columns:
        logger.info("No time column specified, skipping temporal leakage check")
        return {"temporal_leakage_check": "skipped", "reason": "no_time_column"}
    
    try:
        train_max_time = pd.to_datetime(train_df[time_column]).max()
        val_min_time = pd.to_datetime(val_df[time_column]).min()
        test_min_time = pd.to_datetime(test_df[time_column]).min()
        
        temporal_leakage = False
        issues = []
        
        # Check if validation data has earlier timestamps than training data
        if val_min_time < train_max_time:
            temporal_leakage = True
            issues.append(f"Validation data contains earlier timestamps than training data")
            logger.warning(f"Temporal leakage: val_min_time ({val_min_time}) < train_max_time ({train_max_time})")
        
        # Check if test data has earlier timestamps than training data
        if test_min_time < train_max_time:
            temporal_leakage = True
            issues.append(f"Test data contains earlier timestamps than training data")
            logger.warning(f"Temporal leakage: test_min_time ({test_min_time}) < train_max_time ({train_max_time})")
        
        result = {
            "temporal_leakage_check": "completed",
            "time_column": time_column,
            "train_max_time": str(train_max_time),
            "val_min_time": str(val_min_time),
            "test_min_time": str(test_min_time),
            "temporal_leakage_detected": temporal_leakage,
            "issues": issues
        }
        
        return result
        
    except Exception as e:
        logger.error(f"Error checking temporal leakage: {e}")
        return {"temporal_leakage_check": "error", "error": str(e)}


def check_information_leakage(
    train_df: pd.DataFrame,
    val_df: pd.DataFrame,
    test_df: pd.DataFrame
) -> Dict[str, Any]:
    """Check for information leakage through feature statistics."""
    logger.info("Checking for information leakage through feature statistics")
    
    leakage_indicators = []
    
    # Get numeric columns
    numeric_cols = train_df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        try:
            train_mean = train_df[col].mean()
            train_std = train_df[col].std()
            
            val_mean = val_df[col].mean()
            test_mean = test_df[col].mean()
            
            # Check if validation/test means are suspiciously close to training mean
            # This could indicate leakage or preprocessing issues
            val_deviation = abs(val_mean - train_mean) / (train_std + 1e-10)
            test_deviation = abs(test_mean - train_mean) / (train_std + 1e-10)
            
            # Flag if deviation is very small (< 0.1 std)
            if val_deviation < 0.1 or test_deviation < 0.1:
                leakage_indicators.append({
                    "feature": col,
                    "train_mean": train_mean,
                    "train_std": train_std,
                    "val_mean": val_mean,
                    "test_mean": test_mean,
                    "val_deviation_std": val_deviation,
                    "test_deviation_std": test_deviation,
                    "indicator": "suspiciously_similar_distribution"
                })
                logger.warning(f"Information leakage indicator in {col}: val_deviation={val_deviation:.4f}, test_deviation={test_deviation:.4f}")
        
        except Exception as e:
            logger.debug(f"Could not analyze {col}: {e}")
            continue
    
    result = {
        "information_leakage_check": "completed",
        "leakage_indicators": leakage_indicators,
        "potential_leakage": len(leakage_indicators) > 0
    }
    
    return result


def main(
    train_data: str,
    val_data: str,
    test_data: str,
    target_column: str,
    time_column: str = None,
    output_report: str = None,
    correlation_threshold: float = 0.95
) -> Dict[str, Any]:
    """
    Main execution function.
    
    Args:
        train_data: Path to training dataset
        val_data: Path to validation dataset
        test_data: Path to test dataset
        target_column: Name of target column
        time_column: Name of time column (optional)
        output_report: Path to save report
        correlation_threshold: Correlation threshold for suspicious features
        
    Returns:
        Result dictionary with leakage detection results
    """
    try:
        logger.info("[PROTOCOL 11 | DATA LEAKAGE CHECK START]")
        
        # Load datasets
        train_df, val_df, test_df = load_datasets(train_data, val_data, test_data)
        
        # Perform leakage checks
        checks = {
            "row_overlap_train_val": check_row_overlap(train_df, val_df, "train", "validation"),
            "row_overlap_train_test": check_row_overlap(train_df, test_df, "train", "test"),
            "row_overlap_val_test": check_row_overlap(val_df, test_df, "validation", "test"),
            "feature_target_correlation_train": check_feature_target_correlation(train_df, target_column, "train", correlation_threshold),
            "feature_target_correlation_val": check_feature_target_correlation(val_df, target_column, "validation", correlation_threshold),
            "feature_target_correlation_test": check_feature_target_correlation(test_df, target_column, "test", correlation_threshold),
            "temporal_leakage": check_temporal_leakage(train_df, val_df, test_df, time_column),
            "information_leakage": check_information_leakage(train_df, val_df, test_df)
        }
        
        # Aggregate results
        leakage_detected = any([
            checks["row_overlap_train_val"]["leakage_detected"],
            checks["row_overlap_train_test"]["leakage_detected"],
            checks["row_overlap_val_test"]["leakage_detected"],
            checks["feature_target_correlation_train"]["leakage_detected"],
            checks["feature_target_correlation_val"]["leakage_detected"],
            checks["feature_target_correlation_test"]["leakage_detected"],
            checks["temporal_leakage"].get("temporal_leakage_detected", False),
            checks["information_leakage"]["potential_leakage"]
        ])
        
        result = {
            "status": "success" if not leakage_detected else "warning",
            "leakage_detected": leakage_detected,
            "checks": checks,
            "summary": {
                "total_checks": len(checks),
                "leakage_indicators": sum([
                    checks["row_overlap_train_val"]["leakage_detected"],
                    checks["row_overlap_train_test"]["leakage_detected"],
                    checks["row_overlap_val_test"]["leakage_detected"],
                    checks["feature_target_correlation_train"]["leakage_detected"],
                    checks["feature_target_correlation_val"]["leakage_detected"],
                    checks["feature_target_correlation_test"]["leakage_detected"],
                    checks["temporal_leakage"].get("temporal_leakage_detected", False),
                    checks["information_leakage"]["potential_leakage"]
                ])
            },
            "timestamp": datetime.now().isoformat()
        }
        
        # Save report if output path provided
        if output_report:
            output_path = Path(output_report)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w') as f:
                json.dump(result, f, indent=2)
            logger.info(f"Report saved to {output_report}")
        
        logger.info(f"[PROTOCOL 11 | DATA LEAKAGE CHECK COMPLETE] Leakage detected: {leakage_detected}")
        
        return result
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check for data leakage between train/validation/test sets")
    parser.add_argument("--train-data", required=True, help="Path to training dataset")
    parser.add_argument("--val-data", required=True, help="Path to validation dataset")
    parser.add_argument("--test-data", required=True, help="Path to test dataset")
    parser.add_argument("--target-column", required=True, help="Name of target column")
    parser.add_argument("--time-column", help="Name of time column (optional)")
    parser.add_argument("--output-report", help="Path to save report")
    parser.add_argument("--correlation-threshold", type=float, default=0.95, help="Correlation threshold for suspicious features")
    
    args = parser.parse_args()
    
    result = main(
        train_data=args.train_data,
        val_data=args.val_data,
        test_data=args.test_data,
        target_column=args.target_column,
        time_column=args.time_column,
        output_report=args.output_report,
        correlation_threshold=args.correlation_threshold
    )
    
    exit(0 if result["status"] == "success" else 1)
