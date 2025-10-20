# AGENTS.md Migration Guide

**Date**: 2025-10-20  
**Purpose**: Migrate `.cursor/rules/AGENTS.md` to PLAN-MODE compliant `.mdc` format  
**Status**: Ready for Implementation

---

## Migration Overview

### Current State
- **File**: `.cursor/rules/AGENTS.md`
- **Format**: Standard Markdown (`.md`)
- **Status**: ⚠️ Not discoverable by Cursor's rule system
- **Content**: Comprehensive external agent interpretation guide

### Target State
- **File**: `.cursor/rules/master-rules/8-master-rule-external-agent-interpretation.mdc`
- **Format**: Markdown with Cursor (`.mdc`)
- **Status**: ✅ Fully compliant with PLAN-MODE framework
- **Content**: Restructured following 4 Pillars methodology

---

## Migration Steps

### Step 1: Review Generated File
The new `.mdc` file has been created at:
```
/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/meta-analysis/session-current/8-master-rule-external-agent-interpretation.mdc
```

**Review checklist:**
- [ ] YAML frontmatter is properly formatted
- [ ] All 4 Pillars are present (Structure, Personality, Precision, Exemplarity)
- [ ] `[STRICT]` and `[GUIDELINE]` prefixes are used appropriately
- [ ] Examples include both ✅ Correct and ❌ Anti-Pattern sections
- [ ] Content is comprehensive and accurate

### Step 2: Move File to Correct Location
Once reviewed and approved, move the file:

```bash
# From current location
mv /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/meta-analysis/session-current/8-master-rule-external-agent-interpretation.mdc \
   /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/rules/master-rules/8-master-rule-external-agent-interpretation.mdc
```

### Step 3: Archive or Remove Legacy File
Choose one of these options:

**Option A: Archive (Recommended)**
```bash
# Create archive directory if it doesn't exist
mkdir -p /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/rules/archive

# Move legacy file to archive
mv /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/rules/AGENTS.md \
   /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/rules/archive/AGENTS.md.legacy
```

**Option B: Delete**
```bash
# Remove legacy file
rm /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/rules/AGENTS.md
```

### Step 4: Update References
Search for any references to `AGENTS.md` in the codebase:

```bash
# Search for references
grep -r "AGENTS.md" /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING --exclude-dir=node_modules --exclude-dir=.git

# Update references to point to new file
# Replace: .cursor/rules/AGENTS.md
# With: .cursor/rules/master-rules/8-master-rule-external-agent-interpretation.mdc
```

### Step 5: Verify Integration
Test that the new rule is discoverable:

```bash
# List all .mdc files to confirm new file is present
find .cursor/rules/ -name "*.mdc" -type f | sort

# Verify the file is in master-rules directory
ls -la .cursor/rules/master-rules/8-master-rule-external-agent-interpretation.mdc
```

---

## Changes Made During Migration

### 1. Structure & Discoverability (Pillar 1)

#### Added YAML Frontmatter
```yaml
---
description: "TAGS: [global,external-agents,cross-platform,rule-interpretation,compatibility] | TRIGGERS: external agent,claude,chatgpt,gemini,cross-platform,rule loading,mdc format | SCOPE: global | DESCRIPTION: Comprehensive guide for external cloud LLMs to interpret and apply the .mdc rule system, ensuring consistent AI behavior across different platforms."
alwaysApply: false
---
```

**Rationale:**
- Makes rule discoverable by Cursor's rule system
- Provides clear triggers for automatic activation
- Defines scope and tags for context matching

#### Changed File Extension
- **From**: `.md` (not recognized by Cursor)
- **To**: `.mdc` (Cursor-compatible)

#### Moved to Correct Directory
- **From**: `.cursor/rules/` (root level)
- **To**: `.cursor/rules/master-rules/` (proper classification)

#### Added Numbered Prefix
- **From**: `AGENTS.md`
- **To**: `8-master-rule-external-agent-interpretation.mdc`
- **Rationale**: Follows master rule naming convention, number 8 indicates position in sequence

### 2. Personality & Intent (Pillar 2)

#### Added AI Persona Section
```markdown
## 1. AI Persona
When this rule is active, you are a **Cross-Platform AI Integration Specialist**...
```

#### Added Core Principle Section
```markdown
## 2. Core Principle
Consistent AI behavior across platforms depends on a standardized rule interpretation protocol...
```

**Rationale:**
- Defines how AI should think when applying this rule
- Explains the "why" behind the rule's existence
- Sets the cognitive framework for rule execution

### 3. Precision & Clarity (Pillar 3)

#### Added Directive Prefixes
All instructions now use explicit prefixes:
- `[STRICT]` for mandatory actions
- `[GUIDELINE]` for recommended actions

**Examples:**
```markdown
### **[STRICT] Mandatory First Steps**
Before any other action, external AI agents **MUST** execute this initialization sequence:

1. **`[STRICT]` Scan for Rules Directory:**
   - Search for `.cursor/rules/` directory in workspace root
   
### **[GUIDELINE] Evidence Collection**
For each rule application, collect:
```

#### Restructured Content
- Organized into numbered sections following 4 Pillars pattern
- Clear protocol steps with imperative language
- Unambiguous action items

### 4. Exemplarity & Contrast (Pillar 4)

#### Added ✅ Correct Implementation Section
```markdown
## ✅ Correct Implementation

### Example: Rule Loading Sequence
```python
# Pseudo-code demonstrating correct rule loading
def load_rules_for_external_agent():
    # ... detailed correct implementation
