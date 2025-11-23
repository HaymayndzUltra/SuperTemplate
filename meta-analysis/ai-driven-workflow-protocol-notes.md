# AI-Driven Workflow – Protocol Notes

## Protocol 01 – Client Proposal Generation

### High-level purpose
- Converts a raw `JOB-POST.md` from a client platform into a **human-sounding proposal** plus a complete evidence bundle.
- Ensures the proposal passes **5 quality gates** (job post comprehension, tone alignment, human voice, pricing realism, evidence integrity) before handoff to Protocol 02.

### What problem it solves (my understanding)
- Freelance proposals often sound generic, AI-written, or misaligned with the client’s real language, tone, and budget.
- This protocol forces a **disciplined, evidence-driven process** so the proposal:
  - Mirrors the client’s own words and pain points.
  - Uses tone that matches the client’s style (formal / casual / technical).
  - Has pricing justified by market benchmarks and clear risk notes.
  - Comes with full artifacts so later protocols (discovery, project brief) can reuse the analysis.

### Identity & ownership
- **Protocol ID:** 01 – *Client Proposal Generation*.
- **Owner & Executor:** Proposal Writer/Freelancer (same person for this protocol).
- **Downstream Owner:** Discovery Call Lead (Protocol 02).
- Scope is **execution-level**: it’s the first concrete action in the workflow, no upstream protocol inputs required.

### AI role & mission (my interpretation)
- AI acts as a **Human Voice Simulation Architect**:
  - Decode the client’s language and style from the job post.
  - Design a tone and humanization strategy (contractions, uncertainty, forbidden phrases avoidance).
  - Generate and validate artifacts: `jobpost-analysis.json`, `tone-map.json`, `pricing-analysis.json`, `humanization-log.json`, `PROPOSAL.md`, `proposal-summary.json`.
- Success is measured by **human believability**, **evidence completeness**, and **smooth handoff** to Protocol 02.

### Workflow – how it actually runs

**PHASE 0 – Environment & Intake**
- Check prerequisites (JOB-POST.md exists, Python runtime, artifacts dir, script registry valid).
- Create a timestamped `notes.md` in `.artifacts/protocol-01/`.
- Optionally clear old artifacts and copy the authoritative `JOB-POST.md` into the protocol folder, verifying integrity via checksums.

**PHASE 1 – Manual Job Post Extraction**
- Work from the job post **verbatim**, not guesses.
- Extract exact quotes and facts into `notes.md` and a structured `jobpost-analysis.json`:
  - fields: `exact_quotes`, `tech_stack`, `pain_points`, `tone_type`, `urgency_signals`, `vague_requirements`.
- Flag red signals (vague scope, unrealistic budget) and record follow-up questions in `notes.md`.

**PHASE 2 – Tone & Human Voice Strategy**
- Run `tone_mapper.py` on `jobpost-analysis.json` to produce `tone-map.json` with a tone decision and confidence.
- Design a humanization plan and store it in `humanization-log.json`:
  - target tone, minimum contractions, uncertainty line, forbidden phrases list.
- Choose at least 2 differentiators and log them in `notes.md`.

**PHASE 3 – Pricing & Scope Calibration**
- Estimate workload (simple / moderate / complex) and tie it to rate tiers.
- Create `pricing-analysis.json` containing:
  - workload assumptions, hourly rates, total cost, milestone structure.
  - risks (scope creep, under/over quoting) and mitigations.
- Validate that pricing is within **80–120%** of market benchmarks and milestones are balanced.

**PHASE 4 – Draft Human-Simulated Proposal**
- Draft `PROPOSAL.md` using an **anti-template** structure:
  - Opening with a client quote and deliverables/timeline.
  - Interpretation bullets with conditional language (`If`, `Assuming`) and clarifying questions.
  - Approach mini-scenario with concrete timeframes.
  - Optional predictive system evidence paragraph when prior proof is missing.
  - CTA with clear next step and availability.
- Enforce human voice rules:
  - ≥3 contractions, ≥1 uncertainty statement, ≥1 direct question, 0 forbidden phrases.
