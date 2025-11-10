#!/usr/bin/env python3
"""
Transform Protocol Templates

Transforms foundation protocol templates into project-specific instances
by applying customization rules based on PROJECT-BRIEF.md and execution plan.

Usage:
    python scripts/orchestration/transform_protocols.py \
        --templates .artifacts/protocol-05b/loaded-templates.json \
        --project-brief PROJECT-BRIEF.md \
        --execution-plan PROTOCOL-EXECUTION-PLAN.md \
        --output .artifacts/protocol-05b/transformed-protocols.json
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Add project root to path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Transform protocol templates")
    parser.add_argument(
        "--templates",
        required=True,
        help="Path to loaded-templates.json from load_protocol_templates.py"
    )
    parser.add_argument(
        "--project-brief",
        required=True,
        help="Path to PROJECT-BRIEF.md"
    )
    parser.add_argument(
        "--execution-plan",
        required=True,
        help="Path to PROTOCOL-EXECUTION-PLAN.md"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output JSON file path for transformed protocols"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    return parser.parse_args()


def extract_project_info(brief_path: Path) -> Dict:
    """Extract project information from PROJECT-BRIEF.md."""
    try:
        content = brief_path.read_text(encoding='utf-8')
        
        # Extract project name (from title or first heading)
        project_name = "unknown-project"
        for line in content.split('\n')[:30]:
            if line.startswith('# '):
                project_name = line.strip('# ').strip()
                # Convert to kebab-case
                project_name = re.sub(r'[^\w\s-]', '', project_name.lower())
                project_name = re.sub(r'[-\s]+', '-', project_name)
                break
        
        # Extract tech stack (look for common patterns)
        tech_stack = {
            "frontend": "unknown",
            "backend": "unknown",
            "database": "unknown"
        }
        
        content_lower = content.lower()
        
        # Frontend detection
        if 'next.js' in content_lower or 'nextjs' in content_lower:
            tech_stack["frontend"] = "Next.js"
        elif 'react' in content_lower:
            tech_stack["frontend"] = "React"
        elif 'vue' in content_lower:
            tech_stack["frontend"] = "Vue.js"
        
        # Backend detection
        if 'fastapi' in content_lower:
            tech_stack["backend"] = "FastAPI"
        elif 'django' in content_lower:
            tech_stack["backend"] = "Django"
        elif 'express' in content_lower:
            tech_stack["backend"] = "Express.js"
        
        # Database detection
        if 'postgresql' in content_lower or 'postgres' in content_lower:
            tech_stack["database"] = "PostgreSQL"
        elif 'mongodb' in content_lower or 'mongo' in content_lower:
            tech_stack["database"] = "MongoDB"
        elif 'mysql' in content_lower:
            tech_stack["database"] = "MySQL"
        
        return {
            "project_name": project_name,
            "tech_stack": tech_stack
        }
    except Exception as e:
        print(f"[ERROR] Failed to extract project info: {e}", file=sys.stderr)
        return {
            "project_name": "unknown-project",
            "tech_stack": {}
        }


def apply_transformations(template_content: str, project_info: Dict, protocol_id: str) -> str:
    """Apply transformation rules to template content."""
    transformed = template_content
    
    # Rule 1: Project Name Substitution
    project_name = project_info.get("project_name", "unknown-project")
    project_name_title = project_name.replace('-', ' ').title()
    
    transformed = transformed.replace("{PROJECT_NAME}", project_name_title)
    transformed = transformed.replace("{project-name}", project_name)
    
    # Rule 2: Tech Stack Customization
    tech_stack = project_info.get("tech_stack", {})
    frontend = tech_stack.get("frontend", "unknown")
    backend = tech_stack.get("backend", "unknown")
    database = tech_stack.get("database", "unknown")
    
    transformed = transformed.replace("{FRONTEND}", frontend)
    transformed = transformed.replace("{BACKEND}", backend)
    transformed = transformed.replace("{DATABASE}", database)
    
    # Rule 3: Artifact Path Customization
    # Replace generic artifact paths with project-specific paths
    transformed = re.sub(
        r'\.artifacts/protocol-(\d+)/',
        f'.artifacts/{project_name}/protocol-\\1/',
        transformed
    )
    
    # Rule 4: Protocol-specific customizations
    if protocol_id == "06":  # Create PRD
        # Add tech stack-specific validation steps
        if frontend == "Next.js":
            transformed = add_nextjs_validation(transformed)
        if backend == "FastAPI":
            transformed = add_fastapi_validation(transformed)
    
    return transformed


def add_nextjs_validation(content: str) -> str:
    """Add Next.js-specific validation steps."""
    # Find validation section and inject Next.js checks
    validation_marker = "### STEP X: Validate Build Configuration"
    if validation_marker not in content:
        return content
    
    nextjs_validation = """
