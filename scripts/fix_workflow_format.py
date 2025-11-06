#!/usr/bin/env python3
"""
Reformat workflow sections to match validator expectations
Convert from "### Workflow Phases" to "### STEP X" format
"""

import re
from pathlib import Path

def fix_workflow_section(content, protocol_num):
    """Convert workflow section to STEP format"""
    
    # Find the Workflow Orchestration section
    workflow_pattern = r'## WORKFLOW ORCHESTRATION\n\n(.*?)(?=\n---|\n## )'
    match = re.search(workflow_pattern, content, re.DOTALL)
    
    if not match:
        print(f"Protocol {protocol_num:02d}: No WORKFLOW ORCHESTRATION section found")
        return content
    
    workflow_content = match.group(1)
    
    # Extract phases from the current format
    phases = re.findall(r'(\d+)\.\s+\*\*Phase \d+:\s+([^*]+)\*\*\s+-\s+([^\n]+)\n(.*?)(?=\n\d+\.|$)', 
                       workflow_content, re.DOTALL)
    
    if not phases:
        print(f"Protocol {protocol_num:02d}: No phases found in workflow section")
        return content
    
    # Build new STEP format
    new_workflow = "## WORKFLOW ORCHESTRATION\n\n"
    
    for step_num, (_, phase_name, description, phase_details) in enumerate(phases, 1):
        new_workflow += f"### STEP {step_num}\n\n"
        new_workflow += f"**Action:** Execute {phase_name.strip().lower()} activities\n\n"
        new_workflow += f"**Description:** {description.strip()}\n\n"
        
        # Extract input/output/duration from phase details
        input_match = re.search(r'- Input:\s+([^\n]+)', phase_details)
        output_match = re.search(r'- Output:\s+([^\n]+)', phase_details)
        duration_match = re.search(r'- Duration:\s+([^\n]+)', phase_details)
        
        if input_match:
            new_workflow += f"**Input:** {input_match.group(1).strip()}\n\n"
        if output_match:
            new_workflow += f"**Output:** {output_match.group(1).strip()}\n\n"
        
        new_workflow += f"Communication: Document progress and blockers\n\n"
        new_workflow += f"Evidence: Track artifacts and validation results in `.artifacts/protocol-{protocol_num:02d}/workflow-logs/`\n\n"
        
        if duration_match:
            new_workflow += f"**Duration:** {duration_match.group(1).strip()}\n\n"
        
        new_workflow += "---\n\n"
    
    # Add workflow dependencies section
    new_workflow += "### Workflow Dependencies\n\n"
    new_workflow += f"- **Sequential:** STEP 1 → STEP 2 → STEP {len(phases)} (must complete in order)\n"
    new_workflow += "- **Parallel:** None (all steps sequential)\n"
    new_workflow += "- **Conditional:** Halt if validation fails, escalate to supervisor\n\n"
    
    # Add state management section
    new_workflow += "### Workflow State Management\n\n"
    new_workflow += f"- State stored in: `.artifacts/protocol-{protocol_num:02d}/workflow-state.json`\n"
    new_workflow += "- Checkpoint validation at each step boundary\n"
    new_workflow += "- Rollback procedure if step fails: Return to previous step and remediate\n\n"
    
    # Add monitoring section
    new_workflow += "### Workflow Monitoring\n\n"
    new_workflow += f"- Real-time status: `.artifacts/protocol-{protocol_num:02d}/workflow-status.json`\n"
    new_workflow += f"- Execution logs: `.artifacts/protocol-{protocol_num:02d}/workflow-logs/`\n"
    new_workflow += f"- Performance metrics: `.artifacts/protocol-{protocol_num:02d}/workflow-metrics.json`\n\n"
    
    # Replace the old workflow section with new one
    old_section = match.group(0)
    content = content.replace(old_section, new_workflow)
    
    return content

def main():
    """Process all protocols"""
    workflow_dir = Path("/home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow")
    
    for protocol_num in range(1, 24):
        matching_files = list(workflow_dir.glob(f"{protocol_num:02d}-*.md"))
        
        if not matching_files:
            print(f"Protocol {protocol_num:02d}: File not found")
            continue
        
        file_path = matching_files[0]
        print(f"Fixing Protocol {protocol_num:02d}: {file_path.name}")
        
        with open(file_path, 'r') as f:
            content = f.read()
        
        modified_content = fix_workflow_section(content, protocol_num)
        
        if modified_content != content:
            with open(file_path, 'w') as f:
                f.write(modified_content)
            print(f"✅ Protocol {protocol_num:02d} workflow format fixed")
        else:
            print(f"⏭️  Protocol {protocol_num:02d} no changes needed")
    
    print("\n✅ All workflow sections reformatted!")

if __name__ == "__main__":
    main()
