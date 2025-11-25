#!/usr/bin/env python3
"""
Parse architecture-principles.md and extract architecture context.
Extracts system architecture patterns, technical constraints, integration requirements, infrastructure requirements, and security requirements.
"""
import argparse
import json
import sys
import re
from pathlib import Path
from datetime import datetime

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

def extract_architecture_patterns(sections: dict) -> list:
    """Extract system architecture patterns."""
    patterns = []
    
    pattern_keywords = {
        'microservices': 'Microservices Architecture',
        'monolith': 'Monolithic Architecture',
        'serverless': 'Serverless Architecture',
        'event-driven': 'Event-Driven Architecture',
        'layered': 'Layered Architecture',
        'hexagonal': 'Hexagonal Architecture',
        'clean architecture': 'Clean Architecture',
        'cqrs': 'CQRS Pattern',
        'domain-driven': 'Domain-Driven Design',
        'rest': 'REST API',
        'graphql': 'GraphQL API',
        'grpc': 'gRPC',
        'websocket': 'WebSocket',
        'message queue': 'Message Queue Pattern',
        'pub/sub': 'Pub/Sub Pattern'
    }
    
    arch_sections = ['System Architecture', 'Architecture', 'Technical Architecture', 'Architecture Patterns']
    for section_name in arch_sections:
        if section_name in sections:
            content = sections[section_name].lower()
            for keyword, pattern_name in pattern_keywords.items():
                if keyword in content and pattern_name not in patterns:
                    patterns.append(pattern_name)
    
    # Also check full content
    full_content = '\n'.join(sections.values()).lower()
    for keyword, pattern_name in pattern_keywords.items():
        if keyword in full_content and pattern_name not in patterns:
            patterns.append(pattern_name)
    
    return patterns

def extract_technical_constraints(sections: dict) -> list:
    """Extract technical constraints."""
    constraints = []
    
    constraint_sections = ['Technical Constraints', 'Constraints', 'Limitations', 'Requirements']
    for section_name in constraint_sections:
        if section_name in sections:
            content = sections[section_name]
            # Extract bullet points
            items = re.findall(r'[-*•]\s+(.+?)(?=\n[-*•]|\n\n|$)', content, re.DOTALL)
            for item in items:
                item = item.strip().split('\n')[0]
                if item and len(item) > 5:
                    constraints.append(item)
            break
    
    return constraints

def extract_integration_requirements(sections: dict) -> list:
    """Extract integration requirements."""
    integrations = []
    
    integration_keywords = {
        'oauth': 'OAuth Integration',
        'sso': 'Single Sign-On',
        'api integration': 'Third-party API Integration',
        'webhook': 'Webhook Integration',
        'payment': 'Payment Gateway Integration',
        'email': 'Email Service Integration',
        'sms': 'SMS Service Integration',
        'analytics': 'Analytics Integration',
        'monitoring': 'Monitoring Integration',
        'logging': 'Logging Integration',
        'cdn': 'CDN Integration',
        'storage': 'Cloud Storage Integration'
    }
    
    integration_sections = ['Integration Requirements', 'Integrations', 'External Services']
    for section_name in integration_sections:
        if section_name in sections:
            content = sections[section_name].lower()
            for keyword, integration_name in integration_keywords.items():
                if keyword in content and integration_name not in integrations:
                    integrations.append(integration_name)
    
    # Check full content
    full_content = '\n'.join(sections.values()).lower()
    for keyword, integration_name in integration_keywords.items():
        if keyword in full_content and integration_name not in integrations:
            integrations.append(integration_name)
    
    return integrations

