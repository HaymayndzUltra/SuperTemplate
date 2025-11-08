---
description: Apply instructions from workflows @4-protocol-quality-audit.md
auto_execution_mode: 1
---

# PROTOCOL 4: PROTOCOL QUALITY AUDIT

## ⚡ ENHANCED PROTOCOL VALIDATION ORCHESTRATOR

**This protocol is the quality assurance engine for newly created protocols.** It orchestrates the execution of all 10 validators (50 dimensions) to ensure the protocol meets production standards (score ≥0.95).

## AI Persona

I am a **Protocol Quality Engineer** acting as a **Validation Orchestrator**. My mission is to conduct systematic quality validation of protocols using the comprehensive validator system, ensuring complete compliance across all dimensions.

## Mission

To execute all 10 validators against a newly created protocol, identify gaps, provide remediation guidance, and confirm production readiness with a minimum score of 0.95.

---

## EXECUTION FLOW

### PHASE 1: Validation Preparation

1. **Protocol Discovery:**
   * **[MUST]** Identify protocol to validate:
     - **AI Protocols**: `.cursor/AI-project-workflow/{number}-{name}.md` (uppercase AI)
     - **Web-Dev Protocols**: `.cursor/ai-driven-workflow/{number}-{name}.md` (lowercase ai)
     - Backup: `.artifacts/protocol-generation/protocols/{number}-{name}.md`
   * **[CRITICAL]** Determine protocol type from metadata to select correct directory
   * **[MUST]** Load protocol content completely
   * **[MUST]** Verify protocol structure integrity

2. **Validator System Check:**
   * **[CRITICAL]** Load validator specifications:
     - Access: `validators-system/documentation/MASTER-VALIDATOR-COMPLETE-SPEC.md`
     - Load: `.artifacts/protocol-generation/validator-checklist.md`
   * **[MUST]** Identify which validators are implemented vs. manual checks needed

3. **Baseline Establishment:**
   * **[MUST]** Note protocol metadata:
     - Protocol number and name
     - Type and phase assignment
     - Target validator score from PRD
   * **[MUST]** Initialize validation report structure

---

### PHASE 2: Systematic Validator Execution

**[CRITICAL]** Execute actual validator scripts from `/home/haymayndz/SuperTemplate/validators-system/scripts/`

**IMPORTANT**: Validator scripts default to `.cursor/ai-driven-workflow/` directory. For AI protocols in `.cursor/AI-project-workflow/`, you MUST use the `--protocol-dir` flag:

```bash
--protocol-dir .cursor/AI-project-workflow
```

Execute each validator in sequence using the real validation scripts:

#### VALIDATOR 1: Protocol Identity (5 dimensions)

1. **Execute Protocol Identity Validator:**
   ```bash
   cd /home/haymayndz/SuperTemplate
   # For AI protocols (uppercase AI directory):
   python3 validators-system/scripts/validate_protocol_identity.py --protocol {protocol_number} --workspace . --protocol-dir .cursor/AI-project-workflow --report
   
   # For web-dev protocols (lowercase ai directory):
   python3 validators-system/scripts/validate_protocol_identity.py --protocol {protocol_number} --workspace . --report
   ```
   * **[MUST]** Capture validator output and scores
   * **[MUST]** Parse JSON results for each dimension
   * **[MUST]** Document any failures or warnings

2. **Score Analysis:**
   * Metadata Completeness (0.2): Extract from validator output
   * Prerequisites Documentation (0.2): Extract from validator output
   * Integration Points (0.2): Extract from validator output
   * Compliance Standards (0.2): Extract from validator output
   * Documentation Quality (0.2): Extract from validator output

**Validator 1 Total Score:** Extract from validator JSON output

#### VALIDATOR 2: AI Role Definition (5 dimensions)

1. **Execute AI Role Validator:**
   ```bash
   cd /home/haymayndz/SuperTemplate
   # Use --protocol-dir flag for AI protocols:
   python3 validators-system/scripts/validate_protocol_role.py --protocol {protocol_number} --workspace . --protocol-dir .cursor/AI-project-workflow --report
   ```
   * **[MUST]** Capture validator output and scores
   * **[MUST]** Parse JSON results for each dimension
   * **[MUST]** Document any failures or warnings

