---
description: "HIGH-LEVEL CONCEPT: Project Brief-Driven Protocol Generation System"
type: "Design Document - Implementation Blueprint"
audience: "AI Implementers (Windsurf, Cursor, etc.)"
version: "1.0"
---

# PROJECT BRIEF-DRIVEN PROTOCOL GENERATION SYSTEM
## High-Level Concept & Implementation Blueprint

**Purpose**: Provide a clear conceptual framework for building a system that can analyze ANY Project Brief and generate the necessary implementation protocols automatically.

**Audience**: AI agents that will implement this system (not for human developers)

---

## 🎯 CORE CONCEPT

### The Big Idea

Instead of having FIXED protocol sequences (01-23 for SDLC, 06-28 for AI/ML), create a **SMART SYSTEM** that:

1. **Reads** the Project Brief (from Protocol 03)
2. **Analyzes** what type of work is needed
3. **Determines** which protocols are required
4. **Generates** protocols that don't exist yet
5. **Reuses** protocols that already exist (01-05, and any from 06-23)

### Visual Concept

```
┌─────────────────────────────────────────────────┐
│  INPUT: PROJECT-BRIEF.md (Protocol 03)          │
│  - Business goals                               │
│  - Tech stack                                   │
│  - Deliverables                                 │
│  - Timeline & milestones                        │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│  ANALYZER: Intelligent Project Analysis         │
│  - Detect project type                          │
│  - Extract requirements                         │
│  - Identify patterns                            │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│  MAPPER: Protocol Requirement Mapping           │
│  - Map requirements → protocol needs            │
│  - Check existing protocols                     │
│  - Identify gaps                                │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│  GENERATOR: Protocol Creation Engine            │
│  - Generate missing protocols                   │
│  - Follow MASTER RAY structure                  │
│  - Inject project context                       │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│  OUTPUT: Complete Protocol Sequence (06-XX)     │
│  - Customized for this specific project        │
│  - Ready for execution                          │
└─────────────────────────────────────────────────┘
```

---

## 📋 PHASE 1: INTELLIGENT ANALYSIS

### Objective
Understand WHAT the project needs by analyzing the Project Brief deeply.

### Key Questions to Answer

1. **What TYPE of project is this?**
   ```
   Decision Tree:
   
   IF mentions "AI", "ML", "model", "training", "dataset"
      → Project Type = AI/ML
      → Look for: data collection, model training, inference
   
   ELSE IF mentions "mobile", "iOS", "Android", "React Native"
      → Project Type = Mobile App
      → Look for: app store, native features, mobile UI
   
   ELSE IF mentions "API", "backend", "database", "server"
      → Project Type = Backend Service
      → Look for: API endpoints, database, integrations
   
   ELSE IF mentions "UI", "frontend", "React", "Next.js"
      → Project Type = Frontend App
      → Look for: components, state management, UI/UX
   
   ELSE IF mentions "infrastructure", "DevOps", "cloud"
      → Project Type = Infrastructure
      → Look for: deployment, monitoring, scaling
   
   ELSE
      → Project Type = Full-Stack / General
      → Look for: all of the above
   ```

2. **What PHASES are mentioned?**
   ```
   Scan Project Brief for:
   - Month 1, Month 2, etc. → Extract timeline
   - Milestones → Extract deliverables per milestone
   - Phases → Extract phase names and goals
   
   Example from Go + Next.js SaaS:
   - Month 1: Foundation & API Design
   - Month 2: Core Features & Integrations
   - Month 3: Performance & Security
   - Month 4: Testing & Optimization
   
   → This tells us we need protocols for:
     - API design
     - Database schema
     - Integrations (Stripe, AWS, etc.)
     - Performance optimization
     - Security audit
     - Testing
   ```

3. **What DELIVERABLES are required?**
   ```
   Extract from Project Brief sections:
   - "Deliverables"
   - "Success Criteria"
   - "Acceptance Criteria"
   
   Example:
   - "API specification and design documentation"
     → Need Protocol: API Design
   
   - "PostgreSQL database schema with migrations"
     → Need Protocol: Database Schema Design
   
   - "Stripe Connect integration"
     → Need Protocol: Payment Integration (Stripe)
   
   - "Performance profiling report (p95 <200ms)"
     → Need Protocol: Performance Optimization
   ```

4. **What INTEGRATIONS are needed?**
   ```
   Scan for third-party services:
   - Payment: Stripe, PayPal → Payment Integration Protocol
   - Storage: AWS S3, GCS → Storage Integration Protocol
   - Auth: Auth0, Firebase → Authentication Protocol
   - Cache: Redis, Memcached → Caching Protocol
   - Queue: SQS, RabbitMQ → Queue Integration Protocol
   - CDN: CloudFront, Cloudflare → CDN Setup Protocol
   - Email: SendGrid, Mailgun → Email Integration Protocol
   ```

5. **What QUALITY requirements exist?**
   ```
   Extract quality targets:
   - "Test coverage ≥80%" → Need Testing Protocol
   - "p95 <200ms" → Need Performance Protocol
   - "Zero critical vulnerabilities" → Need Security Protocol
   - "OWASP Top 10 compliance" → Need Security Audit Protocol
   - "E2E tests for critical flows" → Need E2E Testing Protocol
   ```

### Output of Phase 1

```json
{
  "project_analysis": {
    "project_type": "Full-Stack SaaS",
    "tech_stack": {
      "backend": ["Go", "PostgreSQL"],
      "frontend": ["Next.js", "TypeScript"],
      "infrastructure": ["AWS", "Docker"]
    },
    "timeline": {
      "duration": "4 months",
      "milestones": [
        {"month": 1, "focus": "Foundation & API Design"},
        {"month": 2, "focus": "Core Features & Integrations"},
        {"month": 3, "focus": "Performance & Security"},
        {"month": 4, "focus": "Testing & Optimization"}
      ]
    },
    "deliverables": [
      "API specification",
      "Database schema",
      "Stripe integration",
      "AWS S3 integration",
      "Performance optimization",
      "Security audit",
      "E2E tests",
      "CI/CD pipeline",
      "Documentation"
    ],
    "integrations": [
      {"service": "Stripe", "type": "payment"},
      {"service": "AWS S3", "type": "storage"},
      {"service": "AWS CloudFront", "type": "cdn"},
      {"service": "AWS SQS", "type": "queue"},
      {"service": "Redis", "type": "cache"}
    ],
    "quality_requirements": {
      "test_coverage": "≥80%",
      "performance": "p95 <200ms",
      "security": "Zero critical vulnerabilities"
    }
  }
}
```

---

## 🗺️ PHASE 2: PROTOCOL REQUIREMENT MAPPING

### Objective
Convert the analysis into a concrete list of protocols needed.

### Mapping Logic

#### Step 1: Check Existing Protocols

```
ALWAYS REUSE Protocols 01-05:
✅ 01: Client Proposal Generation (already done)
✅ 02: Client Discovery Initiation (already done)
✅ 03: Project Brief Creation (already done - source of this analysis)
✅ 04: Project Bootstrap (already done)
✅ 05: Bootstrap Your Project (already done)

CHECK if protocols 06-23 exist and match needs:
- IF Project Type == AI/ML
    → Check if AI-project-workflow/06-28 exist
    → Reuse if they match, generate if not
    
- ELSE IF Project Type == General SDLC
    → Check if .cursor/ai-driven-workflow/06-23 exist
    → Reuse if they match, generate if not
    
- ELSE
    → Generate custom protocols starting from 06
```

#### Step 2: Map Deliverables to Protocol Types

