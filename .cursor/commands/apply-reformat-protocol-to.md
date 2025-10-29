# COMMAND: REFORMAT PROTOCOL WITH CATEGORY-BASED FORMATS

**Usage:** Read this file and execute the reformat steps for the specified target protocol file.

**Target File Parameter:** When executing, specify which protocol file to reformat (e.g., `.cursor/ai-driven-workflow/08-generate-tasks.md`)

## 📋 Purpose

This command reformats existing protocol files to follow the **category-based format system** while **preserving ALL existing content** including reasoning, logic, steps, evidence requirements, gates, and automation hooks.

**Core Principle:** Change ONLY the structural format, never the content.

---

## 🎯 Objective

Reformat the specified protocol file to follow category-based format standards while preserving ALL existing content (reasoning, logic, steps, evidence, gates).

---

## 📥 Input Parameters

When executing this command, you need:

- **Target Protocol File:** Specify the protocol path (e.g., `.cursor/ai-driven-workflow/08-generate-tasks.md`)
- **Preserve Content:** YES (mandatory - non-negotiable)
- **Apply Category Formats:** YES (mandatory)

**Example Execution:**
1. Read this file (`.cursor/commands/apply-reformat-protocol-to.md`)
2. Follow all steps below
3. Apply to target file: `.cursor/ai-driven-workflow/01-client-proposal-generation.md`

---

## 🛠️ Execution Steps

### Output Directory (Single Folder)

All generated outputs must be placed under a single folder to avoid clutter.

- Root: `.artifacts/protocol-reformat/[protocol-stem]/`
- Files:
  - `ORIGINAL-BACKUP.md`
  - `CONTENT-INVENTORY.json`
  - `FORMAT-ANALYSIS.md`
  - `format-changes.diff`
  - `validation-report.md`
  - `REFORMATTED.md` (optional working file before overwrite)

Note: `[protocol-stem]` is the basename of the protocol file without extension (e.g., `01-client-proposal-generation`).

### STEP 1: Content Inventory & Backup

**[STRICT]** Before any changes, create a complete inventory of existing content:

1. **Read the entire protocol file**
2. **Extract and document:**
   - All reasoning blocks and their justifications
   - All logic flows and decision trees
   - All step sequences and substeps
   - All evidence requirements (`.artifacts/...` paths)
   - All gate definitions and validation criteria
   - All automation hooks and scripts
   - All handoff checklists
   - All integration points
   - All [STRICT], [MUST], [GUIDELINE] markers

3. **Create backup file:**
   ```bash
   mkdir -p .artifacts/protocol-reformat/[protocol-stem]
   cp [protocol-path] .artifacts/protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md
   ```

4. **Generate content inventory:**
   Create `.artifacts/protocol-reformat/[protocol-stem]/CONTENT-INVENTORY.json` containing:
   ```json
   {
     "reasoning_blocks_count": 12,
     "evidence_requirements_count": 15,
     "script_references": ["scripts/validate_xyz.py", ...],
     "artifact_paths": [".artifacts/proposal/...", ...],
     "gate_definitions_count": 4,
     "automation_hooks_count": 8
   }
   ```

---

### STEP 2: Section Analysis

**[STRICT]** For EACH section in the protocol, perform this analysis:

#### 2.1 Identify Section Type

Ask for each section: **"What is this section DOING?"**

| Section Behavior | Category File | Variant (if applicable) |
|-----------------|---------------|-------------------------|
| Executing simple workflow | EXECUTION-FORMATS.md | BASIC |
| Executing detailed tracking (5+ substeps) | EXECUTION-FORMATS.md | SUBSTEPS |
| Executing with critical decisions | EXECUTION-FORMATS.md | REASONING |
| Setting rules/standards | GUIDELINES-FORMATS.md | N/A |
| Creating project issues | ISSUE-FORMATS.md | N/A |
| Multi-agent orchestration | PROMPT-FORMATS.md | N/A |
| Protocol analysis/generation | META-FORMATS.md | N/A |

