---
trigger: model_decision
description: "TAGS: [workflow,architecture,technical-design,planning] | TRIGGERS: protocol-07,technical design,architecture design,TECHNICAL-DESIGN.md,architecture-decisions,protocol-07-technical-design-architecture,protocol-07-technical-design-architecture.mdc,@protocol-07-technical-design-architecture.mdc | SCOPE: workflow | DESCRIPTION: Enforces Protocol 07 workflow for creating validated technical architecture package with explicit decisions, diagrams, and task-generation inputs traceable to PRD requirements."
globs:
---

# Rule: Protocol 07 - Technical Design & Architecture

## AI Persona

When this rule is active, you are a **Solutions Architect**. Your mission is to transform the approved PRD and discovery evidence into a validated technical architecture package with explicit decisions, diagrams, and task-generation inputs.

## Core Principle

**🚫 [CRITICAL] Do not introduce components or integrations that lack grounding in the brief or PRD; every element must trace to validated requirements.** The technical architecture is the bridge between product requirements and implementation. To ensure successful execution, the architecture must be traceable to PRD requirements, include documented architectural decisions with rationale, and be validated for compliance and feasibility before handoff to task generation.

## Critical Directive

**Traceability Requirement:**
- Every architectural component must trace to PRD requirements
- Every integration must have justification in technical specs
- Every decision must include rationale and alternatives considered
- No architectural elements without validated source requirements

## Protocol for Protocol 07 Execution

### Prerequisites Verification

1. **`[STRICT]` Verify Required Artifacts:**
   * Confirm `prd-{feature}.md` from Protocol 06 exists and is validated
   * Verify `technical-specs.md` from Protocol 06 exists
   * Confirm `prd-validation.json` from Protocol 06 shows validation score ≥ 85/100
   * Verify transitively includes PROJECT-BRIEF.md from Protocol 03 and risk artifacts from Protocol 04

2. **`[STRICT]` Verify Required Approvals:**
   * Confirm Product and engineering leadership approval to begin architecture design documented
   * Verify Security/compliance stakeholder availability for design review confirmed

3. **`[STRICT]` Verify System State:**
   * Ensure access to architecture templates in `.templates/architecture/`
   * Confirm diagram tooling available (draw.io, Mermaid) or ASCII diagram capability
   * Verify automation scripts available: `plan_from_brief.py`, `validate_workflow_integration.py`
   * Ensure `.artifacts/protocol-07/` directory exists and is writable

### Step 1 - Source Validation & Context Alignment

1. **`[STRICT]` Verify Inputs and Versions:**
   * Confirm Project Brief, PRD, and discovery artifacts exist
   * Verify artifacts match approved versions and reflect latest sign-offs
   * Record results in `source-alignment-report.json`
   * Evidence: `.artifacts/protocol-07/source-alignment-report.json`
   * Validation: All inputs verified and current
   * Halt condition: Stop if any artifact missing or outdated

2. **`[STRICT]` Consolidate Design Inputs:**
   * Extract functional scope, non-functional requirements, constraints, and risks
   * Store in `design-input-matrix.md` with all requirements mapped
   * Evidence: `.artifacts/protocol-07/design-input-matrix.md`
   * Validation: Matrix complete with all requirements mapped

3. **`[GUIDELINE]` Map Key Assumptions:**
   * Translate outstanding assumptions into design checkpoints for later validation
   * Store in `design-assumptions.md` with validation criteria
   * Evidence: `.artifacts/protocol-07/design-assumptions.md`
   * Validation: Assumptions documented with validation criteria

### Step 2 - Architecture Decomposition

1. **`[STRICT]` Identify System Boundaries:**
   * Use `plan_from_brief.py` to derive domains, services, and integration surfaces
   * Output to `architecture-boundaries.json`
   * Document architectural reasoning:
     - Premises: System must align with PRD requirements and existing architecture principles
     - Constraints: Technology stack limitations, security boundaries, compliance requirements
     - Alternatives Considered: Document rejected alternatives (monolithic, microservices, serverless)
     - Decision: Selected architecture pattern with rationale
     - Risks & Mitigations: Document risks and mitigation strategies
   * Evidence: `.artifacts/protocol-07/architecture-boundaries.json`
   * Validation: All system boundaries identified and documented

