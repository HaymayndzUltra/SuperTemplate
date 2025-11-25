#!/usr/bin/env python3
"""
Parse PROJECT-BRIEF.md and extract structured data
Extracts project_name, project_goals, deliverables, tech_stack, quality_requirements, timeline_constraints, team_structure, and explicit_protocol_mentions.
"""
import argparse
import json
import sys
import re
import yaml
from pathlib import Path
from datetime import datetime

def extract_yaml_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter if present."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1])
                remaining = parts[2].strip()
                return frontmatter or {}, remaining
            except yaml.YAMLError:
                pass
    return {}, content

def extract_sections(content: str) -> dict:
    """Extract markdown sections from content."""
    sections = {}
    current_section = None
    current_content = []
    
    lines = content.split('\n')
    for line in lines:
        header_match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if header_match:
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = header_match.group(2).strip()
            current_content = []
        elif current_section:
            current_content.append(line)
    
    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return sections

def extract_project_name(sections: dict, frontmatter: dict) -> str:
    """Extract project name from brief."""
    # Check frontmatter first
    if 'name' in frontmatter:
        return frontmatter['name']
    
    # Check sections
    for section_name in ['Executive Summary', 'Project Name', 'Project Title']:
        if section_name in sections:
            content = sections[section_name]
            # Try to extract name from first line
            first_line = content.split('\n')[0].strip()
            if ':' in first_line:
                return first_line.split(':', 1)[1].strip()
            return first_line
    
    # Try to extract from title
    for key in sections.keys():
        if 'project' in key.lower() and 'brief' not in key.lower():
            return key
    
    return "Unknown Project"

def extract_project_goals(sections: dict) -> list:
    """Extract project goals as array of strings."""
    goals = []
    
    goal_sections = ['Project Goals', 'Goals', 'Objectives', 'Business Objectives', 'Executive Summary']
    for section_name in goal_sections:
        if section_name in sections:
            content = sections[section_name]
            # Split by lines, bullets, or numbered items
            lines = re.split(r'\n\s*[-*•]\s+|\n\s*\d+\.\s+', content)
            for line in lines:
                line = line.strip()
                if line and len(line) > 10:  # Meaningful goal
                    goals.append(line)
            break
    
    return goals

def extract_deliverables(sections: dict) -> list:
    """Extract deliverables as array of objects."""
    deliverables = []
    
    deliverable_sections = ['Deliverables', 'Deliverable', 'Outputs', 'Scope']
    for section_name in deliverable_sections:
        if section_name in sections:
            content = sections[section_name]
            # Extract bullet points or numbered items
            items = re.findall(r'[-*•]\s+(.+?)(?=\n[-*•]|\n\n|$)', content, re.DOTALL)
            for item in items:
                item = item.strip()
                if item:
                    deliverables.append({
                        "name": item.split('\n')[0],
                        "description": item
                    })
            break
    
    return deliverables

def extract_tech_stack(sections: dict, frontmatter: dict) -> dict:
    """Extract technical stack information."""
    tech_stack = {
        "frontend": [],
        "backend": [],
        "database": [],
        "infrastructure": [],
        "ai_ml": []
    }
    
    # Check frontmatter first
    if 'frontend' in frontmatter:
        tech_stack['frontend'] = [frontmatter['frontend']] if isinstance(frontmatter['frontend'], str) else frontmatter['frontend']
    if 'backend' in frontmatter:
        tech_stack['backend'] = [frontmatter['backend']] if isinstance(frontmatter['backend'], str) else frontmatter['backend']
    if 'database' in frontmatter:
        tech_stack['database'] = [frontmatter['database']] if isinstance(frontmatter['database'], str) else frontmatter['database']
    
    # Extract from Technical Architecture or Technical Stack sections
    tech_sections = ['Technical Architecture', 'Technical Stack', 'Technology Stack', 'Tech Stack']
    for section_name in tech_sections:
        if section_name in sections:
            content = sections[section_name].lower()
            
            # Frontend frameworks
            frontend_keywords = ['next.js', 'react', 'vue', 'angular', 'svelte', 'nuxt']
            for keyword in frontend_keywords:
                if keyword in content and keyword not in ' '.join(tech_stack['frontend']).lower():
                    tech_stack['frontend'].append(keyword.title())
            
            # Backend frameworks
            backend_keywords = ['fastapi', 'django', 'flask', 'express', 'rails', 'spring']
            for keyword in backend_keywords:
                if keyword in content and keyword not in ' '.join(tech_stack['backend']).lower():
                    tech_stack['backend'].append(keyword.title())
            
            # Databases
            db_keywords = ['postgresql', 'mysql', 'mongodb', 'redis', 'sqlite', 'supabase']
            for keyword in db_keywords:
                if keyword in content and keyword not in ' '.join(tech_stack['database']).lower():
                    tech_stack['database'].append(keyword.title())
            
            # AI/ML frameworks
            ai_keywords = ['tensorflow', 'pytorch', 'scikit-learn', 'langchain', 'openai', 'claude']
            for keyword in ai_keywords:
                if keyword in content and keyword not in ' '.join(tech_stack['ai_ml']).lower():
                    tech_stack['ai_ml'].append(keyword.title())
            
            # Infrastructure
            infra_keywords = ['aws', 'gcp', 'azure', 'vercel', 'railway', 'docker', 'kubernetes']
            for keyword in infra_keywords:
                if keyword in content and keyword not in ' '.join(tech_stack['infrastructure']).lower():
                    tech_stack['infrastructure'].append(keyword.upper() if keyword in ['aws', 'gcp', 'azure'] else keyword.title())
            
            break
    
    return tech_stack

