# Protocol Alignment Analysis Report
**Generated:** 2025-11-06  
**Scope:** Scaffold/Template/Generation Flow Alignment

---

## Executive Summary

Analyzed 23 protocols and identified critical misalignments between:
- Protocol definitions (what they say)
- Script implementations (what exists)
- Template system (how it works)

**Key Finding:** The generation flow is functional but has protocol documentation gaps and redundant code that should be removed.

---

## Complete Flow Map

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 0: FOUNDATION & DISCOVERY                                 │
├─────────────────────────────────────────────────────────────────┤
│ P01 → P02 → P03: Create PROJECT-BRIEF.md                       │
│                   ├─ MUST include YAML frontmatter:            │
│                   │   name, industry, project_type,            │
│                   │   frontend, backend, database,             │
│                   │   auth, deploy, compliance                 │
│                   └─ Protocol 03 output                        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ P04: PROJECT BOOTSTRAP & CONTEXT ENGINEERING                    │
├─────────────────────────────────────────────────────────────────┤
│ Line 174: Dry run preview                                      │
│   python scripts/generate_from_brief.py \                      │
│     --brief PROJECT-BRIEF.md --dry-run --yes                   │
│                                                                 │
│ Line 228: Actual scaffold generation                           │
│   python scripts/generate_from_brief.py \                      │
│     --brief PROJECT-BRIEF.md \                                 │
│     --output-root . --in-place --no-subdir \                   │
│     --no-cursor-assets --force --yes                           │
│                                                                 │
│ Outputs:                                                        │
│   ├─ bootstrap-manifest.json                                   │
│   ├─ Scaffold directory structure                              │
│   └─ generator-config.json                                     │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ GENERATION CHAIN (Internal)                                     │
├─────────────────────────────────────────────────────────────────┤
│ generate_from_brief.py                                          │
│   ├─ Parses PROJECT-BRIEF.md frontmatter                       │
│   │   (BriefParser.parse() → ScaffoldSpec)                     │
│   ├─ Extracts: frontend, backend, database, etc.               │
│   └─ Calls: generate_client_project.py with params             │
│                                                                 │
│ generate_client_project.py                                      │
│   ├─ Uses: ProjectGenerator                                    │
│   ├─ Reads: template-packs/ via UnifiedTemplateRegistry        │
│   │   ├─ template-packs/frontend/{nextjs,angular,nuxt,expo}   │
│   │   ├─ template-packs/backend/{fastapi,django,nestjs,go}    │
│   │   └─ template-packs/database/{postgres,mongodb,firebase}  │
│   └─ Generates: Complete project scaffold                      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ P05: BOOTSTRAP YOUR PROJECT (Legacy Alignment)                 │
│ P06: CREATE PRD                                                 │
│ P07: TECHNICAL DESIGN & ARCHITECTURE                           │
│ P08: GENERATE TASKS                                             │
│ P09: ENVIRONMENT SETUP VALIDATION                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Issues & Conflicts Identified

### 🔴 CRITICAL ISSUES

#### 1. Missing File Reference (Protocol 04, Line 487)
**Location:** `.cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md:487`

**Current:**
```bash
python3 scripts/bootstrap_registry_compare.py \
  --manifest .artifacts/protocol-04/bootstrap-manifest.json \
  --registry template-packs/registry.yaml
```

**Problem:**
- `scripts/bootstrap_registry_compare.py` - ❌ DOES NOT EXIST
- `template-packs/registry.yaml` - ❌ DOES NOT EXIST
- UnifiedTemplateRegistry auto-discovers templates (no YAML needed)

**Impact:** Protocol 04 validation step will fail

**Recommendation:** REMOVE this line or create the script if validation is needed

---

#### 2. Hardcoded Rules in generate_from_brief.py (Lines 27-84)
**Location:** `scripts/generate_from_brief.py`