### STEP X.Y: Validate Next.js Build (Framework-Specific)

**Action:** Validate Next.js build configuration:

```bash
# Next.js-specific validation
npm run build
npm run type-check
npm run lint
```

**Quality Gates**:
- TypeScript compilation: 0 errors
- ESLint: 0 errors, <10 warnings
- Build size: <500KB initial bundle
"""
    
    # Insert after validation marker
    return content.replace(validation_marker, validation_marker + "\n" + nextjs_validation)


def add_fastapi_validation(content: str) -> str:
    """Add FastAPI-specific validation steps."""
    validation_marker = "### STEP X: Validate API Configuration"
    if validation_marker not in content:
        return content
    
    fastapi_validation = """
### STEP X.Y: Validate FastAPI Configuration (Framework-Specific)

**Action:** Validate FastAPI setup:

```bash
# FastAPI-specific validation
pytest tests/
mypy src/
ruff check src/
```

**Quality Gates**:
- Test coverage: ≥80%
- Type checking: 0 errors
- Linting: 0 errors
"""
    
    return content.replace(validation_marker, validation_marker + "\n" + fastapi_validation)


def main() -> int:
    args = parse_args()
    
    # Resolve paths
    templates_path = ROOT / args.templates
    brief_path = ROOT / args.project_brief
    output_path = ROOT / args.output
    
    # Validate inputs
    if not templates_path.exists():
        print(f"[ERROR] Templates file not found: {templates_path}", file=sys.stderr)
        return 1
    
    if not brief_path.exists():
        print(f"[ERROR] Project brief not found: {brief_path}", file=sys.stderr)
        return 1
    
    # Load templates
    if args.verbose:
        print(f"[INFO] Loading templates from: {templates_path}")
    
    templates_data = json.loads(templates_path.read_text(encoding='utf-8'))
    templates = templates_data.get("templates", [])
    
    if not templates:
        print("[ERROR] No templates found in input file", file=sys.stderr)
        return 1
    
    # Extract project information
    if args.verbose:
        print(f"[INFO] Extracting project info from: {brief_path}")
    
    project_info = extract_project_info(brief_path)
    
    if args.verbose:
        print(f"[INFO] Project: {project_info['project_name']}")
        print(f"[INFO] Tech Stack: {project_info['tech_stack']}")
    
    # Transform templates
    transformed_protocols = []
    customizations_count = 0
    
    for template in templates:
        protocol_id = template["protocol_id"]
        
        if args.verbose:
            print(f"[INFO] Transforming protocol {protocol_id}")
        
        # Apply transformations
        transformed_content = apply_transformations(
            template["content"],
            project_info,
            protocol_id
        )
        
        # Count customizations applied
        customizations = 0
        if "{PROJECT_NAME}" in template["content"]:
            customizations += 1
        if "{FRONTEND}" in template["content"] or "{BACKEND}" in template["content"]:
            customizations += 1
        if ".artifacts/protocol-" in template["content"]:
            customizations += 1
        
        customizations_count += customizations
        
        transformed_protocols.append({
            "protocol_id": protocol_id,
            "source_template": template["template_path"],
            "transformed_content": transformed_content,
            "customizations_applied": customizations,
            "size_bytes": len(transformed_content),
            "line_count": len(transformed_content.split('\n'))
        })
    
    # Create output
    output_data = {
        "transformed_count": len(transformed_protocols),
        "total_customizations": customizations_count,
        "project_info": project_info,
        "protocols": transformed_protocols,
        "metadata": {
            "source_templates": str(templates_path),
            "project_brief": str(brief_path),
            "total_size_bytes": sum(p["size_bytes"] for p in transformed_protocols),
            "total_lines": sum(p["line_count"] for p in transformed_protocols)
        }
    }
    
    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output_data, indent=2), encoding='utf-8')
    
    if args.verbose:
        print(f"[INFO] Transformed {len(transformed_protocols)} protocols")
        print(f"[INFO] Applied {customizations_count} customizations")
        print(f"[INFO] Output written to: {output_path}")
    
    print(f"[OK] Transformed {len(transformed_protocols)} protocols with {customizations_count} customizations")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
