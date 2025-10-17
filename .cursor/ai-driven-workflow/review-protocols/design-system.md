# PROTOCOL: Generic Design System Review (DDD Compliant)

**IMPORTANT**: This protocol is now a specialized pointer to the comprehensive quality audit.

**Primary Protocol**: `.cursor/ai-driven-workflow/4-quality-audit.md`

**Execution Mode**: Mode 6 (Design System Review)
- **Layers**: LAYER 1 (DDD Compliance) + LAYER 6 (Design System)
- **Duration**: 8-15 minutes
- **Usage**: Design system compliance validation

## Design Focus
Please read and apply the comprehensive protocol with **Mode 6: Design System Review** settings:
- Visual consistency validation
- Design system compliance
- Component usage patterns verification
- Brand guidelines adherence

## Design Review Framework (Standard Compliance)

### 1. Design System Compliance (Critical - Design Standard)
**[STRICT] Component Usage Validation:**
- Use of design system components only
- Respect for defined variants and states
- Compliance with spacing/typography guidelines
- Validation of colors according to the defined palette

**[STRICT] Visual Consistency:**
- Visual consistency between modules/services
- Respect for the established visual hierarchy
- Alignment with existing UI patterns
- Validation of responsive breakpoints

### 2. Brand Guidelines Adherence (High Priority - Brand)
**[STRICT] Brand Compliance:**
- Respect for the visual identity (logos, colors, typography)
- Correct application of brand guidelines
- Consistency of tone of voice in the UI
- Compliance with established visual standards

### 3. Component Architecture (Critical - DDD)
**[STRICT] Component Boundaries:**
- Reusable components in `/libs/ui` or equivalent
- No duplication of UI components between services
- Respect for design system abstractions
- Clear separation of presentation/business logic
- **[PRAGMATISM]** `🧠`: Create reusable components, but avoid premature abstractions. A duplicated component is sometimes better than a bad abstraction.

### 4. Design Token Usage (High Priority - Consistency)
**[STRICT] Token Compliance:**
- Use of design tokens (colors, spacing, typography)
- Avoid hardcoded values in CSS
- Respect for token nomenclature
- Consistency of values between components

## Design Review Process

### 1. Design System Audit
- Identify used components vs design system
- Analyze compliance of used variants
- Check application of design tokens
- Control visual consistency

### 2. Brand Compliance Check
- Scan uses of colors/typography
- Check application of visual guidelines
- Control alignment with brand identity
- Validate consistency of visual language

### 3. Component Architecture Review
- Check reusability of components
- Control separation of UI/business concerns
- Analyze organization of components
- Validate the design system architecture

## Design Communication Style

**Standard Compliant Classification:**
- 🚨 **[CRITICAL/BLOCKER]**: 
  - Design system violation (custom component vs system)
  - Non-compliance with brand guidelines
  - Duplication of UI components between services
  - Design tokens ignored (hardcoded values)

- ⚠️ **[IMPROVEMENT]**: 
  - Minor visual inconsistencies
  - Possible UX optimizations
  - Non-optimal but functional components
  - Missing design documentation

- 💡 **[SUGGESTION]**: 
  - Aesthetic improvements
  - Micro-interaction optimizations
  - Suggestions for design system evolution

- 🧠 **[PRAGMATISM]**:
  - Is the component too complex? Could it be simplified while still respecting the design system requirements?

## Design Report Format

```markdown
# 🎨 Generic Design System Review

## Executive Summary
- **Design System Score**: X/10
- **Brand Compliance**: ✅/⚠️/🚨 Status
- **Component Usage**: ✅/⚠️/🚨 Conformity  
- **Visual Consistency**: ✅/⚠️/🚨 Standards adherence

## Critical Violations (Design Standards)

### 🚨 [File:Line] Title of the violation
- **Rule Violated**: Design System / Brand Guidelines reference
- **Issue**: Precise description of the design/brand violation
- **Impact**: Consequences on consistency/user experience
- **Fix**: Specific code/design with examples ✅ CORRECT and ❌ INCORRECT

## Design System Compliance
- Component Usage: ✅/⚠️/🚨
- Design Token Usage: ✅/⚠️/🚨
- Brand Guidelines: ✅/⚠️/🚨
- Visual Consistency: ✅/⚠️/🚨

## Priority Recommendations
1. [CRITICAL] Immediate actions for design system compliance
2. [HIGH] Improvements to brand guidelines
3. [MEDIUM] UI component optimizations
4. [LOW] Aesthetic/UX suggestions
```

**Design Focus**: Maintain the **consistency of the design system**, respect **brand guidelines**, and ensure the **reusability of UI components**.

## Tool Integration Notes

### Universal Design Tools
- Use browser tools for screenshots and visual validation
- Leverage design system documentation
- Access to style guides and brand guidelines
- Validation of design tokens usage

### Generic Tools  
- Analyze component structure with search patterns
- Read CSS/styling files with file readers
- Validate with repository scanning design files