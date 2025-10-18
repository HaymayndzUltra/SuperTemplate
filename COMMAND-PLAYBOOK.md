# Complete Lifecycle Command Playbook

## 🎯 Overview
This playbook provides copy-paste commands for executing the complete AI-driven workflow system. All commands are ready to use and follow the correct protocol sequence.

---

## 🚀 Client Project Lifecycle (Full SDLC)

### Phase 0: Client Engagement & Discovery

#### 1. Client Proposal Generation
```bash
@apply .cursor/ai-driven-workflow/01-client-proposal-generation.md
```
**Purpose**: Generate professional client proposals from job posts
**Prerequisites**: `JOB-POST.md` file
**Evidence**: `.artifacts/protocol-01/jobpost-analysis.json`

#### 2. Client Discovery Initiation
```bash
@apply .cursor/ai-driven-workflow/02-client-discovery-initiation.md
```
**Purpose**: Initiate comprehensive client discovery process
**Prerequisites**: Approved proposal
**Evidence**: `.artifacts/protocol-02/discovery-analysis.json`

#### 3. Project Brief Creation
```bash
@apply .cursor/ai-driven-workflow/03-project-brief-creation.md
```
**Purpose**: Create detailed project brief with scope and success criteria
**Prerequisites**: Completed discovery
**Evidence**: `.artifacts/protocol-03/project-brief.md`

#### 4. Project Bootstrap & Context Engineering
```bash
@apply .cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md
```
**Purpose**: Bootstrap project with proper context and tooling
**Prerequisites**: Approved project brief
**Evidence**: `.artifacts/protocol-04/bootstrap-report.json`

#### 5. Bootstrap Your Project
```bash
@apply .cursor/ai-driven-workflow/05-bootstrap-your-project.md
```
**Purpose**: Initialize project structure and development environment
**Prerequisites**: Project context established
**Evidence**: `.artifacts/protocol-05/project-structure-analysis.json`

### Phase 1-2: Planning & Design

#### 6. Create Product Requirements Document
```bash
@apply .cursor/ai-driven-workflow/06-create-prd.md
```
**Purpose**: Create comprehensive PRD with detailed requirements
**Prerequisites**: Project brief and bootstrap complete
**Evidence**: `.artifacts/protocol-06/prd-document.md`

#### 7. Technical Design & Architecture
```bash
@apply .cursor/ai-driven-workflow/07-technical-design-architecture.md
```
**Purpose**: Design technical architecture and system structure
**Prerequisites**: PRD approved
**Evidence**: `.artifacts/protocol-07/architecture-design.md`

#### 8. Generate Development Tasks
```bash
@apply .cursor/ai-driven-workflow/08-generate-tasks.md
```
**Purpose**: Break PRD into actionable development tasks
**Prerequisites**: Architecture design complete
**Evidence**: `.artifacts/protocol-08/task-breakdown.json`

#### 9. Environment Setup & Validation
```bash
@apply .cursor/ai-driven-workflow/09-environment-setup-validation.md
```
**Purpose**: Setup and validate development environment
**Prerequisites**: Tasks generated
**Evidence**: `.artifacts/protocol-09/environment-validation.json`

### Phase 3: Development

#### 10. Process Development Tasks
```bash
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase
```
**Purpose**: Execute development tasks with evidence collection
**Prerequisites**: Environment validated
**Evidence**: `.artifacts/protocol-10/task-execution-log.json`

#### 11. Integration Testing
```bash
@apply .cursor/ai-driven-workflow/11-integration-testing.md
```
**Purpose**: Perform comprehensive integration testing
**Prerequisites**: Tasks implemented
**Evidence**: `.artifacts/protocol-11/integration-test-results.json`

### Phase 4: Quality & Testing

#### 12. Quality Audit
```bash
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode comprehensive
```
**Purpose**: Comprehensive quality audit and validation
**Prerequisites**: Integration testing complete
**Evidence**: `.artifacts/protocol-12/quality-audit-report.json`

**Alternative Modes**:
```bash
# Quick audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode quick

# Security-focused audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode security

# Architecture review
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode architecture
```

#### 13. UAT Coordination
```bash
@apply .cursor/ai-driven-workflow/13-uat-coordination.md
```
**Purpose**: Coordinate User Acceptance Testing with stakeholders
**Prerequisites**: Quality audit passed
**Evidence**: `.artifacts/protocol-13/uat-results.json`

