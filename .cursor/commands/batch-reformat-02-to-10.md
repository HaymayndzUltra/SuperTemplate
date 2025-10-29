usage: "@apply .cursor/commands/batch-reformat-02-to-10.md"

# COMMAND: Batch Reformat Protocols 02→10 (Strict Sequential)

## 📋 Purpose
- Reformat protocols 02 through 10 sequentially using the category-based formats.
- Prevent agent overload by enforcing strict one-step-at-a-time execution.

## 🔒 Execution Policy
- **[STRICT]** Process steps in order. Do not start the next step until the current step finishes.
- **Stop on error.** If a step fails, halt and report the failure.
- **No parallelization.** Do not batch or prefetch future steps.
- **Outputs** are consolidated automatically by the reformat command under:
  - `.artifacts/protocol-reformat/[protocol-stem]/`
- **Skip completed.** If a protocol folder already exists with `REFORMATTED.md` and `validation-report.md`, skip that step and continue to next.

## 📋 Before Starting
Check `.artifacts/protocol-reformat/BATCH-PROGRESS-SUMMARY.md` to see which protocols are already complete. Skip those steps.

---

## ✅ Steps (02 → 10)

**[STRICT] STEP 1 — Protocol 02**
- **Action:** read `.cursor/ai-driven-workflow/02-client-discovery-initiation.md`
- **Then execute:**
  ```markdown
  @apply .cursor/commands/apply-reformat-protocol-to.md --file=/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/ai-driven-workflow/02-client-discovery-initiation.md
  ```

**[STRICT] STEP 2 — Protocol 03**
- **Action:** read `.cursor/ai-driven-workflow/03-project-brief-creation.md`
- **Then execute:**
  ```markdown
  @apply .cursor/commands/apply-reformat-protocol-to.md --file=/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/ai-driven-workflow/03-project-brief-creation.md
  ```

**[STRICT] STEP 3 — Protocol 04**
- **Action:** read `.cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md`
- **Then execute:**
  ```markdown
  @apply .cursor/commands/apply-reformat-protocol-to.md --file=/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md
  ```

**[STRICT] STEP 4 — Protocol 05**
- **Action:** read `.cursor/ai-driven-workflow/05-bootstrap-your-project.md`
- **Then execute:**
  ```markdown
  @apply .cursor/commands/apply-reformat-protocol-to.md --file=/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/ai-driven-workflow/05-bootstrap-your-project.md
  ```

**[STRICT] STEP 5 — Protocol 06**
- **Action:** read `.cursor/ai-driven-workflow/06-create-prd.md`
- **Then execute:**
  ```markdown
  @apply .cursor/commands/apply-reformat-protocol-to.md --file=/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/ai-driven-workflow/06-create-prd.md
  ```

**[STRICT] STEP 6 — Protocol 07**
- **Action:** read `.cursor/ai-driven-workflow/07-technical-design-architecture.md`
- **Then execute:**
  ```markdown
  @apply .cursor/commands/apply-reformat-protocol-to.md --file=/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/ai-driven-workflow/07-technical-design-architecture.md
  ```

**[STRICT] STEP 7 — Protocol 08**
- **Action:** read `.cursor/ai-driven-workflow/08-generate-tasks.md`
- **Then execute:**
  ```markdown
  @apply .cursor/commands/apply-reformat-protocol-to.md --file=/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/ai-driven-workflow/08-generate-tasks.md
  ```

**[STRICT] STEP 8 — Protocol 09**
- **Action:** read `.cursor/ai-driven-workflow/09-environment-setup-validation.md`
- **Then execute:**
  ```markdown
  @apply .cursor/commands/apply-reformat-protocol-to.md --file=/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/ai-driven-workflow/09-environment-setup-validation.md
  ```

**[STRICT] STEP 9 — Protocol 10**
- **Action:** read `.cursor/ai-driven-workflow/10-process-tasks.md`
- **Then execute:**
  ```markdown
  @apply .cursor/commands/apply-reformat-protocol-to.md --file=/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.cursor/ai-driven-workflow/10-process-tasks.md
  ```

---

## 📦 Expected Outputs (per step)
For each protocol `[protocol-stem]`, the following files will be generated under `.artifacts/protocol-reformat/[protocol-stem]/`:
- `ORIGINAL-BACKUP.md` - Exact copy of original protocol before reformatting
- `CONTENT-INVENTORY.json` - Detailed inventory of all content elements (reasoning blocks, artifacts, scripts, gates)
- `FORMAT-ANALYSIS.md` - Section-by-section format choice documentation with justifications
- `REFORMATTED-PART1.md`, `PART2.md`, etc. - Multi-part reformatted output (for large protocols)
- `REFORMATTED.md` - Final merged reformatted protocol with category-based formats applied
- `format-changes.diff` - Diff showing structural changes only (no content modifications)
- `validation-report.md` - Comprehensive validation report confirming 100% content preservation

## 🧭 Completion Criteria
- All nine steps complete without errors.
- For every protocol:
  - Content counts match exactly (reasoning blocks, artifact paths, script refs)
  - Diffs show structural/formatting changes only
  - Validation report confirms 100% content preservation
  - All automation hooks and integration points intact

## 📊 Progress Tracking
A summary file is automatically maintained at:
- `.artifacts/protocol-reformat/BATCH-PROGRESS-SUMMARY.md`

This tracks:
- ✅ Completed protocols
- 🔄 In-progress protocols  
- ⏳ Pending protocols
- Quality assurance status per protocol

---

## 🔍 Actual Working Pattern (Observed)

Based on successful executions of protocols 02 and 03, here's what actually happens:

### Step-by-Step Process
1. **Read Original:** AI reads the full protocol file
2. **Create Backup:** Copies to `ORIGINAL-BACKUP.md`
3. **Analyze Content:** Generates `CONTENT-INVENTORY.json` with counts
4. **Analyze Format:** Creates `FORMAT-ANALYSIS.md` documenting section-by-section choices
5. **Reformat in Parts:** 
   - Large protocols are reformatted in chunks: `REFORMATTED-PART1.md`, `PART2.md`, etc.
   - This prevents token limit overload
6. **Merge Parts:** All parts combined into final `REFORMATTED.md`
7. **Generate Diff:** Creates `format-changes.diff` comparing original vs reformatted
8. **Validate:** Produces `validation-report.md` confirming 100% content preservation
9. **Update Progress:** Updates `BATCH-PROGRESS-SUMMARY.md`

### Key Success Factors
- ✅ **Multi-part generation** handles large protocols without overflow
- ✅ **Validation at each step** ensures no content loss
- ✅ **Progress tracking** allows resume after interruption
- ✅ **Exact paths** in commands prevent file not found errors

---

## 🔄 How to Resume/Continue

If execution was interrupted or you want to continue from a specific protocol:

### Check Current Status
```bash
cat .artifacts/protocol-reformat/BATCH-PROGRESS-SUMMARY.md
```

### Skip Completed Protocols
When you run `@apply .cursor/commands/batch-reformat-02-to-10.md`, manually skip steps that show ✅ COMPLETE in the progress summary.

### Current Status (as of last run)
- ✅ Protocol 02 - COMPLETE
- ✅ Protocol 03 - COMPLETE  
- ✅ Protocol 04 - COMPLETE
- ✅ Protocol 05 - COMPLETE
- 🔄 Protocol 06 - IN PROGRESS (only backup/inventory/format analysis generated)
- ⏳ Protocols 07-10 - PENDING

### To Continue
- Start from **STEP 5 (Protocol 06)** or the first non-completed protocol in the progress summary.
