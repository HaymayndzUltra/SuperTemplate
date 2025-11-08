# GUIDELINES FORMAT: RULES & STANDARDS STRUCTURE

**Source**: GUIDELINES-FORMATS.md  
**Use Case**: Master rules, coding standards, protocol guidelines  
**When to Use**: Setting behavioral constraints, compliance requirements, or technical standards

---

## TEMPLATE STRUCTURE

```markdown
---
description: "{TAGS} | {TRIGGERS} | {SCOPE} | DESCRIPTION: {Description}"
alwaysApply: {boolean}
---

# {Protocol_Title}: {Protocol_Name}

## 1. {Section_1_Name}

{Section_1_Description}.

**[STRICT] {Critical_Directive}.**

## 2. {Section_2_Name}

{Section_2_Description}.

## 3. {Section_3_Name}
{Section_3_Description}:
-   `{Marker_1}`: {Marker_1_Description}
-   `{Marker_2}`: {Marker_2_Description}

## 4. {Section_4_Name}

### **[STRICT] {Subsection_4_1_Name}**
{Subsection_4_1_Description}:
1.  *"{Step_1_Placeholder}"*
2.  *"{Step_2_Placeholder}"*
3.  *"{Step_3_Placeholder}"*
4.  *"{Step_4_Placeholder}"*

**[STRICT]** {Follow_Up_Directive}.

### {Subsection_4_2_Name}
- **[STRICT]** {Principle_1}.
- **[STRICT]** {Principle_2}.

### {Subsection_4_3_Name}
**[STRICT]** {Protocol_Description}:
- **{Guideline_1}** - {Guideline_1_Description}
- **{Guideline_2}** - {Guideline_2_Description}

### Step 1: {Step_1_Name}
**[STRICT]** {Step_1_Description}.

1.  **Phase 1: {Phase_1_Name}**
    *   **Action:** {Action}.
    *   **Verification Required:** {Verification}.
    *   **Scope:** {Scope}.

2.  **Phase 2: {Phase_2_Name}**
    *   **Principle:** {Principle}.
    *   **Action:** {Action}.

### Step 2: {Step_2_Name}
**[STRICT]** {Step_2_Description}:
1.  {Element_1}.
2.  {Element_2}.
3.  **[STRICT]** {Element_3}.
4.  **[GUIDELINE]** {Element_4}.

### Step 3: {Step_3_Name}
**[STRICT]** {Step_3_Objective}.

1.  **Priority 1: {Priority_1_Name}**
    *   **[STRICT]** {Priority_1_Rule_1}.
    *   **[STRICT]** {Priority_1_Rule_2}.

2.  **Priority 2: {Priority_2_Name}**
    *   **[STRICT]** {Priority_2_Description}.

### Step 4: {Step_4_Name}
**[STRICT]** {Step_4_Primary_Directive}.

### Step 5: {Step_5_Name}
**[STRICT]** {Step_5_Description}:

1. **{Checkpoint_1_Name}:**
   - **[STRICT]** {Checkpoint_1_Condition} → {Checkpoint_1_Action}.

2. **{Checkpoint_2_Name}:**
   - **[STRICT]** {Checkpoint_2_Condition} → {Checkpoint_2_Action}.

#### ✅ {Correct_Format_Section}

> **Example 1:** *"{Example_1_Header}"*
> **Example 2:** *"{Example_2_Header}"*

#### ❌ {Incorrect_Format_Section}

> **Example 1:** *"{Bad_Example_1_Header}"*
> **Example 2:** *"{Bad_Example_2_Header}"*
```

---

## KEY FEATURES

### YAML Frontmatter
```yaml
---
description: "TAGS: [tags] | TRIGGERS: [triggers] | SCOPE: [scope] | DESCRIPTION: [description]"
alwaysApply: true/false
---
```

### Directive Markers
- **`[STRICT]`**: Non-negotiable requirements
- **`[GUIDELINE]`**: Strong recommendations
- **`[CRITICAL]`**: Security or compliance critical items

### Step-Based Structure
- **5 Steps Maximum**: Keep guidelines focused
- **Phase Sub-sections**: Break complex steps into phases
- **Priority Levels**: Clear hierarchy of requirements

### Example Format
```markdown
#### ✅ Correct Format
> **Example 1:** *"{Good example}"*

#### ❌ Incorrect Format  
> **Example 1:** *"{Bad example}"*
```

---

## USAGE EXAMPLE

### UI Design System Guidelines (GUIDELINES FORMAT)