```python
# Pseudo-logic for mapping

MAPPING_RULES = {
    # Architecture & Design
    "API specification": "api-design-protocol",
    "API design": "api-design-protocol",
    "GraphQL schema": "api-design-protocol",
    
    "database schema": "database-schema-protocol",
    "data model": "database-schema-protocol",
    "migrations": "database-schema-protocol",
    
    "architecture": "technical-architecture-protocol",
    "system design": "technical-architecture-protocol",
    
    # Implementation
    "backend implementation": "backend-development-protocol",
    "API endpoints": "api-development-protocol",
    "business logic": "backend-development-protocol",
    
    "frontend": "frontend-development-protocol",
    "UI components": "ui-component-protocol",
    "React app": "frontend-development-protocol",
    
    "mobile app": "mobile-development-protocol",
    
    # Integrations (Pattern: "{service} integration")
    "Stripe": "payment-integration-protocol",
    "PayPal": "payment-integration-protocol",
    "AWS S3": "storage-integration-protocol",
    "CloudFront": "cdn-setup-protocol",
    "SQS": "queue-integration-protocol",
    "Redis": "caching-protocol",
    "Auth0": "authentication-protocol",
    
    # Quality & Testing
    "performance": "performance-optimization-protocol",
    "optimization": "performance-optimization-protocol",
    "load testing": "load-testing-protocol",
    
    "security": "security-audit-protocol",
    "vulnerability": "security-audit-protocol",
    "OWASP": "security-audit-protocol",
    
    "unit tests": "unit-testing-protocol",
    "integration tests": "integration-testing-protocol",
    "E2E tests": "e2e-testing-protocol",
    "test coverage": "test-coverage-protocol",
    
    # Deployment & Operations
    "CI/CD": "cicd-setup-protocol",
    "pipeline": "cicd-setup-protocol",
    "deployment": "deployment-protocol",
    "production": "production-deployment-protocol",
    
    "monitoring": "monitoring-protocol",
    "observability": "observability-protocol",
    "logging": "logging-protocol",
    
    "documentation": "documentation-protocol",
    "API docs": "api-documentation-protocol",
}

# Algorithm
protocols_needed = []

for deliverable in project_brief.deliverables:
    for keyword, protocol_type in MAPPING_RULES.items():
        if keyword.lower() in deliverable.lower():
            protocols_needed.append({
                "type": protocol_type,
                "reason": f"Deliverable: {deliverable}",
                "source": "Project Brief"
            })

# Remove duplicates
protocols_needed = deduplicate(protocols_needed)
```

#### Step 3: Determine Dependencies

```
Dependency Rules:

"api-development-protocol" depends on:
  - "api-design-protocol" (need spec first)
  - "database-schema-protocol" (need data model first)

"frontend-development-protocol" depends on:
  - "api-design-protocol" (need API contract first)

"payment-integration-protocol" depends on:
  - "backend-development-protocol" (need backend structure first)
  - "database-schema-protocol" (need transaction tables first)

"performance-optimization-protocol" depends on:
  - "backend-development-protocol" (need something to optimize)
  - "api-development-protocol" (need endpoints to measure)

"e2e-testing-protocol" depends on:
  - "frontend-development-protocol" (need UI to test)
  - "backend-development-protocol" (need backend to test)

"cicd-setup-protocol" depends on:
  - ALL implementation protocols (need something to deploy)

"production-deployment-protocol" depends on:
  - "cicd-setup-protocol" (need pipeline first)
  - "monitoring-protocol" (need monitoring before deploy)

# Use topological sort to determine order
protocol_order = topological_sort(protocols_needed, dependencies)
```

### Output of Phase 2

```json
{
  "protocol_plan": {
    "total_protocols": 18,
    "reused_protocols": [
      {"id": "01", "name": "Client Proposal Generation", "status": "complete"},
      {"id": "02", "name": "Client Discovery Initiation", "status": "complete"},
      {"id": "03", "name": "Project Brief Creation", "status": "complete"},
      {"id": "04", "name": "Project Bootstrap", "status": "complete"},
      {"id": "05", "name": "Bootstrap Your Project", "status": "complete"}
    ],
    "new_protocols": [
      {
        "id": "06",
        "type": "api-design-protocol",
        "name": "API Design & Specification",
        "reason": "Deliverable: API specification and design documentation",
        "dependencies": [],
        "inputs_from": ["03"],
        "outputs_to": ["07", "08", "09"]
      },
      {
        "id": "07",
        "type": "database-schema-protocol",
        "name": "Database Schema Design",
        "reason": "Deliverable: PostgreSQL database schema with migrations",
        "dependencies": [],
        "inputs_from": ["03", "06"],
        "outputs_to": ["08", "10"]
      },
      {
        "id": "08",
        "type": "backend-development-protocol",
        "name": "Go Backend Implementation",
        "reason": "Deliverable: Go backend structure with clean architecture",
        "dependencies": ["06", "07"],
        "inputs_from": ["06", "07"],
        "outputs_to": ["09", "10", "11"]
      },
      {
        "id": "09",
        "type": "frontend-development-protocol",
        "name": "Next.js Frontend Implementation",
        "reason": "Deliverable: Next.js frontend integration setup",
        "dependencies": ["06"],
        "inputs_from": ["06"],
        "outputs_to": ["19"]
      },
      {
        "id": "10",
        "type": "payment-integration-protocol",
        "name": "Stripe Payment Integration",
        "reason": "Integration: Stripe Connect",
        "dependencies": ["07", "08"],
        "inputs_from": ["07", "08"],
        "outputs_to": ["14"]
      },
      {
        "id": "11",
        "type": "storage-integration-protocol",
        "name": "AWS S3 Storage Integration",
        "reason": "Integration: AWS S3",
        "dependencies": ["08"],
        "inputs_from": ["08"],
        "outputs_to": ["12"]
      },
      {
        "id": "12",
        "type": "cdn-setup-protocol",
        "name": "AWS CloudFront CDN Setup",
        "reason": "Integration: AWS CloudFront",
        "dependencies": ["11"],
        "inputs_from": ["11"],
        "outputs_to": ["14"]
      },
      {
        "id": "13",
        "type": "queue-integration-protocol",
        "name": "AWS SQS Queue Integration",
        "reason": "Integration: AWS SQS",
        "dependencies": ["08"],
        "inputs_from": ["08"],
        "outputs_to": ["14"]
      },
      {
        "id": "14",
        "type": "api-development-protocol",
        "name": "Core API Endpoints Implementation",
        "reason": "Deliverable: Core API endpoints with business logic",
        "dependencies": ["06", "07", "08", "10"],
        "inputs_from": ["06", "07", "08", "10", "11", "12", "13"],
        "outputs_to": ["15", "16"]
      },
      {
        "id": "15",
        "type": "performance-optimization-protocol",
        "name": "Performance Profiling & Optimization",
        "reason": "Quality: p95 <200ms",
        "dependencies": ["14"],
        "inputs_from": ["14"],
        "outputs_to": ["18", "21"]
      },
      {
        "id": "16",
        "type": "security-audit-protocol",
        "name": "Security Audit & OWASP Compliance",
        "reason": "Quality: Zero critical vulnerabilities, OWASP Top 10",
        "dependencies": ["14"],
        "inputs_from": ["14"],
        "outputs_to": ["21"]
      },
      {
        "id": "17",
        "type": "authentication-protocol",
        "name": "JWT Authentication & Session Management",
        "reason": "Deliverable: Auth/session implementation",
        "dependencies": ["06", "07"],
        "inputs_from": ["06", "07"],
        "outputs_to": ["14"]
      },
      {
        "id": "18",
        "type": "caching-protocol",
        "name": "Redis Caching Layer",
        "reason": "Deliverable: Redis caching layer",
        "dependencies": ["14", "15"],
        "inputs_from": ["14", "15"],
        "outputs_to": ["21"]
      },
      {
        "id": "19",
        "type": "e2e-testing-protocol",
        "name": "Cypress E2E Test Suite",
        "reason": "Deliverable: Cypress E2E test suite",
        "dependencies": ["09", "14"],
        "inputs_from": ["09", "14"],
        "outputs_to": ["20"]
      },
      {
        "id": "20",
        "type": "test-coverage-protocol",
        "name": "Test Coverage Verification",
        "reason": "Quality: ≥80% test coverage",
        "dependencies": ["14", "19"],
        "inputs_from": ["14", "19"],
        "outputs_to": ["21"]
      },
      {
        "id": "21",
        "type": "cicd-setup-protocol",
        "name": "CI/CD Pipeline Setup",
        "reason": "Deliverable: CI/CD pipeline",
        "dependencies": ["14", "15", "16", "18", "20"],
        "inputs_from": ["14", "15", "16", "18", "20"],
        "outputs_to": ["22"]
      },
      {
        "id": "22",
        "type": "documentation-protocol",
        "name": "API Documentation & Deployment Guide",
        "reason": "Deliverable: API docs, deployment guide",
        "dependencies": ["14", "21"],
        "inputs_from": ["14", "21"],
        "outputs_to": ["23"]
      },
      {
        "id": "23",
        "type": "production-deployment-protocol",
        "name": "Production Deployment & Handoff",
        "reason": "Final deployment deliverable",
        "dependencies": ["21", "22"],
        "inputs_from": ["21", "22"],
        "outputs_to": []
      }
    ],
    "execution_order": [
      "06", "07", "08", "09", "10", "11", "12", "13", "17",
      "14", "15", "16", "18", "19", "20", "21", "22", "23"
    ]
  }
}
```

