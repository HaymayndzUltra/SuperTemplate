#!/usr/bin/env python3
"""
Classify Project Type
Determines primary project classification based on project brief and architecture.
Classifications: Generic Web App, AI/ML Application, Hybrid, Data Pipeline, Mobile, API/Microservice, Other
"""
import argparse
import json
import sys
import yaml
from pathlib import Path
from datetime import datetime

def load_classification_config(config_path: Path) -> dict:
    """Load classification dimensions configuration."""
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return {}

def calculate_keyword_score(content: str, keywords: list) -> tuple[float, list]:
    """Calculate keyword match score and return matched keywords."""
    content_lower = content.lower()
    matched = []
    for keyword in keywords:
        if keyword.lower() in content_lower:
            matched.append(keyword)
    
    if not keywords:
        return 0.0, []
    
    score = len(matched) / len(keywords)
    return score, matched

def classify_ai_ml(brief_data: dict, arch_data: dict) -> tuple[float, list]:
    """Check if project is AI/ML focused."""
    evidence = []
    score = 0.0
    
    # Check tech stack for AI/ML frameworks
    ai_frameworks = ['tensorflow', 'pytorch', 'scikit-learn', 'keras', 'langchain', 'openai', 'anthropic']
    tech_stack = brief_data.get('tech_stack', {})
    ai_ml_stack = tech_stack.get('ai_ml', [])
    
    if ai_ml_stack:
        score += 0.4
        evidence.append(f"AI/ML frameworks detected: {', '.join(ai_ml_stack)}")
    
    # Check explicit protocol mentions
    protocol_mentions = brief_data.get('explicit_protocol_mentions', [])
    ai_mentions = [m for m in protocol_mentions if any(k in m.lower() for k in ['model', 'training', 'machine learning', 'ai'])]
    if ai_mentions:
        score += 0.3
        evidence.append(f"AI-related mentions: {', '.join(ai_mentions)}")
    
    # Check project goals for AI keywords
    goals = brief_data.get('project_goals', [])
    ai_keywords = ['model', 'training', 'prediction', 'inference', 'machine learning', 'neural', 'embedding']
    goals_text = ' '.join(goals).lower()
    ai_goal_matches = [k for k in ai_keywords if k in goals_text]
    if ai_goal_matches:
        score += 0.3
        evidence.append(f"AI keywords in goals: {', '.join(ai_goal_matches)}")
    
    return min(score, 1.0), evidence

def classify_web_app(brief_data: dict, arch_data: dict) -> tuple[float, list]:
    """Check if project is a generic web application."""
    evidence = []
    score = 0.0
    
    tech_stack = brief_data.get('tech_stack', {})
    
    # Check for frontend frameworks
    frontend = tech_stack.get('frontend', [])
    web_frameworks = ['react', 'vue', 'angular', 'next.js', 'nuxt', 'svelte']
    frontend_matches = [f for f in frontend if any(w.lower() in f.lower() for w in web_frameworks)]
    if frontend_matches:
        score += 0.4
        evidence.append(f"Frontend frameworks: {', '.join(frontend_matches)}")
    
    # Check for backend frameworks
    backend = tech_stack.get('backend', [])
    backend_frameworks = ['express', 'django', 'flask', 'fastapi', 'rails', 'spring']
    backend_matches = [b for b in backend if any(w.lower() in b.lower() for w in backend_frameworks)]
    if backend_matches:
        score += 0.3
        evidence.append(f"Backend frameworks: {', '.join(backend_matches)}")
    
    # Check for database
    database = tech_stack.get('database', [])
    if database:
        score += 0.2
        evidence.append(f"Database: {', '.join(database)}")
    
    # Check infrastructure
    infrastructure = tech_stack.get('infrastructure', [])
    if infrastructure:
        score += 0.1
        evidence.append(f"Infrastructure: {', '.join(infrastructure)}")
    
    return min(score, 1.0), evidence

def classify_api_microservice(brief_data: dict, arch_data: dict) -> tuple[float, list]:
    """Check if project is API/Microservice focused."""
    evidence = []
    score = 0.0
    
    tech_stack = brief_data.get('tech_stack', {})
    
    # No frontend = likely API
    frontend = tech_stack.get('frontend', [])
    if not frontend:
        score += 0.4
        evidence.append("No frontend framework detected")
    
    # Check for API frameworks
    backend = tech_stack.get('backend', [])
    api_frameworks = ['fastapi', 'express', 'flask', 'django rest', 'graphql']
    api_matches = [b for b in backend if any(w.lower() in b.lower() for w in api_frameworks)]
    if api_matches:
        score += 0.3
        evidence.append(f"API frameworks: {', '.join(api_matches)}")
    
    # Check architecture patterns
    arch_patterns = arch_data.get('architecture_patterns', [])
    api_patterns = ['REST API', 'GraphQL API', 'gRPC', 'Microservices Architecture']
    pattern_matches = [p for p in arch_patterns if p in api_patterns]
    if pattern_matches:
        score += 0.3
        evidence.append(f"API patterns: {', '.join(pattern_matches)}")
    
    return min(score, 1.0), evidence

