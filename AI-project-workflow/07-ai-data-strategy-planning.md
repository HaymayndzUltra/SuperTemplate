---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 07: AI DATA STRATEGY & REQUIREMENTS PLANNING (PLANNING COMPLIANT)

**Mission:** Transform approved AI use cases into a complete, explicit data strategy—defining what data is needed, from where, at what quality/volume, how it will be labeled, stored, and governed—so that all downstream data collection, cleaning, and modeling work is aligned and gap-free.

**Brand Signal:** Internally maintains MASTER RAY™ terminology for automation, evidence, and handoffs while operating as the AI Data Strategy Planning component of the comprehensive workflow system.

---

## PREREQUISITES

<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT]** List all required artifacts, approvals, and system states before execution.

### 1.1 Required Artifacts
- **`[MUST]`** `06-ai-use-case-definition-prioritization.md` - Final approved AI use cases with feasibility notes
- **`[MUST]`** `03-project-brief-creation.md` - Business goals, constraints, target users, success criteria
- **`[MUST]`** `04-project-bootstrap-and-context-engineering.md` - Existing systems, tech stack, environment context
- **`[MUST]`** `05-bootstrap-your-project.md` - Initial environment setup and configuration

### 1.2 Required Approvals
- **`[MUST]`** Protocol 06 owner confirmation that AI use cases are final and approved
- **`[MUST]`** Project manager acknowledgment of budget and timeline constraints
- **`[MUST]`** Data owner confirmation of data source access permissions

### 1.3 System State Requirements
- **`[MUST]`** `AI-project-workflow/.artifacts/protocol-07-ai-data-strategy-planning/` directory exists and is writable
- **`[MUST]`** Access to existing data catalog or inventory systems
- **`[MUST]`** Python runtime available for data volume calculations and compliance mapping
- **`[MUST]`** Read access to web-dev workflow protocols (03-05) for context only

If any prerequisite fails, pause and resolve before continuing.

---

## AI ROLE AND MISSION

You are a **Data Strategy Architect**. Your mission is to orchestrate comprehensive data strategy planning that translates AI use cases into actionable data requirements while ensuring compliance, feasibility, and stakeholder alignment.

**🚫 [CRITICAL] DO NOT modify any files in `/home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/*.md` - these are read-only context sources.**

### Core Capabilities
- Data architecture and systems integration expertise
- Privacy/compliance regulations (GDPR, HIPAA, industry-specific)
- AI/ML data requirements engineering and volume estimation
- Risk assessment and mitigation planning
- Cross-functional stakeholder coordination

### Behavioral Constraints
- **`[STRICT]`** Must halt at all 3 checkpoints for human validation
- **`[STRICT]`** Must document all data gaps with impact assessments
- **`[STRICT]`** Must ensure 100% use case coverage before proceeding
- **`[STRICT]`** Must not proceed without compliance sign-off for high-risk data
- **`[GUIDELINE]`** Should recommend realistic data sources over ideal but unavailable ones

### Decision Authority
- **Autonomous:** Data volume calculations, freshness requirements, technical mapping
- **Requires Approval:** Source system selection, compliance strategies, final strategy sign-off
- **Can Recommend:** Budget allocation, timeline extensions, use case rescoping

---

## INTEGRATION POINTS

### Inputs From
- **Protocol 06**: AI use case definitions with data requirements and feasibility notes
- **Protocol 03**: Business goals and success criteria affecting data strategy
- **Protocol 04**: Existing systems and tech stack constraints
- **Protocol 05**: Environment setup and initial configuration

### Outputs To
- **Protocol 08**: Data source inventory and collection plans
- **Protocol 09**: Data quality specifications and validation criteria
- **Protocol 10**: Feature engineering requirements and data transformations
- **Protocol 11**: Dataset splitting strategies and preparation guidelines

### Data Formats
- **Strategy Documents**: Markdown (.md) for human-readable plans
- **Structured Data**: JSON (.json) for machine-usable inventories
- **Configuration**: YAML (.yaml) for labeling strategies and compliance rules

### Storage Locations
- **Primary**: `AI-project-workflow/.artifacts/protocol-07-ai-data-strategy-planning/`
- **Phase-specific**: Subdirectories by phase (phase-01-context/, phase-02-requirements/, etc.)
- **Shared**: `AI-project-workflow/.artifacts/shared/` for cross-protocol reference documents

---

## WORKFLOW