def extract_quality_requirements(sections: dict) -> dict:
    """Extract quality requirements."""
    quality = {}
    
    quality_sections = ['Quality Requirements', 'Quality', 'Quality Standards', 'Development Priorities']
    for section_name in quality_sections:
        if section_name in sections:
            content = sections[section_name]
            # Extract key quality aspects
            if 'code quality' in content.lower() or 'testing' in content.lower():
                quality['code_quality'] = True
            if 'performance' in content.lower():
                quality['performance'] = True
            if 'security' in content.lower():
                quality['security'] = True
            if 'documentation' in content.lower():
                quality['documentation'] = True
            break
    
    return quality

def extract_timeline_constraints(sections: dict) -> dict:
    """Extract timeline constraints."""
    timeline = {}
    
    timeline_sections = ['Timeline Constraints', 'Timeline', 'Schedule', 'Time Constraints', 'Deployment']
    for section_name in timeline_sections:
        if section_name in sections:
            content = sections[section_name]
            # Look for time-related keywords
            if 'deadline' in content.lower():
                timeline['has_deadline'] = True
            if 'milestone' in content.lower():
                timeline['has_milestones'] = True
            break
    
    return timeline

def extract_team_structure(sections: dict, frontmatter: dict) -> dict:
    """Extract team structure information."""
    team = {}
    
    # Check frontmatter
    if 'separate_repos' in frontmatter:
        team['separate_repos'] = frontmatter['separate_repos']
    
    team_sections = ['Team Structure', 'Team', 'Team Composition']
    for section_name in team_sections:
        if section_name in sections:
            content = sections[section_name].lower()
            if 'solo' in content or 'individual' in content:
                team['structure'] = 'solo'
            elif 'team' in content:
                team['structure'] = 'team'
            break
    
    return team

def extract_explicit_protocol_mentions(content: str) -> list:
    """Extract explicit protocol mentions (e.g., 'need AI model training')."""
    mentions = []
    
    protocol_keywords = [
        'ai model training', 'model training', 'machine learning',
        'data pipeline', 'feature engineering', 'model deployment',
        'authentication', 'user management', 'ci/cd', 'monitoring'
    ]
    
    content_lower = content.lower()
    for keyword in protocol_keywords:
        if keyword in content_lower:
            mentions.append(keyword)
    
    return mentions

def main():
    parser = argparse.ArgumentParser(description='Parse PROJECT-BRIEF.md and extract structured data')
    parser.add_argument('--input', default='PROJECT-BRIEF.md', help='Input PROJECT-BRIEF.md file')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    input_path = workspace / args.input
    
    if not input_path.exists():
        print(f"[ERROR] PROJECT-BRIEF.md not found: {input_path}")
        return 1
    
    print(f"[PROTOCOL 05B | PHASE 1] Parsing PROJECT-BRIEF.md...")
    
    # Read file
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter and content
    frontmatter, content = extract_yaml_frontmatter(content)
    
    # Extract sections
    sections = extract_sections(content)
    
    # Extract structured data
    parsed_data = {
        "project_name": extract_project_name(sections, frontmatter),
        "project_goals": extract_project_goals(sections),
        "deliverables": extract_deliverables(sections),
        "tech_stack": extract_tech_stack(sections, frontmatter),
        "quality_requirements": extract_quality_requirements(sections),
        "timeline_constraints": extract_timeline_constraints(sections),
        "team_structure": extract_team_structure(sections, frontmatter),
        "explicit_protocol_mentions": extract_explicit_protocol_mentions(content),
        "frontmatter": frontmatter,
        "sections_detected": list(sections.keys())
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'project-brief-parsed.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(parsed_data, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 1] Parsed data written to: {output_path}")
    print(json.dumps(parsed_data, indent=2))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
