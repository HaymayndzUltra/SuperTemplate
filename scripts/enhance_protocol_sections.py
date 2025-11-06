#!/usr/bin/env python3
"""
Enhance protocol sections with specific content based on protocol context
"""

import os
import re
from pathlib import Path

# Protocol-specific metadata
PROTOCOL_METADATA = {
    1: {
        "owner": "Proposal Writer/Freelancer",
        "category": "Execution",
        "criticality": "High",
        "complexity": "Medium",
        "purpose": "Transform raw job posts into human-voice freelance proposals with evidence tracking",
        "scripts": ["analyze_jobpost", "tone_mapper", "validate_proposal", "aggregate_evidence_01"],
        "phases": ["Environment Setup", "Job Post Extraction", "Tone Calibration", "Pricing Analysis", "Proposal Drafting", "Validation"],
        "stakeholders": ["Freelancer", "Client", "Discovery Lead"]
    },
    2: {
        "owner": "Discovery Call Lead",
        "category": "Execution", 
        "criticality": "High",
        "complexity": "Medium",
        "purpose": "Conduct discovery call with comprehensive pre-call preparation and post-call documentation",
        "scripts": ["validate_gate_02_precall", "validate_gate_02_postcall", "generate_discovery_summary"],
        "phases": ["Context Consolidation", "Discovery Call", "Post-Call Processing"],
        "stakeholders": ["Discovery Lead", "Client", "Project Manager"]
    },
    3: {
        "owner": "Brief Creator",
        "category": "Documentation",
        "criticality": "High", 
        "complexity": "High",
        "purpose": "Create comprehensive project brief from discovery insights",
        "scripts": ["validate_gate_03_brief", "generate_brief", "aggregate_evidence_03"],
        "phases": ["Discovery Analysis", "Brief Drafting", "Stakeholder Review", "Finalization"],
        "stakeholders": ["Brief Creator", "Technical Lead", "Client"]
    },
    4: {
        "owner": "Technical Lead",
        "category": "Execution",
        "criticality": "High",
        "complexity": "High", 
        "purpose": "Bootstrap project with proper context engineering and setup",
        "scripts": ["bootstrap_project", "setup_context", "validate_bootstrap"],
        "phases": ["Context Setup", "Project Initialization", "Environment Configuration"],
        "stakeholders": ["Technical Lead", "Development Team", "DevOps"]
    },
    5: {
        "owner": "Technical Lead",
        "category": "Execution",
        "criticality": "High",
        "complexity": "Medium",
        "purpose": "Complete project bootstrap with all necessary configurations",
        "scripts": ["complete_bootstrap", "validate_setup", "generate_bootstrap_report"],
        "phases": ["Dependency Installation", "Configuration", "Validation"],
        "stakeholders": ["Technical Lead", "Development Team", "QA Lead"]
    },
    6: {
        "owner": "Product Manager",
        "category": "Documentation",
        "criticality": "High",
        "complexity": "High",
        "purpose": "Create detailed Product Requirements Document",
        "scripts": ["generate_prd", "validate_requirements", "aggregate_prd_evidence"],
        "phases": ["Requirements Gathering", "PRD Drafting", "Review Cycles", "Approval"],
        "stakeholders": ["Product Manager", "Technical Lead", "Client", "QA Lead"]
    },
    7: {
        "owner": "System Architect",
        "category": "Design",
        "criticality": "Critical",
        "complexity": "High",
        "purpose": "Design technical architecture and system components",
        "scripts": ["generate_architecture", "validate_design", "create_diagrams"],
        "phases": ["Requirements Analysis", "Architecture Design", "Component Design", "Review"],
        "stakeholders": ["System Architect", "Technical Lead", "Development Team", "Security Lead"]
    },
    8: {
        "owner": "Technical Lead",
        "category": "Planning",
        "criticality": "High",
        "complexity": "Medium",
        "purpose": "Generate and organize development tasks from requirements",
        "scripts": ["generate_tasks", "prioritize_tasks", "assign_tasks"],
        "phases": ["Task Generation", "Prioritization", "Assignment", "Timeline Planning"],
        "stakeholders": ["Technical Lead", "Development Team", "Project Manager"]
    },
    9: {
        "owner": "DevOps Engineer",
        "category": "Infrastructure",
        "criticality": "High",
        "complexity": "Medium",
        "purpose": "Setup and validate development environment",
        "scripts": ["setup_environment", "validate_environment", "run_smoke_tests"],
        "phases": ["Environment Setup", "Configuration", "Validation", "Documentation"],
        "stakeholders": ["DevOps Engineer", "Development Team", "QA Team"]
    },
    10: {
        "owner": "Development Team Lead",
        "category": "Execution",
        "criticality": "High",
        "complexity": "High",
        "purpose": "Process and complete development tasks",
        "scripts": ["process_task", "validate_completion", "update_progress"],
        "phases": ["Task Execution", "Code Review", "Testing", "Integration"],
        "stakeholders": ["Development Team", "Technical Lead", "QA Team"]
    },
    11: {
        "owner": "QA Lead",
        "category": "Testing",
        "criticality": "Critical",
        "complexity": "High",
        "purpose": "Execute comprehensive integration testing",
        "scripts": ["run_integration_tests", "generate_test_report", "track_defects"],
        "phases": ["Test Planning", "Test Execution", "Defect Management", "Reporting"],
        "stakeholders": ["QA Lead", "QA Team", "Development Team", "Product Manager"]
    },
    12: {
        "owner": "QA Manager",
        "category": "Quality",
        "criticality": "High",
        "complexity": "Medium",
        "purpose": "Conduct comprehensive quality audit",
        "scripts": ["run_quality_audit", "generate_audit_report", "track_issues"],
        "phases": ["Audit Planning", "Audit Execution", "Issue Documentation", "Remediation"],
        "stakeholders": ["QA Manager", "Technical Lead", "Product Manager", "Client"]
    },
    13: {
        "owner": "UAT Coordinator",
        "category": "Testing",
        "criticality": "High",
        "complexity": "Medium",
        "purpose": "Coordinate User Acceptance Testing with stakeholders",
        "scripts": ["setup_uat_environment", "track_uat_feedback", "generate_uat_report"],
        "phases": ["UAT Planning", "Environment Setup", "Testing Coordination", "Sign-off"],
        "stakeholders": ["UAT Coordinator", "Client", "Product Manager", "QA Lead"]
    },
    14: {
        "owner": "Release Manager",
        "category": "Deployment",
        "criticality": "Critical",
        "complexity": "High",
        "purpose": "Prepare and validate staging deployment",
        "scripts": ["deploy_to_staging", "run_staging_tests", "validate_staging"],
        "phases": ["Staging Preparation", "Deployment", "Validation", "Performance Testing"],
        "stakeholders": ["Release Manager", "DevOps Team", "QA Team", "Technical Lead"]
    },
    15: {
        "owner": "Release Manager",
        "category": "Deployment",
        "criticality": "Critical",
        "complexity": "High",
        "purpose": "Execute production deployment with rollback capability",
        "scripts": ["deploy_to_production", "validate_production", "monitor_deployment"],
        "phases": ["Pre-deployment Checks", "Deployment Execution", "Validation", "Monitoring"],
        "stakeholders": ["Release Manager", "DevOps Team", "Technical Lead", "Client"]
    },
    16: {
        "owner": "DevOps Lead",
        "category": "Operations",
        "criticality": "High",
        "complexity": "Medium",
        "purpose": "Setup monitoring and observability infrastructure",
        "scripts": ["setup_monitoring", "configure_alerts", "validate_observability"],
        "phases": ["Monitoring Setup", "Alert Configuration", "Dashboard Creation", "Testing"],
        "stakeholders": ["DevOps Lead", "Operations Team", "Technical Lead", "Support Team"]
    },
    17: {
        "owner": "Incident Commander",
        "category": "Operations",
        "criticality": "Critical",
        "complexity": "High",
        "purpose": "Manage incident response and rollback procedures",
        "scripts": ["detect_incident", "execute_rollback", "generate_incident_report"],
        "phases": ["Incident Detection", "Impact Assessment", "Response Execution", "Post-mortem"],
        "stakeholders": ["Incident Commander", "DevOps Team", "Technical Lead", "Client"]
    },
    18: {
        "owner": "Performance Engineer",
        "category": "Optimization",
        "criticality": "Medium",
        "complexity": "High",
        "purpose": "Optimize system performance and resource utilization",
        "scripts": ["run_performance_tests", "analyze_metrics", "apply_optimizations"],
        "phases": ["Performance Analysis", "Bottleneck Identification", "Optimization", "Validation"],
        "stakeholders": ["Performance Engineer", "Technical Lead", "DevOps Team", "Product Manager"]
    },
    19: {
        "owner": "Documentation Lead",
        "category": "Documentation",
        "criticality": "Medium",
        "complexity": "Medium",
        "purpose": "Create comprehensive documentation and knowledge transfer materials",
        "scripts": ["generate_documentation", "validate_docs", "publish_documentation"],
        "phases": ["Documentation Planning", "Content Creation", "Review", "Publishing"],
        "stakeholders": ["Documentation Lead", "Technical Team", "Support Team", "Client"]
    },
    20: {
        "owner": "Project Manager",
        "category": "Closure",
        "criticality": "High",
        "complexity": "Medium",
        "purpose": "Execute project closure activities and handover",
        "scripts": ["generate_closure_report", "archive_artifacts", "final_validation"],
        "phases": ["Closure Planning", "Artifact Collection", "Final Review", "Handover"],
        "stakeholders": ["Project Manager", "Client", "Technical Lead", "Finance"]
    },
    21: {
        "owner": "Support Lead",
        "category": "Support",
        "criticality": "Medium",
        "complexity": "Medium",
        "purpose": "Establish maintenance and support procedures",
        "scripts": ["setup_support_system", "create_runbooks", "train_support_team"],
        "phases": ["Support Setup", "Knowledge Transfer", "Team Training", "Go-live"],
        "stakeholders": ["Support Lead", "Support Team", "Technical Lead", "Client"]
    },
    22: {
        "owner": "Project Manager",
        "category": "Review",
        "criticality": "Medium",
        "complexity": "Low",
        "purpose": "Conduct implementation retrospective and capture lessons learned",
        "scripts": ["collect_feedback", "analyze_metrics", "generate_retrospective"],
        "phases": ["Data Collection", "Analysis", "Retrospective Meeting", "Documentation"],
        "stakeholders": ["Project Manager", "Full Team", "Client", "Leadership"]
    },
    23: {
        "owner": "Governance Lead",
        "category": "Governance",
        "criticality": "High",
        "complexity": "Medium",
        "purpose": "Maintain script governance and registry management",
        "scripts": ["validate_registry", "audit_scripts", "update_governance"],
        "phases": ["Registry Validation", "Script Audit", "Compliance Check", "Updates"],
        "stakeholders": ["Governance Lead", "Technical Lead", "Security Team", "Compliance"]
    }
}