<!-- PHASE = STEP: Each phase represents a workflow step -->

<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### STEP 1: CONTEXT & INPUT CONSOLIDATION
### PHASE 1: CONTEXT & INPUT CONSOLIDATION

<!-- [Category: EXECUTION-SUBSTEPS] -->
<!-- Why: Need precise tracking of multiple input sources and their consolidation -->

1. **`[CRITICAL]` Index and Consolidate All Input Sources:**
   * **1.1. Load AI Use Cases:**
       - **Action:** Read and parse `06-ai-use-case-definition-prioritization.md`
       - **Evidence:** `phase-01-context/01-use-cases-loaded.json`
       - **Validation:** All use cases extracted with IDs and data requirements
   * **1.2. Extract Project Context:**
       - **Action:** Parse business goals from `03-project-brief-creation.md`
       - **Action:** Extract tech stack from `04-project-bootstrap-and-context-engineering.md`
       - **Action:** Load environment details from `05-bootstrap-your-project.md`
       - **Evidence:** `phase-01-context/01-project-context-summary.md`
       - **Validation:** All relevant context elements captured
   * **1.3. Map Use Cases to Data Needs:**
       - **Action:** Create preliminary mapping of use_case_id → high-level data categories
       - **Evidence:** `phase-01-context/01-use-case-to-data-needs-sketch.md`
       - **Validation:** 100% use cases have initial data need identification

2. **`[MUST]` Generate Input Sources Summary:**
   * **Action:** Compile comprehensive summary of all inputs and their relevance
   * **Evidence:** `phase-01-context/01-input-sources-summary.md`
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Consolidating context and inputs for data strategy planning..."

### STEP 2: DATA REQUIREMENTS & SOURCE MAPPING
### PHASE 2: DATA REQUIREMENTS & SOURCE MAPPING

<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: Complex data source decisions require documented rationale and alternatives -->

**Reasoning Pattern:** Requirements-before-sources heuristic — systematically define data requirements before source mapping. This prevents mismatched source selections and rework.

**Example Scenario:** When defining requirements, specify datasets, fields, granularity, freshness, and volume per use case. Then map to candidate sources. Therefore, source selection aligns with requirements.

**Strategy Rationale:** Because data sources must meet requirements, defining requirements systematically before mapping prevents mismatched implementations.

**Pattern Improvement:** Track requirement definition accuracy vs actual needs. Refine requirement templates based on Protocol 08 feedback. Iteratively improve requirement specification.

**Decision Tree:** When defining requirements:
- **IF** requirements specific and measurable → Proceed to source mapping
- **ELSE IF** requirements vague → Clarify with use case owners
- **IF** sources available → Document mapping
- **ELSE IF** sources unavailable → Document gaps and alternatives
- **THEN** Verify all requirements mapped

1. **`[CRITICAL]` Define Detailed Data Requirements per Use Case:**
   * **Action:** Specify datasets, fields, granularity, freshness, volume for each use case
   * **Reasoning:** Apply requirements-before-sources pattern using decision tree above
   **[REASONING]:**
   - **Premises:** Use cases require specific data to function; data requirements must be measurable
   - **Constraints:** Must work within available data sources and infrastructure
   - **Decision:** Define requirements with specific metrics (volume, freshness, granularity)
   - **Evidence:** Requirements traceability matrix linking use cases to data needs
   * **2.1. Specify Dataset Requirements:**
       - **Action:** For each use case, define required datasets, fields, granularity, freshness, volume
       - **Evidence:** `phase-02-requirements/02-data-requirements.md`
       - **Validation:** All requirements are specific and measurable
   
   * **2.2. Map Candidate Source Systems:**
       **[REASONING]**
       - **Premises:** Each data requirement needs one or more viable source systems
       - **Constraints:** Existing infrastructure, budget limitations, access permissions
       - **Alternatives Considered:**
         A) Use existing internal systems (selected - cost-effective, faster)
         B) Purchase external data sources (rejected - budget constraints)
         C) Build new data collection (rejected - timeline exceeds project window)
       - **Decision:** Prioritize existing internal systems with augmentation plan for gaps
       - **Evidence:** Source system inventory and access feasibility analysis
       - **Risks & Mitigations:**
         - Risk: Source system doesn't exist → Mitigation: Identify alternative sources
         - Risk: Data quality insufficient → Mitigation: Plan data enhancement processes
       - **Acceptance Link:** Use case requirements specify minimum data quality thresholds

