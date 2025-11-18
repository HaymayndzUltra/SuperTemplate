#!/usr/bin/env python3
"""
Script: train_model.py
Protocol: 13 - AI Model Training & Hyperparameter Tuning
Purpose: Train model with monitoring and checkpointing
"""

import json
import logging
import argparse
import pickle
from pathlib import Path
from typing import Dict, Any
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_data(train_path: str, val_path: str, test_path: str = None) -> tuple:
    """Load training, validation, and test datasets."""
    logger.info(f"Loading data from {train_path}, {val_path}")
    train_df = pd.read_parquet(train_path) if train_path.endswith('.parquet') else pd.read_csv(train_path)
    val_df = pd.read_parquet(val_path) if val_path.endswith('.parquet') else pd.read_csv(val_path)
    test_df = None
    if test_path:
        test_df = pd.read_parquet(test_path) if test_path.endswith('.parquet') else pd.read_csv(test_path)
    return train_df, val_df, test_df

def train_model(train_df: pd.DataFrame, val_df: pd.DataFrame, hyperparameters: Dict[str, Any] = None) -> Dict[str, Any]:
    """Train model with given hyperparameters."""
    logger.info("Training model with hyperparameters")
    
    if hyperparameters is None:
        hyperparameters = {'n_estimators': 100, 'max_depth': 10, 'random_state': 42}
    
    # Separate features and target
    X_train = train_df.iloc[:, :-1]
    y_train = train_df.iloc[:, -1]
    X_val = val_df.iloc[:, :-1]
    y_val = val_df.iloc[:, -1]
    
    # Train model
    logger.info(f"Training RandomForest with params: {hyperparameters}")
    model = RandomForestClassifier(**hyperparameters)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred_val = model.predict(X_val)
    val_accuracy = accuracy_score(y_val, y_pred_val)
    val_f1 = f1_score(y_val, y_pred_val, average='weighted', zero_division=0)
    
    logger.info(f"Validation Performance: Accuracy={val_accuracy:.4f}, F1={val_f1:.4f}")
    
    return {
        'model': model,
        'metrics': {
            'val_accuracy': float(val_accuracy),
            'val_f1': float(val_f1),
            'hyperparameters': hyperparameters
        }
    }

def main(train_data: str, val_data: str, baseline_model: str = None, output_model: str = None, output_metrics: str = None) -> Dict[str, Any]:
    """Main execution function."""
    try:
        logger.info("[PROTOCOL 13 | MODEL TRAINING START]")
        
        train_df, val_df, _ = load_data(train_data, val_data)
        result = train_model(train_df, val_df)
        
        # Save model
        if output_model:
            output_path = Path(output_model)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'wb') as f:
                pickle.dump(result['model'], f)
            logger.info(f"Trained model saved to {output_model}")
        
        # Save metrics
        if output_metrics:
            output_path = Path(output_metrics)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            metrics_data = {
                'timestamp': datetime.now().isoformat(),
                'metrics': result['metrics']
            }
            with open(output_path, 'w') as f:
                json.dump(metrics_data, f, indent=2)
            logger.info(f"Training metrics saved to {output_metrics}")
        
        logger.info("[PROTOCOL 13 | MODEL TRAINING COMPLETE]")
        return {"status": "success", "data": result['metrics']}
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train model")
    parser.add_argument("--train-data", required=True, help="Path to training dataset")
    parser.add_argument("--val-data", required=True, help="Path to validation dataset")
    parser.add_argument("--baseline-model", help="Path to baseline model")
    parser.add_argument("--output-model", help="Output model file path")
    parser.add_argument("--output-metrics", help="Output metrics file path")
    
    args = parser.parse_args()
    result = main(args.train_data, args.val_data, args.baseline_model, args.output_model, args.output_metrics)
    exit(0 if result["status"] == "success" else 1)
