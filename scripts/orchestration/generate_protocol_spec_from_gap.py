#!/usr/bin/env python3
"""
Generate Protocol Specification from Gap
Generates a complete protocol markdown document from a gap specification.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def generate_identity_section(gap_spec: dict) -> str:
    """Generate the IDENTITY section."""
    return f"""## IDENTITY

**Protocol ID:** {gap_spec['gap_id']}
**Protocol Name:** {gap_spec['gap_name']}
**Version:** 1.0.0
**Track:** {gap_spec.get('track', 'generic').upper()}
**Complexity:** {gap_spec.get('complexity', 'medium').title()}

### Purpose
{gap_spec['gap_description']}

### Scope
This protocol covers the complete workflow for {gap_spec['gap_name'].lower()}.
"""

def generate_ai_role_section(gap_spec: dict) -> str:
    """Generate the AI_ROLE section."""
    name = gap_spec['gap_name']
    return f"""## AI ROLE AND MISSION

### Role Definition
You are an **AI {name} Specialist**. Your mission is to execute the {name.lower()} workflow with precision, ensuring all quality gates pass and evidence is properly documented.

### Responsibilities
- Execute workflow steps in sequence
- Validate inputs and outputs at each step
- Generate required evidence artifacts
- Communicate progress and blockers
- Ensure quality gate compliance

### Constraints
- Follow the defined workflow sequence
- Do not skip validation steps
- Document all decisions with reasoning
- Escalate blockers immediately
"""

def generate_prerequisites_section(gap_spec: dict) -> str:
    """Generate the PREREQUISITES section."""
    integration = gap_spec.get('integration_points', {})
    input_from = integration.get('input_from', [])
    
    prereqs = "## PREREQUISITES\n\n### Required Artifacts\n"
    prereqs += "**[STRICT]** All artifacts must be present before execution:\n\n"
    
    if input_from:
        for source in input_from:
            prereqs += f"- Artifacts from {source}\n"
    else:
        prereqs += "- PROJECT-BRIEF.md from Protocol 03\n"
        prereqs += "- Relevant upstream protocol outputs\n"
    
    prereqs += "\n### Required Approvals\n"
    prereqs += "- Technical Lead authorization\n"
    prereqs += "- Relevant stakeholder sign-off\n"
    
    prereqs += "\n### System State Requirements\n"
    prereqs += "- Access to required systems and credentials\n"
    prereqs += "- Environment properly configured\n"
    
    return prereqs

def generate_workflow_section(gap_spec: dict) -> str:
    """Generate the WORKFLOW section."""
    steps = gap_spec.get('workflow_steps', [])
    
    workflow = "## WORKFLOW\n\n"
    
    for i, step in enumerate(steps):
        step_num = step.get('step_id', i + 1)
        workflow += f"### STEP {step_num}: {step['name']}\n\n"
        
        if step.get('description'):
            workflow += f"**Description:** {step['description']}\n\n"
        
        workflow += "**Action:** **[MUST]** Execute this step:\n\n"
        
        # Inputs
        inputs = step.get('inputs', [])
        if inputs:
            workflow += "**Inputs:**\n"
            for inp in inputs:
                workflow += f"- `{inp}`\n"
            workflow += "\n"
        
        # Outputs
        outputs = step.get('outputs', [])
        if outputs:
            workflow += "**Outputs:**\n"
            for out in outputs:
                workflow += f"- `{out}`\n"
            workflow += "\n"
        
        # Validation
        if step.get('validation'):
            workflow += f"**Validation:** {step['validation']}\n\n"
        
        workflow += "---\n\n"
    
    return workflow

def generate_quality_gates_section(gap_spec: dict) -> str:
    """Generate the QUALITY_GATES section."""
    gates = gap_spec.get('quality_gates', [])
    
    section = "## QUALITY GATES\n\n"
    
    for gate in gates:
        gate_id = gate.get('gate_id', 0)
        section += f"### Gate {gate_id}: {gate['name']}\n\n"
        
        if gate.get('description'):
            section += f"**Description:** {gate['description']}\n\n"
        
        threshold = gate.get('threshold', 0.95)
        section += f"**Threshold:** {threshold * 100}%\n\n"
        
        criteria = gate.get('criteria', [])
        if criteria:
            section += "**Criteria:**\n"
            for criterion in criteria:
                section += f"- [ ] {criterion}\n"
            section += "\n"
        
        section += "**Failure Handling:**\n"
        section += "- If gate fails, halt execution and report blockers\n"
        section += "- Document failure reason in evidence\n"
        section += "- Escalate to technical lead if unresolved\n\n"
        section += "---\n\n"
    
    return section

def generate_automation_hooks_section(gap_spec: dict) -> str:
    """Generate the AUTOMATION_HOOKS section."""
    hooks = gap_spec.get('automation_hooks', [])
    
    section = "## AUTOMATION HOOKS\n\n"
    
    if hooks:
        section += "| Hook ID | Name | Script | Trigger |\n"
        section += "|---------|------|--------|--------|\n"
        
        for hook in hooks:
            section += f"| {hook.get('hook_id', 'N/A')} | {hook.get('name', 'N/A')} | `{hook.get('script', 'N/A')}` | {hook.get('trigger', 'N/A')} |\n"
        
        section += "\n"
    else:
        section += "*No automation hooks defined for this protocol.*\n\n"
    
    return section

def generate_evidence_section(gap_spec: dict) -> str:
    """Generate the EVIDENCE_SUMMARY section."""
    steps = gap_spec.get('workflow_steps', [])
    
    section = "## EVIDENCE SUMMARY\n\n"
    section += "### Required Artifacts\n\n"
    section += "| Artifact | Source Step | Format | Required |\n"
    section += "|----------|-------------|--------|----------|\n"
    
    for step in steps:
        outputs = step.get('outputs', [])
        for output in outputs:
            ext = Path(output).suffix.lstrip('.') or 'unknown'
            section += f"| `{output}` | Step {step.get('step_id', '?')} | {ext.upper()} | Yes |\n"
    
    section += "\n### Evidence Directory\n"
    section += f"`.artifacts/protocol-{gap_spec['gap_id']}/`\n\n"
    
    return section

def generate_integration_section(gap_spec: dict) -> str:
    """Generate the INTEGRATION_POINTS section."""
    integration = gap_spec.get('integration_points', {})
    
    section = "## INTEGRATION POINTS\n\n"
    
    section += "### Input From\n"
    input_from = integration.get('input_from', [])
    if input_from:
        for source in input_from:
            section += f"- {source}\n"
    else:
        section += "- *No specific input dependencies*\n"
    
    section += "\n### Output To\n"
    output_to = integration.get('output_to', [])
    if output_to:
        for dest in output_to:
            section += f"- {dest}\n"
    else:
        section += "- *No specific output dependencies*\n"
    
    section += "\n"
    return section

def generate_communication_section(gap_spec: dict) -> str:
    """Generate the COMMUNICATION section."""
    return """## COMMUNICATION PROTOCOL

