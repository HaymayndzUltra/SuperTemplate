# PROTOCOL: Generic UI/UX Accessibility Review (DDD Compliant)

**IMPORTANT**: This protocol is now a specialized pointer to the comprehensive quality audit.

**Primary Protocol**: `.ai-governor/dev-workflow/4-quality-audit.md`

**Execution Mode**: Mode 7 (UI/UX Accessibility Review)
- **Layers**: LAYER 1 (DDD Compliance) + LAYER 7 (UI/UX & Accessibility)
- **Duration**: 10-20 minutes
- **Usage**: UI/UX and accessibility validation

## UI/UX Focus
Please read and apply the comprehensive protocol with **Mode 7: UI/UX Accessibility** settings:
- WCAG AA+ accessibility compliance
- Responsive design validation
- User experience patterns verification
- Interaction flow consistency

## UI/UX Review Framework (Standard Compliant)

### 1. Accessibility Compliance (Critical - WCAG Standards)
**[STRICT] WCAG AA+ Validation:**
- Color contrast minimum 4.5:1 (normal) / 3:1 (large)
- Full keyboard navigation for all interactive elements
- Appropriate ARIA attributes for screen readers
- Correct semantic HTML structure (headings, landmarks)
- Explicit labels for all inputs/controls

**[STRICT] Inclusive Design:**
- Support for users with motor/visual/auditory/cognitive disabilities
- Text alternatives for non-text content
- No reliance on color alone for information
- Accessible or disable-able timeouts
- Prevention of seizures (animations, flashing)

### 2. Responsive Design (Critical - Multi-Device)
**[STRICT] Breakpoint Validation:**
- Full functionality on mobile/tablet/desktop
- No unintentional horizontal scrolling
- Touch targets minimum 44px for mobile
- Navigation adapted to each viewport
- Performance maintained on all devices

**[STRICT] Content Prioritization:**
- Clear information hierarchy on small screens
- Appropriate progressive disclosure
- Critical content accessible without scrolling
- Interactions optimized by device type

### 3. User Experience Patterns (High Priority - UX Standards)
**[STRICT] Interaction Consistency:**
- Consistent interaction patterns throughout the app
- Visual feedback for all user actions
- Clearly indicated loading/error/success states
- Intuitive and predictable navigation
- Appropriate visual affordances

**[STRICT] Cognitive Load Management:**
- Appropriate information chunks (7±2 rule)
- Progressive disclosure for complex workflows
- Clear labels and instructions
- Prevention and recovery from errors
- Confirmation for destructive actions
- **[PRAGMATISM]** `🧠`: Aim for simplicity. A clear and simple interface is often more accessible than a complex one with ARIA aids.

### 4. Performance UX (High Priority - Core Web Vitals)
**[STRICT] Loading Experience:**
- Largest Contentful Paint <2.5s
- First Input Delay <100ms
- Cumulative Layout Shift <0.1
- Progressive loading with skeletons/placeholders
- Image and asset optimizations

### 5. Multi-Tenant UX (SaaS - Context Specific)
**[STRICT] Tenant Isolation UX:**
- Clear tenant context in the interface
- No data confusion between tenants
- Onboarding adapted by tenant type
- Permissions/roles reflected in the UI
- Appropriate tenant branding (if applicable)

## UI/UX Review Process

### 1. Accessibility Audit
- Scan HTML markup for semantic compliance
- Test full keyboard navigation
- Automatically check color contrasts
- Validate ARIA attributes and labels
- Simulate screen readers and assistive technologies

### 2. Responsive Testing
- Test on standard breakpoints (320px, 768px, 1024px, 1200px+)
- Validate touch interactions on mobile
- Check portrait/landscape orientation
- Control performance on low-end devices
- Test with different font sizes

### 3. UX Flow Validation
- Trace critical user journeys
- Identify friction points and confusion
- Validate user feedback at each step
- Control error states and recovery
- Test edge cases and error scenarios

### 4. Performance UX Analysis
- Measure Core Web Vitals
- Analyze loading sequences
- Identify layout shifts
- Optimize critical rendering path
- Validate perceived performance

## UI/UX Communication Style

**Standard Compliant Classification:**
- 🚨 **[CRITICAL/BLOCKER]**: 
  - WCAG AA violation (contrast, keyboard navigation, ARIA)
  - Broken functionality on mobile/tablet
  - Major inaccessibility (users excluded)
  - Core Web Vitals out of bounds

- ⚠️ **[IMPROVEMENT]**: 
  - WCAG AAA opportunities
  - Identified UX friction
  - Sub-optimal performance
  - Improvable responsive design

- 💡 **[SUGGESTION]**: 
  - Improved micro-interactions
  - Subtle UX optimizations
  - Enhanced accessibility
  - Performance fine-tuning

- 🧠 **[PRAGMATISM]**:
  - Is the accessibility solution too complex? Is there a simpler way to achieve the same level of compliance?

## UI/UX Report Format

```markdown
# ♿ Generic UI/UX Accessibility Review

## Executive Summary
- **Accessibility Score**: X/10 (WCAG AA compliance)
- **Responsive Design**: ✅/⚠️/🚨 Multi-device support
- **UX Patterns**: ✅/⚠️/🚨 User experience quality  
- **Performance UX**: ✅/⚠️/🚨 Core Web Vitals status

## Critical Violations (Accessibility Standards)

### 🚨 [File:Line] Title of the violation
- **Standard Violated**: WCAG AA / UX Best Practice reference
- **Issue**: Precise description of the accessibility/UX violation
- **Impact**: Affected users and consequences
- **Fix**: Specific code/design with examples ✅ CORRECT and ❌ INCORRECT

## Accessibility Metrics
- WCAG AA Compliance: XX% (target: 100%)
- Keyboard Navigation: ✅/⚠️/🚨
- Screen Reader Support: ✅/⚠️/🚨
- Color Contrast Ratio: X.X:1 (minimum: 4.5:1)

## Performance UX Metrics
- Largest Contentful Paint: X.Xs (target: <2.5s)
- First Input Delay: XXms (target: <100ms)
- Cumulative Layout Shift: X.XX (target: <0.1)

## Priority Recommendations
1. [CRITICAL] Immediate WCAG AA compliance
2. [HIGH] Responsive design optimizations
3. [MEDIUM] UX patterns improvements
4. [LOW] Performance and micro-interactions
```

**UI/UX Focus**: Ensure **universal accessibility**, optimize the **multi-device experience**, and maintain **consistent UX patterns**.

## Tool Integration Notes

### Universal UI Tools
- Use browser automation for accessibility testing
- Leverage responsive design testing tools
- Access to accessibility validators and contrast checkers
- Performance monitoring for Core Web Vitals

### Generic Tools  
- Analyze HTML markup with search patterns
- Read CSS/styling files with file readers
- Validate with automated accessibility scanners
- Test with keyboard navigation simulation