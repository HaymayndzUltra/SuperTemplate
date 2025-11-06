---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 02: CLIENT DISCOVERY INITIATION (PROJECT-SCOPING COMPLIANT)

**Purpose:** Equip the solo developer with a complete pre-call discovery toolkit derived from the job post, accepted proposal, and any client replies. All outputs remain internal until the live discovery call concludes, after which they feed Protocol 03 once confirmed.

## IDENTITY & OWNERSHIP

### Protocol Identity
- **Protocol ID:** 02
- **Protocol Name:** Client Discovery Initiation
- **Protocol Owner:** Discovery Call Lead
- **Owner Contact:** [Email/Slack]
- **Created:** 2025-01-01
- **Last Updated:** 2025-11-06
- **Version:** 2.0

### Protocol Classification
- **Category:** Execution
- **Criticality:** High
- **Complexity:** Medium
- **Scope:** Module

### Protocol Lineage
- **Predecessor:** Protocol 01 (Client Proposal Generation)
- **Successor:** Protocol 03 (Project Brief Creation)
- **Related Protocols:** Protocol 04 (Project Bootstrap)

### Protocol Metadata
- **Purpose:** Conduct discovery call with comprehensive pre-call preparation and post-call documentation
- **Success Criteria:** All 4 quality gates pass, discovery artifacts complete for Protocol 03
- **Failure Modes:** Incomplete preparation, missing call recording, unclear requirements capture
- **Recovery Procedure:** Re-engage client for clarification, document gaps, schedule follow-up if needed

---

## ROLES & RESPONSIBILITIES

### Primary Roles

#### Protocol Executor
- **Role:** Discovery Call Lead
- **Responsibilities:**
  - Prepare pre-call materials
  - Conduct discovery call
  - Document outcomes and decisions
  - Generate post-call artifacts
- **Authority:** Can request clarifications and schedule follow-ups
- **Escalation:** Project Manager for scope issues

#### Protocol Owner
- **Role:** Discovery Call Lead (same as executor)
- **Responsibilities:**
  - Approve call agenda
  - Review pre-call preparation
  - Sign off on discovery outcomes
  - Validate handoff to Protocol 03
- **Authority:** Final decision on requirements interpretation

#### Downstream Owner
- **Role:** Brief Creator (Protocol 03 owner)
- **Responsibilities:**
  - Receive discovery artifacts
  - Validate completeness of requirements
  - Request clarifications if needed
  - Confirm readiness for brief creation
- **Authority:** Can request additional discovery if gaps exist

### Role Interactions
- **Executor → Owner:** Self-review for Protocol 02
- **Owner → Downstream:** Handoff via discovery summary and call notes
- **Downstream → Executor:** Feedback on discovery quality and completeness

### Decision Authority Matrix
| Decision Type | Executor | Owner | Downstream | Executive |
|---------------|----------|-------|------------|-----------|
| Call Agenda | ✅ | ✅ | ❌ | ❌ |
| Requirement Interpretation | ✅ | ✅ | ❌ | ❌ |
| Scope Definition | ❌ | ✅ | ❌ | ✅ |
| Follow-up Calls | ✅ | ✅ | ❌ | ❌ |
| Protocol Changes | ❌ | ❌ | ❌ | ✅ |

---

## 1. PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT] All prerequisites must be met before protocol execution.**

### Required Artifacts
**[STRICT]** The following source artifacts must exist:
- `PROPOSAL.md` from Protocol 01 (accepted proposal content)
- `proposal-summary.json` from Protocol 01 (proposal highlights)
- Job post copy saved as `.artifacts/protocol-01/job-post.md`
- Client reply transcript saved as `.artifacts/protocol-02/client-reply.md` (optional if no response yet)

### Required Assignment
**[STRICT]**
- Developer assigned as discovery owner with access to Cursor workspace and `.cursor/rules/`
- Meeting link placeholder or scheduled discovery call invitation

### System State Requirements
**[STRICT]** System must meet the following conditions:
- Access to discovery templates in `.artifacts/protocol-02/templates/`
- Optional scripts available: `summarize_job_post.py`, `assumption_extractor.py`, `integration_inventory_prefill.py`

---

## 2. AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

You are a **Solo Lead Developer** preparing for a discovery call. Your mission is to convert available written inputs into a validated discovery toolkit that:
1. Establishes clear understanding of business goals and constraints.
2. Lists every unanswered item to confirm live with the client.
3. Generates Protocol 03 prerequisite artifacts immediately after call updates.

**[STRICT] AI assistance is limited to internal data preparation, note structuring, and checklists. All client interactions remain human-led.**

---

## 3. WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### PHASE 1: Context Consolidation (Pre-Call Intelligence)
<!-- [Category: EXECUTION-BASIC] -->

**Reasoning Pattern:** Extract-before-interpret heuristic — systematically extract all available information from source documents before attempting interpretation or synthesis. This prevents premature assumption formation and ensures comprehensive coverage.

**Example Scenario:** When analyzing a job post that mentions "e-commerce platform," extract all specific requirements (payment processing, inventory management, shipping integration) before assuming which features are in-scope. This ensures no critical requirements are missed during discovery call preparation.

**Strategy Rationale:** Because written proposals may overlook subtle requirements or constraints, extracting verbatim information first creates a complete baseline. Therefore, interpretation happens with full context, reducing the risk of assumptions that require correction during the live call.

**Decision Tree:** When building discovery brief:
- **IF** job post contains clear business goals → Extract verbatim with source citation
- **ELSE IF** goals are vague → Mark as `ASSUMPTION` in assumptions tracker
- **IF** proposal commitments conflict with job post → Flag as `RISK` requiring client confirmation
- **THEN** Log decision rationale in discovery brief validation notes

1. **`[MUST]` Build Discovery Brief**
   * **Action:** Summarize job post and proposal commitments into `discovery-brief.md`, covering Business Goals, Target Users, Success Metrics, Constraints, and Client Tone.
   * **Reasoning:** Use extract-before-interpret pattern to systematically gather information before synthesis. Apply decision tree above when encountering ambiguous or conflicting information.
   * **Problem-Solving:** If source documents are incomplete or contradictory, identify root cause (missing context, ambiguous requirements, or conflicting priorities) and document mitigation strategy (flag for client confirmation, research alternative sources, or escalate to proposal owner).
   * **Evidence:** `.artifacts/protocol-02/discovery-brief.md`
   * **Validation:** Each section cites source line references.

2. **`[MUST]` Compile Assumptions & Gap Tracker**
   * **Action:** Identify assumptions and missing data; record in `assumptions-gaps.md` with status (`confirmed`, `ASK CLIENT`, `research`).
   * **Reasoning:** Apply assumption validation pattern — every assumption must be traceable to its source and have a validation path (client confirmation, research, or test hypothesis).
   * **Decision Criteria:** When categorizing assumptions:
  - **ASK CLIENT:** Requires client expertise or preference (e.g., "What is your preferred tech stack?")
  - **RESEARCH:** Can be answered through independent investigation (e.g., "What are industry standards for this feature?")
  - **CONFIRMED:** Already validated in proposal or previous communication
   * **Evidence:** `.artifacts/protocol-02/assumptions-gaps.md`
   * **Validation:** Every proposal assumption mapped to a follow-up action.

