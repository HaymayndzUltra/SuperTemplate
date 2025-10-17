#!/usr/bin/env python3
"""
Standardize frontmatter for all .mdc files in project-rules according to Cursor 2025 specs.
Only modifies frontmatter; preserves rule content.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def parse_existing_frontmatter(content: str) -> Tuple[Dict[str, str], str]:
    """Parse existing frontmatter and return (metadata, body)"""
    if not content.startswith('---\n'):
        return {}, content
    
    try:
        end_idx = content.find('\n---\n', 4)
        if end_idx == -1:
            return {}, content
        
        frontmatter_text = content[4:end_idx]
        body = content[end_idx + 5:]  # Skip \n---\n
        
        metadata = {}
        for line in frontmatter_text.split('\n'):
            line = line.strip()
            if ':' in line and not line.startswith('#'):
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip().strip('"\'')
        
        return metadata, body
    except Exception:
        return {}, content


def infer_globs_from_content(body: str, filename: str) -> str:
    """Infer appropriate globs pattern from rule content and filename"""
    body_lower = body.lower()
    filename_lower = filename.lower()
    
    # Framework-specific patterns
    if 'nextjs' in filename_lower or 'next.js' in body_lower:
        return 'frontend/**/*.tsx,frontend/**/*.ts,**/*.tsx,**/*.ts'
    elif 'angular' in filename_lower or 'angular' in body_lower:
        return 'frontend/**/*.ts,**/*.component.ts,**/*.service.ts'
    elif 'react' in filename_lower and 'native' not in filename_lower:
        return '**/*.tsx,**/*.jsx,**/*.ts,**/*.js'
    elif 'vue' in filename_lower:
        return '**/*.vue,**/*.ts,**/*.js'
    elif 'fastapi' in filename_lower:
        return 'backend/**/*.py,**/*main.py,**/*api*.py'
    elif 'django' in filename_lower:
        return 'backend/**/*.py,**/models.py,**/views.py,**/urls.py'
    elif 'nestjs' in filename_lower:
        return 'backend/**/*.ts,**/*.controller.ts,**/*.service.ts'
    elif 'golang' in filename_lower or 'go' in filename_lower:
        return 'backend/**/*.go,**/*main.go,**/*api*.go'
    
    # Language-specific patterns
    elif 'typescript' in filename_lower:
        return '**/*.ts,**/*.tsx'
    elif 'python' in filename_lower:
        return '**/*.py'
    elif 'javascript' in filename_lower:
        return '**/*.js,**/*.jsx'
    elif 'html' in filename_lower:
        return '**/*.html,**/*.htm'
    elif 'css' in filename_lower:
        return '**/*.css,**/*.scss,**/*.sass'
    
    # Testing patterns
    elif 'test' in filename_lower or 'spec' in body_lower:
        return '**/*.test.ts,**/*.spec.ts,**/*.test.js,**/*.spec.js'
    
    # Infrastructure patterns
    elif 'terraform' in filename_lower:
        return '**/*.tf,**/*.tfvars'
    elif 'docker' in body_lower:
        return '**/Dockerfile,**/docker-compose.yml,**/*.dockerfile'
    
    # Compliance patterns (usually always apply)
    elif any(word in filename_lower for word in ['hipaa', 'gdpr', 'sox', 'pci', 'compliance']):
        return ''  # Empty globs for compliance (usually alwaysApply)
    
    # Utility patterns
    elif 'api' in filename_lower:
        return '**/*api*.py,**/*api*.ts,**/*api*.js'
    elif 'database' in filename_lower or 'db' in filename_lower:
        return '**/*model*.py,**/*schema*.py,**/*.sql'
    
    # Default: empty globs (agent-requested)
    return ''


def infer_always_apply(filename: str, existing_meta: Dict[str, str]) -> bool:
    """Determine if rule should be alwaysApply based on filename and content"""
    filename_lower = filename.lower()
    
    # Explicit always apply from existing metadata
    if existing_meta.get('alwaysApply') == 'true':
        return True
    
    # Compliance rules are usually always apply
    if any(word in filename_lower for word in ['compliance', 'security', 'hipaa', 'gdpr', 'sox', 'pci']):
        return True
    
    # Global/master rules
    if 'global' in filename_lower or 'master' in filename_lower:
        return True
    
    # Best practices might be always apply
    if 'best-practices' in filename_lower:
        return True
    
    # Default: false
    return False


def generate_description(filename: str, body: str, existing_meta: Dict[str, str]) -> str:
    """Generate appropriate description if missing or improve existing one"""
    
    # Use existing description if it's good
    existing_desc = existing_meta.get('description', '').strip()
    if existing_desc and len(existing_desc) > 10 and 'TAGS:' not in existing_desc:
        return existing_desc
    
    filename_lower = filename.lower().replace('.mdc', '').replace('-', ' ')
    body_lower = body.lower()
    
    # Framework descriptions
    if 'nextjs' in filename_lower:
        return "Next.js development best practices and component patterns"
    elif 'angular' in filename_lower:
        return "Angular application development guidelines and component architecture"
    elif 'react' in filename_lower and 'native' not in filename_lower:
        return "React component development and modern hooks patterns"
    elif 'vue' in filename_lower:
        return "Vue.js component development and composition API patterns"
    elif 'fastapi' in filename_lower:
        return "FastAPI backend development with async patterns and Pydantic"
    elif 'django' in filename_lower:
        return "Django web framework development and REST API patterns"
    elif 'nestjs' in filename_lower:
        return "NestJS backend development with decorators and dependency injection"
    
    # Language descriptions
    elif 'typescript' in filename_lower:
        return "TypeScript development with strict typing and modern features"
    elif 'python' in filename_lower:
        return "Python development best practices and modern coding patterns"
    elif 'javascript' in filename_lower:
        return "JavaScript development patterns and ES6+ features"
    
    # Compliance descriptions
    elif 'hipaa' in filename_lower:
        return "HIPAA compliance requirements for healthcare applications"
    elif 'gdpr' in filename_lower:
        return "GDPR compliance requirements for EU data protection"
    elif 'sox' in filename_lower:
        return "SOX compliance requirements for financial reporting"
    elif 'pci' in filename_lower:
        return "PCI DSS compliance requirements for payment processing"
    
    # Testing descriptions
    elif 'test' in filename_lower:
        return "Testing strategies and framework-specific testing patterns"
    
    # Infrastructure descriptions
    elif 'terraform' in filename_lower:
        return "Infrastructure as Code with Terraform best practices"
    elif 'azure' in filename_lower:
        return "Azure cloud services and deployment patterns"
    elif 'aws' in filename_lower:
        return "AWS cloud services and deployment patterns"
    
    # Generic fallback
    return f"Development guidelines for {filename_lower.replace('_', ' ')}"


def standardize_frontmatter_file(file_path: Path) -> bool:
    """Standardize frontmatter for a single .mdc file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        existing_meta, body = parse_existing_frontmatter(content)
        
        # Generate new frontmatter
        filename = file_path.name
        description = generate_description(filename, body, existing_meta)
        globs = infer_globs_from_content(body, filename)
        always_apply = infer_always_apply(filename, existing_meta)
        
        # Build new frontmatter
        new_frontmatter = ['---']
        new_frontmatter.append(f'description: {description}')
        if globs:
            new_frontmatter.append(f'globs: {globs}')
        else:
            new_frontmatter.append('globs:')
        new_frontmatter.append(f'alwaysApply: {str(always_apply).lower()}')
        new_frontmatter.append('---')
        
        # Combine with body
        new_content = '\n'.join(new_frontmatter) + '\n\n' + body.lstrip()
        
        # Write back
        file_path.write_text(new_content, encoding='utf-8')
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Main execution"""
    rules_dir = Path('/workspace/.cursor/rules/project-rules')
    
    if not rules_dir.exists():
        print(f"Rules directory not found: {rules_dir}")
        return 1
    
    # Find all .mdc files
    mdc_files = list(rules_dir.rglob('*.mdc'))
    print(f"Found {len(mdc_files)} .mdc files")
    
    success_count = 0
    for mdc_file in mdc_files:
        if standardize_frontmatter_file(mdc_file):
            success_count += 1
        else:
            print(f"Failed: {mdc_file}")
    
    print(f"Standardized {success_count}/{len(mdc_files)} files")
    return 0 if success_count == len(mdc_files) else 1


if __name__ == '__main__':
    exit(main())