# 🔮 Cursor Prompts - AI Governor Framework

## ⚡ **NEW: UNIFIED `/review` COMMAND**

**Single entry point with intelligent protocol selection!**

The core review system now uses **unified `/review` orchestrator** with **interactive protocol selection** and **automatic custom/generic fallback**.

```bash
# Single command - interactive selection via AI Governor
@review

# Will show:
☐ Code Review - DDD compliance + Code quality
☐ 🚀 Run All (Comprehensive Quality Gate)  
☐ Security Check - Multi-tenant validation
☐ Architecture Review - Performance validation
☐ Design System Compliance - Visual consistency
☐ UI/UX & Accessibility - WCAG + Responsive
☐ Pre-Production Security - Complete validation
```

## 📋 Overview

These prompts enable using the **AI Governor Framework** directly in **Cursor** via `@prompt-name` interface. They use the **centralized quality audit** with **automatic fallback** for tool-agnostic access to review and validation protocols.

## 🎯 Available Prompts

### Core Review Prompts

| Prompt | Usage | Mode 4-quality-audit | Fallback Logic |
|--------|-------|---------------------|----------------|
| `@review` | **UNIFIED ENTRY POINT** with interactive selection | All modes via selection | Custom → Generic automatic fallback |
| `@security` | Direct security audit | Mode: `security` | `custom/microsaas-security-check.md` → `security-check.md` |
| `@architecture-validator` | Architecture deep analysis | Mode: `architecture` | `custom/microsaas-architecture-review.md` → `architecture-review.md` |
| `@security-auditor` | Comprehensive security audit | Mode: `deep-security` | `custom/microsaas-pre-production.md` → `pre-production.md` |

### Integration with Cursor Features

#### Context Integration
```bash
# UNIFIED ENTRY POINT - Interactive selection
@review @codebase

# Direct security check for auth/data changes
@security @recent-changes

# Architecture validation for service changes
@architecture-validator @services/auth/src/index.ts

# Comprehensive security audit
@security-auditor @services/billing @apps/gateway
```

#### Composer Mode
```bash
# Apply suggestions automatically from unified review
@review fix issues found

# Implement architecture improvements
@architecture-validator implement suggestions

# Apply security recommendations
@security implement security fixes
```

## 🔄 Workflow Integration

### During Development (Inner Loop)
```bash
# Quick check after features (unified interface)
@review

# Security validation before commit
@security @recent-changes
```

### Post-Implementation (Outer Loop)
```bash
# Comprehensive quality gate
@review
# → Select "🚀 Run All (Comprehensive Quality Gate)"

# Architecture validation for service changes
@architecture-validator @services

# Pre-production security validation
@security-auditor @codebase
```

## 🎪 Usage Examples

### Feature Development - Authentication
```bash
# During implementation
@review
# → Select "Code Review" to check JWT validation implementation

# Security audit post-implementation  
@security audit authentication flow for multi-tenant compliance

# Architecture validation
@architecture-validator validate auth service bounded context integrity
```

### Feature Development - Billing  
```bash
# Quick review with interactive selection
@review @recent-changes
# → Select "Code Review + Security Check"

# Comprehensive security audit
@security-auditor check payment data isolation and RLS policies
```

## 🛠️ Configuration and Setup

### Cursor Settings
```json
{
  "cursor.enablePrompts": true,
  "cursor.promptPaths": [".cursor/prompts/"],
  "cursor.autoContext": ["@codebase", "@recent-changes"]
}
```

### Project Integration
1. **Automatic discovery**: Prompts auto-detected from `.cursor/prompts/`
2. **Context awareness**: Integration with `@codebase` and `@recent-changes`
3. **Tool-agnostic**: Direct reference to AI Governor protocols
4. **Centralized router**: Automatic custom → generic fallback via `_review-router.md`

## 🎯 Master Rules Compliance

All prompts rigorously respect:
- **Master Rule 0**: DDD Bounded Contexts and Ubiquitous Language
- **Master Rule 3**: Code Quality standards (error handling, SRP, naming)
- **Common Rule**: Service Bindings RPC (no HTTP between Workers)
- **Monorepo Setup**: Clean apps/services/libs structure

## 🚀 Cursor-Specific Advantages

✅ **Native Integration**: Familiar `@prompt-name` syntax  
✅ **Context Aware**: Auto-integration with `@codebase`, `@recent-changes`  
✅ **Composer Compatible**: Suggestions directly applicable  
✅ **Multi-file Analysis**: Support for patterns `@services/*`, `@apps/*`  
✅ **Tool Agnostic**: Same logic as Claude Code, Aider, Continue.dev  
✅ **Unified Interface**: Single `/review` command with interactive selection
✅ **Smart Fallback**: Custom protocols when available, generic always work

## 📊 Performance Tips

### For Solo Teams
```bash
# Focus on speed + learning
@review after each commit (select "Code Review")
@review for parent tasks (select "🚀 Run All")
```

### For 2-3 Person Teams
```bash
# Balance structure + flexibility  
@security before PR
@review comprehensive during pair-programming
```

### For 4+ Person Teams  
```bash
# Rigorous process + standardization
@review comprehensive mandatory (select "🚀 Run All")
@architecture-validator for architectural changes
```

## 🆕 **NEW: Auto-Customization**

**Zero-config setup for any project:**
```bash
# Generate custom protocols fitted to your project
Apply instructions from .cursor/ai-driven-workflow/review-protocols/custom/customize-review-protocols.md

# This will:
# 1. Analyze your Master Rules, stack, and domain
# 2. Generate 6 custom protocols perfectly fitted to your project
# 3. Update router to use custom protocols automatically
# 4. Provide verification checklist
```

---

**🎉 Result**: Native integration of **AI Governor Framework** in **Cursor** with **intelligent automatic fallback** providing access to DDD validation protocols via familiar `@prompt` syntax. **Degraded mode** (generic) AND **optimized mode** (custom) based on context. **Superior to Anthropic's approach** with unified interface and zero-config customization.