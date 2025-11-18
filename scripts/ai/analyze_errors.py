#!/usr/bin/env python3
"""
Script: analyze_errors.py
Protocol: 14 - AI Model Validation & Evaluation
Purpose: Generate confusion matrix and error summary artifacts.
"""

import argparse
import json
from pathlib import Path
from typing import Any, Dict

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix


def build_error_summary(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, Any]:
    labels = sorted(list(set(y_true) | set(y_pred)))
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    summary = {
        "labels": labels,
        "confusion_matrix": cm.tolist(),
        "total": int(len(y_true)),
        "accuracy": float((y_true == y_pred).sum() / len(y_true))
    }
    misclassified = []
    for idx, (truth, pred) in enumerate(zip(y_true, y_pred)):
        if truth != pred:
            misclassified.append({"index": idx, "actual": int(truth), "predicted": int(pred)})
    summary["misclassified_samples"] = misclassified
    return summary


def main():
    parser = argparse.ArgumentParser(description="Analyze prediction errors")
    parser.add_argument("--predictions", required=True)
    parser.add_argument("--labels", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    y_true = pd.read_csv(args.labels)["label"].to_numpy()
    y_pred = pd.read_csv(args.predictions)["prediction"].to_numpy()

    summary = build_error_summary(y_true, y_pred)
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)


if __name__ == "__main__":
    main()
