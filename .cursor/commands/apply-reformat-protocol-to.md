# COMMAND: REFORMAT PROTOCOL WITH CATEGORY-BASED FORMATS

**For Codex Users:** If `@apply` syntax doesn't work, use this command instead:
```
Analyze .cursor/commands/apply-reformat-protocol-to.md and apply to [target file]
```

**Usage:** Read this file and execute the reformat steps for the specified target protocol file.

**Target File Parameter:** When executing, specify which protocol file to reformat:
- Protocol files: `.cursor/ai-driven-workflow/[protocol-name].md`
- Or already reformatted: `.artifacts/new-protocol-reformat/[protocol-stem]/*.md`

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
- **--force-format (optional):** Override auto-selector for all sections
  - Choices: `EXECUTION::REASONING|EXECUTION::SUBSTEPS|EXECUTION::BASIC|GUIDELINES|ISSUE|PROMPT|META`
  - Precedence: Inline `[format: ...]` > `--force-format` > auto-selector

**Example Execution:**
1. Read this file (`.cursor/commands/apply-reformat-protocol-to.md`)
2. Follow all steps below
3. Apply to target file: `.cursor/ai-driven-workflow/01-client-proposal-generation.md`

---

## 🛠️ Execution Steps

### Output Directory (Single Folder)

All generated outputs must be placed under a single folder to avoid clutter.

- Root: `.artifacts/new-protocol-reformat/[protocol-stem]/`
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
   mkdir -p .artifacts/new-protocol-reformat/[protocol-stem]
   cp [protocol-path] .artifacts/new-protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md
   ```

4. **Generate content inventory:**
   Create `.artifacts/new-protocol-reformat/[protocol-stem]/CONTENT-INVENTORY.json` containing:
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

### STEP 1.5: Auto-Format Selector (Section-Level)

**Goal:** For each top-level section/phase in the target protocol, automatically pick the correct category + variant from the 6 format files, then annotate the section with a one-line HTML comment documenting the choice and the "Why".

#### Signals & Heuristics (greppable, content-preserving)
- REASONING_HITS: `^\[REASONING\]|^- +Premises:|^- +Constraints:|^- +Alternatives|^- +Decision:|^- +Evidence:|^- +Risks` 
- SUBSTEP_HITS: `^[[:space:]]*([0-9]+(\.[0-9]+)+[.)]?|[0-9]+[.)])[[:space:]]` 
- ROLE_HITS: `^\*\*System:\*\*|^\*\*Developer:\*\*|^\*\*User:\*\*` 
- META_HITS: `Format (A|B|C|D)|generator-?instructions|Circular Validation|Format Classification|Reusable Component Extraction` 
- ISSUE_HITS: `Subtasks|Priority.*\[P[0-4]\]|File Scaffolding` 
- GUIDELINE_MARKS: `^\*\*\[STRICT\]|\*\*\[GUIDELINE\]` 
- HAS_FRONTMATTER: unang linya `---` 
- IS_RULES_HEADING: heading contains `rules|guidelines|standards` (case-insensitive)

**Density rule:** `reasoning_density = reasoning_hits / max(1, section_lines)`; if ≥ `0.01` ⇒ EXECUTION::REASONING.

#### Decision Rules (ordered; first match wins)
1. PROMPT (may role blocks)
2. META (meta-generator/format A–D/analyzer cues)
3. ISSUE (issue scaffold/priorities/subtasks)
4. GUIDELINES (frontmatter + [STRICT]/[GUIDELINE] + rules/guidelines heading)
5. EXECUTION::REASONING (density ≥ 0.01)
6. EXECUTION::SUBSTEPS (substeps ≥ 6)
7. EXECUTION::BASIC (fallback)

**Overrides (precedence)**
1. Inline heading tag: `[format: CATEGORY[::VARIANT]]` 
2. `--force-format=…` 
3. Auto-selector

**Annotation (single-line)**
```html
<!-- FORMAT:{CATEGORY}[::{VARIANT}] | WHY:{signal/override} -->
```

**Minimal CLI Hook (optional)**
```
--force-format=EXECUTION::REASONING|EXECUTION::SUBSTEPS|EXECUTION::BASIC|GUIDELINES|ISSUE|PROMPT|META
```

---

### STEP 2: Section Analysis

**[STRICT]** For EACH section in the protocol, perform this analysis:

#### 2.1 Identify Section Type (Automated then Human-Confirm)

1. Run **STEP 1.5 Auto-Format Selector** to compute a candidate choice per section.
2. Insert the one-line HTML annotation documenting the choice and "Why".
3. Allow inline override via `[format: ...]` in the heading (case-insensitive).

**Reference table for validation:**

| Section Behavior | Category | Variant (if applicable) |
|-----------------|---------------|-------------------------|
| Executing simple workflow | EXECUTION | BASIC |
| Executing detailed tracking (6+ substeps) | EXECUTION | SUBSTEPS |
| Executing with critical decisions | EXECUTION | REASONING |
| Setting rules/standards | GUIDELINES | N/A |
| Creating project issues | ISSUE | N/A |
| Multi-agent orchestration | PROMPT | N/A |
| Protocol analysis/generation | META | N/A |

#### 2.2 Document Format Choice (Enforced)

Each section MUST contain the annotation:

```html
<!-- FORMAT:{CATEGORY}[::{VARIANT}] | WHY:{reason/override} -->
```

**Absence or malformed annotation is a blocker.**

**Example Section Analysis:**

```markdown
## WORKFLOW

