---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 05: BOOTSTRAP YOUR PROJECT (LEGACY ALIGNMENT COMPLIANT)

**Purpose:** Execute BOOTSTRAP YOUR PROJECT workflow with quality validation and evidence generation.

## PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

### Required Artifacts Standards
**[STRICT]** All artifacts must be present and validated before protocol execution:

- **`.cursor/context-kit/governance-status.md`** from Protocol 04
  - Format: Baseline governance summary document
  - Validation: File existence and readability
  - Location: `.cursor/context-kit/` directory
  
- **`bootstrap-manifest.json`** from Protocol 04
  - Format: Generated scaffold inventory in JSON format
  - Requirements: Valid JSON structure with asset listings
  - Location: `.artifacts/protocol-04/`
  
- **Repository access manifest**
  - Format: List of directories allowed for modification
  - Requirements: Clear definition of governed vs. production directories
  - Location: Project documentation

### Required Approvals Standards  
**[STRICT]** Following approvals must be documented:

- **Product Owner Approval**
  - Purpose: Authorization to proceed with legacy bootstrap alignment
  - Documentation: Written approval in communication log
  - Validation: Timestamp and approver identification
  
- **Engineering Lead Confirmation**
  - Purpose: Confirm Cursor rule governance requirement
  - Documentation: Technical decision record
  - Validation: Rationale for governance approach

### System State Requirements Standards
**System must meet following requirements:**

- **Command Execution Capability**
  - Requirement: Shell command execution for rule normalization
  - Validation: Script execution permissions verified
  
- **Repository Access**
  - Requirement: Read-only access to production code
  - Validation: No write operations permitted to production files
  
- **Cursor Editor Availability**
  - Requirement: Cursor installed if `.mdc` rules required
  - Validation: Editor version and extension compatibility

---

## AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

### Role Definition
You are an **AI Codebase Analyst & Context Architect**. Your mission is to align legacy bootstrap procedures with the modern governed scaffold, configure AI governance tooling, and produce a validated context kit while avoiding direct production code changes.

### Critical Directive
**🚫 [CRITICAL] Do not edit or delete production application files; all modifications must remain within governed directories.**

### Operational Boundaries
- **Permitted:** Modify `.cursor/`, `.artifacts/`, documentation files
- **Prohibited:** Alter production source code, configuration files, user data
- **Validation:** All operations logged with rollback capability

---

## WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### STEP 1: Governance Tooling Activation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple workflow steps for tooling confirmation and rule configuration -->

1. **`[MUST]` Confirm Tooling Requirements:**
   * **Action:** Ask whether the team uses Cursor; if yes, prepare `.cursor/rules/` for rule activation.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Confirming editor tooling to activate governance rules."
   * **Evidence:** `.artifacts/protocol-05/tooling-confirmation.log`
   * **Validation:** Tooling choice documented
   * **Halt condition:** Pause until tooling confirmation received.

2. **`[MUST]` Configure Cursor Rule Structure:**
   * **Action:** Locate `master-rules` and `common-rules` directories, move them under `.cursor/rules/`, rename `.md` files to `.mdc`, and ensure YAML frontmatter includes `alwaysApply` metadata.
   * **Communication:** 
     > "Migrating master and common rules into Cursor-compatible `.mdc` format."
   * **Evidence:** `.artifacts/protocol-05/rule-migration-report.md`
   * **Validation:** All rules contain valid frontmatter

3. **`[GUIDELINE]` Run Cursor Rule Generation:**
   * **Action:** If `PROJECT-BRIEF.md` or minimal signals exist, execute `/Generate Cursor Rules --dry-run`, review output, then rerun without `--dry-run` once approved.
   * **Evidence:** Generated rule files in `.cursor/rules/`
   * **Validation:** Rules align with project context
   
   **Example (DO):**
   ```text
   /Generate Cursor Rules --dry-run
   ```

### STEP 2: Repository Mapping and Stack Detection
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward repository analysis and stack detection -->

1. **`[MUST]` Map Repository Structure:**
   * **Action:** Produce a comprehensive tree of the repository, capturing key directories and files for architectural insight.
   * **Communication:** 
     > "[PHASE 2] - Mapping repository structure to identify foundational assets."
   * **Evidence:** `.artifacts/protocol-05/repo-structure.txt`
   * **Validation:** Structure completeness verified
   * **Halt condition:** Await user validation of proposed key files.

