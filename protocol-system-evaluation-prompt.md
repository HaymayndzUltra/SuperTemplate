# AI-Driven Workflow Protocol System Evaluation Prompt

## Overview

You are an AI evaluation specialist with extensive experience in assessing AI-driven protocols and developer workflows. I would like you to rigorously test a comprehensive meta-instruction protocol system designed to support the complete software development lifecycle from client discovery to production maintenance.

## Evaluation Scope

### Starting Point: 5 Foundation Protocols

Begin your evaluation with these 5 protocols as the workflow entry point:

1. **01-client-proposal-generation.md** - Client proposal creation
2. **02-client-discovery-initiation.md** - Initial client discovery  
3. **01-project-brief-creation.md** - Project brief/PRD creation
4. **00-project-bootstrap-and-context-engineering.md** - Project initialization
5. **00-generate-rules.md** - Cursor rules generation

### Complete Protocol Sequence (28 Total)

From the 5 starting protocols, trace the workflow through all 28 protocols in this sequence:

**Phase 0: Foundation (5)** → 01 → 02 → 01 → 00 → 00-generate-rules

**Phase 1-2: Planning (3)** → 1 → 6 → 2 → 7

**Phase 3: Development (2)** → 3 → 9

**Phase 4: Quality (3)** → 4 → 15 → 10

**Phase 5: Deployment (4)** → 11 → 12 → 13 → 14

**Phase 6: Closure (5)** → 16 → 17 → 18 → 5 → 8

## Evaluation Framework

### 1. Protocol Validation

For each of the 28 protocols, examine:

#### ✅ Completeness Checklist
- [ ] All required sections present (Role, Mission, Workflow, Integration, Quality Gates, Communication, Handoff)
- [ ] Step-by-step execution algorithm defined
- [ ] Prerequisites clearly documented
- [ ] Evidence requirements specified
- [ ] Automation hooks defined
- [ ] Integration points mapped
- [ ] Quality gates with measurable criteria
- [ ] Communication protocols established
- [ ] Handoff checklist complete

#### ❌ Gap Identification
- Missing sections or incomplete content
- Unclear or ambiguous instructions
- Missing evidence requirements
- Undefined quality gates
- Missing automation hooks
- Unclear integration points
- Missing communication protocols
- Incomplete handoff procedures

#### 💡 Improvement Suggestions
- Specific recommendations for missing content
- Clarity improvements for ambiguous sections
- Integration enhancement suggestions
- Evidence requirement refinements
- Automation opportunity identification
- Communication protocol improvements
- Handoff procedure enhancements

### 2. Integration Validation

#### Handoff Analysis
For each protocol transition, validate:
- **Input Artifacts**: Does Protocol N receive complete inputs from Protocol N-1?
- **Output Artifacts**: Does Protocol N produce all required outputs for Protocol N+1?
- **Quality Gates**: Are quality gates properly enforced at handoff points?
- **Evidence Flow**: Does evidence flow seamlessly between protocols?

#### Dependency Mapping
- Verify all prerequisite dependencies are satisfied
- Check for circular dependencies
- Identify missing dependencies
- Validate dependency ordering

### 3. Scoring Framework

#### Per-Protocol Scoring (1-10 scale)
Each protocol scored across 6 dimensions:

1. **Completeness** (1-10): All sections present, fully detailed
2. **Clarity** (1-10): Easy to understand and follow
3. **Actionability** (1-10): Steps are concrete and executable
4. **Integration** (1-10): Seamless handoffs with adjacent protocols
5. **Evidence** (1-10): Clear, measurable validation criteria
6. **Automation** (1-10): Automation hooks well-defined and executable

**Overall Protocol Score**: Average of 6 dimensions

#### System-Level Scoring
- **Overall Alignment Score**: Percentage of perfect protocol handoffs
- **Coverage Score**: Percentage of SDLC phases covered
- **Completeness Score**: Average of all protocol completeness scores
- **Integration Score**: Average of all protocol integration scores

### 4. Real-world Simulation

Test the protocols under various project scenarios:

#### Scenario 1: Simple Project
- Single-page application with basic CRUD
- Minimal external integrations
- Standard deployment pipeline

#### Scenario 2: Medium Complexity Project
- Multi-service architecture
- Database migrations
- CI/CD pipeline with testing

#### Scenario 3: Complex Enterprise Project
- Microservices architecture
- Multiple external integrations
- Advanced monitoring and observability
- Compliance requirements

#### Scenario 4: Crisis Scenario
- Production incident requiring rollback
- Performance degradation
- Security vulnerability

### 5. Reporting Requirements

#### Comprehensive Markdown Report Structure:

```markdown
# AI-Driven Workflow Protocol System Evaluation

## Executive Summary
- Overall system scores
- Critical findings
- High-priority recommendations

## Protocol Sequence Map
- Visual workflow diagram
- Protocol dependencies
- Integration points

## Per-Protocol Analysis
### Protocol 01: Client Proposal Generation
#### ✅ Completeness Checklist
#### ❌ Gaps Identified
#### 💡 Improvement Suggestions
#### Scores
- Completeness: X/10
- Clarity: X/10
- Actionability: X/10
- Integration: X/10
- Evidence: X/10
- Automation: X/10
- **Overall: X/10**

[Repeat for all 28 protocols]

## Integration Analysis
### Critical Integration Points
### Handoff Quality Matrix
### Evidence Flow Analysis
### Dependency Validation

## Scoring Summary
### System-Level Scores
### Per-Protocol Score Matrix
### Dimension Analysis

## Improvement Roadmap
### Critical Fixes (Required)
### High-Priority Enhancements
### Medium-Priority Improvements
### Nice-to-Have Additions

## Real-world Simulation Results
### Scenario 1: Simple Project
### Scenario 2: Medium Complexity Project
### Scenario 3: Complex Enterprise Project
### Scenario 4: Crisis Scenario
```

#### Scoring Spreadsheet Requirements:
Excel/CSV format with:
- Per-protocol scores across 6 dimensions
- System-level aggregate scores
- Color-coded priority matrix
- Gap tracking checklist

## Success Criteria

- All 28 protocols evaluated with detailed analysis
- Complete integration mapping with handoff validation
- Comprehensive scoring across all dimensions
- Actionable improvement recommendations
- Prioritized enhancement roadmap
- Real-world simulation results
- Complete documentation package

## Context Files

The following files contain the complete protocol system:

### Foundation Protocols (5)
- `.cursor/ai-driven-workflow/01-client-proposal-generation.md`
- `.cursor/ai-driven-workflow/02-client-discovery-initiation.md`
- `.cursor/ai-driven-workflow/01-project-brief-creation.md`
- `.cursor/ai-driven-workflow/00-project-bootstrap-and-context-engineering.md`
- `.cursor/ai-driven-workflow/00-generate-rules.md`

### Core Workflow Protocols (23)
- `.cursor/ai-driven-workflow/1-create-prd.md`
- `.cursor/ai-driven-workflow/2-generate-tasks.md`
- `.cursor/ai-driven-workflow/3-process-tasks.md`
- `.cursor/ai-driven-workflow/4-quality-audit.md`
- `.cursor/ai-driven-workflow/5-implementation-retrospective.md`
- `.cursor/ai-driven-workflow/6-technical-design-architecture.md`
- `.cursor/ai-driven-workflow/7-environment-setup-validation.md`
- `.cursor/ai-driven-workflow/8-script-governance-protocol.md`
- `.cursor/ai-driven-workflow/9-integration-testing.md`
- `.cursor/ai-driven-workflow/10-pre-deployment-staging.md`
- `.cursor/ai-driven-workflow/11-production-deployment.md`
- `.cursor/ai-driven-workflow/12-monitoring-observability.md`
- `.cursor/ai-driven-workflow/13-incident-response-rollback.md`
- `.cursor/ai-driven-workflow/14-performance-optimization.md`
- `.cursor/ai-driven-workflow/15-uat-coordination.md`
- `.cursor/ai-driven-workflow/16-documentation-knowledge-transfer.md`
- `.cursor/ai-driven-workflow/17-project-closure.md`
- `.cursor/ai-driven-workflow/18-maintenance-support.md`

### Supporting Documentation
- `.cursor/ai-driven-workflow/README.md`
- `.cursor/ai-driven-workflow/AGENTS.md`
- `.cursor/commands/AGENTS.md`
- `.cursor/commands/elaborate.md`

## Evaluation Instructions

1. **Read all 28 protocol files** to understand the complete workflow structure
2. **Analyze each protocol** using the completeness checklist, gap identification, and improvement suggestions framework
3. **Map integration points** between consecutive protocols to validate handoff completeness
4. **Score each protocol** across the 6 dimensions (1-10 scale)
5. **Calculate system-level scores** for overall assessment
6. **Simulate real-world scenarios** to test protocol robustness
7. **Generate comprehensive report** with detailed findings and recommendations
8. **Create scoring spreadsheet** with all metrics and priority matrix

## Expected Deliverables

1. **Comprehensive Markdown Report** (as specified above)
2. **Scoring Spreadsheet** (Excel/CSV format)
3. **Protocol Gap Analysis** (detailed per-protocol findings)
4. **Integration Validation Report** (handoff analysis)
5. **Real-world Simulation Results** (scenario testing outcomes)
6. **Improvement Roadmap** (prioritized action items)

## Evaluation Timeline

- **Phase 1**: Protocol Analysis (2-3 hours)
- **Phase 2**: Integration Validation (1-2 hours)
- **Phase 3**: Scoring & Simulation (1-2 hours)
- **Phase 4**: Report Generation (1-2 hours)

**Total Estimated Time**: 5-9 hours

## Quality Standards

- **Thoroughness**: Every protocol must be analyzed in detail
- **Accuracy**: Scores must be justified with specific evidence
- **Actionability**: Recommendations must be concrete and implementable
- **Completeness**: All evaluation criteria must be addressed
- **Clarity**: Findings must be clearly communicated with examples

## Success Metrics

- **Coverage**: 100% of protocols analyzed
- **Integration**: All handoff points validated
- **Scoring**: Complete dimensional analysis
- **Simulation**: All scenarios tested
- **Documentation**: Comprehensive report package

---

**Begin your evaluation now. Focus on thoroughness, accuracy, and actionable insights that will help improve this AI-driven workflow protocol system.**
