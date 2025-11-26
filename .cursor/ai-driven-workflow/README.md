# MASTER RAY™ Generic Workflow Protocols

**Universal Software Development Workflow - From Client Discovery to Project Closure**

---

## 🎯 Overview

This directory contains the **Generic Track** protocols for software development projects. These protocols provide a comprehensive, validated workflow for any software project—from initial client discovery through deployment and maintenance.

### Key Features

- **22+ Validated Protocols**: Complete lifecycle coverage
- **6 Workflow Phases**: Foundation → Planning → Development → Testing → Deployment → Closure
- **Quality Gates**: Each protocol has mandatory validation checkpoints
- **Evidence-Driven**: Artifact generation for audit trails
- **Human-AI Collaboration**: Clear handoff points and communication protocols

---

## 📂 Protocol Map

### Phase 1: Foundation & Discovery

| Protocol | Name | Purpose |
|----------|------|---------|
| 01 | [Client Proposal Generation](./01-client-proposal-generation.md) | Generate professional proposals from requirements |
| 02 | [Client Discovery Initiation](./02-client-discovery-initiation.md) | Structured stakeholder discovery sessions |
| 03 | [Project Brief Creation](./03-project-brief-creation.md) | Synthesize discovery into actionable brief |
| 04 | [Bootstrap & Context Engineering](./04-project-bootstrap-context-engineering.md) | Initialize project context and AI understanding |

### Phase 2: Planning & Design

| Protocol | Name | Purpose |
|----------|------|---------|
| 05b | [Protocol Orchestration](./05b-project-protocol-orchestration-v2.md) | **ROUTER**: Select and sequence protocols |
| 05c | [Generate Rules](./05c-generate-rules.md) | Create project-specific rules |
| 06 | [Create PRD](./06-create-prd.md) | Product Requirements Document generation |
| 07 | [Technical Design & Architecture](./07-technical-design-architecture.md) | System architecture and design decisions |
| 08 | [Generate Tasks](./08-generate-tasks.md) | Break PRD into actionable tasks |

### Phase 3: Development

| Protocol | Name | Purpose |
|----------|------|---------|
| 09 | [Environment Setup & Validation](./09-environment-setup-validation.md) | Configure development environment |
| 10 | [Process Tasks](./10-process-tasks.md) | Execute development tasks systematically |
| 11 | [Integration Testing](./11-integration-testing.md) | Validate component integration |

### Phase 4: Quality & Testing

| Protocol | Name | Purpose |
|----------|------|---------|
| 12 | [Quality Audit](./12-quality-audit.md) | Comprehensive quality assessment |
| 13 | [UAT Coordination](./13-uat-coordination.md) | User Acceptance Testing management |
| 31 | [Validation Recovery](./31-validation-recovery-remediation.md) | Handle validation failures |

### Phase 5: Deployment & Operations

| Protocol | Name | Purpose |
|----------|------|---------|
| 14 | [Pre-Deployment Staging](./14-pre-deployment-staging.md) | Staging environment verification |
| 15 | [Production Deployment](./15-production-deployment.md) | Safe production release |
| 16 | [Monitoring & Observability](./16-monitoring-observability.md) | Setup monitoring dashboards |
| 17 | [Incident Response & Rollback](./17-incident-response-rollback.md) | Emergency procedures |
| 18 | [Performance Optimization](./18-performance-optimization.md) | Post-deployment optimization |

### Phase 6: Closure & Maintenance

| Protocol | Name | Purpose |
|----------|------|---------|
| 19 | [Documentation & Knowledge Transfer](./19-documentation-knowledge-transfer.md) | Finalize documentation |
| 20 | [Project Closure](./20-project-closure.md) | Formal project completion |
| 21 | [Maintenance & Support](./21-maintenance-support.md) | Ongoing support procedures |
| 22 | [Implementation Retrospective](./22-implementation-retrospective.md) | Lessons learned |

### Supporting Protocols

| Protocol | Name | Purpose |
|----------|------|---------|
| 23 | [Script Governance](./23-script-governance-protocol.md) | Manage automation scripts |
| 24 | [Client Discovery (Alternate)](./24-client-discovery-ALTERNATE-TRACK.md) | Alternative discovery approach |
| 25 | [Protocol Integration Map](./25-protocol-integration-map-DOCUMENTATION.md) | Cross-protocol dependencies |
| 26 | [Integration Guide](./26-integration-guide-DOCUMENTATION.md) | How to integrate protocols |
| 27 | [Validation Guide](./27-validation-guide-DOCUMENTATION.md) | Validation standards |
| 28 | [Meta-Instruction Builder](./28-meta-instruction-builder.md) | Build AI instructions |

---

## 🔄 Workflow Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    MASTER RAY™ GENERIC WORKFLOW                        │
└─────────────────────────────────────────────────────────────────────────┘

Phase 1: Foundation                Phase 2: Planning
┌──────────────────────┐          ┌──────────────────────┐
│  01 → 02 → 03 → 04   │    →     │  05b → 06 → 07 → 08  │
│  Proposal  Discovery │          │  Router  PRD  Arch   │
│  Brief     Bootstrap │          │  Rules   Tasks       │
└──────────────────────┘          └──────────────────────┘
                                           │
                                           ▼