---

## 🏗️ PHASE 3: PROTOCOL GENERATION

### Objective
Generate each protocol following the MASTER RAY structure exactly.

### CRITICAL: 11-Validator System

**[STRICT]** Every generated protocol MUST pass ALL 11 validators with score ≥0.95

Located in: `/validators-system/scripts/`

#### The 11 Validators:

1. **validate_protocol_identity.py**
   - Validates: Protocol metadata, ID, name, version, classification
   - Checks: Required sections present, phase assignment, lineage
   
2. **validate_protocol_role.py**
   - Validates: AI role definition, mission statement, capabilities
   - Checks: Role clarity, decision authority, behavioral constraints
   
3. **validate_protocol_workflow.py**
   - Validates: Workflow steps, phases, execution sequence
   - Checks: Step completeness, validation points, halt conditions
   
4. **validate_protocol_gates.py**
   - Validates: Quality gates, thresholds, measurement methods
   - Checks: Gate definitions, pass criteria, automation
   
5. **validate_protocol_scripts.py**
   - Validates: Automation script references, registry compliance
   - Checks: Script existence, purpose, integration
   
6. **validate_protocol_communication.py**
   - Validates: Status announcements, error messages
   - Checks: Communication templates, announcement format
   
7. **validate_protocol_evidence.py**
   - Validates: Evidence artifacts, manifest completeness
   - Checks: Artifact requirements, storage locations, formats
   
8. **validate_protocol_handoff.py**
   - Validates: Handoff checklist, deliverables, integration points
   - Checks: Pre-handoff validation, downstream compatibility
   
9. **validate_protocol_reasoning.py**
   - Validates: Decision logic, reasoning patterns
   - Checks: Decision documentation, rationale clarity
   
10. **validate_protocol_reflection.py**
    - Validates: Continuous improvement, lessons learned
    - Checks: Reflection quality, optimization tracking
    
11. **validate_all_protocols.py** (Master Orchestrator)
    - Runs all 10 validators
    - Aggregates scores
    - Generates master validation report
    - Output: `.artifacts/validation/protocol-{ID}-master-report.json`

#### Validation Command:

```bash
python validators-system/scripts/validate_all_protocols.py \
  --workspace /path/to/workspace \
  --protocol-dir AI-project-workflow \
  --protocol-id 06
```

#### Required Score:

```
Overall Score: ≥0.95 (out of 1.0)
Status: PASS
All 10 individual validators: ≥0.95 each
```

If score <0.95 → Protocol MUST be regenerated/fixed!

---

### CRITICAL: Script Registry System

**[STRICT]** Protocols reference automation scripts. Scripts can be REUSED or CREATED.

Located in: `/scripts/script-registry.json`

#### Script Strategy:

**Option 1: REUSE Existing Scripts**
```
Check script-registry.json for existing scripts:
- protocol-gates: Gate validation scripts
- evidence-aggregation: Evidence collection scripts
- protocol-validators: Quality gate validators
- protocol-automation: Protocol-specific automation

If match found:
  → Reference existing script in protocol
  → Verify script is registered
  → Document script purpose in protocol
```

**Option 2: CREATE New Scripts**
```
If no existing script matches:
  → Design new script for protocol needs
  → Create script file in scripts/{category}/
  → Register in script-registry.json
  → Document in protocol AUTOMATION HOOKS section

New Script Template:
{
  "script_name": {
    "path": "scripts/{category}/{script_name}.py",
    "protocol": "{protocol_id}",
    "purpose": "{what it automates}",
    "owner": "Protocol Generation System",
    "status": "active",
    "dependencies": ["python3", "..."],
    "version": "1.0"
  }
}
```

#### Script Registry Structure:

```json
{
  "protocol-gates": {
    "gate-runner": "scripts/run_protocol_gates.py",
    "protocol-01-validators": ["scripts/validate_gate_01_*.py"],
    "protocol-02-validators": ["scripts/validate_gate_02_*.py"]
  },
  "evidence-aggregation": {
    "scripts": ["scripts/aggregate_evidence_*.py"]
  },
  "protocol-automation": {
    "protocol-06": {
      "automation-scripts": ["scripts/generate_prd_assets.py"]
    }
  }
}
```

#### Decision Logic for Scripts:

```python
def determine_scripts(protocol_spec, script_registry):
    """
    Determine which scripts to use for this protocol
    """
    scripts_needed = []
    
    # Check for existing scripts by protocol type
    protocol_type = protocol_spec["type"]
    
    if protocol_type in script_registry["protocol-automation"]:
        # Reuse existing scripts
        existing = script_registry["protocol-automation"][protocol_type]
        scripts_needed.extend(existing["automation-scripts"])
    else:
        # Generate new script specs
        new_scripts = generate_script_specs(protocol_spec)
        scripts_needed.extend(new_scripts)
    
    return scripts_needed
```

#### Minimum Scripts Per Protocol:

**[GUIDELINE]** Most protocols should have at least 2-3 automation scripts:
- 1 script for main automation task
- 1 script for validation/verification
- 1 script for evidence generation (optional)

**Examples:**
- API Design Protocol: `generate_openapi_spec.py`, `validate_api_design.py`
- Database Schema Protocol: `generate_migrations.py`, `validate_schema.py`
- Performance Protocol: `profile_api_performance.py`, `generate_performance_report.py`

---

### The MASTER RAY Protocol Structure (STRICT)

Every protocol MUST have these sections in this order:

```markdown
---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL {ID}: {NAME}

## IDENTITY & OWNERSHIP

### Protocol Identity
- **Protocol ID:** {number}
- **Protocol Name:** {descriptive name}
- **Protocol Owner:** {role}
- **Owner Contact:** [Email/Slack]
- **Created:** {date}
- **Last Updated:** {date}
- **Version:** {version}

### Protocol Classification
- **Category:** {Execution|Documentation|Quality|etc}
- **Criticality:** {High|Medium|Low}
- **Complexity:** {High|Medium|Low}
- **Scope:** Module

### Protocol Lineage
- **Predecessor:** Protocol {X}
- **Successor:** Protocol {Y}
- **Related Protocols:** {list}

### Protocol Metadata
- **Purpose:** {one sentence purpose}
- **Success Criteria:** {what defines success}
- **Failure Modes:** {what can go wrong}
- **Recovery Procedure:** {how to recover}

---

## ROLES & RESPONSIBILITIES

### Primary Roles

#### Protocol Executor
- **Role:** {role name}
- **Responsibilities:** {list}
- **Authority:** {what they can decide}
- **Escalation:** {who to escalate to}

#### Protocol Owner
- **Role:** {role name}
- **Responsibilities:** {list}
- **Authority:** {what they can decide}

#### Downstream Owner
- **Role:** {next protocol owner}
- **Responsibilities:** {list}
- **Authority:** {what they can decide}

### Role Interactions
- **Executor → Owner:** {interaction pattern}
- **Owner → Downstream:** {handoff process}
- **Downstream → Executor:** {feedback loop}

### Decision Authority Matrix
| Decision Type | Executor | Owner | Downstream | Executive |
|---------------|----------|-------|------------|-----------|
| {Decision 1}  | ✅/❌    | ✅/❌  | ✅/❌       | ✅/❌      |

---

## PREREQUISITES

### Required Artifacts
- **`[MUST]`** {artifact name} from Protocol {X} - {purpose}
- **`[MUST]`** {artifact name} from Protocol {Y} - {purpose}

### Required Approvals
- **`[MUST]`** {approval type from whom}

### System State Requirements
- **`[MUST]`** {system requirement}

If any prerequisite fails, pause and resolve before continuing.

---

## AI ROLE AND MISSION

You are a **{Role Name}**. Your mission is to {mission statement}.

**🚫 [CRITICAL] {critical constraint}**

### Core Capabilities
- {capability 1}
- {capability 2}

### Behavioral Constraints
- **[STRICT]** {strict constraint}
- **[GUIDELINE]** {guideline constraint}

### Decision Authority
- **Autonomous:** {what AI can decide alone}
- **Requires Approval:** {what needs human approval}

---

## WORKFLOW

### STEP 1: {Step Name}
### PHASE 1: {Phase Name}
<!-- [Category: EXECUTION-{VARIANT}] -->
<!-- Why: {reasoning for this variant} -->

**[REASONING]:**
- **Decision Logic:** {decision tree or heuristic}
- **Pattern Applied:** {pattern name and explanation}

1. **`[MUST]` {Action Name}:**
   * **Action:** {what to do}
   * **Communication:** 
     > "[MASTER RAY™ | PHASE {N} START] - {status message}"
   * **Evidence:** `.artifacts/protocol-{ID}/{artifact-name}`
   * **Validation:** {how to verify}
   * **Halt condition:** {when to stop}

[Repeat for all steps in phase]

[Repeat PHASE for all workflow phases]

---

## QUALITY GATES

### Gate 1: {Gate Name}
- **Type:** {boolean|numeric|percentage}
- **Threshold:** {specific threshold}
- **Blocking:** {true|false}
- **Measurement:** {how to measure}
- **Evidence:** {artifact that proves it}

[Minimum 3 gates per protocol]

---

## EVIDENCE SUMMARY

### Required Artifacts
- `.artifacts/protocol-{ID}/{artifact-1}.{ext}` - {purpose}
- `.artifacts/protocol-{ID}/{artifact-2}.{ext}` - {purpose}
- `.artifacts/protocol-{ID}/{artifact-3}.{ext}` - {purpose}

[Minimum 3 artifacts per protocol]

### Artifact Structure
{describe the expected format/structure}

---

## COMMUNICATION PROTOCOLS

### Status Announcements
```
[PROTOCOL {ID} | PHASE {N} START] - {description}
[MILESTONE ACHIEVED: {milestone}]
[QUALITY GATE PASSED: Gate {N}]
[PROTOCOL {ID} | PHASE {N} COMPLETE]
```

### Error Announcements
```
[PROTOCOL {ID} | GATE {N} FAILED: {reason}]
[PROTOCOL {ID} | BLOCKED: {reason}]
```

---

## HANDOFF CHECKLIST

### Pre-handoff Validation
- [ ] All quality gates passed
- [ ] Evidence artifacts generated
- [ ] Automation scripts executed
- [ ] Integration points validated
- [ ] Documentation complete

### Handoff Deliverables
- [ ] {specific deliverable 1}
- [ ] {specific deliverable 2}
- [ ] {specific deliverable 3}

[Minimum 5 checklist items total]

---

## SCRIPT INTEGRATION (Optional)

### Automation Scripts Reference
- `scripts/{category}/{script_name}.py` - {purpose}

---

## INTEGRATION POINTS

### Inputs From
- **Protocol {X}:** {what data/artifacts}
  - Format: {expected format}
  - Location: {artifact path}

### Outputs To
- **Protocol {Y}:** {what data/artifacts}
  - Format: {output format}
  - Location: {artifact path}

---

## REASONING & REFLECTION

### Decision Logic
- **{Decision Point}:** {reasoning with project context}

### Continuous Improvement
- **Lessons Learned:** {capture space}
- **Optimization Opportunities:** {improvement ideas}
- **Technical Debt:** {known issues}
```

### Context Injection Rules

When generating each protocol section:

#### 1. Identity & Ownership
```
AUTO-INJECT from Project Brief:
- Protocol Name: Based on deliverable name
- Protocol Owner: From role in Project Brief
- Created Date: Current date
- Version: 1.0
```

#### 2. Prerequisites
```
AUTO-INJECT from Project Brief:
- Required Artifacts: From previous protocol outputs
- System Requirements: From tech stack in Project Brief
```

#### 3. AI Role and Mission
```
AUTO-INJECT from Project Brief:
- Role Name: Match to deliverable type
- Mission: Specific to this project's goals
- Constraints: From Project Brief constraints

Example:
- If deliverable = "API specification"
  → Role = "API Architect"
  → Mission = "Design RESTful API for {project_name} supporting {features}"
```

#### 4. Workflow Steps
```
AUTO-INJECT from Project Brief:
- Step actions: Specific to tech stack
- Evidence paths: Use actual project paths
- Validation criteria: From success criteria in Project Brief

Example:
- If tech stack = Go + PostgreSQL
  → Generate Go-specific steps
  → Reference PostgreSQL-specific validation
```

#### 5. Quality Gates
```
AUTO-INJECT from Project Brief:
- Thresholds: From success criteria
- Metrics: From quality requirements

Example:
- If "test coverage ≥80%"
  → Gate: Test Coverage ≥80%
  → Measurement: go test -cover
```

### Generation Algorithm

