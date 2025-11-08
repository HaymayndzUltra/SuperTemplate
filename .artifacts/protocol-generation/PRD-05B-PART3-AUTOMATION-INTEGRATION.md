# PROTOCOL-PRD PART 3: AUTOMATION & INTEGRATION SPECIFICATIONS

## AUTOMATION SUITE (19 Scripts)

### Core Scripts (1-7)

#### 1. parse_project_brief.py
**Purpose:** Parse PROJECT-BRIEF.md and extract requirements  
**Phase:** PHASE 1  
**Complexity:** Medium (200-300 LOC)  

**Inputs:**
- PROJECT-BRIEF.md (workspace root)

**Outputs:**
- project-brief-parsed.json

**Key Functions:**
```python
def parse_project_brief(filepath: str) -> dict:
    """Extract structured data from PROJECT-BRIEF.md"""
    
def extract_requirements(content: str) -> list:
    """Parse requirements section"""
    
def extract_tech_stack(content: str) -> dict:
    """Parse technology stack"""
```

**Error Handling:**
- Missing file: BLOCK, return to Protocol 03
- Invalid markdown: Attempt repair, flag warnings
- Missing sections: Request completion

**Runtime:** <5 seconds  
**Parallelizable:** Yes  
**Retry Limit:** 3  

---

#### 2. parse_architecture.py
**Purpose:** Parse architecture-principles.md and extract constraints  
**Phase:** PHASE 1  
**Complexity:** Medium (200-300 LOC)  

**Inputs:**
- architecture-principles.md (from Protocol 05)

**Outputs:**
- architecture-parsed.json

**Key Functions:**
```python
def parse_architecture(filepath: str) -> dict:
    """Extract architecture patterns and constraints"""
    
def extract_constraints(content: str) -> dict:
    """Parse technical constraints"""
```

**Runtime:** <5 seconds  
**Parallelizable:** Yes  
**Retry Limit:** 3  

---

#### 3. classify_project.py
**Purpose:** Classify project type with confidence scoring  
**Phase:** PHASE 2  
**Complexity:** High (400-500 LOC)  

**Inputs:**
- project-brief-parsed.json
- architecture-parsed.json

**Outputs:**
- project-classification.json
- classification-reasoning.md

**Key Functions:**
```python
def classify_project(brief: dict, arch: dict) -> dict:
    """Classify as AI/Web/API/Mobile/Hybrid"""
    
def calculate_confidence(keywords: list, patterns: list) -> float:
    """Calculate classification confidence (0-100%)"""
    
def generate_reasoning(classification: dict) -> str:
    """Document WHY classified as X"""
```

**Classification Logic:**
```python
ai_keywords = ["model", "training", "inference", "ML", "AI", "prediction"]
web_keywords = ["web app", "UI", "dashboard", "frontend", "React"]
api_keywords = ["API", "REST", "GraphQL", "microservice", "endpoint"]
mobile_keywords = ["mobile", "iOS", "Android", "React Native", "Flutter"]

# Multi-label classification with confidence scores
```

**Runtime:** <30 seconds  
**Parallelizable:** No  
**Retry Limit:** 2  

---

#### 4. detect_characteristics.py
**Purpose:** Run 27+ parallel characteristic detectors  
**Phase:** PHASE 2  
**Complexity:** High (500-700 LOC)  

**Inputs:**
- project-brief-parsed.json
- architecture-parsed.json

**Outputs:**
- characteristics-detection.json
- project-fingerprint.json

**27 Detector Functions:**
```python
def detect_ml_ai(data: dict) -> dict:
    """Detect ML/AI components"""
    
def detect_web_ui(data: dict) -> dict:
    """Detect web UI framework"""
    
def detect_api(data: dict) -> dict:
    """Detect API/microservices"""
    
# ... 24 more detectors
```

**Parallelization:**
- All 27 detectors run simultaneously
- Results aggregated after completion

**Runtime:** <1 minute (parallel)  
**Parallelizable:** Yes (27 tasks)  
**Retry Limit:** 3 per detector  

---

#### 5. map_protocols.py
**Purpose:** Map characteristics to protocols with selection rules  
**Phase:** PHASE 3  
**Complexity:** High (400-600 LOC)  

**Inputs:**
- characteristics-detection.json
- project-classification.json
- Available protocols (scan directories)

**Outputs:**
- characteristic-protocol-mapping.json
- protocol-selection.json
- protocol-priority-matrix.json