Phase 3: Development              Phase 4: Testing
┌──────────────────────┐          ┌──────────────────────┐
│  09 → 10 → 11        │    →     │  12 → 13 → 31        │
│  Env    Process      │          │  Audit UAT Recovery  │
│  Setup  Tasks        │          │                      │
└──────────────────────┘          └──────────────────────┘
                                           │
                                           ▼
Phase 5: Deployment               Phase 6: Closure
┌──────────────────────┐          ┌──────────────────────┐
│  14 → 15 → 16 → 17   │    →     │  19 → 20 → 21 → 22   │
│  Stage Deploy Monitor│          │  Docs Close Support  │
│  Incident Perf       │          │  Retro               │
└──────────────────────┘          └──────────────────────┘
```

---

## 🎛️ Protocol 05b: The Router

Protocol 05b is the **intelligent orchestrator** that selects which protocols apply to your project.

### How It Works

1. **Input**: Project brief, characteristics, constraints
2. **Classification**: Analyzes 27+ dimensions to classify project type
3. **Selection**: Picks relevant protocols from both tracks
4. **Sequencing**: Orders protocols based on dependencies
5. **Customization**: Adjusts parameters per project needs
6. **Output**: Complete execution plan

### Triggering the Router

```markdown
Invoke Protocol 05b when:
- Starting a new project
- Project scope significantly changes
- Switching development phases
- Adding new workstreams
```

See [05b-project-protocol-orchestration-v2.md](./05b-project-protocol-orchestration-v2.md) for details.

---

## 📋 Protocol Structure

Every protocol follows this standardized structure:

```markdown
# Protocol [ID]: [Name]

## 1. Identity & Ownership
- Protocol ID, Version, Owner
- Status, Dependencies

## 2. Integration Points
- Inputs from previous protocols
- Outputs to next protocols

## 3. AI Role & Mission
- AI persona for this protocol
- Specific capabilities

## 4. Workflow (Phases)
- Step-by-step instructions
- Decision points
- Parallel paths

## 5. Quality Gates
- Validation checkpoints
- Pass/fail criteria
- Remediation paths

## 6. Communication Protocols
- Human handoff points
- Status messages
- Error communication

## 7. Automation Hooks
- Scripts to execute
- Parameters required

## 8. Handoff Checklist
- What must exist before next protocol

## 9. Evidence Summary
- Artifacts generated
- Storage location

## 10. Reasoning & Reflection
- Design rationale
- Evolution notes
```

---

## 🔌 Integration with AI/ML Track

This Generic Track integrates with the [AI/ML Track](../../AI-project-workflow/) for machine learning projects:

```
Generic Track                    AI/ML Track
─────────────                    ───────────
01-04: Foundation        ←→      01-05: Foundation (shared)
05b: Router              ←→      Selects AI/ML protocols
06-07: PRD & Architecture →      06-07: Use Case & Data Strategy
08-10: Tasks & Dev       →       08-15: ML Pipeline
12-17: Testing & Deploy  →       16-24: Model Deployment
```

The Router (05b) automatically determines which track(s) apply based on project classification.

---

## 🛠️ Quick Start

### For a New Project

1. **Run Protocol 01**: Generate client proposal
2. **Run Protocol 02**: Conduct discovery session
3. **Run Protocol 03**: Create project brief
4. **Run Protocol 04**: Bootstrap context
5. **Run Protocol 05b**: Router selects remaining protocols

### For an Existing Project

1. **Gather context**: Existing docs, codebase, constraints
2. **Run Protocol 04**: Bootstrap context with existing info
3. **Run Protocol 05b**: Router generates execution plan
4. **Follow generated plan**: Execute selected protocols

---

## ✅ Quality Assurance

### Validators

Each protocol is validated by the [Validator System](../../validators-system/):

| Validator | What It Checks |
|-----------|----------------|
| Identity | Unique ID, version, ownership |
| AI Role | Clear AI mission and persona |
| Workflow | Complete, valid phases |
| Quality Gates | Defined checkpoints |
| Script Integration | Automation hooks |
| Communication | Handoff clarity |
| Evidence | Artifact definitions |
| Handoff | Exit criteria |
| Reasoning | Design rationale |
| Reflection | Evolution notes |

### Passing Score

- **Threshold**: ≥0.95 (95%)
- **All validators must pass** for protocol to be valid

---

## 📚 Related Documentation

- [AI/ML Protocols](../../AI-project-workflow/) - Machine learning workflow
- [Validator System](../../validators-system/) - Protocol validation
- [Orchestration Scripts](../../scripts/orchestration/) - Automation
- [ARCHITECTURE.md](../../ARCHITECTURE.md) - System architecture

---

## 🔍 Protocol Selection Guide

| Project Type | Key Protocols |
|--------------|---------------|
| **Web App** | 01-08, 10-15, 19-20 |
| **API Service** | 02-04, 06-11, 14-17 |
| **Mobile App** | 01-08, 10-15, 18-20 |
| **ML Project** | Generic 01-05 + AI/ML Track |
| **Maintenance** | 21, 31 |
| **Greenfield** | Full sequence 01-22 |

---

**MASTER RAY™ Generic Workflow** - Validated excellence from discovery to delivery.

