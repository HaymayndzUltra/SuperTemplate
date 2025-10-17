# Template Governance Guidelines

The unified template registry consolidates every template pack used across the
workflow.  To keep the catalog healthy and compliant with quality gates,
follow the governance practices below.

## Source of Truth

* The registry loads templates from, in order of priority:
  1. `template-packs/`
  2. `unified_workflow/templates/`
  3. `project_generator/template-packs/`
* Higher priority locations automatically override lower priority duplicates.
  Duplicate detections are logged with their resolved paths to aid curation.

## Contribution Checklist

1. **Metadata** – Every template must ship a `template.manifest.json` containing
   a human-readable description, semantic version, and variant information.
2. **Variants** – Non-base variants should live inside subdirectories under the
   template root.  Use descriptive names such as `postgres` or `aws`.
3. **Dependencies** – Declare runtime or infrastructure requirements in the
   manifest so downstream tooling can surface compatibility warnings.
4. **Documentation** – Include a `README.md` in each template detailing setup
   steps, environment variables, and expected outputs.
5. **Testing** – Verify template application through the unified project
   generator before submitting changes.  Ensure generated projects pass
   `python3 -m pytest`.

## Change Management

* Submit governance updates alongside template changes and record rationale in
  commit messages.
* When deprecating a template, add a `deprecated` tag to the manifest and note
  the replacement option.  The registry still lists deprecated templates but
  surfaces their status to consumers.
* Run the unified CLI telemetry report (`unified --show-telemetry`) to discover
  unused templates and determine deprecation candidates.

## Compliance Considerations

Templates that introduce regulated data flows (HIPAA, SOC2, PCI) must include:

* Pre-configured compliance overlays (CI/CD jobs, infrastructure baselines).
* Links to generated compliance documentation (`COMPLIANCE.md`) describing how
  the template satisfies control objectives.
* Automation hooks for `ComplianceValidator` so quality gates can attach
  evidence automatically during audits.

Adhering to these guidelines keeps the registry consistent, auditable, and
ready for integration with workflow automation.
