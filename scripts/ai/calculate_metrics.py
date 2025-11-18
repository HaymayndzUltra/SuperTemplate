#!/usr/bin/env python3
"""
Script: calculate_metrics.py
Protocol: 14 - AI Model Validation & Evaluation
Purpose: Compute core classification metrics from ground-truth and prediction CSV files.
"""

import argparse
import json
from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score


def compute_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    metrics = {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
    }
    try:
        metrics["roc_auc"] = float(roc_auc_score(y_true, y_pred))
    except ValueError:
        metrics["roc_auc"] = 0.0
    return metrics


def main():
    parser = argparse.ArgumentParser(description="Compute validation metrics")
    parser.add_argument("--y_true", required=True, help="CSV file with column 'label'")
    parser.add_argument("--y_pred", required=True, help="CSV file with column 'prediction'")
    parser.add_argument("--out", required=True, help="Output JSON path")
    args = parser.parse_args()

    y_true = pd.read_csv(args.y_true)["label"].to_numpy()
    y_pred = pd.read_csv(args.y_pred)["prediction"].to_numpy()

    metrics = compute_metrics(y_true, y_pred)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump({"metrics": metrics}, f, indent=2)


if __name__ == "__main__":
    main()