### Status Updates
- Report progress at each step completion
- Flag blockers immediately
- Provide estimated completion time

### Format
```
[PROTOCOL {id}] Step {n} of {total}: {step_name}
Status: {IN_PROGRESS | COMPLETE | BLOCKED}
Progress: {percentage}%
```

### Escalation
- Blockers: Escalate within 30 minutes
- Questions: Flag for clarification before proceeding
- Decisions: Document reasoning in evidence
""".replace("{id}", gap_spec['gap_id'])

def generate_handoff_section(gap_spec: dict) -> str:
    """Generate the HANDOFF section."""
    return f"""## HANDOFF CHECKLIST

### Pre-Handoff Verification
- [ ] All workflow steps completed
- [ ] All quality gates passed
- [ ] All evidence artifacts generated
- [ ] Evidence manifest created
- [ ] Checksums verified

### Handoff Package
- [ ] Evidence package assembled
- [ ] Manifest includes all artifacts
- [ ] No placeholder values remaining
- [ ] Ready for downstream protocol

### Sign-Off
- [ ] Technical review complete
- [ ] Stakeholder approval obtained
"""

def generate_protocol_markdown(gap_spec: dict) -> str:
    """Generate complete protocol markdown document."""
    
    header = f"""# PROTOCOL {gap_spec['gap_id']}: {gap_spec['gap_name'].upper()}

**Version:** 1.0.0
**Generated:** {datetime.now().isoformat()}
**Track:** {gap_spec.get('track', 'generic').upper()}

---

"""
    
    sections = [
        header,
        generate_identity_section(gap_spec),
        generate_ai_role_section(gap_spec),
        generate_prerequisites_section(gap_spec),
        generate_workflow_section(gap_spec),
        generate_quality_gates_section(gap_spec),
        generate_automation_hooks_section(gap_spec),
        generate_evidence_section(gap_spec),
        generate_integration_section(gap_spec),
        generate_communication_section(gap_spec),
        generate_handoff_section(gap_spec)
    ]
    
    # Add REASONING section if requested
    if 'REASONING' in gap_spec.get('required_sections', []):
        sections.append("""## REASONING

### Decision Documentation
Document all significant decisions made during protocol execution:

| Decision | Options Considered | Selected | Rationale |
|----------|-------------------|----------|-----------|
| | | | |

### Risk Assessment
Document identified risks and mitigations:

| Risk | Severity | Mitigation | Status |
|------|----------|------------|--------|
| | | | |
""")
    
    # Add REFLECTION section if requested
    if 'REFLECTION' in gap_spec.get('required_sections', []):
        sections.append("""## REFLECTION

### Lessons Learned
- What went well:
- What could be improved:
- Recommendations for future executions:

### Metrics
- Total execution time:
- Quality score:
- Blockers encountered:
""")
    
    sections.append(f"""
---

*This protocol was generated by Protocol 0 - Gap Fill Generator*
*Generated: {datetime.now().isoformat()}*
""")
    
    return '\n'.join(sections)

def main():
    parser = argparse.ArgumentParser(description='Generate protocol specification from gap')
    parser.add_argument('--input', required=True, help='Path to gap-specification.json')
    parser.add_argument('--output', help='Output markdown file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 0] Generating protocol from gap specification...")
    
    # Load gap specification
    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = workspace / input_path
    
    with open(input_path, 'r', encoding='utf-8') as f:
        gap_spec = json.load(f)
    
    # Generate protocol markdown
    protocol_md = generate_protocol_markdown(gap_spec)
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        protocol_id = gap_spec['gap_id']
        protocol_name = gap_spec['gap_name'].lower().replace(' ', '-')
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'new-protocols' / f'{protocol_id}-{protocol_name}.md'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(protocol_md)
    
    print(f"[PROTOCOL 0] Protocol generated successfully")
    print(f"  - Protocol ID: {gap_spec['gap_id']}")
    print(f"  - Protocol Name: {gap_spec['gap_name']}")
    print(f"  - Output: {output_path}")
    
    # Write generation log
    log_path = output_path.parent / 'creation-log.json'
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "gap_specification": str(input_path),
        "generated_protocol": str(output_path),
        "protocol_id": gap_spec['gap_id'],
        "protocol_name": gap_spec['gap_name'],
        "sections_generated": len(gap_spec.get('required_sections', [])),
        "workflow_steps": len(gap_spec.get('workflow_steps', [])),
        "quality_gates": len(gap_spec.get('quality_gates', [])),
        "status": "success"
    }
    
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, indent=2)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