```python
def generate_protocol(protocol_spec, project_brief):
    """
    Generate a single protocol following MASTER RAY structure
    """
    
    protocol = {}
    
    # SECTION 1: Identity & Ownership
    protocol["identity"] = {
        "id": protocol_spec["id"],
        "name": protocol_spec["name"],
        "owner": infer_owner_role(protocol_spec["type"]),
        "created": datetime.now(),
        "version": "1.0",
        "category": infer_category(protocol_spec["type"]),
        "criticality": infer_criticality(protocol_spec["dependencies"]),
        "complexity": infer_complexity(protocol_spec["type"]),
        "predecessor": protocol_spec["dependencies"][0] if protocol_spec["dependencies"] else "Protocol 05",
        "successor": protocol_spec["outputs_to"][0] if protocol_spec["outputs_to"] else "Protocol XX",
        "purpose": f"{protocol_spec['reason']} for {project_brief['project_name']}",
        "success_criteria": generate_success_criteria(protocol_spec, project_brief)
    }
    
    # SECTION 2: Roles & Responsibilities
    protocol["roles"] = generate_roles(protocol_spec["type"])
    
    # SECTION 3: Prerequisites
    protocol["prerequisites"] = {
        "artifacts": generate_prerequisites(protocol_spec["inputs_from"], protocol_spec["dependencies"]),
        "approvals": generate_approvals(protocol_spec["type"]),
        "system_state": generate_system_requirements(project_brief["tech_stack"])
    }
    
    # SECTION 4: AI Role and Mission
    protocol["ai_role"] = {
        "role": infer_ai_role(protocol_spec["type"]),
        "mission": generate_mission(protocol_spec, project_brief),
        "constraints": generate_constraints(protocol_spec["type"]),
        "capabilities": generate_capabilities(protocol_spec["type"]),
        "decision_authority": generate_decision_authority(protocol_spec["type"])
    }
    
    # SECTION 5: Workflow
    protocol["workflow"] = generate_workflow_steps(
        protocol_spec["type"],
        project_brief["tech_stack"],
        project_brief["deliverables"]
    )
    
    # SECTION 6: Quality Gates
    protocol["quality_gates"] = generate_quality_gates(
        protocol_spec["type"],
        project_brief["quality_requirements"]
    )
    
    # SECTION 7: Evidence Summary
    protocol["evidence"] = generate_evidence_requirements(protocol_spec["id"], protocol_spec["type"])
    
    # SECTION 8: Communication Protocols
    protocol["communication"] = generate_communication_templates(protocol_spec["id"])
    
    # SECTION 9: Handoff Checklist
    protocol["handoff"] = generate_handoff_checklist(protocol_spec["type"], protocol_spec["outputs_to"])
    
    # SECTION 10: Script Integration (Optional)
    protocol["scripts"] = generate_script_references(protocol_spec["type"])
    
    # SECTION 11: Integration Points
    protocol["integration"] = {
        "inputs": generate_input_specs(protocol_spec["inputs_from"]),
        "outputs": generate_output_specs(protocol_spec["outputs_to"])
    }
    
    # SECTION 12: Reasoning & Reflection
    protocol["reasoning"] = generate_reasoning_template(protocol_spec["type"])
    
    return protocol
```

---

## ✅ VALIDATION WORKFLOW (MANDATORY)

### The Validation Cycle

After generating each protocol, IMMEDIATELY validate:

```
┌─────────────────────────────────────────────┐
│  1. Generate Protocol                       │
│     - All 12 sections complete              │
│     - Context injected                      │
│     - Scripts referenced                    │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  2. Run Validation                          │
│     python validate_all_protocols.py \      │
│       --protocol-id {ID}                    │
└─────────────────────────────────────────────┘
                    ↓
        ┌───────────┴───────────┐
        │                       │
        ↓                       ↓
┌───────────────┐      ┌───────────────┐
│  PASS         │      │  FAIL         │
│  Score ≥0.95  │      │  Score <0.95  │
└───────────────┘      └───────────────┘
        │                       │
        ↓                       ↓
┌───────────────┐      ┌───────────────────────────┐
│ Save protocol │      │ Analyze failing validators│
│ Mark validated│      │ - Identity issues?        │
│ Proceed next  │      │ - Workflow incomplete?    │
└───────────────┘      │ - Gates unclear?          │
                       │ - Scripts missing?        │
                       └───────────────────────────┘
                                ↓
                       ┌───────────────────────────┐
                       │ Fix Protocol Issues       │
                       │ - Add missing sections    │
                       │ - Clarify quality gates   │
                       │ - Complete workflow steps │
                       │ - Add script references   │
                       └───────────────────────────┘
                                ↓
                       ┌───────────────────────────┐
                       │ Re-run Validation         │
                       │ (Repeat until PASS)       │
                       └───────────────────────────┘
```

### Common Validation Failures & Fixes

#### 1. Identity Validator Failure (<0.95)

**Common Issues:**
- Missing required sections
- Incomplete protocol metadata
- Phase assignment incorrect

**Fixes:**
```python
# Ensure all required sections present
REQUIRED_SECTIONS = [
    "PREREQUISITES",
    "AI ROLE AND MISSION",
    "WORKFLOW",
    "INTEGRATION POINTS",
    "QUALITY GATES",
    "COMMUNICATION PROTOCOLS",
    "AUTOMATION HOOKS",
    "HANDOFF CHECKLIST",
    "EVIDENCE SUMMARY"
]

# Add missing sections with proper format
```

#### 2. Workflow Validator Failure (<0.95)

**Common Issues:**
- Steps lack validation criteria
- Missing halt conditions
- Incomplete communication announcements

**Fixes:**
```markdown
Every workflow step MUST have:

1. **`[MUST]` Action Name:**
   * **Action:** {what to do}
   * **Communication:** 
     > "[MASTER RAY™ | PHASE {N} START] - {message}"
   * **Evidence:** .artifacts/protocol-{ID}/{artifact}
   * **Validation:** {how to verify success}
   * **Halt condition:** {when to stop if failure}
```

#### 3. Quality Gates Validator Failure (<0.95)

**Common Issues:**
- Gates not measurable
- Missing thresholds
- No measurement method defined

**Fixes:**
```markdown
Every gate MUST have:

### Gate 1: {Specific Metric Name}
- **Type:** boolean | numeric | percentage
- **Threshold:** {exact threshold value}
- **Blocking:** true | false
- **Measurement:** {specific measurement method}
- **Evidence:** {artifact that proves it}

Example (GOOD):
### Gate 1: Test Coverage ≥80%
- **Type:** percentage
- **Threshold:** ≥80%
- **Blocking:** true
- **Measurement:** go test -cover or jest --coverage
- **Evidence:** .artifacts/protocol-14/coverage-report.json

Example (BAD):
### Gate 1: Good Test Coverage
- No type specified
- No threshold
- "Good" is not measurable
```

#### 4. Scripts Validator Failure (<0.95)

**Common Issues:**
- Scripts referenced but not in registry
- Script purpose unclear
- No automation hooks section

**Fixes:**
```markdown
Add AUTOMATION HOOKS section:

## SCRIPT INTEGRATION

### Automation Scripts Reference
- `scripts/{category}/{script_name}.py` - {specific purpose}
  - Protocol: {ID}
  - Inputs: {what it needs}
  - Outputs: {what it produces}
  - Registry: scripts/script-registry.json

Then update script-registry.json:
{
  "script_name": {
    "path": "scripts/{category}/{script_name}.py",
    "protocol": "{ID}",
    "purpose": "{purpose}",
    "status": "active"
  }
}
```

#### 5. Evidence Validator Failure (<0.95)

**Common Issues:**
- Artifact paths not specified
- Less than 3 artifacts defined
- No artifact structure documented

**Fixes:**
```markdown
## EVIDENCE SUMMARY

### Required Artifacts
- `.artifacts/protocol-{ID}/artifact-1.{ext}` - {purpose}
- `.artifacts/protocol-{ID}/artifact-2.{ext}` - {purpose}
- `.artifacts/protocol-{ID}/artifact-3.{ext}` - {purpose}

[Minimum 3 artifacts required]

### Artifact Structure
{describe expected format/content}
```