**Key Functions:**
```python
def map_characteristics_to_protocols(chars: dict, protocols: list) -> dict:
    """Map each characteristic to relevant protocols"""
    
def apply_selection_rules(mapping: dict, brief: dict) -> dict:
    """Classify as REQUIRED/RECOMMENDED/MAYBE/SKIP"""
    
def generate_priority_matrix(selection: dict) -> dict:
    """Rank protocols by priority"""
```

**Selection Rules:**
```python
REQUIRED = explicit in PROJECT-BRIEF OR critical for project type
RECOMMENDED = strongly beneficial but not mandatory
MAYBE = could add value, user decides
SKIP = not applicable or explicitly excluded
```

**Runtime:** <30 seconds  
**Parallelizable:** Partially  
**Retry Limit:** 2  

---

#### 6. analyze_gaps.py
**Purpose:** Detect protocol coverage gaps  
**Phase:** PHASE 3  
**Complexity:** Medium (300-400 LOC)  

**Inputs:**
- project-brief-parsed.json
- protocol-selection.json

**Outputs:**
- gap-analysis.json
- coverage-report.json

**Key Functions:**
```python
def detect_gaps(requirements: list, selected_protocols: list) -> list:
    """Identify unmapped requirements"""
    
def calculate_coverage(requirements: list, protocols: list) -> float:
    """Calculate coverage percentage"""
    
def prioritize_gaps(gaps: list) -> list:
    """Rank gaps by criticality"""
```

**Coverage Calculation:**
```python
coverage = (mapped_requirements / total_requirements) * 100
critical_coverage = (mapped_critical / total_critical) * 100
```

**Runtime:** <20 seconds  
**Parallelizable:** Yes (with coverage calculation)  
**Retry Limit:** 2  

---

#### 7. sequence_protocols.py
**Purpose:** Build dependency graph and determine execution order  
**Phase:** PHASE 5  
**Complexity:** High (400-500 LOC)  

**Inputs:**
- protocol-selection.json
- Protocol metadata (prerequisites from each protocol)

**Outputs:**
- execution-sequence.json
- dependency-graph.json
- critical-path-analysis.json

**Key Functions:**
```python
def build_dependency_graph(protocols: list) -> dict:
    """Create directed graph of protocol dependencies"""
    
def topological_sort(graph: dict) -> list:
    """Order protocols respecting dependencies"""
    
def identify_parallel_opportunities(graph: dict) -> list:
    """Find protocols that can run simultaneously"""
    
def calculate_critical_path(graph: dict, estimates: dict) -> dict:
    """Determine longest path (bottleneck)"""
```

**Runtime:** <30 seconds  
**Parallelizable:** No  
**Retry Limit:** 5 (circular dependency resolution)  

---

### Enhanced Scripts (8-15)

#### 8. validate_protocol_evidence.py
**Purpose:** Validate Protocol 05 artifacts (Pre-Flight)  
**Phase:** PHASE 0  
**Complexity:** Medium (250-350 LOC)  

**Validation Checks:**
- bootstrap-manifest.json exists and valid JSON
- architecture-principles.md exists and complete
- Protocol 05 quality gates all passed
- PROJECT-BRIEF.md exists and valid

**Runtime:** <30 seconds  
**Retry Limit:** 0 (blocking)  

---

#### 9. calculate_classification_confidence.py
**Purpose:** Calculate confidence scores and enforce 85% threshold  
**Phase:** PHASE 2  
**Complexity:** Low (150-200 LOC)  

**Confidence Formula:**
```python
confidence = (matched_keywords / total_keywords) * keyword_weight +
             (matched_patterns / total_patterns) * pattern_weight +
             (explicit_mentions / total_checks) * explicit_weight
```

**Thresholds:**
- ≥85%: Auto-proceed
- 70-84%: WARNING, proceed with caution
- <70%: BLOCK, require human review

**Runtime:** <10 seconds  

---

#### 10. validate_protocol_coverage.py
**Purpose:** Enforce 95% coverage threshold (Gate 3)  
**Phase:** PHASE 3  
**Complexity:** Medium (200-300 LOC)  

**Coverage Validation:**
```python
overall_coverage >= 95%
critical_coverage == 100%
conflicting_protocols == 0
```

**Actions:**
- Pass: Continue to PHASE 4 or skip if no gaps
- Fail: BLOCK, force PHASE 4 execution

**Runtime:** <20 seconds  

---

