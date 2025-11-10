# Transformation Engine: Template-to-Instance Protocol Generation

**Version**: 1.0.0  
**Created**: 2025-01-10  
**Purpose**: Transform foundation protocol templates into project-specific customized instances

---

## 🎯 OVERVIEW

The Transformation Engine is the core component of the Project-Specific Protocol Generation System. It takes foundation protocol templates from `.cursor/ai-driven-workflow/` and transforms them into customized, project-specific protocol instances saved in `{project}/.cursor/project-protocols/`.

### Key Capabilities
- **Template Loading**: Read and parse foundation protocol templates
- **Parameterization**: Replace placeholders with project-specific values
- **Customization**: Inject tech stack-specific sections and validation rules
- **Validation**: Ensure generated protocols pass 11-validator system (≥0.95 score)
- **Tracking**: Maintain generation manifest for audit and regeneration

---

## 📁 DIRECTORY STRUCTURE

```
transformation-engine/
├── README.md (this file)
├── core/
│   ├── __init__.py
│   ├── template_loader.py (load foundation templates)
│   ├── parameter_extractor.py (extract parameterization points)
│   ├── transformation_rules.py (apply transformation rules)
│   ├── customization_injector.py (inject project-specific customizations)
│   └── protocol_writer.py (write generated protocols to disk)
├── rules/
│   ├── project_name_substitution.py
│   ├── tech_stack_customization.py
│   ├── workflow_step_customization.py
│   ├── artifact_path_customization.py
│   └── validation_rule_injection.py
├── schemas/
│   ├── template_schema.json (foundation template structure)
│   ├── transformation_config_schema.json (transformation configuration)
│   └── generation_manifest_schema.json (generation tracking)
├── tests/
│   ├── test_template_loader.py
│   ├── test_transformation_rules.py
│   └── test_integration.py
└── examples/
    ├── example_template.md (sample foundation template)
    ├── example_transformed.md (sample generated protocol)
    └── example_manifest.json (sample generation manifest)
```

---

## 🔧 TRANSFORMATION RULES

### Rule 1: Project Name Substitution

**Purpose**: Replace generic placeholders with actual project information

**Placeholders**:
- `{PROJECT_NAME}` → Actual project name from PROJECT-BRIEF.md
- `{PROJECT_TYPE}` → Classification from Protocol 05b PHASE 2 (e.g., "Web Application", "AI/ML Application")
- `{PROJECT_DOMAIN}` → Domain from PROJECT-BRIEF.md (e.g., "E-commerce", "Healthcare", "Finance")
- `{PROJECT_DESCRIPTION}` → Short description from PROJECT-BRIEF.md
- `{COMPANY_NAME}` → Company/client name from PROJECT-BRIEF.md

**Example**:
```markdown
# PROTOCOL 06: CREATE PRD FOR {PROJECT_NAME}

**Project Type**: {PROJECT_TYPE}
**Domain**: {PROJECT_DOMAIN}
```

**Transforms to**:
```markdown
# PROTOCOL 06: CREATE PRD FOR Artisan's Corner Dashboard

**Project Type**: Web Application
**Domain**: E-commerce Analytics
```

**Implementation**: `rules/project_name_substitution.py`

---

### Rule 2: Tech Stack Customization

**Purpose**: Inject technology-specific sections, validation steps, and automation scripts

**Tech Stack Detection**: Read from PROJECT-BRIEF.md `tech_stack` section:
```yaml
tech_stack:
  frontend: "Next.js 14, React 18, TypeScript, TailwindCSS"
  backend: "FastAPI, Python 3.11"
  database: "PostgreSQL 15, Redis"
  infrastructure: "Docker, AWS ECS, CloudFront"
  ai_ml: "TensorFlow 2.x, scikit-learn" (if applicable)
```

**Customization Logic**:

1. **Frontend Customization**:
   - If `frontend` contains "Next.js" → Inject Next.js-specific validation steps
   - If `frontend` contains "React" → Add React component testing requirements
   - If `frontend` contains "TypeScript" → Add TypeScript type checking gates

2. **Backend Customization**:
   - If `backend` contains "FastAPI" → Inject FastAPI-specific API testing
   - If `backend` contains "Django" → Add Django migration validation
   - If `backend` contains "Go" → Add Go-specific linting and testing

3. **Database Customization**:
   - If `database` contains "PostgreSQL" → Add PostgreSQL schema validation
   - If `database` contains "MongoDB" → Add MongoDB schema validation
   - If `database` contains "Firebase" → Add Firebase security rules validation

4. **AI/ML Customization**:
   - If `ai_ml` present → Inject AI-specific protocols (model training, evaluation, deployment)
   - Add model validation gates
   - Add data pipeline validation

**Example Injection**:
```markdown
### STEP X.Y: Validate Frontend Build (Next.js-specific)

**Action:** **[MUST]** Validate Next.js build configuration:

```bash
# Next.js-specific validation
npm run build
npm run type-check
npm run lint
```

**Quality Gates**:
- TypeScript compilation: 0 errors
- ESLint: 0 errors, <10 warnings
- Build size: <500KB initial bundle
```

