#!/usr/bin/env python3
"""
Validator for Protocol 24: AI Model Retraining & Update Pipeline
Validates retraining trigger conditions, automated workflows, and rollout strategies.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple


def validate_retraining_triggers(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate retraining trigger configuration."""
    errors = []
    
    trigger_config = evidence_path / "trigger-config.yaml"
    if not trigger_config.exists():
        errors.append("Missing trigger-config.yaml")
        return False, errors
    
    # Check trigger types defined
    required_triggers = [
        "performance_degradation",
        "data_drift",
        "concept_drift",
        "scheduled_retraining",
        "manual_trigger"
    ]
    
    content = trigger_config.read_text()
    for trigger in required_triggers:
        if trigger not in content:
            errors.append(f"Missing trigger type: {trigger}")
    
    return len(errors) == 0, errors


def validate_retraining_pipeline(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate automated retraining pipeline."""
    errors = []
    
    pipeline_file = evidence_path / "retraining-pipeline.py"
    if not pipeline_file.exists():
        errors.append("Missing retraining-pipeline.py")
        return False, errors
    
    content = pipeline_file.read_text()
    
    # Check required components
    required_components = [
        "def trigger_retraining",
        "def load_new_data",
        "def train_model",
        "def validate_model",
        "def compare_models",
        "mlflow"
    ]
    
    for component in required_components:
        if component not in content:
            errors.append(f"Missing component: {component}")
    
    return len(errors) == 0, errors


def validate_ab_testing(evidence_path: Path) -> Tuple[bool, List[str]]:
    """Validate A/B testing configuration."""
    errors = []
    
    rollout_plan = evidence_path / "rollout-plan.md"
    if not rollout_plan.exists():
        errors.append("Missing rollout-plan.md")
        return False, errors
    
    content = rollout_plan.read_text()
    
    # Check A/B testing elements
    required_elements = [
        "traffic split",
        "statistical significance",
        "sample size",
        "success criteria",
        "rollback conditions"
    ]
    
    for element in required_elements:
        if element.lower() not in content.lower():
            errors.append(f"Missing A/B testing element: {element}")
    
    return len(errors) == 0, errors


def validate_protocol_24(protocol_path: str) -> Dict:
    """Main validation function for Protocol 24."""
    
    protocol_path = Path(protocol_path)
    evidence_path = protocol_path.parent.parent / "evidence" / "protocol-24-retraining"
    
    results = {
        "protocol_id": "24",
        "protocol_name": "AI Model Retraining & Update Pipeline",
        "validation_status": "PASS",
        "gates": {},
        "overall_score": 0.0,
        "errors": []
    }
    
    # Gate 1: Retraining Triggers
    gate1_pass, gate1_errors = validate_retraining_triggers(evidence_path)
    results["gates"]["gate_1_triggers"] = {
        "name": "Retraining Trigger Configuration",
        "status": "PASS" if gate1_pass else "FAIL",
        "errors": gate1_errors
    }
    
    # Gate 2: Retraining Pipeline
    gate2_pass, gate2_errors = validate_retraining_pipeline(evidence_path)
    results["gates"]["gate_2_pipeline"] = {
        "name": "Automated Retraining Pipeline",
        "status": "PASS" if gate2_pass else "FAIL",
        "errors": gate2_errors
    }
    
    # Gate 3: A/B Testing
    gate3_pass, gate3_errors = validate_ab_testing(evidence_path)
    results["gates"]["gate_3_ab_testing"] = {
        "name": "A/B Testing & Rollout",
        "status": "PASS" if gate3_pass else "FAIL",
        "errors": gate3_errors
    }
    
    # Calculate overall score
    gates_passed = sum([gate1_pass, gate2_pass, gate3_pass])
    results["overall_score"] = (gates_passed / 3) * 100
    
    # Determine overall status
    if gates_passed < 3:
        results["validation_status"] = "FAIL"
        results["errors"] = gate1_errors + gate2_errors + gate3_errors
    
    return results


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: validate_retraining.py <protocol_path>")
        sys.exit(1)
    
    result = validate_protocol_24(sys.argv[1])
    print(json.dumps(result, indent=2))
    
    sys.exit(0 if result["validation_status"] == "PASS" else 1)
