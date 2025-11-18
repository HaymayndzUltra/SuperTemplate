#!/usr/bin/env python3
"""
Script: tune_hyperparameters.py
Protocol: 13 - AI Model Training & Hyperparameter Tuning
Purpose: Hyperparameter optimization using Bayesian/Grid/Random search
"""

import json, logging, argparse, pickle
from pathlib import Path
from typing import Dict, Any
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import accuracy_score, f1_score
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_data(train_path: str, val_path: str):
    train_df = pd.read_parquet(train_path) if train_path.endswith('.parquet') else pd.read_csv(train_path)
    val_df = pd.read_parquet(val_path) if val_path.endswith('.parquet') else pd.read_csv(val_path)
    return train_df, val_df

def tune_hyperparameters(train_df: pd.DataFrame, val_df: pd.DataFrame, method: str = "random"):
    logger.info(f"Tuning hyperparameters using {method} search")
    X_train, y_train = train_df.iloc[:, :-1], train_df.iloc[:, -1]
    X_val, y_val = val_df.iloc[:, :-1], val_df.iloc[:, -1]
    
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [5, 10, 15, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    
    if method == "grid":
        search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, n_jobs=-1)
    else:
        search = RandomizedSearchCV(RandomForestClassifier(random_state=42), param_grid, n_iter=20, cv=3, n_jobs=-1, random_state=42)
    
    search.fit(X_train, y_train)
    best_model = search.best_estimator_
    y_pred = best_model.predict(X_val)
    
    return {
        'best_params': search.best_params_,
        'best_score': search.best_score_,
        'val_accuracy': float(accuracy_score(y_val, y_pred)),
        'val_f1': float(f1_score(y_val, y_pred, average='weighted', zero_division=0))
    }

def main(train_data: str, val_data: str, search_space: str = None, output_results: str = None, optimization_method: str = "random"):
    try:
        logger.info("[PROTOCOL 13 | HYPERPARAMETER TUNING START]")
        train_df, val_df = load_data(train_data, val_data)
        results = tune_hyperparameters(train_df, val_df, optimization_method)
        
        if output_results:
            Path(output_results).parent.mkdir(parents=True, exist_ok=True)
            with open(output_results, 'w') as f:
                json.dump({'timestamp': datetime.now().isoformat(), 'results': results}, f, indent=2)
            logger.info(f"Tuning results saved to {output_results}")
        
        logger.info("[PROTOCOL 13 | HYPERPARAMETER TUNING COMPLETE]")
        return {"status": "success", "data": results}
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tune hyperparameters")
    parser.add_argument("--train-data", required=True)
    parser.add_argument("--val-data", required=True)
    parser.add_argument("--search-space")
    parser.add_argument("--output-results")
    parser.add_argument("--optimization-method", default="random")
    args = parser.parse_args()
    result = main(args.train_data, args.val_data, args.search_space, args.output_results, args.optimization_method)
    exit(0 if result["status"] == "success" else 1)