**Implementation**: `rules/tech_stack_customization.py`

---

### Rule 3: Workflow Step Customization

**Purpose**: Add, remove, or modify workflow steps based on project characteristics

**Customization Triggers**:
- **Project Complexity** (from Protocol 05b classification):
  - Simple → Reduce validation steps, streamline workflow
  - Standard → Use default workflow steps
  - Complex → Add additional validation gates, detailed documentation
  - Enterprise → Add compliance checks, security audits, extensive testing

- **Team Size** (from PROJECT-BRIEF.md):
  - Solo (1) → Simplify approval steps, reduce meetings
  - Small (2-5) → Standard workflow
  - Medium (6-15) → Add coordination steps, team reviews
  - Large (16+) → Add formal approval gates, stakeholder sign-offs

- **Timeline Constraints** (from PROJECT-BRIEF.md):
  - Tight (<4 weeks) → Prioritize critical steps, allow parallel execution
  - Standard (4-12 weeks) → Use default workflow
  - Flexible (>12 weeks) → Add optional quality improvements, research phases

**Example Customization**:

**Original Template**:
```markdown
### STEP 3.1: Create Initial PRD Draft
### STEP 3.2: Internal Review
### STEP 3.3: Stakeholder Review
### STEP 3.4: Finalize PRD
```

**Customized for Solo Developer**:
```markdown
### STEP 3.1: Create Initial PRD Draft
### STEP 3.2: Self-Review Checklist
### STEP 3.3: Finalize PRD
```

**Customized for Enterprise Team**:
```markdown
### STEP 3.1: Create Initial PRD Draft
### STEP 3.2: Technical Lead Review
### STEP 3.3: Architecture Review Board
### STEP 3.4: Security Review
### STEP 3.5: Stakeholder Approval
### STEP 3.6: Legal/Compliance Review
### STEP 3.7: Finalize PRD
```

**Implementation**: `rules/workflow_step_customization.py`

---

### Rule 4: Artifact Path Customization

**Purpose**: Update artifact paths to project-specific locations

**Path Transformations**:
- `.artifacts/protocol-{ID}/` → `.artifacts/{project-name}/protocol-{ID}/`
- Generic artifact names → Project-specific names
- Update integration points to reference project-specific paths

**Example**:

**Original Template**:
```markdown
Evidence: `.artifacts/protocol-06/prd-draft.md`
```

**Customized**:
```markdown
Evidence: `.artifacts/artisans-corner-dashboard/protocol-06/prd-draft.md`
```

**Implementation**: `rules/artifact_path_customization.py`

---

### Rule 5: Validation Rule Injection

**Purpose**: Add project-specific validators and quality thresholds

**Injection Points**:
- Quality gates → Inject project-specific thresholds
- Validation scripts → Add tech stack-specific validators
- Compliance requirements → Inject regulatory checks (GDPR, HIPAA, SOC2)

**Example**:

**Original Template**:
```markdown
### Gate 1: PRD Completeness
- All required sections present
- Validation score ≥0.90
```

**Customized for Healthcare Project**:
```markdown
### Gate 1: PRD Completeness
- All required sections present
- Validation score ≥0.95 (higher threshold for healthcare)
- HIPAA compliance checklist complete
- PHI handling procedures documented
- Security requirements validated
```

**Implementation**: `rules/validation_rule_injection.py`

---

## 🔄 TRANSFORMATION PIPELINE

### Pipeline Flow

```
1. LOAD TEMPLATES
   ↓
   Read foundation templates from .cursor/ai-driven-workflow/
   Parse YAML frontmatter
   Extract parameterization points
   ↓
2. EXTRACT CONTEXT
   ↓
   Read PROJECT-BRIEF.md
   Read PROTOCOL-EXECUTION-PLAN.md
   Read customization requirements
   ↓
3. APPLY TRANSFORMATIONS
   ↓
   Rule 1: Project Name Substitution
   Rule 2: Tech Stack Customization
   Rule 3: Workflow Step Customization
   Rule 4: Artifact Path Customization
   Rule 5: Validation Rule Injection
   ↓
4. VALIDATE GENERATED PROTOCOLS
   ↓
   Run 11-validator system
   Check score ≥0.95
   Retry if needed (max 3 attempts)
   ↓
5. WRITE TO DISK
   ↓
   Save to .cursor/project-protocols/
   Create generation manifest
   Update PROTOCOL-EXECUTION-PLAN.md
   ↓
6. GENERATE REPORT
   ↓
   Create PROTOCOL-GENERATION-REPORT.md
   Log all transformations applied
```

---

## 📊 GENERATION MANIFEST

### Manifest Structure