#### 2.2 Document Format Choice

For each section, add an HTML comment at the beginning:

```markdown
<!-- [Category: EXECUTION-FORMATS - REASONING variant] -->
<!-- Why: This phase involves critical go/no-go decisions requiring documented premises, alternatives, and risk assessment -->
```

**Example Section Analysis:**

```markdown
## WORKFLOW

<!-- [Category: EXECUTION-FORMATS - Mixed variants by phase] -->

### PHASE 1: Context Preparation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple file loading and validation, no complex decisions -->

### PHASE 2: Stakeholder Alignment
<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: Critical decision on proposal scope requires documented alternatives and risk assessment -->

### PHASE 3: Detailed Breakdown
<!-- [Category: EXECUTION-SUBSTEPS] -->
<!-- Why: Multiple precise substeps (7+ steps) requiring exact tracking and evidence collection -->

### PHASE 4: Validation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward validation checklist -->
```

---

### STEP 3: Format Application

**[STRICT]** Apply the selected format to each section following these rules:

#### Rule 1: Preserve ALL Content Elements

**✅ MUST KEEP:**
- Every reasoning block
- Every logic explanation
- Every step description
- Every evidence requirement (exact path: `.artifacts/...`)
- Every validation criterion
- Every script reference (exact name and path)
- Every gate definition
- Every handoff item
- Every [STRICT], [MUST], [GUIDELINE] marker
- Every example (DO/DON'T blocks)

#### Rule 2: Change ONLY Structure

**❌ DO NOT:**
- Remove or summarize content
- Change script names or paths
- Modify evidence artifact paths
- Remove reasoning justifications
- Simplify decision documentation
- Merge steps to reduce length
- Remove "redundant" validation checks

**✅ DO:**
- Change header levels (e.g., `###` to `####`)
- Change numbering style (e.g., `1.` to `1.1`)
- Add `[REASONING]` blocks where decisions exist
- Restructure subsections for clarity
- Add format choice comments
- Improve visual hierarchy

#### Rule 3: Format-Specific Transformations

**If applying EXECUTION-BASIC:**

```markdown
## PHASE [N]: [Phase Name]

1. **`[MUST]` [Step Name]:**
   * **Action:** [What to do - preserve exact original wording]
   * **Evidence:** [Required output - preserve exact artifact path]
   * **Validation:** [How to verify - preserve exact criteria]
   
   **Example (DO):**
   [If original has example, preserve it exactly]
   
   **Example (DON'T):**
   [If original has anti-pattern, preserve it exactly]
```

**If applying EXECUTION-SUBSTEPS:**

```markdown
## PHASE [N]: [Phase Name]

1. **`[MUST]` [Main Step Name]:**
   * **[N].1. [Substep Name]:**
       * **Action:** [What to do - preserve exact original wording]
       * **Evidence:** [Required output - preserve exact artifact path]
       * **Validation:** [How to verify - preserve exact criteria]
   
   * **[N].2. [Substep Name]:**
       * **Action:** [What to do - preserve exact original wording]
       * **Evidence:** [Required output - preserve exact artifact path]
       * **Validation:** [How to verify - preserve exact criteria]
   
   * **[N].3. [Substep Name]:**
       * **Action:** [What to do]
       * **Evidence:** [Required output]
```

**If applying EXECUTION-REASONING:**

```markdown
## PHASE [N]: [Phase Name]

1. **`[MUST]` [Step Name]:**
   * **Action:** [What to do - preserve exact original wording]
   
   **[REASONING]:**
   - **Premises:** [Starting facts/conditions - extract from original context]
   - **Constraints:** [Limitations/requirements - extract from original]
   - **Alternatives Considered:**
     * **A)** [Option 1] - [Why selected/rejected - from original logic]
     * **B)** [Option 2] - [Why selected/rejected - from original logic]
     * **C)** [Option 3] - [If exists in original]
   - **Decision:** [Final choice and justification - from original]
   - **Evidence:** [Supporting data/references for decision]
   - **Risks & Mitigations:**
     * **Risk:** [Potential issue] → **Mitigation:** [How to address]
     * [Additional risks from original]
   - **Acceptance Link:** [Reference to requirement/standard/PRD section]
   
   * **Evidence:** [Required output - preserve exact artifact path]
   * **Validation:** [How to verify - preserve exact criteria]
   
   **Example (DO):**
   [If original has example, preserve it exactly]
```

---

### STEP 4: Cross-Reference Validation

**[STRICT]** After reformatting, validate that:

1. **Reasoning Preservation:**
   - [ ] Every reasoning block from original appears in reformatted version
   - [ ] All decision justifications are present
   - [ ] All alternative considerations are documented

2. **Technical Reference Preservation:**
   - [ ] Every script reference is preserved exactly (no path changes)
   - [ ] Every evidence requirement is preserved exactly (no artifact path changes)
   - [ ] Every automation command is preserved exactly

3. **Gate Preservation:**
   - [ ] Every gate definition is complete
   - [ ] All gate criteria are documented
   - [ ] All gate automation hooks are present

4. **Integration Preservation:**
   - [ ] All integration points are documented
   - [ ] All handoff items are present
   - [ ] All approval requirements are listed

5. **Content Count Validation:**
   ```bash
# Count key elements using consolidated paths
ORIG=.artifacts/protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md
REF=[protocol-path]

grep -c "\[REASONING\]" "$ORIG"; grep -c "\[REASONING\]" "$REF"  # Must match
grep -c "\.artifacts/" "$ORIG"; grep -c "\.artifacts/" "$REF"      # Must match
grep -c "scripts/" "$ORIG"; grep -c "scripts/" "$REF"                # Must match
```

---

### STEP 5: Diff Comparison

**[STRICT]** Generate a comprehensive diff report:

```bash
# 1. Compare structure changes only (ignore whitespace)
diff -u .artifacts/protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md \
       [protocol-path] > .artifacts/protocol-reformat/[protocol-stem]/format-changes.diff

# 2. Verify no content loss - Reasoning blocks
echo "Original reasoning blocks:"
grep -c "REASONING" .artifacts/protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md
echo "Reformatted reasoning blocks:"
grep -c "REASONING" [protocol-path]

# 3. Verify no content loss - Evidence paths
echo "Original evidence paths:"
grep -c ".artifacts/" .artifacts/protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md
echo "Reformatted evidence paths:"
grep -c ".artifacts/" [protocol-path]

# 4. Verify no content loss - Script references
echo "Original script references:"
grep -c "scripts/" .artifacts/protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md
echo "Reformatted script references:"
grep -c "scripts/" [protocol-path]

# 5. Verify no content loss - Gates
echo "Original gates:"
grep -c "Gate [0-9]:" .artifacts/protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md
echo "Reformatted gates:"
grep -c "Gate [0-9]:" [protocol-path]
```

---

### STEP 6: Quality Checklist

**[STRICT]** Before finalizing, confirm:

#### Content Preservation Checklist
- [ ] All reasoning blocks preserved (count matches original)
- [ ] All logic flows preserved (no simplification)
- [ ] All steps preserved (no merging or removal)
- [ ] All evidence paths unchanged (exact matches)
- [ ] All script references unchanged (exact matches)
- [ ] All gate definitions complete (no summary)
- [ ] All handoffs documented (no omissions)
- [ ] All examples preserved (DO/DON'T blocks intact)
- [ ] All [STRICT]/[MUST]/[GUIDELINE] markers preserved

#### Format Application Checklist
- [ ] Format follows category-based standards
- [ ] Section format choices documented with comments
- [ ] Each section has "Why" justification for format choice
- [ ] Visual hierarchy is improved
- [ ] Numbering is consistent within each section
- [ ] [REASONING] blocks added where decisions exist

#### Technical Integrity Checklist
- [ ] Diff report shows ONLY structural changes
- [ ] No artifact paths were modified
- [ ] No script names were changed
- [ ] No validation criteria were simplified
- [ ] No automation hooks were removed

---

## 📤 Output Deliverables

After successful execution, generate (centralized in `.artifacts/protocol-reformat/[protocol-stem]/`):

1. **Reformatted Protocol:**  
   `[protocol-path]` (overwrites original after validation)

2. **Output Folder:**  
   `.artifacts/protocol-reformat/[protocol-stem]/` containing:
   - `ORIGINAL-BACKUP.md`
   - `CONTENT-INVENTORY.json`
   - `FORMAT-ANALYSIS.md`
   - `format-changes.diff`
   - `validation-report.md`

3. **Format Analysis (example template):**  
   Saved as `FORMAT-ANALYSIS.md`
   ```markdown
   # Format Analysis for [Protocol Name]
   
   ## Section-by-Section Format Choices
   
   ### PHASE 1: [Name]
   - **Format Applied:** EXECUTION-BASIC
   - **Reasoning:** Simple workflow steps with straightforward validation
   - **Content Preserved:** 3 steps, 3 evidence requirements, 1 script reference
   
   ### PHASE 2: [Name]
   - **Format Applied:** EXECUTION-REASONING
   - **Reasoning:** Critical go/no-go decision requiring documented alternatives
   - **Content Preserved:** 1 decision point, 3 alternatives, 2 risk mitigations
   
   [Continue for all sections...]
   ```

4. **Validation Report (example template):**  
   Saved as `validation-report.md`
   ```markdown
   # Validation Report for [Protocol Name]
   
   ## Content Preservation Validation
   
   | Element Type | Original Count | Reformatted Count | Status |
   |--------------|----------------|-------------------|--------|
   | Reasoning blocks | 12 | 12 | ✅ PASS |
   | Evidence paths | 15 | 15 | ✅ PASS |
   | Script references | 8 | 8 | ✅ PASS |
   | Gate definitions | 4 | 4 | ✅ PASS |
   | Handoff items | 6 | 6 | ✅ PASS |
   
   ## Format Application Validation
   
   | Section | Original Format | Applied Format | Justification |
   |---------|----------------|----------------|---------------|
   | PHASE 1 | Unstructured | EXECUTION-BASIC | Simple workflow |
   | PHASE 2 | Unstructured | EXECUTION-REASONING | Critical decisions |
   | PHASE 3 | Unstructured | EXECUTION-SUBSTEPS | 7 detailed substeps |
   
   ## Overall Status: ✅ PASS
   ```

---

## ✅ Success Criteria

**The reformat is successful if:**

✅ All content from original protocol is present in reformatted version  
✅ Format follows category-based selection principles  
✅ Each section uses the most appropriate format variant  
✅ Format choices are documented and justified  
✅ No script paths or artifact paths were modified  
✅ All reasoning logic is preserved  
✅ Protocol remains fully executable  
✅ Validation report shows 100% content preservation  
✅ Diff shows ONLY structural/formatting changes

---

## ❌ Anti-Patterns to Avoid

**DO NOT:**

❌ Choose one format for entire protocol without section-by-section analysis  
❌ Remove "verbose" reasoning blocks to "clean up" the document  
❌ Change evidence artifact paths "for consistency"  
❌ Simplify complex REASONING blocks to BASIC format to reduce length  
❌ Apply SUBSTEPS format when simple BASIC would suffice (over-engineering)  
❌ Miss the "Why" justification comments for format choices  
❌ Merge multiple steps into one to make protocol "shorter"  
❌ Remove examples or DO/DON'T blocks as "redundant"  
❌ Change script names to "standardize" them  
❌ Simplify validation criteria to "streamline" the process

---

## 🔧 Troubleshooting

### Issue: Content appears to be lost after reformat

**Solution:**
1. Compare content inventory JSON before/after
2. Run validation report script
3. If mismatch found, restore from backup and re-analyze section format choices
4. Ensure REASONING variant was used for decision-heavy sections

### Issue: Diff shows unexpected content changes

**Solution:**
1. Review diff line by line
2. Identify if changes are:
   - Structural only (acceptable) - e.g., header level changes
   - Content modifications (unacceptable) - restore from backup
3. Re-run with stricter content preservation rules

### Issue: Format choice seems wrong for a section

**Solution:**
1. Re-read the section's actual behavior
2. Ask: "What is this section DOING?" (not "What is it about?")
3. Check if section involves:
   - Simple workflow? → BASIC
   - Detailed tracking? → SUBSTEPS
   - Critical decisions? → REASONING
4. Update format choice and document why

---

## 📚 Related Resources

- **Category Format Files:**
  - `examples/EXECUTION-FORMATS.md` - 3 execution variants
  - `examples/GUIDELINES-FORMATS.md` - Rules format
  - `examples/ISSUE-FORMATS.md` - Issue tracking format
  - `examples/PROMPT-FORMATS.md` - Multi-agent format
  - `examples/META-FORMATS.md` - Protocol analysis format

- **Category Selection Guide:**
  - `examples/README.md` - Category-based selection principles

---

## 🎯 Usage Examples

### Example 1: Reformat Protocol 08 (Generate Tasks)

```markdown
@apply .cursor/commands/apply-reformat-protocol-to.md --file=.cursor/ai-driven-workflow/08-generate-tasks.md
```

**Expected Result:**
- PHASE 1-2: EXECUTION-BASIC (simple context loading)
- PHASE 3: EXECUTION-REASONING (critical task breakdown decisions)
- PHASE 4-5: EXECUTION-SUBSTEPS (detailed task decomposition with 7+ substeps)
- PHASE 6: EXECUTION-BASIC (validation checklist)

### Example 2: Reformat Protocol 14 (Pre-Deployment Staging)

```markdown
@apply .cursor/commands/apply-reformat-protocol-to.md --file=.cursor/ai-driven-workflow/14-pre-deployment-staging.md
```

**Expected Result:**
- PHASE 1: EXECUTION-SUBSTEPS (staging alignment with precise comparison steps)
- PHASE 2: EXECUTION-REASONING (deployment rehearsal go/no-go decision)
- PHASE 3: EXECUTION-SUBSTEPS (rollback verification sequence)
- PHASE 4: EXECUTION-REASONING (readiness review approval decision)

### Example 3: Reformat Protocol 01 (Client Proposal)

```markdown
@apply .cursor/commands/reformat-protocol.md --file=.cursor/ai-driven-workflow/01-client-proposal-generation.md
```

**Expected Result:**
- PHASE 1: EXECUTION-BASIC (brief loading)
- PHASE 2: EXECUTION-REASONING (pricing strategy decision with alternatives)
- PHASE 3: EXECUTION-SUBSTEPS (detailed proposal generation with 5+ substeps)
- PHASE 4: EXECUTION-BASIC (validation)

---

## 🚀 Quick Start

1. **Identify protocol to reformat**
2. **Invoke command:**
   ```markdown
   @apply .cursor/commands/apply-reformat-protocol-to.md --file=[your-protocol-path]
   ```
3. **Review validation report**
4. **Verify diff shows only structural changes**
5. **Confirm protocol is still executable**
6. **Archive backup and deliverables**

---

## 📝 Notes

- **Backup First:** Always creates backup before any changes
- **Content Sacred:** Content preservation is non-negotiable
- **Format Flexible:** Format choices are per-section, not per-protocol
- **Document Choices:** Every format choice must have a "Why" comment
- **Validate Everything:** Multiple validation layers ensure no content loss

---

**[MASTER RAY™]** This command ensures protocol evolution without regression.

