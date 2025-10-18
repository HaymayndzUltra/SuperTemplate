#!/usr/bin/env python3
"""
Real Job Post Analysis Script
Actually parses and analyzes job post content
"""
import json
import re
from pathlib import Path
from typing import Dict, List, Any
import nltk
from textstat import flesch_reading_ease, flesch_kincaid_grade

def analyze_job_post(file_path: str) -> Dict[str, Any]:
    """Actually analyze job post content"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Real text analysis
    sentences = nltk.sent_tokenize(content)
    words = nltk.word_tokenize(content)
    
    # Extract actual requirements
    tech_stack = extract_tech_stack(content)
    timeline = extract_timeline(content)
    budget = extract_budget(content)
    
    # Real readability analysis
    readability_score = flesch_reading_ease(content)
    grade_level = flesch_kincaid_grade(content)
    
    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "tech_stack": tech_stack,
        "timeline": timeline,
        "budget": budget,
        "readability_score": readability_score,
        "grade_level": grade_level,
        "analysis_timestamp": "2025-01-18T14:30:00Z"
    }

def extract_tech_stack(content: str) -> List[str]:
    """Extract actual technology mentions"""
    tech_patterns = [
        r'Next\.js', r'React', r'Vue', r'Angular',
        r'FastAPI', r'Django', r'Flask', r'Express',
        r'PostgreSQL', r'MySQL', r'MongoDB', r'Redis',
        r'Docker', r'Kubernetes', r'AWS', r'Azure'
    ]
    
    found_tech = []
    for pattern in tech_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            found_tech.append(pattern.replace(r'\.', '.'))
    
    return found_tech

def extract_timeline(content: str) -> str:
    """Extract actual timeline information"""
    timeline_patterns = [
        r'(\d+)\s*weeks?',
        r'(\d+)\s*months?',
        r'(\d+)\s*days?'
    ]
    
    for pattern in timeline_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            return match.group(0)
    
    return "Not specified"

def extract_budget(content: str) -> str:
    """Extract actual budget information"""
    budget_patterns = [
        r'\$[\d,]+(?:k|K)?',
        r'[\d,]+(?:k|K)?\s*dollars?'
    ]
    
    for pattern in budget_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            return match.group(0)
    
    return "Not specified"

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python analyze_jobpost.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        result = analyze_job_post(input_file)
        
        # Write real analysis results
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        
        print(f"Analysis complete. Results saved to {output_file}")
        
    except Exception as e:
        print(f"Error analyzing job post: {e}")
        sys.exit(1)
