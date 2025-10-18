# 🤖 AGENTS.md - AI-Driven Workflow Protocol Guide

## Purpose
This document explains how AI agents (including GPT-5-Codex) should interpret and execute the AI-driven workflow protocols in this directory.

## Understanding AI-Driven Workflow

### What is AI-Driven Workflow?
The AI-driven workflow is a **5-phase development lifecycle** that transforms AI from a simple code generator into a reliable engineering partner. Each protocol represents a specific reasoning phase that mirrors how senior developers work.

### Core Philosophy
- **"Why Before How"**: Every action must align with cognitive dependencies
- **Developer Cognitive Loop**: Protocols follow natural developer thinking patterns
- **Reasoning Integrity**: Automation extends reasoning, never replaces it
- **Evidence-Based**: All actions must be validated and documented

## Protocol Structure

### File Organization
```
.cursor/ai-driven-workflow/
├── 0-bootstrap-your-project.md      # Phase 0: Project initialization
├── 1-create-prd.md                  # Phase 1: Requirements documentation
├── 2-generate-tasks.md              # Phase 2: Task planning
├── 3-process-tasks.md               # Phase 3: Task execution
├── 4-quality-audit.md               # Phase 4: Quality validation
├── 5-implementation-retrospective.md # Phase 5: Continuous improvement
├── review-protocols/                 # Quality review protocols
└── README.md                        # Workflow overview
```

### Protocol Format
Each protocol follows this structure:
```markdown
# PROTOCOL: [Name] ([Domain] Compliant)

## Purpose
Clear explanation of what this protocol accomplishes.

## Role Assignment
The AI acts as a [specific role] during this phase.

## Prerequisites
What must be completed before this protocol.

## Execution Steps
1. **Step 1**: Detailed instructions
2. **Step 2**: Next actions
3. **Step 3**: Validation requirements

## Evidence Collection
What evidence must be collected and documented.

## Quality Gates
Validation checkpoints that must be passed.
```

## Phase-by-Phase Execution

### Phase 0: Bootstrap Your Project
**AI Role**: Project Analyst
**Purpose**: Analyze codebase and build Context Kit

**Execution Logic**:
1. **Scan Codebase**: Analyze entire project structure
2. **Identify Patterns**: Detect technology stack, architecture patterns
3. **Generate Context Kit**: Create foundational READMEs and rules
4. **Validate Understanding**: Confirm AI comprehension of project

**Evidence Required**:
- Project structure analysis
- Technology stack identification
- Generated context documentation
- Validation of AI understanding

### Phase 1: Create PRD
**AI Role**: Product Manager
**Purpose**: Transform requirements into implementation-ready PRD

**Execution Logic**:
1. **Analyze Requirements**: Understand business needs
2. **Define Scope**: Determine what to build
3. **Create Architecture**: Design system structure
4. **Document Specifications**: Write detailed requirements

**Evidence Required**:
- Requirements analysis
- Scope definition
- Architecture design
- PRD documentation

### Phase 2: Generate Tasks
**AI Role**: Technical Lead
**Purpose**: Break PRD into actionable development tasks

**Execution Logic**:
1. **Decompose PRD**: Break down requirements into tasks
2. **Estimate Effort**: Assess complexity and time requirements
3. **Prioritize Tasks**: Order tasks by dependencies and importance
4. **Create Delivery Plan**: Organize tasks into phases

**Evidence Required**:
- Task decomposition
- Effort estimates
- Priority ordering
- Delivery plan

### Phase 3: Process Tasks
**AI Role**: Senior Developer
**Purpose**: Execute tasks with evidence collection

**Execution Logic**:
1. **Select Task**: Choose next task to work on
2. **Implement Solution**: Write code following standards
3. **Validate Implementation**: Test and verify functionality
4. **Document Evidence**: Record implementation details

**Evidence Required**:
- Task selection rationale
- Implementation details
- Validation results
- Evidence documentation

### Phase 4: Quality Audit
**AI Role**: Quality Assurance Engineer
**Purpose**: Validate implementation quality and readiness

**Execution Logic**:
1. **Run Quality Checks**: Execute automated validation
2. **Review Code**: Analyze code quality and standards
3. **Test Functionality**: Verify feature completeness
4. **Document Findings**: Record quality assessment

**Evidence Required**:
- Quality check results
- Code review findings
- Test results
- Quality assessment

### Phase 5: Implementation Retrospective
**AI Role**: Engineering Manager
**Purpose**: Analyze process and identify improvements

**Execution Logic**:
1. **Analyze Process**: Review workflow execution
2. **Identify Issues**: Find problems and inefficiencies
3. **Document Learnings**: Record insights and improvements
4. **Update Protocols**: Enhance workflow based on learnings

**Evidence Required**:
- Process analysis
- Issue identification
- Learning documentation
- Protocol updates

## Review Protocols Integration

