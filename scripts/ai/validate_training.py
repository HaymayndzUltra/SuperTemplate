#!/usr/bin/env python3
"""
Script: validate_training.py
Protocol: 13 - AI Model Training & Hyperparameter Tuning
Purpose: Validate training results and generate report
"""

import json, logging, argparse, pickle
from pathlib import Path
from typing import Dict, Any
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_data(test_path: str):
    test_df = pd.read_parquet(test_path) if test_path.endswith('.parquet') else pd.read_csv(test_path)
    return test_df

def validate_training(model, test_df: pd.DataFrame, baseline_metrics: Dict[str, Any] = None):
    logger.info("Validating training results")
    X_test, y_test = test_df.iloc[:, :-1], test_df.iloc[:, -1]
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
    
    improvement = None
    if baseline_metrics and 'accuracy' in baseline_metrics:
        baseline_acc = baseline_metrics.get('accuracy', 0)
        improvement = ((accuracy - baseline_acc) / baseline_acc * 100) if baseline_acc > 0 else 0
    
    return {
        'test_accuracy': float(accuracy),
        'test_precision': float(precision),
        'test_recall': float(recall),
        'test_f1': float(f1),
        'improvement_pct': float(improvement) if improvement else None
    }

def main(model: str, test_data: str, baseline_metrics: str = None, output_report: str = None):
    try:
        logger.info("[PROTOCOL 13 | TRAINING VALIDATION START]")
        
        with open(model, 'rb') as f:
            trained_model = pickle.load(f)
        
        test_df = load_data(test_data)
        baseline = None
        if baseline_metrics and Path(baseline_metrics).exists():
            with open(baseline_metrics, 'r') as f:
                baseline = json.load(f).get('metrics', {})
        
        results = validate_training(trained_model, test_df, baseline)
        
        if output_report:
            Path(output_report).parent.mkdir(parents=True, exist_ok=True)
            report = f"""# Training Validation Report

**Date**: {datetime.now().isoformat()}

## Test Performance

- Accuracy: {results['test_accuracy']:.4f}
- Precision: {results['test_precision']:.4f}
- Recall: {results['test_recall']:.4f}
- F1-Score: {results['test_f1']:.4f}

## Improvement

- Improvement over baseline: {results['improvement_pct']:.2f}% if results['improvement_pct'] else 'N/A'

## Status

✅ Training validation complete
"""
            with open(output_report, 'w') as f:
                f.write(report)
            logger.info(f"Validation report saved to {output_report}")
        
        logger.info("[PROTOCOL 13 | TRAINING VALIDATION COMPLETE]")
        return {"status": "success", "data": results}
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate training")
    parser.add_argument("--model", required=True)
    parser.add_argument("--test-data", required=True)
    parser.add_argument("--baseline-metrics")
    parser.add_argument("--output-report")
    args = parser.parse_args()
    result = main(args.model, args.test_data, args.baseline_metrics, args.output_report)
    exit(0 if result["status"] == "success" else 1)