#### 14. Pre-Deployment Staging
```bash
@apply .cursor/ai-driven-workflow/14-pre-deployment-staging.md
```
**Purpose**: Pre-deployment staging validation and preparation
**Prerequisites**: UAT completed
**Evidence**: `.artifacts/protocol-14/staging-validation.json`

### Phase 5: Deployment & Operations

#### 15. Production Deployment
```bash
@apply .cursor/ai-driven-workflow/15-production-deployment.md
```
**Purpose**: Execute production deployment with rollback planning
**Prerequisites**: Staging validation passed
**Evidence**: `.artifacts/protocol-15/deployment-report.json`

#### 16. Monitoring & Observability
```bash
@apply .cursor/ai-driven-workflow/16-monitoring-observability.md
```
**Purpose**: Setup comprehensive monitoring and observability
**Prerequisites**: Deployment successful
**Evidence**: `.artifacts/protocol-16/monitoring-setup.json`

#### 17. Incident Response & Rollback
```bash
@apply .cursor/ai-driven-workflow/17-incident-response-rollback.md
```
**Purpose**: Incident management and rollback procedures
**Prerequisites**: Monitoring active
**Evidence**: `.artifacts/protocol-17/incident-response-log.json`

#### 18. Performance Optimization
```bash
@apply .cursor/ai-driven-workflow/18-performance-optimization.md
```
**Purpose**: Performance analysis and optimization
**Prerequisites**: System stable
**Evidence**: `.artifacts/protocol-18/performance-analysis.json`

### Phase 6: Closure & Maintenance

#### 19. Documentation & Knowledge Transfer
```bash
@apply .cursor/ai-driven-workflow/19-documentation-knowledge-transfer.md
```
**Purpose**: Create comprehensive documentation and knowledge transfer
**Prerequisites**: System optimized
**Evidence**: `.artifacts/protocol-19/documentation-package.zip`

#### 20. Project Closure
```bash
@apply .cursor/ai-driven-workflow/20-project-closure.md
```
**Purpose**: Project closure and stakeholder sign-off
**Prerequisites**: Documentation complete
**Evidence**: `.artifacts/protocol-20/project-closure-report.json`

#### 21. Maintenance & Support
```bash
@apply .cursor/ai-driven-workflow/21-maintenance-support.md
```
**Purpose**: Ongoing maintenance and support planning
**Prerequisites**: Project closed
**Evidence**: `.artifacts/protocol-21/maintenance-plan.md`

#### 22. Implementation Retrospective
```bash
@apply .cursor/ai-driven-workflow/22-implementation-retrospective.md
```
**Purpose**: Process analysis and lessons learned
**Prerequisites**: Maintenance plan created
**Evidence**: `.artifacts/protocol-22/retrospective-report.md`

---

## 🔧 Technical Development Workflow

### Quick Development Cycle
For rapid development without full client engagement:

```bash
# 1. Bootstrap project
@apply .cursor/ai-driven-workflow/05-bootstrap-your-project.md

# 2. Create requirements
@apply .cursor/ai-driven-workflow/06-create-prd.md

# 3. Design architecture
@apply .cursor/ai-driven-workflow/07-technical-design-architecture.md

# 4. Generate tasks
@apply .cursor/ai-driven-workflow/08-generate-tasks.md

# 5. Execute development
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase

# 6. Integration testing
@apply .cursor/ai-driven-workflow/11-integration-testing.md

# 7. Quality audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode quick
```

### MVP Development
For minimum viable product development:

```bash
# Essential MVP workflow
@apply .cursor/ai-driven-workflow/05-bootstrap-your-project.md
@apply .cursor/ai-driven-workflow/06-create-prd.md
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode quick
```

### Enterprise Development
For complex enterprise projects:

```bash
# Full enterprise workflow (use complete client project lifecycle above)
# All 22 protocols in sequence for maximum quality and compliance
```

---

## 🔍 Quality Assurance Workflow

### Comprehensive Quality Check
```bash
# Full quality audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode comprehensive

# Security-focused audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode security

# Architecture review
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode architecture

# Pre-deployment validation
@apply .cursor/ai-driven-workflow/14-pre-deployment-staging.md
```

