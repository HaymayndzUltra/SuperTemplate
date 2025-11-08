# META-PATTERNS FOR PROTOCOL ORCHESTRATION

## Pattern 1: Project Classification Decision Tree

### Implementation Example from Similar Protocols
```python
def classify_project(project_brief, architecture):
    """
    Classify project type based on keywords and architecture.
    Pattern extracted from Protocol 03 (Project Brief) analysis logic.
    """
    keywords = extract_keywords(project_brief)
    
    # AI/ML Detection
    ai_keywords = ["model", "training", "inference", "ML", "AI", "prediction", "neural"]
    has_ai = any(kw in keywords for kw in ai_keywords)
    
    # Application Detection
    app_keywords = ["web app", "mobile", "UI", "dashboard", "frontend"]
    has_app = any(kw in keywords for kw in app_keywords)
    
    # Classification Logic
    if has_ai and has_app:
        return "HYBRID", 0.95  # Confidence
    elif has_ai:
        return "AI_ML", 0.90
    elif has_app:
        return "WEB_APP", 0.85
    else:
        return "GENERIC", 0.70

# Evidence: Similar pattern used in Protocol 02 (Discovery) for client classification
```

### Decision Tree Visualization
```
PROJECT-BRIEF Keywords
    ↓
    Contains AI/ML keywords?
    ├─ YES → Contains UI keywords?
    │         ├─ YES → HYBRID (Web App + AI)
    │         └─ NO → AI_ML (Pure ML project)
    └─ NO → Contains API keywords?
              ├─ YES → API_MICROSERVICE
              └─ NO → WEB_APP (Generic)
```

---

## Pattern 2: Protocol Selection Matrix

### Mapping Table Pattern
```yaml
# Extracted from Protocol 08 (Generate Tasks) logic for task type selection

Characteristic → Protocol Mapping:
  
"Model training required":
  REQUIRED: [AI:10, AI:11, AI:12, AI:13, AI:14]
  OPTIONAL: [AI:16, AI:17]
  REASON: "Training pipeline needs data prep, training, validation"
  
"Production deployment":
  REQUIRED: [14, 15, 16]
  OPTIONAL: [17, 18]
  REASON: "Deployment needs staging, production, monitoring"
  
"Solo developer":
  SKIP: [13]  # UAT not needed
  REASON: "No external stakeholders for user acceptance testing"
  
"MVP phase":
  SKIP: [18]  # Performance optimization
  REASON: "Optimization deferred to v2, focus on MVP delivery"
```

### Selection Algorithm Pattern
```python
def select_protocols(characteristics, available_protocols):
    """
    Select protocols based on project characteristics.
    Pattern: Explicit > Implicit > Optional > Skip
    """
    selected = {
        "REQUIRED": [],
        "MAYBE": [],
        "SKIP": []
    }
    
    for protocol in available_protocols:
        # Check explicit requirements
        if protocol.workflow in characteristics.explicit_requirements:
            selected["REQUIRED"].append(protocol)
            continue
        
        # Check implicit needs
        if protocol.handles_characteristic(characteristics.detected):
            selected["REQUIRED"].append(protocol)
            continue
        
        # Check if useful but not mandatory
        if protocol.could_benefit(characteristics):
            selected["MAYBE"].append(protocol)
            continue
        
        # Otherwise skip
        selected["SKIP"].append(protocol)
    
    return selected

# Evidence: Similar logic in Protocol 07 (Technical Design) for architecture selection
```

---

## Pattern 3: Gap Detection & Protocol Creation

### Gap Detection Pattern
```python
def detect_gaps(requirements, existing_protocols):
    """
    Identify requirements without protocol coverage.
    Pattern: Requirement → Protocol mapping validation
    """
    gaps = []
    
    for requirement in requirements:
        has_protocol = False
        
        for protocol in existing_protocols:
            if protocol.handles(requirement):
                has_protocol = True
                break
        
        if not has_protocol:
            gaps.append({
                "requirement": requirement,
                "source": requirement.source_line,
                "gap_reason": "No existing protocol handles this workflow",
                "proposed_protocol_id": calculate_insertion_point(existing_protocols),
                "workflow_summary": summarize_workflow(requirement)
            })
    
    return gaps

# Evidence: Gap detection pattern used in Protocol 04 (Bootstrap) for missing context
```