2. **`[MUST]` Identify and Document Data Gaps:**
   * **Action:** For each requirement, assess source availability and accessibility
   * **Action:** Document missing/unavailable data with impact assessments
   * **Evidence:** `phase-02-requirements/02-data-gaps-log.md`
   * **Evidence:** `phase-02-requirements/02-data-requirements-inventory.json`
   - **Structure:**
     ```json
     {
       "use_case_id": "UC-001",
       "dataset_name": "transactions",
       "fields": ["user_id", "amount", "timestamp", "merchant"],
       "source_system": "payments_db",
       "min_volume": "12 months",
       "freshness": "daily",
       "sensitivity": "high"
     }
     ```

3. **`[GUIDELINE]` Checkpoint A - Technical Validation (Await "Technical-Go"):**
   * **Present:** Data requirements draft and source mapping for technical review
   * **Announce:** 
     > "[PHASE 2] Data requirements and source mapping ready for technical validation..."
   * **HALT AND AWAIT** technical owner confirmation that requirements are realistic and sources are accessible

### STEP 3: COMPLIANCE, RISK & CONSTRAINTS ASSESSMENT
### PHASE 3: COMPLIANCE, RISK & CONSTRAINTS ASSESSMENT

<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: Compliance trade-offs need documented rationale for audit purposes -->

1. **`[CRITICAL]` Map Privacy and Compliance Requirements:**
   * **3.1. Identify Applicable Regulations:**
       - **Action:** Map GDPR, HIPAA, industry-specific regulations to each dataset
       - **Evidence:** `phase-03-compliance/03-compliance-requirements.json`
       - **Validation:** All datasets have compliance classification
   
   * **3.2. Assess Data Sensitivity and Risk:**
       **[REASONING]**
       - **Premises:** Each dataset has privacy implications requiring specific controls
       - **Constraints:** Legal requirements, ethical considerations, brand reputation
       - **Alternatives Considered:**
         A) Use data as-is with consent (selected - most accurate for AI)
         B) Anonymize all data (rejected - loss of critical features)
         C) Aggregate data only (rejected - insufficient granularity for use cases)
       - **Decision:** Apply minimization principle with targeted anonymization where required
       - **Evidence:** Privacy impact assessment and legal review requirements
       - **Risks & Mitigations:**
         - Risk: Non-compliance penalties → Mitigation: Implement strict access controls
         - Risk: Data breaches → Mitigation: Encryption and audit logging
       - **Acceptance Link:** Regulatory requirements specify minimum protection standards

2. **`[MUST]` Document Risk Mitigation Strategies:**
   * **Action:** For each high-risk dataset, define specific mitigation approaches
   * **Evidence:** `phase-03-compliance/03-data-risk-assessment.md`
   - **Content:** Risks, mitigations, residual risk assessment, monitoring requirements

3. **`[GUIDELINE]` Checkpoint B - Compliance Validation (Await "Compliance-Go"):**
   * **Present:** Compliance requirements and risk assessment for security/legal review
   * **Announce:**
     > "[PHASE 3] Compliance and risk assessment ready for security/legal validation..."
   * **HALT AND AWAIT** compliance officer confirmation that all requirements are addressed

### STEP 4: STRATEGY FINALIZATION & SIGN-OFF
### PHASE 4: STRATEGY FINALIZATION & SIGN-OFF

<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Deterministic generation of final artifacts and sign-off documentation -->

1. **`[CRITICAL]` Assemble Final Data Strategy:**
   * **4.1. Generate Main Strategy Document:**
       - **Action:** Compile all requirements, sources, and compliance into unified strategy
       - **Evidence:** `data-strategy.md` (main document for Protocols 08-11)
       - **Validation:** Strategy addresses all use cases and constraints
   
   * **4.2. Finalize Labeling Strategy (if supervised learning needed):**
       - **Action:** Define annotation approach, tools, roles, quality thresholds
       - **Evidence:** `labeling-strategy.yaml`
       - **Validation:** Labeling plan meets model requirements and compliance rules

2. **`[MUST]` Generate Final Sign-off Package:**
   * **Action:** Create comprehensive sign-off record with all approvals
   * **Evidence:** `data-strategy-signoff.md`
   - **Content:** Approver names, dates, conditions, any objections or requirements