**Current Implementation:**
```python
# Lines 27-51: Hardcoded rule mappings
FRONTEND_RULES = {
    "nextjs": ["nextjs.mdc", "nextjs-formatting.mdc", ...],
    "angular": ["angular.mdc", "typescript.mdc"],
    "nuxt": ["vue.mdc", "typescript.mdc"],
    "expo": ["expo.mdc", "react-native.mdc", "typescript.mdc"],
}

BACKEND_RULES = {
    "fastapi": ["fastapi.mdc", "python.mdc", "rest-api.mdc", ...],
    "django": ["django.mdc", "python.mdc", ...],
    "nestjs": ["nodejs.mdc", "typescript.mdc", ...],
    "go": ["golang.mdc", "nethttp.mdc", ...],
}

DB_ADDONS = {...}
COMPLIANCE_RULES = {...}

# Lines 66-84: Manual manifest building
def build_fe_manifest(frontend, compliance): ...
def build_be_manifest(backend, database, compliance): ...
```

**Problem:**
- Duplicates logic already in `ProjectGenerator._resolve_template_rule_source()` (generator.py:640)
- Harder to maintain (2 places to update)
- Bypasses UnifiedTemplateRegistry's auto-discovery

**Impact:** 
- Rule updates require changes in multiple files
- Risk of inconsistency between hardcoded lists and actual templates

**Recommendation:** 
- REMOVE hardcoded mappings
- Let `ProjectGenerator` handle rule selection via `_resolve_template_rule_source()`
- Or move logic to template-packs metadata if centralized configuration needed

---

#### 3. Protocol 07 Missing Stack Selection Step
**Location:** `.cursor/ai-driven-workflow/07-technical-design-architecture.md`

**Current State:**
- Line 155: References "Technology stack limitations" as constraint
- ❌ NO explicit step to SELECT technology stack
- ❌ NO integration with template-packs selection
- ❌ NO output defining chosen stack for Protocol 08

**Problem:**
- Protocol 03 creates brief with stack info (frontmatter)
- Protocol 04 generates scaffold based on brief
- **BUT**: Protocol 07 (Architecture Design) should validate/confirm stack decisions
- **GAP**: No formal architecture decision record for stack selection

**Impact:**
- Architecture decisions disconnected from scaffold generation
- No ADR (Architecture Decision Record) for stack choices
- Downstream protocols assume stack without documented rationale

**Recommendation:**
Add to Protocol 07:
```markdown
### STEP 2: Technology Stack Validation

1. **`[MUST]` Review Generated Stack:**
   * **Action:** Review scaffold stack from Protocol 04 bootstrap-manifest.json
   * **Evidence:** `.artifacts/protocol-07/stack-review.json`
   * **Validation:** Stack aligns with architectural constraints

2. **`[MUST]` Document Stack Rationale:**
   * **Action:** Create ADR documenting why selected stack (frontend/backend/db)
   * **Evidence:** `.artifacts/protocol-07/adr-stack-selection.md`
   * **Validation:** ADR includes alternatives considered
```

---

### 🟡 MEDIUM PRIORITY ISSUES

#### 4. Protocol 03 Missing Frontmatter Specification
**Location:** `.cursor/ai-driven-workflow/03-project-brief-creation.md`

**Current State:**
- Protocol 03 creates PROJECT-BRIEF.md
- ❌ NO specification that frontmatter is REQUIRED
- ❌ NO template showing frontmatter format
- ❌ NO validation that frontmatter is present

**Problem:**
- BriefParser expects frontmatter (brief_parser.py:99-111)
- If frontmatter missing, parser falls back to keyword guessing (less accurate)
- No quality gate ensuring brief has required metadata

**Impact:**
- Scaffold generation may select wrong stack
- Manual intervention needed if parser guesses incorrectly

**Recommendation:**
Add to Protocol 03:
```markdown
### STEP 3: Structure Project Brief

1. **`[MUST]` Create Brief with YAML Frontmatter:**
   * **Action:** Initialize PROJECT-BRIEF.md with required frontmatter
   * **Template:**
     ```yaml
     ---
     name: project-name
     industry: healthcare|finance|ecommerce|saas|enterprise
     project_type: web|mobile|api|fullstack|microservices
     frontend: nextjs|nuxt|angular|expo|none
     backend: fastapi|django|nestjs|go|none
     database: postgres|mongodb|firebase|none
     auth: auth0|firebase|cognito|custom|none
     deploy: aws|azure|gcp|vercel|self-hosted
     compliance: hipaa,gdpr,sox,pci
     features: feature1,feature2
     ---
     # Project Brief: {name}
     ...
     ```
   * **Evidence:** `.artifacts/protocol-03/PROJECT-BRIEF.md`
   * **Validation:** Frontmatter present and parseable
```