def enhance_protocol_file(file_path, protocol_num):
    """Enhance a protocol file with specific content"""
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    metadata = PROTOCOL_METADATA.get(protocol_num, {})
    if not metadata:
        print(f"No metadata for protocol {protocol_num}")
        return False
    
    # Enhance Identity section
    content = enhance_identity_section(content, protocol_num, metadata)
    
    # Enhance Roles section
    content = enhance_roles_section(content, protocol_num, metadata)
    
    # Enhance Scripts section
    content = enhance_scripts_section(content, protocol_num, metadata)
    
    # Enhance Workflow section
    content = enhance_workflow_section(content, protocol_num, metadata)
    
    # Enhance Handoff section
    content = enhance_handoff_section(content, protocol_num, metadata)
    
    # Enhance Communication section
    content = enhance_communication_section(content, protocol_num, metadata)
    
    # Write back
    with open(file_path, 'w') as f:
        f.write(content)
    
    return True

def enhance_identity_section(content, protocol_num, metadata):
    """Enhance the Identity & Ownership section with specific content"""
    
    # Update owner
    content = re.sub(
        r'\*\*Protocol Owner:\*\* \[Role/Name\]',
        f'**Protocol Owner:** {metadata["owner"]}',
        content
    )
    
    # Update category
    content = re.sub(
        r'\*\*Category:\*\* Execution',
        f'**Category:** {metadata["category"]}',
        content
    )
    
    # Update criticality
    content = re.sub(
        r'\*\*Criticality:\*\* High',
        f'**Criticality:** {metadata["criticality"]}',
        content
    )
    
    # Update complexity
    content = re.sub(
        r'\*\*Complexity:\*\* Medium',
        f'**Complexity:** {metadata["complexity"]}',
        content
    )
    
    # Update purpose
    content = re.sub(
        r'\*\*Purpose:\*\* \[Clear statement of protocol purpose\]',
        f'**Purpose:** {metadata["purpose"]}',
        content
    )
    
    return content