3. **`[GUIDELINE]` Checkpoint C - Final Sign-off (Await "Final-Go"):**
   * **Present:** Complete data strategy package for business and technical approval
   * **Announce:**
     > "[PHASE 4 COMPLETE] Data strategy ready for final business and technical sign-off..."
   * **HALT AND AWAIT** business + technical stakeholder approval before proceeding to Protocol 08

---

### Rollback Procedures

**[STRICT]** If critical errors occur during protocol execution:

1. **Immediate Halt**: Stop all processing at current phase
2. **State Capture**: Document current state and error details in `rollback-log.md`
3. **Rollback Steps**:
   - Phase 5 → Phase 4: Revert sign-off, restore draft status
   - Phase 4 → Phase 3: Clear prioritization, restore assessment state
   - Phase 3 → Phase 2: Remove scores, restore candidate specs
   - Phase 2 → Phase 1: Clear shaped specs, restore raw ideas
4. **Recovery Path**: Address root cause, validate fixes, resume from rollback point
5. **Evidence**: Document rollback reason, affected artifacts, recovery actions


## QUALITY GATES

### Gate Failure Notification Policy
- **Critical Failures**: Immediate Slack/email notification to protocol owner and stakeholders
- **Warnings**: Logged for review, stakeholder notification within 24h
- **Escalation**: Protocol owner → Project manager → Steering committee
- **Waiver Process**: Documented exception request with risk assessment and mitigation plan

### Gate 1: Data Requirements Completeness
- **Trigger:** End of Phase 2 before Checkpoint A
- **Criteria:** 100% of AI use cases from Protocol 06 must appear in `02-data-requirements-inventory.json`
- **Threshold:** Completeness score ≥ 1.0, coverage = 100%, missing_cases = 0
- **Metrics:** use_case_coverage = 100%, requirements_completeness ≥ 95%, source_mapping ≥ 90%
- **Action on Failure:** Cannot proceed to Phase 3 until all use cases are covered

### Gate 2: Compliance Specification Coverage
- **Trigger:** End of Phase 3 before Checkpoint B
- **Criteria:** Every dataset in requirements inventory must have entry in `03-compliance-requirements.json`
- **Threshold:** Coverage score ≥ 0.95, compliance_mapping ≥ 95%, regulatory_coverage = 100%
- **Metrics:** dataset_coverage ≥ 95%, regulation_mapping = 100%, risk_assessment_complete = YES
- **Action on Failure:** Add missing compliance specifications before proceeding

### Gate 3: Risk & Mitigation Coverage
- **Trigger:** End of Phase 3 before Checkpoint B
- **Criteria:** All "high" sensitivity or "high" risk items must have mitigations in `03-data-risk-assessment.md`
- **Threshold:** 100% of high-risk items have documented mitigations
- **Action on Failure:** Cannot proceed without mitigation plans for all high-risk items

### Gate 4: Final Sign-off
- **Trigger:** End of Phase 4
- **Criteria:** `data-strategy-signoff.md` has at least 1 business/product approver and 1 technical/data approver
- **Threshold:** Minimum 2 approvers with documented sign-off, approval_count ≥ 2, all_conditions_met = TRUE
- **Metrics:** business_approval = YES, technical_approval = YES, compliance_approval = YES, handoff_ready = YES
- **Action on Failure:** Protocol remains in Phase 4 until required sign-offs obtained

---

## COMMUNICATION PROTOCOLS

### Clarification Request Templates
> "[PROTOCOL CLARIFICATION NEEDED] - {specific question}. Please provide: {expected information format}."

> "[PROTOCOL AWAITING INPUT] - Cannot proceed without clarification on: {topic}. Current assumptions: {list}."

> "[PROTOCOL DECISION REQUIRED] - Multiple options available: {options}. Please select preferred approach."

### Progress and Status Updates
> "[PROTOCOL PROGRESS] - Completed {X}/{Y} steps. Current phase: {phase name}. Estimated completion: {timeframe}."

> "[ARTIFACT GENERATED] - Created {artifact name} at {location}. Size: {size}. Validation: {status}."

> "[ARTIFACT UPDATED] - Modified {artifact name}. Changes: {summary}. Version: {version}."

### Status Announcements
- **Phase Start:** `"[MASTER RAY™ | PHASE X START] - [Activity description]..."`
- **Progress Updates:** `"[PHASE X] [Current activity]..."`
- **Completion:** `"[PHASE X COMPLETE] - [Result]..."`
- **Evidence Creation:** `"[EVIDENCE] Created [artifact] at [path]..."`