<!-- FORMAT:EXECUTION | WHY:Mixed variants by phase -->

### PHASE 1: Context Preparation
<!-- FORMAT:EXECUTION::BASIC | WHY:Simple file loading, no decisions -->

### PHASE 2: Stakeholder Alignment
<!-- FORMAT:EXECUTION::REASONING | WHY:reasoning_density=0.02, critical scope decision -->

### PHASE 3: Detailed Breakdown
<!-- FORMAT:EXECUTION::SUBSTEPS | WHY:substeps=8 -->

### PHASE 4: Validation
<!-- FORMAT:EXECUTION::BASIC | WHY:Straightforward checklist -->
```

---

### STEP 3: Determine Generation Strategy (Multi-Part vs Single)

**[CRITICAL]** Large protocols (800+ lines) must be reformatted in multiple parts to prevent token overflow!

#### 3.1 Check Protocol Size

```bash
# Count lines in original protocol
wc -l [protocol-path]
```

#### 3.2 Choose Strategy

| Protocol Size | Strategy | Output Files |
|--------------|----------|--------------|
| < 800 lines | **Single Generation** | `REFORMATTED.md` only |
| 800-1500 lines | **Multi-Part (3 parts)** | `REFORMATTED-PART1.md`, `PART2.md`, `PART3.md` → merge to `REFORMATTED.md` |
| 1500+ lines | **Multi-Part (5 parts)** | `REFORMATTED-PART1.md`, `PART2.md`, `PART3.md`, `PART4.md`, `PART5.md` → merge to `REFORMATTED.md` |

#### 3.3 Multi-Part Generation Process

**If protocol is large (800+ lines):**

1. **Divide protocol into logical sections:**
   - PART1: Prerequisites + AI Role + First 1-2 workflow steps
   - PART2: Next 2-3 workflow steps
   - PART3: Remaining workflow steps
   - PART4: Quality Gates + Communication (if needed)
   - PART5: Automation + Handoff + Reflection (if needed)

2. **Generate each part separately:**
   ```markdown
   # Generate PART1
   - Apply category-based formats to sections 1-2
   - Save to `.artifacts/new-protocol-reformat/[protocol-stem]/REFORMATTED-PART1.md`
   
   # Generate PART2
   - Apply category-based formats to sections 3-5
   - Save to `.artifacts/new-protocol-reformat/[protocol-stem]/REFORMATTED-PART2.md`
   
   # Continue for all parts...
   ```

3. **Merge all parts into final REFORMATTED.md:**
   ```bash
   cd .artifacts/new-protocol-reformat/[protocol-stem]/
   cat REFORMATTED-PART1.md > REFORMATTED.md
   echo "" >> REFORMATTED.md
   cat REFORMATTED-PART2.md >> REFORMATTED.md
   echo "" >> REFORMATTED.md
   cat REFORMATTED-PART3.md >> REFORMATTED.md
   # Continue for all parts...
   ```

4. **Verify merged file:**
   - Check that all sections are present
   - Check that content flows logically
   - Check that no content was duplicated

**Why Multi-Part?**
- Prevents token overflow during generation
- Allows focused formatting on specific sections
- Makes validation easier (can check each part)
- Enables recovery if one part fails (no need to regenerate all)

---

### STEP 4: Format Application

**[STRICT]** Apply the selected format to each section (or part) following these rules:

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

**If applying GUIDELINES:**
- Rewrap using YAML frontmatter + `[STRICT]`/`[GUIDELINE]` structure from `examples/GUIDELINES-FORMATS.md`

**If applying ISSUE:**
- Rewrap using 9-subtask scaffold from `examples/ISSUE-FORMATS.md`

**If applying PROMPT:**
- Rewrap using System/Developer/User role blocks from `examples/PROMPT-FORMATS.md`

**If applying META:**
- Rewrap using analyzer/classifier (Format A/B/C/D) structure from `examples/META-FORMATS.md`

#### Guards Before Transformation

**[STRICT]** Before transforming any section:
- **Verify** that the chosen `{CATEGORY}[::{VARIANT}]` is one of the allowed values:
  - `EXECUTION::REASONING`
  - `EXECUTION::SUBSTEPS`
  - `EXECUTION::BASIC`
  - `GUIDELINES`
  - `ISSUE`
  - `PROMPT`
  - `META`
- If not in allowed set, fallback to `EXECUTION::BASIC` and log a WARNING in `validation-report.md`.
- If `EXECUTION::REASONING`, append structural `[REASONING]` blocks after each step (structure only; do not invent content).

---

### STEP 5: Cross-Reference Validation

**[STRICT]** After reformatting and merging (if multi-part), validate that:

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
ORIG=.artifacts/new-protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md
REF=.artifacts/new-protocol-reformat/[protocol-stem]/REFORMATTED.md

grep -c "\[REASONING\]" "$ORIG"; grep -c "\[REASONING\]" "$REF"  # Must match
grep -c "\.artifacts/" "$ORIG";  grep -c "\.artifacts/" "$REF"      # Must match
grep -c "scripts/" "$ORIG";      grep -c "scripts/" "$REF"          # Must match
```

