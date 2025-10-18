# TEMPLATE: Enhanced Static Protocol for MicroSaaS Custom Protocols

## 🎯 Template Structure

Use this template to update all `custom_*.md` files with Enhanced Static Review approach.

### **Header Template**
```markdown
# ENHANCED STATIC PROTOCOL: MicroSaaS [PROTOCOL_NAME] (Cloudflare Workers + Supabase)

## ⚡ **ENHANCED STATIC REVIEW WITH MICROSAAS INTELLIGENCE**

**Revolutionary approach**: Combines **proven static protocol reliability** with **intelligent MicroSaaS-specific targeting** for Cloudflare Workers + Supabase stack.

**Enhanced Execution Mode**: `[MODE]` (Context-Enhanced)
- **Layers**: [SPECIFIC_LAYERS]
- **Enhanced Duration**: [OLD_DURATION] → [NEW_DURATION] (40% faster with smart targeting)
- **Usage**: [SPECIFIC_USAGE] with intelligent context analysis

## 🧠 Context Analysis for MicroSaaS

**Enhanced Intelligence**: This protocol automatically analyzes your git changes for MicroSaaS-specific patterns:

```typescript
interface MicroSaaSContext {
  workerServices: boolean;     // services/, workers/ file changes
  supabaseIntegration: boolean; // supabase/, database/ changes  
  serviceBindings: boolean;    // wrangler.toml, service communications
  multiTenantAuth: boolean;    // auth/, tenant/, RLS changes
  edgeComputing: boolean;      // edge-specific optimizations
  [SPECIFIC_CONTEXT]: boolean; // protocol-specific context
}
```

**Smart Recommendations**: 
- **[CONTEXT_1]** → [RECOMMENDATION_1]
- **[CONTEXT_2]** → [RECOMMENDATION_2]
- **[CONTEXT_3]** → [RECOMMENDATION_3]

## 🎯 Enhanced MicroSaaS-Specific Validation

### **Rule Injection for MicroSaaS Stack**

**Smart Rule Filtering**: Based on detected context, prioritize relevant validation rules:

**Critical Rules (Always Apply)**:
- **Master Rule: Error Handling** - All I/O operations in try/catch (Cloudflare Workers requirement)
- **Master Rule: Code Quality** - Functions <30 lines, explicit naming for Workers environment  
- **Common Rule: Service Bindings** - Mandatory for Worker-to-Worker communication

**Context-Triggered Rules**:
- **[PROTOCOL_CONTEXT]** → [SPECIFIC_RULES]
- **Workers Context** → Edge performance optimization, cold start minimization
- **Supabase Context** → Multi-tenant RLS compliance, database security patterns

**Enhanced Execution Instructions**:
1. **Execute Critical Rules First** - Worker reliability foundation
2. **Apply Context Rules** - [PROTOCOL]-specific targeting  
3. **Skip Irrelevant Checks** - Don't validate non-[PROTOCOL] patterns
4. **Deep Dive Focus Areas** - [FOCUS_AREAS]

## 📋 Static Protocol Framework (MicroSaaS Enhanced)

### **Layer X: [PROTOCOL_LAYER] (Enhanced for MicroSaaS)**

[EXISTING_CONTENT_ENHANCED]
```

### **Footer Template**
```markdown
---

## 🚀 **ENHANCED STATIC BENEFITS FOR MICROSAAS**

**🎯 Context-Aware Intelligence:**
- **40% more efficient** through MicroSaaS-specific rule filtering
- **Smart recommendations** based on Cloudflare Workers + Supabase patterns
- **Targeted validation** focusing on [PROTOCOL_FOCUS]
- **[SPECIFIC_BENEFIT]** with context detection

**🛡️ Proven Reliability + MicroSaaS Intelligence:**
- **Static protocol foundation** ensures comprehensive validation coverage
- **Enhanced with context analysis** for intelligent targeting of MicroSaaS patterns
- **Graceful degradation** to static validation when context analysis fails
- **Cloudflare Workers + Supabase specialization** without losing universal DDD principles

**🎉 Result**: Revolutionary **Enhanced Static Review** specifically optimized for MicroSaaS architecture with **[SPECIFIC_OPTIMIZATION]** while maintaining **proven [PROTOCOL] compliance** reliability.
```

## 📋 Protocol-Specific Mappings

### **custom_security-check.md**
- PROTOCOL_NAME: "Security Check"
- MODE: "security"
- SPECIFIC_LAYERS: "LAYER 2 (Security & Multi-tenant) + LAYER 1 (DDD Boundaries)"
- PROTOCOL_CONTEXT: "Security Context"
- SPECIFIC_RULES: "Multi-tenant RLS, JWT validation, secrets management"
- FOCUS_AREAS: "Service Bindings security, RLS policies, tenant isolation"

### **custom_architecture-review.md**
- PROTOCOL_NAME: "Architecture Review"
- MODE: "architecture"
- SPECIFIC_LAYERS: "LAYER 1 (DDD Compliance) + LAYER 4 (Architecture & Performance)"
- PROTOCOL_CONTEXT: "Architecture Context"
- SPECIFIC_RULES: "Service boundaries, performance patterns, scalability"
- FOCUS_AREAS: "Bounded Contexts, Workers performance, edge architecture"

### **custom_design-system.md**
- PROTOCOL_NAME: "Design System Compliance"
- MODE: "design"
- SPECIFIC_LAYERS: "LAYER 5 (Design System) + LAYER 1 (Component Architecture)"
- PROTOCOL_CONTEXT: "Design Context"
- SPECIFIC_RULES: "Component library compliance, design token usage"
- FOCUS_AREAS: "Design tokens, component consistency, brand guidelines"

### **custom_ui-accessibility.md**
- PROTOCOL_NAME: "UI/UX & Accessibility"
- MODE: "ui"
- SPECIFIC_LAYERS: "LAYER 6 (UI/UX & Accessibility) + LAYER 1 (DDD)"
- PROTOCOL_CONTEXT: "Accessibility Context"
- SPECIFIC_RULES: "WCAG compliance, multi-tenant UX patterns"
- FOCUS_AREAS: "Accessibility, responsive design, multi-tenant UX"

### **custom_pre-production.md**
- PROTOCOL_NAME: "Pre-Production Security"
- MODE: "deep-security"
- SPECIFIC_LAYERS: "LAYER 2 + LAYER 1 + LAYER 7 (Complete validation)"
- PROTOCOL_CONTEXT: "Pre-Production Context"
- SPECIFIC_RULES: "Comprehensive security validation, deployment readiness"
- FOCUS_AREAS: "Production security, performance validation, compliance"