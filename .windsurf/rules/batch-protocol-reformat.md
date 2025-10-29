---
trigger: always_on
---

# AI Agent Instructions - Batch Protocol Reformat

## 🚨 CRITICAL EXECUTION RULES

When executing batch reformat commands (reading `.cursor/commands/batch-reformat-02-to-23.md`), you **MUST** follow these rules **WITHOUT EXCEPTION**:

**Note:** The `@apply` syntax you may see in documentation is Cursor-specific and for reference only. Instead, **read the command file and follow the instructions directly**.

---

## 📋 Strict Sequential Execution Protocol

### Rule 1: One Step at a Time
**[STRICT]** Execute **ONLY ONE STEP** at a time. Do not proceed to the next step until the current step is **100% complete**.

**What "Complete" Means:**
- ✅ Protocol file has been read
- ✅ `apply-reformat-protocol-to.md` command has been executed
- ✅ All output files generated (ORIGINAL-BACKUP.md, CONTENT-INVENTORY.json, FORMAT-ANALYSIS.md, REFORMATTED.md, format-changes.diff, validation-report.md)
- ✅ Validation report confirms 100% content preservation
- ✅ Progress summary has been updated

### Rule 2: Mandatory Progress Update After Each Step
**[STRICT]** After **EVERY SINGLE STEP**, you **MUST** update the progress summary file:

```
/home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts/protocol-reformat/BATCH-PROGRESS-SUMMARY.md
```

**Update Requirements:**
1. Read the current BATCH-PROGRESS-SUMMARY.md
2. Update the status for the protocol you just completed
3. Update timestamps
4. Update completion counts
5. Save the updated summary

**Example Update:**
```markdown
## Protocol 06 - create-prd
- Status: ✅ COMPLETE
- Completed: 2025-10-29 14:30:00
- Validation: 100% content preservation confirmed
- Files: ORIGINAL-BACKUP.md, CONTENT-INVENTORY.json, FORMAT-ANALYSIS.md, REFORMATTED.md, format-changes.diff, validation-report.md
```

### Rule 3: No Parallelization or Prefetching
**[STRICT]** Do NOT:
- ❌ Read multiple protocol files at once
- ❌ Start the next step while the current step is still processing
- ❌ Batch multiple steps together
- ❌ "Prepare" or "prefetch" future steps

**Why:** This causes token overflow, incomplete processing, and validation errors.

### Rule 4: Checkpoint Validation Before Proceeding
**[STRICT]** Before moving to the next step, you **MUST** validate:

```
✓ Current protocol's output directory exists
✓ All 6+ required files are present
✓ validation-report.md shows 100% content preservation
✓ BATCH-PROGRESS-SUMMARY.md reflects completion
✓ No errors in previous step
```

**If ANY checkpoint fails:** STOP and report the issue. Do NOT proceed.

---

## 🔄 Execution Flow (Required Pattern)

For each step in the batch command:

```
1. READ: Load protocol file
   ↓
2. EXECUTE: Run apply-reformat-protocol-to.md command
   ↓
3. VALIDATE: Confirm all outputs generated correctly
   ↓
4. UPDATE: Update BATCH-PROGRESS-SUMMARY.md
   ↓
5. CHECKPOINT: Verify all validation criteria met
   ↓
6. PROCEED: Move to next step (or STOP if error)
```

**[BLOCKING]** You **MUST** complete steps 1-5 before moving to step 6.

---

## 📊 Progress Summary Update Template

After **EVERY** completed step, update the summary with this pattern:

```markdown
## Summary
- Total Protocols: 22 (02-23)
- Completed: [N]
- In Progress: [0 or 1]
- Pending: [remaining count]
- Failed: [count if any]

## Detailed Status

### ✅ Completed Protocols

#### Protocol [NN] - [protocol-name]
- Status: ✅ COMPLETE
- Started: [timestamp]
- Completed: [timestamp]
- Duration: [time taken]
- Output Directory: `.artifacts/protocol-reformat/[protocol-stem]/`
- Validation: 100% content preservation confirmed
- Files Generated:
  - ✅ ORIGINAL-BACKUP.md
  - ✅ CONTENT-INVENTORY.json
  - ✅ FORMAT-ANALYSIS.md
  - ✅ REFORMATTED.md
  - ✅ format-changes.diff
  - ✅ validation-report.md

[Repeat for each completed protocol]

### 🔄 In Progress Protocols
[None or current protocol]

### ⏳ Pending Protocols
[List remaining protocols]
```

---

## 🛑 Error Handling & Recovery

### If a Step Encounters an Error:
**[STRICT]** Do NOT stop immediately. Instead, follow this intelligent recovery protocol:

1. **ANALYZE the error:**
   - Identify the root cause
   - Determine if it's recoverable
   - Check what succeeded and what failed

2. **ATTEMPT to FIX:**
   - If file not found → verify path and retry
   - If parsing error → analyze content structure and adjust
   - If validation incomplete → regenerate missing outputs
   - If token overflow → break into smaller chunks
   - If formatting issue → apply corrections and retry

3. **RETRY the step:**
   - Apply the fix
   - Re-execute the failed operation
   - Validate the results

4. **ONLY STOP if:**
   - ❌ Error persists after 3 fix attempts
   - ❌ Root cause is unclear/unknown
   - ❌ Fix would require human decision-making
   - ❌ Data integrity would be compromised

5. **IF STOPPING, report:**
   - Which protocol failed
   - What attempts were made to fix
   - Why the error couldn't be resolved
   - Current state of output files
   - Mark as FAILED in BATCH-PROGRESS-SUMMARY.md

### If Validation Fails:
1. **ANALYZE the validation failure:**
   - Check content inventory counts
   - Compare original vs reformatted
   - Identify missing or changed content

2. **ATTEMPT to FIX:**
   - If content missing → regenerate that section
   - If format incorrect → reapply correct format
   - If counts mismatch → verify and correct inventory

3. **RETRY validation:**
   - Re-run validation checks
   - Confirm 100% content preservation

4. **ONLY STOP if:**
   - Content cannot be preserved accurately
   - Validation fails after multiple fix attempts
   - Structural integrity compromised

**Philosophy:** Be resilient and self-healing. Most errors are fixable through analysis and retry. Only escalate when truly stuck.

---

## 📁 Output Directory Structure Verification

After each step, verify this structure exists:

```
.artifacts/protocol-reformat/[protocol-stem]/
├── ORIGINAL-BACKUP.md          ← Exact copy of original
├── CONTENT-INVENTORY.json      ← Content element counts
├── FORMAT-ANALYSIS.md          ← Format decisions documented
├── REFORMATTED-PART1.md        ← Reformatted chunks (if large)
├── REFORMATTED-PART2.md        ← (if needed)
├── REFORMATTED.md              ← Final merged output
├── format-changes.diff         ← Structural changes only
└── validation-report.md        ← 100% preservation proof
```

**[STRICT]** If this structure is incomplete, the step is NOT complete.

---

## ✅ Success Criteria Checklist

For each protocol, confirm:

- [ ] Protocol file read successfully
- [ ] Command executed without errors
- [ ] Output directory created
- [ ] ORIGINAL-BACKUP.md exists and matches source
- [ ] CONTENT-INVENTORY.json generated with accurate counts
- [ ] FORMAT-ANALYSIS.md documents all format decisions
- [ ] REFORMATTED.md generated (merged if multi-part)
- [ ] format-changes.diff shows structural changes only
- [ ] validation-report.md confirms 100% content preservation
- [ ] BATCH-PROGRESS-SUMMARY.md updated with completion
- [ ] All automation hooks intact
- [ ] No content loss or modification detected

**[STRICT]** ALL checkboxes must be checked before proceeding to next step.

---

## 🎯 Completion Goal

The batch reformat is **COMPLETE** only when:

1. All 22 protocols (02-23) show ✅ COMPLETE status
2. BATCH-PROGRESS-SUMMARY.md shows "Completed: 22"
3. All validation reports confirm 100% content preservation
4. No protocols marked as FAILED or IN PROGRESS

---

## 🔧 Command Reference

**To execute batch reformat:**
1. Read the file: `.cursor/commands/batch-reformat-02-to-23.md`
2. Follow each step sequentially as instructed

**To check progress:**
```bash
cat /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts/protocol-reformat/BATCH-PROGRESS-SUMMARY.md
```

**To verify specific protocol:**
```bash
ls -la /home/haymayndz/AI-DRIVEN-TEMPLATE-TESTING/.artifacts/protocol-reformat/[protocol-stem]/
```

---

## 💡 Remember

- **Quality over speed** - Take time to ensure each step is perfect
- **One step at a time** - No shortcuts, no parallelization
- **Always update progress** - After every single step
- **Validate before proceeding** - Confirm success before moving on
- **Be resilient on errors** - Analyze, fix, and retry before escalating
- **Self-healing approach** - Most errors are fixable, only stop when truly stuck

**These rules exist to prevent token overflow, ensure data integrity, and maintain process traceability while allowing intelligent error recovery.**

---

## 📝 Last Updated
- Document Version: 1.1
- Last Modified: 2025-10-29
- Changes: Added intelligent error recovery protocol (analyze, fix, retry before stopping)
- Purpose: Ensure strict sequential execution of batch protocol reformat operations with resilient error handling