3. **`[GUIDELINE]` Draft Risk & Opportunity Radar**
   * **Action:** Generate `risk-opportunity-list.md` with initial risks, blockers, and upside notes.
   * **Reasoning:** Use risk taxonomy pattern — categorize risks by type (technical, business, timeline, resource) and severity (blocker, high, medium, low). For each risk, document root cause analysis, impact assessment, and mitigation strategy.
   * **Problem-Solving Logic:** When identifying risks:
  1. **Problem Identification:** Extract potential blockers from proposal assumptions, technical constraints, and timeline dependencies
  2. **Root Cause Analysis:** Trace each risk to its underlying cause (e.g., "Unclear integration requirements" → Root cause: "No access to third-party API documentation")
  3. **Solution Development:** Propose mitigation strategies (e.g., "Request API documentation as discovery question")
  4. **Validation:** Confirm mitigation strategy is actionable and has success criteria
   * **Evidence:** `.artifacts/protocol-02/risk-opportunity-list.md`
   * **Validation:** At least three risks documented with impact and mitigation idea.

### PHASE 2: Question & Scenario Preparation
<!-- [Category: EXECUTION-BASIC] -->

**Reasoning Pattern:** Structured interrogation strategy — organize questions by discovery theme (business, technical, operational) and prioritize by dependency order (blocking questions first, then clarifying questions, then optimization questions).

**Example Scenario:** For a fintech project, business questions about regulatory compliance must be answered before technical questions about payment processing architecture. Therefore, P0 questions focus on compliance requirements, while P1 questions explore technical implementation details.

**Strategy Rationale:** Because Protocol 03 handoff depends on confirmed business goals and technical constraints, prioritizing blocking questions ensures critical prerequisites are addressed first. This systematic approach prevents discovery call from running out of time before addressing essential questions.

**Meta-Cognitive Check:** Before generating questions, assess your own limitations:
- **Awareness:** Recognize that written proposals may not capture client's true priorities or constraints
- **Limitations:** Acknowledge that certain information requires live conversation to clarify nuance
- **Capacity:** Understand that discovery call duration limits the number of questions that can be thoroughly addressed
- **Correction:** Be prepared to adjust question prioritization based on pre-call client responses or new information

**Learning Mechanism:** Track which question categories yield the most valuable insights and refine future discovery question banks accordingly. Document patterns in `lessons-learned.md`.

1. **`[MUST]` Generate Themed Question Bank**
   * **Action:** Populate `question-bank.md` with prioritized questions grouped by Business Outcomes, User Journeys, Functional Scope, Technical Stack, Integrations, Compliance, and Delivery Logistics.
   * **Reasoning:** Apply structured interrogation strategy — prioritize questions that unblock Protocol 03 prerequisites (business goals, technical constraints, timeline commitments).
   * **Decision Criteria:** When prioritizing questions:
  - **P0 (Must-Ask):** Questions that block Protocol 03 handoff (e.g., MVP scope, acceptance criteria)
  - **P1 (Should-Ask):** Questions that clarify key assumptions (e.g., "Who owns integration X?")
  - **P2 (Nice-to-Ask):** Questions that optimize delivery (e.g., "What's your preferred testing approach?")
   * **Evidence:** `.artifacts/protocol-02/question-bank.md`
   * **Validation:** Every `ASK CLIENT` item in `assumptions-gaps.md` links to at least one question ID.

2. **`[MUST]` Prefill Integration & Dependency Inventory**
   * **Action:** Create `integration-inventory.md` listing known systems, data owners, access requirements, and risk flags. Mark unknown fields with `@ASK_CLIENT` and tie them to the question bank.
   * **Reasoning:** Use dependency mapping pattern — identify which integrations are blocking (required for MVP) versus optional (post-MVP enhancements). Apply decision tree:
  - **IF** integration is mentioned in proposal → Extract details and mark as `CONFIRMED` or `NEEDS_CLARIFICATION`
  - **IF** integration is not mentioned but logically required → Mark as `ASSUMPTION` and create discovery question
  - **IF** integration status unknown → Mark as `@ASK_CLIENT` and link to question bank
   * **Problem-Solving:** When encountering incomplete integration information:
  1. **Root Cause:** Identify why information is missing (not captured in proposal, client oversight, or intentionally deferred)
  2. **Solution:** Create targeted discovery questions to fill gaps
  3. **Validation:** Verify integration inventory completeness before call
   * **Evidence:** `.artifacts/protocol-02/integration-inventory.md`
   * **Validation:** Table covers System, Purpose, Owner, Data Availability, Risk, Next Action.

3. **`[GUIDELINE]` Prepare Scenario Response Guides**
   * **Action:** Document `scenario-guides.md` covering likely pivots (budget adjustment, scope expansion, compliance gaps) with trigger phrases, recommended responses, and fallback plans.
   * **Reasoning:** Apply scenario planning heuristic — anticipate three most likely pivot scenarios based on proposal assumptions and client communication patterns. For each scenario, document:
  - **Trigger Phrases:** Client statements that indicate pivot (e.g., "Actually, we also need...")
  - **Impact Assessment:** How pivot affects timeline, budget, and technical scope
  - **Mitigation Strategy:** Recommended response that protects proposal commitments while accommodating client needs
   * **Evidence:** `.artifacts/protocol-02/scenario-guides.md`
   * **Validation:** Minimum of three scenarios mapped to proposal commitments.

### PHASE 3: Call Logistics & Live Support Setup
<!-- [Category: EXECUTION-BASIC] -->

**Reasoning Pattern:** Fail-fast validation pattern — verify all prerequisites are met before call begins. If any critical artifact is missing or incomplete, halt and complete before proceeding.

**Example Scenario:** If `question-bank.md` is incomplete but call is scheduled in 30 minutes, fail-fast pattern requires completing the question bank before joining the call. This prevents the discovery call from proceeding without proper preparation, which could result in missed critical questions.

**Strategy Rationale:** Because discovery calls are time-limited and cannot be easily rescheduled, ensuring all prerequisites are complete before the call maximizes the value of the conversation. Therefore, detecting gaps early allows time for remediation rather than discovering gaps during the call itself.

**Decision Tree:** When preparing for call:
- **IF** all pre-call artifacts complete → Mark `ready-for-call-summary.md` as `pre_call_ready`
- **ELSE IF** critical artifacts missing → Identify blockers and create action plan
- **IF** question bank incomplete → Prioritize questions by Protocol 03 blocking status
- **THEN** Log readiness status and remaining actions

1. **`[MUST]` Assemble Call Agenda & Checklist**
   * **Action:** Create `call-agenda.md` including introductions, discovery themes, wrap-up, plus reminders (recording consent, recap send deadline, follow-up owner).
   * **Reasoning:** Apply structured facilitation pattern — organize agenda by time blocks (introduction: 5 min, discovery themes: 45 min, wrap-up: 10 min) to ensure all priority questions are addressed.
   * **Problem-Solving:** If scheduled call duration is insufficient for all questions:
  1. **Root Cause:** Too many questions or inadequate prioritization
  2. **Solution:** Focus on P0 questions first, defer P1/P2 to follow-up
  3. **Validation:** Verify agenda duration matches scheduled meeting time
   * **Evidence:** `.artifacts/protocol-02/call-agenda.md`
   * **Validation:** Agenda duration matches scheduled meeting; checklist covers Cursor context load, question bank review, and equipment check.

