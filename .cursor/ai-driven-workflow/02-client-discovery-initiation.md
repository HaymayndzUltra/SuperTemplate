---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 02: CLIENT DISCOVERY INITIATION (PROJECT-SCOPING COMPLIANT)

**Purpose:** Equip the solo developer with a complete pre-call discovery toolkit derived from the job post, accepted proposal, and any client replies. All outputs remain internal until the live discovery call concludes, after which they feed Protocol 03 once confirmed.

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

1. **`[MUST]` Build Discovery Brief**
   * **Action:** Summarize job post and proposal commitments into `discovery-brief.md`, covering Business Goals, Target Users, Success Metrics, Constraints, and Client Tone.
   * **Evidence:** `.artifacts/protocol-02/discovery-brief.md`
   * **Validation:** Each section cites source line references.

2. **`[MUST]` Compile Assumptions & Gap Tracker**
   * **Action:** Identify assumptions and missing data; record in `assumptions-gaps.md` with status (`confirmed`, `ASK CLIENT`, `research`).
   * **Evidence:** `.artifacts/protocol-02/assumptions-gaps.md`
   * **Validation:** Every proposal assumption mapped to a follow-up action.

3. **`[GUIDELINE]` Draft Risk & Opportunity Radar**
   * **Action:** Generate `risk-opportunity-list.md` with initial risks, blockers, and upside notes.
   * **Evidence:** `.artifacts/protocol-02/risk-opportunity-list.md`
   * **Validation:** At least three risks documented with impact and mitigation idea.

### PHASE 2: Question & Scenario Preparation
<!-- [Category: EXECUTION-BASIC] -->

1. **`[MUST]` Generate Themed Question Bank**
   * **Action:** Populate `question-bank.md` with prioritized questions grouped by Business Outcomes, User Journeys, Functional Scope, Technical Stack, Integrations, Compliance, and Delivery Logistics.
   * **Evidence:** `.artifacts/protocol-02/question-bank.md`
   * **Validation:** Every `ASK CLIENT` item in `assumptions-gaps.md` links to at least one question ID.

2. **`[MUST]` Prefill Integration & Dependency Inventory**
   * **Action:** Create `integration-inventory.md` listing known systems, data owners, access requirements, and risk flags. Mark unknown fields with `@ASK_CLIENT` and tie them to the question bank.
   * **Evidence:** `.artifacts/protocol-02/integration-inventory.md`
   * **Validation:** Table covers System, Purpose, Owner, Data Availability, Risk, Next Action.

3. **`[GUIDELINE]` Prepare Scenario Response Guides**
   * **Action:** Document `scenario-guides.md` covering likely pivots (budget adjustment, scope expansion, compliance gaps) with trigger phrases, recommended responses, and fallback plans.
   * **Evidence:** `.artifacts/protocol-02/scenario-guides.md`
   * **Validation:** Minimum of three scenarios mapped to proposal commitments.

### PHASE 3: Call Logistics & Live Support Setup
<!-- [Category: EXECUTION-BASIC] -->

1. **`[MUST]` Assemble Call Agenda & Checklist**
   * **Action:** Create `call-agenda.md` including introductions, discovery themes, wrap-up, plus reminders (recording consent, recap send deadline, follow-up owner).
   * **Evidence:** `.artifacts/protocol-02/call-agenda.md`
   * **Validation:** Agenda duration matches scheduled meeting; checklist covers Cursor context load, question bank review, and equipment check.

2. **`[MUST]` Prepare Live Notes Template**
   * **Action:** Build `discovery-call-notes.md` aligned to the question bank, with columns `Client Notes`, `Action`, `Owner`, `Due Date`, `Status` (`confirmed`, `follow-up`, `risk`).
   * **Evidence:** `.artifacts/protocol-02/discovery-call-notes.md`
   * **Validation:** Template ready for real-time copy/paste and tagging.

3. **`[MUST]` Produce Ready-for-Call Summary**
   * **Action:** Summarize artifact readiness in `ready-for-call-summary.md`, list top unanswered questions, risk watchlist, and confirm whether artifacts were loaded into `.cursor/rules/`.
   * **Evidence:** `.artifacts/protocol-02/ready-for-call-summary.md`
   * **Validation:** Status field set to `pre_call_ready`; outstanding items reference question IDs.

### PHASE 4: Post-Call Consolidation
<!-- [Category: EXECUTION-BASIC] -->

1. **`[MUST]` Update Client Discovery Form**
   * **Action:** Transfer confirmed answers into `client-discovery-form.md`, including MVP scope, acceptance criteria, priorities, and notes on open items.
   * **Evidence:** `.artifacts/protocol-02/client-discovery-form.md`
   * **Validation:** No feature remains without owner, priority, and acceptance detail; unresolved items flagged `follow-up` with next action.

2. **`[MUST]` Refresh Technical Scope & Integrations**
   * **Action:** Update `scope-clarification.md` and `integration-inventory.md` with final stack decisions, integration owners, access status, and constraints.
   * **Evidence:** `.artifacts/protocol-02/scope-clarification.md`, `.artifacts/protocol-02/integration-inventory.md`
   * **Validation:** All `@ASK_CLIENT` tags resolved or reassigned with follow-up owner and due date.

