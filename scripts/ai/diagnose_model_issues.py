#!/usr/bin/env python3
"""
Script: diagnose_model_issues.py
Protocol: 14 - AI Model Validation & Evaluation
Purpose: Compare train vs validation metrics to flag overfitting/underfitting.
"""

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Tuple

import pandas as pd


def load_metrics(path: str) -> Dict[str, float]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict) and "metrics" in data:
        return data["metrics"]
    return data


def compute_deltas(train: Dict[str, float], val: Dict[str, float]) -> Dict[str, float]:
    deltas = {}
    for key, t_value in train.items():
        v_value = val.get(key)
        if isinstance(t_value, (int, float)) and isinstance(v_value, (int, float)):
            deltas[key] = float(abs(t_value - v_value))
    return deltas


def classify(delta: float, threshold: float) -> str:
    if delta > threshold:
        return "risk"
    if delta > threshold * 0.5:
        return "watch"
    return "stable"


def main():
    parser = argparse.ArgumentParser(description="Diagnose model overfitting/underfitting")
    parser.add_argument("--train-metrics", required=True, help="JSON file with train metrics")
    parser.add_argument("--val-metrics", required=True, help="JSON file with validation metrics")
    parser.add_argument("--out", required=True, help="Output markdown path")
    parser.add_argument("--threshold", type=float, default=0.05, help="Delta threshold")
    args = parser.parse_args()

    train = load_metrics(args.train_metrics)
    val = load_metrics(args.val_metrics)
    deltas = compute_deltas(train, val)

    rows: list[Tuple[str, float, float, float, str]] = []
    for metric, delta in deltas.items():
        status = classify(delta, args.threshold)
        rows.append((metric, train.get(metric, 0.0), val.get(metric, 0.0), delta, status))

    df = pd.DataFrame(rows, columns=["metric", "train", "validation", "delta", "status"])
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("# Overfitting Diagnosis\n\n")
        f.write(df.to_markdown(index=False))
        f.write("\n\n## Summary\n")
        f.write(json.dumps({"threshold": args.threshold, "deltas": deltas}, indent=2))


if __name__ == "__main__":
    main()
