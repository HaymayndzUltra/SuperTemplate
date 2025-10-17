# Quick Start: Protocol & Analysis Generators

## 🚀 TLDR: Dalawang Main Tools

### 1. **Meta-Analysis Generator** 
Gumawa ng analysis mula sa existing protocol
```
Protocol → Analysis
```

### 2. **Protocol Generator**
Gumawa ng bagong protocol mula sa requirements
```
Requirements Form → Protocol
```

---

## 📋 HOW TO: Generate Meta-Analysis

### Step 1: Identify Source Protocol
```
Example: .cursor/ai-driven-workflow/0-bootstrap-your-project.md
```

### Step 2: Tell AI to Use Meta-Analysis Generator
```
"Generate meta-analysis for 0-bootstrap-your-project.md 
using meta-analysis-generator-instructions.md"
```

### Step 3: AI Outputs
```
analysis-0-bootstrap-your-project.md

Contains:
✓ Phase Map (4 layers)
✓ Meta-Architecture Diagram
✓ Commentary
✓ Inference Summary
✓ Output Instructions
```

---

## 📝 HOW TO: Generate New Protocol

### Step 1: Copy Template Form
```
cp protocol-input-form.yaml my-protocol-form.yaml
```

### Step 2: Fill Out Form
```yaml
protocol_number: "7"
protocol_name: "my-new-protocol"
domain_compliance: "Domain"
ai_role: "AI Role"
# ... fill all required fields
```

**Tip:** Look at `sample-filled-form.yaml` for example

### Step 3: Tell AI to Generate Protocol
```
"Generate protocol using protocol-generator-instructions.md 
with my-protocol-form.yaml"
```

### Step 4: AI Outputs
```
7-my-new-protocol.md

Contains:
✓ AI Role & Mission
✓ Execution Steps (with phases)
✓ Integration Points
✓ Quality Gates
✓ Communication Protocols
✓ Handoff Checklist
```

### Step 5: Validate (Automatic)
AI automatically runs circular validation:
```
Generated Protocol → Meta-Analysis Generator → Validation Report

If PASS ✓ → Protocol is ready
If FAIL ✗ → AI regenerates with fixes
```

---

## 🔄 CIRCULAR VALIDATION FLOW

```
┌─────────────────┐
│   Fill Form     │
│ (YAML file)     │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│ AI Generates    │
│   Protocol      │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│ AI Validates    │
│ with Meta-      │
│ Analysis Gen.   │
└────────┬────────┘
         │
         ↓
    ┌────┴────┐
    │  PASS?  │
    └────┬────┘
         │
    ┌────┴────┐
    │         │
   YES       NO
    │         │
    ↓         ↓
 DELIVER   REGENERATE
           (with fixes)
```

---

## 📁 FILE QUICK REFERENCE

### Main Instructions
| File | Use When |
|------|----------|
| `meta-analysis-generator-instructions.md` | Analyzing existing protocols |
| `protocol-generator-instructions.md` | Creating new protocols |

### Templates & Examples
| File | Use When |
|------|----------|
| `protocol-input-form.yaml` | Template for new protocol requirements |
| `sample-filled-form.yaml` | Example of filled form |
| `6-deployment-automation.md` | Example generated protocol |
| `analysis-6-deployment-automation.md` | Example generated analysis |

### Summary
| File | Use When |
|------|----------|
| `GENERATOR-SYSTEM-SUMMARY.md` | Full system documentation |
| `QUICK-START-GENERATORS.md` | Quick start guide (this file) |

---

## 💡 COMMON TASKS

### Task 1: Analyze All Existing Protocols
```
For each protocol in .cursor/ai-driven-workflow/:
1. Tell AI: "Generate meta-analysis for [protocol-name].md"
2. AI outputs: analysis-[protocol-name].md
3. Review analysis for insights
```

### Task 2: Create Protocol Series
```
1. Fill form for Protocol 7
2. AI generates Protocol 7
3. AI validates Protocol 7
4. Fill form for Protocol 8 (using Protocol 7 output as input)
5. AI generates Protocol 8
6. Repeat as needed
```

### Task 3: Validate Protocol Quality
```
1. You have: custom-protocol.md
2. Tell AI: "Run meta-analysis on custom-protocol.md"
3. AI outputs: analysis-custom-protocol.md
4. Check if all 4 layers present:
   - Layer 1: System-Level Decisions ✓
   - Layer 2: Behavioral Control ✓
   - Layer 3: Procedural Logic ✓
   - Layer 4: Communication Grammar ✓
5. If all present → Protocol is valid
6. If missing → Protocol needs restructuring
```

---

## ⚙️ FORM FILLING TIPS

### Required Fields (Cannot be empty)
- `protocol_number` - Sequential number
- `protocol_name` - Kebab-case name
- `domain_compliance` - Domain tag
- `purpose` - 1-2 sentence mission
- `ai_role` - AI persona
- `phases` - At least 1 phase with steps
- `integration` - Inputs/outputs
- `communication` - Templates

### Optional but Recommended
- `automation_hooks` - Scripts to run
- `error_handling` - Failure scenarios
- `special_considerations` - Unique requirements

### Pro Tips
1. **Copy from sample-filled-form.yaml** - Easier than starting from scratch
2. **One phase at a time** - Don't overwhelm, start small
3. **Reference existing protocols** - See how others structured phases
4. **Test circular validation** - Always validate generated protocol

---

## 🎯 SUCCESS CHECKLIST

### For Meta-Analysis Generation
- [ ] Source protocol identified
- [ ] AI used meta-analysis-generator-instructions.md
- [ ] Output has all 5 sections
- [ ] All 4 layers present
- [ ] ASCII diagram formatted correctly
- [ ] Line references accurate

### For Protocol Generation
- [ ] Form completely filled
- [ ] AI used protocol-generator-instructions.md
- [ ] Output matches existing protocol format
- [ ] All required sections present
- [ ] Circular validation passed
- [ ] Ready for use in workflow

---

## 🆘 TROUBLESHOOTING

### Problem: Generated protocol doesn't pass validation
**Solution:** Check form completeness, ensure all phases have proper structure

### Problem: Meta-analysis missing layers
**Solution:** Source protocol may not have clear structure, try different protocol first

### Problem: AI confused about which generator to use
**Solution:** Be explicit: "Use [generator-name].md to [action]"

### Problem: Form too complex to fill
**Solution:** Start with sample-filled-form.yaml, modify instead of creating from scratch

---

## 🎉 YOU'RE READY!

**To generate meta-analysis:**
```
"Generate meta-analysis for [protocol].md 
using meta-analysis-generator-instructions.md"
```

**To generate new protocol:**
```
1. Fill: protocol-input-form.yaml
2. Say: "Generate protocol from filled form 
   using protocol-generator-instructions.md"
```

**Simple as that!** 🚀

---

**Need detailed explanation?** → Read `GENERATOR-SYSTEM-SUMMARY.md`
**Need examples?** → See `sample-filled-form.yaml` and `6-deployment-automation.md`
**Need validation?** → Check `analysis-6-deployment-automation.md`
