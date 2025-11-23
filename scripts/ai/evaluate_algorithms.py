#!/usr/bin/env python3
"""
Script: evaluate_algorithms.py
Protocol: 12 - AI Algorithm Selection & Baseline Model
Purpose: Evaluate multiple algorithms on training data and create evaluation matrix
"""

import json
import logging
import argparse
from pathlib import Path
from typing import Dict, Any
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
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

def evaluate_algorithms(train_df: pd.DataFrame, val_df: pd.DataFrame, problem_type: str = "classification") -> Dict[str, Any]:
    """Evaluate multiple algorithms."""
    logger.info(f"Evaluating algorithms for {problem_type} task")
    
    # Separate features and target
    X_train = train_df.iloc[:, :-1]
    y_train = train_df.iloc[:, -1]
    X_val = val_df.iloc[:, :-1]
    y_val = val_df.iloc[:, -1]
    
    # Define algorithms
    algorithms = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42),
        'KNN': KNeighborsClassifier(n_neighbors=5),
        'SVM': SVC(kernel='rbf', random_state=42)
    }
    
    results = []
    for name, model in algorithms.items():
        try:
            logger.info(f"Training {name}...")
            model.fit(X_train, y_train)
            y_pred = model.predict(X_val)
            
            accuracy = accuracy_score(y_val, y_pred)
            precision = precision_score(y_val, y_pred, average='weighted', zero_division=0)
            recall = recall_score(y_val, y_pred, average='weighted', zero_division=0)
            f1 = f1_score(y_val, y_pred, average='weighted', zero_division=0)
            
            results.append({
                'algorithm': name,
                'accuracy': float(accuracy),
                'precision': float(precision),
                'recall': float(recall),
                'f1_score': float(f1),
                'status': 'success'
            })
            logger.info(f"{name}: Accuracy={accuracy:.4f}, F1={f1:.4f}")
        except Exception as e:
            logger.error(f"Error training {name}: {e}")
            results.append({'algorithm': name, 'status': 'failed', 'error': str(e)})
    
    return {
        'timestamp': datetime.now().isoformat(),
        'problem_type': problem_type,
        'algorithms_evaluated': len([r for r in results if r['status'] == 'success']),
        'results': results
    }

def main(train_data: str, val_data: str, problem_type: str = "classification", output_matrix: str = None) -> Dict[str, Any]:
    """Main execution function."""
    try:
        logger.info("[PROTOCOL 12 | ALGORITHM EVALUATION START]")
        
        train_df, val_df = load_data(train_data, val_data)
        evaluation_results = evaluate_algorithms(train_df, val_df, problem_type)
        
        if output_matrix:
            output_path = Path(output_matrix)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w') as f:
                json.dump(evaluation_results, f, indent=2)
            logger.info(f"Evaluation matrix saved to {output_matrix}")
        
        logger.info("[PROTOCOL 12 | ALGORITHM EVALUATION COMPLETE]")
        return {"status": "success", "data": evaluation_results}
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate multiple algorithms")
    parser.add_argument("--train-data", required=True, help="Path to training dataset")
    parser.add_argument("--val-data", required=True, help="Path to validation dataset")
    parser.add_argument("--problem-type", default="classification", help="Problem type")
    parser.add_argument("--output-matrix", help="Output matrix file path")
    
    args = parser.parse_args()
    result = main(args.train_data, args.val_data, args.problem_type, args.output_matrix)
    exit(0 if result["status"] == "success" else 1)
