# Architecture Decision: Project-Specific Protocol Generation System

**Date**: 2025-01-10  
**Decision ID**: AD-001  
**Status**: ✅ Accepted  
**Framework Version**: 1.0

---

## 📋 CONTEXT

### Problem Statement
The current protocol system (`.cursor/ai-driven-workflow/`) contains 28+ generic protocols that work for any project. However, each project has unique requirements (tech stack, scope, domain) that require customized protocols. The question is: **How should we organize and generate project-specific protocols?**

### Current State
- **Foundation**: 28 protocols in `.cursor/ai-driven-workflow/` (generic templates)
- **Protocol 05b**: Analyzes PROJECT-BRIEF.md and sequences protocols
- **Gap**: No mechanism to generate customized, project-specific protocol instances
- **Pain Point**: Manual customization of protocols per project is time-consuming and error-prone

### Options Considered
1. **Option A**: Keep all protocols in `.cursor/ai-driven-workflow/`, use conditionals
2. **Option B**: Generate project-specific protocols in `{project}/.cursor/project-protocols/`
3. **Option C (Hybrid)**: Foundation templates in `.cursor/ai-driven-workflow/` + Generated instances in `{project}/.cursor/project-protocols/`

---

## 🧮 EVALUATION

### Criterion 1: Project Isolation Requirements
- **Score**: 5/5 (Critical)
- **Rationale**: 
  - Multi-project workspace expected (freelance developer handling multiple clients)
  - Each project has different tech stack (Next.js vs Django vs Go)
  - Project-specific customizations essential (e-commerce vs SaaS vs AI/ML)
  - High risk of cross-project contamination if protocols shared
- **Evidence**:
  - Current workspace has `SAMPLE-AI-PROJECT/` demonstrating multi-project structure
  - Template-packs support 15+ tech stack combinations
  - Protocol 03 (Project Brief) captures project-specific requirements
  - Protocol 05b already sequences protocols per project needs

**Conclusion**: Critical isolation needed → Score 5/5

---

### Criterion 2: Maintenance Overhead Acceptable
- **Score**: 4/5 (High)
- **Rationale**:
  - Solo developer with deep technical expertise
  - Time available for maintenance (not a large team with limited bandwidth)
  - Protocol updates infrequent (stable foundation)
  - Automation available (11-validator system, script registry)
- **Evidence**:
  - Existing validator system can validate generated protocols
  - Script registry (`scripts/script-registry.json`) shows automation maturity
  - Protocol 05b already has complex analysis logic (can be extended)
  - `.artifacts/` system shows evidence tracking capability

**Conclusion**: High maintenance acceptable with automation → Score 4/5

---

### Criterion 3: Template Reuse Needed
- **Score**: 5/5 (Critical)
- **Rationale**:
  - Expect 10+ projects per year (freelance pipeline)
  - Protocols are stable (28 protocols already defined)
  - High customization needs per project (different domains)
  - Frequent updates to foundation templates (continuous improvement)
- **Evidence**:
  - 28 protocols already exist as foundation
  - Protocol 01-05 are project-agnostic (reusable)
  - Protocol 06-28 need project-specific customization
  - DRY principle essential for maintainability

**Conclusion**: Critical template reuse needed → Score 5/5

---

### Criterion 4: Integration Complexity
- **Score**: 4/5 (Complex)
- **Rationale**:
  - Must integrate with existing Protocol 05b (complex analysis logic)
  - Must integrate with 11-validator system
  - Must integrate with script registry and automation hooks
  - Backward compatibility required (existing workflows must not break)
- **Evidence**:
  - Protocol 05b has 6 phases already (adding Phase 7 for generation)
  - Validator system in `validators-system/` with 20+ validators
  - Script registry has 250+ scripts to integrate with
  - `.cursor/ai-driven-workflow/` has 43 existing protocols

**Conclusion**: Complex integration required → Score 4/5

---