3. **`[MUST]` Finalize Timeline & Milestones**
   * **Action:** Record agreed milestones, dependencies, and budget guardrails in `timeline-discussion.md`; mark conflicts and mitigation steps.
   * **Evidence:** `.artifacts/protocol-02/timeline-discussion.md`
   * **Validation:** Document lists start date, key checkpoints, decision gates, and risk indicators.

4. **`[MUST]` Confirm Collaboration Plan**
   * **Action:** Capture cadence, tools, timezone overlap, and escalation steps in `communication-plan.md`, noting solo reminders where applicable.
   * **Evidence:** `.artifacts/protocol-02/communication-plan.md`
   * **Validation:** Plan contains contacts, response SLA, tooling, and escalation triggers.

5. **`[MUST]` Draft Discovery Recap**
   * **Action:** Write `discovery-recap.md` summarizing outcomes, decisions, open items, and next steps; include approval checkbox and signature line.
   * **Evidence:** `.artifacts/protocol-02/discovery-recap.md`
   * **Validation:** Recap references artifacts, lists pending items with owners, and logs send date.

6. **`[GUIDELINE]` Archive Session Evidence**
   * **Action:** Save transcript, recording link, and chat export to `.artifacts/protocol-02/transcripts/` using timestamped filenames.
   * **Evidence:** `.artifacts/protocol-02/transcripts/YYYYMMDD-discovery-call.txt`
   * **Validation:** Folder contains transcript stub or pointer for audit.

## 4. QUALITY GATES & STATUS MARKERS
<!-- [Category: GUIDELINES-FORMATS] -->

### Gate 0: Pre-Call Readiness
- **Criteria:** `discovery-brief.md`, `assumptions-gaps.md`, `question-bank.md`, `integration-inventory.md`, `call-agenda.md`, and `ready-for-call-summary.md` complete; all unknowns tagged `ASK CLIENT` with question reference.
- **Pass Action:** Mark `ready-for-call-summary.md` status to `pre_call_ready`; load artifacts into `.cursor/rules/` (manual developer action).
- **Failure Handling:** Re-run summarization scripts or manually complete missing sections.

### Gate 1: Post-Call Data Capture
- **Criteria:** `client-discovery-form.md`, `scope-clarification.md`, `integration-inventory.md`, `timeline-discussion.md`, `communication-plan.md` updated with confirmed answers; outstanding items labeled `follow-up` with owner.
- **Pass Action:** Set artifact front-matter `status: confirmed`; timestamp updates.
- **Failure Handling:** If key details missing, schedule follow-up conversation and log items in `discovery-call-notes.md`.

### Gate 2: Recap & Approval
- **Criteria:** `discovery-recap.md` drafted, sent to client, approval status logged in `discovery-approval-log.json`.
- **Pass Action:** Update recap status `approved`; attach signed confirmation or email record.
- **Failure Handling:** If approval pending >72 hours, send reminder; escalate if client feedback requests revisions.

### Gate 3: Protocol 03 Handoff Readiness
- **Criteria:** All Protocol 03 prerequisites (@.cursor/ai-driven-workflow/03-project-brief-creation.md#17-20) linked and validated; assumptions tracker reflects resolution status; recap approval logged.
- **Pass Action:** Execute Protocol 03 handoff checklist; notify next protocol owner (solo developer = self reminder).
- **Failure Handling:** Document blockers in `handoff-blockers.md`; do not initiate Protocol 03 until resolved.

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

## 8. CONTINUOUS IMPROVEMENT & METRICS
<!-- [Category: META-FORMATS] -->

- Log iterative lessons in `.artifacts/protocol-02/lessons-learned.md` and tag updates applied to templates.
- Maintain `improvement-metrics-YYYY-QN.json` capturing discovery duration, gate pass rate, and downstream rework.
- Append scenario refinements or recurring blockers to `.artifacts/protocol-02/common-blockers-playbook.md` with resolution notes.
- Quarterly, summarize retro outcomes in `.artifacts/protocol-02/discovery-retrospective-YYYY-MM-DD.md` and surface changes to Protocol 01/03 owners.

**Completion Condition:** All mandatory artifacts present, status-tagged, and approvals recorded in `discovery-approval-log.json`. Gate 3 must pass (or waivers logged) before initiating Protocol 03.

---

## 9. VALIDATION & AUTOMATION
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

## 10. HANDOFF CHECKLIST
<!-- [Category: EXECUTION-BASIC] -->

### Pre-Handoff Review
- [ ] Gate 0-3 results recorded (JSON/log) with status `pass` or documented waiver.
- [ ] `assumptions-gaps.md` has no remaining `ASK CLIENT` or `follow-up` items without owner/due date.
- [ ] `ready-for-call-summary.md` states `status: pre_call_ready` and links loaded artifacts.
- [ ] Evidence manifest generated and archived.

### Execute Handoff
1. Compress `.artifacts/protocol-02/` into dated archive; record checksum in `project-ledger.json`.
2. Post summary in delivery channel with links to recap, integration inventory, and outstanding risks.
3. Trigger Protocol 03: `@apply .cursor/ai-driven-workflow/03-project-brief-creation.md`.
4. Log completion in protocol execution register with timestamp and validator references.

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