### Validation Report Interpretation

```json
{
  "protocol_id": "06",
  "overall_score": 0.94,
  "validation_status": "fail",
  "validators": {
    "protocol_identity": {"status": "pass", "score": 0.98},
    "protocol_role": {"status": "pass", "score": 0.96},
    "protocol_workflow": {"status": "pass", "score": 0.95},
    "protocol_quality_gates": {"status": "fail", "score": 0.88},
    "protocol_scripts": {"status": "pass", "score": 0.97},
    "protocol_communication": {"status": "pass", "score": 0.96},
    "protocol_evidence": {"status": "fail", "score": 0.92},
    "protocol_handoff": {"status": "pass", "score": 0.95},
    "protocol_reasoning": {"status": "pass", "score": 0.96},
    "protocol_reflection": {"status": "pass", "score": 0.95}
  },
  "issues": [
    {
      "validator": "protocol_quality_gates",
      "severity": "high",
      "issue": "Gate 2 lacks measurable threshold"
    },
    {
      "validator": "protocol_evidence",
      "severity": "medium",
      "issue": "Only 2 artifacts defined, minimum 3 required"
    }
  ]
}
```

**Action Plan:**
1. Focus on failing validators (score <0.95)
2. Read issues array for specific problems
3. Fix identified issues
4. Re-run validation
5. Repeat until overall_score ≥0.95

### Validation Best Practices

✅ **DO:**
- Run validation immediately after generation
- Fix issues before moving to next protocol
- Save validation reports for audit trail
- Document what was fixed and why

❌ **DON'T:**
- Skip validation because "it looks good"
- Proceed with failed protocols
- Ignore warnings (they often become errors)
- Generate all protocols then validate (validate incrementally)

---

## 🎯 PHASE 4: CONTEXT-AWARE CREATION

### The "No Redundant Questions" Principle

When creating each protocol:

#### What AI Already Knows (DON'T ASK)
```
From Protocol 03 (Project Brief):
✅ Project name and objectives
✅ Tech stack (languages, frameworks, databases)
✅ Timeline and milestones
✅ Budget and resources
✅ Success criteria
✅ Quality requirements
✅ Integration requirements
✅ Constraints and assumptions

From Protocol 02 (Discovery):
✅ Client preferences
✅ Communication style
✅ Risk factors
✅ Stakeholder information

From Protocol 01 (Proposal):
✅ Pricing structure
✅ Deliverable commitments
✅ Client expectations
```

#### What AI Might Need to Ask (MINIMAL)
```
Protocol-Specific Details ONLY:

Example for Protocol 06 (API Design):
- "API versioning strategy: /v1/ prefix or header?"
- "Rate limiting: requests per minute?"
- "Pagination: offset-based or cursor-based?"

Example for Protocol 10 (Stripe Integration):
- "Stripe webhooks: which events to handle?"
- "Payment flow: one-time or subscription?"
- "Error handling: retry strategy?"

MAX 3-5 questions per protocol!
```

#### Context Injection Strategy

```python
def inject_project_context(protocol_template, project_brief):
    """
    Replace generic placeholders with project-specific values
    """
    
    context_map = {
        # From Project Brief
        "{project_name}": project_brief["name"],
        "{backend_language}": project_brief["tech_stack"]["backend"][0],
        "{frontend_framework}": project_brief["tech_stack"]["frontend"][0],
        "{database}": project_brief["tech_stack"]["database"],
        "{cloud_provider}": project_brief["infrastructure"]["cloud"],
        
        # From Quality Requirements
        "{test_coverage_target}": project_brief["quality"]["test_coverage"],
        "{performance_target}": project_brief["quality"]["performance"],
        "{security_requirement}": project_brief["quality"]["security"],
        
        # From Timeline
        "{project_duration}": project_brief["timeline"]["duration"],
        "{milestone_count}": len(project_brief["timeline"]["milestones"]),
        
        # Inferred Context
        "{test_framework}": infer_test_framework(project_brief["tech_stack"]),
        "{coverage_tool}": infer_coverage_tool(project_brief["tech_stack"]),
        "{ci_cd_platform}": infer_cicd_platform(project_brief),
    }
    
    # Replace all placeholders
    for placeholder, value in context_map.items():
        protocol_template = protocol_template.replace(placeholder, str(value))
    
    return protocol_template
```

---

## 📊 COMPLETE WORKFLOW EXAMPLE

### Input: Go + Next.js SaaS Project Brief

```markdown
# Project Brief
- **Project:** Early-Stage SaaS Platform
- **Backend:** Go 1.21+, PostgreSQL 15+
- **Frontend:** Next.js 14+, TypeScript
- **Infrastructure:** AWS (S3, CloudFront, SQS), Redis
- **Integrations:** Stripe, AWS services
- **Quality:** Test coverage ≥80%, p95 <200ms, Zero critical vulns
- **Timeline:** 4 months
- **Deliverables:** 
  - API specification
  - Database schema
  - Stripe integration
  - AWS S3/CloudFront/SQS integration
  - Performance optimization
  - Security audit
  - E2E tests
  - CI/CD pipeline
  - Documentation
```

### Step 1: Analysis Output

```json
{
  "project_type": "Full-Stack SaaS",
  "protocols_needed": 18,
  "specific_protocols": [
    "api-design", "database-schema", "backend-dev", "frontend-dev",
    "stripe-integration", "s3-integration", "cloudfront-setup", 
    "sqs-integration", "api-endpoints", "performance-opt", 
    "security-audit", "auth-implementation", "redis-cache",
    "e2e-testing", "test-coverage", "cicd-setup", 
    "documentation", "production-deploy"
  ]
}
```

### Step 2: Protocol 06 Generation (Example)