2. **`[MUST]` Prepare Live Notes Template**
   * **Action:** Build `discovery-call-notes.md` aligned to the question bank, with columns `Client Notes`, `Action`, `Owner`, `Due Date`, `Status` (`confirmed`, `follow-up`, `risk`).
   * **Reasoning:** Use structured note-taking pattern — link each note to its source question ID for traceability. Apply decision criteria when categorizing notes:
  - **CONFIRMED:** Client provided definitive answer
  - **FOLLOW-UP:** Requires additional research or client input
  - **RISK:** Identified blocker or concern requiring mitigation
   * **Evidence:** `.artifacts/protocol-02/discovery-call-notes.md`
   * **Validation:** Template ready for real-time copy/paste and tagging.

3. **`[MUST]` Produce Ready-for-Call Summary**
   * **Action:** Summarize artifact readiness in `ready-for-call-summary.md`, list top unanswered questions, risk watchlist, and confirm whether artifacts were loaded into `.cursor/rules/`.
   * **Reasoning:** Apply readiness validation pattern — before call, verify all prerequisites met and identify any remaining blockers. Document status explicitly to enable fail-fast decision making.
   * **Evidence:** `.artifacts/protocol-02/ready-for-call-summary.md`
   * **Validation:** Status field set to `pre_call_ready`; outstanding items reference question IDs.

### PHASE 4: Post-Call Consolidation
<!-- [Category: EXECUTION-BASIC] -->

**Reasoning Pattern:** Consolidation-before-handoff heuristic — systematically consolidate all call outcomes into validated artifacts before attempting Protocol 03 handoff. This ensures downstream protocol receives complete, validated inputs.

**Example Scenario:** After discovery call, consolidate all confirmed answers into `client-discovery-form.md`, resolve all `@ASK_CLIENT` tags in integration inventory, and validate that all Protocol 03 prerequisites are satisfied before triggering next protocol. This prevents Protocol 03 from starting with incomplete or ambiguous inputs.

**Strategy Rationale:** Because Protocol 03 depends on validated discovery artifacts, consolidating outcomes before handoff ensures downstream protocol has all required information. Therefore, systematic consolidation reduces the risk of Protocol 03 execution failures due to missing or ambiguous inputs.

**Learning Mechanism:** After each call, track which discovery questions yielded most valuable insights and refine question bank accordingly. Document patterns in `lessons-learned.md` for continuous improvement.

1. **`[MUST]` Update Client Discovery Form**
   * **Action:** Transfer confirmed answers into `client-discovery-form.md`, including MVP scope, acceptance criteria, priorities, and notes on open items.
   * **Reasoning:** Use systematic transfer pattern — map each call note to its corresponding section in discovery form. Apply validation criteria to ensure completeness.
   * **Problem-Solving:** If call notes are incomplete or ambiguous:
  1. **Root Cause:** Inadequate note-taking during call or missing follow-up questions
  2. **Solution:** Document ambiguities as `FOLLOW-UP` items with owner and due date
  3. **Validation:** Verify no feature remains without owner, priority, and acceptance detail
   * **Evidence:** `.artifacts/protocol-02/client-discovery-form.md`
   * **Validation:** No feature remains without owner, priority, and acceptance detail; unresolved items flagged `follow-up` with next action.

2. **`[MUST]` Refresh Technical Scope & Integrations**
   * **Action:** Update `scope-clarification.md` and `integration-inventory.md` with final stack decisions, integration owners, access status, and constraints.
   * **Reasoning:** Apply dependency resolution pattern — resolve all `@ASK_CLIENT` tags with confirmed answers or reassign with follow-up action. Document decision rationale for each integration.
   * **Decision Criteria:** When updating integration status:
  - **CONFIRMED:** Client confirmed integration details during call
  - **NEEDS_FOLLOW-UP:** Requires additional information from client or third party
  - **DEFERRED:** Intentionally postponed to post-MVP phase
   * **Evidence:** `.artifacts/protocol-02/scope-clarification.md`, `.artifacts/protocol-02/integration-inventory.md`
   * **Validation:** All `@ASK_CLIENT` tags resolved or reassigned with follow-up owner and due date.

3. **`[MUST]` Finalize Timeline & Milestones**
   * **Action:** Record agreed milestones, dependencies, and budget guardrails in `timeline-discussion.md`; mark conflicts and mitigation steps.
   * **Reasoning:** Use timeline validation pattern — verify milestones are realistic given technical constraints and resource availability. Document any conflicts and their mitigation strategies.
   * **Evidence:** `.artifacts/protocol-02/timeline-discussion.md`
   * **Validation:** Document lists start date, key checkpoints, decision gates, and risk indicators.

4. **`[MUST]` Confirm Collaboration Plan**
   * **Action:** Capture cadence, tools, timezone overlap, and escalation steps in `communication-plan.md`, noting solo reminders where applicable.
   * **Reasoning:** Apply communication clarity pattern — explicitly document communication expectations to prevent misunderstandings. Include escalation triggers and response SLAs.
   * **Evidence:** `.artifacts/protocol-02/communication-plan.md`
   * **Validation:** Plan contains contacts, response SLA, tooling, and escalation triggers.

5. **`[MUST]` Draft Discovery Recap**
   * **Action:** Write `discovery-recap.md` summarizing outcomes, decisions, open items, and next steps; include approval checkbox and signature line.
   * **Reasoning:** Use recap synthesis pattern — consolidate all call outcomes into client-facing summary. Ensure recap aligns with artifacts and includes approval mechanism.
   * **Evidence:** `.artifacts/protocol-02/discovery-recap.md`
   * **Validation:** Recap references artifacts, lists pending items with owners, and logs send date.

6. **`[GUIDELINE]` Archive Session Evidence**
   * **Action:** Save transcript, recording link, and chat export to `.artifacts/protocol-02/transcripts/` using timestamped filenames.
   * **Reasoning:** Apply evidence preservation pattern — archive all call artifacts for audit trail and future reference. Use consistent naming convention for easy retrieval.
   * **Evidence:** `.artifacts/protocol-02/transcripts/YYYYMMDD-discovery-call.txt`
   * **Validation:** Folder contains transcript stub or pointer for audit.

## QUALITY GATES
<!-- [Category: GUIDELINES-FORMATS] -->

### Gate 1: Pre-Call Readiness
**Type:** Prerequisite  
**Purpose:** Confirm discovery preparation artifacts complete before any client touchpoint.  
**Pass Criteria:**
- **Threshold:** Preparation coverage score ≥95%; unresolved discovery questions ≤5.  
- **Boolean Check:** `ready-for-call-summary.md` status equals `pre_call_ready`.  
- **Metrics:** Checklist completion metrics recorded in `ready-for-call-summary.md`; unknowns resolution metric in `assumptions-gaps.md`.  
- **Evidence Link:** Evidence validated against `.artifacts/protocol-02/ready-for-call-summary.md` and `.artifacts/protocol-02/discovery-brief.md`.  
**Automation:**
- Script: `python3 scripts/validate_gate_02_pre_call.py --output .artifacts/protocol-02/gate0-validation.json`.  
- Script: `python3 scripts/summarize_job_post.py --job-post .artifacts/protocol-01/job-post.md --proposal .artifacts/protocol-01/PROPOSAL.md --output .artifacts/protocol-02/discovery-brief.md`.  
- CI Integration: Gate executed via `real-validation-pipeline.yml` in CI/CD workflow; fails gate blocks merge.  
- Config: `config/protocol_gates/02.yaml` enumerates readiness thresholds and metric ranges.  
**Failure Handling:**
- **Rollback:** Halt outreach, regenerate missing artifacts, rerun readiness validator.  
- **Notification:** Post alert in project channel and flag Protocol 02 owner when readiness score <95%.  
- **Waiver:** Only permitted with documented rationale in `.artifacts/protocol-02/gate-waivers.json` and temporary client approval.