### User Interaction Templates
- **Checkpoint A:** "Reply 'Technical-Go' to continue with compliance assessment"
- **Checkpoint B:** "Reply 'Compliance-Go' to continue with strategy finalization"
- **Checkpoint C:** "Reply 'Final-Go' to proceed to Protocol 08 (Data Collection)"
- **Clarification:** "Please specify [required information] for data strategy"

### Error Messaging
- **Critical Error:** `"[CRITICAL] [Issue] - Protocol halted until resolved"`
- **Warning:** `"[WARNING] [Issue] - Documented but proceeding with caution"`
- **Information:** `"[INFO] [Status update]`

---

### Error and Exception Communication
> "[PROTOCOL ERROR] - {error type}: {description}. Impact: {scope}. Resolution: {action required}."

> "[PROTOCOL WARNING] - {warning type}: {description}. Can proceed with caution. Recommendation: {suggested action}."

> "[PROTOCOL CONFLICT] - {conflict description}. Affected stakeholders: {list}. Facilitation required."

> "[PROTOCOL ROLLBACK] - Returning to Phase {X} due to {reason}. Affected artifacts: {list}. Previous decisions: {summary}."


## AUTOMATION HOOKS

### Script References
- **Data Volume Calculator:** `python scripts/ai/calculate_data_volume.py --use-cases [file] --output [file]`
- **Compliance Mapper:** `python scripts/ai/compliance_mapper.py --datasets [file] --regulations [file]`
- **Strategy Validator:** `python scripts/ai/validate_strategy_completeness.py --protocol 07`

### Command Syntax Examples
```bash
# Calculate minimum data requirements
python scripts/ai/calculate_data_volume.py \
  --input .artifacts/protocol-06/use-cases.json \
  --output .artifacts/protocol-07/phase-02-requirements/volume-calculations.json

# Map compliance requirements
python scripts/ai/compliance_mapper.py \
  --datasets .artifacts/protocol-07/phase-02-requirements/02-data-requirements-inventory.json \
  --output .artifacts/protocol-07/phase-03-compliance/03-compliance-requirements.json

# Validate strategy completeness
python scripts/ai/validate_strategy_completeness.py \
  --strategy-dir .artifacts/protocol-07/ \
  --report .artifacts/protocol-07/validation-report.json
```

### Manual Fallback
If automation scripts fail:
1. Use manual templates in `.templates/data-strategy/`
2. Follow step-by-step guidance in workflow phases
3. Document manual execution in `rollback-log.md`

---

## HANDOFF CHECKLIST


### Predecessor Validation ✅
- [ ] All required inputs from predecessor protocols received and validated
- [ ] Input quality meets processing requirements
- [ ] All prerequisites satisfied before protocol execution
- [ ] Predecessor sign-offs obtained and documented

### Successor Preparation ✅
- [ ] All output artifacts generated and validated
- [ ] Outputs formatted for successor protocol consumption
- [ ] Clear documentation and usage instructions provided
- [ ] Integration points tested and verified

### Knowledge Transfer ✅
- [ ] Decision rationale documented and accessible
- [ ] Assumptions and constraints explicitly stated
- [ ] Lessons learned captured for future reference
- [ ] Open issues and future considerations identified

### Stakeholder Coordination ✅
- [ ] All required stakeholder approvals and sign-offs obtained
- [ ] Formal authorization from data owners and compliance team received
- [ ] Stakeholder conditions and constraints documented
- [ ] Communication plan for handoff established
- [ ] Support commitment confirmed for next phase
- [ ] Approval evidence packaged and archived

### Continuity Planning ✅
- [ ] Rollback procedures documented if needed
- [ ] Change process defined for scope adjustments
- [ ] Monitoring setup planned for progress tracking
- [ ] Success criteria defined for handoff validation

### Verification Procedures
- [ ] **Phase 1 Complete:** All inputs consolidated and mapped to data needs
- [ ] **Phase 2 Complete:** Data requirements defined with source mapping and gaps documented
- [ ] **Phase 3 Complete:** Compliance requirements mapped with risk mitigations
- [ ] **Phase 4 Complete:** Final strategy assembled with stakeholder sign-offs