### Criterion 5: Scalability Requirements
- **Score**: 4/5 (High)
- **Rationale**:
  - Expect 20-30 projects per year (freelance scale)
  - Growth rate moderate (1-2 new projects per month)
  - Resource constraints moderate (solo developer)
  - Performance requirements moderate (generation should be fast)
- **Evidence**:
  - Current workspace shows multi-project capability
  - Template-packs support multiple project types
  - Protocol system designed for reuse
  - Automation reduces resource constraints

**Conclusion**: High scalability needed → Score 4/5

---

### Criterion 6: Customization Flexibility
- **Score**: 5/5 (Extreme)
- **Rationale**:
  - High variety of project types (e-commerce, SaaS, AI/ML, dashboards)
  - Client-specific requirements always unique
  - Tech stack diversity extreme (15+ combinations in template-packs)
  - Domain complexity varies widely
- **Evidence**:
  - Template-packs show 15+ tech stack combinations
  - Protocol 03 captures unique project requirements
  - Protocol 05b already classifies projects (Simple/Standard/Complex/Enterprise)
  - AI-project-workflow shows domain-specific protocols

**Conclusion**: Extreme customization needed → Score 5/5

---

## 📊 TOTAL SCORE

```
Total Score = (5 + 4 + 5 + 4 + 4 + 5) / 6 = 4.5/5.0
```

**Recommendation**: **Hybrid Architecture** (Foundation templates + Project-specific instances)

---

## ✅ DECISION

### Chosen Architecture: Hybrid (Option C)

**Structure**:
```
Foundation Templates (Read-Only):
  .cursor/ai-driven-workflow/
    ├── 01-client-proposal-generation.md (template)
    ├── 02-client-discovery-initiation.md (template)
    └── ... (all 28 protocols as templates)
    ↓
Protocol 05b Enhanced (Generator):
  - Analyzes PROJECT-BRIEF.md
  - Selects needed protocols
  - Transforms templates → project-specific
  - Generates customized instances
    ↓
Project-Specific Instances (Generated):
  {project-root}/.cursor/project-protocols/
    ├── 06-create-prd.md (customized)
    ├── 07-technical-design-architecture.md (customized)
    └── ... (only needed protocols)
```

**Key Principles**:
1. **Single Source of Truth**: Foundation templates in `.cursor/ai-driven-workflow/`
2. **Project Isolation**: Each project gets `.cursor/project-protocols/` directory
3. **No Duplication**: Templates stay in foundation, instances generated per project
4. **Backward Compatible**: Existing Protocol 05b workflow preserved

---

## 🎯 CONSEQUENCES

### Positive
✅ **Complete Project Isolation**: Each project has own protocol instances, no cross-contamination  
✅ **Template Reuse**: Foundation templates remain single source of truth (DRY)  
✅ **Extreme Customization**: Each project gets fully customized protocols  
✅ **Scalability**: Can handle 20-30+ projects without protocol conflicts  
✅ **Maintainability**: Update foundation templates, regenerate project instances  
✅ **Backward Compatible**: Existing workflows continue to work  
✅ **Validation**: Generated protocols pass through 11-validator system  

### Negative
⚠️ **Maintenance Overhead**: Must maintain transformation engine and generation logic  
⚠️ **Complexity**: More complex than simple shared protocols  
⚠️ **Storage**: More files (templates + instances per project)  
⚠️ **Versioning**: Must track template versions and instance versions  
⚠️ **Migration**: Existing projects need migration to new structure  

### Trade-offs Accepted
- **Complexity for Flexibility**: Accept higher complexity to gain extreme customization
- **Storage for Isolation**: Accept more files to gain complete project isolation
- **Maintenance for Scalability**: Accept maintenance overhead to gain scalability
- **Initial Effort for Long-term Gain**: Accept upfront implementation effort for long-term efficiency

---

## 🔄 ALTERNATIVES CONSIDERED