### Gate 2: Post-Call Data Capture
**Type:** Execution  
**Purpose:** Guarantee live-call insights instantly reflected in canonical artifacts.  
**Pass Criteria:**
- **Threshold:** Data capture completeness ≥92%; follow-up backlog cleared within 24 hours.  
- **Boolean Check:** `client-discovery-form.md` front matter `status: confirmed`.  
- **Metrics:** Metrics summarised in `gate1-data-capture.json` (owner coverage metric, follow-up closure metric).  
- **Evidence Link:** Evidence validated against `.artifacts/protocol-02/client-discovery-form.md` and `.artifacts/protocol-02/discovery-call-notes.md`.  
**Automation:**
- Script: `python3 scripts/validate_gate_02_data_capture.py --output .artifacts/protocol-02/gate1-data-capture.json`.  
- Script: `python3 scripts/assumption_extractor.py --inputs .artifacts/protocol-01/PROPOSAL.md .artifacts/protocol-02/client-reply.md --output .artifacts/protocol-02/assumptions-gaps.md`.  
- CI Integration: Validation stage runs on `ubuntu-latest` runner to enforce live-note synchronisation.  
- Config: `config/protocol_gates/02.yaml` defines capture thresholds and follow-up SLA metrics.  
**Failure Handling:**
- **Rollback:** Return to call notes, update fields, re-run validator before distributing recap.  
- **Notification:** Notify discovery lead via Slack/email if follow-up backlog persists >24 hours.  
- **Waiver:** Documented in `gate-waivers.json` with justification and plan; requires account lead signature.

### Gate 3: Recap & Approval
**Type:** Execution  
**Purpose:** Ensure recap sent, tracked, and approved to preserve contractual alignment.  
**Pass Criteria:**
- **Threshold:** Recap approval rate ≥90% within 72 hours; reminder cadence ≤2.  
- **Boolean Check:** `discovery-approval-log.json` entries include `status: approved`.  
- **Metrics:** Metrics captured in `.artifacts/protocol-02/gate2-recap.json` (approval latency metric, reminder count metric).  
- **Evidence Link:** Evidence validated against `.artifacts/protocol-02/discovery-recap.md` and `.artifacts/protocol-02/discovery-approval-log.json`.  
**Automation:**
- Script: `python3 scripts/validate_gate_02_recap.py --output .artifacts/protocol-02/gate2-recap.json`.  
- CI Integration: CI job posts recap approval status to validation summary dashboard.  
- Config: `config/protocol_gates/02.yaml` stores reminder cadence thresholds and approval metrics.  
- Evidence Hook: Recap delivery logged through `python3 scripts/notify_client_summary.py` (manual trigger).  
**Failure Handling:**
- **Rollback:** Revise recap content based on feedback and resend before proceeding.  
- **Notification:** Escalate to account manager if approval pending >72 hours; log escalation in recap file.  
- **Waiver:** Not applicable – approvals mandatory for downstream brief creation.

### Gate 4: Protocol 03 Handoff Readiness
**Type:** Completion  
**Purpose:** Validate downstream prerequisites before activating Project Brief creation.  
**Pass Criteria:**
- **Threshold:** Handoff readiness score ≥0.96 from automation aggregator; zero blocking assumptions.  
- **Boolean Check:** Handoff verification log marks `status: ready`.  
- **Metrics:** Gate metrics summarised in `.artifacts/protocol-02/gate3-handoff.json` (dependency readiness metric, blocker count metric).  
- **Evidence Link:** Evidence validated against `.artifacts/protocol-02/handoff-verification.json` and `.artifacts/protocol-02/assumptions-gaps.md`.  
**Automation:**
- Script: `python3 scripts/validate_gate_02_handoff.py --output .artifacts/protocol-02/gate3-handoff.json`.  
- Script: `python3 scripts/aggregate_evidence_02.py --output .artifacts/protocol-02 --protocol-id 02`.  
- CI Integration: `script-registry-enforcement.yml` ensures registered scripts executed before approvals.  
- Config: `config/protocol_gates/02.yaml` enumerates minimum evidence score and dependency metrics.  
**Failure Handling:**
- **Rollback:** Suspend Protocol 03 kickoff, resolve blockers noted in `handoff-blockers.md`, rerun handoff validator.  
- **Notification:** Alert Protocol 03 owner that handoff paused and share blocker summary.  
- **Waiver:** Only allowed during emergency escalations with CTO sign-off; record waiver path in `gate-waivers.json`.

### Compliance Integration
- **Industry Standards:** CommonMark Markdown, JSON Schema, YAML configuration for discovery bundles.  
- **Security Requirements:** SOC2 logging of discovery artifacts, GDPR-compliant handling of personal data, encrypted storage for transcripts.  
- **Regulatory Compliance:** FTC truth-in-advertising for recap commitments, contractual compliance on approval tracking, retention aligned with ISO 9001 documentation controls.  
- **Governance:** Gate thresholds governed through `config/protocol_gates/02.yaml` and surfaced in protocol governance dashboard; automation telemetry logged in `.artifacts/validation/protocol_quality_gates-summary.json`.

---

## 5. ARTIFACT INVENTORY & PROTOCOL 03 ALIGNMENT
<!-- [Category: GUIDELINES-FORMATS] -->

| Protocol 02 Artifact | Purpose | Protocol 03 Usage |
|----------------------|---------|-------------------|
| `discovery-brief.md` | Pre-call summary of goals, users, metrics, tone | Seeds `context-summary.md` |
| `assumptions-gaps.md` | Pending questions & validation status | Feeds `validation-issues.md` if unresolved |
| `risk-opportunity-list.md` | Early risk register | Supports risk appendix |
| `question-bank.md` | Themed discovery questions | Guides live notes and requirement capture |
| `integration-inventory.md` | System & dependency overview | Inputs to `scope-clarification.md` |
| `scenario-guides.md` | Pivot playbooks | Optional appendix for Protocol 03 |
| `call-agenda.md` / `discovery-call-notes.md` | Live call structure & evidence | Audit trail and evidence bundle |
| `ready-for-call-summary.md` | Readiness confirmation | Reference before call |
| `client-discovery-form.md` | Confirmed functional requirements | Mandatory prerequisite @.cursor/ai-driven-workflow/03-project-brief-creation.md#18 |
| `scope-clarification.md` | Technical stack & constraints | Mandatory prerequisite @.cursor/ai-driven-workflow/03-project-brief-creation.md#19 |
| `timeline-discussion.md` | Milestones & scheduling | Mandatory prerequisite @.cursor/ai-driven-workflow/03-project-brief-creation.md#20 |
| `communication-plan.md` | Collaboration expectations | Mandatory prerequisite @.cursor/ai-driven-workflow/03-project-brief-creation.md#20 |
| `discovery-recap.md` | Client-facing summary & sign-off | Approval evidence @.cursor/ai-driven-workflow/03-project-brief-creation.md#23-27 |
| `discovery-approval-log.json` | Approval tracking | Validates Gate 2 & 3 |
| `transcripts/` folder | Session evidence | Supports audits & learning |