### Code Review Workflow
```bash
# Quick code review
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode quick

# Security scan
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode security

# Performance analysis
@apply .cursor/ai-driven-workflow/18-performance-optimization.md
```

### Pre-Production Validation
```bash
# Staging validation
@apply .cursor/ai-driven-workflow/14-pre-deployment-staging.md

# UAT coordination
@apply .cursor/ai-driven-workflow/13-uat-coordination.md

# Final quality check
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode comprehensive
```

---

## 🚨 Emergency Response Workflow

### Incident Management
```bash
# Incident response
@apply .cursor/ai-driven-workflow/17-incident-response-rollback.md

# Performance optimization
@apply .cursor/ai-driven-workflow/18-performance-optimization.md

# Monitoring setup
@apply .cursor/ai-driven-workflow/16-monitoring-observability.md
```

### Bug Fix Workflow
```bash
# Security audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode security

# Task execution for fixes
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase

# Integration testing
@apply .cursor/ai-driven-workflow/11-integration-testing.md
```

### Rollback Procedures
```bash
# Incident response with rollback
@apply .cursor/ai-driven-workflow/17-incident-response-rollback.md

# Performance optimization after rollback
@apply .cursor/ai-driven-workflow/18-performance-optimization.md
```

---

## 🔧 Maintenance Workflow

### Ongoing Maintenance
```bash
# Maintenance planning
@apply .cursor/ai-driven-workflow/21-maintenance-support.md

# Documentation updates
@apply .cursor/ai-driven-workflow/19-documentation-knowledge-transfer.md

# Script governance
@apply .cursor/ai-driven-workflow/23-script-governance-protocol.md
```

### System Updates
```bash
# Environment validation
@apply .cursor/ai-driven-workflow/09-environment-setup-validation.md

# Task execution for updates
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase

# Quality audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode quick
```

### Performance Monitoring
```bash
# Performance optimization
@apply .cursor/ai-driven-workflow/18-performance-optimization.md

# Monitoring setup
@apply .cursor/ai-driven-workflow/16-monitoring-observability.md
```

---

## 🎯 Custom Workflows

### Feature Development
```bash
# Generate tasks for new feature
@apply .cursor/ai-driven-workflow/08-generate-tasks.md

# Execute feature development
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase

# Integration testing
@apply .cursor/ai-driven-workflow/11-integration-testing.md

# Quality audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode quick
```

### API Development
```bash
# Architecture design
@apply .cursor/ai-driven-workflow/07-technical-design-architecture.md

# Task generation
@apply .cursor/ai-driven-workflow/08-generate-tasks.md

# Development execution
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase

# Integration testing
@apply .cursor/ai-driven-workflow/11-integration-testing.md
```

### Database Migration
```bash
# Architecture review
@apply .cursor/ai-driven-workflow/07-technical-design-architecture.md

# Task execution
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase

# Integration testing
@apply .cursor/ai-driven-workflow/11-integration-testing.md

# Quality audit
@apply .cursor/ai-driven-workflow/12-quality-audit.md --mode security
```

---

## 🔧 Advanced Commands

### Context Integration
```bash
# Full codebase context
@apply .cursor/ai-driven-workflow/10-process-tasks.md @codebase

# Recent changes context
@apply .cursor/ai-driven-workflow/12-quality-audit.md @recent-changes

# File-specific context
@apply .cursor/ai-driven-workflow/07-technical-design-architecture.md @filename
```

### Automation Scripts
```bash
# Validate protocols
python scripts/validate_protocols.py

# Test protocol execution
python scripts/test_protocol_execution.py

# Check evidence collection
python scripts/validate_evidence.py

# Run quality audit
python scripts/run_quality_audit.py
```

### CI/CD Integration
```bash
# Linting workflow
.github/workflows/ci-lint.yml

# Testing workflow
.github/workflows/ci-test.yml

# Security scan
.github/workflows/security-scan.yml

# Deployment
.github/workflows/deploy.yml
```

---

## 📋 Command Reference