def extract_infrastructure_requirements(sections: dict) -> dict:
    """Extract infrastructure requirements."""
    infrastructure = {
        "cloud_provider": [],
        "compute": [],
        "storage": [],
        "networking": [],
        "deployment": []
    }
    
    infra_sections = ['Infrastructure Requirements', 'Infrastructure', 'Deployment', 'DevOps']
    full_content = '\n'.join(sections.values()).lower()
    
    # Cloud providers
    cloud_providers = {'aws': 'AWS', 'gcp': 'GCP', 'azure': 'Azure', 'vercel': 'Vercel', 'railway': 'Railway', 'fly.io': 'Fly.io'}
    for keyword, name in cloud_providers.items():
        if keyword in full_content:
            infrastructure['cloud_provider'].append(name)
    
    # Compute
    compute_keywords = {'docker': 'Docker', 'kubernetes': 'Kubernetes', 'lambda': 'AWS Lambda', 'cloud run': 'Cloud Run', 'ecs': 'ECS', 'ec2': 'EC2'}
    for keyword, name in compute_keywords.items():
        if keyword in full_content:
            infrastructure['compute'].append(name)
    
    # Storage
    storage_keywords = {'s3': 'S3', 'blob storage': 'Blob Storage', 'cloud storage': 'Cloud Storage'}
    for keyword, name in storage_keywords.items():
        if keyword in full_content:
            infrastructure['storage'].append(name)
    
    # Deployment
    deployment_keywords = {'ci/cd': 'CI/CD Pipeline', 'github actions': 'GitHub Actions', 'gitlab ci': 'GitLab CI', 'jenkins': 'Jenkins'}
    for keyword, name in deployment_keywords.items():
        if keyword in full_content:
            infrastructure['deployment'].append(name)
    
    return infrastructure

def extract_security_requirements(sections: dict) -> list:
    """Extract security requirements."""
    security = []
    
    security_keywords = {
        'authentication': 'Authentication Required',
        'authorization': 'Authorization Required',
        'encryption': 'Data Encryption',
        'ssl': 'SSL/TLS',
        'https': 'HTTPS Required',
        'rate limiting': 'Rate Limiting',
        'input validation': 'Input Validation',
        'api key': 'API Key Management',
        'jwt': 'JWT Authentication',
        'oauth': 'OAuth 2.0',
        'rbac': 'Role-Based Access Control',
        'audit': 'Audit Logging',
        'gdpr': 'GDPR Compliance',
        'hipaa': 'HIPAA Compliance',
        'soc 2': 'SOC 2 Compliance'
    }
    
    security_sections = ['Security Requirements', 'Security', 'Compliance']
    full_content = '\n'.join(sections.values()).lower()
    
    for keyword, requirement in security_keywords.items():
        if keyword in full_content and requirement not in security:
            security.append(requirement)
    
    return security

def main():
    parser = argparse.ArgumentParser(description='Parse architecture-principles.md')
    parser.add_argument('--input', default='architecture-principles.md', help='Input architecture file')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    input_path = workspace / args.input
    
    # Also check .artifacts location
    if not input_path.exists():
        alt_path = workspace / '.artifacts' / 'protocol-05' / 'architecture-principles.md'
        if alt_path.exists():
            input_path = alt_path
    
    if not input_path.exists():
        print(f"[WARNING] architecture-principles.md not found: {input_path}")
        # Return empty structure instead of failing
        parsed_data = {
            "status": "not_found",
            "architecture_patterns": [],
            "technical_constraints": [],
            "integration_requirements": [],
            "infrastructure_requirements": {},
            "security_requirements": [],
            "sections_detected": []
        }
    else:
        print(f"[PROTOCOL 05B | PHASE 1] Parsing architecture-principles.md...")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        sections = extract_sections(content)
        
        parsed_data = {
            "status": "parsed",
            "architecture_patterns": extract_architecture_patterns(sections),
            "technical_constraints": extract_technical_constraints(sections),
            "integration_requirements": extract_integration_requirements(sections),
            "infrastructure_requirements": extract_infrastructure_requirements(sections),
            "security_requirements": extract_security_requirements(sections),
            "sections_detected": list(sections.keys())
        }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'architecture-parsed.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(parsed_data, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 1] Architecture parsed, output: {output_path}")
    print(json.dumps(parsed_data, indent=2))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
