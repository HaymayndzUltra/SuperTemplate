# Audit Implementation Plan

## Task 1
- Task Name: Reconcile protocol-referenced gate scripts or provide fallbacks
- Report Source: "Implement minimal gate scripts for each referenced validate_gate_* and run_protocol_*_gates.py, or update protocols to reference existing, real scripts (e.g., consolidate gate checks into scripts/validate_workflow_integration.py). Add a central scripts/script-registry.json entry per new script and enforce with Protocol 23. Expected Outcome: Protocol automation becomes runnable; CI failures reduced. Effort: M Risk: Low-Medium." / "Missing gate scripts referenced by protocols... Severity: High Confidence: High"
- Report Section: Recommendations – Reconcile protocol-referenced gate scripts or provide fallbacks
- Priority: High
- Effort: M
- Action Steps:
  1. Implement minimal gate scripts for each referenced validate_gate_* and run_protocol_*_gates.py, or update protocols to reference existing, real scripts (e.g., consolidate gate checks into scripts/validate_workflow_integration.py).
  2. Add a central scripts/script-registry.json entry per new script and enforce with Protocol 23.
- Success Criteria: Protocol automation becomes runnable; CI failures reduced.

## Task 2
- Task Name: Correct CI snippets and align gate runner names
- Report Source: "Update Protocol 11 and 15 CI examples to reference the correct runner names and protocol numbers. Add a test in scripts/validate_workflow_integration.py to detect protocol-number mismatches in example YAML. Expected Outcome: Clear, accurate CI wiring; fewer operator errors. Effort: S Risk: Low." / "CI snippet/script mismatches (wrong protocol numbers in filenames)... Severity: Medium Confidence: High"
- Report Section: Recommendations – Correct CI snippets and align gate runner names
- Priority: Medium
- Effort: S
- Action Steps:
  1. Update Protocol 11 and 15 CI examples to reference the correct runner names and protocol numbers.
  2. Add a test in scripts/validate_workflow_integration.py to detect protocol-number mismatches in example YAML.
- Success Criteria: Clear, accurate CI wiring; fewer operator errors.

## Task 3
- Task Name: Add protocol-level template-pack selection and generator step
- Report Source: "In Protocol 05–07, add a “Template Selection & Generator” step referencing scripts/generate_client_project.py with required inputs and evidence outputs (e.g., generator-config.json, scaffold manifests). Include decision criteria for stacks and compliance. Expected Outcome: Standardized scaffolding across projects; better integration of template-packs. Effort: M Risk: Low." / "Protocols lack explicit template-pack selection/usage guidance... Severity: Medium Confidence: High"
- Report Section: Recommendations – Add protocol-level template-pack selection and generator step
- Priority: Medium
- Effort: M
- Action Steps:
  1. In Protocol 05–07, add a “Template Selection & Generator” step referencing scripts/generate_client_project.py with required inputs and evidence outputs (e.g., generator-config.json, scaffold manifests).
  2. Include decision criteria for stacks and compliance.
- Success Criteria: Standardized scaffolding across projects; better integration of template-packs.
