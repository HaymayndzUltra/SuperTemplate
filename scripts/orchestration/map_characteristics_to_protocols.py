#!/usr/bin/env python3
"""
Map Characteristics to Protocols
Maps detected project characteristics to required protocols.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

# Protocol mapping based on characteristics
CHARACTERISTIC_PROTOCOL_MAP = {
    # AI/ML characteristics
    "model_training": ["06", "07", "08", "09", "10", "11", "12", "13"],
    "model_deployment": ["14", "15", "16"],
    "model_monitoring": ["17"],
    "feature_engineering": ["10"],
    "data_pipeline": ["08", "09"],
    "bias_detection": ["13"],
    "explainability": ["13"],
    
    # Data characteristics
    "database_sql": ["04", "05"],
    "database_nosql": ["04", "05"],
    "database_vector": ["08", "09"],
    "realtime_processing": ["12"],
    "batch_processing": ["09"],
    
    # Application characteristics
    "authentication": ["04", "05"],
    "user_management": ["04", "05"],
    "file_uploads": ["04"],
    "realtime_features": ["04", "05"],
    "internationalization": ["05"],
    "multitenancy": ["04", "05"],
    
    # Infrastructure characteristics
    "cloud_aws": ["18", "19"],
    "cloud_gcp": ["18", "19"],
    "cloud_azure": ["18", "19"],
    "containerization": ["18", "19"],
    "cicd_pipeline": ["18", "19"],
    "monitoring": ["22"],
    "scalability": ["18"],
    
    # Compliance characteristics
    "gdpr_compliance": ["20", "21"],
    "hipaa_compliance": ["20", "21"],
    "soc2_compliance": ["20", "21"],
    "security_audit": ["20", "21", "SR"]
}

# Protocol metadata
PROTOCOL_INFO = {
    "01": {"name": "Client Proposal Generation", "track": "generic"},
    "02": {"name": "Client Discovery", "track": "generic"},
    "03": {"name": "Project Brief Creation", "track": "generic"},
    "04": {"name": "Project Bootstrap", "track": "generic"},
    "05": {"name": "Context Engineering", "track": "generic"},
    "05b": {"name": "Protocol Orchestration", "track": "generic"},
    "06": {"name": "AI Use Case Definition", "track": "ai_ml"},
    "07": {"name": "AI Data Strategy", "track": "ai_ml"},
    "08": {"name": "AI Data Collection", "track": "ai_ml"},
    "09": {"name": "AI Data Cleaning", "track": "ai_ml"},
    "10": {"name": "AI Feature Engineering", "track": "ai_ml"},
    "11": {"name": "AI Dataset Preparation", "track": "ai_ml"},
    "12": {"name": "AI Model Training", "track": "ai_ml"},
    "13": {"name": "AI Model Evaluation", "track": "ai_ml"},
    "14": {"name": "AI Model Deployment", "track": "ai_ml"},
    "15": {"name": "AI Model Integration", "track": "ai_ml"},
    "16": {"name": "AI Model Serving", "track": "ai_ml"},
    "17": {"name": "AI Model Monitoring", "track": "ai_ml"},
    "18": {"name": "Performance Optimization", "track": "generic"},
    "19": {"name": "Documentation", "track": "generic"},
    "20": {"name": "Project Handover", "track": "generic"},
    "21": {"name": "Retrospective", "track": "generic"},
    "22": {"name": "Monitoring Setup", "track": "generic"},
    "23": {"name": "Script Governance", "track": "generic"},
    "AR": {"name": "Architecture Review", "track": "generic"},
    "CR": {"name": "Code Review", "track": "generic"},
    "SR": {"name": "Security Review", "track": "generic"}
}

def map_characteristics_to_protocols(characteristics: list) -> dict:
    """Map detected characteristics to protocol recommendations."""
    
    protocol_scores = {}
    protocol_reasons = {}
    
    for char in characteristics:
        if not char.get('detected'):
            continue
        
        char_id = char.get('id')
        char_name = char.get('name')
        char_confidence = char.get('confidence', 0)
        
        # Get protocols for this characteristic
        protocols = CHARACTERISTIC_PROTOCOL_MAP.get(char_id, [])
        
        for protocol_id in protocols:
            if protocol_id not in protocol_scores:
                protocol_scores[protocol_id] = 0
                protocol_reasons[protocol_id] = []
            
            # Add weighted score based on characteristic confidence
            protocol_scores[protocol_id] += char_confidence / 100
            protocol_reasons[protocol_id].append({
                "characteristic": char_name,
                "confidence": char_confidence
            })
    
    return protocol_scores, protocol_reasons

def categorize_protocols(protocol_scores: dict, protocol_reasons: dict, classification: str) -> dict:
    """Categorize protocols into MUST, SHOULD, MAYBE."""
    
    categorized = {
        "must": [],
        "should": [],
        "maybe": []
    }
    
    # Base protocols always required
    base_protocols = ["03", "04", "05", "05b"]
    
    # Track-specific base protocols
    if classification in ['ai_ml_application', 'hybrid_application']:
        base_protocols.extend(["06", "07"])
    
    for protocol_id in base_protocols:
        if protocol_id in PROTOCOL_INFO:
            categorized['must'].append({
                "id": protocol_id,
                "name": PROTOCOL_INFO[protocol_id]['name'],
                "track": PROTOCOL_INFO[protocol_id]['track'],
                "reason": "Base protocol - always required",
                "score": 100
            })
    
    # Score-based categorization
    for protocol_id, score in sorted(protocol_scores.items(), key=lambda x: x[1], reverse=True):
        if protocol_id in base_protocols:
            continue
        
        if protocol_id not in PROTOCOL_INFO:
            continue
        
        protocol_entry = {
            "id": protocol_id,
            "name": PROTOCOL_INFO[protocol_id]['name'],
            "track": PROTOCOL_INFO[protocol_id]['track'],
            "score": round(score * 100, 2),
            "reasons": protocol_reasons.get(protocol_id, [])
        }
        
        # Categorize based on score
        if score >= 1.5:  # Strong match (multiple characteristics)
            categorized['must'].append(protocol_entry)
        elif score >= 0.7:  # Good match
            categorized['should'].append(protocol_entry)
        elif score >= 0.3:  # Weak match
            categorized['maybe'].append(protocol_entry)
    
    return categorized

def main():
    parser = argparse.ArgumentParser(description='Map characteristics to protocols')
    parser.add_argument('--characteristics', required=True, help='Path to characteristics-detection.json')
    parser.add_argument('--classification', required=True, help='Path to project-classification.json')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 3] Mapping characteristics to protocols...")
    
    # Load characteristics data
    char_path = Path(args.characteristics)
    if not char_path.is_absolute():
        char_path = workspace / char_path
    
    with open(char_path, 'r', encoding='utf-8') as f:
        characteristics_data = json.load(f)
    
    # Load classification data
    class_path = Path(args.classification)
    if not class_path.is_absolute():
        class_path = workspace / class_path
    
    with open(class_path, 'r', encoding='utf-8') as f:
        classification_data = json.load(f)
    
    # Map characteristics to protocols
    characteristics = characteristics_data.get('all_characteristics', [])
    protocol_scores, protocol_reasons = map_characteristics_to_protocols(characteristics)
    
    # Categorize protocols
    classification = classification_data.get('classification', 'generic_web_app')
    categorized = categorize_protocols(protocol_scores, protocol_reasons, classification)
    
    # Build output
    output = {
        "timestamp": datetime.now().isoformat(),
        "classification": classification,
        "protocol_mapping": categorized,
        "summary": {
            "must_count": len(categorized['must']),
            "should_count": len(categorized['should']),
            "maybe_count": len(categorized['maybe']),
            "total_recommended": len(categorized['must']) + len(categorized['should'])
        },
        "input_files": {
            "characteristics": str(char_path),
            "classification": str(class_path)
        }
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'characteristic-protocol-mapping.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 3] Protocol mapping complete")
    print(f"  - MUST protocols: {output['summary']['must_count']}")
    print(f"  - SHOULD protocols: {output['summary']['should_count']}")
    print(f"  - MAYBE protocols: {output['summary']['maybe_count']}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
