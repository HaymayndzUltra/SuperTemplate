#!/usr/bin/env python3
"""
Detect Project Characteristics
Identifies technical characteristics across 27+ dimensions to inform protocol selection.
"""
import argparse
import json
import sys
import yaml
from pathlib import Path
from datetime import datetime

def load_dimensions_config(workspace: Path) -> dict:
    """Load classification dimensions configuration."""
    config_path = workspace / 'config' / 'classification-dimensions.yaml'
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return {"dimensions": []}

def detect_characteristic(content: str, dimension: dict) -> dict:
    """Detect a single characteristic based on dimension config."""
    content_lower = content.lower()
    
    matches = []
    
    # Check keywords
    keywords = dimension.get('keywords', [])
    for keyword in keywords:
        if keyword.lower() in content_lower:
            matches.append({"type": "keyword", "match": keyword})
    
    # Check tech stack indicators
    tech_indicators = dimension.get('tech_stack_indicators', [])
    for indicator in tech_indicators:
        if indicator.lower() in content_lower:
            matches.append({"type": "tech_stack", "match": indicator})
    
    # Calculate confidence
    total_indicators = len(keywords) + len(tech_indicators)
    if total_indicators == 0:
        confidence = 0.0
    else:
        # Weight tech stack matches higher
        keyword_matches = len([m for m in matches if m['type'] == 'keyword'])
        tech_matches = len([m for m in matches if m['type'] == 'tech_stack'])
        
        weight = dimension.get('confidence_weight', 0.8)
        confidence = min(1.0, (keyword_matches * 0.3 + tech_matches * 0.7) / max(1, total_indicators / 2) * weight)
    
    return {
        "id": dimension.get('id'),
        "name": dimension.get('name'),
        "category": dimension.get('category'),
        "detected": confidence >= 0.5,
        "confidence": round(confidence * 100, 2),
        "matches": matches
    }

def detect_all_characteristics(brief_data: dict, arch_data: dict, config: dict) -> list:
    """Detect all characteristics based on config."""
    # Combine all content for searching
    content_parts = []
    
    # Add brief content
    content_parts.append(json.dumps(brief_data))
    
    # Add architecture content
    content_parts.append(json.dumps(arch_data))
    
    combined_content = ' '.join(content_parts)
    
    results = []
    dimensions = config.get('dimensions', [])
    
    for dimension in dimensions:
        result = detect_characteristic(combined_content, dimension)
        results.append(result)
    
    return results

def categorize_results(results: list) -> dict:
    """Categorize detection results by category."""
    categories = {}
    
    for result in results:
        category = result.get('category', 'other')
        if category not in categories:
            categories[category] = {
                "detected": [],
                "not_detected": []
            }
        
        if result.get('detected'):
            categories[category]['detected'].append(result)
        else:
            categories[category]['not_detected'].append(result)
    
    return categories

def main():
    parser = argparse.ArgumentParser(description='Detect project characteristics')
    parser.add_argument('--brief', required=True, help='Path to project-brief-parsed.json')
    parser.add_argument('--architecture', help='Path to architecture-parsed.json')
    parser.add_argument('--classification', help='Path to project-classification.json')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 2] Detecting project characteristics...")
    
    # Load configuration
    config = load_dimensions_config(workspace)
    
    # Load parsed brief
    brief_path = Path(args.brief)
    if not brief_path.is_absolute():
        brief_path = workspace / brief_path
    
    with open(brief_path, 'r', encoding='utf-8') as f:
        brief_data = json.load(f)
    
    # Load architecture data (optional)
    arch_data = {}
    if args.architecture:
        arch_path = Path(args.architecture)
        if not arch_path.is_absolute():
            arch_path = workspace / arch_path
        if arch_path.exists():
            with open(arch_path, 'r', encoding='utf-8') as f:
                arch_data = json.load(f)
    
    # Load classification data (optional)
    classification_data = {}
    if args.classification:
        class_path = Path(args.classification)
        if not class_path.is_absolute():
            class_path = workspace / class_path
        if class_path.exists():
            with open(class_path, 'r', encoding='utf-8') as f:
                classification_data = json.load(f)
    
    # Detect characteristics
    results = detect_all_characteristics(brief_data, arch_data, config)
    
    # Categorize results
    categorized = categorize_results(results)
    
    # Calculate summary
    detected_count = sum(1 for r in results if r.get('detected'))
    total_count = len(results)
    
    # Build output
    output = {
        "timestamp": datetime.now().isoformat(),
        "project_classification": classification_data.get('classification', 'unknown'),
        "summary": {
            "total_dimensions": total_count,
            "detected": detected_count,
            "not_detected": total_count - detected_count,
            "detection_rate": round(detected_count / total_count * 100, 2) if total_count > 0 else 0
        },
        "by_category": categorized,
        "all_characteristics": results,
        "input_files": {
            "brief": str(brief_path),
            "architecture": str(args.architecture) if args.architecture else None,
            "classification": str(args.classification) if args.classification else None
        }
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'characteristics-detection.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 2] Characteristic detection complete")
    print(f"  - Total dimensions: {total_count}")
    print(f"  - Detected: {detected_count}")
    print(f"  - Detection rate: {output['summary']['detection_rate']}%")
    
    # Print detected characteristics by category
    for category, data in categorized.items():
        if data['detected']:
            print(f"  - {category.upper()}: {', '.join(c['name'] for c in data['detected'])}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