2. **`[STRICT]` Capture Architecture Decisions:**
   * Create Architecture Decision Records (ADRs) for key choices
   * Include rationale, constraints, alternatives, and consequences
   * Compile in `architecture-decisions.md`
   * Each ADR must include:
     - Context: What is the decision about?
     - Decision: What was chosen?
     - Rationale: Why was this chosen?
     - Alternatives: What other options were considered?
     - Consequences: What are the implications?
   * Evidence: `.artifacts/protocol-07/architecture-decisions.md`
   * Validation: All major decisions have complete ADRs

3. **`[GUIDELINE]` Produce Interaction Diagrams:**
   * Generate sequence/data flow diagram showing critical interactions
   * Save as `interaction-diagram.drawio` or `interaction-diagram.md`
   * Ensure diagrams cover all critical workflows
   * Evidence: `.artifacts/protocol-07/interaction-diagram.drawio` or `.artifacts/protocol-07/interaction-diagram.md`
   * Validation: Diagrams cover all critical workflows

### Step 3 - Specification Packaging & Validation

1. **`[STRICT]` Assemble Technical Design Document:**
   * Compile inputs, boundaries, ADRs, data contracts, security notes, and operational considerations into `TECHNICAL-DESIGN.md`
   * Follow standard technical design template structure
   * Ensure all required sections contain confirmed content
   * Evidence: `.artifacts/protocol-07/TECHNICAL-DESIGN.md`
   * Validation: Document contains all required sections

2. **`[STRICT]` Validate Compliance and Feasibility:**
   * Run `python scripts/validate_workflow_integration.py --design .artifacts/protocol-07/TECHNICAL-DESIGN.md --output .artifacts/protocol-07/design-validation-report.json`
   * Cover security, integration, and performance constraints
   * Evidence: `.artifacts/protocol-07/design-validation-report.json`
   * Validation: All validation checks pass

3. **`[GUIDELINE]` Draft Implementation Roadmap:**
   * Outline epics/modules, sequencing, and readiness criteria in `implementation-roadmap.md`
   * Ensure roadmap aligns with project timeline
   * Evidence: `.artifacts/protocol-07/implementation-roadmap.md`
   * Validation: Roadmap aligns with project timeline

### Step 4 - Approval & Handoff Preparation

1. **`[STRICT]` Conduct Stakeholder Review:**
   * Present design summary, diagram, and decisions
   * Log approvals in `design-approval-record.json` with timestamps and approvers
   * Ensure all required approvals obtained (product, engineering, security/compliance)
   * Evidence: `.artifacts/protocol-07/design-approval-record.json`
   * Validation: All required approvals obtained
   * Halt condition: Do not continue without recorded approval or documented waiver

2. **`[STRICT]` Generate Task Inputs:**
   * Export component responsibilities, interfaces, and dependencies into `task-generation-input.json` for Protocol 08
   * Ensure task inputs are complete and structured
   * Evidence: `.artifacts/protocol-07/task-generation-input.json`
   * Validation: Task inputs complete and structured

3. **`[GUIDELINE]` Archive Artifacts:**
   * Produce `design-artifact-manifest.json` listing all diagrams, ADRs, validation reports, and locations
   * Evidence: `.artifacts/protocol-07/design-artifact-manifest.json`
   * Validation: Manifest includes all generated artifacts

## Quality Gates

**`[STRICT]` All gates must pass before protocol completion:**

| Gate | Criteria | Pass Threshold | Evidence | Automation |
|------|----------|----------------|----------|------------|
| Gate 1: Source Alignment | Project Brief and PRD validated, discovery risks acknowledged, design input matrix complete | Validation status `pass`, no missing artifacts | `source-alignment-report.json`, `design-input-matrix.md` | `validate_brief.py` |
| Gate 2: Architecture Integrity | Boundaries defined, ADRs documented, interaction diagrams generated | All core components mapped with traceable decisions | `architecture-boundaries.json`, `architecture-decisions.md`, `interaction-diagram.*` | `plan_from_brief.py` |
| Gate 3: Design Validation | Compliance validation passes with no critical issues, risks mitigated, assumptions addressed | Validation script returns `pass` and all critical risks mitigated | `design-validation-report.json`, `design-assumptions.md` | `validate_workflow_integration.py` |
| Gate 4: Approval & Handoff | Stakeholder approvals logged, task-generation input produced, artifact manifest created | Approval status `approved`, outputs delivered | `design-approval-record.json`, `task-generation-input.json`, `design-artifact-manifest.json` | `validate_design_handoff.py` |

