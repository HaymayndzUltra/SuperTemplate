#!/usr/bin/env python3
"""
Script: split_dataset.py
Protocol: 11 - AI Dataset Preparation & Splitting
Purpose: Split feature-engineered datasets into train/validation/test sets with stratification support
"""

import json
import logging
import argparse
from pathlib import Path
from typing import Dict, Any, Tuple
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
from datetime import datetime
import hashlib

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def calculate_checksum(file_path: str) -> str:
    """Calculate SHA-256 checksum for a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def load_dataset(input_path: str) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Load dataset from parquet or CSV file."""
    logger.info(f"Loading dataset from {input_path}")
    
    if input_path.endswith('.parquet'):
        df = pd.read_parquet(input_path)
    elif input_path.endswith('.csv'):
        df = pd.read_csv(input_path)
    else:
        raise ValueError(f"Unsupported file format: {input_path}")
    
    metadata = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "columns": list(df.columns),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()}
    }
    
    logger.info(f"Dataset loaded: {metadata['total_rows']} rows, {metadata['total_columns']} columns")
    return df, metadata


def validate_split_ratios(train_ratio: float, val_ratio: float, test_ratio: float) -> bool:
    """Validate that split ratios sum to 1.0."""
    total = train_ratio + val_ratio + test_ratio
    if abs(total - 1.0) > 0.001:
        logger.error(f"Split ratios do not sum to 1.0: {train_ratio} + {val_ratio} + {test_ratio} = {total}")
        return False
    return True


def split_dataset(
    df: pd.DataFrame,
    train_ratio: float,
    val_ratio: float,
    test_ratio: float,
    stratify_column: str = None,
    random_state: int = 42
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, Dict[str, Any]]:
    """
    Split dataset into train/validation/test sets.
    
    Args:
        df: Input dataframe
        train_ratio: Training set ratio (0.0-1.0)
        val_ratio: Validation set ratio (0.0-1.0)
        test_ratio: Test set ratio (0.0-1.0)
        stratify_column: Column to stratify by (for classification tasks)
        random_state: Random seed for reproducibility
        
    Returns:
        Tuple of (train_df, val_df, test_df, split_metadata)
    """
    logger.info(f"Splitting dataset: train={train_ratio}, val={val_ratio}, test={test_ratio}")
    
    # Validate ratios
    if not validate_split_ratios(train_ratio, val_ratio, test_ratio):
        raise ValueError("Invalid split ratios")
    
    # Determine stratification
    stratify = None
    if stratify_column and stratify_column in df.columns:
        stratify = df[stratify_column]
        logger.info(f"Applying stratified split on column: {stratify_column}")
    
    # First split: train vs (val + test)
    temp_ratio = val_ratio + test_ratio
    if stratify is not None:
        train_df, temp_df = train_test_split(
            df,
            test_size=temp_ratio,
            random_state=random_state,
            stratify=stratify
        )
    else:
        train_df, temp_df = train_test_split(
            df,
            test_size=temp_ratio,
            random_state=random_state
        )
    
    # Second split: val vs test
    val_test_ratio = test_ratio / temp_ratio
    stratify_temp = None
    if stratify_column:
        stratify_temp = temp_df[stratify_column]
    
    if stratify_temp is not None:
        val_df, test_df = train_test_split(
            temp_df,
            test_size=val_test_ratio,
            random_state=random_state,
            stratify=stratify_temp
        )
    else:
        val_df, test_df = train_test_split(
            temp_df,
            test_size=val_test_ratio,
            random_state=random_state
        )
    
    # Calculate actual ratios
    actual_train_ratio = len(train_df) / len(df)
    actual_val_ratio = len(val_df) / len(df)
    actual_test_ratio = len(test_df) / len(df)
    
    # Validate ratios are within tolerance
    tolerance = 0.02  # 2% tolerance
    train_diff = abs(actual_train_ratio - train_ratio)
    val_diff = abs(actual_val_ratio - val_ratio)
    test_diff = abs(actual_test_ratio - test_ratio)
    
    if train_diff > tolerance or val_diff > tolerance or test_diff > tolerance:
        logger.warning(f"Split ratios deviate from target:")
        logger.warning(f"  Train: target={train_ratio:.2%}, actual={actual_train_ratio:.2%}, diff={train_diff:.2%}")
        logger.warning(f"  Val: target={val_ratio:.2%}, actual={actual_val_ratio:.2%}, diff={val_diff:.2%}")
        logger.warning(f"  Test: target={test_ratio:.2%}, actual={actual_test_ratio:.2%}, diff={test_diff:.2%}")
    
    split_metadata = {
        "target_ratios": {
            "train": train_ratio,
            "validation": val_ratio,
            "test": test_ratio
        },
        "actual_ratios": {
            "train": actual_train_ratio,
            "validation": actual_val_ratio,
            "test": actual_test_ratio
        },
        "split_counts": {
            "train": len(train_df),
            "validation": len(val_df),
            "test": len(test_df)
        },
        "stratified": stratify_column is not None,
        "stratify_column": stratify_column,
        "random_state": random_state
    }
    
    logger.info(f"Split complete: train={len(train_df)}, val={len(val_df)}, test={len(test_df)}")
    
    return train_df, val_df, test_df, split_metadata