2. **`[MUST]` Validate Analysis Plan:**
   * **Action:** Present the proposed key files (e.g., package manifests, entry points) and pause for user confirmation before deep analysis.
   * **Communication:** 
     > "Proposed analysis targets: `package.json`, `src/main.tsx`, `vite.config.ts`. Confirm or adjust before proceeding."
   * **Evidence:** `.artifacts/protocol-05/analysis-plan.md`
   * **Validation:** User approval recorded

3. **`[MUST]` Capture Stack Signals:**
   * **Action:** Analyze confirmed files to determine languages, frameworks, and build tooling; store in `.cursor/bootstrap/detected-stack.json`.
   * **Communication:** 
     > "Recording detected stack characteristics for context kit seeding."
   * **Evidence:** `.cursor/bootstrap/detected-stack.json`
   * **Validation:** Stack detection coverage ≥ 90%

### STEP 3: Thematic Investigation & Principle Extraction
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple investigation and principle extraction steps -->

1. **`[MUST]` Define Investigation Themes:**
   * **Action:** Generate thematic questions (security, data flow, conventions) tailored to the detected stack.
   * **Communication:** 
     > "[PHASE 3] - Establishing thematic investigation plan covering security, data flow, and conventions."
   * **Evidence:** `.artifacts/protocol-05/investigation-themes.md`
   * **Validation:** Themes cover critical aspects

2. **`[MUST]` Perform Semantic Deep Dives:**
   * **Action:** Use approved search tools to examine code implementing each theme; collect supporting snippets.
   * **Communication:** 
     > "Executing semantic analysis to uncover architectural principles."
   * **Evidence:** `.artifacts/protocol-05/theme-findings.json`
   * **Validation:** Findings documented with code references

3. **`[GUIDELINE]` Synthesize Principles:**
   * **Action:** Translate findings into pragmatic principles and document in `architecture-principles.md`.
   * **Evidence:** `architecture-principles.md`
   * **Validation:** Principles actionable and specific
   
   **Example (DO):**
   ```markdown
   - Authentication relies on HMAC middleware (`src/middleware/validateHmac.ts`).
   - Error responses standardize `{ success: false, error }` envelope.
   ```

### STEP 4: Validation Checkpoint and Context Kit Initialization
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward validation and context initialization -->

1. **`[MUST]` Present Consolidated Findings:**
   * **Action:** Share summary of understanding and outstanding questions; pause for user feedback before automation.
   * **Communication:** 
     > "[PHASE 4] - Presenting bootstrap findings for validation prior to context kit generation."
   * **Evidence:** `.artifacts/protocol-05/validation-brief.md`
   * **Validation:** User feedback incorporated
   * **Halt condition:** Wait for user confirmation or corrections.

2. **`[MUST]` Initialize Context Kit Structure:**
   * **Action:** Create `.cursor/context-kit/` directories and seed README with validated principles and outstanding questions.
   * **Communication:** 
     > "Initializing context kit directories with validated principles."
   * **Evidence:** `.cursor/context-kit/README.md`
   * **Validation:** Context kit structure created

3. **`[GUIDELINE]` Record Manual Validation Log:**
   * **Action:** Document validation feedback and decisions in `.artifacts/protocol-05/manual-validation-log.md`.
   * **Evidence:** `.artifacts/protocol-05/manual-validation-log.md`
   * **Validation:** Feedback captured completely

### STEP 5: Documentation and Rule Alignment
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple documentation and rule management steps -->

1. **`[MUST]` Generate Documentation Plan:**
   * **Action:** Identify READMEs requiring creation or updates; capture mapping in `documentation-plan.md`.
   * **Communication:** 
     > "[PHASE 5] - Planning README updates aligned with validated principles."
   * **Evidence:** `.artifacts/protocol-05/documentation-plan.md`
   * **Validation:** Plan covers all necessary documentation

2. **`[MUST]` Produce or Update READMEs:**
   * **Action:** Create targeted READMEs capturing architecture, workflows, and conventions; obtain user approval for each.
   * **Communication:** 
     > "Publishing README updates; awaiting approval for each document."
   * **Evidence:** `.artifacts/protocol-05/readme-updates/`
   * **Validation:** Each README approved by user

3. **`[MUST]` Normalize and Audit Rules:**
   * **Action:** Run `python scripts/normalize_project_rules.py --target .cursor/rules/` and `python scripts/rules_audit_quick.py --output .artifacts/protocol-05/rule-audit-report.md`; update context kit with audit link.
   * **Communication:** 
     > "Normalizing project rules and recording audit evidence."
   * **Evidence:** `.artifacts/protocol-05/rule-audit-report.md`
   * **Validation:** Audit severity ≤ Medium