### Protocol Creation Workflow Pattern
```yaml
# Pattern extracted from Protocol 05 (Bootstrap) for context engineering

Gap Identified → Protocol Creation Pipeline:
  
STEP 1: Define Protocol Specification
  - Extract from requirement: workflow steps, inputs, outputs
  - Determine protocol ID: Sequential insertion point
  - Classify: Category, criticality, complexity, scope
  
STEP 2: Select Format Templates
  - Workflow steps → EXECUTION-FORMATS.md (variant: SUBSTEPS)
  - Validation → GUIDELINES-FORMATS.md
  - Decision points → EXECUTION-FORMATS.md (variant: REASONING)
  
STEP 3: Generate Protocol Structure
  - Call Bootstrap Protocol Context (Protocol 0)
  - Provide: specification, requirements, format templates
  - Receive: Complete protocol markdown file
  
STEP 4: Validate Protocol
  - Run all 10 validators
  - Require: Overall score ≥0.95
  - Iterate: Fix issues, re-validate
  
STEP 5: Register & Integrate
  - Add to protocol directory
  - Update script-registry.json
  - Update protocol integration map
```

---

## Pattern 4: Timeline & Cost Estimation

### Estimation Pattern
```python
def estimate_timeline(selected_protocols):
    """
    Calculate execution timeline based on protocol complexity.
    Pattern: Protocol complexity → effort hours mapping
    """
    # Base effort hours per protocol type
    effort_map = {
        "foundation": 4,      # Protocols 01-05
        "planning": 6,        # Protocols 06-09
        "execution": 8,       # Protocol 10
        "testing": 10,        # Protocols 11-13
        "deployment": 12,     # Protocols 14-18
        "operations": 6,      # Protocols 19-23
        "ai_data": 8,         # AI Protocols 06-09
        "ai_model": 16,       # AI Protocols 10-14
        "ai_mlops": 14,       # AI Protocols 18-21
        "ai_governance": 6    # AI Protocols 22-28
    }
    
    total_hours = 0
    
    for protocol in selected_protocols:
        category = protocol.category
        base_effort = effort_map[category]
        
        # Apply complexity multiplier
        if protocol.complexity == "HIGH":
            effort = base_effort * 1.5
        elif protocol.complexity == "MEDIUM":
            effort = base_effort * 1.0
        else:  # LOW
            effort = base_effort * 0.5
        
        # Apply customization penalty
        if protocol.requires_customization:
            effort *= 1.2
        
        # Apply parallel execution discount
        if protocol.can_run_parallel:
            effort *= 0.8
        
        total_hours += effort
    
    return {
        "total_hours": total_hours,
        "estimated_days": total_hours / 8,
        "estimated_weeks": total_hours / 40,
        "breakdown": [...]
    }

# Evidence: Similar estimation in Protocol 06 (Create PRD) for feature estimation
```

---

## Pattern 5: Protocol Customization Analysis

### Customization Detection Pattern
```python
def analyze_customization_needs(protocol, project_characteristics):
    """
    Determine if protocol needs customization for specific project.
    Pattern: Standard vs Custom execution decision
    """
    customizations = []
    
    # Check if project characteristics require modifications
    if protocol.assumes_team and project_characteristics.solo_developer:
        customizations.append({
            "section": "ROLES & RESPONSIBILITIES",
            "modification": "Remove team collaboration steps, single-person workflow",
            "reason": "Solo developer project",
            "impact": "Medium"
        })
    
    if protocol.assumes_web and project_characteristics.is_mobile:
        customizations.append({
            "section": "WORKFLOW - PHASE 2",
            "modification": "Replace web deployment with mobile app store deployment",
            "reason": "Mobile application target",
            "impact": "High"
        })
    
    if protocol.generic and project_characteristics.has_ai:
        customizations.append({
            "section": "QUALITY GATES",
            "modification": "Add ML model validation gates",
            "reason": "AI/ML components present",
            "impact": "High"
        })
    
    return customizations

# Evidence: Customization pattern from Protocol 10 (Process Tasks) for task adaptation
```