---

#### 5. Current brief.md Missing Frontmatter
**Location:** `/home/haymayndz/SuperTemplate/brief.md`

**Current State:**
```markdown
# Project Brief: AI Delivery Track

## Summary
Establish a dedicated AI/ML delivery lane...
```

**Problem:**
- ❌ No YAML frontmatter
- If used as input, BriefParser will guess stack from keywords
- No explicit stack definition for AI/ML delivery track

**Recommendation:**
Add frontmatter to brief.md:
```yaml
---
name: ai-delivery-track
industry: saas
project_type: fullstack
frontend: nextjs
backend: fastapi
database: postgres
auth: auth0
deploy: aws
compliance: gdpr
features: ml-pipeline,model-monitoring,data-validation
---
# Project Brief: AI Delivery Track
...
```

---

### 🟢 LOW PRIORITY / ENHANCEMENTS

#### 6. Protocol 05 Optional Scaffold Generation
**Location:** `.cursor/ai-driven-workflow/05-bootstrap-your-project.md:291`

**Current:**
```markdown
4. **`[GUIDELINE]` Offer Optional Scaffold Generation:**
   * **Action:** If `brief.md` detected, offer `/Generate Project --brief <path>`
```

**Issue:**
- References `/Generate Project` command (unclear if implemented)
- Ambiguous when this should be used vs Protocol 04 generation

**Recommendation:**
- Clarify this is for legacy projects WITHOUT Protocol 04 scaffold
- Or remove if Protocol 04 is always used

---

#### 7. Protocol 09 Uses scaffold_phase_artifacts.py
**Location:** `.cursor/ai-driven-workflow/09-environment-setup-validation.md`

**Current:**
- Lines 173, 406, 506: `python scripts/scaffold_phase_artifacts.py --phase env`
- File exists: `scripts/scaffold_phase_artifacts.py` ✅

**Status:** ✅ Working as intended

---

## Recommended Changes

### Priority 1: Fix Protocol 04 Broken Reference

**File:** `.cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md`

**Change Line 487:**
```diff
- Script: `python3 scripts/bootstrap_registry_compare.py --manifest .artifacts/protocol-04/bootstrap-manifest.json --registry template-packs/registry.yaml`.
+ Script: `python3 scripts/validate_scaffold.py --manifest .artifacts/protocol-04/bootstrap-manifest.json --output .artifacts/protocol-04/scaffold-validation-report.json`.
```

**Rationale:**
- `validate_scaffold.py` already referenced at line 236
- Removes dependency on non-existent files
- Maintains validation intent

---

### Priority 2: Remove Hardcoded Rules from generate_from_brief.py

**File:** `scripts/generate_from_brief.py`

**Remove Lines 27-84:**
```python
# DELETE THESE:
FRONTEND_RULES = {...}
BACKEND_RULES = {...}
DB_ADDONS = {...}
COMPLIANCE_RULES = {...}
def build_fe_manifest(...): ...
def build_be_manifest(...): ...
```

**Update Lines 185-288:** (FE/BE generation sections)
```diff
- manifest = build_fe_manifest(spec.frontend, comp_list)
- fe_manifest_path = output_root / "_rules_manifests" / f"{fe_name}.json"
- write_rules_manifest(fe_manifest_path, manifest)
- fe_argv.extend(["--rules-manifest", str(fe_manifest_path)])
+ # Let ProjectGenerator auto-select rules based on stack
+ fe_argv.append("--rules-mode")
+ fe_argv.append("auto")
```

**Rationale:**
- ProjectGenerator already has `_resolve_template_rule_source()` at line 640
- UnifiedTemplateRegistry auto-discovers templates
- Single source of truth for rule selection
- Easier maintenance

---

### Priority 3: Add Stack Selection to Protocol 07

**File:** `.cursor/ai-driven-workflow/07-technical-design-architecture.md`