### Alternative 1: Option A (Shared Protocols with Conditionals)
**Structure**: Keep all protocols in `.cursor/ai-driven-workflow/`, use conditionals like `{#if tech_stack == "nextjs"}...{/if}`

**Why Not Chosen**:
- ❌ **Low Isolation**: All projects share same files, high contamination risk
- ❌ **Low Scalability**: Conditionals become unmaintainable with 20+ projects
- ❌ **Low Customization**: Limited to conditional sections, not full customization
- ❌ **High Complexity**: Protocol files become bloated with conditionals
- **Score**: Would score 2.5/5.0 (Shared Protocols with Variants)

---

### Alternative 2: Option B (Pure Project-Specific Generation)
**Structure**: Generate all protocols (including 01-05) in `{project}/.cursor/project-protocols/`, no foundation templates

**Why Not Chosen**:
- ❌ **No Template Reuse**: Duplicates all protocols per project (violates DRY)
- ❌ **High Maintenance**: Must update every project when protocols change
- ❌ **High Storage**: Stores 28 protocols × N projects (wasteful)
- ✅ **High Isolation**: Complete isolation (good)
- ✅ **High Customization**: Full customization (good)
- **Score**: Would score 3.8/5.0 (Template-Based Generation)
- **Why Hybrid Better**: Hybrid gets same isolation/customization with better template reuse

---

## 🛠️ IMPLEMENTATION NOTES

### Phase 1: Decision Framework (Current)
- ✅ Framework created (`DECISION-FRAMEWORK.md`)
- ✅ Decision documented (this file)
- ⏳ Review process established

### Phase 2: Protocol 05b Enhancement
- Extend Protocol 05b with Phase 7: Protocol Generation
- Create transformation engine (template → instance)
- Define storage structure (`{project}/.cursor/project-protocols/`)

### Phase 3: Generation Engine
- Design template parameterization format
- Create transformation rules (PROJECT-BRIEF → customizations)
- Implement generation pipeline

### Phase 4: Validation System
- Integrate with 11-validator system
- Create quality gates (≥0.95 compliance)
- Build remediation workflows

### Key Risks
1. **Template Updates Breaking Instances**: Mitigate with versioning strategy
2. **Transformation Logic Complexity**: Mitigate with incremental implementation
3. **Validation Overhead**: Mitigate with async validation, caching

---

## 📅 REVIEW SCHEDULE

### Next Review
**Date**: 2025-04-10 (3 months)

### Review Triggers (Re-evaluate if any occur)
- Protocol system scales beyond 30 projects
- Maintenance overhead becomes unsustainable
- Team size changes (solo → team)
- New architectural patterns emerge
- Framework score changes by ≥1.0 points

### Success Metrics (Measure at review)
- **Generation Time**: <30 seconds per project
- **Validator Compliance**: ≥95% of generated protocols pass
- **Customization Coverage**: ≥90% of project needs met
- **Developer Satisfaction**: ≥4/5 rating

---

## 📊 DECISION SUMMARY

| Aspect | Score | Status |
|--------|-------|--------|
| Project Isolation | 5/5 | ✅ Critical need met |
| Maintenance Overhead | 4/5 | ✅ Acceptable with automation |
| Template Reuse | 5/5 | ✅ Critical need met |
| Integration Complexity | 4/5 | ✅ Complex but manageable |
| Scalability | 4/5 | ✅ High scalability achieved |
| Customization Flexibility | 5/5 | ✅ Extreme flexibility achieved |
| **Overall** | **4.5/5.0** | ✅ **Hybrid Architecture Recommended** |

---

**Decision Status**: ✅ Accepted  
**Implementation Status**: 🚧 Phase 1 Complete, Phase 2-4 Pending  
**Next Action**: Start Phase 2 - Protocol 05b Enhancement

---

**Approved By**: System Architect  
**Date**: 2025-01-10  
**Signature**: [Digital signature placeholder]