- Update `humanization-log.json` with final counts and checks.

**PHASE 5 – Validation & Packaging**
- Run a **validation chain**:
  - Prerequisites → structure → voice → pricing → evidence → SHA integrity.
- Execute automation scripts to check structure, voice metrics, pricing realism, and artifact completeness.
- Generate `proposal-summary.json` summarizing differentiators, pricing, and next steps.
- Final check that all required artifacts exist and match their checksums.

### Quality gates (how the protocol decides pass/fail)
- **Gate 1 – Job Post Comprehension:**
  - `jobpost-analysis.json` must have ≥90% coverage and ≥2 verbatim quotes.
  - If coverage is low, go back to Phase 1, re-extract, and re-run analysis.

- **Gate 2 – Tone Alignment:**
  - `tone-map.json` must show tone confidence ≥80% and a defined differentiator list.
  - If confidence is low, revisit tone analysis and possibly override manually with documentation.

- **Gate 3 – Human Voice Compliance:**
  - `humanization-log.json` / `PROPOSAL.md` must show ≥3 contractions, ≥1 uncertainty marker, 0 forbidden phrases.
  - No waivers allowed; failure forces a return to drafting.

- **Gate 4 – Pricing Realism:**
  - Pricing must sit within 80–120% of market benchmarks and milestones must be balanced.
  - If not, adjust pricing or justify premium pricing and record it in `pricing-analysis.json`.

- **Gate 5 – Evidence Integrity:**
  - All expected artifacts must be present and listed in an evidence manifest with valid SHA checksums.
  - No waivers; missing/invalid artifacts block handoff.

### Automation & scripts (how it connects to scripts)
- Uses a set of Python scripts under `scripts/` to:
  - Analyze job posts (`analyze_jobpost.py`).
  - Map tone (`tone_mapper.py`).
  - Validate proposal structure and human voice (`validate_proposal_structure.py`, `validate_proposal.py`).
  - Validate pricing (`validate_pricing.py`).
  - Aggregate and validate evidence (`aggregate_evidence_01.py`, `validate_evidence_manifest.py`).
  - Run gates and pre/post validations (`run_protocol_gates.py`, `validate_prerequisites_01.py`, `validate_protocol_01.py`).
- Commands for pre-execution, execution, aggregation, and post-validation are defined with clear flags and exit codes.

### Integration points (how it fits in the bigger workflow)
- **Inputs (external):**
  - `JOB-POST.md` from the client platform.
  - Portfolio references and rate benchmarks.
  - Gate config: `config/protocol_gates/01.yaml`, `gates_config.yaml`.

- **Outputs (downstream):**
  - Core artifacts in `.artifacts/protocol-01/`:
    - `jobpost-analysis.json`
    - `tone-map.json`
    - `pricing-analysis.json`
    - `humanization-log.json`
    - `PROPOSAL.md`
    - `proposal-summary.json`
    - `evidence-manifest.json` / evidence bundle zip
  - Protocol 02 uses the validated proposal and summary as starting point for discovery.
  - Protocol 03 can reuse `proposal-summary.json` and analysis artifacts when defining the project brief.

### Handoff & readiness (when Protocol 01 is “done” in my understanding)
- Protocol 01 is **complete and ready for Protocol 02** when:
  - All 5 gates pass with recorded metrics.
  - All required artifacts exist in `.artifacts/protocol-01/` and are checksum-verified.
  - `PROPOSAL.md` matches human voice rules without forbidden phrases.
  - `proposal-summary.json` is generated and accurately reflects differentiators, pricing, and next steps.
  - Reviewer/client sign-off is captured in `reviewer-signoff.json` or equivalent.

### Reflection & learning
- The protocol bakes in **retrospective and knowledge capture**:
  - `retrospective-log.json` for “what worked / what didn’t / improvement actions”.
  - `knowledge-base/` for client patterns, automation wins, and edge cases.
  - Roadmap for future enhancements (AI detection bypass, CRM integration, predictive acceptance scoring).
- It treats each proposal run as a data point to improve tone heuristics, pricing rules, and automation coverage over time.