#### 11. create_protocol_from_gap.py
**Purpose:** Call Protocol 0 to generate new protocols  
**Phase:** PHASE 4  
**Complexity:** High (500-700 LOC)  

**Integration with Protocol 0:**
```python
def create_protocol_from_gap(gap_spec: dict) -> dict:
    """
    1. Generate protocol specification
    2. Call Bootstrap Protocol Context (Protocol 0)
    3. Receive generated protocol
    4. Validate protocol (score >= 0.95)
    5. Iterate up to 5 times if needed
    6. Register in script registry
    """
```

**Validation Loop:**
```python
for iteration in range(5):
    protocol = call_protocol_0(gap_spec)
    result = validate_protocol(protocol)
    if result.score >= 0.95:
        return protocol
    protocol = apply_fixes(protocol, result.issues)
escalate_to_user()
```

**Runtime:** <15 minutes per protocol (max 5 iterations)  
**Parallelizable:** Yes (multiple gaps)  

---

#### 12. estimate_timeline.py
**Purpose:** Calculate effort and timeline estimates  
**Phase:** PHASE 5  
**Complexity:** Medium (300-400 LOC)  

**Estimation Formula:**
```python
base_effort = protocol_category_hours[category]
complexity_multiplier = {HIGH: 1.5, MEDIUM: 1.0, LOW: 0.5}
customization_penalty = 1.2 if requires_customization else 1.0
parallel_discount = 0.8 if can_run_parallel else 1.0

effort = base_effort * complexity_multiplier * customization_penalty * parallel_discount
```

**Effort Map:**
```python
effort_map = {
    "foundation": 4,
    "planning": 6,
    "execution": 8,
    "testing": 10,
    "deployment": 12,
    "ai_data": 8,
    "ai_model": 16,
    "ai_mlops": 14
}
```

**Runtime:** <30 seconds  

---

#### 13. analyze_customization_needs.py
**Purpose:** Detect required protocol modifications  
**Phase:** PHASE 5  
**Complexity:** Medium (300-400 LOC)  

**Customization Detection:**
```python
def analyze_customization(protocol: dict, project: dict) -> list:
    """
    Check if protocol assumptions match project reality
    Examples:
    - Protocol assumes team → Project is solo dev
    - Protocol assumes web → Project is mobile
    - Protocol generic → Project has AI components
    """
```

**Output Format:**
```json
{
  "protocol_id": "13",
  "section": "ROLES & RESPONSIBILITIES",
  "modification": "Remove team collaboration steps",
  "reason": "Solo developer project",
  "impact": "Medium"
}
```

**Runtime:** <20 seconds  

---

#### 14. generate_execution_plan.py
**Purpose:** Generate PROTOCOL-EXECUTION-PLAN.md  
**Phase:** PHASE 6  
**Complexity:** Medium (300-400 LOC)  

**Plan Sections:**
1. Executive Summary
2. Project Analysis
3. Protocol Selection
4. Gap Analysis
5. Execution Sequence
6. Customization Requirements
7. Timeline & Resources
8. Approval & Sign-off

**Runtime:** <1 minute  
**Parallelizable:** Yes (with checklist generation)  

---

#### 15. generate_checklist.py
**Purpose:** Generate PROTOCOL-CHECKLIST.md  
**Phase:** PHASE 6  
**Complexity:** Low (100-150 LOC)  

**Format:**
```markdown
# Protocol Execution Checklist

## Phase 1: Planning
- [ ] Protocol 06: Create PRD (Generic) - 6 hours
- [ ] Protocol 07: Technical Design (Generic) - 8 hours

## Phase 2: Data Preparation
- [ ] Protocol 08: Data Collection (AI) - 8 hours
...
```

**Runtime:** <30 seconds  
**Parallelizable:** Yes  

---

### Supporting Scripts (16-19)

#### 16. package_handoff.py
**Purpose:** Create handoff-package.zip  
**Phase:** PHASE 6  
**Complexity:** Low (150-200 LOC)  