2. **Score Analysis:**
   * Role Definition Clarity (0.2): Extract from validator output
   * Mission Statement (0.2): Extract from validator output
   * Behavioral Constraints (0.2): Extract from validator output
   * Output Specifications (0.2): Extract from validator output
   * Behavior Patterns (0.2): Extract from validator output

**Validator 2 Total Score:** Extract from validator JSON output

#### VALIDATOR 3: Workflow Algorithm (5 dimensions)

1. **Execute Workflow Validator:**
   ```bash
   cd /home/haymayndz/SuperTemplate
   python3 validators-system/scripts/validate_protocol_workflow.py --protocol {protocol_number} --workspace . --report
   ```
   * **[MUST]** Capture validator output and scores
   * **[MUST]** Parse JSON results for each dimension
   * **[MUST]** Document any failures or warnings

2. **Score Analysis:**
   * Structure Clarity (0.2): Extract from validator output
   * Step Definitions (0.2): Extract from validator output
   * Markers and Directives (0.2): Extract from validator output
   * Halt Conditions (0.2): Extract from validator output
   * Evidence Generation (0.2): Extract from validator output

**Validator 3 Total Score:** Extract from validator JSON output

#### VALIDATOR 4: Quality Gates (5 dimensions)

1. **Execute Quality Gates Validator:**
   ```bash
   cd /home/haymayndz/SuperTemplate
   python3 validators-system/scripts/validate_protocol_gates.py --protocol {protocol_number} --workspace . --report
   ```
   * **[MUST]** Capture validator output and scores
   * **[MUST]** Parse JSON results for each dimension
   * **[MUST]** Document any failures or warnings

2. **Score Analysis:**
   * Gate Definitions (0.2): Extract from validator output
   * Pass/Fail Criteria (0.2): Extract from validator output
   * Automation Integration (0.2): Extract from validator output
   * Failure Handling (0.2): Extract from validator output
   * Compliance Tracking (0.2): Extract from validator output

**Validator 4 Total Score:** Extract from validator JSON output

#### VALIDATOR 5: Script Integration (5 dimensions)

1. **Execute Script Integration Validator:**
   ```bash
   cd /home/haymayndz/SuperTemplate
   python3 validators-system/scripts/validate_protocol_scripts.py --protocol {protocol_number} --workspace . --report
   ```
   * **[MUST]** Capture validator output and scores
   * **[MUST]** Parse JSON results for each dimension
   * **[MUST]** Document any failures or warnings

2. **Score Analysis:**
   * Script References (0.2): Extract from validator output
   * File Existence (0.2): Extract from validator output
   * Registry Compliance (0.2): Extract from validator output
   * Syntax Validation (0.2): Extract from validator output
   * Error Handling (0.2): Extract from validator output

**Validator 5 Total Score:** Extract from validator JSON output

#### VALIDATOR 6: Communication Protocol (5 dimensions)

1. **Execute Communication Validator:**
   ```bash
   cd /home/haymayndz/SuperTemplate
   python3 validators-system/scripts/validate_protocol_communication.py --protocol {protocol_number} --workspace . --report
   ```
   * **[MUST]** Capture validator output and scores
   * **[MUST]** Parse JSON results for each dimension
   * **[MUST]** Document any failures or warnings

2. **Score Analysis:**
   * Announcement Templates (0.2): Extract from validator output
   * User Interaction (0.2): Extract from validator output
   * Error Messaging (0.2): Extract from validator output
   * Escalation Paths (0.2): Extract from validator output
   * Communication Consistency (0.2): Extract from validator output

**Validator 6 Total Score:** Extract from validator JSON output

#### VALIDATOR 7: Evidence Package (5 dimensions)

1. **Execute Evidence Validator:**
   ```bash
   cd /home/haymayndz/SuperTemplate
   python3 validators-system/scripts/validate_protocol_evidence.py --protocol {protocol_number} --workspace . --report
   ```
   * **[MUST]** Capture validator output and scores
   * **[MUST]** Parse JSON results for each dimension
   * **[MUST]** Document any failures or warnings

2. **Score Analysis:**
   * Evidence Types (0.2): Extract from validator output
   * Storage Locations (0.2): Extract from validator output
   * Validation Methods (0.2): Extract from validator output
   * Retention Policies (0.2): Extract from validator output
   * Audit Trail (0.2): Extract from validator output

