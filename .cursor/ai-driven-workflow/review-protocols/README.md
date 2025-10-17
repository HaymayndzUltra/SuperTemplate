# 🔍 AI Governor Review Protocols - Revolutionary Unified System

## ⚡ **NEW: UNIFIED `/review` ORCHESTRATOR**

**A single, central orchestrator for all quality audits!**

These protocols define the **revolutionary core logic** for AI code reviews, all driven by the **central `4-quality-audit.md` orchestrator**. This system provides an **interactive protocol selection** interface with **automatic custom/generic fallback**. It is **tool-agnostic** and **superior to Anthropic's approach**.

## 🎯 Revolutionary Philosophy

**Enhanced Separation of Responsibilities:**
- **review-protocols/** = The library of specialized business intelligence protocols (DDD, architecture, security).
- **Tool adapters** = Interface specific (`.claude/`, `.cursor/`, etc.) pointing to the central orchestrator.
- **`../4-quality-audit.md`** = The strategic orchestrator and quality audit engine.
- **Centralized router** = Automatic protocol selection and fallback logic.

## 📁 Unified Protocol Architecture

### **🎯 MAIN ORCHESTRATOR**
- **`../4-quality-audit.md`** - **EXECUTION ENGINE & UNIFIED ENTRY POINT** - 6-layer quality audit with multiple modes, interactive selection, and smart recommendations.

### **🔧 Enhanced Static Review Utilities**
- **`utils/_review-router.md`** - **CENTRALIZED ROUTER** - Automatic custom ↔ generic fallback logic
- **`utils/context-analyzer.md`** - **CONTEXT INTELLIGENCE** - Git change analysis + smart recommendations
- **`utils/rule-injection-system.md`** - **RULE FILTERING** - 40% efficiency gains through targeted validation
- **`utils/enhanced-static-validation.md`** - **VALIDATION FRAMEWORK** - Testing and performance metrics

### **Generic Protocols (Universal DDD - Always Available)**
- **`code-review.md`** - DDD compliance + Code quality core (Mode: `quick`)
- **`security-check.md`** - Security + Bounded Context boundaries (Mode: `security`)
- **`architecture-review.md`** - DDD + Performance architecture (Mode: `architecture`)
- **`design-system.md`** - Component usage + Visual consistency (Mode: `design`)
- **`ui-accessibility.md`** - Accessibility + User experience validation (Mode: `ui`)
- **`pre-production.md`** - Complete security validation with testing (Mode: `deep-security`)

### **Custom Stack-Specific Protocols (Enhanced When Available)**
- **`custom/custom_code-review.md`** - Cloudflare Workers + Supabase optimized
- **`custom/custom_security-check.md`** - Service Bindings + RLS specific
- **`custom/custom_architecture-review.md`** - Workers architecture specific
- **`custom/custom_design-system.md`** - MicroSaaS design patterns specific
- **`custom/custom_ui-accessibility.md`** - SaaS UI/UX + multi-tenant accessibility
- **`custom/custom_pre-production.md`** - Full stack security assessment

## 🔧 Revolutionary Tool Integration (Unified `/review` & `@review`)

**BREAKTHROUGH**: All tools now use the **central orchestrator** for an interactive experience with automatic fallback:

### Claude Code (Revolutionary)
```bash
# UNIFIED ENTRY POINT - Interactive selection
/review
# → Calls 4-quality-audit.md, which shows interactive protocol selection
# → Context-aware recommendations
# → Automatic custom ↔ generic fallback

# Direct commands for specific needs
/security             # Direct security audit (mode: security)
/architecture-validator # Deep architecture analysis (mode: architecture)
/security-auditor     # Comprehensive security audit (mode: deep-security)

# Direct mode execution (for automation)
Apply instructions from .cursor/ai-driven-workflow/4-quality-audit.md --mode [quick|security|architecture|design|ui|deep-security|comprehensive]
```

### Cursor (Enhanced)
```bash
# UNIFIED ENTRY POINT via Cursor prompts
@review
# → Calls 4-quality-audit.md, which shows interactive protocol selection
# → Automatic custom ↔ generic fallback

# Direct mode execution
@apply .cursor/ai-driven-workflow/4-quality-audit.md --mode [quick|security|architecture|design|ui|deep-security|comprehensive]
```

### Aider (Streamlined)
```python
# Unified review interface by loading the orchestrator
/load .cursor/ai-driven-workflow/4-quality-audit.md
# → The orchestrator will then prompt for the mode
```

### **🤖 Intelligent Fallback Logic (Automatic)**
```bash
# The router, called by the orchestrator, automatically selects the best protocol for each mode:
Mode: quick → custom/custom_code-review.md ↔ code-review.md
Mode: security → custom/custom_security-check.md ↔ security-check.md  
Mode: architecture → custom/custom_architecture-review.md ↔ architecture-review.md
Mode: design → custom/custom_design-system.md ↔ design-system.md
Mode: ui → custom/custom_ui-accessibility.md ↔ ui-accessibility.md
Mode: deep-security → custom/custom_pre_production.md ↔ pre-production.md
Mode: comprehensive → 4-quality-audit.md (orchestrator - all layers)
```

## 🎪 Revolutionary Dev-Workflow Integration

The unified protocols are automatically integrated into:
- **Protocol 3** (Implementation) → `/review` or `@review` for interactive selection during coding
- **Protocol 4** (Quality Audit) → **CENTRALIZED ORCHESTRATOR** with 6-layer validation  
- **Enhanced Workflow** → Fewer steps with superior UX

## 📊 Master Rules Compliance

All protocols rigorously respect:
- **`0-master-rule-architectural-principles.mdc`** → Domain-Driven Design (DDD)
- **`3-master-rule-code-quality-checklist.md`** → Quality standards
- **`common-rule-cloudflare-service-bindings.mdc`** → Service Bindings RPC
- **`common-rule-monorepo-setup-conventions.mdc`** → apps/services/libs structure

## 🆕 **NEW: Auto-Customization**

### Zero-Config Project Setup
```bash
# Generate custom protocols fitted to any project
Apply instructions from .cursor/ai-driven-workflow/review-protocols/custom/customize-review-protocols.md

# Automatic analysis and generation:
# 1. Analyze Master Rules, technology stack, domain context
# 2. Generate 6 custom protocols perfectly fitted to project
# 3. Update router for automatic custom → generic fallback
# 4. Provide verification and testing checklist
```

### Adding New Protocols
1. **Generic Version**: Create `new-protocol.md` - Tool-agnostic, universal patterns
2. **Stack-Specific Version**: Create `custom/project-new-protocol.md` - Platform/tech-specific
3. **Update Router**: Add mapping in `_review-router.md`
4. **Tool Integration**: The central orchestrator will automatically pick up the new mode if the router is updated.

### Modifying Existing Protocols  
1. **Generic protocols** (root): Modify for universal compatibility
2. **Stack-specific protocols** (`custom/`): Adapt for your stack
3. **Automatic propagation** to all tools via centralized system
4. **Single source of truth** = zero duplication

## 🎯 Revolutionary Advantages

✅ **Unified Interface**: Single `/review` or `@review` command  
✅ **Intelligent Fallback**: Automatic custom ↔ generic protocol selection  
✅ **Context Awareness**: Smart recommendations based on file changes  
✅ **Tool Agnostic**: Same experience across Claude Code, Cursor, Aider  
✅ **Zero Configuration**: Auto-customization for any project  
✅ **Superior UX**: Simplified UX over multi-command approaches  
✅ **GitHub Actions**: Smart automation with context detection  
✅ **6-Layer Validation**: Enhanced coverage including Design + UX  
✅ **Open Source Ready**: Generic protocols work standalone  
✅ **Maintenance Optimized**: Centralized logic, no duplication  

## 🆚 **Superiority vs Anthropic**

| **Aspect** | **Anthropic** | **AI Governor** | **Winner** |
|------------|---------------|-----------------|-------------|
| **Interface** | Multiple commands | Unified `/review` | 🏆 **US** |
| **Protocol Coverage** | 3/6 domains | 6/6 domains | 🏆 **US** |
| **Customization** | Manual setup | Auto-customization | 🏆 **US** |
| **Tool Support** | Claude only | Multi-tool agnostic | 🏆 **US** |
| **CI/CD** | Basic GitHub Actions | Smart context detection | 🏆 **US** |
| **Fallback System** | None | Intelligent custom→generic | 🏆 **US** |

---

**🎉 REVOLUTIONARY RESULT**: A **superior-to-Anthropic** AI code review platform with a **unified `/review` interface**, **intelligent protocol selection**, **automatic customization**, and **tool-agnostic design**. Achieves **faster development velocity** while maintaining **highest quality standards** with **zero configuration** for any project. **The future of AI-powered code review is here**.

---

## Folder Overview and Evidence References

### Directory structure (subset)
- `README.md` – This overview and integration details
- `code-review.md` – Generic DDD/code-quality protocol
- `security-check.md` – Security-focused validation
- `architecture-review.md` – Architecture/performance validation
- `design-system.md` – Design system checks
- `ui-accessibility.md` – UX/a11y checks
- `pre-production.md` – Deep security validation
- `utils/` – Orchestration utilities and router logic

### How this folder is used by the orchestrator
- Entry point `../4-quality-audit.md` routes to protocols here based on selected mode and availability of custom variants.
- Router logic lives in `utils/_review-router.md` and performs custom↔generic fallback.

### Evidence (code references)

```19:26:/home/haymayndz/ai-driven-template/.cursor/ai-driven-workflow/review-protocols/README.md
### **🔧 Enhanced Static Review Utilities**
- **`utils/_review-router.md`** - **CENTRALIZED ROUTER** - Automatic custom ↔ generic fallback logic
- **`utils/context-analyzer.md`** - **CONTEXT INTELLIGENCE** - Git change analysis + smart recommendations
```

```20:25:/home/haymayndz/ai-driven-template/.cursor/ai-driven-workflow/README.md
### Step 3: Execute Tasks with Integrated Quality Gates
... **Apply instructions from ai-driven-workflow/4-quality-audit.md**
```