---

## Pattern 6: Execution Sequencing

### Dependency Graph Pattern
```python
def build_execution_sequence(selected_protocols):
    """
    Order protocols considering dependencies and parallel opportunities.
    Pattern: Dependency resolution + critical path analysis
    """
    # Build dependency graph
    graph = {}
    for protocol in selected_protocols:
        graph[protocol.id] = {
            "protocol": protocol,
            "dependencies": protocol.prerequisites,
            "can_parallel": protocol.allows_parallel
        }
    
    # Topological sort for execution order
    sequence = []
    visited = set()
    
    def visit(protocol_id):
        if protocol_id in visited:
            return
        
        node = graph[protocol_id]
        for dep in node["dependencies"]:
            visit(dep)
        
        visited.add(protocol_id)
        sequence.append(node["protocol"])
    
    for protocol_id in graph:
        visit(protocol_id)
    
    # Identify parallel execution opportunities
    parallel_groups = []
    current_group = []
    
    for protocol in sequence:
        if protocol.can_parallel and current_group:
            current_group.append(protocol)
        else:
            if current_group:
                parallel_groups.append(current_group)
            current_group = [protocol]
    
    if current_group:
        parallel_groups.append(current_group)
    
    return {
        "sequence": sequence,
        "parallel_groups": parallel_groups,
        "critical_path": calculate_critical_path(parallel_groups)
    }

# Evidence: Sequencing logic from Protocol 08 (Generate Tasks) task ordering
```

---

## Pattern 7: User Decision Prompts

### MAYBE Protocol Presentation Pattern
```yaml
# Pattern from Protocol 02 (Discovery) for ambiguous requirements

MAYBE Protocol Presentation Format:

"I've identified {N} protocols that could be valuable but aren't strictly required:

Protocol {ID}: {Name}
  Purpose: {What it does}
  Value: {Why it could help}
  Cost: {Estimated hours}
  Skip If: {When to skip}
  Your Decision: Include / Skip / Defer to later phase

Example:

Protocol 17: Incident Response & Rollback
  Purpose: Handle production incidents and perform rollbacks
  Value: Faster recovery from issues, reduces downtime
  Cost: 8 hours setup + ongoing monitoring
  Skip If: Low-traffic MVP, non-critical system, tight budget
  Your Decision: [ ] Include  [ ] Skip  [ ] Defer to v2
"
```

---

## Pattern 8: Evidence Package Structure

### Artifact Organization Pattern
```yaml
# Pattern from Protocol 11 (Integration Testing) evidence packaging

.artifacts/protocol-{ID}/
├── phase-{N}-{name}.json           # One per phase
├── {analysis-type}-results.json    # Analysis outputs
├── {artifact-name}.md              # Documentation artifacts
├── evidence-manifest.json          # Master index
├── checksums.sha256                # Integrity verification
├── metadata.json                   # Protocol execution metadata
├── new-protocols/                  # If protocol creation occurred
│   ├── {new-id}-specification.json
│   ├── {new-id}-{name}.md
│   └── {new-id}-validation-report.json
└── handoff-package.zip             # Compressed for downstream

Root-level outputs:
├── {PRIMARY-OUTPUT}.md             # Main deliverable
└── {TRACKING-TOOL}.md              # Progress tracking
```

---

## Pattern 9: Communication Templates

