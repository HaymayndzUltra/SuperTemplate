#!/usr/bin/env python3
"""
Generate Classification Reasoning Document
Creates human-readable explanation of classification decision.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def generate_reasoning_markdown(classification_data: dict, characteristics_data: dict, confidence_data: dict) -> str:
    """Generate markdown reasoning document."""
    
    classification = classification_data.get('classification_display', 'Unknown')
    confidence = confidence_data.get('confidence', {})
    
    md = f"""# Project Classification Reasoning

## Classification Decision

**Project Type:** {classification}
**Confidence Score:** {confidence.get('final_confidence', 0)}%
**Confidence Level:** {confidence.get('confidence_level', 'unknown').upper()}
**Gate 1 Status:** {confidence_data.get('gate_1_status', 'UNKNOWN')}

---

## Evidence Supporting Classification

### Primary Classification Scores

"""
    
    # Add classification scores
    scores = classification_data.get('scores', {})
    for type_name, score_data in scores.items():
        score = score_data.get('score', 0)
        evidence = score_data.get('evidence', [])
        display_name = type_name.replace('_', ' ').title()
        
        md += f"#### {display_name}: {score}%\n"
        if evidence:
            for e in evidence:
                md += f"- {e}\n"
        else:
            md += "- No specific evidence detected\n"
        md += "\n"
    
    md += """---

## Characteristic Detection Summary

"""
    
    # Add characteristic summary by category
    by_category = characteristics_data.get('by_category', {})
    for category, data in by_category.items():
        detected = data.get('detected', [])
        if detected:
            md += f"### {category.upper().replace('_', ' ')}\n\n"
            for char in detected:
                md += f"- **{char['name']}** (Confidence: {char['confidence']}%)\n"
                matches = char.get('matches', [])
                if matches:
                    match_strs = [m['match'] for m in matches[:3]]
                    md += f"  - Matches: {', '.join(match_strs)}\n"
            md += "\n"
    
    md += """---

## Confidence Breakdown

"""
    
    components = confidence.get('components', {})
    md += f"- **Base Classification Confidence:** {components.get('base_classification_confidence', 0)}%\n"
    md += f"- **Characteristic Support Score:** {components.get('characteristic_support_score', 0)}%\n"
    
    supporting = confidence.get('supporting_characteristics', [])
    if supporting:
        md += f"\n**Supporting Characteristics:** {', '.join(supporting)}\n"
    
    missing = confidence.get('missing_expected_characteristics', [])
    if missing:
        md += f"\n**Missing Expected Characteristics:** {', '.join(missing)}\n"
    
    md += """
---

## Implications for Protocol Selection

Based on this classification, the following protocol tracks are recommended:

"""
    
    classification_type = classification_data.get('classification', 'unknown')
    
    protocol_recommendations = {
        'ai_ml_application': [
            "AI/ML Track Protocols (06-17): Use Case Definition through Model Monitoring",
            "Data-focused protocols for pipeline and feature engineering",
            "Model deployment and serving protocols"
        ],
        'generic_web_app': [
            "Generic Track Protocols (01-05): Bootstrap through Quality Audit",
            "Frontend and backend development protocols",
            "Testing and deployment protocols"
        ],
        'hybrid_application': [
            "Generic Track Protocols for web infrastructure",
            "AI/ML Track Protocols for ML components",
            "Integration protocols for connecting both tracks"
        ],
        'api_microservice': [
            "API development protocols",
            "Backend-focused protocols",
            "Infrastructure and deployment protocols"
        ],
        'data_pipeline': [
            "Data engineering protocols",
            "ETL and processing protocols",
            "Monitoring and observability protocols"
        ],
        'mobile_application': [
            "Mobile development protocols",
            "Cross-platform or native protocols as appropriate",
            "Mobile-specific testing protocols"
        ]
    }
    
    recommendations = protocol_recommendations.get(classification_type, ["Generic protocols"])
    for rec in recommendations:
        md += f"- {rec}\n"
    
    md += f"""
---

## Next Steps

"""
    
    if confidence.get('requires_human_review'):
        md += """**⚠️ HUMAN REVIEW REQUIRED**

The classification confidence is below the 85% threshold. Please review the evidence above and confirm or override the classification before proceeding.

"""
    else:
        md += """Classification confidence meets the 85% threshold. Ready to proceed with protocol selection.

"""
    
    md += f"""---

*Generated: {datetime.now().isoformat()}*
"""
    
    return md

def main():
    parser = argparse.ArgumentParser(description='Generate classification reasoning document')
    parser.add_argument('--classification', required=True, help='Path to project-classification.json')
    parser.add_argument('--characteristics', required=True, help='Path to characteristics-detection.json')
    parser.add_argument('--confidence', help='Path to classification-confidence.json')
    parser.add_argument('--output', help='Output markdown file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 2] Generating classification reasoning document...")
    
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
    
    # Load confidence data (optional, will calculate if not provided)
    confidence_data = {}
    if args.confidence:
        conf_path = Path(args.confidence)
        if not conf_path.is_absolute():
            conf_path = workspace / conf_path
        if conf_path.exists():
            with open(conf_path, 'r', encoding='utf-8') as f:
                confidence_data = json.load(f)
    
    # If no confidence data, create minimal structure
    if not confidence_data:
        confidence_data = {
            "confidence": {
                "final_confidence": classification_data.get('confidence_score', 0),
                "confidence_level": classification_data.get('confidence_level', 'unknown'),
                "components": {},
                "supporting_characteristics": [],
                "missing_expected_characteristics": [],
                "requires_human_review": classification_data.get('confidence_score', 0) < 85
            },
            "gate_1_status": "PASS" if classification_data.get('confidence_score', 0) >= 85 else "FAIL"
        }
    
    # Generate markdown
    markdown = generate_reasoning_markdown(classification_data, characteristics_data, confidence_data)
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'classification-reasoning.md'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"[PROTOCOL 05B | PHASE 2] Reasoning document generated: {output_path}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