All artifacts include front-matter fields: `status`, `last_updated`, `prepared_by` for traceability.

---

## 6. COMMUNICATION & HALT PROMPTS
<!-- [Category: GUIDELINES-FORMATS] -->

- **Phase Announcements:**
  - `[PHASE 1 START] - Consolidating proposal and job post into pre-call brief.`
  - `[PHASE 2 START] - Preparing question bank, integration inventory, and scenarios.`
  - `[PHASE 3 START] - Finalizing call agenda, live notes template, and readiness summary.`
  - `[PHASE 4 START] - Converting live notes into confirmed artifacts and recap.`

- **Stop Conditions:**
  - `[HALT] Client interaction required – await developer action before sending any external message.`
  - `[REMINDER] Discovery recap approval pending >48h – review follow-up plan.`

- **Completion Self-Check:**
  ```markdown
  ## Protocol 02 Completion Review
  - Discovery artifacts ready for Protocol 03: [Yes/No]
  - Pending items in assumptions tracker: [List or "None"]
  - Discovery recap approval status: [approved | awaiting_client | not_sent]
  - Next action before Protocol 03: [description]
  ```

---

## 7. OPTIONAL AUTOMATION HOOKS
<!-- [Category: EXECUTION-BASIC] -->

1. **Summarize Job Post & Proposal**
   ```bash
   python scripts/summarize_job_post.py \
     --job-post .artifacts/protocol-01/job-post.md \
     --proposal .artifacts/protocol-01/PROPOSAL.md \
     --output .artifacts/protocol-02/discovery-brief.md
   ```

2. **Extract Assumptions & Questions**
   ```bash
   python scripts/assumption_extractor.py \
     --inputs .artifacts/protocol-01/PROPOSAL.md .artifacts/protocol-02/client-reply.md \
     --output .artifacts/protocol-02/assumptions-gaps.md
   ```

3. **Prefill Integration Inventory**
   ```bash
   python scripts/integration_inventory_prefill.py \
     --source .artifacts/protocol-01/PROPOSAL.md \
     --output .artifacts/protocol-02/integration-inventory.md
   ```

Automation is optional; manual updates acceptable if validations pass.

---

## 8. RETROSPECTIVE ANALYSIS & CONTINUOUS IMPROVEMENT
<!-- [Category: META-FORMATS] -->

### Retrospective Analysis
After each discovery call completion, conduct retrospective analysis:

**Performance Metrics:**
- Discovery call duration vs. planned duration
- Percentage of questions answered vs. questions prepared
- Number of assumptions validated vs. assumptions identified
- Gate pass rate (Gate 0-3 completion status)

**Issue Identification:**
- Document any blockers encountered during discovery (e.g., client unavailable, incomplete information, scope changes)
- Identify root causes of issues (e.g., "Insufficient pre-call preparation" → Root cause: "Question bank not prioritized by dependency")
- Record successful mitigation strategies for future reference

**Success Recognition:**
- Highlight effective discovery techniques (e.g., "Scenario guides prevented scope creep during call")
- Document well-prepared artifacts that facilitated smooth handoff to Protocol 03
- Note client feedback on discovery process quality

### Continuous Improvement

**Improvement Opportunities:**
- Review question bank effectiveness — which questions yielded most valuable insights?
- Optimize artifact templates based on Protocol 03 feedback
- Refine scenario guides with actual pivot scenarios encountered
- Enhance integration inventory template with frequently missing fields

**Tracking Mechanisms:**
- Maintain `improvement-metrics-YYYY-QN.json` capturing discovery duration, gate pass rate, and downstream rework
- Track assumption validation rate (how many assumptions confirmed vs. assumed)
- Monitor Protocol 03 handoff bottlenecks (which prerequisites delay handoff most frequently)

**Evidence of Improvement:**
- Log iterative lessons in `.artifacts/protocol-02/lessons-learned.md` and tag updates applied to templates
- Append scenario refinements or recurring blockers to `.artifacts/protocol-02/common-blockers-playbook.md` with resolution notes
- Quarterly, summarize retro outcomes in `.artifacts/protocol-02/discovery-retrospective-YYYY-MM-DD.md` and surface changes to Protocol 01/03 owners

### System Evolution

**Version History:**
- Document protocol version changes in git history with rationale (e.g., "v2.1: Added meta-cognitive checks to Phase 2")
- Track impact of protocol improvements on downstream protocol success rates
- Assess rollback procedures if protocol changes cause regression in Protocol 03 handoff quality

**Rationale for Changes:**
- Link protocol modifications to specific validation failures or user feedback
- Document why changes were necessary (e.g., "Added root cause analysis to risk identification because risks were not being properly mitigated")

**Impact Assessment:**
- Measure effect of protocol improvements on discovery call effectiveness
- Track whether added reasoning patterns reduce assumption validation failures
- Evaluate if reflection enhancements improve Protocol 03 handoff quality

### Knowledge Capture & Organizational Learning

**Lessons Learned:**
- Document discovery best practices in `.artifacts/protocol-02/lessons-learned.md`
- Capture anti-patterns to avoid (e.g., "Don't assume client understands technical terminology without confirming")
- Share successful discovery techniques with Protocol 01 team (proposal quality improvements)

**Knowledge Base:**
- Maintain curated question bank examples in `.artifacts/protocol-02/question-bank-examples.md`
- Build catalog of common integration patterns and their discovery requirements
- Create wiki entry for discovery call facilitation techniques

**Storage & Organization:**
- Archive successful discovery artifacts as templates for future projects
- Store retrospective outcomes in indexed format for easy retrieval
- Maintain knowledge repository links in `.artifacts/protocol-02/knowledge-index.md`

**Knowledge Sharing:**
- Publish quarterly discovery insights to Protocol 01/03 teams
- Share scenario response guides with other discovery practitioners
- Broadcast lessons learned through team communication channels

### Future Planning & Roadmap

**Roadmap:**
- **Next Phase:** After Protocol 02 completion, proceed to Protocol 03 (Project Brief Creation) with validated discovery artifacts
- **Upcoming Improvements:** Plan integration with automated calendar scheduling tools, AI-powered question prioritization, and transcript analysis automation
- **Timeline:** Review discovery protocol effectiveness quarterly and plan major enhancements bi-annually

**Priorities:**
- **High Priority:** Automate discovery recap generation from call notes
- **Medium Priority:** Integrate with calendar APIs for automatic call scheduling
- **Low Priority:** Develop ML model for question relevance scoring

**Resource Planning:**
- Allocate time for quarterly retrospective analysis (2 hours per quarter)
- Budget for protocol enhancement work (4 hours per bi-annual review)
- Plan for knowledge sharing sessions with Protocol 01/03 teams (1 hour per quarter)

**Completion Condition:** All mandatory artifacts present, status-tagged, and approvals recorded in `discovery-approval-log.json`. Gate 3 must pass (or waivers logged) before initiating Protocol 03.

