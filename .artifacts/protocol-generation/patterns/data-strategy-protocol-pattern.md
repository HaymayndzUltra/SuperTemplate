# Data Strategy Protocol Pattern - Reusable Template

**Source**: Protocol 07 - AI Data Strategy & Requirements Planning  
**Pattern ID**: DSP-001  
 **Use Case**: Data-intensive protocols requiring compliance, risk assessment, and stakeholder coordination  
**Validator Performance**: Achieves 0.96+ on critical validators  
**Complexity**: Standard (4 phases, moderate automation)

---

## 🎯 PATTERN OVERVIEW

### When to Use This Pattern
- **Data Strategy Planning**: Translating AI use cases to data requirements
- **Compliance-Heavy Protocols**: Multiple regulations (GDPR, HIPAA, etc.)
- **Risk Assessment Required**: Data sensitivity and privacy implications
- **Multi-Stakeholder Coordination**: Technical, business, and compliance approval needed

### Pattern Benefits
- ✅ **High Validator Scores**: 0.96+ on Workflow Algorithm and Cognitive Reasoning
- ✅ **Built-in Compliance**: Automatic regulation mapping and risk assessment
- ✅ **Stakeholder Alignment**: Clear checkpoints and sign-off procedures
- ✅ **Evidence-Driven**: Comprehensive artifact generation and tracking

---

## 🏗️ STRUCTURAL TEMPLATE

### Protocol Header
```markdown
---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL {XX}: {DATA STRATEGY NAME} (PLANNING COMPLIANT)

**Mission:** Transform approved AI use cases into a complete, explicit data strategy—defining what data is needed, from where, at what quality/volume, how it will be labeled, stored, and governed—so that all downstream data collection, cleaning, and modeling work is aligned and gap-free.

**Brand Signal:** Internally maintains MASTER RAY™ terminology for automation, evidence, and handoffs while operating as the {Domain} Strategy Planning component of the comprehensive workflow system.
```