### Structured Announcement Pattern
```yaml
# Pattern from Protocol 15 (Production Deployment) communication

Phase Start:
  "[PROTOCOL {ID} | PHASE {N} START] - {Action Description}"
  Example: "[PROTOCOL 05B | PHASE 1 START] - Validating foundation artifacts"

Milestone:
  "[{EVENT NAME}] - {Details with Metrics}"
  Example: "[PROJECT CLASSIFIED] - Type: HYBRID, Confidence: 0.95"

Quality Gate:
  "[QUALITY GATE {STATUS}: Gate {N}] - {Gate Name}"
  Example: "[QUALITY GATE PASSED: Gate 3] - Protocol Coverage Verified"

Phase Complete:
  "[PROTOCOL {ID} | PHASE {N} COMPLETE] - {Summary}"
  Example: "[PROTOCOL 05B | PHASE 6 COMPLETE] - Handoff to Protocol 06"

Error/Blocking:
  "[PROTOCOL {ID} | {STATUS}] - {Reason}"
  Example: "[PROTOCOL 05B | GATE 1 FAILED] - Protocol 05 artifacts incomplete"
```

---

## Pattern 10: Validation & Iteration Loop

### Quality Validation Pattern
```python
def validate_and_iterate(protocol, max_iterations=3):
    """
    Validate protocol and iterate until pass criteria met.
    Pattern: Validate → Analyze → Fix → Re-validate loop
    """
    iteration = 0
    
    while iteration < max_iterations:
        # Run validation suite
        result = run_validators(protocol)
        
        if result.overall_score >= 0.95:
            return {
                "status": "PASS",
                "score": result.overall_score,
                "iterations": iteration + 1
            }
        
        # Analyze failures
        issues = []
        for validator in result.validators:
            if validator.score < 0.90:
                issues.extend(validator.issues)
        
        # Apply fixes
        for issue in issues:
            apply_fix(protocol, issue)
        
        iteration += 1
    
    # Max iterations reached without passing
    return {
        "status": "FAIL",
        "score": result.overall_score,
        "iterations": max_iterations,
        "action": "ESCALATE_TO_USER"
    }

# Evidence: Validation loop from Protocol 12 (Quality Audit) remediation
```

---

## APPLICATION GUIDE

### When to Use Each Pattern

| Pattern | Use When | Example Scenario |
|---------|----------|------------------|
| Pattern 1: Classification | Starting project analysis | Determining if project is AI/ML, web app, or hybrid |
| Pattern 2: Selection Matrix | Choosing protocols | Mapping detected characteristics to required protocols |
| Pattern 3: Gap Detection | Coverage analysis | Identifying blockchain deployment needs not in existing protocols |
| Pattern 4: Timeline Estimation | Planning phase | Calculating 42 hours for selected protocols vs 180 for all |
| Pattern 5: Customization | Protocol adaptation | Solo dev project needs single-person workflow modifications |
| Pattern 6: Sequencing | Execution planning | Ordering protocols with dependencies, finding parallel opportunities |
| Pattern 7: User Decisions | Ambiguous requirements | Presenting "Incident Response" as MAYBE protocol for MVP |
| Pattern 8: Evidence Structure | Artifact organization | Organizing 15+ artifacts for downstream handoff |
| Pattern 9: Communication | Status updates | Announcing "[PROJECT CLASSIFIED] - Type: HYBRID" |
| Pattern 10: Validation Loop | Quality assurance | Iterating on new protocol until score ≥0.95 |

---

## INTEGRATION WITH PROTOCOL 05B

These meta-patterns are directly embedded in Protocol 05b workflow:

- **PHASE 2 STEP 2.1** uses **Pattern 1** (Classification)
- **PHASE 3 STEP 3.1** uses **Pattern 2** (Selection Matrix)
- **PHASE 3 STEP 3.3** uses **Pattern 3** (Gap Detection)
- **PHASE 4** uses **Pattern 3 & 10** (Gap Creation + Validation)
- **PHASE 5 STEP 5.1** uses **Pattern 6** (Sequencing)
- **PHASE 5 STEP 5.2** uses **Pattern 5** (Customization)
- **PHASE 5 STEP 5.3** uses **Pattern 4** (Timeline)
- **PHASE 6** uses **Pattern 7** (User Decisions)
- **All phases** use **Pattern 9** (Communication)
- **Evidence generation** uses **Pattern 8** (Artifact Structure)