```markdown
---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 06: API DESIGN & SPECIFICATION

## IDENTITY & OWNERSHIP

### Protocol Identity
- **Protocol ID:** 06
- **Protocol Name:** API Design & Specification
- **Protocol Owner:** API Architect
- **Created:** 2025-11-07
- **Version:** 1.0

### Protocol Classification
- **Category:** Documentation
- **Criticality:** High
- **Complexity:** Medium
- **Scope:** Module

### Protocol Lineage
- **Predecessor:** Protocol 05 (Bootstrap Your Project)
- **Successor:** Protocol 07 (Database Schema Design), Protocol 08 (Backend Implementation)

### Protocol Metadata
- **Purpose:** Design RESTful API specification for Early-Stage SaaS Platform
- **Success Criteria:** OpenAPI spec approved, JWT auth designed, performance targets documented
- **Failure Modes:** Incomplete spec, unclear endpoints, missing auth design
- **Recovery Procedure:** Return to requirements, clarify with stakeholders, regenerate spec

---

## PREREQUISITES

### Required Artifacts
- **`[MUST]`** `PROJECT-BRIEF.md` from Protocol 03 - Business requirements and success criteria
- **`[MUST]`** `architecture-principles.md` from Protocol 05 - Technical constraints

### Required Approvals
- **`[MUST]`** Technical lead approval for API architecture approach

### System State Requirements
- **`[MUST]`** OpenAPI spec generation tools available
- **`[MUST]`** API design templates in `.templates/api/`

---

## AI ROLE AND MISSION

You are an **API Architect** specializing in RESTful API design for Go-based systems. Your mission is to create a comprehensive API specification for the Early-Stage SaaS Platform that supports user authentication, product management, and order processing with JWT-based auth and <200ms p95 response time targets.

**🚫 [CRITICAL] DO NOT design endpoints without understanding data model requirements first.**

### Core Capabilities
- RESTful API design following Go best practices
- OpenAPI 3.0 specification generation
- JWT authentication architecture
- Performance-oriented endpoint design
- API versioning strategy

### Behavioral Constraints
- **[STRICT]** Must validate all endpoints against performance targets (p95 <200ms)
- **[STRICT]** Must design for PostgreSQL 15+ as primary database
- **[GUIDELINE]** Follow REST conventions for resource naming
- **[GUIDELINE]** Include rate limiting in design

---

## WORKFLOW

### STEP 1: Requirements Analysis
### PHASE 1: Requirements Analysis

1. **`[MUST]` Extract API Requirements from Project Brief:**
   * **Action:** Identify all API-related requirements and success criteria
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Analyzing API requirements from Project Brief..."
   * **Evidence:** `.artifacts/protocol-06/api-requirements-summary.md`
   * **Validation:** All functional requirements mapped to potential endpoints
   * **Halt condition:** Stop if requirements unclear or conflicting

2. **`[MUST]` Identify Resource Models:**
   * **Action:** Extract domain entities (Users, Products, Orders, etc.) from requirements
   * **Communication:** 
     > "[PHASE 1] Identifying resource models and relationships..."
   * **Evidence:** `.artifacts/protocol-06/resource-models.yaml`
   * **Validation:** All resources have clear CRUD operations defined

[... continue with complete workflow ...]

---

## QUALITY GATES

### Gate 1: API Specification Complete
- **Type:** boolean
- **Threshold:** 100% of identified resources have endpoint definitions
- **Blocking:** true
- **Measurement:** Manual review of OpenAPI spec completeness
- **Evidence:** `.artifacts/protocol-06/openapi-spec.yaml`

### Gate 2: Performance Design Review
- **Type:** boolean
- **Threshold:** All endpoints designed to meet p95 <200ms target
- **Blocking:** true
- **Measurement:** Architecture review with performance analysis
- **Evidence:** `.artifacts/protocol-06/performance-design-analysis.md`

### Gate 3: Security Design Approved
- **Type:** boolean
- **Threshold:** JWT auth design and secure endpoints approved by technical lead
- **Blocking:** true
- **Measurement:** Security architecture review
- **Evidence:** `.artifacts/protocol-06/security-design-approval.json`

---

[... continue with all other sections ...]
```

---

## 🚀 IMPLEMENTATION STRATEGY FOR AI AGENTS

### For Windsurf/Claude/Cursor

When implementing this system:

#### Phase 1: Build the Analyzer
```
Input: PROJECT-BRIEF.md
Output: project_analysis.json

Tasks:
1. Read and parse PROJECT-BRIEF.md
2. Extract project type, tech stack, deliverables, timeline
3. Identify integration requirements
4. Extract quality requirements
5. Generate structured analysis JSON
```

#### Phase 2: Build the Mapper
```
Input: project_analysis.json
Output: protocol_plan.json

Tasks:
1. Load mapping rules (deliverable → protocol type)
2. Match deliverables to protocol types
3. Determine dependencies using dependency rules
4. Run topological sort for execution order
5. Generate complete protocol plan JSON
```

#### Phase 3: Build the Generator
```
Input: protocol_plan.json + PROJECT-BRIEF.md + script-registry.json
Output: Individual protocol .md files

Tasks:
1. For each protocol in plan:
   a. Load appropriate protocol template/structure
   b. Inject project-specific context
   c. Determine automation scripts (reuse or create)
   d. Generate all 12 sections
   e. Write to AI-project-workflow/{ID}-{name}.md
2. Update script-registry.json with new scripts
3. Create protocol registry
4. Generate handoff artifacts
```

#### Phase 4: Build the Validator (MANDATORY)
```
Input: Generated protocol files
Output: validation_report.json (score ≥0.95 REQUIRED)

Tasks:
1. Run validate_all_protocols.py for each generated protocol
2. Check overall score ≥0.95
3. If PASS:
   - Save validation report
   - Mark protocol as validated
   - Proceed to next protocol
4. If FAIL:
   - Identify failing validators
   - Fix protocol issues
   - Re-run validation
   - Repeat until PASS
5. Generate master validation report

BLOCKING: Cannot proceed with protocol execution if validation fails!
```

#### Phase 5: Build the Script Generator (Optional)
```
Input: New script specifications from Phase 3
Output: Script stub files + registry updates

Tasks:
1. For each new script needed:
   a. Generate Python script template
   b. Add docstring with purpose and protocol ID
   c. Add placeholder implementation
   d. Save to scripts/{category}/{script_name}.py
2. Update script-registry.json with new entries
3. Generate script documentation
```

---

## 💡 KEY DESIGN PRINCIPLES

### 1. Intelligence Over Templates
```
❌ BAD: Use fixed template with placeholders
✅ GOOD: Analyze project and generate contextual content

Example:
❌ "Implement {language} backend with {database}"
✅ "Implement Go 1.21+ backend with gorilla/mux routing, 
    connecting to PostgreSQL 15+ with lib/pq driver,
    targeting p95 <200ms response times for all endpoints"
```

### 2. Context Over Questions
```
❌ BAD: Ask user for info already in Project Brief
✅ GOOD: Extract from existing artifacts

Example:
❌ "What database are you using?"
✅ Read from PROJECT-BRIEF.md: "PostgreSQL 15+"
```

### 3. Specificity Over Generality
```
❌ BAD: Generic protocol that could apply to any project
✅ GOOD: Protocol specific to THIS project's requirements

Example:
❌ "Test the application"
✅ "Run Cypress E2E tests covering authentication, 
    product catalog, and checkout flows to achieve 
    ≥80% coverage target specified in Project Brief"
```

### 4. Traceability Over Assumptions
```
❌ BAD: Generate requirements without justification
✅ GOOD: Every requirement traces back to Project Brief

Example:
✅ Quality Gate: "Test Coverage ≥80%"
   Reason: "From Project Brief success criteria (line 47)"
```

### 5. Reusability Over Duplication
```
❌ BAD: Regenerate protocols 01-05 every time
✅ GOOD: Always reuse existing protocols, only generate new ones

Example:
✅ Protocols 01-05: Always reused (foundation)
✅ Protocols 06-23: Check if existing SDLC protocols match
✅ Protocols 06-28: Generate if AI/ML project needs them
```

---

## 🎯 SUCCESS CRITERIA

This system is successful if:

✅ **Completeness**: Generates ALL needed protocols (no gaps)
✅ **Accuracy**: Protocols match project requirements exactly
✅ **Structure**: Follows MASTER RAY structure perfectly
✅ **Context**: No generic placeholders, all project-specific
✅ **Dependencies**: Correct execution order determined
✅ **Traceability**: Every protocol element traces to Project Brief
✅ **Efficiency**: Minimal questions (≤5 per protocol)
✅ **Reusability**: Reuses existing protocols when appropriate
✅ **Validation**: ALL protocols pass 11 validators with score ≥0.95
✅ **Script Integration**: Scripts properly referenced or created and registered
✅ **Quality Assurance**: Zero validation failures before protocol execution

---

## 📚 REFERENCE EXAMPLES

### Example 1: AI/ML Project
```
Input: Project Brief mentions "machine learning", "model training", "dataset"
Output: Generate Protocols 06-28 for AI/ML lifecycle
Reuse: Protocols 01-05 (foundation)
Generate: 06-ai-use-case-definition through 28-ai-project-retrospective
```

### Example 2: Mobile App Project
```
Input: Project Brief mentions "React Native", "iOS", "Android", "mobile"
Output: Generate mobile-specific protocols
Reuse: Protocols 01-05 (foundation)
Generate: 
  - 06-mobile-architecture-design
  - 07-mobile-ui-component-development
  - 08-native-module-integration
  - 09-mobile-api-integration
  - 10-mobile-performance-optimization
  - 11-ios-app-store-submission
  - 12-android-play-store-submission
  - ...
```