---

## EVIDENCE SUMMARY
<!-- [Category: GUIDELINES-FORMATS] -->

### Artifact Generation Table

| Artifact Name | Metrics | Location | Evidence Link |
|---------------|---------|----------|---------------|
| discovery-brief.md | Metrics include preparation coverage score ≥95% and citation completeness metric | `.artifacts/protocol-02/discovery-brief.md` | Evidence link: Gate 1 readiness validation |
| assumptions-gaps.md | Validation metrics: follow-up closure rate ≥90%, dependency resolution metric ≤2 pending | `.artifacts/protocol-02/assumptions-gaps.md` | Evidence link: Gate 4 handoff verification |
| question-bank.md | Metric coverage: 100% ASK_CLIENT items linked, priority ranking metric recorded | `.artifacts/protocol-02/question-bank.md` | Evidence link: Gate 1 readiness validation |
| client-discovery-form.md | Metrics track confirmation threshold ≥92% across features and owner assignment metric | `.artifacts/protocol-02/client-discovery-form.md` | Evidence link: Gate 2 data capture validation |
| discovery-recap.md | Approval metrics: approval latency ≤72h, reminder metric ≤2 | `.artifacts/protocol-02/discovery-recap.md` | Evidence link: Gate 3 recap approval validation |
| handoff-verification.json | Handoff readiness metric ≥0.96 with blocker metric = 0 | `.artifacts/protocol-02/handoff-verification.json` | Evidence link: Gate 4 handoff readiness validation |
| evidence-manifest.json | Manifest metrics: artifact count match (100%), checksum verification metric = pass | `.artifacts/protocol-02/evidence-manifest.json` | Evidence link: Aggregated evidence validator |

### Storage Structure

**Protocol Directory:** `.artifacts/protocol-02/`  
- **Subdirectories:** `transcripts/`, optional `knowledge-base/`, manifest root otherwise flat.  
- **Permissions:** Read/write for protocol executor, read-only downstream (Protocols 03 & governance).  
- **Naming Convention:** `{artifact-name}.{extension}` (e.g., `assumptions-gaps.md`, `gate2-recap.json`).

### Manifest Completeness

**Manifest File:** `.artifacts/protocol-02/evidence-manifest.json`

**Metadata Requirements:**
- Timestamp: ISO 8601 format (e.g., `2025-11-06T05:34:29Z`).  
- Artifact checksums: SHA-256 hash per artifact listed in manifest integrity block.  
- Size: File size (bytes) recorded for every artifact.  
- Dependencies: Enumerate upstream Protocol 01 artifacts and linked downstream consumers.  

**Dependency Tracking:**
- Input: `PROPOSAL.md`, `proposal-summary.json`, any client transcript or email inputs.  
- Output: All artifacts listed in Artifact Generation Table plus `gate*-*.json` validator outputs.  
- Transformations: Proposal + client reply → discovery brief → live call artefacts → recap → handoff verification.  

**Coverage:** 100% of required artifacts and validator logs referenced in manifest, including SHA verification entries.

### Traceability

**Input Sources:**
- **Input From:** `.artifacts/protocol-01/proposal-summary.json` – Downstream context from Protocol 01.  
- **Input From:** Client discovery call transcripts – Raw conversational evidence captured in `transcripts/`.  

**Output Artifacts:**
- **Output To:** `discovery-brief.md` – Pre-call briefing consumed by discovery operator.  
- **Output To:** `assumptions-gaps.md` – Action log feeding gating decisions.  
- **Output To:** `question-bank.md` – Ranked prompts for live discovery.  
- **Output To:** `client-discovery-form.md` – Canonical requirements sheet for Protocol 03.  
- **Output To:** `discovery-recap.md` – Client-facing summary for approval evidence.  
- **Output To:** `handoff-verification.json` – Final readiness confirmation for Protocol 03.  
- **Output To:** `evidence-manifest.json` – Consolidated inventory for audit.  

**Transformation Steps:**
1. Proposal artifacts → discovery-brief.md: Summarise context and metrics for call setup.  
2. Discovery call → live notes → assumptions-gaps.md: Capture validations and pending actions.  
3. Live notes → client-discovery-form.md: Formalise requirements with owners and priorities.  
4. Validated artifacts → discovery-recap.md: Produce client-ready synopsis with approval block.  
5. Recap + trackers → handoff-verification.json: Compute readiness score and dependency metrics.  

**Audit Trail:**
- Each transformation logged in evidence manifest with timestamp and checksum entry.  
- Validator outputs stored alongside artifacts for independent verification.  
- Dependencies mapped to upstream Protocol 01 artifacts and downstream Protocol 03 consumption.  
- Handoff ledger updates recorded in `.artifacts/project-ledger.json` referencing manifest path.

### Archival Strategy

**Compression:**
- Artifacts compressed into `.artifacts/protocol-02/evidence-bundle.zip` after Protocol 03 acknowledges handoff.  
- Compression format: ZIP with standard compression level for compatibility.  

**Retention Policy:**
- Active artifacts: Retained for 120 days post-protocol completion.  
- Archived bundles: Retained for 3 years post-project closure to meet client audit requirements.  
- Cleanup: Quarterly automation purges artifacts exceeding retention; exceptions documented for regulated engagements.  

**Retrieval Procedures:**
- Active artifacts: Direct access from `.artifacts/protocol-02/` with manifest cross-reference.  
- Archived bundles: Retrieve from `evidence-bundle.zip`, verify via manifest checksums before reuse.  
- Integrity verification: Recompute SHA-256 hash and compare with manifest for every restored artifact.  

**Cleanup Process:**
- Quarterly script updates `.artifacts/protocol-02/cleanup-log.json` with deleted artifact list and checksum snapshot.  
- Critical artifacts flagged as `extended_retention: true` remain until manual review clears them.  
- Retention report forwarded to governance lead for compliance attestation.

---

## 10. VALIDATION & AUTOMATION
<!-- [Category: EXECUTION-BASIC] -->

| Gate | Script | What it checks | Evidence Output |
|------|--------|----------------|-----------------|
| Gate 0 – Pre-Call Readiness | `python scripts/validate_gate_02_pre_call.py` | Presence of pre-call artifacts and tagged unknowns | JSON stdout (optionally saved to `gate0-validation.json`) |
| Gate 1 – Data Capture | `python scripts/validate_gate_02_data_capture.py` | Post-call artifacts updated with owners, priorities, cadence | `gate1-data-capture.json` |
| Gate 2 – Recap Approval | `python scripts/validate_gate_02_recap.py` | Recap send log plus approval status | `gate2-recap.json` |
| Gate 3 – Handoff Ready | `python scripts/validate_gate_02_handoff.py` | Protocol 03 prerequisites satisfied, no open blockers | `gate3-handoff.json` |

**Aggregator:**
```bash
python scripts/aggregate_evidence_02.py \
  --output .artifacts/protocol-02 \
  --protocol-id 02
```
- Generates `.artifacts/protocol-02/evidence-manifest.json` summarizing validator outcomes and artifact presence.
- Upload manifest and logs as part of compliance evidence bundle.

**CI Reference:** Update `.github/workflows/real-validation-pipeline.yml` (or equivalent) to invoke the four validators followed by the aggregator. Ensure failure of any gate blocks merge.

