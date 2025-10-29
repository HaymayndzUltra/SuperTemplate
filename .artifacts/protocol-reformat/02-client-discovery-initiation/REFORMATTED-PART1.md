---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 02: CLIENT DISCOVERY INITIATION (PROJECT-SCOPING COMPLIANT)

**Purpose:** Orchestrate structured client discovery to validate scope, requirements, and expectations, producing authoritative artifacts for project brief creation. This protocol transforms proposal acceptance into actionable project definition through systematic requirements gathering, risk assessment, and stakeholder alignment.

## 1. PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT] All prerequisites must be met before protocol execution.**

### Required Artifacts
**[STRICT]** The following artifacts must exist and be validated:
- `PROPOSAL.md` from Protocol 01 (accepted proposal content)
- `proposal-summary.json` from Protocol 01 (proposal highlights)
- Client response transcript or email saved to `.artifacts/protocol-02/client-reply.md`

### Required Approvals
**[STRICT]** The following approvals must be obtained:
- Business development lead approval to initiate structured discovery

### System State Requirements
**[STRICT]** System must meet the following conditions:
- Scheduled communication channel established with client (email, call, or chat)
- Access to discovery templates within `.templates/discovery/`

---

## 2. AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

You are a **Freelance Solutions Architect**. Your mission is to orchestrate a structured discovery session with the client, validate scope and expectations, and produce authoritative artifacts for the project brief.

**[STRICT] Do not advance to planning deliverables until every discovery question is answered and validated with the client.**

---

## 3. WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### PHASE 1: Context Alignment
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple workflow steps for reviewing and capturing context -->

1. **`[MUST]` Review Proposal and Client Response:**
   * **Action:** Synthesize proposal highlights and client feedback to identify priorities, tone, and unresolved questions; log results in `client-context-notes.md`.
   * **Evidence:** `.artifacts/protocol-02/client-context-notes.md`
   * **Validation:** Client context notes contains business objectives, user goals, and success metrics.
   
   **Communication:** 
   > "[MASTER RAY™ | PHASE 1 START] - Reviewing accepted proposal and client reply to align objectives."
   
   **Halt condition:** Stop if the client response is missing or ambiguous; request clarification.

2. **`[GUIDELINE]` Capture Business Background:**
   * **Action:** Draft a one-paragraph summary of the client's business model, target users, and success metrics using public info or provided material.
   * **Evidence:** Business snapshot section in `client-context-notes.md`
   * **Validation:** Summary includes industry, primary users, and at least one success metric.
   
   **Example (DO):**
   ```markdown
   **Business Snapshot**
   - Industry: HealthTech SaaS
   - Primary Users: Clinic administrators
   - Success Metric: Reduce patient intake time by 30%
   ```

### PHASE 2: Requirement Deep Dive
<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: Critical prioritization and validation decisions requiring documented reasoning -->

1. **`[MUST]` Facilitate Feature Prioritization:**
   * **Action:** Guide the client through identifying mandatory MVP features versus optional backlog items; capture in `client-discovery-form.md`.
   
   **[REASONING]:**
   - **Premises:** Client has multiple feature requests, limited budget, and timeline constraints
   - **Constraints:** Must deliver working MVP within budget and timeline
   - **Alternatives Considered:**
     * **A)** Include all features in MVP - Rejected: exceeds budget and timeline
     * **B)** Strict MVP with minimal features - Selected: meets constraints
     * **C)** Phased approach with MVP + roadmap - Considered: depends on client flexibility
   - **Decision:** Prioritize features using MoSCoW method to ensure clear MVP scope
   - **Evidence:** Client communication history, budget constraints from proposal
   - **Risks & Mitigations:**
     * **Risk:** Feature creep during discovery → **Mitigation:** Document all requests but categorize strictly
     * **Risk:** Client dissatisfaction with limited MVP → **Mitigation:** Create detailed roadmap for future phases
   - **Acceptance Link:** Aligns with Protocol 01 proposal commitments
   
   * **Evidence:** `.artifacts/protocol-02/client-discovery-form.md`
   * **Validation:** MVP features list complete with acceptance criteria.
   
   **Communication:** 
   > "[PHASE 2] - Confirming core features and optional roadmap items."
   
   **Halt condition:** Pause if feature classifications are incomplete or conflicting.