def classify_data_pipeline(brief_data: dict, arch_data: dict) -> tuple[float, list]:
    """Check if project is data pipeline focused."""
    evidence = []
    score = 0.0
    
    protocol_mentions = brief_data.get('explicit_protocol_mentions', [])
    data_mentions = [m for m in protocol_mentions if any(k in m.lower() for k in ['data pipeline', 'etl', 'data processing'])]
    if data_mentions:
        score += 0.5
        evidence.append(f"Data pipeline mentions: {', '.join(data_mentions)}")
    
    # Check for data processing frameworks
    tech_stack = brief_data.get('tech_stack', {})
    all_tech = str(tech_stack).lower()
    data_frameworks = ['airflow', 'spark', 'dask', 'prefect', 'dagster']
    data_matches = [f for f in data_frameworks if f in all_tech]
    if data_matches:
        score += 0.5
        evidence.append(f"Data frameworks: {', '.join(data_matches)}")
    
    return min(score, 1.0), evidence

def classify_mobile(brief_data: dict, arch_data: dict) -> tuple[float, list]:
    """Check if project is mobile application."""
    evidence = []
    score = 0.0
    
    tech_stack = brief_data.get('tech_stack', {})
    all_tech = str(tech_stack).lower()
    
    mobile_keywords = ['react native', 'flutter', 'swift', 'kotlin', 'ios', 'android', 'mobile']
    mobile_matches = [k for k in mobile_keywords if k in all_tech]
    if mobile_matches:
        score += 0.8
        evidence.append(f"Mobile technologies: {', '.join(mobile_matches)}")
    
    return min(score, 1.0), evidence

def determine_classification(scores: dict) -> tuple[str, float, str]:
    """Determine final classification based on scores."""
    # Sort by score
    sorted_scores = sorted(scores.items(), key=lambda x: x[1][0], reverse=True)
    
    top_type, (top_score, top_evidence) = sorted_scores[0]
    
    # Check for hybrid
    ai_score = scores.get('ai_ml_application', (0, []))[0]
    web_score = scores.get('generic_web_app', (0, []))[0]
    
    if ai_score >= 0.5 and web_score >= 0.5:
        return 'hybrid_application', (ai_score + web_score) / 2, "Mix of AI/ML and web application features"
    
    # Confidence levels
    if top_score >= 0.9:
        confidence = "high"
    elif top_score >= 0.7:
        confidence = "medium"
    else:
        confidence = "low"
    
    return top_type, top_score, confidence

def main():
    parser = argparse.ArgumentParser(description='Classify project type')
    parser.add_argument('--brief', required=True, help='Path to project-brief-parsed.json')
    parser.add_argument('--architecture', help='Path to architecture-parsed.json')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 2] Classifying project type...")
    
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
    
    # Calculate scores for each classification
    scores = {
        'ai_ml_application': classify_ai_ml(brief_data, arch_data),
        'generic_web_app': classify_web_app(brief_data, arch_data),
        'api_microservice': classify_api_microservice(brief_data, arch_data),
        'data_pipeline': classify_data_pipeline(brief_data, arch_data),
        'mobile_application': classify_mobile(brief_data, arch_data)
    }
    
    # Determine final classification
    classification, confidence_score, confidence_level = determine_classification(scores)
    
    # Build result
    result = {
        "timestamp": datetime.now().isoformat(),
        "classification": classification,
        "classification_display": classification.replace('_', ' ').title(),
        "confidence_score": round(confidence_score * 100, 2),
        "confidence_level": confidence_level,
        "scores": {
            k: {"score": round(v[0] * 100, 2), "evidence": v[1]}
            for k, v in scores.items()
        },
        "input_files": {
            "brief": str(brief_path),
            "architecture": str(args.architecture) if args.architecture else None
        }
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'project-classification.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 2] Classification complete")
    print(f"  - Type: {result['classification_display']}")
    print(f"  - Confidence: {result['confidence_score']}% ({result['confidence_level']})")
    print(json.dumps(result, indent=2))
    
    # Return non-zero if confidence is too low
    if confidence_score < 0.7:
        print(f"[WARNING] Low confidence classification - human review recommended")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