### Review Protocol Structure
Located in `review-protocols/` directory:
- **code-review.md**: Code quality validation
- **security-check.md**: Security compliance
- **architecture-review.md**: Architecture validation
- **design-system.md**: UI/UX compliance
- **ui-accessibility.md**: Accessibility validation
- **pre-production.md**: Pre-deployment validation

### Review Protocol Usage
Review protocols are triggered by:
1. **Quality Audit Phase**: Automatic execution during Phase 4
2. **Manual Trigger**: Explicit user request
3. **Context Detection**: Automatic based on code changes
4. **Integration Hooks**: CI/CD pipeline integration

## Evidence Collection System

### Evidence Types
Each protocol must collect specific evidence:

1. **Analysis Evidence**: Understanding and comprehension
2. **Implementation Evidence**: Code and configuration
3. **Validation Evidence**: Testing and verification
4. **Process Evidence**: Workflow execution details

### Evidence Format
```json
{
  "protocol": "protocol-name",
  "phase": "phase-number",
  "timestamp": "2024-01-01T00:00:00Z",
  "evidence": {
    "analysis": "analysis details",
    "implementation": "implementation details",
    "validation": "validation results",
    "process": "process documentation"
  },
  "quality_gates": {
    "gate1": "passed",
    "gate2": "passed"
  }
}
```

## Quality Gates

### Gate Types
1. **Prerequisite Gates**: Must pass before protocol execution
2. **Execution Gates**: Must pass during protocol execution
3. **Completion Gates**: Must pass before protocol completion
4. **Integration Gates**: Must pass for workflow integration

### Gate Validation
Each gate requires:
- **Clear Criteria**: Specific validation requirements
- **Evidence Collection**: Documentation of gate passage
- **Failure Handling**: What to do if gate fails
- **Recovery Process**: How to retry failed gates

## Integration with Cursor

### Cursor Commands Integration
Workflow protocols integrate with Cursor commands:

```bash
# Apply specific protocol
@apply .cursor/ai-driven-workflow/1-create-prd.md

# Execute with context
@apply .cursor/ai-driven-workflow/3-process-tasks.md @codebase

# Quality audit
@apply .cursor/ai-driven-workflow/4-quality-audit.md --mode comprehensive
```

### Context Awareness
Protocols leverage Cursor's context features:
- **@codebase**: Full project context
- **@recent-changes**: Git change analysis
- **@filename**: File-specific context
- **@recent-changes**: Recent modification analysis

## Automation Integration

### Script Integration
Protocols integrate with automation scripts:
- **Bootstrap Scripts**: Project initialization automation
- **Generation Scripts**: Code and documentation generation
- **Validation Scripts**: Quality and compliance checking
- **Deployment Scripts**: Release and deployment automation

### CI/CD Integration
Workflow protocols integrate with CI/CD:
- **Quality Gates**: Automated validation in pipelines
- **Evidence Collection**: Automated documentation
- **Process Validation**: Workflow compliance checking
- **Integration Testing**: End-to-end validation

## Best Practices for AI Agents

### Protocol Execution
1. **Follow Sequence**: Execute protocols in order
2. **Collect Evidence**: Document all actions and decisions
3. **Validate Gates**: Ensure all quality gates pass
4. **Maintain Context**: Keep context throughout execution

### Evidence Management
1. **Document Everything**: Record all analysis and decisions
2. **Validate Evidence**: Ensure evidence is complete and accurate
3. **Store Persistently**: Save evidence for future reference
4. **Link Dependencies**: Connect evidence across protocols

### Quality Assurance
1. **Check Prerequisites**: Verify all prerequisites are met
2. **Execute Thoroughly**: Complete all protocol steps
3. **Validate Results**: Ensure outcomes meet requirements
4. **Document Findings**: Record all validation results

## Error Handling

### Protocol Failures
When protocols fail:
1. **Identify Root Cause**: Determine why failure occurred
2. **Document Failure**: Record failure details and context
3. **Implement Fix**: Address the underlying issue
4. **Retry Protocol**: Re-execute from appropriate point

### Quality Gate Failures
When quality gates fail:
1. **Stop Execution**: Halt protocol execution
2. **Analyze Failure**: Understand why gate failed
3. **Implement Fix**: Address the issue
4. **Re-validate**: Re-run gate validation

### Integration Failures
When integrations fail:
1. **Fallback Mode**: Use alternative approaches
2. **Manual Override**: Allow human intervention
3. **Document Issue**: Record integration problems
4. **Update Protocols**: Improve based on learnings

## Troubleshooting

### Common Issues
1. **Missing Prerequisites**: Ensure all prerequisites are met
2. **Incomplete Evidence**: Verify evidence collection
3. **Failed Quality Gates**: Address gate failures
4. **Integration Problems**: Resolve integration issues

