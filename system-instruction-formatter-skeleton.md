---
description: "TAGS: [{TAGS}] | TRIGGERS: {TRIGGERS} | SCOPE: {SCOPE} | DESCRIPTION: {DESCRIPTION}"
globs: {GLOB_PATTERN}
---

<!-- SYSTEM-START:{SYSTEM_IDENTIFIER} -->

# {RULE_NAME} ({RULE_TYPE})

## Meta-Intent
{META_INTENT_DESCRIPTION}

## AI Persona
You are a **{PERSONA_ROLE}**.

### Behavioral Directives
- Treat **[STRICT]** as non-negotiable; **[GUIDELINE]** as contextual.
- {BEHAVIORAL_DIRECTIVE_1}
- {BEHAVIORAL_DIRECTIVE_2}

---

## Core Principle
{CORE_PRINCIPLE_STATEMENT}

---

## Directive Grammar
{RULE_GRAMMAR_REFERENCE}

- Canonical tags: `[STRICT]`, `[GUIDELINE]`, `[CRITICAL]`, `[REQUIRED]`, `[OPTIONAL]`
- {DEPRECATED_ALIAS_MAPPING}

---

## Precedence & Conflict Resolution

### **[STRICT] Precedence Matrix**
1. {PRECEDENCE_RULE_1}
2. {PRECEDENCE_RULE_2}
3. {PRECEDENCE_RULE_3}

### **[STRICT] Conflict Protocol**
- {CONFLICT_DETECTION_RULE}
- Emit:
  `[RULE CONFLICT] "{CONFLICT_X}" conflicts with "{CONFLICT_Y}". Quote: "{CONFLICT_Y_EXCERPT}". Request guidance.`
- {AUTO_RESOLUTION_RULE}

---

## Formatting Process

### **[STRICT] STEP 1: {STEP_1_NAME}**
- {STEP_1_DESCRIPTION_1}
- {STEP_1_DESCRIPTION_2}

### **[STRICT] STEP 2: {STEP_2_NAME}**
- {STEP_2_DESCRIPTION_1}
- {STEP_2_DESCRIPTION_2}

### **[STRICT] STEP 3: {STEP_3_NAME}**
- {STEP_3_DESCRIPTION_1}
- {STEP_3_DESCRIPTION_2}

### **[STRICT] Instruction Type Detection**
- Classify the raw instruction into exactly one type:
  - {INSTRUCTION_TYPE_1} | {INSTRUCTION_TYPE_2} | {INSTRUCTION_TYPE_3} | {INSTRUCTION_TYPE_4} | {INSTRUCTION_TYPE_5}
- If ambiguous → emit `[VALIDATION_ERROR] Ambiguous instruction type`.

### **[STRICT] Section Selection Rules**
- {SECTION_SELECTION_RULE_1}
- {SECTION_SELECTION_RULE_2}
- {SECTION_SELECTION_RULE_3}
- {SECTION_SELECTION_RULE_4}
- {SECTION_SELECTION_RULE_5}
- {SECTION_SELECTION_RULE_6}
- {SECTION_SELECTION_RULE_7}
- {SECTION_SELECTION_RULE_8}

### **[STRICT] Canonicalization & Failure Modes**
- {CANONICALIZATION_RULE_1}
- Unknown tags → `[VALIDATION_ERROR] Unknown directive tag "{TAG_NAME}"`.
- {MALFORMED_HEADING_RULE}

### **[STRICT] Minimal Profiles (Auto-apply)**
- {PROFILE_TYPE_1}:
  - Include: {PROFILE_INCLUDE_1}
  - Optional: {PROFILE_OPTIONAL_1}
  - Omit: {PROFILE_OMIT_1}
- {PROFILE_TYPE_2}:
  - Include: {PROFILE_INCLUDE_2}
  - Optional: {PROFILE_OPTIONAL_2}
- {PROFILE_TYPE_3}:
  - Include: {PROFILE_INCLUDE_3}
  - Require: {PROFILE_REQUIRE_3}
- {PROFILE_TYPE_4}:
  - Include: {PROFILE_INCLUDE_4}
  - Omit: {PROFILE_OMIT_4}
- {PROFILE_TYPE_5}:
  - Include: {PROFILE_INCLUDE_5}
  - Optional: {PROFILE_OPTIONAL_5}

---

## Validation & Quality Gates

### **[STRICT] Structural Validation**
- {STRUCTURAL_VALIDATION_RULE_1}
- {STRUCTURAL_VALIDATION_RULE_2}

### **[STRICT] Enforcement Rubric**
- {ENFORCEMENT_RUBRIC_1}
- {ENFORCEMENT_RUBRIC_2}
- {ENFORCEMENT_RUBRIC_3}

### **[STRICT] Lint Rules**
- {LINT_RULE_1}
- {LINT_RULE_2}
- {LINT_RULE_3}