4. **`[GUIDELINE]` Offer Optional Scaffold Generation:**
   * **Action:** If `brief.md` detected, offer `/Generate Project --brief <path>` to create scaffold in sibling directory; document decision.
   * **Evidence:** Decision documented in execution log
   * **Validation:** User decision recorded

### STEP 6: Project Rule Finalization and Template Discovery
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward rule generation and template inventory -->

1. **`[MUST]` Generate Rule Updates from READMEs:**
   * **Action:** Create or update project rules reflecting README guidance; link each rule to its source doc.
   * **Communication:** 
     > "[PHASE 6] - Translating documentation into enforceable project rules."
   * **Evidence:** `.cursor/rules/project-rules/*.mdc`
   * **Validation:** Rules traceable to documentation

2. **`[MUST]` Validate Rules Post-Update:**
   * **Action:** Re-run rule audit and capture results in `rule-audit-final.md`; ensure no critical findings.
   * **Communication:** 
     > "Revalidating project rules after updates."
   * **Evidence:** `.artifacts/protocol-05/rule-audit-final.md`
   * **Validation:** No critical audit findings

3. **`[GUIDELINE]` Inventory Template Packs:**
   * **Action:** List available template packs using TemplateRegistry and store in `.cursor/context-kit/template-inventory.md`.
   * **Evidence:** `.cursor/context-kit/template-inventory.md`
   * **Validation:** Template inventory complete
   
   **Example (DO):**
   ```bash
   python -c "from project_generator.template_registry import TemplateRegistry; print(TemplateRegistry.list_all())" \
     > .cursor/context-kit/template-inventory.md
   ```

---
## REFLECTION & LEARNING
<!-- [Category: META-FORMATS] -->
<!-- Why: Meta-level retrospective and continuous improvement tracking -->

### Retrospective Guidance

#### Execution Retrospective Framework
After completing protocol execution (successful or halted), conduct retrospective:

**Timing:** Within 24-48 hours of completion

**Participants:** Protocol executor, downstream consumers, stakeholders

**Agenda Structure:**

1. **What went well:**
   - Which steps executed smoothly and efficiently?
   - Which quality gates were well-calibrated?
   - Which artifacts provided high value to downstream protocols?

2. **What went poorly:**
   - Which steps encountered blockers or delays?
   - Which quality gates were too strict or too lenient?
   - Which artifacts required rework or clarification?

3. **Action items:**
   - Protocol template updates needed?
   - Quality gate threshold adjustments?
   - New automation opportunities?

**Output:** Retrospective report stored in protocol execution artifacts

### Continuous Improvement Opportunities

#### Improvement Identification Process
- Identify patterns based on protocol-specific execution data
- Analyze recurring blockers and their root causes
- Document enhancement opportunities with business cases

#### Process Optimization Tracking
- **Key Performance Metrics:** Execution time, quality gate pass rates, rework frequency
- **Monitoring Cadence:** Quarterly metrics dashboard with trend analysis
- **Velocity Tracking:** Measure downstream satisfaction and completion rates
- **Automation Pipeline:** Identify manual steps for automation conversion

#### Tracking Mechanisms and Metrics
- **Dashboard Components:** Quarterly trends, pass/fail ratios, execution velocity
- **Improvement Log:** Before/after comparisons with measurable outcomes
- **Evidence Repository:** Validation artifacts demonstrating improvements

#### Evidence of Improvement and Validation
- **Metric Trends:** Improvement trajectories over time periods
- **A/B Testing:** Protocol change validation through controlled testing
- **Stakeholder Feedback:** Satisfaction scores and feedback integration
- **Downstream Impact:** Protocol consumer satisfaction ratings

### System Evolution

#### Version History
- **Current Version:** Implementation date and version number
- **Previous Versions:** Change log with deprecation notices
- **Migration Path:** Upgrade procedures for protocol consumers

#### Rationale for Changes
- **Change Documentation:** Reasons for each protocol evolution
- **Evidence Base:** Supporting data for change decisions
- **Impact Assessment:** Expected outcomes and risk analysis

#### Impact Assessment
- **Measured Outcomes:** Actual vs. expected change results
- **Baseline Comparison:** Performance against previous versions
- **Hypothesis Validation:** Confirmation of improvement assumptions