```

#### Added ❌ Anti-Pattern to Avoid Section
```markdown
## ❌ Anti-Pattern to Avoid

### Example: Incorrect Rule Loading
```python
# WRONG: Loading rules without priority system
def load_rules_incorrectly():
    # ... examples of what NOT to do
```

### Why it's wrong:
1. **No Priority System:** Kernel rules may not load first...
```

**Rationale:**
- Shows concrete examples of correct implementation
- Highlights common mistakes to avoid
- Explains why anti-patterns fail

---

## Content Preservation

### What Was Preserved
✅ All technical content from original `AGENTS.md`
✅ Rule loading logic and priority system
✅ Context analysis requirements
✅ Frontmatter format specifications
✅ Error handling protocols
✅ Platform-agnostic integration guidance
✅ Quick reference card
✅ All pseudo-code examples

### What Was Enhanced
✨ Added YAML frontmatter for discoverability
✨ Added AI Persona and Core Principle sections
✨ Added `[STRICT]` and `[GUIDELINE]` prefixes throughout
✨ Restructured into 4 Pillars format
✨ Added explicit anti-pattern examples
✨ Enhanced code examples with correct/incorrect comparisons
✨ Improved section numbering and hierarchy

### What Was Removed
❌ None - All content was preserved and enhanced

---

## Validation Checklist

Before finalizing migration, verify:

### Structure & Discoverability
- [ ] File has `.mdc` extension
- [ ] File is in `.cursor/rules/master-rules/` directory
- [ ] Filename follows convention: `8-master-rule-external-agent-interpretation.mdc`
- [ ] YAML frontmatter is present and valid
- [ ] Frontmatter contains only `description` and `alwaysApply` keys
- [ ] Description includes TAGS, TRIGGERS, SCOPE, and DESCRIPTION

### Personality & Intent
- [ ] AI Persona section is present
- [ ] Core Principle section is present
- [ ] Both sections clearly define "how to think" and "why"

### Precision & Clarity
- [ ] All directives use `[STRICT]` or `[GUIDELINE]` prefixes
- [ ] Protocol steps are clear and actionable
- [ ] Imperative language is used throughout
- [ ] No ambiguous instructions

### Exemplarity & Contrast
- [ ] ✅ Correct Implementation section is present
- [ ] ❌ Anti-Pattern to Avoid section is present
- [ ] Examples are complete and runnable (pseudo-code)
- [ ] Anti-patterns include explanations of why they're wrong

### Content Integrity
- [ ] All original content is preserved
- [ ] Technical accuracy is maintained
- [ ] No information was lost during restructuring
- [ ] Enhancements add value without changing meaning

---

## Testing Plan

### Test 1: Rule Discovery
**Objective**: Verify Cursor can discover the new rule

**Steps**:
1. Open Cursor IDE
2. Trigger rule discovery (e.g., mention "external agent" in a request)
3. Verify rule is loaded and announced

**Expected Result**: Rule appears in loaded rules list

### Test 2: Rule Application
**Objective**: Verify rule applies correctly when triggered

**Steps**:
1. Make a request mentioning "external agent" or "cross-platform"
2. Observe AI behavior
3. Verify rule instructions are followed

**Expected Result**: AI follows rule protocol and announces rule application

### Test 3: Legacy File Cleanup
**Objective**: Verify legacy file doesn't interfere

**Steps**:
1. Confirm `AGENTS.md` is archived or removed
2. Search for any remaining references
3. Update documentation if needed

**Expected Result**: No conflicts, clean migration

---

## Rollback Plan

If issues arise, rollback is simple:

### Rollback Steps
```bash
# 1. Remove new .mdc file
rm /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/rules/master-rules/8-master-rule-external-agent-interpretation.mdc

# 2. Restore legacy file from archive (if archived)
mv /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/rules/archive/AGENTS.md.legacy \
   /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/rules/AGENTS.md

# 3. Verify restoration
ls -la /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/rules/AGENTS.md
```

---

## Post-Migration Tasks

### Documentation Updates
- [ ] Update README.md to reference new rule location
- [ ] Update any developer guides mentioning AGENTS.md
- [ ] Update rule inventory in documentation

### Communication
- [ ] Notify team of migration
- [ ] Update any external documentation
- [ ] Add migration note to changelog

### Monitoring
- [ ] Monitor for any issues in first week
- [ ] Collect feedback from users
- [ ] Address any discovered issues

---

## Success Criteria

Migration is considered successful when:

✅ New `.mdc` file is in correct location  
✅ File follows all 4 Pillars of PLAN-MODE framework  
✅ Cursor can discover and load the rule  
✅ Rule applies correctly when triggered  
✅ Legacy file is archived or removed  
✅ All references are updated  
✅ No functionality is lost  
✅ Team is informed and documentation is updated  

---

## Conclusion

This migration transforms `AGENTS.md` from a static documentation file into a fully functional, discoverable rule that Cursor can automatically load and apply. The restructuring follows the PLAN-MODE framework while preserving all original content and enhancing it with clear directives, examples, and anti-patterns.

**Next Steps:**
1. Review the generated `.mdc` file
2. Execute migration steps
3. Test rule discovery and application
4. Complete post-migration tasks

**Questions or Issues:**
If any issues arise during migration, refer to the Rollback Plan section or consult the PLAN-MODE framework documentation.
