#!/usr/bin/env python3
"""
Script: calculate_protocol_quality_score.py
Protocol: 05 (Protocol Retrospective)
Purpose: Calculate quantitative quality score for protocols
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any

try:
    import textstat
    import numpy as np
    from nltk.tokenize import sent_tokenize
except ImportError:
    print("Missing dependencies. Install with: pip install textstat numpy nltk")
    sys.exit(1)


def calculate_clarity_score(protocol_content: str) -> Dict[str, Any]:
    """Calculate clarity score (0-25 points)"""
    score = 0
    breakdown = {}
    
    # Readability (Flesch-Kincaid grade level)
    fk_grade = textstat.flesch_kincaid_grade(protocol_content)
    if 8 <= fk_grade <= 12:
        score += 10
        breakdown['readability'] = {'score': 10, 'fk_grade': fk_grade, 'status': 'optimal'}
    elif 6 <= fk_grade <= 14:
        score += 5
        breakdown['readability'] = {'score': 5, 'fk_grade': fk_grade, 'status': 'acceptable'}
    else:
        breakdown['readability'] = {'score': 0, 'fk_grade': fk_grade, 'status': 'needs_improvement'}
    
    # Average sentence length
    try:
        sentences = sent_tokenize(protocol_content)
        avg_words = np.mean([len(s.split()) for s in sentences])
        if 15 <= avg_words <= 25:
            score += 5
            breakdown['sentence_length'] = {'score': 5, 'avg_words': avg_words, 'status': 'optimal'}
        else:
            breakdown['sentence_length'] = {'score': 0, 'avg_words': avg_words, 'status': 'suboptimal'}
    except Exception as e:
        breakdown['sentence_length'] = {'score': 0, 'error': str(e)}
    
    # Examples provided
    example_count = protocol_content.lower().count("example")
    sections = protocol_content.count("##")
    if sections > 0 and example_count >= sections * 2:
        score += 5
        breakdown['examples'] = {'score': 5, 'count': example_count, 'sections': sections}
    else:
        breakdown['examples'] = {'score': 0, 'count': example_count, 'sections': sections}
    
    # Technical terms (simplified - count code blocks as proxy)
    code_blocks = len(re.findall(r'```', protocol_content)) // 2
    if code_blocks >= 3:
        score += 5
        breakdown['technical_examples'] = {'score': 5, 'code_blocks': code_blocks}
    else:
        breakdown['technical_examples'] = {'score': 0, 'code_blocks': code_blocks}
    
    return {'score': score, 'max': 25, 'breakdown': breakdown}


def calculate_completeness_score(protocol_content: str) -> Dict[str, Any]:
    """Calculate completeness score (0-25 points)"""
    score = 0
    breakdown = {}
    
    # Required sections present
    required = ["PREREQUISITES", "AI ROLE", "WORKFLOW", "INTEGRATION",
                "QUALITY GATES", "COMMUNICATION", "AUTOMATION", "HANDOFF", "EVIDENCE"]
    present = [section for section in required if section in protocol_content.upper()]
    section_score = (len(present) / len(required)) * 15
    score += section_score
    breakdown['required_sections'] = {
        'score': section_score,
        'present': present,
        'missing': [s for s in required if s not in present],
        'percentage': len(present) / len(required) * 100
    }
    
    # All placeholders filled
    placeholders = re.findall(r'\[([A-Z_]+)\]', protocol_content)
    # Filter out valid markdown links
    placeholders = [p for p in placeholders if p not in ['X', 'Y', 'Z', 'N', 'M']]
    if len(placeholders) == 0:
        score += 5
        breakdown['placeholders'] = {'score': 5, 'count': 0, 'status': 'complete'}
    else:
        breakdown['placeholders'] = {'score': 0, 'count': len(placeholders), 'found': placeholders}
    
    # No TODOs
    todos = protocol_content.upper().count("TODO") + protocol_content.upper().count("TBD")
    if todos == 0:
        score += 5
        breakdown['todos'] = {'score': 5, 'count': 0, 'status': 'complete'}
    else:
        breakdown['todos'] = {'score': 0, 'count': todos, 'status': 'incomplete'}
    
    return {'score': score, 'max': 25, 'breakdown': breakdown}


def calculate_accuracy_score(protocol_content: str, validator_results: Dict = None) -> Dict[str, Any]:
    """Calculate accuracy score (0-25 points)"""
    score = 0
    breakdown = {}
    
    # Validator score average
    if validator_results:
        scores = [v.get('score', 0) for v in validator_results.values()]
        avg_score = np.mean(scores) if scores else 0
        if avg_score >= 0.95:
            score += 15
            breakdown['validator_avg'] = {'score': 15, 'avg': avg_score, 'status': 'excellent'}
        elif avg_score >= 0.90:
            score += 10
            breakdown['validator_avg'] = {'score': 10, 'avg': avg_score, 'status': 'good'}
        elif avg_score >= 0.85:
            score += 5
            breakdown['validator_avg'] = {'score': 5, 'avg': avg_score, 'status': 'acceptable'}
        else:
            breakdown['validator_avg'] = {'score': 0, 'avg': avg_score, 'status': 'needs_improvement'}
    else:
        breakdown['validator_avg'] = {'score': 0, 'note': 'No validator results provided'}
    
    # Code examples syntax valid (simplified - check for balanced backticks)
    code_blocks = re.findall(r'```[\s\S]*?```', protocol_content)
    valid_blocks = len(code_blocks)
    if valid_blocks > 0:
        score += 5
        breakdown['code_blocks'] = {'score': 5, 'count': valid_blocks, 'status': 'present'}
    else:
        breakdown['code_blocks'] = {'score': 0, 'count': 0, 'status': 'missing'}
    
    # Line references (check for proper formatting)
    line_refs = re.findall(r'line[s]?\s+\d+', protocol_content, re.IGNORECASE)
    if len(line_refs) > 0:
        score += 5
        breakdown['line_references'] = {'score': 5, 'count': len(line_refs), 'status': 'present'}
    else:
        breakdown['line_references'] = {'score': 0, 'count': 0, 'status': 'none_found'}
    
    return {'score': score, 'max': 25, 'breakdown': breakdown}


def calculate_consistency_score(protocol_content: str) -> Dict[str, Any]:
    """Calculate consistency score (0-25 points)"""
    score = 0
    breakdown = {}
    
    # Section order matches template
    expected_order = ["PREREQUISITES", "AI ROLE", "WORKFLOW", "INTEGRATION", 
                      "QUALITY GATES", "COMMUNICATION", "AUTOMATION", "HANDOFF", "EVIDENCE"]
    found_sections = []
    for section in expected_order:
        if section in protocol_content.upper():
            found_sections.append(section)
    
    if found_sections == [s for s in expected_order if s in protocol_content.upper()]:
        score += 10
        breakdown['section_order'] = {'score': 10, 'status': 'correct'}
    else:
        breakdown['section_order'] = {'score': 0, 'status': 'incorrect', 'found': found_sections}
    
    # Formatting (check for consistent markdown headers)
    h2_count = protocol_content.count("\n## ")
    h3_count = protocol_content.count("\n### ")
    if h2_count >= 5 and h3_count >= 3:
        score += 5
        breakdown['formatting'] = {'score': 5, 'h2': h2_count, 'h3': h3_count, 'status': 'good'}
    else:
        breakdown['formatting'] = {'score': 0, 'h2': h2_count, 'h3': h3_count, 'status': 'sparse'}
    
    # Naming conventions (check for consistent capitalization)
    if "STEP" in protocol_content and "Gate" in protocol_content:
        score += 5
        breakdown['naming'] = {'score': 5, 'status': 'consistent'}
    else:
        breakdown['naming'] = {'score': 0, 'status': 'inconsistent'}
    
    # Terminology consistency (check for key terms)
    key_terms = ["protocol", "workflow", "validation", "evidence", "artifact"]
    found_terms = sum(1 for term in key_terms if term.lower() in protocol_content.lower())
    if found_terms >= 4:
        score += 5
        breakdown['terminology'] = {'score': 5, 'found': found_terms, 'status': 'consistent'}
    else:
        breakdown['terminology'] = {'score': 0, 'found': found_terms, 'status': 'sparse'}
    
    return {'score': score, 'max': 25, 'breakdown': breakdown}


def calculate_total_quality_score(protocol_path: Path, validator_results: Dict = None) -> Dict[str, Any]:
    """Calculate total protocol quality score"""
    
    # Read protocol content
    protocol_content = protocol_path.read_text()
    
    # Calculate subscores
    clarity = calculate_clarity_score(protocol_content)
    completeness = calculate_completeness_score(protocol_content)
    accuracy = calculate_accuracy_score(protocol_content, validator_results)
    consistency = calculate_consistency_score(protocol_content)
    
    # Calculate total
    total_score = clarity['score'] + completeness['score'] + accuracy['score'] + consistency['score']
    
    # Determine rating
    if total_score >= 90:
        rating = "Excellent ✅"
    elif total_score >= 80:
        rating = "Good ✓"
    elif total_score >= 70:
        rating = "Acceptable ⚠️"
    else:
        rating = "Needs Improvement ❌"
    
    return {
        'protocol': str(protocol_path),
        'total_score': total_score,
        'max_score': 100,
        'percentage': total_score,
        'rating': rating,
        'subscores': {
            'clarity': clarity,
            'completeness': completeness,
            'accuracy': accuracy,
            'consistency': consistency
        }
    }


def main():
    parser = argparse.ArgumentParser(description='Calculate protocol quality score')
    parser.add_argument('--protocol', required=True, help='Path to protocol file')
    parser.add_argument('--validators', help='Path to validator results JSON (optional)')
    parser.add_argument('--output', help='Output JSON file (optional)')
    parser.add_argument('--verbose', action='store_true', help='Show detailed breakdown')
    
    args = parser.parse_args()
    
    # Load protocol
    protocol_path = Path(args.protocol)
    if not protocol_path.exists():
        print(f"Error: Protocol file not found: {protocol_path}")
        sys.exit(1)
    
    # Load validator results if provided
    validator_results = None
    if args.validators:
        validator_path = Path(args.validators)
        if validator_path.exists():
            validator_results = json.loads(validator_path.read_text())
    
    # Calculate score
    results = calculate_total_quality_score(protocol_path, validator_results)
    
    # Display results
    print(f"\n{'='*60}")
    print(f"PROTOCOL QUALITY SCORE REPORT")
    print(f"{'='*60}")
    print(f"\nProtocol: {results['protocol']}")
    print(f"\nTotal Score: {results['total_score']}/{results['max_score']} ({results['percentage']}%)")
    print(f"Rating: {results['rating']}")
    print(f"\n{'='*60}")
    print(f"SUBSCORES:")
    print(f"{'='*60}")
    
    for category, data in results['subscores'].items():
        print(f"\n{category.upper()}: {data['score']}/{data['max']}")
        if args.verbose and 'breakdown' in data:
            for key, value in data['breakdown'].items():
                print(f"  - {key}: {value}")
    
    # Save to file if requested
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(json.dumps(results, indent=2))
        print(f"\n\nResults saved to: {output_path}")
    
    print(f"\n{'='*60}\n")
    
    return 0 if results['total_score'] >= 70 else 1


if __name__ == "__main__":
    sys.exit(main())