**Insert after STEP 1 (after line ~180):**
```markdown
### STEP 2: Technology Stack Validation & Documentation
<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: Critical architecture decision requiring validation and documentation -->

**Reasoning Pattern:** Validate-then-document — confirm scaffold-generated stack aligns with architectural constraints before detailed design. This prevents rework if stack is incompatible with requirements.

1. **`[MUST]` Review Generated Technology Stack:**
   * **Action:** Read `.artifacts/protocol-04/bootstrap-manifest.json` to extract frontend, backend, database selections
   * **Communication:** 
     > "Reviewing technology stack from scaffold: {frontend}, {backend}, {database}"
   * **Evidence:** `.artifacts/protocol-07/stack-review.json`
   * **Validation:** Stack components match PROJECT-BRIEF.md frontmatter
   * **Halt condition:** Stop if stack incompatible with requirements (e.g., healthcare project with non-HIPAA-compliant DB)

2. **`[MUST]` Create Architecture Decision Record (ADR) for Stack:**
   * **Action:** Document stack selection rationale in `adr-001-technology-stack.md`:
     - Chosen: {frontend}/{backend}/{database}
     - Alternatives Considered: List rejected options
     - Rationale: Why chosen stack best fits requirements
     - Consequences: Known tradeoffs and constraints
   * **Evidence:** `.artifacts/protocol-07/adr-001-technology-stack.md`
   * **Validation:** ADR follows standard format, includes 3+ alternatives

3. **`[GUIDELINE]` Validate Stack Against Constraints:**
   * **Action:** Check stack compatibility with:
     - Compliance requirements (HIPAA, SOX, PCI, GDPR)
     - Performance requirements (scalability, latency)
     - Team expertise (skill gaps)
     - Deployment target (cloud provider compatibility)
   * **Evidence:** `.artifacts/protocol-07/stack-validation-report.json`
   * **Validation:** All constraints satisfied or waivers documented
```

**Renumber existing STEP 2 → STEP 3, etc.**

---

### Priority 4: Add Frontmatter Spec to Protocol 03

**File:** `.cursor/ai-driven-workflow/03-project-brief-creation.md`

**Add to STEP 2 or 3 (Structure Brief section):**
```markdown
### STEP X: Initialize Brief with YAML Frontmatter
<!-- [Category: EXECUTION-BASIC] -->

1. **`[MUST]` Create Brief Header with Metadata:**
   * **Action:** Create `PROJECT-BRIEF.md` starting with YAML frontmatter block
   * **Template:**
     ```yaml
     ---
     name: client-project-name
     industry: healthcare|finance|ecommerce|saas|enterprise
     project_type: web|mobile|api|fullstack|microservices
     frontend: nextjs|nuxt|angular|expo|none
     backend: fastapi|django|nestjs|go|none
     database: postgres|mongodb|firebase|none
     auth: auth0|firebase|cognito|custom|none
     deploy: aws|azure|gcp|vercel|self-hosted
     compliance: hipaa,gdpr,sox,pci  # comma-separated
     features: feature1,feature2  # comma-separated
     ---
     # Project Brief: {name}
     
     ## Summary
     ...
     ```
   * **Communication:** 
     > "Initializing PROJECT-BRIEF.md with technology stack metadata"
   * **Evidence:** `.artifacts/protocol-03/PROJECT-BRIEF.md`
   * **Validation:** Frontmatter parseable by BriefParser

2. **`[MUST]` Select Technology Stack:**
   * **Action:** Based on discovery findings, select:
     - **Industry**: Match business domain
     - **Project Type**: Match delivery format (web/mobile/api)
     - **Frontend**: Match UI requirements
     - **Backend**: Match API/business logic needs
     - **Database**: Match data model requirements
     - **Auth**: Match security/compliance needs
     - **Deploy**: Match infrastructure preferences
     - **Compliance**: List all applicable regulations
   * **Communication:**
     > "Technology selections: frontend={frontend}, backend={backend}, database={database}"
   * **Evidence:** Recorded in frontmatter
   * **Validation:** All required fields populated

3. **`[GUIDELINE]` Validate Stack with Client:**
   * **Action:** Confirm technology choices with client/stakeholders
   * **Evidence:** Client confirmation recorded in discovery notes
   * **Validation:** No objections to technology selections
```

---

### Priority 5: Update Current brief.md

**File:** `/home/haymayndz/SuperTemplate/brief.md`

**Add frontmatter:**
```diff
+ ---
+ name: ai-delivery-track
+ industry: saas
+ project_type: fullstack
+ frontend: nextjs
+ backend: fastapi
+ database: postgres
+ auth: auth0
+ deploy: aws
+ compliance: gdpr
+ features: ml-pipeline,model-monitoring,data-validation,responsible-ai
+ ---
  # Project Brief: AI Delivery Track
  
  ## Summary
  ...
```

