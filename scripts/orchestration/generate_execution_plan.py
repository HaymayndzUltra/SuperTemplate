#!/usr/bin/env python3
"""
Generate Execution Plan
Generates the final PROTOCOL-EXECUTION-PLAN.md document.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def generate_plan_markdown(
    classification_data: dict,
    sequence_data: dict,
    timeline_data: dict,
    customization_data: dict,
    brief_data: dict
) -> str:
    """Generate the execution plan markdown document."""
    
    project_name = brief_data.get('project_name', 'Project')
    classification = classification_data.get('classification_display', 'Unknown')
    confidence = classification_data.get('confidence_score', 0)
    
    timeline = timeline_data.get('timeline', {})
    totals = timeline.get('totals', {})
    
    md = f"""# Protocol Execution Plan

## Project Overview

**Project Name:** {project_name}
**Classification:** {classification}
**Classification Confidence:** {confidence}%
**Generated:** {datetime.now().isoformat()}

---

## Executive Summary

This execution plan outlines the protocol sequence for delivering the {project_name} project. Based on the project classification as a **{classification}**, the following protocols have been selected and sequenced for optimal delivery.

### Timeline Summary

| Metric | Minimum | Typical | Maximum |
|--------|---------|---------|---------|
| Hours | {totals.get('hours', {}).get('min', 'N/A')} | {totals.get('hours', {}).get('typical', 'N/A')} | {totals.get('hours', {}).get('max', 'N/A')} |
| Days | {totals.get('days', {}).get('min', 'N/A')} | {totals.get('days', {}).get('typical', 'N/A')} | {totals.get('days', {}).get('max', 'N/A')} |
| Weeks | {totals.get('weeks', {}).get('min', 'N/A')} | {totals.get('weeks', {}).get('typical', 'N/A')} | {totals.get('weeks', {}).get('max', 'N/A')} |

---

## Protocol Sequence

"""
    
    # Add sequence details
    sequence = sequence_data.get('sequence', [])
    phases = sequence_data.get('phases', [])
    customizations = {c['protocol_id']: c for c in customization_data.get('customizations', [])}
    protocol_estimates = {p['protocol_id']: p for p in timeline.get('protocol_estimates', [])}
    
    for phase in phases:
        phase_num = phase.get('phase_number', 0)
        md += f"### Phase {phase_num}\n\n"
        
        for protocol in phase.get('protocols', []):
            protocol_id = protocol.get('id')
            protocol_name = protocol.get('name')
            track = protocol.get('track', 'generic')
            
            estimate = protocol_estimates.get(protocol_id, {}).get('estimate', {})
            custom = customizations.get(protocol_id, {})
            
            md += f"#### Protocol {protocol_id}: {protocol_name}\n\n"
            md += f"- **Track:** {track.upper()}\n"
            md += f"- **Estimated Time:** {estimate.get('typical_hours', 'N/A')} hours (range: {estimate.get('min_hours', 'N/A')}-{estimate.get('max_hours', 'N/A')})\n"
            
            # Add dependencies
            deps = protocol.get('dependencies', [])
            if deps:
                md += f"- **Dependencies:** {', '.join(deps)}\n"
            
            # Add customizations
            if custom.get('customizations'):
                md += f"\n**Customizations:**\n"
                for c in custom.get('customizations', []):
                    md += f"- {c.get('type', 'General')}: {c.get('detail', 'N/A')}\n"
            
            if custom.get('tech_stack_adaptations'):
                md += f"\n**Tech Stack Adaptations:**\n"
                for a in custom.get('tech_stack_adaptations', []):
                    md += f"- {a.get('component', 'Component')}: {a.get('adaptation', 'N/A')}\n"
            
            md += "\n"
        
        md += "---\n\n"
    
    # Add tech stack section
    tech_stack = brief_data.get('tech_stack', {})
    md += """## Technical Stack

"""
    
    for component, technologies in tech_stack.items():
        if technologies:
            md += f"### {component.replace('_', ' ').title()}\n"
            if isinstance(technologies, list):
                for tech in technologies:
                    md += f"- {tech}\n"
            else:
                md += f"- {technologies}\n"
            md += "\n"
    
    # Add quality requirements
    quality = brief_data.get('quality_requirements', {})
    if quality:
        md += """## Quality Requirements

"""
        for req, value in quality.items():
            if value:
                md += f"- **{req.replace('_', ' ').title()}:** Required\n"
        md += "\n"
    
    # Add assumptions and notes
    md += """## Assumptions and Notes

1. Timeline estimates assume dedicated resources working full-time on the project.
2. Estimates include buffer for reviews and iterations.
3. Actual timeline may vary based on project complexity and team capacity.
4. Protocol customizations have been factored into time estimates.

---

## Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Project Lead | | | |
| Technical Lead | | | |
| Stakeholder | | | |

---

*This execution plan was generated by Protocol 05b - Project Protocol Orchestration*
"""
    
    return md

def main():
    parser = argparse.ArgumentParser(description='Generate protocol execution plan')
    parser.add_argument('--classification', required=True, help='Path to project-classification.json')
    parser.add_argument('--sequence', required=True, help='Path to protocol-sequence.json')
    parser.add_argument('--timeline', required=True, help='Path to timeline-estimate.json')
    parser.add_argument('--customizations', required=True, help='Path to customization-analysis.json')
    parser.add_argument('--brief', required=True, help='Path to project-brief-parsed.json')
    parser.add_argument('--output', help='Output markdown file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 6] Generating execution plan...")
    
    # Load all input files
    def load_json(path_arg):
        path = Path(path_arg)
        if not path.is_absolute():
            path = workspace / path
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    classification_data = load_json(args.classification)
    sequence_data = load_json(args.sequence)
    timeline_data = load_json(args.timeline)
    customization_data = load_json(args.customizations)
    brief_data = load_json(args.brief)
    
    # Generate plan
    plan_md = generate_plan_markdown(
        classification_data,
        sequence_data,
        timeline_data,
        customization_data,
        brief_data
    )
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / 'PROTOCOL-EXECUTION-PLAN.md'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(plan_md)
    
    # Also save to artifacts
    artifacts_path = workspace / '.artifacts' / 'protocol-05b' / 'PROTOCOL-EXECUTION-PLAN.md'
    artifacts_path.parent.mkdir(parents=True, exist_ok=True)
    with open(artifacts_path, 'w', encoding='utf-8') as f:
        f.write(plan_md)
    
    print(f"[PROTOCOL 05B | PHASE 6] Execution plan generated")
    print(f"  - Output: {output_path}")
    print(f"  - Artifact: {artifacts_path}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