### Example 3: Infrastructure Project
```
Input: Project Brief mentions "Kubernetes", "Terraform", "AWS", "DevOps"
Output: Generate infrastructure protocols
Reuse: Protocols 01-05 (foundation)
Generate:
  - 06-infrastructure-architecture-design
  - 07-terraform-infrastructure-as-code
  - 08-kubernetes-cluster-setup
  - 09-ci-cd-pipeline-configuration
  - 10-monitoring-observability-setup
  - 11-security-compliance-audit
  - ...
```

---

## 🔄 ITERATION & IMPROVEMENT

### Feedback Loop

After each protocol generation:

1. **Capture Metrics**
   - Time to generate
   - Questions asked
   - Context injection accuracy
   - Validation pass rate

2. **Identify Patterns**
   - Common deliverable types
   - Frequent dependencies
   - Recurring quality gates

3. **Improve Mapping Rules**
   - Add new deliverable → protocol mappings
   - Refine dependency rules
   - Update context injection templates

4. **Expand Protocol Library**
   - Create new protocol types as patterns emerge
   - Document successful protocol structures
   - Build reusable protocol templates

---

## 🎬 CONCLUSION

This system transforms the protocol generation process from:

**BEFORE:**
- Fixed protocol sequences (01-23, 06-28)
- Manual protocol creation
- Generic content
- Time-consuming
- Error-prone

**AFTER:**
- Dynamic protocol generation
- Automated based on Project Brief
- Project-specific content
- Fast and efficient
- Traceable and accurate

**Key Innovation**: The system READS the Project Brief and GENERATES exactly what's needed - no more, no less.

---

## 📊 COMPLETE WORKFLOW SUMMARY (WITH VALIDATION & SCRIPTS)

### End-to-End Process

```
USER ACTION: "Analyze Project Brief and Generate Protocol Plan"
                           ↓
┌─────────────────────────────────────────────────────────┐
│ PHASE 1: INTELLIGENT ANALYSIS                           │
│ ├─ Read PROJECT-BRIEF.md                                │
│ ├─ Extract project type, tech stack, deliverables       │
│ ├─ Identify integrations and quality requirements       │
│ └─ Output: project_analysis.json                        │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ PHASE 2: PROTOCOL REQUIREMENT MAPPING                   │
│ ├─ Map deliverables → protocol types                    │
│ ├─ Check existing protocols for reuse                   │
│ ├─ Determine dependencies                               │
│ ├─ Run topological sort for execution order             │
│ └─ Output: protocol_plan.json                           │
└─────────────────────────────────────────────────────────┘
                           ↓
          Present plan to user → Wait for approval
                           ↓
┌─────────────────────────────────────────────────────────┐
│ USER ACTION: "Create Protocol 06"                       │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ PHASE 3: PROTOCOL GENERATION                            │
│ ├─ Load protocol spec from protocol_plan.json           │
│ ├─ Load script-registry.json                            │
│ ├─ Check for reusable scripts                           │
│ ├─ Generate all 12 sections with context                │
│ ├─ Reference/create automation scripts                  │
│ ├─ Inject project-specific details                      │
│ ├─ Write to AI-project-workflow/06-{name}.md            │
│ └─ Update script-registry.json if new scripts           │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ PHASE 4: VALIDATION (AUTOMATIC - NO USER ACTION)        │
│ ├─ Run validate_all_protocols.py --protocol-id 06       │
│ ├─ Check 10 validators (identity, role, workflow, etc)  │
│ ├─ Calculate overall score                              │
│ ├─ Generate validation report                           │
│ └─ Output: .artifacts/validation/protocol-06-*.json     │
└─────────────────────────────────────────────────────────┘
                           ↓
              ┌────────────┴────────────┐
              │                         │
              ↓                         ↓
    ┌─────────────────┐     ┌─────────────────────┐
    │ PASS (≥0.95)    │     │ FAIL (<0.95)        │
    │ ✅ Protocol OK  │     │ ❌ Needs Fixing     │
    └─────────────────┘     └─────────────────────┘
              │                         │
              ↓                         ↓
    ┌─────────────────┐     ┌─────────────────────┐
    │ Save & Mark     │     │ Analyze Issues      │
    │ Validated       │     │ - Which validators  │
    │                 │     │ - What's wrong      │
    │ Report to user: │     │ - How to fix        │
    │ "Protocol 06    │     └─────────────────────┘
    │  validated ✓"   │                 │
    └─────────────────┘                 ↓
              │               ┌─────────────────────┐
              │               │ Auto-Fix Issues     │
              │               │ - Add missing parts │
              │               │ - Clarify gates     │
              │               │ - Complete workflow │
              │               └─────────────────────┘
              │                         │
              │                         ↓
              │               ┌─────────────────────┐
              │               │ Re-validate         │
              │               │ (Loop until PASS)   │
              │               └─────────────────────┘
              │                         │
              └─────────────┬───────────┘
                            ↓
              ┌─────────────────────────┐
              │ Protocol 06 COMPLETE    │
              │ - Generated ✓           │
              │ - Validated ✓           │
              │ - Scripts integrated ✓  │
              └─────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│ USER ACTION: "Create Protocol 07"                       │
│ (Repeat Phase 3 → Phase 4 for each protocol)            │
└─────────────────────────────────────────────────────────┘
                            ↓
              [Continue for all protocols 06-XX]
                            ↓
┌─────────────────────────────────────────────────────────┐
│ ALL PROTOCOLS COMPLETE                                   │
│ - All generated ✅                                       │
│ - All validated (score ≥0.95) ✅                        │
│ - All scripts registered ✅                             │
│ - Ready for execution ✅                                │
└─────────────────────────────────────────────────────────┘
```

### Key Checkpoints

**Checkpoint 1: After Analysis**
- [ ] Project type correctly identified
- [ ] All deliverables extracted
- [ ] Integrations mapped
- [ ] Quality requirements captured

**Checkpoint 2: After Mapping**
- [ ] All needed protocols identified
- [ ] No gaps in lifecycle coverage
- [ ] Dependencies correct
- [ ] Execution order logical

**Checkpoint 3: After Each Protocol Generation**
- [ ] All 12 sections present
- [ ] Context injected (no placeholders)
- [ ] Scripts referenced or created
- [ ] Validation score ≥0.95
- [ ] Protocol saved and marked validated

**Checkpoint 4: After All Protocols**
- [ ] All protocols validated
- [ ] Script registry updated
- [ ] Protocol registry complete
- [ ] Handoff artifacts ready

### Critical Success Factors

1. **Validation is MANDATORY** - Never skip, never bypass
2. **Scripts are INTEGRATED** - Reuse when possible, create when needed
3. **Context is INJECTED** - Every protocol is project-specific
4. **Quality is ENFORCED** - Score ≥0.95 is non-negotiable
5. **Process is ITERATIVE** - Generate → Validate → Fix → Repeat

---

**Document Version:** 1.0
**Created:** 2025-11-07
**Updated:** 2025-11-07 (Added Validators & Script Registry)
**For:** AI Implementers (Windsurf, Cursor, etc.)
**Status:** Design Complete - Ready for Implementation

**Critical Components:**
- ✅ 11 Validators (score ≥0.95 required)
- ✅ Script Registry (reuse + create strategy)
- ✅ Validation Workflow (mandatory, blocking)
- ✅ Quality Assurance (zero failures before execution)