---

## SCRIPTS & AUTOMATION

### Automation Scripts Referenced
| Script Name | Purpose | Location | Status |
|-------------|---------|----------|--------|
| `gate_utils.py` | Gate Utils | `scripts/` | ✅ Exists |
| `validate_gate_02_data_capture.py` | Validate Gate 02 Data Capture | `scripts/` | ✅ Exists |
| `aggregate_evidence_02.py` | Aggregate Evidence 02 | `scripts/` | ✅ Exists |
| `validate_gate_02_handoff.py` | Validate Gate 02 Handoff | `scripts/` | ✅ Exists |
| `run_protocol_gates.py` | Run Protocol Gates | `scripts/` | ✅ Exists |
| `validate_gate_02_recap.py` | Validate Gate 02 Recap | `scripts/` | ✅ Exists |
| `validate_gate_02_pre_call.py` | Validate Gate 02 Pre Call | `scripts/` | ✅ Exists |

### Script Dependencies
- **Input:** Required artifacts from previous protocol
- **Output:** Protocol artifacts and validation reports
- **External Dependencies:** Python 3.8+, standard libraries

### Automation Hooks
- **Pre-execution:** Load context from previous protocol
- **During execution:** Validate protocol execution
- **Post-execution:** Generate evidence bundle

### Script Maintenance
- Scripts reviewed and tested: 2025-11-06
- Last execution: 2025-11-06
- Known issues: None

----------------|---------|----------|--------|
| `validate_gate_02_precall.py` | Validate Gate 02 Precall | `scripts/` | ✅ Exists |
| `validate_gate_02_postcall.py` | Validate Gate 02 Postcall | `scripts/` | ✅ Exists |
| `generate_discovery_summary.py` | Generate Discovery Summary | `scripts/` | ✅ Exists |

### Script Dependencies
- **Input:** proposal-summary.json from Protocol 01, client responses, call recordings
- **Output:** 8+ artifacts (discovery-summary, call-notes, requirements-map, etc.)
- **External Dependencies:** Python 3.8+, audio transcription tools (optional)

### Automation Hooks
- **Pre-execution:** Context consolidation from Protocol 01
- **During execution:** Call recording and note-taking tools
- **Post-execution:** Evidence aggregation, summary generation

### Script Maintenance
- Scripts reviewed and tested: 2025-11-06
- Last execution: 2025-11-06
- Known issues: None

---

## WORKFLOW ORCHESTRATION

### STEP 1

**Action:** Execute context consolidation activities

**Description:** Execution phase

**Input:** Required artifacts from previous phase

**Output:** Validated artifacts for next phase

Communication: Document progress and blockers

Evidence: Track artifacts and validation results in `.artifacts/protocol-02/workflow-logs/`

**Duration:** Varies based on complexity

---

### STEP 2

**Action:** Execute discovery call activities

**Description:** Execution phase

**Input:** Required artifacts from previous phase

**Output:** Validated artifacts for next phase

Communication: Document progress and blockers

Evidence: Track artifacts and validation results in `.artifacts/protocol-02/workflow-logs/`

**Duration:** Varies based on complexity

---

### STEP 3

**Action:** Execute post-call processing activities

**Description:** Execution phase

**Input:** Required artifacts from previous phase

**Output:** Validated artifacts for next phase

Communication: Document progress and blockers

Evidence: Track artifacts and validation results in `.artifacts/protocol-02/workflow-logs/`

**Duration:** Varies based on complexity

---

### Workflow Dependencies

- **Sequential:** STEP 1 → STEP 2 → STEP 3 (must complete in order)
- **Parallel:** None (all steps sequential)
- **Conditional:** Halt if validation fails, escalate to supervisor

### Workflow State Management

- State stored in: `.artifacts/protocol-02/workflow-state.json`
- Checkpoint validation at each step boundary
- Rollback procedure if step fails: Return to previous step and remediate

### Workflow Monitoring

- Real-time status: `.artifacts/protocol-02/workflow-status.json`
- Execution logs: `.artifacts/protocol-02/workflow-logs/`
- Performance metrics: `.artifacts/protocol-02/workflow-metrics.json`


---

## AUTOMATION HOOKS

### Pre-Execution Setup

**Environment Variables:**
- `PROTOCOL_ID=02` - Protocol identifier
- `WORKSPACE_ROOT=.` - Root workspace directory
- `ARTIFACTS_DIR=.artifacts/protocol-02/` - Artifacts storage location
- `LOG_LEVEL=INFO` - Logging verbosity (DEBUG, INFO, WARNING, ERROR)

**Required Permissions:**
- Read access to: `.cursor/ai-driven-workflow/02-*.md`, `.artifacts/`
- Write access to: `.artifacts/protocol-02/`, `scripts/logs/`
- Execute access to: `scripts/validate_*.py`, `scripts/aggregate_*.py`

**System Dependencies:**
- Python 3.8+
- bash/sh shell
- Standard Unix utilities (grep, sed, awk)

### Automation Commands

#### Command 1: Pre-Execution Validation
```bash
python3 scripts/validate_prerequisites_02.py \
  --protocol 02 \
  --workspace . \
  --strict
```
**Flags:**
- `--protocol 02` - Protocol ID to validate
- `--workspace .` - Workspace root directory
- `--strict` - Enforce strict validation

**Output:** `.artifacts/protocol-02/prerequisites-validation.json`
**Exit Codes:** 0=success, 1=validation failed, 2=prerequisites missing

#### Command 2: Protocol Execution
```bash
python3 scripts/run_protocol_gates.py \
  --protocol 02 \
  --input .artifacts/protocol-02/input/ \
  --output .artifacts/protocol-02/output/ \
  --log-file .artifacts/protocol-02/execution.log \
  --error-handling retry
```
**Flags:**
- `--protocol 02` - Protocol ID
- `--input DIR` - Input artifacts directory
- `--output DIR` - Output artifacts directory
- `--log-file FILE` - Execution log file path
- `--error-handling {retry|escalate|halt}` - Error handling strategy

**Output:** `.artifacts/protocol-02/output/`
**Exit Codes:** 0=success, 1=execution error, 2=validation gate failed

#### Command 3: Evidence Aggregation
```bash
python3 scripts/aggregate_evidence_02.py \
  --protocol 02 \
  --artifacts-dir .artifacts/protocol-02/ \
  --output-manifest \
  --checksum sha256
```
**Flags:**
- `--protocol 02` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--output-manifest` - Generate manifest file
- `--checksum {md5|sha256}` - Checksum algorithm

**Output:** `.artifacts/protocol-02/EVIDENCE-MANIFEST.json`
**Exit Codes:** 0=success, 1=aggregation failed

#### Command 4: Post-Execution Validation
```bash
python3 scripts/validate_protocol_02.py \
  --protocol 02 \
  --artifacts-dir .artifacts/protocol-02/ \
  --quality-gates strict \
  --report json
```
**Flags:**
- `--protocol 02` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--quality-gates {strict|standard|relaxed}` - Gate strictness
- `--report {json|html|text}` - Report format

**Output:** `.artifacts/protocol-02/validation-report.json`
**Exit Codes:** 0=all gates pass, 1=gate failure, 2=critical error

### Error Handling & Fallback Procedures

