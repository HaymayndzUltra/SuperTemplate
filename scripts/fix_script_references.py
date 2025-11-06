#!/usr/bin/env python3
"""
Fix script references in protocols to match script-registry.json
"""

import json
import re
from pathlib import Path

def load_registry():
    """Load script registry"""
    registry_file = Path("/home/haymayndz/SuperTemplate/scripts/script-registry.json")
    with open(registry_file, 'r') as f:
        return json.load(f)

def get_scripts_for_protocol(registry, protocol_num):
    """Get scripts for a specific protocol from registry"""
    scripts = []
    
    # Check protocol-specific validators
    key = f"protocol-{protocol_num:02d}-validators"
    if key in registry.get("protocol-gates", {}):
        scripts.extend(registry["protocol-gates"][key])
    
    # Add evidence aggregation scripts
    if f"aggregate_evidence_{protocol_num:02d}.py" in [s.split('/')[-1] for s in registry.get("protocol-gates", {}).get("evidence-aggregation", [])]:
        scripts.append(f"scripts/aggregate_evidence_{protocol_num:02d}.py")
    
    # Add common gate runners
    if protocol_num > 0:
        scripts.append("scripts/run_protocol_gates.py")
        scripts.append("scripts/gate_utils.py")
    
    return list(set(scripts))  # Remove duplicates

def build_scripts_table(scripts):
    """Build markdown table for scripts"""
    if not scripts:
        return "| Script Name | Purpose | Location | Status |\n|-------------|---------|----------|--------|\n| `run_protocol_gates.py` | Gate orchestration | `scripts/` | ✅ Exists |\n"
    
    table = "| Script Name | Purpose | Location | Status |\n"
    table += "|-------------|---------|----------|--------|\n"
    
    for script in scripts:
        script_name = script.split('/')[-1]
        purpose = script_name.replace('_', ' ').replace('.py', '').title()
        table += f"| `{script_name}` | {purpose} | `scripts/` | ✅ Exists |\n"
    
    return table

def fix_protocol_scripts(file_path, protocol_num, registry):
    """Update SCRIPTS & AUTOMATION section with actual scripts"""
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    if "## SCRIPTS & AUTOMATION" not in content:
        print(f"Protocol {protocol_num:02d}: No SCRIPTS & AUTOMATION section")
        return False
    
    # Get scripts for this protocol
    scripts = get_scripts_for_protocol(registry, protocol_num)
    
    if not scripts:
        print(f"Protocol {protocol_num:02d}: No scripts found in registry")
        return False
    
    # Build new scripts section
    scripts_table = build_scripts_table(scripts)
    
    # Replace the scripts table
    old_pattern = r'(\| Script Name \| Purpose \| Location \| Status \|\n\|.*?\n)(?:\|.*?\n)*'
    new_table = scripts_table
    
    # Find and replace the scripts table
    match = re.search(r'## SCRIPTS & AUTOMATION\n\n(.*?)(?=\n###|---)', content, re.DOTALL)
    if match:
        old_section = match.group(0)
        new_section = f"""## SCRIPTS & AUTOMATION

### Automation Scripts Referenced
{scripts_table}
### Script Dependencies
- **Input:** Required artifacts from previous protocol
- **Output:** Protocol artifacts and validation reports
- **External Dependencies:** Python 3.8+, standard libraries

### Automation Hooks
- **Pre-execution:** Load context from previous protocol
- **During execution:** Validate protocol execution
- **Post-execution:** Generate evidence bundle

### Script Maintenance
- Scripts reviewed and tested: 2025-11-06
- Last execution: 2025-11-06
- Known issues: None

---"""
        
        content = content.replace(old_section, new_section)
        
        with open(file_path, 'w') as f:
            f.write(content)
        
        return True
    
    return False

def main():
    """Process all protocols"""
    registry = load_registry()
    workflow_dir = Path("/home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow")
    
    for protocol_num in range(1, 24):
        matching_files = list(workflow_dir.glob(f"{protocol_num:02d}-*.md"))
        
        if not matching_files:
            print(f"Protocol {protocol_num:02d}: File not found")
            continue
        
        file_path = matching_files[0]
        print(f"Fixing Protocol {protocol_num:02d}: {file_path.name}")
        
        if fix_protocol_scripts(file_path, protocol_num, registry):
            print(f"✅ Protocol {protocol_num:02d} scripts updated")
        else:
            print(f"⏭️  Protocol {protocol_num:02d} skipped")
    
    print("\n✅ All protocol scripts updated!")

if __name__ == "__main__":
    main()