```json
{
  "generation_timestamp": "2025-01-10T14:30:00Z",
  "project_name": "artisans-corner-dashboard",
  "project_type": "Web Application",
  "foundation_version": "1.0.0",
  "transformation_engine_version": "1.0.0",
  "protocols_generated": [
    {
      "protocol_id": "06",
      "protocol_name": "Create PRD",
      "source_template": ".cursor/ai-driven-workflow/06-create-prd.md",
      "generated_file": ".cursor/project-protocols/06-create-prd-artisans-corner.md",
      "customizations_applied": [
        "project_name_substitution",
        "tech_stack_customization_nextjs",
        "tech_stack_customization_fastapi",
        "workflow_step_customization_solo",
        "artifact_path_customization",
        "validation_rule_injection_ecommerce"
      ],
      "validation_score": 0.97,
      "generation_duration_ms": 1250
    }
  ],
  "total_protocols": 15,
  "total_customizations": 42,
  "total_duration_ms": 18750,
  "validation_summary": {
    "protocols_passed": 15,
    "protocols_failed": 0,
    "average_score": 0.96,
    "min_score": 0.95,
    "max_score": 0.98
  }
}
```

---

## 🧪 TESTING STRATEGY

### Unit Tests
- Test each transformation rule independently
- Verify placeholder replacement accuracy
- Validate customization injection logic
- Test error handling and edge cases

### Integration Tests
- Test complete transformation pipeline
- Verify generated protocols pass validators
- Test manifest generation
- Verify file writing and permissions

### End-to-End Tests
- Test with real PROJECT-BRIEF.md files
- Generate protocols for different project types
- Validate against 11-validator system
- Verify regeneration capability

---

## 🚀 USAGE

### Basic Usage

```bash
# Generate project-specific protocols
python scripts/orchestration/transform_protocols.py \
  --templates .artifacts/protocol-05b/loaded-templates.json \
  --project-brief PROJECT-BRIEF.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --output .artifacts/protocol-05b/transformed-protocols.json
```

### Advanced Usage

```bash
# Generate with custom transformation rules
python scripts/orchestration/transform_protocols.py \
  --templates .artifacts/protocol-05b/loaded-templates.json \
  --project-brief PROJECT-BRIEF.md \
  --execution-plan PROTOCOL-EXECUTION-PLAN.md \
  --custom-rules transformation-engine/custom-rules.yaml \
  --output .artifacts/protocol-05b/transformed-protocols.json \
  --verbose
```

---

## 📝 CONFIGURATION

### Transformation Configuration File

```yaml
# transformation-config.yaml

transformation_rules:
  project_name_substitution:
    enabled: true
    placeholders:
      - "{PROJECT_NAME}"
      - "{PROJECT_TYPE}"
      - "{PROJECT_DOMAIN}"
  
  tech_stack_customization:
    enabled: true
    frameworks:
      nextjs:
        validation_steps: ["build", "type-check", "lint"]
        quality_gates: ["bundle_size", "lighthouse_score"]
      fastapi:
        validation_steps: ["pytest", "mypy", "ruff"]
        quality_gates: ["test_coverage", "api_response_time"]
  
  workflow_step_customization:
    enabled: true
    complexity_mapping:
      simple: "streamlined"
      standard: "default"
      complex: "detailed"
      enterprise: "comprehensive"
  
  artifact_path_customization:
    enabled: true
    path_template: ".artifacts/{project-name}/protocol-{id}/"
  
  validation_rule_injection:
    enabled: true
    compliance_frameworks:
      - "GDPR" (if EU project)
      - "HIPAA" (if healthcare)
      - "SOC2" (if enterprise)

validation:
  min_score: 0.95
  max_retry_attempts: 3
  auto_fix_enabled: true

output:
  directory: ".cursor/project-protocols"
  naming_convention: "{protocol-id}-{protocol-name}-{project-name}.md"
  manifest_file: ".protocol-manifest.json"
```

---

## 🔍 TROUBLESHOOTING

### Common Issues

**Issue 1: Validation Score <0.95**
- **Cause**: Generated protocol missing required sections or invalid format
- **Solution**: Check transformation rules, ensure all required sections injected
- **Auto-fix**: Enable `auto_fix_enabled: true` in configuration

**Issue 2: Template Not Found**
- **Cause**: Foundation template missing or incorrect path
- **Solution**: Verify template exists in `.cursor/ai-driven-workflow/`
- **Fallback**: Skip protocol or use generic template

**Issue 3: Customization Injection Failed**
- **Cause**: Invalid tech stack specification or missing customization rule
- **Solution**: Validate PROJECT-BRIEF.md tech_stack section
- **Fallback**: Generate without customization (warn user)

**Issue 4: Write Permission Denied**
- **Cause**: Insufficient permissions for `.cursor/project-protocols/` directory
- **Solution**: Check directory permissions, create directory if missing
- **Escalation**: Block generation, request user intervention

---

## 📚 REFERENCES

- **Protocol 05b**: Main orchestration protocol that invokes transformation engine
- **Decision Framework**: Architectural decision rationale for Hybrid Architecture
- **11-Validator System**: Validation system for generated protocols
- **PROJECT-BRIEF.md**: Source of project-specific information

---

**Status**: ✅ Active  
**Maintained By**: Transformation Engine Team  
**Last Updated**: 2025-01-10
