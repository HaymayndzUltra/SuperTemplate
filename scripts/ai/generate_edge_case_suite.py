#!/usr/bin/env python3
"""
Script: generate_edge_case_suite.py
Protocol: 15 - AI Model Testing & Edge Case Validation
Purpose: Produce a markdown catalog of prioritized edge cases.
"""

import argparse
import random
from pathlib import Path
from typing import List

TEMPLATE = """# Edge Case Register

| ID | Scenario | Category | Severity | Expected Outcome |
|----|----------|----------|----------|------------------|
{rows}

Total scenarios: {count}
"""

SCENARIOS = [
    ("SC-001", "Adversarial noise injection", "computer-vision", "critical", "Model rejects tampered input"),
    ("SC-002", "Low-light image", "computer-vision", "high", "Confidence ≥ 0.8"),
    ("SC-003", "Extreme temperature sensor readings", "iot", "medium", "Clipped to safe range"),
    ("SC-004", "Long-tail intent: refund in dialect", "nlp", "high", "Correct intent label"),
    ("SC-005", "Mixed-language utterance", "nlp", "medium", "Confidence ≥ 0.7"),
    ("SC-006", "Data spike 10x normal", "time-series", "critical", "Alert triggered"),
    ("SC-007", "Out-of-date firmware metadata", "iot", "medium", "Graceful fallback"),
    ("SC-008", "Obstructed camera frame", "computer-vision", "high", "Reject inference"),
    ("SC-009", "Extremely long text input", "nlp", "medium", "Truncated safely"),
    ("SC-010", "Null sensor packets", "iot", "high", "Auto-retry"),
    ("SC-011", "Class imbalance replay", "ml", "medium", "No degradation"),
    ("SC-012", "Toxic content detection", "nlp", "critical", "Block request"),
    ("SC-013", "Rapid-fire requests", "performance", "high", "Latency within SLA"),
    ("SC-014", "GPU memory pressure", "infrastructure", "medium", "Auto-scale"),
    ("SC-015", "Incorrect timezone data", "time-series", "medium", "Normalize timestamp"),
    ("SC-016", "Model drift snapshot", "ml", "critical", "Raise drift alert"),
    ("SC-017", "Bias probe: protected group", "fairness", "high", "Metric parity ±5%"),
    ("SC-018", "Explainability stress", "explainability", "medium", "Generate SHAP within 2s"),
    ("SC-019", "Blackout region data", "compliance", "critical", "Deny processing"),
    ("SC-020", "Corrupted protobuf payload", "infrastructure", "high", "Return 4xx error"),
]


def pick_scenarios(seed: int) -> List[str]:
    random.seed(seed)
    chosen = random.sample(SCENARIOS, k=min(len(SCENARIOS), 20))
    rows = [f"| {sid} | {scenario} | {category} | {severity} | {outcome} |" for sid, scenario, category, severity, outcome in chosen]
    rows.sort()
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate edge case catalog")
    parser.add_argument("--config", required=False, help="Configuration file (unused placeholder)")
    parser.add_argument("--out", required=True, help="Output markdown path")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    rows = pick_scenarios(args.seed)
    content = TEMPLATE.format(rows="\n".join(rows), count=len(rows))

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")
    print(f"Edge case register created: {out_path} ({len(rows)} scenarios)")


if __name__ == "__main__":
    main()