```markdown
---
description: "TAGS: [ui, design-system, foundation, tokens, accessibility, contrast, grid] | TRIGGERS: [foundation, design tokens, style guide, AA, grid, spacing, typography] | SCOPE: [common-rules] | DESCRIPTION: Normalize UI foundations and emit production-ready tokens, grids, and acceptance checks without hard-coded, unjustified values."
alwaysApply: true
---

# UI Foundation Design System

## 1. Design Token Architecture

Design tokens must follow a systematic hierarchy that enables semantic theming and platform scalability while maintaining designer-developer handoff clarity.

**[STRICT] All design tokens must be derived from core primitive values, never hard-coded.**

## 2. Color System Requirements

Color palettes must ensure WCAG AA compliance and support multiple semantic themes (light, dark, high contrast).

## 3. Typography Standards
Typography standards must ensure readability across all device sizes and support international character sets:
-   `font-family-primary`: System font stack for body text
-   `font-family-secondary`: System font stack for headings
-   `font-scale`: Modular scale with 1.25 ratio for headings

## 4. Spacing and Layout System

### **[STRICT] Spacing Token Generation**
Spacing tokens must follow mathematical progression for visual harmony:
1.  *"Generate base spacing unit from 4px grid system"*
2.  *"Create scale using 8px base unit (4, 8, 12, 16, 24, 32, 48, 64)"*
3.  *"Apply semantic naming (xs, sm, md, lg, xl, 2xl)"*
4.  *"Validate all spacing combinations maintain visual rhythm"*

**[STRICT]** Document spacing rationale and mathematical relationships in design system documentation.

### Grid System Requirements
- **[STRICT]** Use CSS Grid for main layout structures.
- **[STRICT]** Use Flexbox for component-level alignment.
- **[STRICT]** Maintain 12-column grid system with responsive breakpoints.

### Component Spacing Rules
**[STRICT]** Component spacing must follow token-based system:
- **{guideline-margin}** - Use margin tokens for component-to-component spacing
- **{guideline-padding}** - Use padding tokens for internal component spacing
- **{guideline-consistency}** - Apply consistent spacing patterns across similar components

### Step 1: Token Generation Process
**[STRICT]** Generate all design tokens from primitive values before any component development:

1.  **Phase 1: Primitive Definition**
    *   **Action:** Define base values for colors, typography, spacing.
    *   **Verification Required:** All values have mathematical relationships.
    *   **Scope:** Core design system tokens only.

2.  **Phase 2: Semantic Derivation**
    *   **Principle:** Semantic tokens derive from primitives with clear intent.
    *   **Action:** Create semantic tokens (color-primary, text-body, etc.).

### Step 2: Accessibility Validation
**[STRICT]** Validate all color combinations meet WCAG AA requirements:
1.  Test all text color combinations against background colors.
2.  Verify interactive elements meet 4.5:1 contrast ratio minimum.
3.  **[STRICT]** Document any exceptions with accessibility board approval.
4.  **[GUIDELINE]** Target AAA compliance for critical user interface elements.

### Step 3: Component Integration
**[STRICT]** Ensure all components reference design tokens, never hard-coded values:

1.  **Priority 1: Critical Components**
    *   **[STRICT]** Buttons, forms, navigation must use token system.
    *   **[STRICT]** All interactive states (hover, focus, active) tokenized.

2.  **Priority 2: Supporting Components**
    *   **[STRICT]** Cards, modals, tooltips follow token patterns.
    *   **[GUIDELINE]** Decorative elements may use direct values with documentation.

### Step 4: Quality Assurance
**[STRICT]** Implement automated token validation in build pipeline.

### Step 5: Documentation Requirements
**[STRICT]** Document all design decisions with rationale:

1. **Token Documentation:**
   - **[STRICT]** Each token includes usage guidelines and examples.
   - **[STRICT]** Mathematical relationships clearly explained.

2. **Component Documentation:**
   - **[STRICT]** Component examples show token usage patterns.
   - **[STRICT]** Responsive behavior documented with breakpoints.

#### ✅ Correct Token Usage

> **Example 1:** *"Use `color-primary-500` for primary actions, never `#3B82F6` directly"*
> **Example 2:** *"Apply `spacing-md-16` for component margins, maintain consistent rhythm"*

#### ❌ Incorrect Token Usage

> **Example 1:** *"Hard-code hex colors in component styles"*
> **Example 2:** *"Use arbitrary spacing values without token reference"*
```

---

## WHEN TO USE THIS FORMAT

### ✅ Perfect For:
- **Design Systems**: UI/UX standards and component guidelines
- **Coding Standards**: Development best practices and conventions
- **Security Policies**: Compliance requirements and security controls
- **Process Standards**: Workflow requirements and quality gates
- **API Standards**: Interface specifications and data contracts

### ❌ Avoid For:
- **Execution Workflows**: Use EXECUTION formats instead
- **Creative Tasks**: Too rigid for exploratory work
- **Simple Checklists**: Overkill for basic task lists
- **User Guides**: Too technical for end-user documentation

---

## CUSTOMIZATION GUIDELINES

### Section Organization
- **5 Sections Maximum**: Keep guidelines focused and digestible
- **Logical Flow**: Start with principles, end with examples
- **Clear Hierarchy**: Use numbered sections and subsections

### Directive Usage
- **`[STRICT]`**: For non-negotiable requirements (security, compliance)
- **`[GUIDELINE]`**: For strong recommendations with flexibility
- **`[CRITICAL]`**: For items that could cause system failure

### Example Quality
- **Real Examples**: Use actual code/values from your system
- **Before/After**: Show transformation when applicable
- **Rationale**: Explain why correct example is better

---

## BENEFITS

### Standardization
- **Consistent Application**: Clear rules prevent interpretation drift
- **Quality Assurance**: Examples provide reference implementation
- **Team Alignment**: Everyone follows same standards

### Compliance
- **Audit Ready**: Clear documentation of requirements
- **Regulatory Alignment**: Strict directives for compliance items
- **Risk Mitigation**: Critical requirements clearly marked

### Maintainability
- **Version Control**: Changes tracked and communicated
- **Update Process**: Clear modification procedures
- **Knowledge Transfer**: New team members can quickly learn standards

---

*This GUIDELINES format provides comprehensive rule documentation for standards that require strict compliance and clear implementation guidance.*