def save_datasets(
    train_df: pd.DataFrame,
    val_df: pd.DataFrame,
    test_df: pd.DataFrame,
    output_dir: str,
    version: str = "v1.0.0"
) -> Dict[str, str]:
    """Save split datasets to output directory."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Save datasets
    train_path = output_path / f"train-{version}.parquet"
    val_path = output_path / f"validation-{version}.parquet"
    test_path = output_path / f"test-{version}.parquet"
    
    logger.info(f"Saving datasets to {output_dir}")
    train_df.to_parquet(train_path)
    val_df.to_parquet(val_path)
    test_df.to_parquet(test_path)
    
    logger.info(f"Train dataset saved: {train_path}")
    logger.info(f"Validation dataset saved: {val_path}")
    logger.info(f"Test dataset saved: {test_path}")
    
    # Calculate checksums
    checksums = {
        "train": calculate_checksum(str(train_path)),
        "validation": calculate_checksum(str(val_path)),
        "test": calculate_checksum(str(test_path))
    }
    
    return {
        "train": str(train_path),
        "validation": str(val_path),
        "test": str(test_path),
        "checksums": checksums
    }


def main(input_data: str, train_ratio: float, val_ratio: float, test_ratio: float,
         stratify_column: str = None, output_dir: str = None, version: str = "v1.0.0") -> Dict[str, Any]:
    """
    Main execution function.
    
    Args:
        input_data: Path to input dataset
        train_ratio: Training set ratio
        val_ratio: Validation set ratio
        test_ratio: Test set ratio
        stratify_column: Column to stratify by
        output_dir: Output directory for split datasets
        version: Version tag for datasets
        
    Returns:
        Result dictionary with status and data
    """
    try:
        logger.info("[PROTOCOL 11 | PHASE 3 START] Dataset Preparation & Splitting")
        
        # Load dataset
        df, input_metadata = load_dataset(input_data)
        
        # Split dataset
        train_df, val_df, test_df, split_metadata = split_dataset(
            df,
            train_ratio,
            val_ratio,
            test_ratio,
            stratify_column=stratify_column
        )
        
        # Save datasets
        if output_dir is None:
            output_dir = ".artifacts/protocol-11/datasets/"
        
        dataset_paths = save_datasets(train_df, val_df, test_df, output_dir, version)
        
        result = {
            "status": "success",
            "data": {
                "input_metadata": input_metadata,
                "split_metadata": split_metadata,
                "dataset_paths": dataset_paths
            },
            "metrics": {
                "train_size": len(train_df),
                "validation_size": len(val_df),
                "test_size": len(test_df),
                "train_ratio": split_metadata["actual_ratios"]["train"],
                "validation_ratio": split_metadata["actual_ratios"]["validation"],
                "test_ratio": split_metadata["actual_ratios"]["test"]
            },
            "artifacts": [
                dataset_paths["train"],
                dataset_paths["validation"],
                dataset_paths["test"]
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        logger.info("[PROTOCOL 11 | PHASE 3 COMPLETE] Dataset splitting complete")
        logger.info(f"Result: {json.dumps(result, indent=2)}")
        
        return result
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split dataset into train/validation/test sets")
    parser.add_argument("--input-data", required=True, help="Path to input dataset")
    parser.add_argument("--train-ratio", type=float, default=0.70, help="Training set ratio")
    parser.add_argument("--val-ratio", type=float, default=0.15, help="Validation set ratio")
    parser.add_argument("--test-ratio", type=float, default=0.15, help="Test set ratio")
    parser.add_argument("--stratify-column", help="Column to stratify by")
    parser.add_argument("--output-dir", default=".artifacts/protocol-11/datasets/", help="Output directory")
    parser.add_argument("--version", default="v1.0.0", help="Version tag")
    
    args = parser.parse_args()
    
    result = main(
        input_data=args.input_data,
        train_ratio=args.train_ratio,
        val_ratio=args.val_ratio,
        test_ratio=args.test_ratio,
        stratify_column=args.stratify_column,
        output_dir=args.output_dir,
        version=args.version
    )
    
    exit(0 if result["status"] == "success" else 1)