### Protocol Numbers & Names
| # | Protocol Name | Command |
|---|---------------|---------|
| 01 | client-proposal-generation | `@apply .cursor/ai-driven-workflow/01-client-proposal-generation.md` |
| 02 | client-discovery-initiation | `@apply .cursor/ai-driven-workflow/02-client-discovery-initiation.md` |
| 03 | project-brief-creation | `@apply .cursor/ai-driven-workflow/03-project-brief-creation.md` |
| 04 | project-bootstrap-and-context-engineering | `@apply .cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md` |
| 05 | bootstrap-your-project | `@apply .cursor/ai-driven-workflow/05-bootstrap-your-project.md` |
| 06 | create-prd | `@apply .cursor/ai-driven-workflow/06-create-prd.md` |
| 07 | technical-design-architecture | `@apply .cursor/ai-driven-workflow/07-technical-design-architecture.md` |
| 08 | generate-tasks | `@apply .cursor/ai-driven-workflow/08-generate-tasks.md` |
| 09 | environment-setup-validation | `@apply .cursor/ai-driven-workflow/09-environment-setup-validation.md` |
| 10 | process-tasks | `@apply .cursor/ai-driven-workflow/10-process-tasks.md` |
| 11 | integration-testing | `@apply .cursor/ai-driven-workflow/11-integration-testing.md` |
| 12 | quality-audit | `@apply .cursor/ai-driven-workflow/12-quality-audit.md` |
| 13 | uat-coordination | `@apply .cursor/ai-driven-workflow/13-uat-coordination.md` |
| 14 | pre-deployment-staging | `@apply .cursor/ai-driven-workflow/14-pre-deployment-staging.md` |
| 15 | production-deployment | `@apply .cursor/ai-driven-workflow/15-production-deployment.md` |
| 16 | monitoring-observability | `@apply .cursor/ai-driven-workflow/16-monitoring-observability.md` |
| 17 | incident-response-rollback | `@apply .cursor/ai-driven-workflow/17-incident-response-rollback.md` |
| 18 | performance-optimization | `@apply .cursor/ai-driven-workflow/18-performance-optimization.md` |
| 19 | documentation-knowledge-transfer | `@apply .cursor/ai-driven-workflow/19-documentation-knowledge-transfer.md` |
| 20 | project-closure | `@apply .cursor/ai-driven-workflow/20-project-closure.md` |
| 21 | maintenance-support | `@apply .cursor/ai-driven-workflow/21-maintenance-support.md` |
| 22 | implementation-retrospective | `@apply .cursor/ai-driven-workflow/22-implementation-retrospective.md` |
| 23 | script-governance-protocol | `@apply .cursor/ai-driven-workflow/23-script-governance-protocol.md` |
| 24 | client-discovery | `@apply .cursor/ai-driven-workflow/24-client-discovery.md` |
| 25 | protocol-integration-map | `@apply .cursor/ai-driven-workflow/25-protocol-integration-map.md` |
| 26 | integration-guide | `@apply .cursor/ai-driven-workflow/26-integration-guide.md` |
| 27 | validation-guide | `@apply .cursor/ai-driven-workflow/27-validation-guide.md` |

### Quality Audit Modes
| Mode | Command | Purpose |
|------|---------|---------|
| comprehensive | `--mode comprehensive` | Full quality audit |
| quick | `--mode quick` | Quick quality check |
| security | `--mode security` | Security-focused audit |
| architecture | `--mode architecture` | Architecture review |
| design | `--mode design` | UI/UX review |
| ui | `--mode ui` | UI accessibility check |
| deep-security | `--mode deep-security` | Deep security analysis |

---

## 🎯 Success Tips

### Best Practices
1. **Follow Sequence**: Execute protocols in numerical order
2. **Collect Evidence**: Document all actions and decisions
3. **Validate Gates**: Ensure all quality gates pass
4. **Use Context**: Leverage `@codebase`, `@recent-changes`, `@filename`
5. **Check Prerequisites**: Verify all prerequisites before execution

### Common Patterns
- **Client Projects**: Use full lifecycle (01-22)
- **Technical Projects**: Use development cycle (05-12)
- **Emergency Response**: Use incident protocols (17-18)
- **Maintenance**: Use maintenance protocols (19-23)

### Troubleshooting
- **Missing Prerequisites**: Check required artifacts and approvals
- **Failed Gates**: Address issues and re-run validation
- **Integration Problems**: Verify protocol dependencies
- **Evidence Issues**: Ensure complete documentation

---

**Ready to execute? Copy-paste any command above to start your AI-driven workflow!** 🚀
