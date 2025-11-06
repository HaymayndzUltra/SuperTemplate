# Protocol 08b: AI Change Request Management

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: change_management
phase: "Between task generation and execution"
priority: critical
alwaysApply: true
tags: [change-control, impact-analysis, approval-workflow, traceability]
triggers: [requirement-change, scope-change, timeline-change, model-change]
```

## 1. Protocol Overview

**Purpose**: Establish a formal change request process for AI/ML projects to manage modifications between task generation and execution phases, ensuring proper impact analysis, stakeholder approval, and documentation traceability.

**When to Apply**: 
- After Protocol 08 (task generation)
- Before Protocol 10 (task execution)
- Whenever changes to requirements, scope, timeline, or model architecture are requested

**Critical Success Factors**:
- All changes documented with impact analysis
- Stakeholder approval obtained before implementation
- Traceability maintained across all artifacts
- No orphaned artifacts from changes

## 2. Change Request Categories

### 2.1 Requirement Changes
- Functional requirement modifications
- Performance threshold adjustments
- Data source changes
- Model accuracy target updates

### 2.2 Scope Changes
- Feature additions/removals
- Integration boundary modifications
- Platform/deployment target changes
- User segment adjustments

### 2.3 Timeline Changes
- Milestone adjustments
- Resource availability changes
- Dependency timeline shifts
- External constraint updates

### 2.4 Technical Changes
- Model architecture modifications
- Algorithm selection changes
- Infrastructure requirement updates
- Tool/framework migrations

## 3. Change Request Workflow

### Step 1: Change Request Initiation
**Duration**: 1-2 hours

**Activities**:
1. Create change request form
2. Document initial change description
3. Identify requestor and stakeholders
4. Assign unique change ID

**Outputs**:
```markdown
# CHANGE-REQUEST-{id}.md

## Change Request Information
- **ID**: CR-{YYYY}-{MM}-{DD}-{sequence}
- **Requestor**: {name/role}
- **Date**: {submission_date}
- **Priority**: Critical | High | Medium | Low
- **Type**: Requirement | Scope | Timeline | Technical

## Change Description
{detailed_description_of_requested_change}

## Business Justification
{why_this_change_is_needed}

## Initial Risk Assessment
- **Risk Level**: High | Medium | Low
- **Primary Risks**: {list_key_risks}
```

### Step 2: Impact Analysis
**Duration**: 2-4 hours

**Activities**:
1. Analyze downstream effects
2. Evaluate resource implications
3. Assess timeline impacts
4. Calculate cost implications
5. Identify affected artifacts

**Impact Analysis Template**:
```markdown
## Impact Analysis

### Affected Components
- [ ] Data Pipeline
- [ ] Feature Engineering
- [ ] Model Architecture
- [ ] Training Process
- [ ] Evaluation Metrics
- [ ] Deployment Configuration
- [ ] Monitoring Setup

### Resource Impact
- **Additional Hours**: {estimate}
- **Additional Resources**: {list}
- **Budget Impact**: ${amount}

### Timeline Impact
- **Current Milestone**: {date}
- **Projected Milestone**: {new_date}
- **Delay**: {days}
- **Critical Path Impact**: Yes/No

### Technical Impact
- **Code Changes Required**: {list_modules}
- **Data Changes Required**: {list_datasets}
- **Model Retraining Required**: Yes/No
- **Infrastructure Changes**: {list}

### Risk Impact
- **New Risks Introduced**: {list}
- **Existing Risk Changes**: {list}
- **Mitigation Required**: {list}
```

### Step 3: Approval Workflow
**Duration**: 1-2 days

**Approval Matrix**:
| Change Type | Approver Level | SLA |
|------------|----------------|-----|
| Minor (no timeline/cost impact) | Technical Lead | 4 hours |
| Medium (< 1 week impact) | Product Owner | 1 day |
| Major (> 1 week or > $10k) | Steering Committee | 2 days |
| Critical (milestone risk) | Executive Sponsor | Same day |

**Approval Documentation**:
```markdown
## Approval Record

### Approval Chain
1. **Technical Review**
   - Reviewer: {name}
   - Date: {date}
   - Decision: Approved | Rejected | Conditional
   - Comments: {feedback}

2. **Business Review**
   - Reviewer: {name}
   - Date: {date}
   - Decision: Approved | Rejected | Conditional
   - Comments: {feedback}

3. **Final Approval**
   - Approver: {name}
   - Date: {date}
   - Decision: Approved | Rejected
   - Conditions: {if_any}
```

### Step 4: Implementation Planning
**Duration**: 2-3 hours

**Activities**:
1. Update project backlog
2. Revise task definitions
3. Update dependencies
4. Communicate changes
5. Update documentation

**Implementation Checklist**:
```markdown
## Implementation Plan

### Backlog Updates
- [ ] Requirements.md updated
- [ ] Tasks-{feature}.md revised
- [ ] Dependencies mapped
- [ ] Priorities adjusted

### Communication Plan
- [ ] Team notified
- [ ] Stakeholders informed
- [ ] Documentation updated
- [ ] Training scheduled (if needed)

### Rollback Plan
- [ ] Rollback criteria defined
- [ ] Rollback steps documented
- [ ] Rollback owner assigned
```

## 4. Evidence Requirements

### Required Evidence Package
```
CHANGE-EVIDENCE-{id}/
├── change-request-{id}.md
├── impact-analysis-{id}.md
├── approval-records/
│   ├── technical-approval-{id}.pdf
│   ├── business-approval-{id}.pdf
│   └── executive-approval-{id}.pdf (if required)
├── communication/
│   ├── stakeholder-notification-{id}.md
│   └── team-briefing-{id}.md
└── artifacts/
    ├── updated-requirements-{id}.md
    ├── updated-tasks-{id}.md
    └── dependency-matrix-{id}.md