**Validator 7 Total Score:** Extract from validator JSON output

#### VALIDATOR 8: Handoff Checklist (5 dimensions)

1. **Execute Handoff Validator:**
   ```bash
   cd /home/haymayndz/SuperTemplate
   python3 validators-system/scripts/validate_protocol_handoff.py --protocol {protocol_number} --workspace . --report
   ```
   * **[MUST]** Capture validator output and scores
   * **[MUST]** Parse JSON results for each dimension
   * **[MUST]** Document any failures or warnings

2. **Score Analysis:**
   * Handoff Criteria (0.2): Extract from validator output
   * Deliverables List (0.2): Extract from validator output
   * Sign-off Requirements (0.2): Extract from validator output
   * Documentation (0.2): Extract from validator output
   * Continuity (0.2): Extract from validator output

**Validator 8 Total Score:** Extract from validator JSON output

#### VALIDATOR 9: Cognitive Reasoning (5 dimensions)

1. **Execute Reasoning Validator:**
   ```bash
   cd /home/haymayndz/SuperTemplate
   python3 validators-system/scripts/validate_protocol_reasoning.py --protocol {protocol_number} --workspace . --report
   ```
   * **[MUST]** Capture validator output and scores
   * **[MUST]** Parse JSON results for each dimension
   * **[MUST]** Document any failures or warnings

2. **Score Analysis:**
   * Reasoning Models (0.2): Extract from validator output
   * Decision Frameworks (0.2): Extract from validator output
   * Context Handling (0.2): Extract from validator output
   * Adaptability (0.2): Extract from validator output
   * Meta-Cognition (0.2): Extract from validator output

**Validator 9 Total Score:** Extract from validator JSON output

#### VALIDATOR 10: Meta-Reflection (5 dimensions)

1. **Execute Reflection Validator:**
   ```bash
   cd /home/haymayndz/SuperTemplate
   python3 validators-system/scripts/validate_protocol_reflection.py --protocol {protocol_number} --workspace . --report
   ```
   * **[MUST]** Capture validator output and scores
   * **[MUST]** Parse JSON results for each dimension
   * **[MUST]** Document any failures or warnings

2. **Score Analysis:**
   * Self-Assessment (0.2): Extract from validator output
   * Learning Integration (0.2): Extract from validator output
   * Improvement Cycles (0.2): Extract from validator output
   * Feedback Processing (0.2): Extract from validator output
   * Evolution (0.2): Extract from validator output

**Validator 10 Total Score:** Extract from validator JSON output

---

### PHASE 3: Comprehensive Score Calculation

1. **Execute All Validators Script:**
   ```bash
   cd /home/haymayndz/SuperTemplate
   python3 validators-system/scripts/validate_all_protocols.py --protocol {protocol_number} --workspace . --output .artifacts/protocol-generation/validation-scores-{protocol_number}.json
   ```
   * **[CRITICAL]** This script runs all 10 validators automatically
   * **[MUST]** Capture combined JSON output with all scores
   * **[MUST]** Parse overall score and individual validator scores

2. **Score Aggregation:**
   * **Critical Validators Weight (70%)**: Validators 4, 5, 7, 8, 9
   * **Supporting Validators Weight (30%)**: Validators 1, 2, 3, 6, 10
   * **Overall Score Formula**: `(Critical_Avg × 0.7) + (Supporting_Avg × 0.3)`
   * **Pass Threshold**: Overall score ≥0.95 required for production

3. **Score Analysis:**
   * **[MUST]** Identify any validator scoring <0.90
   * **[MUST]** Flag critical validators scoring <0.95
   * **[MUST]** Calculate remediation priority based on score gaps

---

### PHASE 4: Evidence Generation and Reporting

1. **Generate Validation Evidence:**
   ```bash
   # Create evidence directory
   mkdir -p .artifacts/protocol-generation/validation-evidence-{protocol_number}/
   
   # Copy all validator outputs to evidence directory
   cp .artifacts/protocol-generation/validation-scores-{protocol_number}.json .artifacts/protocol-generation/validation-evidence-{protocol_number}/
   
   # Generate individual validator reports
   for validator in identity role workflow gates scripts communication evidence handoff reasoning reflection; do
     python3 validators-system/scripts/validate_protocol_${validator}.py --protocol {protocol_number} --file {protocol_path} --report .artif