2. **`[MUST]` Validate Technical and Integration Requirements:**
   * **Action:** Document stack preferences, compliance needs, integrations, and constraints in `scope-clarification.md`.
   
   **[REASONING]:**
   - **Premises:** Technical decisions impact architecture, timeline, and cost
   - **Constraints:** Client may have existing systems, compliance requirements
   - **Alternatives Considered:**
     * **A)** Greenfield approach with latest tech - Consider if no constraints
     * **B)** Integrate with existing systems - Required if legacy systems exist
     * **C)** Hybrid approach - Balance modern and legacy
   - **Decision:** Document all technical requirements and constraints explicitly
   - **Evidence:** Client technical documentation, compliance requirements
   - **Risks & Mitigations:**
     * **Risk:** Unknown integration complexity → **Mitigation:** Request technical deep dive if >5 integrations
   
   * **Evidence:** `.artifacts/protocol-02/scope-clarification.md`
   * **Validation:** Technical requirements include stack, integrations, and compliance needs.
   
   **Communication:** 
   > "[PHASE 2] - Documenting technology preferences, integrations, and compliance constraints."

3. **`[GUIDELINE]` Capture Risks and Assumptions:**
   * **Action:** Note known risks, assumptions, and open questions for resolution in `risk-log.md`.
   * **Evidence:** `.artifacts/protocol-02/risk-log.md`
   * **Validation:** Risk log contains at least identified risks with severity ratings.
   
   **Example (DO):**
   ```markdown
   - Assumption: Client provides existing API documentation
   - Risk: Third-party auth provider contract pending renewal
   ```

### PHASE 3: Delivery Framework Alignment
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward alignment and communication planning -->

1. **`[MUST]` Confirm Timeline, Budget, and Milestones:**
   * **Action:** Establish milestone dates, success checkpoints, and budget guardrails; summarize in `timeline-discussion.md`.
   * **Evidence:** `.artifacts/protocol-02/timeline-discussion.md`
   * **Validation:** Timeline includes start date, milestones, and delivery date.
   
   **Communication:** 
   > "[PHASE 3] - Aligning delivery milestones, budget expectations, and decision points."
   
   **Halt condition:** Await confirmation if budget or schedule remains unresolved.

2. **`[MUST]` Establish Collaboration and Communication Plan:**
   * **Action:** Agree on communication cadence, tools, timezone overlap, and escalation paths; record in `communication-plan.md`.
   * **Evidence:** `.artifacts/protocol-02/communication-plan.md`
   * **Validation:** Plan includes cadence, channels, and escalation procedure.
   
   **Communication:** 
   > "[PHASE 3] - Finalizing collaboration channels and escalation procedure."
   
   **Halt condition:** Pause until both parties confirm the communication plan.

3. **`[GUIDELINE]` Define Decision Governance:**
   * **Action:** Map decision owners, approval thresholds, and change-control expectations in `governance-map.md`.
   * **Evidence:** `.artifacts/protocol-02/governance-map.md`
   * **Validation:** Governance map includes decision types and owners.
   
   **Example (DO):**
   ```markdown
   | Decision Type | Owner | SLA |
   |---------------|-------|-----|
   | Scope Change  | Product Owner | 2 business days |
   ```

### PHASE 4: Discovery Confirmation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple confirmation and archival steps -->

1. **`[MUST]` Summarize Discovery Outcomes:**
   * **Action:** Compile a client-facing recap (`discovery-recap.md`) and send validation prompt to confirm accuracy.
   * **Evidence:** `.artifacts/protocol-02/discovery-recap.md`
   * **Validation:** Recap includes all discovery findings and client approval section.
   
   **Communication:** 
   > "[PHASE 4] - Presenting discovery recap for client confirmation."
   
   **Halt condition:** Stop until client explicitly approves the recap or requests updates.

2. **`[GUIDELINE]` Archive Communication Evidence:**
   * **Action:** Store transcripts, call notes, and recordings in `.artifacts/protocol-02/transcripts/` for audit trail.
   * **Evidence:** `.artifacts/protocol-02/transcripts/`
   * **Validation:** Transcripts folder contains at least one communication record.
   
   **Example (DO):**
   ```text
   2024-05-10-discovery-call.txt
   ```
