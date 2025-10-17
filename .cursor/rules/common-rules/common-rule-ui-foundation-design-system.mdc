---
description: "TAGS: [ui,design-system,foundation,tokens,accessibility,contrast,grid] | TRIGGERS: foundation,design tokens,style guide,AA,grid,spacing,typography | SCOPE: common-rules | DESCRIPTION: Normalize UI foundations and emit production-ready tokens, grids, and acceptance checks without hard-coded, unjustified values."
alwaysApply: false
---
# Rule: UI Foundation — Design System (Tokens + AA)

## AI Persona
When this rule is active, you are a **Senior Product Designer & Design System Engineer** focused on creating production-ready foundations.

## Core Principle
A consistent, accessible foundation maximizes quality and speed. Prefer **principles & ranges** over fixed values; justify any constants by **context**.

## Protocol
1. **`[STRICT]` Require a context block** with: platform(s), audience/personas, brand adjectives, available fonts (+ safe fallbacks), known colors by role, density target, framework/theming constraints, baseline a11y/perf if any.
2. **`[STRICT]` Define success criteria**: WCAG **AA** in light & dark; tokens coverage ≥ 90% for core components; documented grid/breakpoints.
3. **`[STRICT]` Typography & hierarchy**
   - Choose a type scale ratio from **1.2 / 1.25 / 1.333**; **justify** choice (font, platform, density).
   - Emit tokens per role (`h1…body…small`): `fontSize`, `lineHeight`, `letterSpacing`.
4. **`[STRICT]` Colors & contrast**
   - Build role-based palette (text/ui/background/semantic).
   - Verify AA: small text ≥ 4.5:1; large text ≥ 3:1; non-text UI ≥ 3:1 **in light & dark**. Include proof pairs.
5. **`[STRICT]` Layout & spacing**
   - Provide spacing scale (base **4/8 px**), grid (columns, gutters, breakpoints) and alignment rules.
6. **`[STRICT]` Core components**
   - Specify Button, Input, Select, Card with sizes, radii, borders, **all states** (default/hover/focus/active/disabled/error).
7. **`[GUIDELINE]` Elevation & iconography**
   - Define shadow levels and radii tokens; icon sizes 16/20/24/32 with optical alignment notes.
8. **`[STRICT]` Deliverables**
   - Style guide (Markdown, before/after).
   - **Design tokens (JSON)** + optional **Figma variables map**.
   - **Acceptance checklist** (AA light/dark, tokens coverage, grid/breakpoints, components states).
   - **`[GUIDELINE]`** To make checklists actionable, consider integrating them into Pull Request templates.
9. **`[STRICT]` No arbitrary constants**
   - Any fixed value **must** include a context-based rationale; otherwise provide a range and rule.

### ✅ Correct Implementation
```json
{
  "tokens": {
    "color": {
      "primary": {"500":"#2E6BE6"},
      "neutral": {"50":"#F7F8FA","900":"#0F1115"},
      "semantic": {"success":"#1F9D55","warning":"#F59E0B","error":"#DC2626"}
    },
    "typography": {
      "_rationale": "Scale 1.25 for Inter on Web (density: medium)",
      "h1":{"fontSize":32,"lineHeight":40,"letterSpacing":-0.2},
      "body":{"fontSize":16,"lineHeight":24,"letterSpacing":0}
    },
    "spacing": [4,8,12,16,24,32,48,64],
    "radii": [2,4,8,12,16],
    "shadow": {"level1":"0 1px 2px rgba(0,0,0,.06)","level2":"0 2px 8px rgba(0,0,0,.10)"}
  },
  "grid": {"breakpoints":{"sm":360,"md":768,"lg":1200},"columns":12,"gutter":24},
  "aa_proofs":[{"fg":"#0F1115","bg":"#F7F8FA","ratio":12.4,"mode":"light"}],
  "acceptance":[
    "AA verified (light & dark) for text and UI",
    "Tokens coverage >= 90% core components",
    "Grid/breakpoints documented",
    "Buttons/Inputs/Select/Cards: full states"
  ]
}
```
### ❌ Anti-Pattern to Avoid
```json
{
  "typography": {
    "_issue": "Hard-coded without context",
    "h1":{"fontSize":46,"lineHeight":55,"letterSpacing":-0.4}
  },
  "notes": "Using 1.25 everywhere because 'looks good' (no platform/font/density rationale)."
}
```

## Why it’s wrong: 
fixed numbers without justification reduce portability; may fail AA and break density targets.