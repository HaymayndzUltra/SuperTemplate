#!/usr/bin/env python3
"""
Calculate Classification Confidence
Calculates overall confidence score for project classification.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def calculate_confidence(classification_data: dict, characteristics_data: dict) -> dict:
    """Calculate comprehensive confidence score."""
    
    # Base confidence from classification
    base_confidence = classification_data.get('confidence_score', 0) / 100
    
    # Get classification type
    classification_type = classification_data.get('classification', 'unknown')
    
    # Get relevant characteristics for this classification type
    characteristics = characteristics_data.get('all_characteristics', [])
    
    # Define which characteristics support which classification
    classification_characteristics = {
        'ai_ml_application': ['model_training', 'model_deployment', 'feature_engineering', 'data_pipeline', 'model_monitoring'],
        'generic_web_app': ['authentication', 'user_management', 'database_sql', 'database_nosql', 'realtime_features'],
        'hybrid_application': ['model_training', 'authentication', 'database_sql', 'realtime_features'],
        'api_microservice': ['authentication', 'database_sql', 'containerization', 'cicd_pipeline'],
        'data_pipeline': ['data_pipeline', 'batch_processing', 'realtime_processing', 'data_volume_large'],
        'mobile_application': ['authentication', 'user_management']
    }
    
    # Calculate characteristic support
    relevant_chars = classification_characteristics.get(classification_type, [])
    supporting_chars = []
    conflicting_chars = []
    
    for char in characteristics:
        char_id = char.get('id')
        if char_id in relevant_chars and char.get('detected'):
            supporting_chars.append(char)
        elif char_id in relevant_chars and not char.get('detected'):
            conflicting_chars.append(char)
    
    # Calculate support score
    if relevant_chars:
        support_score = len(supporting_chars) / len(relevant_chars)
    else:
        support_score = 0.5  # Neutral if no relevant characteristics defined
    
    # Calculate final confidence
    # Weight: 60% base classification, 40% characteristic support
    final_confidence = (base_confidence * 0.6) + (support_score * 0.4)
    
    # Determine confidence level
    if final_confidence >= 0.9:
        confidence_level = "high"
    elif final_confidence >= 0.7:
        confidence_level = "medium"
    elif final_confidence >= 0.5:
        confidence_level = "low"
    else:
        confidence_level = "very_low"
    
    return {
        "final_confidence": round(final_confidence * 100, 2),
        "confidence_level": confidence_level,
        "components": {
            "base_classification_confidence": round(base_confidence * 100, 2),
            "characteristic_support_score": round(support_score * 100, 2)
        },
        "supporting_characteristics": [c['name'] for c in supporting_chars],
        "missing_expected_characteristics": [c['name'] for c in conflicting_chars],
        "requires_human_review": confidence_level in ["low", "very_low"]
    }

def main():
    parser = argparse.ArgumentParser(description='Calculate classification confidence')
    parser.add_argument('--classification', required=True, help='Path to project-classification.json')
    parser.add_argument('--characteristics', required=True, help='Path to characteristics-detection.json')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 2] Calculating classification confidence...")
    
    # Load classification data
    class_path = Path(args.classification)
    if not class_path.is_absolute():
        class_path = workspace / class_path
    
    with open(class_path, 'r', encoding='utf-8') as f:
        classification_data = json.load(f)
    
    # Load characteristics data
    char_path = Path(args.characteristics)
    if not char_path.is_absolute():
        char_path = workspace / char_path
    
    with open(char_path, 'r', encoding='utf-8') as f:
        characteristics_data = json.load(f)
    
    # Calculate confidence
    confidence = calculate_confidence(classification_data, characteristics_data)
    
    # Build output
    output = {
        "timestamp": datetime.now().isoformat(),
        "classification": classification_data.get('classification'),
        "classification_display": classification_data.get('classification_display'),
        "confidence": confidence,
        "gate_1_status": "PASS" if confidence['final_confidence'] >= 85 else "FAIL",
        "input_files": {
            "classification": str(class_path),
            "characteristics": str(char_path)
        }
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'classification-confidence.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 2] Confidence calculation complete")
    print(f"  - Classification: {output['classification_display']}")
    print(f"  - Final Confidence: {confidence['final_confidence']}%")
    print(f"  - Confidence Level: {confidence['confidence_level']}")
    print(f"  - Gate 1 Status: {output['gate_1_status']}")
    
    if confidence['requires_human_review']:
        print(f"[WARNING] Low confidence - human review required")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