### **[STRICT] Validation Gates (Applicability-Aware)**
- Gate A ({GATE_A_NAME}): {GATE_A_CRITERIA}
- Gate B ({GATE_B_NAME}): {GATE_B_CRITERIA}
- Gate C ({GATE_C_NAME}): {GATE_C_CRITERIA}
- Gate D ({GATE_D_NAME}): {GATE_D_CRITERIA}
- Gate E ({GATE_E_NAME}): {GATE_E_CRITERIA}

### **[STRICT] Applicability Report**
- Produce a short table: `Section | Included? | Reason`
- If any mandatory section (per type) is missing → `[VALIDATION_ERROR] Missing required section for {SECTION_TYPE}`.

---

## Security & Safety Protocols

### **[STRICT] Security Sections**
- If touching {SECURITY_DOMAINS}:
  - {SECURITY_REQUIREMENT_1}
  - {SECURITY_REQUIREMENT_2}
  - {SECURITY_REQUIREMENT_3}

### **[STRICT] Compliance Hooks**
- {COMPLIANCE_PLACEHOLDER_1}
- {COMPLIANCE_PLACEHOLDER_2}

---

## Versioning & Change Management

### **[STRICT] Semver**
- `{VERSION_FORMAT}` in rule footer
- {CHANGELOG_REQUIREMENT}

### **[STRICT] Deprecation**
- {DEPRECATION_RULE_1}
- {DEPRECATION_RULE_2}

---

## Testing & Verification

### **[STRICT] Test Harness**
- Include at least one runnable example ({EXAMPLE_INPUT} → {EXAMPLE_OUTPUT})
- Include one failure case ({FAILURE_CASE}) with expected error message

### **[GUIDELINE] Golden Samples**
- {GOLDEN_SAMPLES_RULE}

---

## Telemetry & Observability

### **[GUIDELINE] Metrics**
- Count: {METRIC_1}, {METRIC_2}, {METRIC_3}
- Emit `{SIGNAL_1}`, `{SIGNAL_2}`, `{SIGNAL_3}` signals

### **[GUIDELINE] Applicability Metrics**
- Emit JSON: `{"type":"{TYPE_PLACEHOLDER}", "included":["{INCLUDED_PLACEHOLDER}"], "skipped":["{SKIPPED_PLACEHOLDER}"]}`

---

## Extensibility

### **[STRICT] Extension Points**
- `{HOOK_1}`, `{HOOK_2}`
- `{HOOK_3}`, `{HOOK_4}`

### **[GUIDELINE] Plugin Schema**
- Minimal interface: `{INTERFACE_PROPERTY_1}`, `{INTERFACE_PROPERTY_2}`, `{INTERFACE_METHOD}`

---

## Example Transformation

### ✅ Correct
```markdown
### **[STRICT]** {CORRECT_EXAMPLE_TITLE}
- {CORRECT_EXAMPLE_DESCRIPTION_1}
- {CORRECT_EXAMPLE_DESCRIPTION_2}
```

### ❌ Anti-Pattern
```markdown
### {ANTI_PATTERN_TITLE}
- {ANTI_PATTERN_DESCRIPTION_1}
- {ANTI_PATTERN_DESCRIPTION_2}
```

---

## Usage

### **[STRICT] Input Requirements**
- {INPUT_REQUIREMENT_1}
- {INPUT_REQUIREMENT_2}

### **[STRICT] Processing Steps**
- {PROCESSING_STEP_1}
- {PROCESSING_STEP_2}
- {PROCESSING_STEP_3}

### **[STRICT] Output Delivery**
- {OUTPUT_DELIVERY_RULE_1}
- Signals: `{OUTPUT_SIGNAL}`

---

## Success Criteria

### **[STRICT] Formatting Accuracy**
- {FORMATTING_ACCURACY_CRITERIA_1}
- {FORMATTING_ACCURACY_CRITERIA_2}

### **[STRICT] Content Preservation**
- {CONTENT_PRESERVATION_RULE}

---

## System Integrity Check
- Emit `{INTEGRITY_SIGNAL}` when all gates pass

---

## Branding (Optional, Non-intrusive)
- Announce once per session after rules load (if enabled):
  `[BRAND] {BRAND_NAME} v{VERSION} initialized`
- Append footer only on final formatted document (not in code/YAML):
  `— Powered by {BRAND_NAME} v{VERSION}`
- Env switch: `{BRAND_ENV_VAR}=false` disables announcements.

---

## Version
- Spec: `{VERSION_NUMBER}`
- Changelog:
  - {CHANGELOG_ENTRY_1}
  - {CHANGELOG_ENTRY_2}
  - {CHANGELOG_ENTRY_3}

<!-- SYSTEM-END:{SYSTEM_IDENTIFIER} -->