---

## Implementation Plan

### Phase 1: Fix Critical Blockers (Day 1)
1. ✅ Update Protocol 04 line 487 (remove broken script reference)
2. ✅ Add frontmatter to current brief.md (enable testing)
3. ✅ Test scaffold generation with updated brief

### Phase 2: Remove Redundant Code (Day 2)
1. ✅ Remove hardcoded rules from generate_from_brief.py
2. ✅ Update generate_from_brief.py to use --rules-mode auto
3. ✅ Test FE/BE generation flow
4. ✅ Verify ProjectGenerator rule selection works

### Phase 3: Protocol Documentation (Day 3)
1. ✅ Add Stack Selection step to Protocol 07
2. ✅ Add Frontmatter spec to Protocol 03
3. ✅ Update Protocol 05 clarification (optional generation)
4. ✅ Review Protocol 09 (no changes needed)

### Phase 4: Validation (Day 4)
1. ✅ Run end-to-end test: P03 → P04 → P07
2. ✅ Verify all quality gates pass
3. ✅ Validate evidence artifacts generated
4. ✅ Test with multiple stack combinations

---

## Testing Checklist

### Test Case 1: Healthcare Web App
```yaml
---
name: health-portal
industry: healthcare
project_type: fullstack
frontend: nextjs
backend: fastapi
database: postgres
auth: auth0
deploy: aws
compliance: hipaa,gdpr
---
```

**Expected:**
- ✅ Scaffold generated with Next.js frontend
- ✅ FastAPI backend templates
- ✅ PostgreSQL database config
- ✅ HIPAA compliance rules included
- ✅ Auth0 integration configured

### Test Case 2: Mobile E-commerce
```yaml
---
name: shop-mobile
industry: ecommerce
project_type: mobile
frontend: expo
backend: nestjs
database: mongodb
auth: firebase
deploy: gcp
compliance: pci,gdpr
---
```

**Expected:**
- ✅ Expo mobile app scaffold
- ✅ NestJS backend with TypeORM
- ✅ MongoDB integration
- ✅ PCI-DSS compliance checks
- ✅ Firebase Auth setup

### Test Case 3: API-Only Service
```yaml
---
name: fintech-api
industry: finance
project_type: api
frontend: none
backend: go
database: postgres
auth: cognito
deploy: aws
compliance: sox,pci
---
```

**Expected:**
- ✅ No frontend scaffold
- ✅ Go backend with net/http
- ✅ PostgreSQL with strict SOX controls
- ✅ AWS Cognito integration
- ✅ Compliance validation scripts

---

## Risk Assessment

### Low Risk Changes ✅
- Protocol documentation updates (P03, P07)
- Adding frontmatter to brief.md
- Updating P04 script reference

**Impact:** Documentation only, no code changes

### Medium Risk Changes ⚠️
- Removing hardcoded rules from generate_from_brief.py
- Changing to --rules-mode auto

**Mitigation:**
- Test with existing projects first
- Verify ProjectGenerator rule selection works
- Keep backup of original file

### High Risk Changes 🔴
- (None identified)

---

## Success Criteria

### Must Have ✅
- [ ] Protocol 04 runs without errors
- [ ] Scaffold generates with correct stack
- [ ] Rules auto-selected match stack
- [ ] All protocols reference existing files only

### Should Have 📋
- [ ] Protocol 03 specifies frontmatter format
- [ ] Protocol 07 validates and documents stack
- [ ] ADR created for stack selection
- [ ] End-to-end flow tested

### Nice to Have 🌟
- [ ] Protocol 05 clarified (legacy vs new)
- [ ] Stack selection guide for users
- [ ] Template contribution guide updated

---

## Next Steps

**Immediate Actions:**
1. Review this analysis with team
2. Approve Priority 1-2 changes
3. Create git branch for changes
4. Implement Phase 1 fixes
5. Test with brief.md

**Follow-up:**
- Document learnings in Protocol 22 (Implementation Retrospective)
- Update Protocol 23 (Script Governance) with new script registry
- Consider creating template-packs contribution guide

---

**End of Report**