### Debug Commands
```bash
# Validate protocol structure
python scripts/validate_protocols.py

# Test protocol execution
python scripts/test_protocol_execution.py

# Check evidence collection
python scripts/validate_evidence.py
```

## Protocol Quality Analysis & Remediation

### Current State Assessment
Based on comprehensive analysis of all 28 protocols in the AI-driven workflow system, four detailed audit reports have been generated (see `@report.md` for complete analysis):

#### Report 1: Structural Completeness Analysis
- **Scope**: All 28 protocols evaluated for structural compliance
- **Key Findings**: 6 protocols missing core sections, 22 protocols with minor gaps
- **Critical Issues**: Missing prerequisites, scattered automation hooks, incomplete integration points
- **Average Score**: 6.90/10 across all protocols

#### Report 2: Integration & Handoff Analysis  
- **Scope**: Protocol-to-protocol integration and evidence flow
- **Key Findings**: 12 critical handoff failures, 8 evidence flow issues
- **Critical Issues**: Missing integration sections, broken artifact chains, incomplete handoffs
- **Impact**: Workflow continuity compromised across multiple protocols

#### Report 3: Quality Gates & Validation Analysis
- **Scope**: Quality assurance mechanisms and validation criteria
- **Key Findings**: Implied prerequisites, scattered quality gates, missing validation scripts
- **Critical Issues**: Non-measurable criteria, incomplete failure handling, missing automation
- **Impact**: Quality assurance gaps throughout workflow

#### Report 4: Communication & Automation Analysis
- **Scope**: Communication protocols and automation integration
- **Key Findings**: Inconsistent communication templates, scattered automation hooks
- **Critical Issues**: Missing communication sections, narrative-only automation, incomplete error handling
- **Impact**: Reduced automation effectiveness and communication clarity

### Remediation Strategy

#### Phase 1: Critical Protocol Restructure (6 protocols)
**Target Protocols**: 00-generate-rules, 1, 2, 3, 4, 5
**Action Required**: Complete structural rewrite using proven patterns
**Success Criteria**: All 9 mandatory sections present, 10/10 quality scores

#### Phase 2: Major Section Additions (8 protocols)  
**Target Protocols**: 00a, 00B, 01, 00, 0, 00-CD, 8, review-protocols
**Action Required**: Add missing prerequisites, consolidate automation, fix integration
**Success Criteria**: Complete structural compliance, 8.0+ quality scores

#### Phase 3: Prerequisites Enhancement (14 protocols)
**Target Protocols**: 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
**Action Required**: Add explicit prerequisites sections
**Success Criteria**: Clear prerequisite validation, improved workflow continuity

### Implementation Approach

#### For AI Agents (GPT-5-Codex)
1. **Reference Analysis Reports**: Use `@report.md` for detailed protocol-specific issues
2. **Follow Proven Patterns**: Apply structural patterns from high-scoring protocols (6, 7, 9, 10, 11, 12, 13, 15)
3. **Maintain Integration**: Ensure seamless handoffs between protocols
4. **Validate Quality**: Use measurable criteria for all quality gates
5. **Consolidate Automation**: Group all scripts in dedicated sections

#### For Protocol Regeneration
1. **Use Master Checklist**: Reference `MASTER-VERIFICATION-CHECKLIST.md` for comprehensive remediation matrix
2. **Apply Structural Patterns**: Follow `STRUCTURAL-PATTERNS-REFERENCE.md` for proven templates
3. **Execute Systematic Remediation**: Address issues in priority order (Critical → High → Medium)
4. **Validate Circular Integration**: Ensure protocols work together as cohesive system
5. **Achieve Target Scores**: Target 10/10 in Completeness, Clarity, Actionability, Integration, Evidence, Automation

### Quality Targets
- **Current Average**: 6.90/10
- **Target Average**: ≥9.5/10  
- **Protocols ≥8.0**: 14/28 → 28/28 (100%)
- **Protocols <7.0**: 8/28 → 0/28 (0%)
- **Protocols <5.0**: 6/28 → 0/28 (0%)

## Conclusion

The AI-driven workflow provides a structured approach to AI-assisted development. By understanding the protocol structure, execution logic, and evidence requirements, AI agents can effectively guide development from initial concept to production deployment.

**Key Takeaways**:
- **Sequential Execution**: Protocols must be executed in order
- **Evidence Required**: All actions must be documented
- **Quality Gates**: Validation checkpoints must be passed
- **Integration**: Protocols work together as a cohesive system
- **Continuous Improvement**: Learnings feed back into protocol enhancement
- **Quality Assurance**: Systematic remediation based on comprehensive analysis

This system ensures that AI agents can provide consistent, high-quality assistance while maintaining the reasoning integrity and evidence-based approach that makes the workflow effective.

**Next Steps**: Use the analysis reports in `@report.md` to systematically remediate all 28 protocols, achieving 10/10 quality scores across all metrics while maintaining seamless integration and evidence flow throughout the complete SDLC lifecycle.