6. **Selection Integrity Counters:**
   
   **[STRICT]** Validate format selection integrity:
   
   - **Per-category counts:** Count sections using each `{CATEGORY}[::{VARIANT}]`.
   - **GUIDELINES:** Warn if no YAML frontmatter detected (check first 10 lines for `---`).
   - **ISSUE:** Warn if subtasks < 9 (count `- [ ]` checkboxes).
   - **PROMPT:** Warn if role blocks < 3 (count `**System:**`, `**Developer:**`, `**User:**`).
   - **META:** Warn if meta cues not detected post-transform (check for format A/B/C/D or analyzer phases).
   
   **Write all warnings to `validation-report.md`.**

---

### STEP 6: Diff Comparison

**[STRICT]** Generate a comprehensive diff report (comparing original vs final merged REFORMATTED.md):

```bash
# 1. Compare structure changes only (ignore whitespace)
diff -u .artifacts/new-protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md \
       .artifacts/new-protocol-reformat/[protocol-stem]/REFORMATTED.md \
       > .artifacts/new-protocol-reformat/[protocol-stem]/format-changes.diff

# 2. Verify no content loss - Reasoning blocks
echo "Original reasoning blocks:"
grep -c "REASONING" .artifacts/new-protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md
echo "Reformatted reasoning blocks:"
grep -c "REASONING" .artifacts/new-protocol-reformat/[protocol-stem]/REFORMATTED.md

# 3. Verify no content loss - Evidence paths
echo "Original evidence paths:"
grep -c ".artifacts/" .artifacts/new-protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md
echo "Reformatted evidence paths:"
grep -c ".artifacts/" .artifacts/new-protocol-reformat/[protocol-stem]/REFORMATTED.md

# 4. Verify no content loss - Script references
echo "Original script references:"
grep -c "scripts/" .artifacts/new-protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md
echo "Reformatted script references:"
grep -c "scripts/" .artifacts/new-protocol-reformat/[protocol-stem]/REFORMATTED.md

# 5. Verify no content loss - Gates
echo "Original gates:";    grep -Ei -c '(^|[[:space:]])Gate(s)?[[:space:]:#]' \
  .artifacts/new-protocol-reformat/[protocol-stem]/ORIGINAL-BACKUP.md
echo "Reformatted gates:"; grep -Ei -c '(^|[[:space:]])Gate(s)?[[:space:]:#]' \
  .artifacts/new-protocol-reformat/[protocol-stem]/REFORMATTED.md
```

---

### STEP 7: Quality Checklist

**[STRICT]** Before finalizing, confirm (all checks on final merged REFORMATTED.md):

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

After successful execution, generate (centralized in `.artifacts/new-protocol-reformat/[protocol-stem]/`):

1. **Reformatted Protocol:**  
   `[protocol-path]` (overwrites original after validation)