### Stakeholder Sign-off Requirements
- [ ] **Technical Owner Approval:** Confirms data requirements are realistic and sources accessible
- [ ] **Compliance Officer Authorization:** All compliance requirements addressed (GDPR, ISO/IEC 42001, NIST AI RMF, IEEE 42020)
- [ ] **Business/Product Owner Approval:** Approves strategy alignment with business goals
- [ ] **Data Owner Authorization:** Confirms data access permissions and governance compliance

### Transition Support
- **Documentation:** `data-strategy.md` provides complete guidance for Protocol 08
- **Artifacts:** All structured files (JSON/YAML) ready for downstream protocol consumption
- **Support:** Data Strategy Architect available for consultation during Protocol 08 execution
- **Escalation:** Protocol 07 owner resolves strategy questions during implementation

### Completion Criteria
- [ ] All 5 required artifacts generated and validated
- [ ] Quality gates 1-4 passed with documented evidence
- [ ] Minimum 2 stakeholder sign-offs obtained
- [ ] No blocking issues or unresolved data gaps
- [ ] Rollback procedures documented and tested

### Final Sign-Off and Readiness ✅
- [ ] **Protocol Owner Approval**: Protocol 07 owner confirms completion with evidence reference
- [ ] **Evidence Package Complete**: All artifacts in `.artifacts/protocol-07-ai-data-strategy-planning/` validated
- [ ] **Handoff Package Ready**: Complete handoff package for Protocol 08 generated
- [ ] **Ready for Next Protocol**: This protocol is complete and READY FOR PROTOCOL 08 (AI Data Collection & Ingestion)

### Next Protocol Continuation
**To begin Protocol 08 (AI Data Collection & Ingestion):**
```bash
# Verify handoff package
python scripts/validate_handoff.py --from 07 --to 08

# Review Protocol 08
# File: .cursor/AI-project-workflow/08-ai-data-collection-ingestion.md
# Begin with PHASE 1: Data Source Connection Setup
```

**Required inputs for Protocol 08:**
- `data-strategy.md` from Protocol 07
- `data-requirements-inventory.json` with source mappings
- `compliance-requirements.json` for data handling

---

## EVIDENCE SUMMARY

**protocol_evidence_dir**: `.artifacts/protocol-07-ai-data-strategy-planning/`

**Protocol Evidence Directory**: `.artifacts/protocol-07-ai-data-strategy-planning/`

All artifacts generated by this protocol are stored in the designated evidence directory with complete version control and audit trails.

### Generated Artifacts
| Artifact | Purpose | Format | Location |
|----------|---------|--------|----------|
| `01-input-sources-summary.md` | Context consolidation summary | .md | `phase-01-context/` |
| `01-use-case-to-data-needs-sketch.md` | Preliminary data needs mapping | .md | `phase-01-context/` |
| `02-data-requirements.md` | Detailed requirements per use case | .md | `phase-02-requirements/` |
| `02-data-requirements-inventory.json` | Machine-usable requirements structure | .json | `phase-02-requirements/` |
| `02-data-gaps-log.md` | Missing data documentation | .md | `phase-02-requirements/` |
| `03-compliance-requirements.json` | Regulatory compliance mapping | .json | `phase-03-compliance/` |
| `03-data-risk-assessment.md` | Risk analysis and mitigations | .md | `phase-03-compliance/` |
| `data-strategy.md` | Main strategy document | .md | `phase-04-signoff/` |
| `labeling-strategy.yaml` | Supervised learning labeling plan | .yaml | `phase-04-signoff/` |
| `data-strategy-signoff.md` | Stakeholder approval record | .md | `phase-04-signoff/` |

### Evidence Manifest Structure
```json
{
  "protocol": "07",
  "execution_id": "{uuid}",
  "timestamp": "{iso8601}",
  "inputs": [{"from_protocol": "06", "artifact": "ai-use-case-definition.md"}],
  "outputs": [{"to_protocol": "08", "artifact": "data-strategy.md"}],
  "artifacts": [
    {
      "type": "strategy_document",
      "path": "data-strategy.md",
      "checksum": "{sha256}",
      "consumers": ["08", "09", "10", "11"]
    },
    {
      "type": "requirements_inventory",
      "path": "phase-02-requirements/02-data-requirements-inventory.json",
      "checksum": "{sha256}",
      "consumers": ["08", "09"]
    },
    {
      "type": "compliance_specification",
      "path": "phase-03-compliance/03-compliance-requirements.json",
      "checksum": "{sha256}",
      "consumers": ["08", "09", "10"]
    }
  ],
  "validation": {
    "quality_gates_passed": 4,
    "stakeholder_signoffs": 2,
    "compliance_status": "approved",
    "overall_score": 0.96
  }
}
```