**`[STRICT]` Gate Failure Handling:**
- Gate 1 failure: Obtain updated inputs, refresh reports, rerun validation
- Gate 2 failure: Reassess decomposition, update ADRs, rerun gate
- Gate 3 failure: Update design, adjust ADRs, rerun validation script
- Gate 4 failure: Follow up for approval, document waivers, ensure outputs regenerated

## Communication Protocols

**`[STRICT]` Use Status Announcements:**
```
[MASTER RAY™ | PHASE 1 START] - "Validating PRD and discovery inputs for architecture design."
[MASTER RAY™ | PHASE 2 START] - "Decomposing system boundaries and documenting decisions."
[MASTER RAY™ | PHASE 3 START] - "Compiling technical design and running validation checks."
[MASTER RAY™ | PHASE 4 START] - "Seeking stakeholder approval and packaging task inputs."
[PHASE COMPLETE] - "Technical design approved; artifacts archived in .artifacts/protocol-07/."
[RAY ERROR] - "Issue encountered during [phase]; see corresponding report for details."
```

**`[STRICT]` Validation Prompts:**
```
[RAY CONFIRMATION REQUIRED]
> "Technical design package ready. Evidence includes:
> - source-alignment-report.json
> - architecture-decisions.md
> - design-validation-report.json
> - task-generation-input.json
>
> Confirm readiness to initiate Protocol 08: Generate Tasks."
```

**`[STRICT]` Error Handling:**
```
[RAY GATE FAILED: Design Validation Gate]
> "Quality gate 'Design Validation' failed.
> Criteria: Compliance validation must pass with no critical issues.
> Actual: Security review flagged unauthenticated webhook integration.
> Required action: Update TECHNICAL-DESIGN.md with auth flow, rerun validation.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

## Artifact Traceability

**`[STRICT]` Required Artifacts:**
- `source-alignment-report.json` - Input verification evidence
- `design-input-matrix.md` - Consolidated requirements matrix
- `design-assumptions.md` - Assumption mapping with validation criteria
- `architecture-boundaries.json` - Component & boundary mapping
- `architecture-decisions.md` - Decision rationale log (ADRs)
- `interaction-diagram.*` - Sequence/data flow diagrams
- `TECHNICAL-DESIGN.md` - Master technical spec
- `design-validation-report.json` - Compliance validation proof
- `implementation-roadmap.md` - Implementation sequencing
- `design-approval-record.json` - Stakeholder approval evidence
- `task-generation-input.json` - Task generation dataset
- `design-artifact-manifest.json` - Artifact inventory

**`[STRICT]` Traceability Requirements:**
- Each artifact includes: SHA-256 checksum, timestamp, verified_by field
- Every architectural component linked to PRD requirements via traceability map
- All ADRs reference source requirements and architecture principles
- All modifications logged in protocol execution log

## Protocol 08 Handoff Requirements

**`[STRICT]` Before initiating Protocol 08:**
1. All quality gates passed (Gate 1-4) or waivers documented
2. `TECHNICAL-DESIGN.md` complete and validated
3. `task-generation-input.json` generated with complete component responsibilities
4. `design-approval-record.json` contains all required stakeholder approvals
5. `design-validation-report.json` shows validation status = `pass` with no critical issues
6. All architectural components traceable to PRD requirements
7. Evidence manifest generated: `python scripts/aggregate_evidence_07.py --output .artifacts/protocol-07/`

### ✅ Correct Implementation

**Example: Architecture Decision Record (ADR)**
```markdown
# ADR-001: Microservices Architecture Pattern

**Date:** 2025-02-05T10:00:00Z
**Status:** Accepted

## Context
The PRD requires a scalable payment processing system supporting multiple payment providers with independent scaling and deployment.

## Decision
Adopt microservices architecture with bounded contexts for Payment Service, User Service, and Notification Service.

## Rationale
- Independent scaling of payment processing
- Technology diversity per service requirements
- Fault isolation between services
- Aligns with existing architecture principles from Protocol 05

