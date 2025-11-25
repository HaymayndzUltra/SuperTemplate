#!/usr/bin/env python3
"""
Validate PROJECT-BRIEF.md Integrity
Validates that PROJECT-BRIEF.md exists and contains all required sections.
"""
import argparse
import json
import sys
import re
from pathlib import Path
from datetime import datetime

def validate_file_exists(file_path: Path) -> tuple[bool, str]:
    """Check if file exists and is readable."""
    if not file_path.exists():
        return False, f"File not found: {file_path}"
    if not file_path.is_file():
        return False, f"Path is not a file: {file_path}"
    if not file_path.stat().st_size > 0:
        return False, f"File is empty: {file_path}"
    return True, "File exists and is readable"

def extract_sections(content: str) -> dict:
    """Extract markdown sections from content."""
    sections = {}
    current_section = None
    current_content = []
    
    lines = content.split('\n')
    for line in lines:
        # Check for markdown headers (# ## ###)
        header_match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if header_match:
            # Save previous section if exists
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            # Start new section
            current_section = header_match.group(2).strip()
            current_content = []
        elif current_section:
            current_content.append(line)
    
    # Save last section
    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return sections

def check_section_presence(sections: dict, required_sections: list) -> tuple[bool, list]:
    """Check if required sections are present."""
    missing = []
    found = []
    
    for required in required_sections:
        # Check exact match
        found_section = None
        for section_name in sections.keys():
            if required.lower() in section_name.lower():
                found_section = section_name
                break
        
        if found_section:
            found.append(found_section)
        else:
            missing.append(required)
    
    return len(missing) == 0, missing, found

def validate_project_brief(file_path: Path) -> dict:
    """Validate PROJECT-BRIEF.md structure and content."""
    checks = []
    all_passed = True
    
    # Check file exists
    exists, msg = validate_file_exists(file_path)
    checks.append({
        "check": "File exists",
        "status": "pass" if exists else "fail",
        "message": msg
    })
    if not exists:
        return {
            "status": "fail",
            "checks": checks,
            "checks_passed": 0,
            "checks_total": len(checks)
        }
    
    # Read file content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        checks.append({
            "check": "File readable",
            "status": "fail",
            "message": f"Error reading file: {str(e)}"
        })
        return {
            "status": "fail",
            "checks": checks,
            "checks_passed": 0,
            "checks_total": len(checks)
        }
    
    checks.append({
        "check": "File readable",
        "status": "pass",
        "message": "File read successfully"
    })
    
    # Check for YAML frontmatter (optional but recommended)
    has_frontmatter = content.startswith('---')
    checks.append({
        "check": "YAML frontmatter",
        "status": "pass" if has_frontmatter else "warn",
        "message": "Frontmatter present" if has_frontmatter else "No frontmatter (optional)"
    })
    
    # Extract sections
    sections = extract_sections(content)
    
    # Required sections per 05b spec
    required_sections = [
        "Project Name",
        "Project Goals",
        "Deliverables",
        "Technical Stack",
        "Quality Requirements",
        "Timeline Constraints",
        "Team Structure"
    ]
    
    # Also check for common variations
    section_variations = {
        "Project Name": ["Project Name", "Name", "Project Title", "Executive Summary"],
        "Project Goals": ["Project Goals", "Goals", "Objectives", "Business Objectives"],
        "Deliverables": ["Deliverables", "Deliverable", "Outputs"],
        "Technical Stack": ["Technical Stack", "Tech Stack", "Technology Stack", "Technical Architecture"],
        "Quality Requirements": ["Quality Requirements", "Quality", "Quality Standards"],
        "Timeline Constraints": ["Timeline Constraints", "Timeline", "Schedule", "Time Constraints"],
        "Team Structure": ["Team Structure", "Team", "Team Composition"]
    }
    
    all_sections_found = True
    found_sections = []
    missing_sections = []
    
    for required in required_sections:
        found = False
        # Check exact match
        for section_name in sections.keys():
            if required.lower() in section_name.lower():
                found = True
                found_sections.append(section_name)
                break
        
        # Check variations
        if not found and required in section_variations:
            for variation in section_variations[required]:
                for section_name in sections.keys():
                    if variation.lower() in section_name.lower():
                        found = True
                        found_sections.append(section_name)
                        break
                if found:
                    break
        
        if not found:
            all_sections_found = False
            missing_sections.append(required)
    
    checks.append({
        "check": "Required sections present",
        "status": "pass" if all_sections_found else "fail",
        "found": found_sections,
        "missing": missing_sections,
        "total_sections": len(sections)
    })
    
    if not all_sections_found:
        all_passed = False
    
    # Check section content quality (non-empty)
    empty_sections = []
    for section_name, section_content in sections.items():
        if len(section_content.strip()) < 10:  # Very short content
            empty_sections.append(section_name)
    
    if empty_sections:
        checks.append({
            "check": "Section content quality",
            "status": "warn",
            "message": f"Sections with minimal content: {', '.join(empty_sections)}"
        })
    
    return {
        "status": "pass" if all_passed else "fail",
        "checks": checks,
        "checks_passed": sum(1 for c in checks if c.get("status") == "pass"),
        "checks_total": len(checks),
        "sections_found": found_sections,
        "sections_missing": missing_sections,
        "total_sections_detected": len(sections)
    }

def main():
    parser = argparse.ArgumentParser(description='Validate PROJECT-BRIEF.md integrity')
    parser.add_argument('--file', default='PROJECT-BRIEF.md', help='Path to PROJECT-BRIEF.md')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    brief_path = workspace / args.file
    
    print(f"[PROTOCOL 05B | STEP 2.2] Validating PROJECT-BRIEF.md integrity...")
    
    result = validate_project_brief(brief_path)
    result['file_path'] = str(brief_path)
    result['timestamp'] = datetime.now().isoformat()
    
    # Write evidence artifact
    output_dir = workspace / '.artifacts' / 'protocol-05b'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / 'project-brief-validation.json'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    
    print(json.dumps(result, indent=2))
    
    if result['status'] == 'pass':
        print("[PROTOCOL 05B | STEP 2.2 COMPLETE] PROJECT-BRIEF.md validated")
        return 0
    else:
        print("[PROTOCOL 05B | STEP 2.2 FAILED] PROJECT-BRIEF.md validation failed")
        print("[ERROR] Missing sections - return to Protocol 03")
        return 1

if __name__ == "__main__":
    sys.exit(main())
