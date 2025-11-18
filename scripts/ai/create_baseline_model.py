#!/usr/bin/env python3
"""
Script: create_baseline_model.py
Protocol: 12 - AI Algorithm Selection & Baseline Model
Purpose: Create and train baseline model with selected algorithm
"""

import json
import logging
import argparse
import pickle
from pathlib import Path
from typing import Dict, Any
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_data(train_path: str, val_path: str) -> tuple:
    """Load training and validation datasets."""
    logger.info(f"Loading data from {train_path} and {val_path}")
    train_df = pd.read_parquet(train_path) if train_path.endswith('.parquet') else pd.read_csv(train_path)
    val_df = pd.read_parquet(val_path) if val_path.endswith('.parquet') else pd.read_csv(val_path)
    return train_df, val_df

def create_baseline_model(train_df: pd.DataFrame, val_df: pd.DataFrame, algorithm: str = "random-forest") -> Dict[str, Any]:
    """Create and train baseline model."""
    logger.info(f"Creating baseline model with {algorithm}")
    
    # Separate features and target
    X_train = train_df.iloc[:, :-1]
    y_train = train_df.iloc[:, -1]
    X_val = val_df.iloc[:, :-1]
    y_val = val_df.iloc[:, -1]
    
    # Select algorithm
    if algorithm == "random-forest":
        model = RandomForestClassifier(n_estimators=100, random_state=42)
    elif algorithm == "logistic-regression":
        model = LogisticRegression(max_iter=1000, random_state=42)
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")
    
    # Train model
    logger.info("Training baseline model...")
    model.fit(X_train, y_train)
    
    # Evaluate on validation set
    y_pred = model.predict(X_val)
    accuracy = accuracy_score(y_val, y_pred)
    precision = precision_score(y_val, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_val, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_val, y_pred, average='weighted', zero_division=0)
    
    # Calculate random baseline
    random_baseline = 1.0 / len(set(y_val))
    
    logger.info(f"Baseline Performance: Accuracy={accuracy:.4f}, F1={f1:.4f}")
    logger.info(f"Random Baseline: {random_baseline:.4f}")
    
    return {
        'model': model,
        'metrics': {
            'accuracy': float(accuracy),
            'precision': float(precision),
            'recall': float(recall),
            'f1_score': float(f1),
            'random_baseline': float(random_baseline),
            'above_random': accuracy > random_baseline
        }
    }

def main(train_data: str, val_data: str, algorithm: str = "random-forest", output_model: str = None, output_metrics: str = None) -> Dict[str, Any]:
    """Main execution function."""
    try:
        logger.info("[PROTOCOL 12 | BASELINE MODEL CREATION START]")
        
        train_df, val_df = load_data(train_data, val_data)
        result = create_baseline_model(train_df, val_df, algorithm)
        
        # Save model
        if output_model:
            output_path = Path(output_model)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'wb') as f:
                pickle.dump(result['model'], f)
            logger.info(f"Baseline model saved to {output_model}")
        
        # Save metrics
        if output_metrics:
            output_path = Path(output_metrics)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            metrics_data = {
                'timestamp': datetime.now().isoformat(),
                'algorithm': algorithm,
                'metrics': result['metrics']
            }
            with open(output_path, 'w') as f:
                json.dump(metrics_data, f, indent=2)
            logger.info(f"Baseline metrics saved to {output_metrics}")
        
        logger.info("[PROTOCOL 12 | BASELINE MODEL CREATION COMPLETE]")
        return {"status": "success", "data": result['metrics']}
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create baseline model")
    parser.add_argument("--train-data", required=True, help="Path to training dataset")
    parser.add_argument("--val-data", required=True, help="Path to validation dataset")
    parser.add_argument("--algorithm", default="random-forest", help="Algorithm to use")
    parser.add_argument("--output-model", help="Output model file path")
    parser.add_argument("--output-metrics", help="Output metrics file path")
    
    args = parser.parse_args()
    result = main(args.train_data, args.val_data, args.algorithm, args.output_model, args.output_metrics)
    exit(0 if result["status"] == "success" else 1)