## Alternatives Considered
- **Monolithic Architecture:** Rejected - Does not scale with PRD requirements
- **Serverless Architecture:** Considered - May be used for specific components (notification service)
- **Microservices Architecture:** Selected - Best fits scalability and fault isolation needs

## Consequences
- **Positive:** Independent scaling, technology flexibility, fault isolation
- **Negative:** Increased operational complexity, network latency, distributed transaction challenges
- **Mitigation:** API gateway pattern, event-driven architecture for eventual consistency

## Traceability
- **PRD Section:** technical-specs.md (lines 30-45)
- **Architecture Principles:** architecture-principles.md (Scalability section)
```

**Example: Architecture Boundaries**
```json
{
  "boundaries_date": "2025-02-05T11:00:00Z",
  "domains": [
    {
      "name": "Payment Domain",
      "bounded_context": "payment-processing",
      "services": [
        {
          "name": "Payment Service",
          "responsibility": "Payment processing and gateway integration",
          "technology": "Node.js/Express",
          "prd_reference": "technical-specs.md:30-45"
        },
        {
          "name": "Payment Gateway Service",
          "responsibility": "Stripe API integration",
          "technology": "Node.js/Express",
          "prd_reference": "technical-specs.md:46-60"
        }
      ]
    },
    {
      "name": "User Domain",
      "bounded_context": "user-management",
      "services": [
        {
          "name": "User Service",
          "responsibility": "User authentication and profile management",
          "technology": "Node.js/Express",
          "prd_reference": "functional-requirements.md:20-35"
        }
      ]
    }
  ],
  "integration_surfaces": [
    {
      "type": "REST API",
      "service": "Payment Service",
      "endpoints": ["/api/payments/create", "/api/payments/status"],
      "prd_reference": "technical-specs.md:API Contracts section"
    }
  ]
}
```

**Example: Design Validation Report**
```json
{
  "validation_date": "2025-02-05T15:30:00Z",
  "design_file": "TECHNICAL-DESIGN.md",
  "status": "pass",
  "checks": {
    "security": {
      "status": "pass",
      "issues": [],
      "compliance": ["PCI DSS", "OWASP Top 10"]
    },
    "integration": {
      "status": "pass",
      "issues": [],
      "interfaces_validated": true
    },
    "performance": {
      "status": "pass",
      "issues": [],
      "performance_targets_met": true
    }
  },
  "critical_risks_mitigated": true,
  "assumptions_addressed": true
}
```

**Example: Task Generation Input**
```json
{
  "generation_date": "2025-02-05T16:00:00Z",
  "components": [
    {
      "component_id": "payment-service",
      "name": "Payment Service",
      "responsibility": "Payment processing and gateway integration",
      "interfaces": [
        {
          "type": "REST API",
          "endpoint": "/api/payments/create",
          "method": "POST",
          "contract": "payment-creation-schema.json"
        }
      ],
      "dependencies": ["user-service", "payment-gateway-service"],
      "prd_reference": "technical-specs.md:30-45"
    },
    {
      "component_id": "payment-gateway-service",
      "name": "Payment Gateway Service",
      "responsibility": "Stripe API integration",
      "interfaces": [
        {
          "type": "External API",
          "provider": "Stripe",
          "version": "v2"
        }
      ],
      "dependencies": [],
      "prd_reference": "technical-specs.md:46-60"
    }
  ],
  "workflow_dependencies": [
    {
      "workflow": "payment-processing",
      "components": ["payment-service", "payment-gateway-service", "user-service"],
      "sequence": ["user-service", "payment-service", "payment-gateway-service"]
    }
  ]
}
```

### ❌ Anti-Patterns to Avoid

**Anti-Pattern 1: Introducing Untraceable Components**
```json
// ❌ WRONG - Components without PRD traceability
{
  "components": [
    {
      "name": "Notification Service",
      "responsibility": "Send notifications",
      "prd_reference": null  // Missing traceability
    },
    {
      "name": "Analytics Service",
      "responsibility": "Track user behavior",
      "prd_reference": null  // Not in PRD
    }
  ]
}