2. **Output Folder:**  
   `.artifacts/new-protocol-reformat/[protocol-stem]/` containing:
   - `ORIGINAL-BACKUP.md` - Exact copy of original protocol
   - `CONTENT-INVENTORY.json` - Structured content counts
   - `FORMAT-ANALYSIS.md` - Section-by-section format choices
   - `REFORMATTED-PART1.md` - First part (if multi-part generation)
   - `REFORMATTED-PART2.md` - Second part (if multi-part generation)
   - `REFORMATTED-PART3.md` - Third part (if multi-part generation)
   - `REFORMATTED-PART4.md` - Fourth part (if multi-part generation, 1500+ lines)
   - `REFORMATTED-PART5.md` - Fifth part (if multi-part generation, 1500+ lines)
   - `REFORMATTED.md` - Final merged output (all parts combined)
   - `format-changes.diff` - Structural changes only
   - `validation-report.md` - 100% content preservation proof

3. **Format Analysis (auto-filled):**  
   Saved as `FORMAT-ANALYSIS.md`
   ```markdown
   # Format Analysis for [Protocol Name]
   
   ## Section-by-Section Format Choices
   
   | Section | Signals Detected | Decision Rule | Format Applied | Why |
   |---------|-----------------|---------------|----------------|-----|
   | PHASE 1: [Name] | REASONING: 0, SUBSTEPS: 0 | Rule 7 (default) | EXECUTION::BASIC | Simple workflow steps with straightforward validation |
   | PHASE 2: [Name] | REASONING_DENSITY: 0.02 | Rule 5 (density ≥ 0.01) | EXECUTION::REASONING | Critical go/no-go decision requiring documented alternatives |
   | PHASE 3: [Name] | SUBSTEPS: 8 | Rule 6 (≥6 substeps) | EXECUTION::SUBSTEPS | Multiple precise substeps requiring exact tracking |
   
   [Continue for all sections...]
   
   ## Category Distribution
   
   - **EXECUTION::BASIC:** 5 sections
   - **EXECUTION::SUBSTEPS:** 2 sections
   - **EXECUTION::REASONING:** 3 sections
   - **GUIDELINES:** 0 sections
   - **ISSUE:** 0 sections
   - **PROMPT:** 0 sections
   - **META:** 0 sections
   
   ## Manual Overrides Applied
   
   - PHASE 4: Override from auto-selected EXECUTION::BASIC to EXECUTION::REASONING (inline tag `[format: EXECUTION::REASONING]`)
   
   [List any human corrections or --force-format flags used]
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
   | PHASE 1 | Unstructured | EXECUTION::BASIC | Simple workflow |
   | PHASE 2 | Unstructured | EXECUTION::REASONING | Critical decisions |
   | PHASE 3 | Unstructured | EXECUTION::SUBSTEPS | 7 detailed substeps |
   
   ## Selection Integrity
   
   | Category | Section Count | Validation |
   |----------|---------------|------------|
   | EXECUTION::BASIC | 5 | ✅ PASS |
   | EXECUTION::REASONING | 3 | ✅ PASS |
   | EXECUTION::SUBSTEPS | 2 | ✅ PASS |
   | GUIDELINES | 0 | N/A |
   | ISSUE | 0 | N/A |
   | PROMPT | 0 | N/A |
   | META | 0 | N/A |
   
   **Warnings:**
   - None
   
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
   - Simple workflow? → EXECUTION::BASIC
   - Detailed tracking? → EXECUTION::SUBSTEPS
   - Critical decisions? → EXECUTION::REASONING
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
- PHASE 1-2: EXECUTION::BASIC (simple context loading)
- PHASE 3: EXECUTION::REASONING (critical task breakdown decisions)
- PHASE 4-5: EXECUTION::SUBSTEPS (detailed task decomposition with 7+ substeps)
- PHASE 6: EXECUTION::BASIC (validation checklist)

### Example 2: Reformat Protocol 14 (Pre-Deployment Staging)

```markdown
@apply .cursor/commands/apply-reformat-protocol-to.md --file=.cursor/ai-driven-workflow/14-pre-deployment-staging.md
```

**Expected Result:**
- PHASE 1: EXECUTION::SUBSTEPS (staging alignment with precise comparison steps)
- PHASE 2: EXECUTION::REASONING (deployment rehearsal go/no-go decision)
- PHASE 3: EXECUTION::SUBSTEPS (rollback verification sequence)
- PHASE 4: EXECUTION::REASONING (readiness review approval decision)

### Example 3: Reformat Protocol 01 (Client Proposal)

```markdown
@apply .cursor/commands/apply-reformat-protocol-to.md --file=.cursor/ai-driven-workflow/01-client-proposal-generation.md
```

**Expected Result:**
- PHASE 1: EXECUTION::BASIC (brief loading)
- PHASE 2: EXECUTION::REASONING (pricing strategy decision with alternatives)
- PHASE 3: EXECUTION::SUBSTEPS (detailed proposal generation with 6+ substeps)
- PHASE 4: EXECUTION::BASIC (validation)

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

