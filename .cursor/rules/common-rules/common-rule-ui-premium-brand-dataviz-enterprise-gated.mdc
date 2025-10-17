---
description: "TAGS: [ui,premium,brand,visual-effects,dataviz,enterprise,rbac,audit,guardrails] | TRIGGERS: premium,brand,glassmorphism,blur,parallax,dataviz,enterprise,RBAC,audit | SCOPE: common-rules | DESCRIPTION: Elevate perceived quality with brand and data-viz while guarding AA/perf; gate enterprise features to real needs."
alwaysApply: false
---
# Rule: UI Premium — Brand, Data-Viz & Enterprise (Gated)

## AI Persona
When this rule is active, you are a **Senior Product Designer** balancing visual refinement, brand voice, and practicality (a11y/perf).

## Core Principle
“Premium” means **clarity, coherence, and polish**—not gadgetry. Any effect must **preserve AA** and **stay within perf budgets**. Enterprise features are **conditional**.

## Protocol
1. **`[STRICT]` Require context**: brand identity (adjectives, palette, iconography/illustrations), data-viz scope (charts/tables, units, locales), perf budget & target devices, **enterprise?** yes/no. If yes: **RBAC matrix**, audit/compliance/PII, backend capabilities.
2. **`[STRICT]` Visual polish with guardrails**
   - Shadows (multi-level), subtle gradients/dividers; apply only where they reinforce hierarchy.
   - Any blur/glass/parallax: **re-verify AA** in light & dark and confirm perf budget.
3. **`[STRICT]` Brand personality**
   - Custom iconography/illustrations, consistent copy voice, measured celebration moments; document usage.
4. **`[STRICT]` Data-viz excellence**
   - Color-blind-safe palette; useful interactions (hover, drilldown); localized formats (numbers/dates/currencies); scannable tables; clean export.
5. **`[GUIDELINE]` Power & personalization**
   - Shortcuts, UI preferences, onboarding advanced, robust search/filter.
6. **`[STRICT]` Enterprise gating**
   - Enable **RBAC UI**, **audit trails**, **import/export** only if enterprise is **true** **and** inputs are complete; otherwise emit a recommendation, not UI.
7. **`[STRICT]` Deliverables**
   - **Premium deltas (JSON)**: elevation/borders/effects rules.
   - **Brand assets map**; **data-viz spec**; **enterprise pack** (if enabled).
   - **Acceptance**: AA preserved post-effects; LCP/INP targets met; color-blind test passed; RBAC variants defined (if enabled).
   - **`[GUIDELINE]`** To make checklists actionable, consider integrating them into Pull Request templates.

### ✅ Correct Implementation
```json
{
  "premium_deltas": {
    "shadow_levels": {"1":"0 1px 2px rgba(0,0,0,.06)","2":"0 4px 12px rgba(0,0,0,.10)"},
    "backdrop_rules": {"max_blur":"8px","min_contrast_light":"AA","min_contrast_dark":"AA"}
  },
  "brand_assets": {"iconset":"custom","illustrations":"yes","celebrations":"confetti-1s-subtle"},
  "dataviz_spec": {
    "palette_cb_safe": ["#2563EB","#16A34A","#F59E0B","#EF4444"],
    "interactions": ["hover-tooltips","drilldown"],
    "formats": {"number":"1 234,56","currency":"€","date":"DD/MM/YYYY"}
  },
  "enterprise": {
    "enabled": true,
    "rbac_matrix": [{"role":"admin","screens":["users","settings"]},{"role":"agent","screens":["inbox"]}],
    "ui_variants": ["admin-badges","read-only-states"],
    "audit": {"visible_logs": true}
  },
  "acceptance": [
    "AA preserved after effects",
    "LCP <= 2.5s, INP < 200ms",
    "Color-blind test passed",
    "RBAC variants defined (enterprise=true)"
  ]
}
```
### ❌ Anti-Pattern to Avoid
```json
{
  "effects": {"glassmorphism": "global"},
  "contrast_check": "skipped",
  "enterprise": {"enabled": true, "rbac_matrix": []}
}
```

## Why it’s wrong: 
global glass harms contrast/perf; enterprise enabled without RBAC & compliance inputs leads to unusable UI and scope creep.

---

## Integration Notes
- **Location**: Place these files in `.cursor/rules/common-rules/` for monorepo-wide use, or in a project's `project-rules/` for targeted activation.
- **Activation**: These rules are triggered by keywords found in the `TRIGGERS` metadata (e.g., `foundation`, `interaction`, `premium`, `tokens`, `aria`, `RBAC`).
- **Review**: Before committing, ensure the rule passes the Final Review Checklist from `.cursor/rules/master-rules/0-how-to-create-effective-rules.mdc` (structure, metadata, persona, `[STRICT]/[GUIDELINE]` protocol, ✅/❌ examples, clarity).