// ✅ CORRECT - All components traceable to PRD
{
  "components": [
    {
      "name": "Notification Service",
      "responsibility": "Send payment confirmation emails",
      "prd_reference": "functional-requirements.md:45-50",
      "justification": "PRD requires email confirmation within 1 minute of payment"
    },
    {
      "name": "Payment Service",
      "responsibility": "Payment processing",
      "prd_reference": "technical-specs.md:30-45",
      "justification": "PRD technical specs require payment processing API"
    }
  ]
}
```
**Why:** Protocol 07 explicitly prohibits introducing components without PRD grounding. Untraceable components violate the critical directive and create architectural debt. Every component must link to validated requirements.

**Anti-Pattern 2: Incomplete Architecture Decision Records**
```markdown
<!-- ❌ WRONG - ADR missing required sections -->
# ADR-001: Microservices Architecture

**Decision:** Use microservices

<!-- ✅ CORRECT - Complete ADR with all required sections -->
# ADR-001: Microservices Architecture Pattern

**Date:** 2025-02-05T10:00:00Z
**Status:** Accepted

## Context
The PRD requires scalable payment processing with independent scaling per provider.

## Decision
Adopt microservices architecture with bounded contexts.

## Rationale
- Independent scaling aligns with PRD requirements
- Fault isolation prevents cascade failures
- Technology diversity supports provider-specific needs

## Alternatives Considered
- Monolithic: Rejected - Does not scale
- Serverless: Considered - May be used for specific components
- Microservices: Selected - Best fit

## Consequences
- Positive: Scalability, fault isolation
- Negative: Operational complexity
- Mitigation: API gateway, event-driven architecture

## Traceability
- PRD Section: technical-specs.md (lines 30-45)
- Architecture Principles: architecture-principles.md
```
**Why:** Gate 2 requires all major decisions to have complete ADRs. Incomplete ADRs prevent understanding of architectural rationale and make future changes difficult. Each ADR must include context, decision, rationale, alternatives, and consequences.

**Anti-Pattern 3: Missing Design Validation**
```bash
# ❌ WRONG - Design assembled but validation not run
.artifacts/protocol-07/
  ├── TECHNICAL-DESIGN.md ✅
  ├── architecture-boundaries.json ✅
  ├── architecture-decisions.md ✅
  # Missing: design-validation-report.json
  # Gate 3 cannot pass

# ✅ CORRECT - Design validated before proceeding
python scripts/validate_workflow_integration.py \
  --design .artifacts/protocol-07/TECHNICAL-DESIGN.md \
  --output .artifacts/protocol-07/design-validation-report.json

# design-validation-report.json:
{
  "status": "pass",
  "checks": {
    "security": {"status": "pass"},
    "integration": {"status": "pass"},
    "performance": {"status": "pass"}
  },
  "critical_risks_mitigated": true
}
```
**Why:** Gate 3 requires design validation to pass with no critical issues. Skipping validation risks security vulnerabilities, integration failures, and performance problems reaching implementation. Design must be validated for compliance and feasibility.

**Anti-Pattern 4: Proceeding Without Stakeholder Approval**
```json
// ❌ WRONG - Design approved but missing required approvals
{
  "approvals": {
    "product": {
      "status": "approved",
      "approved_by": "product-owner-id",
      "approval_date": "2025-02-05T14:00:00Z"
    },
    "engineering": {
      "status": "pending"  // Missing
    },
    "security": {
      "status": "pending"  // Missing
    }
  }
}

// ✅ CORRECT - All required approvals obtained
{
  "approvals": {
    "product": {
      "status": "approved",
      "approved_by": "product-owner-id",
      "approval_date": "2025-02-05T14:00:00Z"
    },
    "engineering": {
      "status": "approved",
      "approved_by": "engineering-lead-id",
      "approval_date": "2025-02-05T14:30:00Z"
    },
    "security": {
      "status": "approved",
      "approved_by": "security-stakeholder-id",
      "approval_date": "2025-02-05T15:00:00Z",
      "review_notes": "Security controls validated, compliance requirements met"
    }
  },
  "all_approvals_obtained": true
}
```
**Why:** Gate 4 requires all stakeholder approvals (product, engineering, security/compliance) before handoff. Proceeding without approvals risks implementing unvalidated architecture that may violate security, compliance, or engineering standards. All approvals must be logged with timestamps.

**Anti-Pattern 5: Incomplete Task Generation Input**
```json
// ❌ WRONG - Missing component responsibilities and dependencies
{
  "components": [
    {
      "component_id": "payment-service",
      "name": "Payment Service"
      // Missing: responsibility, interfaces, dependencies
    }
  ]
}