#### Rollback Procedures
- **Rollback Process:** Steps to revert to previous protocol version
- **Trigger Criteria:** Conditions requiring rollback initiation
- **Communication Plan:** Stakeholder notification procedures

### Knowledge Capture and Organizational Learning

#### Lessons Learned Repository
Maintain structured lessons learned:
- **Context:** Project/execution environment details
- **Insight:** Discovery or pattern identified
- **Action:** Response to the insight
- **Outcome:** Results and broader applicability

#### Knowledge Base Growth
- **Pattern Extraction:** Systematic mining of execution data
- **Update Schedule:** Regular knowledge base maintenance cycles
- **Quality Metrics:** Content accuracy and relevance scoring

#### Knowledge Sharing Mechanisms
- **Distribution Channels:** Internal wikis, team meetings, newsletters
- **Onboarding Integration:** New team member training materials
- **Cross-Team Sessions:** Regular knowledge transfer meetings
- **Access Controls:** Appropriate permissions and search capabilities

### Future Planning

#### Roadmap
- **Enhancement Timeline:** Planned improvements with delivery dates
- **Integration Plans:** Cross-protocol coordination initiatives
- **Automation Expansion:** Progressive automation targets

#### Priorities
- **Initiative Ranking:** Prioritized improvement list
- **Resource Allocation:** Required capacity and skills
- **Benefit Analysis:** Expected ROI for each initiative

#### Resource Requirements
- **Development Effort:** Engineering hours and skill requirements
- **Infrastructure Needs:** Tools, systems, and platforms
- **Team Capacity:** Staffing and training requirements

#### Timeline
- **Milestone Schedule:** Major enhancement delivery dates
- **Dependency Mapping:** Cross-team and system dependencies
- **Risk Mitigation:** Contingency planning and buffers

---

## INTEGRATION POINTS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for inputs/outputs and artifact storage -->

### Input Standards
**Inputs From:**
- **Protocol 04:** 
  - `bootstrap-manifest.json` - Generated scaffold inventory
  - `governance-status.md` - Modern bootstrap outputs guiding legacy alignment
  
- **Protocol 03:**
  - `PROJECT-BRIEF.md` - Reference for documentation tone and scope

### Output Standards
**Outputs To:**
- **Protocol 08:**
  - `.cursor/context-kit/README.md` - Context documentation for task generation
  - `template-inventory.md` - Available templates for task generation
  
- **Protocol 23:**
  - `rule-audit-final.md` - Evidence for script governance alignment
  
- **Protocol 02 or 24:**
  - `architecture-principles.md` - Canonical conventions for discovery
  - Decision point documentation for protocol selection

### Artifact Storage Standards
**Storage Locations:**
- **Primary Evidence:** `.artifacts/protocol-05/` - All protocol execution artifacts
- **Context Assets:** `.cursor/context-kit/` - Context and configuration files
- **Rule Files:** `.cursor/rules/` - Governance rule definitions

---

## QUALITY GATES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting validation standards and criteria -->

### Gate 1: Governance Activation Gate
- **Criteria:** Cursor rule migration completed, metadata validated, tooling confirmation logged
- **Evidence:** `.artifacts/protocol-05/rule-migration-report.md`, `.artifacts/protocol-05/tooling-confirmation.log`
- **Pass Threshold:** All migrated files contain valid YAML frontmatter
- **Failure Handling:** Remediate missing metadata, rerun migration steps, document corrections
- **Automation:** `python scripts/validate_rule_metadata.py --path .cursor/rules/`

### Gate 2: Repository Mapping Gate
- **Criteria:** Repository structure captured, analysis plan approved by user, detected stack file generated
- **Evidence:** `.artifacts/protocol-05/repo-structure.txt`, `.artifacts/protocol-05/analysis-plan.md`, `.cursor/bootstrap/detected-stack.json`
- **Pass Threshold:** User approval recorded and stack detection coverage ≥ 90%
- **Failure Handling:** Revise analysis plan, gather missing files, rerun detection
- **Automation:** `python scripts/validate_repo_mapping.py --structure .artifacts/protocol-05/repo-structure.txt`

### Gate 3: Principle Validation Gate
- **Criteria:** Investigation themes approved, findings documented, validation brief acknowledged by user
- **Evidence:** `.artifacts/protocol-05/investigation-themes.md`, `.artifacts/protocol-05/theme-findings.json`, `.artifacts/protocol-05/validation-brief.md`
- **Pass Threshold:** User confirmation recorded; outstanding questions < 3 critical items
- **Failure Handling:** Address feedback, update findings, rerun gate
- **Automation:** `python scripts/validate_principles.py --input .artifacts/protocol-05/theme-findings.json`

