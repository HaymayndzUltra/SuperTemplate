---
name: review
description: Unified AI Governor review with interactive protocol selection (DDD Compliant)
allow_tools:
  - Bash(git diff:*), Bash(git status:*), Bash(git log:*)
  - Read, Glob, Grep, LS, Task
  - mcp__supabase__*
  - mcp__cloudflare-bindings__*
  - mcp__ide__getDiagnostics
---

# ⚡ UNIFIED `/review` COMMAND

**Single entry point with intelligent protocol selection!**

**IMPORTANT**: This is the **revolutionary unified `/review` orchestrator** that provides interactive protocol selection with automatic custom/generic fallback.

**Router**: `.cursor/ai-driven-workflow/review-protocols/_review-router.md`

**Primary Execution**: Apply the unified review orchestrator:
`.cursor/ai-driven-workflow/review-protocols/review.md`

**Alternative Execution**: Direct mode selection via quality audit:
`.cursor/ai-driven-workflow/4-quality-audit.md --mode [MODE]`

The system will automatically:
1. **Present** interactive protocol selection interface
2. **Detect** custom protocols availability  
3. **Select** appropriate protocols (custom → generic fallback)
4. **Execute** via centralized orchestrator
5. **Report** unified results regardless of source

## 🎯 Interactive Protocol Selection

**You will present the user with this selection interface:**

☐ **Code Review** - DDD compliance + Code quality  
☐ **🚀 Run All (Comprehensive Quality Gate)**  
☐ **Security Check** - Multi-tenant validation  
☐ **Architecture Review** - Performance validation  
☐ **Design System Compliance** - Visual consistency  
☐ **UI/UX & Accessibility** - WCAG + Responsive  
☐ **Pre-Production Security** - Complete validation  

**Based on user selection, execute the corresponding mode via:**
`.cursor/ai-driven-workflow/4-quality-audit.md --mode [MODE]`

## 🤖 Execution Mapping

| User Selection | Mode | Execution |
|---------------|------|-----------|
| Code Review | `quick` | DDD compliance + Code quality core |
| Security Check | `security` | Security + Bounded Context boundaries |
| Architecture Review | `architecture` | DDD + Performance architecture |
| Design System Compliance | `design` | Component usage + Visual consistency |
| UI/UX & Accessibility | `ui` | Accessibility + User experience |
| Pre-Production Security | `deep-security` | Complete security validation |
| 🚀 Run All | `comprehensive` | All protocols with intelligent prioritization |

## 🔄 Smart Recommendations

**Provide context-aware suggestions based on git changes:**

- **Recent auth/security files changed** → Suggest: Security Check + Pre-Production Security
- **UI components/design tokens modified** → Suggest: Design System Compliance + UI/UX
- **Architecture/service changes** → Suggest: Architecture Review + Code Review
- **Pre-merge/release context** → Suggest: Run All (Comprehensive)
- **Daily development** → Suggest: Code Review

## 🎯 Unified Output

All selected protocols will generate a **unified report** format regardless of whether custom or generic protocols are used, ensuring consistent results across different project setups.

---

**🚀 Revolutionary DX**: Single `/review` entry point with **intelligent protocol selection**, **automatic fallback**, and **context-aware recommendations**. **Superior to Anthropic's multi-command approach** with **zero learning curve** and **maximum flexibility**.