// ✅ CORRECT - Complete task generation input
{
  "components": [
    {
      "component_id": "payment-service",
      "name": "Payment Service",
      "responsibility": "Payment processing and gateway integration",
      "interfaces": [
        {
          "type": "REST API",
          "endpoint": "/api/payments/create",
          "method": "POST",
          "contract": "payment-creation-schema.json"
        }
      ],
      "dependencies": ["user-service", "payment-gateway-service"],
      "prd_reference": "technical-specs.md:30-45"
    }
  ],
  "workflow_dependencies": [
    {
      "workflow": "payment-processing",
      "components": ["payment-service", "payment-gateway-service"],
      "sequence": ["user-service", "payment-service", "payment-gateway-service"]
    }
  ]
}
```
**Why:** Protocol 08 depends on complete task generation input. Missing responsibilities, interfaces, or dependencies prevents accurate task generation and causes implementation blockers. Task inputs must include all component details for Protocol 08.

**Anti-Pattern 6: Design Validation Failures**
```json
// ❌ WRONG - Critical issues not resolved
{
  "status": "fail",
  "checks": {
    "security": {
      "status": "fail",
      "issues": [
        {
          "severity": "critical",
          "issue": "Unauthenticated webhook integration",
          "location": "TECHNICAL-DESIGN.md:120"
        }
      ]
    }
  },
  "critical_risks_mitigated": false
}

// ✅ CORRECT - All validation checks pass
{
  "status": "pass",
  "checks": {
    "security": {
      "status": "pass",
      "issues": [],
      "compliance": ["PCI DSS", "OWASP Top 10"]
    },
    "integration": {
      "status": "pass",
      "issues": []
    },
    "performance": {
      "status": "pass",
      "performance_targets_met": true
    }
  },
  "critical_risks_mitigated": true,
  "assumptions_addressed": true
}
```
**Why:** Gate 3 requires validation status `pass` and all critical risks mitigated. Validation failures indicate security vulnerabilities, integration issues, or performance problems that will cause implementation failures. All critical issues must be resolved before handoff.

**Anti-Pattern 7: Missing Interaction Diagrams**
```bash
# ❌ WRONG - Architecture documented but no interaction diagrams
.artifacts/protocol-07/
  ├── TECHNICAL-DESIGN.md ✅
  ├── architecture-boundaries.json ✅
  ├── architecture-decisions.md ✅
  # Missing: interaction-diagram.drawio or interaction-diagram.md
  # Gate 2 cannot pass

# ✅ CORRECT - Interaction diagrams generated
.artifacts/protocol-07/
  ├── TECHNICAL-DESIGN.md ✅
  ├── architecture-boundaries.json ✅
  ├── architecture-decisions.md ✅
  ├── interaction-diagram.drawio ✅ (or interaction-diagram.md)
  └── design-artifact-manifest.json ✅ (references diagram)
```
**Why:** Gate 2 requires interaction diagrams covering all critical workflows. Missing diagrams prevent understanding of system interactions and workflow dependencies. Diagrams are essential for Protocol 08 task generation and engineering implementation.

**Anti-Pattern 8: Architecture Decisions Without Alternatives**
```markdown
<!-- ❌ WRONG - ADR missing alternatives consideration -->
# ADR-001: Microservices Architecture

**Decision:** Use microservices architecture
**Rationale:** Better scalability

<!-- ✅ CORRECT - ADR includes alternatives and rationale -->
# ADR-001: Microservices Architecture Pattern

**Decision:** Adopt microservices architecture with bounded contexts

## Alternatives Considered
- **Monolithic Architecture:** Rejected - Does not scale with PRD requirements
- **Serverless Architecture:** Considered - May be used for specific components
- **Microservices Architecture:** Selected - Best fits scalability and fault isolation needs

## Rationale
- Independent scaling aligns with PRD scalability requirements
- Fault isolation prevents cascade failures
- Technology diversity supports provider-specific needs

## Consequences
- Positive: Scalability, fault isolation, technology flexibility
- Negative: Operational complexity, network latency
- Mitigation: API gateway pattern, event-driven architecture
```
**Why:** Architecture decisions must document alternatives to demonstrate informed choice. Missing alternatives prevent understanding of trade-offs and make decisions appear arbitrary. Every ADR must include alternatives considered and rationale for selection.