### Gate 4: Governance Alignment Gate
- **Criteria:** Documentation updates approved, rule audit final report passes, template inventory generated
- **Evidence:** `.artifacts/protocol-05/documentation-plan.md`, `.artifacts/protocol-05/rule-audit-final.md`, `.cursor/context-kit/template-inventory.md`
- **Pass Threshold:** Rule audit severity ≤ Medium and documentation approvals recorded
- **Failure Handling:** Resolve audit findings, update docs/rules, rerun validation
- **Automation:** `python scripts/rules_audit_quick.py --output .artifacts/protocol-05/rule-audit-final.md`

---

## COMMUNICATION PROTOCOLS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting communication standards and templates -->

### Status Announcement Standards
```
[MASTER RAY™ | PHASE 1 START] - "Activating governance tooling and migrating rules for legacy bootstrap."
[MASTER RAY™ | PHASE 2 START] - "Mapping repository structure and confirming analysis targets."
[MASTER RAY™ | PHASE 3 START] - "Performing thematic investigations to extract architecture principles."
[MASTER RAY™ | PHASE 4 START] - "Presenting findings and initializing context kit."
[MASTER RAY™ | PHASE 5 START] - "Updating documentation and normalizing project rules."
[MASTER RAY™ | PHASE 6 START] - "Finalizing project rules and cataloging template inventory."
[PHASE COMPLETE] - "Legacy bootstrap alignment complete; evidence archived."
[RAY ERROR] - "Encountered issue during [phase]; refer to associated artifact for remediation."
```

### Validation Prompt Standards
```
[RAY CONFIRMATION REQUIRED]
> "Bootstrap analysis findings ready for validation. Evidence prepared:
> - repo-structure.txt
> - analysis-plan.md
> - theme-findings.json
>
> Please confirm accuracy before documentation and rule updates proceed."
```

### Error Handling Standards
```
[RAY GATE FAILED: Principle Validation Gate]
> "Quality gate 'Principle Validation' failed.
> Criteria: Validated findings with fewer than three unresolved critical questions.
> Actual: Four critical questions remain unanswered.
> Required action: Schedule follow-up investigation, update validation-brief.md, rerun gate.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## AUTOMATION HOOKS
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple execution of validation scripts with clear steps -->

**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.

### Validation Scripts

1. **Prerequisite Validation:**
   * **Action:** Execute prerequisite checks
   * **Command:** `python scripts/validate_prerequisites_0.py`
   * **Evidence:** Validation output log
   * **Validation:** Exit code 0

2. **Quality Gate Automation:**
   * **Action:** Run automated quality gate validations
   * **Commands:**
     ```bash
     python scripts/validate_rule_metadata.py --path .cursor/rules/
     python scripts/validate_repo_mapping.py --structure .artifacts/protocol-05/repo-structure.txt
     python scripts/validate_principles.py --input .artifacts/protocol-05/theme-findings.json
     python scripts/rules_audit_quick.py --output .artifacts/protocol-05/rule-audit-final.md
     ```
   * **Evidence:** Individual validation reports
   * **Validation:** All scripts return success status

3. **Evidence Aggregation:**
   * **Action:** Collect and organize all evidence artifacts
   * **Command:** `python scripts/aggregate_evidence_0.py --output .artifacts/protocol-05/`
   * **Evidence:** Aggregated evidence manifest
   * **Validation:** All required artifacts present

### CI/CD Integration
```yaml
name: Protocol 05 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 05 Gates
        run: python scripts/run_protocol_0_gates.py
