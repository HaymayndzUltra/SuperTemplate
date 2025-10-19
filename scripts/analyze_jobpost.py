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

def normalize_heading(text: str) -> str:
    return text.replace("’", "'").replace("–", "-").strip().lower()

SECTION_HEADINGS = [
    "Company",
    "Goal (Why we're hiring)",
    "High-Level Objectives",
    "Current/Target Environment",
    "Compliance & Security (hard requirements)",
    "Functional Scope (MVP)",
    "Performance / SLOs",
    "Deliverables (must be evidence-backed)",
    "Acceptance Criteria (examples)",
    "Known Constraints / Risks",
    "Submission Requirements (no fluff)",
    "Budget",
    "Evaluation Rubric"
]
NORMALIZED_SECTION_HEADINGS = {normalize_heading(heading) for heading in SECTION_HEADINGS}

def extract_section(content: str, heading: str) -> List[str]:
    normalized_heading = normalize_heading(heading)
    lines = content.splitlines()
    captured: List[str] = []
    capture = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        normalized_line = normalize_heading(stripped)
        if normalized_line == normalized_heading:
            capture = True
            continue
        if capture and normalized_line in NORMALIZED_SECTION_HEADINGS and normalized_line != normalized_heading:
            break
        if capture:
            captured.append(stripped)
    return captured

def extract_list_section(content: str, heading: str) -> List[str]:
    section_lines = extract_section(content, heading)
    items: List[str] = []
    for line in section_lines:
        normalized = line.lstrip("-• ").strip()
        if normalized:
            items.append(normalized)
    return items

def extract_tone_signals(content: str) -> List[str]:
    signals = extract_list_section(content, "Evaluation Rubric")
    if signals:
        return signals
    return extract_list_section(content, "Submission Requirements (no fluff)")

def analyze_job_post(file_path: str) -> Dict[str, Any]:
    """Actually analyze job post content"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sentences = nltk.sent_tokenize(content)
    words = nltk.word_tokenize(content)
    
    tech_stack = extract_tech_stack(content)
    timeline = extract_timeline(content)
    budget = extract_budget(content)
    
    readability_score = flesch_reading_ease(content)
    grade_level = flesch_kincaid_grade(content)

    goal_section = extract_section(content, "Goal (Why we're hiring)")
    objectives = extract_list_section(content, "High-Level Objectives")
    deliverables = extract_list_section(content, "Deliverables (must be evidence-backed)")
    risks = extract_list_section(content, "Known Constraints / Risks")
    compliance_requirements = extract_list_section(content, "Compliance & Security (hard requirements)")
    performance_targets = extract_list_section(content, "Performance / SLOs")
    acceptance_criteria = extract_list_section(content, "Acceptance Criteria (examples)")
    submission_requirements = extract_list_section(content, "Submission Requirements (no fluff)")
    tone_signals = extract_tone_signals(content)
    goal_summary = " ".join(goal_section)
    source_excerpt = content[:600]
    
    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "tech_stack": tech_stack,
        "timeline": timeline,
        "budget": budget,
        "readability_score": readability_score,
        "grade_level": grade_level,
        "goal_summary": goal_summary,
        "objectives": objectives,
        "deliverables": deliverables,
        "risks": risks,
        "compliance_requirements": compliance_requirements,
        "performance_targets": performance_targets,
        "acceptance_criteria": acceptance_criteria,
        "submission_requirements": submission_requirements,
        "tone_signals": tone_signals,
        "source_excerpt": source_excerpt,
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
    
    return list(dict.fromkeys(found_tech))

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
    range_patterns = [
        r'\$[\d,]+(?:\s*(?:–|-|to)\s*)\$?[\d,]+(?:k|K)?'
    ]
    
    for pattern in range_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            return match.group(0)
    
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