### AI Role Definition
```markdown
## AI ROLE AND MISSION

You are a **{Domain} Strategy Architect**. Your mission is to orchestrate comprehensive {domain} strategy planning that translates {input type} into actionable {output type} while ensuring compliance, feasibility, and stakeholder alignment.

**🚫 [CRITICAL] DO NOT modify any files in `{protected_path}/*.md` - these are read-only context sources.**

### Core Capabilities
- {Domain} architecture and systems integration expertise
- Privacy/compliance regulations (list applicable regulations)
- AI/ML {domain} requirements engineering and estimation
- Risk assessment and mitigation planning
- Cross-functional stakeholder coordination

### Behavioral Constraints
- **`[STRICT]`** Must halt at all {number} checkpoints for human validation
- **`[STRICT]`** Must document all {domain} gaps with impact assessments
- **`[GUIDELINE]`** Prioritize existing {resources} with augmentation plan
```

### 4-Phase Workflow Structure

#### Phase 1: Context & Input Consolidation (SUBSTEPS)
```markdown
### PHASE 1: CONTEXT & INPUT CONSOLIDATION

<!-- [Category: EXECUTION-SUBSTEPS] -->
<!-- Why: Need precise tracking of multiple input sources and their consolidation -->

1. **`[CRITICAL]` Index and Consolidate All Input Sources:**
   * **1.1. Load {Primary Input}:**
       - **Action:** Read and parse `{input_file}`
       - **Evidence:** `phase-01-context/01-{input_type}-loaded.json`
       - **Validation:** All {input_type} extracted with IDs and {domain} requirements
   * **1.2. Extract Project Context:**
       - **Action:** Parse business goals from `{context_file}`
       - **Action:** Extract tech stack from `{tech_file}`
       - **Action:** Load environment details from `{env_file}`
       - **Evidence:** `phase-01-context/01-project-context-summary.md`
       - **Validation:** All relevant context elements captured
   * **1.3. Map Use Cases to {Domain} Needs:**
       - **Action:** Create preliminary mapping of {input_id} → high-level {domain} categories
       - **Evidence:** `phase-01-context/01-use-case-to-{domain}-sketch.md`
       - **Validation:** 100% use cases have initial {domain} need identification

2. **`[MUST]` Generate Input Sources Summary:**
   * **Action:** Compile comprehensive summary of all inputs and their relevance
   * **Evidence:** `phase-01-context/01-input-sources-summary.md`
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Consolidating context and inputs for {domain} strategy planning..."
```

#### Phase 2: Requirements & Source Mapping (REASONING)
```markdown
### PHASE 2: {DOMAIN} REQUIREMENTS & SOURCE MAPPING

<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: Complex {domain} source decisions require documented rationale and alternatives -->

1. **`[CRITICAL]` Define Detailed {Domain} Requirements per Use Case:**
   * **2.1. Specify Dataset Requirements:**
       - **Action:** For each use case, define required {datasets}, {fields}, {granularity}, {freshness}, {volume}
       - **Evidence:** `phase-02-requirements/02-{domain}-requirements.md`
       - **Validation:** All requirements are specific and measurable
   
   * **2.2. Map Candidate Source Systems:**
       **[REASONING]**
       - **Premises:** Each {domain} requirement needs one or more viable source systems
       - **Constraints:** Existing infrastructure, budget limitations, access permissions
       - **Alternatives Considered:**
         A) Use existing internal systems (selected - cost-effective, faster)
         B) Purchase external {domain} sources (rejected - budget constraints)
         C) Build new {domain} collection (rejected - timeline exceeds project window)
       - **Decision:** Prioritize existing internal systems with augmentation plan for gaps
       - **Evidence:** Source system inventory and access feasibility analysis
       - **Risks & Mitigations:**
         - Risk: Source system doesn't exist → Mitigation: Identify alternative sources
         - Risk: {Domain} quality insufficient → Mitigation: Plan {domain} enhancement processes
       - **Acceptance Link:** Use case requirements specify minimum {domain} quality thresholds

2. **`[MUST]` Identify and Document {Domain} Gaps:**
   * **Action:** For each requirement, assess source availability and accessibility
   * **Action:** Document missing/unavailable {domain} with impact assessments
   * **Evidence:** `phase-02-requirements/02-{domain}-gaps-log.md`
   * **Evidence:** `phase-02-requirements/02-{domain}-requirements-inventory.json`
   - **Structure:**
     ```json
     {
       "use_case_id": "UC-001",
       "{dataset_type}": "{dataset_name}",
       "fields": ["{field1}", "{field2}", "{field3}"],
       "source_system": "{system_name}",
       "min_{volume_type}": "{time_period}",
       "freshness": "{update_frequency}",
       "sensitivity": "{risk_level}"
     }
     ```

3. **`[GUIDELINE]` Checkpoint A - Technical Validation (Await "Technical-Go"):**
   * **Present:** {Domain} requirements draft and source mapping for technical review
   * **Announce:** 
     > "[PHASE 2] {Domain} requirements and source mapping ready for technical validation..."
   * **HALT AND AWAIT** technical owner confirmation that requirements are realistic and sources are accessible
```

#### Phase 3: Compliance, Risk & Constraints (REASONING)
```markdown
### PHASE 3: COMPLIANCE, RISK & CONSTRAINTS ASSESSMENT

<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: Compliance trade-offs need documented rationale for audit purposes -->

1. **`[CRITICAL]` Map Privacy and Compliance Requirements:**
   * **3.1. Identify Applicable Regulations:**
       - **Action:** Map {list of regulations} to each {dataset}
       - **Evidence:** `phase-03-compliance/03-compliance-requirements.json`
       - **Validation:** All {datasets} have compliance classification
   
   * **3.2. Assess {Domain} Sensitivity and Risk:**
       **[REASONING]**
       - **Premises:** Each {dataset} has privacy implications requiring specific controls
       - **Constraints:** Legal requirements, ethical considerations, brand reputation
       - **Alternatives Considered:**
         A) Use {domain} as-is with consent (selected - most accurate for AI)
         B) Anonymize all {domain} (rejected - loss of critical features)
         C) Aggregate {domain} only (rejected - insufficient granularity for use cases)
       - **Decision:** Apply minimization principle with targeted anonymization where required
       - **Evidence:** Privacy impact assessment and legal review requirements
       - **Risks & Mitigations:**
         - Risk: Non-compliance penalties → Mitigation: Implement strict access controls
         - Risk: {Domain} breaches → Mitigation: Encryption and audit logging
       - **Acceptance Link:** Regulatory requirements specify minimum protection standards

2. **`[MUST]` Document Risk Mitigation Strategies:**
   * **Action:** For each high-risk {dataset}, define specific mitigation approaches
   * **Evidence:** `phase-03-compliance/03-{domain}-risk-assessment.md`
   - **Content:** Risks, mitigations, residual risk assessment, monitoring requirements

3. **`[GUIDELINE]` Checkpoint B - Compliance Validation (Await "Compliance-Go"):**
   * **Present:** Compliance requirements and risk assessment for security/legal review
   * **Announce:**
     > "[PHASE 3] Compliance and risk assessment ready for security/legal validation..."
   * **HALT AND AWAIT** compliance officer confirmation that all requirements are addressed
```

#### Phase 4: Strategy Finalization & Sign-off (BASIC)
```markdown
### PHASE 4: STRATEGY FINALIZATION & SIGN-OFF

<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Deterministic generation of final artifacts and sign-off documentation -->

1. **`[CRITICAL]` Assemble Final {Domain} Strategy:**
   * **4.1. Generate Main Strategy Document:**
       - **Action:** Compile all requirements, sources, and compliance into unified strategy
       - **Evidence:** `{domain}-strategy.md` (main document for downstream protocols)
       - **Validation:** Strategy addresses all use cases and constraints
   
   * **4.2. Finalize {Optional} Strategy (if applicable):**
       - **Action:** Define {optional} approach, tools, roles, quality thresholds
       - **Evidence:** `{optional}-strategy.yaml`
       - **Validation:** {Optional} plan meets model requirements and compliance rules

2. **`[MUST]` Generate Final Sign-off Package:**
   * **Action:** Create comprehensive sign-off record with all approvals
   * **Evidence:** `{domain}-strategy-signoff.md`
   - **Content:** Approver names, dates, conditions, any objections or requirements

3. **`[GUIDELINE]` Checkpoint C - Final Sign-off (Await "Final-Go"):**
   * **Present:** Complete {domain} strategy package for business and technical approval
   * **Announce:**
     > "[PHASE 4 COMPLETE] {Domain} strategy ready for final business and technical sign-off..."
   * **HALT AND AWAIT** business + technical stakeholder approval before proceeding to next protocol
```

---

## 🔧 AUTOMATION SCRIPTS PATTERN

### Required Scripts
```markdown
### Script References
- **{Domain} Calculator:** `python scripts/ai/{domain}_calculator.py --{input} [file] --output [file]`
- **Compliance Mapper:** `python scripts/ai/compliance_mapper.py --{datasets} [file] --{regulations} [file]`
- **Strategy Validator:** `python scripts/ai/validate_{domain}_completeness.py --protocol {number}`

### Command Syntax Examples
```bash
# Calculate minimum {domain} requirements
python scripts/ai/{domain}_calculator.py \
  --input .artifacts/protocol-{prev}/{input_file}.json \
  --output .artifacts/protocol-{number}/phase-02-requirements/{output_file}.json

# Map compliance requirements
python scripts/ai/compliance_mapper.py \
  --{datasets} .artifacts/protocol-{number}/phase-02-requirements/{inventory_file}.json \
  --output .artifacts/protocol-{number}/phase-03-compliance/{compliance_file}.json

# Validate strategy completeness
python scripts/ai/validate_{domain}_completeness.py \
  --{strategy_dir} .artifacts/protocol-{number}/ \
  --report .artifacts/protocol-{number}/validation-report.json
```
```

---

## 📊 EVIDENCE PACKAGE PATTERN

### Standard Artifacts
```markdown
### Generated Artifacts
| Artifact | Purpose | Format | Location |
|----------|---------|--------|----------|
| `01-input-sources-summary.md` | Context consolidation summary | .md | `phase-01-context/` |
| `01-use-case-to-{domain}-sketch.md` | Preliminary {domain} needs mapping | .md | `phase-01-context/` |
| `02-{domain}-requirements.md` | Detailed requirements per use case | .md | `phase-02-requirements/` |
| `02-{domain}-requirements-inventory.json` | Machine-usable requirements structure | .json | `phase-02-requirements/` |
| `02-{domain}-gaps-log.md` | Missing {domain} documentation | .md | `phase-02-requirements/` |
| `03-compliance-requirements.json` | Regulatory compliance mapping | .json | `phase-03-compliance/` |
| `03-{domain}-risk-assessment.md` | Risk analysis and mitigations | .md | `phase-03-compliance/` |
| `{domain}-strategy.md` | Main strategy document | .md | `phase-04-signoff/` |
| `{optional}-strategy.yaml` | {Optional} planning | .yaml | `phase-04-signoff/` |
| `{domain}-strategy-signoff.md` | Stakeholder approval record | .md | `phase-04-signoff/` |
```

---

## 🎯 CUSTOMIZATION GUIDELINES

### Domain-Specific Adaptation

#### For Model Development Protocols
- Replace `{Domain}` with "Model Development"
- Replace `{datasets}` with "training data", "validation sets", "test sets"
- Replace compliance with "model governance", "ML ethics", "performance standards"

#### For Infrastructure Protocols
- Replace `{Domain}` with "Infrastructure"
- Replace `{datasets}` with "systems", "resources", "environments"
- Replace compliance with "security standards", "operational requirements", "SLA compliance"

#### For Governance Protocols
- Replace `{Domain}` with "Governance"
- Replace `{datasets}` with "policies", "procedures", "controls"
- Replace compliance with "audit requirements", "regulatory alignment", "risk management"

### Complexity Adjustments

#### Simple Protocols (2 phases)
- Combine Phase 1 and Phase 2
- Use EXECUTION-BASIC for both phases
- Reduce checkpoint count to 2

#### Complex Protocols (5+ phases)
- Split Phase 2 into separate "Requirements" and "Source Mapping" phases
- Add additional compliance phases for different regulation types
- Use EXECUTION-REASONING for more decision points

---

## ⚡ PERFORMANCE METRICS

### Validator Score Expectations
- **Protocol Identity**: 0.98+ (header, prerequisites, integration)
- **AI Role**: 1.0 (clear persona with domain expertise)
- **Workflow Algorithm**: 0.96+ (4-phase structure with HALT points)
- **Quality Gates**: 0.96+ (clear criteria and thresholds)
- **Script Integration**: 1.0 (all scripts implemented)
- **Communication Protocol**: 0.98+ (standard templates)
- **Evidence Package**: 1.0 (comprehensive artifacts)
- **Handoff Checklist**: 0.98+ (stakeholder sign-offs)
- **Cognitive Reasoning**: 0.94+ (REASONING blocks in phases 2-3)
- **Meta-Reflection**: 0.96+ (continuous improvement)

### Expected Overall Score: **0.976+ (Production Ready)**

---

## 🔄 SUCCESS STORIES

### Protocol 07: AI Data Strategy & Requirements Planning
- **Achieved**: 0.976 overall validator score
- **Timeline**: 4 hours creation + 4 hours improvements
- **Key Success**: Comprehensive compliance mapping and risk assessment
- **Lessons Learned**: Script integration must be planned, not afterthought

### Future Applications
- **Protocol XX**: Model Development Strategy Planning
- **Protocol YY**: Infrastructure Requirements Planning  
- **Protocol ZZ**: Governance Framework Planning

---

**Data Strategy Protocol Pattern DSP-001 - Proven production-ready template for data-intensive protocols**