```

### Manual Fallback Procedures
When automation is unavailable, execute manual validation:

1. **Manual Rule Review:**
   * **Action:** Review rules manually for metadata compliance
   * **Evidence:** `manual-rule-review.md` with reviewer initials
   * **Validation:** Checklist completion

2. **Repository Walkthrough:**
   * **Action:** Conduct manual repository walkthrough meeting
   * **Evidence:** `.artifacts/protocol-05/manual-walkthrough-notes.md`
   * **Validation:** Meeting minutes documented

3. **Validation Documentation:**
   * **Action:** Document all manual validation results
   * **Evidence:** `.artifacts/protocol-05/manual-validation-log.md`
   * **Validation:** Comprehensive log with timestamps

---
## HANDOFF CHECKLIST
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple checklist execution for protocol completion -->

### Continuous Improvement Validation

1. **Execution Feedback Collection:**
   * **Action:** Collect and log execution feedback
   * **Evidence:** Feedback documented in protocol artifacts
   * **Validation:** [ ] Feedback collected and logged

2. **Lessons Learned Documentation:**
   * **Action:** Document lessons learned in protocol artifacts
   * **Evidence:** Lessons captured in retrospective report
   * **Validation:** [ ] Lessons learned documented

3. **Quality Metrics Capture:**
   * **Action:** Record quality metrics for improvement tracking
   * **Evidence:** Metrics logged in tracking system
   * **Validation:** [ ] Quality metrics captured

4. **Knowledge Base Update:**
   * **Action:** Update knowledge base with new patterns or insights
   * **Evidence:** Knowledge base entries created/updated
   * **Validation:** [ ] Knowledge base updated

5. **Protocol Adaptation Opportunities:**
   * **Action:** Identify and log protocol adaptation opportunities
   * **Evidence:** Opportunities documented in improvement log
   * **Validation:** [ ] Adaptation opportunities identified and logged

6. **Retrospective Scheduling:**
   * **Action:** Schedule retrospective if required for this phase
   * **Evidence:** Meeting scheduled and participants notified
   * **Validation:** [ ] Retrospective scheduled (if required)

### Pre-Handoff Validation
Before declaring protocol complete, validate:

1. **Prerequisites Verification:**
   * **Action:** Confirm all prerequisites were met
   * **Evidence:** Prerequisites checklist completed
   * **Validation:** [ ] All prerequisites met

2. **Workflow Completion:**
   * **Action:** Verify all workflow steps completed successfully
   * **Evidence:** Step completion logs
   * **Validation:** [ ] All workflow steps completed

3. **Quality Gate Passage:**
   * **Action:** Confirm all quality gates passed or waivers documented
   * **Evidence:** Gate validation reports
   * **Validation:** [ ] All quality gates passed

4. **Evidence Capture:**
   * **Action:** Verify all evidence artifacts captured and stored
   * **Evidence:** Evidence manifest complete
   * **Validation:** [ ] All evidence artifacts captured

5. **Integration Output Generation:**
   * **Action:** Confirm all integration outputs generated
   * **Evidence:** Output artifacts present
   * **Validation:** [ ] All integration outputs generated

6. **Automation Execution:**
   * **Action:** Verify all automation hooks executed successfully
   * **Evidence:** Automation execution logs
   * **Validation:** [ ] All automation hooks executed

7. **Communication Log:**
   * **Action:** Confirm communication log is complete
   * **Evidence:** All required communications documented
   * **Validation:** [ ] Communication log complete

### Handoff to Protocol 02 or 24

**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 02 (Standard Discovery) or Protocol 24 (Alternate Track)

**Decision Point:** See `documentation/protocol-branching-guide.md` to choose between:
- **Protocol 02:** Standard comprehensive discovery (waterfall, new clients, formal process)
- **Protocol 24:** Alternate quick discovery (agile, existing clients, lean process)

**Evidence Package:**
- `architecture-principles.md` - Canonical conventions for discovery
- `template-inventory.md` - Available accelerators for discovery-led customization

**Execution:**
```bash
# Trigger next protocol (choose one)
@apply .cursor/ai-driven-workflow/02-client-discovery-initiation.md
# OR
@apply .cursor/ai-driven-workflow/24-client-discovery.md
```

---

## EVIDENCE SUMMARY
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for evidence collection and quality metrics -->

### Learning and Improvement Mechanisms

#### Feedback Collection Standards
- **Artifact Feedback:** All artifacts generate feedback for continuous improvement
- **Quality Gate Tracking:** Historical logs maintain gate outcome patterns
- **Pattern Analysis:** Regular analysis for threshold calibration

#### Improvement Tracking Standards
- **Execution Metrics:** Quarterly monitoring of protocol performance
- **Template Evolution:** Change logging with before/after comparisons
- **Knowledge Updates:** Knowledge base refresh after every 5 executions

#### Knowledge Integration Standards
- **Pattern Cataloging:** Execution patterns stored in institutional knowledge base
- **Best Practice Documentation:** Proven approaches shared across teams
- **Blocker Resolution:** Common issues maintained with proven solutions

#### Adaptation Standards
- **Context Adaptation:** Protocol adjusts based on project complexity, domain, constraints
- **Threshold Tuning:** Quality gates adjust dynamically based on risk tolerance
- **Workflow Optimization:** Efficiency improvements based on historical data

### Generated Artifacts
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `rule-migration-report.md` | `.artifacts/protocol-05/` | Proof of governance activation | Protocol 23 |
| `analysis-plan.md` | `.artifacts/protocol-05/` | Approved repository analysis scope | Protocol 08 |
| `theme-findings.json` | `.artifacts/protocol-05/` | Captured architectural principles | Protocol 04-CD |
| `rule-audit-final.md` | `.artifacts/protocol-05/` | Final rule validation evidence | Protocol 23 |
| `template-inventory.md` | `.cursor/context-kit/` | Template availability summary | Protocol 08 |
| `repo-structure.txt` | `.artifacts/protocol-05/` | Repository mapping documentation | Protocol 08 |
| `detected-stack.json` | `.cursor/bootstrap/` | Technology stack identification | Protocol 08 |
| `validation-brief.md` | `.artifacts/protocol-05/` | User validation checkpoint | Audit trail |
| `architecture-principles.md` | `.artifacts/protocol-05/` | Synthesized principles | Protocol 02/24 |
| `documentation-plan.md` | `.artifacts/protocol-05/` | README update strategy | Documentation |
| `investigation-themes.md` | `.artifacts/protocol-05/` | Thematic analysis framework | Protocol 08 |
| `README.md` | `.cursor/context-kit/` | Context kit documentation | Multiple protocols |

### Traceability Matrix

#### Upstream Dependencies
- **Input Artifacts:** Inherited from Protocol 04 (bootstrap-manifest.json, governance-status.md) and Protocol 03 (PROJECT-BRIEF.md)
- **Configuration Dependencies:** Scripts directory, Cursor editor (optional), rule directories
- **External Dependencies:** Python runtime, shell command execution, file system access

#### Downstream Consumers
- **Output Consumers:** Protocol 08 (primary), Protocol 23 (governance), Protocol 02 or 24 (discovery)
- **Shared Artifacts:** Context kit used by multiple protocols
- **Archive Requirements:** 90-day retention for evidence artifacts

#### Verification Chain
- **Artifact Integrity:** SHA-256 checksum, timestamp, verified_by field
- **Verification Procedure:** Automated validation via scripts, manual review for user approvals
- **Audit Trail:** All modifications logged in protocol execution log

### Quality Metrics
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Gate 2 Pass Rate | ≥ 90% | [TBD] | ⏳ |
| Gate 3 Pass Rate | ≥ 85% | [TBD] | ⏳ |
| Gate 4 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
| User Approval Rate | ≥ 90% | [TBD] | ⏳ |

---

## REASONING & COGNITIVE PROCESS
<!-- [Category: META-FORMATS] -->
<!-- Why: Meta-level protocol analysis and reasoning patterns documentation -->

### Reasoning Patterns

#### Primary Pattern: Systematic Execution
- **Approach:** Sequential protocol execution with validation checkpoints
- **Validation:** Quality gates at each major phase transition
- **Evidence:** Comprehensive artifact generation for traceability

#### Secondary Pattern: Quality-Driven Validation
- **Approach:** Multi-layered quality assurance through automated and manual gates
- **Validation:** Threshold-based pass/fail criteria with clear remediation paths
- **Evidence:** Detailed validation reports for each gate

#### Pattern Improvement Strategy
- **Effectiveness Tracking:** Monitor gate pass rates and downstream feedback
- **Review Cadence:** Quarterly pattern effectiveness assessment
- **Iteration Process:** Evidence-based pattern refinement from execution data

### Decision Logic

#### Decision Point 1: Execution Readiness
**Context:** Determining if prerequisites are met to begin protocol execution

**Decision Criteria:**
- All prerequisite artifacts present and valid
- Required approvals obtained and documented
- System state validated and healthy

**Outcomes:**
- **Proceed:** Execute protocol workflow with full automation
- **Halt:** Document missing prerequisites, notify stakeholders, await resolution

**Logging:** Record decision rationale and prerequisites status in execution log

#### Decision Point 2: Protocol Handoff Selection
**Context:** Choosing between Protocol 02 (standard) or Protocol 24 (alternate) for discovery

**Decision Criteria:**
- Client relationship status (new vs. existing)
- Project methodology preference (waterfall vs. agile)
- Process requirements (formal vs. lean)

**Outcomes:**
- **Protocol 02:** Standard comprehensive discovery process
- **Protocol 24:** Alternate quick discovery process

**Logging:** Document selection rationale in handoff checklist

### Root Cause Analysis Framework

When protocol execution encounters blockers or quality gate failures:

1. **Identify Symptom:**
   - What immediate issue prevented progress?
   - Which quality gate or step failed?
   - What error messages or indicators appeared?

2. **Trace to Root Cause:**
   - Was prerequisite artifact missing or incomplete?
   - Did upstream protocol deliver inadequate inputs?
   - Were instructions ambiguous or insufficient?
   - Did environmental conditions fail?
   - Was user approval delayed or denied?

3. **Document in Protocol Execution Log:**
   ```markdown
   **Blocker:** [Description of blocking issue]
   **Root Cause:** [Analysis of underlying cause]
   **Resolution:** [Action taken to resolve]
   **Prevention:** [Process/template update to prevent recurrence]
   ```

4. **Implement Fix:**
   - Update protocol documentation if needed
   - Re-engage stakeholders for missing inputs
   - Adjust execution parameters
   - Resolve environmental issues

5. **Validate Fix:**
   - Re-run failed quality gates
   - Confirm resolution with evidence
   - Document lessons learned

### Learning Mechanisms

#### Feedback Loops
**Purpose:** Establish continuous feedback collection to inform protocol improvements

- **Execution Feedback:** Outcome data collected after each protocol run
- **Quality Gate Outcomes:** Pass/fail patterns tracked in historical logs
- **Downstream Protocol Feedback:** Issues reported by dependent protocols captured
- **Continuous Monitoring:** Automated alerts for anomalies and performance degradation

#### Improvement Tracking
**Purpose:** Systematically track protocol effectiveness improvements over time

- **Metrics Tracking:** KPIs monitored in quarterly dashboards
- **Template Evolution:** All protocol changes logged with rationale and impact
- **Effectiveness Measurement:** Before/after metrics compared for each improvement
- **Continuous Monitoring:** Automated alerts when metrics degrade below thresholds

#### Knowledge Base Integration
**Purpose:** Build and leverage institutional knowledge to accelerate protocol quality

- **Pattern Library:** Repository of successful execution patterns maintained
- **Best Practices:** Proven approaches documented for common scenarios
- **Common Blockers:** Typical issues cataloged with proven resolutions
- **Industry Templates:** Specialized variations for specific domains created

#### Adaptation Mechanisms
**Purpose:** Enable protocol to automatically adjust based on context and patterns

- **Context Adaptation:** Execution adjusted based on project type, complexity, constraints
- **Threshold Tuning:** Quality gate thresholds modified based on risk tolerance
- **Workflow Optimization:** Steps streamlined based on historical efficiency data
- **Tool Selection:** Optimal automation chosen based on available resources

### Meta-Cognition

#### Self-Awareness and Process Awareness
**Purpose:** Enable AI to maintain explicit awareness of execution state and limitations

**Awareness Statement Protocol:**
At each major execution checkpoint, generate awareness statement:
- Current phase and step status
- Artifacts completed vs. pending
- Identified blockers and their severity
- Confidence level in current outputs
- Known limitations and assumptions
- Required inputs for next steps

#### Process Monitoring and Progress Tracking
**Purpose:** Continuously track execution status and detect anomalies

- **Progress Tracking:** Execution status updated after each step
- **Velocity Monitoring:** Execution delays flagged beyond expected duration
- **Quality Monitoring:** Gate pass rates and artifact completeness tracked
- **Anomaly Detection:** Alerts triggered on unexpected patterns or deviations

#### Self-Correction Protocols
**Purpose:** Enable autonomous detection and correction of execution issues

- **Halt Condition Detection:** Blockers recognized and escalated appropriately
- **Quality Gate Failure Handling:** Corrective action plans generated automatically
- **Anomaly Response:** Diagnoses and fixes proposed for unexpected conditions
- **Recovery Procedures:** Execution state maintained for graceful resume

#### Continuous Improvement Integration
**Purpose:** Systematically capture lessons and evolve protocol effectiveness

- **Retrospective Execution:** After-action reviews conducted post-completion
- **Template Review Cadence:** Scheduled protocol enhancement cycles implemented
- **Gate Calibration:** Periodic adjustment of pass criteria based on data
- **Tool Evaluation:** Assessment of automation effectiveness performed regularly