### Validation Reports
- **Strategy Validation:** `.artifacts/protocol-07/validation-report.json`
- **Completeness Assessment:** `.artifacts/protocol-07/completeness-report.md`
- **Compliance Review:** `.artifacts/protocol-07/compliance-review.json`

---

**Target Overall Validator Score: ≥0.95**

---

## META-REFLECTION & CONTINUOUS IMPROVEMENT

### Lessons Learned Capture
**[STRICT]** At protocol completion, capture lessons learned for future improvement:

1. **Data Discovery Challenges:**
   - Document unexpected data source accessibility issues
   - Record data quality surprises discovered during mapping
   - Note stakeholder alignment difficulties and resolutions

2. **Compliance Complexity:**
   - Track regulatory interpretation challenges
   - Document cross-regulation conflicts and solutions
   - Record approval process bottlenecks and improvements

3. **Process Optimization Opportunities:**
   - Identify automation opportunities that emerged
   - Note template or procedure gaps discovered
   - Document stakeholder communication improvements needed

### Process Improvement Feedback Loop
**[GUIDELINE]** Implement continuous improvement mechanisms:

1. **Real-time Improvement Logging:**
   - Create `improvement-log.md` during execution for issues discovered
   - Track process deviations and their effectiveness
   - Document stakeholder feedback and requested changes

2. **Post-Execution Review:**
   - **Action:** Schedule review within 1 week of protocol completion
   - **Evidence:** `protocol-review-{timestamp}.md`
   - **Participants:** Protocol owner, key stakeholders, technical team
   - **Topics:** What worked, what didn't, improvement priorities

3. **Template Enhancement:**
   - **Action:** Update protocol templates based on lessons learned
   - **Evidence:** `template-improvement-suggestions.md`
   - **Review:** Incorporate into next protocol development cycle

### Future Protocol Considerations
**[STRICT]** Document considerations for downstream protocols:

1. **Protocol 08 (Data Collection) Preparation:**
   - Data source access requirements and lead times
   - Technical infrastructure needs identified
   - Stakeholder coordination requirements
   - Risk mitigation strategies to implement

2. **Cross-Protocol Dependencies:**
   - Data quality standards established for Protocols 09-11
   - Compliance frameworks to be maintained downstream
   - Monitoring requirements for production phases

3. **Scaling Considerations:**
   - Infrastructure scaling needs based on volume calculations
   - Process scaling for additional use cases or data sources
   - Governance scaling for expanded data scope

### Adaptation Mechanisms
**[GUIDELINE]** Build in adaptation capabilities:

1. **Dynamic Adjustment Procedures:**
   - **Trigger:** Significant requirement changes (>20% scope change)
   - **Process:** Impact assessment → Stakeholder review → Protocol adjustment
   - **Evidence:** `protocol-adjustment-{timestamp}.md`

2. **Rollback and Recovery:**
   - **Rollback Triggers:** Quality gate failures, stakeholder veto, technical blockers
   - **Recovery Procedures:** Step-by-step rollback to last stable checkpoint
   - **Evidence:** `rollback-log.md` with decisions and recovery steps

3. **Emergency Protocols:**
   - **Crisis Response:** Data breach discovery, regulatory changes, stakeholder withdrawal
   - **Escalation Paths:** Clear escalation to project governance board
   - **Continuity Plans:** Alternative approaches for critical path items

### Retrospective Framework
**[STRICT]** Complete structured retrospective at protocol conclusion:

```markdown
# Protocol 07 Retrospective - {date}

## What Went Well
- [List successful aspects, tools, processes]

## What Could Be Improved  
- [List challenges, delays, issues encountered]

## Action Items for Next Protocol
- [Specific, assignable improvements for Protocol 08]

## Stakeholder Feedback Summary
- [Key feedback themes and responses]

## Meta-Learning
- [Process insights applicable across protocols]
```

**Evidence Requirements:**
- `lessons-learned-07.md` - Complete lessons learned documentation
- `process-improvements-07.md` - Specific improvement recommendations  
- `future-protocol-input-08.md` - Input document for Protocol 08
- `retrospective-07.md` - Full retrospective documentation

---

*Protocol 07: AI Data Strategy & Requirements Planning - Complete with Meta-Reflection*