```

## 5. Quality Gates

### Gate 1: Impact Analysis Completeness
**Pass Criteria**:
- [ ] All impact dimensions assessed
- [ ] Quantitative estimates provided
- [ ] Dependencies identified
- [ ] Risks documented

### Gate 2: Approval Completeness
**Pass Criteria**:
- [ ] Required approvers identified
- [ ] All approvals obtained
- [ ] Conditions documented
- [ ] Evidence archived

### Gate 3: Implementation Readiness
**Pass Criteria**:
- [ ] Backlog updated
- [ ] Tasks revised
- [ ] Team informed
- [ ] Rollback plan exists

## 6. Automation Hooks

### Validation Script
```python
#!/usr/bin/env python3
# validators-system/08b-change-request/validate_change_request.py

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple

def validate_change_request(change_id: str) -> Tuple[bool, List[str]]:
    """Validate change request completeness and approval chain."""
    errors = []
    evidence_path = Path(f"evidence/CHANGE-EVIDENCE-{change_id}")
    
    # Check required files
    required_files = [
        f"change-request-{change_id}.md",
        f"impact-analysis-{change_id}.md",
        "approval-records/technical-approval-{change_id}.pdf"
    ]
    
    for file in required_files:
        if not (evidence_path / file).exists():
            errors.append(f"Missing required file: {file}")
    
    # Validate impact analysis
    impact_file = evidence_path / f"impact-analysis-{change_id}.md"
    if impact_file.exists():
        content = impact_file.read_text()
        required_sections = [
            "Affected Components",
            "Resource Impact", 
            "Timeline Impact",
            "Technical Impact"
        ]
        for section in required_sections:
            if section not in content:
                errors.append(f"Missing impact analysis section: {section}")
    
    return len(errors) == 0, errors
```

### Notification Automation
```yaml
# .github/workflows/change-request-notification.yml
name: Change Request Notification

on:
  pull_request:
    paths:
      - 'protocols/change-requests/**.md'

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Parse Change Request
        id: parse
        run: |
          echo "Parsing change request details..."
          # Extract metadata and send notifications
      
      - name: Notify Stakeholders
        uses: actions/github-script@v6
        with:
          script: |
            // Send notifications to approvers based on change type
```

## 7. Metrics & Monitoring

### Key Metrics
- **Change Request Volume**: Count per sprint
- **Approval Turnaround Time**: Average hours by type
- **Change Implementation Success Rate**: Successful/Total
- **Change-Related Defects**: Defects traced to changes
- **Rollback Frequency**: Rollbacks/Changes

### Monitoring Dashboard
```python
# monitoring/change_request_metrics.py
def generate_change_metrics_dashboard():
    """Generate change request metrics dashboard."""
    metrics = {
        "total_changes": count_change_requests(),
        "avg_approval_time": calculate_approval_time(),
        "success_rate": calculate_success_rate(),
        "by_type": group_by_type(),
        "by_impact": group_by_impact()
    }
    return metrics
```

## 8. Integration Points

### Upstream Dependencies
- Protocol 08: Generate Tasks (provides baseline)
- Protocol 06: PRD Creation (defines requirements)
- Protocol 07: Technical Design (defines architecture)

### Downstream Effects
- Protocol 10: Process Tasks (implements changes)
- Protocol 11: Integration Testing (validates changes)
- Protocol 19: Documentation (updates docs)

## 9. Common Pitfalls & Mitigations

### Pitfall 1: Incomplete Impact Analysis
**Mitigation**: Use automated dependency scanning to identify all affected components

### Pitfall 2: Approval Delays
**Mitigation**: Implement escalation triggers for SLA breaches

### Pitfall 3: Poor Change Communication
**Mitigation**: Automated notifications and status dashboards

### Pitfall 4: Missing Traceability
**Mitigation**: Enforce linking between change requests and task updates

## 10. Success Criteria

**Protocol Success Metrics**:
- 100% of changes have complete impact analysis
- 95% of changes approved within SLA
- 0 orphaned artifacts from changes
- 100% traceability from request to implementation
- < 5% changes require rollback

## Appendix A: Templates

### A.1 Quick Change Assessment
For minor changes with minimal impact:
```markdown
# Quick Change Assessment
- **Change**: {one_line_description}
- **Impact**: Low | Medium | High
- **Effort**: < 2 hours | 2-8 hours | > 8 hours
- **Risk**: Low | Medium | High
- **Decision**: Implement | Defer | Reject
```

### A.2 Emergency Change Process
For critical production fixes:
```markdown
# Emergency Change Request
- **Incident ID**: {link_to_incident}
- **Severity**: P0 | P1
- **Fix Description**: {what_needs_changing}
- **Rollback Plan**: {how_to_rollback}
- **Post-Implementation Review**: {scheduled_date}
```

## Appendix B: RACI Matrix

| Activity | Requestor | Tech Lead | Product Owner | Steering Committee |
|----------|-----------|-----------|---------------|-------------------|
| Initiate Change | A | I | I | I |
| Impact Analysis | C | R | C | I |
| Approve Minor | I | A | I | - |
| Approve Major | I | R | A | C |
| Approve Critical | I | R | R | A |
| Implement | I | R | I | I |
| Verify | C | A | R | I |

**Legend**: R=Responsible, A=Accountable, C=Consulted, I=Informed