def enhance_roles_section(content, protocol_num, metadata):
    """Enhance the Roles & Responsibilities section"""
    
    # Update executor role
    content = re.sub(
        r'\*\*Role:\*\* \[Title/Name\]',
        f'**Role:** {metadata["owner"]}',
        content,
        count=1
    )
    
    # Update authority placeholders
    content = re.sub(
        r'\*\*Authority:\*\* \[What decisions can they make\]',
        f'**Authority:** Can make decisions on protocol execution and quality gates',
        content,
        count=1
    )
    
    # Update escalation
    content = re.sub(
        r'\*\*Escalation:\*\* \[Who to escalate to\]',
        f'**Escalation:** Technical Lead or Project Manager',
        content,
        count=1
    )
    
    return content

def enhance_scripts_section(content, protocol_num, metadata):
    """Enhance the Scripts & Automation section"""
    
    if 'scripts' not in metadata:
        return content
    
    # Build script table
    script_table = "| Script Name | Purpose | Location | Status |\n"
    script_table += "|-------------|---------|----------|--------|\n"
    
    for script in metadata['scripts']:
        script_table += f"| `{script}.py` | {script.replace('_', ' ').title()} | `scripts/` | ✅ Exists |\n"
    
    # Replace generic table
    pattern = r'\| Script Name \| Purpose \| Location \| Status \|.*?\n(?:\|.*?\n)*'
    content = re.sub(pattern, script_table, content, flags=re.DOTALL)
    
    return content