**Package Contents:**
- All .artifacts/protocol-05b/*.json files
- evidence-manifest.json
- checksums.sha256

**Runtime:** <30 seconds  

---

#### 17. smart_rollback.py
**Purpose:** Rollback to specific phase on failure  
**Phase:** All (error handling)  
**Complexity:** Medium (250-300 LOC)  

**Rollback Logic:**
```python
def smart_rollback(failure_info: dict) -> str:
    """
    Determine which phase to rollback to based on failure type
    Clean up partial artifacts
    Reset state to checkpoint
    """
```

**Runtime:** <10 seconds  

---

#### 18. gate_validator.py
**Purpose:** Validate quality gates 0-6  
**Phase:** All (after each phase)  
**Complexity:** Medium (300-400 LOC)  

**Gate Validation:**
```python
def validate_gate(gate_id: int, data: dict) -> dict:
    """
    Run gate-specific validation
    Log decision
    Return pass/fail with details
    """
```

**Runtime:** <30 seconds per gate  

---

#### 19. communication.py
**Purpose:** Standardized announcement utility  
**Phase:** All  
**Complexity:** Low (100-150 LOC)  

**Announcement Formats:**
```python
def announce(protocol_id: str, event_type: str, details: dict):
    """
    [PROTOCOL 05B | PHASE X START]
    [MILESTONE ACHIEVED]
    [QUALITY GATE PASSED: Gate N]
    [PROTOCOL 05B | ERROR]
    """
```

**Runtime:** <1 second  

---

## SCRIPT REGISTRY INTEGRATION

### Registry Schema
```json
{
  "protocol_05b_scripts": {
    "parse_project_brief": {
      "path": "scripts/protocol-05b/parse_project_brief.py",
      "protocol": "05b",
      "phase": "PHASE 1",
      "purpose": "Parse PROJECT-BRIEF.md and extract requirements",
      "inputs": ["PROJECT-BRIEF.md"],
      "outputs": ["project-brief-parsed.json"],
      "owner": "Workflow Orchestration Architect",
      "status": "active",
      "dependencies": ["pathlib", "json", "logging", "markdown"],
      "version": "1.0",
      "estimated_runtime_seconds": 5,
      "can_run_parallel": true,
      "retry_limit": 3,
      "error_handling": "retry_then_block"
    }
  }
}
```

### Registration Process
1. Create script in `scripts/protocol-05b/`
2. Add entry to `scripts/script-registry.json`
3. Validate JSON schema
4. Test script execution
5. Document in protocol

---

## ERROR HANDLING STANDARDS

### Standard Error Template
```python
import logging
import json
from pathlib import Path

class ProtocolError(Exception):
    """Base exception for protocol errors"""
    pass

class ValidationError(ProtocolError):
    """Recoverable validation error"""
    pass

class CriticalError(ProtocolError):
    """Non-recoverable critical error"""
    pass

def main():
    try:
        result = process()
        log_success(result)
        save_artifact(result)
        return {"status": "success", "data": result}
        
    except ValidationError as e:
        log_error(e, recoverable=True)
        return {"status": "retry", "error": str(e)}
        
    except CriticalError as e:
        log_error(e, recoverable=False)
        return {"status": "critical", "error": str(e)}
        
    finally:
        save_execution_log()
```

### Error Log Structure
```json
{
  "timestamp": "2025-11-08T10:00:00+08:00",
  "script": "classify_project.py",
  "phase": "PHASE 2",
  "error_type": "ValidationError",
  "error_message": "Classification confidence below threshold",
  "recoverable": true,
  "retry_count": 1,
  "stack_trace": "...",
  "context": {...}
}
```

---

## INTEGRATION SPECIFICATIONS

### UPSTREAM INTEGRATION (Inputs)

#### From Protocol 03 (Project Brief)
**Artifact:** PROJECT-BRIEF.md  
**Location:** Workspace root  
**Format:** Markdown  

**Required Fields:**
- project_name: string
- project_goals: array[string]
- deliverables: array[object]
- tech_stack: object
- quality_requirements: object
- timeline_constraints: object
- team_structure: object

**Validation:**
- Must exist at workspace root
- Must be valid markdown
- Must have all required sections

**Error Handling:**
- Missing file: BLOCK, return to Protocol 03
- Invalid format: Attempt parse, flag warnings
- Missing sections: Request completion

---

#### From Protocol 05 (Bootstrap Your Project)
**Artifacts:**
1. bootstrap-manifest.json
2. architecture-principles.md

**bootstrap-manifest.json Schema:**
```json
{
  "project_type": "string",
  "scaffold_structure": {},
  "tooling_config": {},
  "timestamp": "ISO8601"
}
```

**architecture-principles.md Sections:**
- System Architecture
- Technical Constraints
- Integration Requirements
- Infrastructure Requirements

**Error Handling:**
- Missing files: BLOCK, return to Protocol 05
- Invalid JSON: Attempt repair, else BLOCK
- Missing fields: Request completion

---

### DOWNSTREAM INTEGRATION (Outputs)

#### Primary Output: PROTOCOL-EXECUTION-PLAN.md
**Location:** Workspace root  
**Format:** Markdown  

**Required Sections:**
1. Executive Summary (classification, protocol count, timeline)
2. Project Analysis (classification details, characteristics, confidence)
3. Protocol Selection (REQUIRED/RECOMMENDED/MAYBE/SKIP with rationale)
4. Gap Analysis (gaps identified, new protocols created, coverage metrics)
5. Execution Sequence (ordered list, dependencies, parallel opportunities)
6. Customization Requirements (per-protocol modifications, rationale, impact)
7. Timeline & Resources (effort estimates, total hours, milestones)
8. Approval & Sign-off (timestamp, approver, conditions)

---

#### Secondary Output: PROTOCOL-CHECKLIST.md
**Location:** Workspace root  
**Format:** Markdown (checkbox list)  

**Format:**
```markdown
- [ ] Protocol XX: [Name] ([Source: Generic/AI]) - [Hours]
```

---

#### Tertiary Output: handoff-package.zip
**Location:** .artifacts/protocol-05b/  
**Contents:**
- All JSON artifacts from .artifacts/protocol-05b/
- evidence-manifest.json
- checksums.sha256

**Purpose:**
- Complete context for next protocol
- Audit trail
- Rollback support

---

### LATERAL INTEGRATION

#### Protocol 0 (Bootstrap Protocol Context)
**When:** PHASE 4 (gap detection)  
**Interface:** File-based handoff  

**Input to Protocol 0:**
- gap-specification.json
- workflow-requirements.md
- format-template-suggestions.yaml

**Output from Protocol 0:**
- {new-protocol-id}-{name}.md
- protocol-metadata.json

**Error Handling:**
- Protocol 0 fails: Retry once, then escalate
- Invalid protocol: Return to Protocol 0 with feedback

---

#### Validator System
**When:** PHASE 4 (new protocol validation)  
**Interface:** CLI command  

**Command:**
```bash
python validators-system/scripts/validate_all_protocols.py \
  --protocol-id {id} \
  --protocol-dir {dir}
```

**Output:** validation-report.json  

**Error Handling:**
- Validator fails: Retry with different parameters
- Score <0.95: Iterate up to 5 times
- System error: Escalate immediately

---

#### Script Registry
**When:** PHASE 4 (new protocol registration)  
**Interface:** JSON file update  
**Location:** scripts/script-registry.json  

**Update Pattern:** Add new entry per script  
**Validation:** JSON schema check  

**Error Handling:**
- Invalid JSON: Repair and retry
- Duplicate entry: Merge or escalate

---

## CHECKPOINT & RECOVERY SYSTEM

### Checkpoint Strategy
**Save state after each phase completion to enable recovery**

**Checkpoint Files:**
- Location: `.artifacts/protocol-05b/checkpoints/`
- Format: `checkpoint-phase-{N}.json`

**Checkpoint Schema:**
```json
{
  "phase": 2,
  "timestamp": "2025-11-08T10:00:00+08:00",
  "status": "complete",
  "artifacts_generated": ["project-classification.json", "..."],
  "next_phase": 3,
  "state_snapshot": {...}
}
```

### Recovery Workflow
1. Detect checkpoint files on startup
2. Load last successful checkpoint
3. Verify artifact integrity
4. Resume from next phase
5. Skip completed work

### Recovery Scenarios
- **System crash:** Resume from last checkpoint
- **User abort:** Save checkpoint, allow resume later
- **Validation failure:** Rollback to previous checkpoint
- **Critical error:** Save state, escalate for manual recovery

---

## PERFORMANCE & SCALABILITY

### Project Size Categories

**Small Project (<10 requirements):**
- Protocols selected: ~10-15
- Execution time: ~5 minutes
- Parallelization: Minimal benefit

**Medium Project (10-50 requirements):**
- Protocols selected: ~15-25
- Execution time: ~15-20 minutes
- Parallelization: 40% time savings

**Large Project (50-200 requirements):**
- Protocols selected: ~25-40
- Execution time: ~30-45 minutes
- Parallelization: 60% time savings
- Optimization: Caching, incremental processing

**Very Large Project (>200 requirements):**
- Protocols selected: ~40-60
- Execution time: ~60-90 minutes
- Mitigations: Batch processing, streaming JSON, progress indicators

---