**If Command 1 (Prerequisites) Fails:**
1. Check log: `.artifacts/protocol-02/prerequisites-validation.json`
2. Verify all input artifacts exist
3. Ensure all environment variables are set
4. **Fallback:** Run with `--strict=false`
5. **Escalate:** Notify Protocol Owner if still failing

**If Command 2 (Execution) Fails:**
1. Check log: `.artifacts/protocol-02/execution.log`
2. Review error code and message
3. **Retry:** Re-run with `--error-handling retry` (up to 3 times)
4. **Fallback:** Run with `--error-handling escalate`
5. **Escalate:** Notify supervisor with logs

**If Command 3 (Aggregation) Fails:**
1. Verify all artifacts present in output directory
2. Check artifact file formats and integrity
3. **Fallback:** Run without `--output-manifest`
4. **Escalate:** If artifacts corrupted, restart from Command 2

**If Command 4 (Validation) Fails:**
1. Review validation report
2. Identify which quality gates failed
3. **Fallback:** Run with `--quality-gates relaxed`
4. **Escalate:** Return to Command 2 and remediate

### Scheduling & Execution Context

**Execution Timing:**
- Pre-execution: 5 minutes (setup + prerequisites validation)
- Main execution: 15-45 minutes (depends on protocol complexity)
- Post-execution: 10 minutes (aggregation + validation)
- Total: 30-60 minutes per protocol

**Parallel Execution:** Can run up to 4 protocols in parallel (if resources allow)

**CI/CD Integration:**
- Trigger on: Protocol file changes, manual trigger
- Timeout: 90 minutes per protocol
- Retry policy: 2 retries on transient failures
- Notification: Slack/Email on success/failure

### Monitoring & Logging

**Log Files:**
- `.artifacts/protocol-02/execution.log` - Main execution log
- `.artifacts/protocol-02/validation.log` - Validation log
- `.artifacts/protocol-02/error.log` - Error log (if any)

**Status Files:**
- `.artifacts/protocol-02/workflow-status.json` - Real-time status
- `.artifacts/protocol-02/workflow-metrics.json` - Performance metrics

**Checkpoints:**
- After prerequisites validation
- After each command execution
- Before handoff to next protocol

### Success Criteria

✅ All commands execute successfully (exit code 0)
✅ All quality gates pass (validation report shows PASS)
✅ Evidence manifest generated and checksums verified
✅ All artifacts stored in `.artifacts/protocol-02/`
✅ No errors in execution, validation, or aggregation logs
✅ Protocol ready for handoff to next protocol

---
## HANDOFF CHECKLIST

### Pre-Handoff Validation
- [ ] All artifacts generated and stored in `.artifacts/protocol-02/`
- [ ] Evidence manifest complete with checksums
- [ ] Quality gates passed (all 4 gates show PASS status)
- [ ] Downstream protocol owner notified and ready
- [ ] No blocking issues or waivers pending

### Handoff Package Contents
- **Evidence Bundle:** `PROTOCOL-02-EVIDENCE.zip` containing:
  - All gate validation reports
  - Discovery artifacts (prep, summary, requirements)
  - Call notes and recordings
  - Traceability matrix
- **Readiness Attestation:** Signed-off by protocol owner
- **Next Protocol Brief:** Clear handoff to Protocol 03

### Handoff Verification
- [ ] Checksum verification passed
- [ ] Downstream protocol has received package
- [ ] Downstream protocol confirms receipt and readiness
- [ ] No outstanding questions or clarifications needed

### Sign-Off
- Protocol Owner: _________________ Date: _________
- Downstream Owner: _________________ Date: _________

---

## COMMUNICATION & STAKEHOLDER ALIGNMENT

### Status Announcements (Template)
```
[PROTOCOL 02 | PHASE X START] - [Action description]
[PROTOCOL 02 | PHASE X COMPLETE] - [Outcome with evidence reference]
[PROTOCOL 02 ERROR] - [Error type and resolution]
```

### Stakeholder Notifications
- **Primary Stakeholder:** Discovery Call Lead - Notification method: Email/Slack
- **Secondary Stakeholders:** Client, Project Manager - Notification method: Email
- **Escalation Path:** Project Manager → Executive for scope issues

### Feedback Collection
- Collect feedback from Protocol 03 owner on discovery completeness
- Document any gaps or clarification needs
- Log feedback in `.artifacts/protocol-02/feedback-log.json`

### Communication Cadence
- Pre-call notification to client
- Post-call summary within 24 hours
- Weekly status updates if follow-ups needed

---

## 10. HANDOFF CHECKLIST (LEGACY)
<!-- [Category: EXECUTION-BASIC] -->

### Pre-Handoff Review
- [ ] Gate 0-3 results recorded (JSON/log) with status `pass` or documented waiver.
- [ ] `assumptions-gaps.md` has no remaining `ASK CLIENT` or `follow-up` items without owner/due date.
- [ ] `ready-for-call-summary.md` states `status: pre_call_ready` and links loaded artifacts.
- [ ] Evidence manifest generated and archived.
- [ ] Retrospective analysis completed with lessons learned documented.
- [ ] Knowledge capture artifacts updated with new insights.
- [ ] Future planning roadmap reviewed and updated.

### Execute Handoff
1. Compress `.artifacts/protocol-02/` into dated archive; record checksum in `project-ledger.json`.
2. Post summary in delivery channel with links to recap, integration inventory, and outstanding risks.
3. Trigger Protocol 03: `@apply .cursor/ai-driven-workflow/03-project-brief-creation.md`.
4. Log completion in protocol execution register with timestamp and validator references.
5. Share lessons learned and improvement opportunities with Protocol 01/03 teams.
6. Update knowledge base with discovery insights and best practices.

---

## 11. EVIDENCE & TRACEABILITY
<!-- [Category: GUIDELINES-FORMATS] -->

| Artifact | Required | Notes |
|----------|----------|-------|
| `discovery-brief.md` | ✅ | Cite proposal/job-post line references per section |
| `assumptions-gaps.md` | ✅ | Each open item tagged `ASK CLIENT` or `follow-up` with owner |
| `question-bank.md` | ✅ | Link question IDs back to assumptions tracker |
| `integration-inventory.md` | ✅ | Columns: System, Purpose, Owner, Data, Risk, Next Action |
| `ready-for-call-summary.md` | ✅ | Status `pre_call_ready` plus artifact checklist |
| `client-discovery-form.md` | ✅ | Feature, priority, owner, acceptance criteria |
| `scope-clarification.md` | ✅ | Final stack decisions, access requirements |
| `timeline-discussion.md` | ✅ | Milestones, checkpoints, contingency notes |
| `communication-plan.md` | ✅ | Cadence, tooling, escalation steps |
| `discovery-recap.md` | ✅ | Approval timestamp and summary of decisions |
| `discovery-approval-log.json` | ✅ | Structured record of approval metadata |
| `transcripts/` | ☑️ Recom. | Store transcript or pointer for audit |

**Traceability Actions:**
- Run `python scripts/validate_protocol_handoffs.py --from-protocol 02 --to-protocol 03 --output .artifacts/protocol-02/handoff-verification.json`.
- Append evidence manifest path and archive location to `.artifacts/project-ledger.json`.
- Maintain SHA-256 hashes for all markdown artifacts in `evidence-manifest.json` integrity section.

---