def enhance_workflow_section(content, protocol_num, metadata):
    """Enhance the Workflow Orchestration section"""
    
    if 'phases' not in metadata:
        return content
    
    # Build phases content
    phases_content = "### Workflow Phases\n"
    for i, phase in enumerate(metadata['phases'], 1):
        phases_content += f"{i}. **Phase {i}: {phase}** - Execution phase\n"
        phases_content += f"   - Input: Required artifacts from previous phase\n"
        phases_content += f"   - Process: Execute {phase.lower()} activities\n"
        phases_content += f"   - Output: Validated artifacts for next phase\n"
        phases_content += f"   - Duration: Varies based on complexity\n\n"
    
    # Replace generic phases
    pattern = r'### Workflow Phases\n.*?(?=\n### )'
    content = re.sub(pattern, phases_content, content, flags=re.DOTALL)
    
    return content

def enhance_handoff_section(content, protocol_num, metadata):
    """Enhance the Handoff Checklist section"""
    
    # Update next protocol reference
    if protocol_num < 23:
        next_protocol = f"{protocol_num + 1:02d}"
        content = re.sub(
            r'Clear handoff to Protocol \d+',
            f'Clear handoff to Protocol {next_protocol}',
            content
        )
    else:
        content = re.sub(
            r'Clear handoff to Protocol \d+',
            'Project completion and closure',
            content
        )
    
    return content

def enhance_communication_section(content, protocol_num, metadata):
    """Enhance the Communication & Stakeholder Alignment section"""
    
    if 'stakeholders' not in metadata:
        return content
    
    # Update primary stakeholder
    if metadata['stakeholders']:
        content = re.sub(
            r'\*\*Primary Stakeholder:\*\* \[Role\]',
            f'**Primary Stakeholder:** {metadata["stakeholders"][0]}',
            content
        )
    
    # Update secondary stakeholders
    if len(metadata['stakeholders']) > 1:
        secondary = ', '.join(metadata['stakeholders'][1:])
        content = re.sub(
            r'\*\*Secondary Stakeholders:\*\* \[List\]',
            f'**Secondary Stakeholders:** {secondary}',
            content
        )
    
    return content

def main():
    """Main function to enhance all protocols"""
    workflow_dir = Path("/home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow")
    
    # Process protocols 1-23
    for protocol_num in range(1, 24):
        protocol_file = workflow_dir / f"{protocol_num:02d}-*.md"
        
        # Find the actual file
        matching_files = list(workflow_dir.glob(f"{protocol_num:02d}-*.md"))
        
        if not matching_files:
            print(f"Protocol {protocol_num:02d} file not found, skipping...")
            continue
            
        file_path = matching_files[0]
        print(f"Enhancing Protocol {protocol_num:02d}: {file_path.name}")
        
        if enhance_protocol_file(file_path, protocol_num):
            print(f"✅ Protocol {protocol_num:02d} enhanced successfully")
        else:
            print(f"❌ Protocol {protocol_num:02d} enhancement failed")
    
    print("\n✅ All protocols enhanced!")

if __name__ == "__main__":
    main()
