# 🎯 Centralized Review Router

**REVOLUTIONARY**: This router provides **intelligent custom ↔ generic fallback logic** for the unified `/review` orchestrator.

## Router Logic

**IMPORTANT**: This file implements the automatic fallback logic used by all tool adapters and GitHub Actions workflows.

### Step 1: Environment Detection
```bash
# Check if custom/ folder exists
CUSTOM_DIR=".ai-governor/dev-workflow/review-protocols/custom/"
GENERIC_DIR=".ai-governor/dev-workflow/review-protocols/"

if [[ -d "$CUSTOM_DIR" ]]; then
    echo "✅ Custom protocols directory detected"
    CUSTOM_AVAILABLE=true
else
    echo "ℹ️ No custom protocols directory - using generic fallback"
    CUSTOM_AVAILABLE=false
fi
```

### Step 2: Protocol-Specific Selection

#### Code Review Protocol
```bash
PROTOCOL_NAME="code-review"
CUSTOM_FILE="${CUSTOM_DIR}custom_code-review.md"
GENERIC_FILE="${GENERIC_DIR}code-review.md"

if [[ $CUSTOM_AVAILABLE == true && -f "$CUSTOM_FILE" ]]; then
    echo "🎯 Using CUSTOM: $CUSTOM_FILE (Stack-specific optimized)"
    SELECTED_PROTOCOL="$CUSTOM_FILE"
else
    echo "🌐 Using GENERIC: $GENERIC_FILE (Universal DDD patterns)"
    SELECTED_PROTOCOL="$GENERIC_FILE"
fi
```

#### Security Check Protocol
```bash
PROTOCOL_NAME="security-check"
CUSTOM_FILE="${CUSTOM_DIR}custom_security-check.md"
GENERIC_FILE="${GENERIC_DIR}security-check.md"

if [[ $CUSTOM_AVAILABLE == true && -f "$CUSTOM_FILE" ]]; then
    echo "🎯 Using CUSTOM: $CUSTOM_FILE (Stack-specific security patterns)"
    SELECTED_PROTOCOL="$CUSTOM_FILE"
else
    echo "🌐 Using GENERIC: $GENERIC_FILE (Universal security patterns)"
    SELECTED_PROTOCOL="$GENERIC_FILE"
fi
```

#### Architecture Review Protocol
```bash
PROTOCOL_NAME="architecture-review"
CUSTOM_FILE="${CUSTOM_DIR}custom_architecture-review.md"
GENERIC_FILE="${GENERIC_DIR}architecture-review.md"

if [[ $CUSTOM_AVAILABLE == true && -f "$CUSTOM_FILE" ]]; then
    echo "🎯 Using CUSTOM: $CUSTOM_FILE (Workers architecture specific)"
    SELECTED_PROTOCOL="$CUSTOM_FILE"
else
    echo "🌐 Using GENERIC: $GENERIC_FILE (Universal multi-service architecture)"
    SELECTED_PROTOCOL="$GENERIC_FILE"
fi
```

#### Pre-Production Security Protocol
```bash
PROTOCOL_NAME="pre-production"
CUSTOM_FILE="${CUSTOM_DIR}custom_pre-production.md"
GENERIC_FILE="${GENERIC_DIR}pre-production.md"

if [[ $CUSTOM_AVAILABLE == true && -f "$CUSTOM_FILE" ]]; then
    echo "🎯 Using CUSTOM: $CUSTOM_FILE (Cloudflare + Supabase security stack)"
    SELECTED_PROTOCOL="$CUSTOM_FILE"
else
    echo "🌐 Using GENERIC: $GENERIC_FILE (Universal deep security patterns)"
    SELECTED_PROTOCOL="$GENERIC_FILE"
fi
```

#### Design System Protocol
```bash
PROTOCOL_NAME="design-system"
CUSTOM_FILE="${CUSTOM_DIR}custom_design-system.md"
GENERIC_FILE="${GENERIC_DIR}design-system.md"

if [[ $CUSTOM_AVAILABLE == true && -f "$CUSTOM_FILE" ]]; then
    echo "🎯 Using CUSTOM: $CUSTOM_FILE (MicroSaaS design system specific)"
    SELECTED_PROTOCOL="$CUSTOM_FILE"
else
    echo "🌐 Using GENERIC: $GENERIC_FILE (Universal design system patterns)"
    SELECTED_PROTOCOL="$GENERIC_FILE"
fi
```

#### UI/UX Accessibility Protocol
```bash
PROTOCOL_NAME="ui-accessibility"
CUSTOM_FILE="${CUSTOM_DIR}custom_ui-accessibility.md"
GENERIC_FILE="${GENERIC_DIR}ui-accessibility.md"

if [[ $CUSTOM_AVAILABLE == true && -f "$CUSTOM_FILE" ]]; then
    echo "🎯 Using CUSTOM: $CUSTOM_FILE (MicroSaaS UI/UX + accessibility specific)"
    SELECTED_PROTOCOL="$CUSTOM_FILE"
else
    echo "🌐 Using GENERIC: $GENERIC_FILE (Universal UI/UX accessibility patterns)"
    SELECTED_PROTOCOL="$GENERIC_FILE"
fi
```

## Tool Adapter Integration

### Standard Usage Pattern
```markdown
**IMPORTANT**: This [command/subagent/prompt] uses the centralized router for automatic protocol selection.

**Router**: `.ai-governor/dev-workflow/review-protocols/utils/_review-router.md`

**Execution**: Apply the centralized quality audit with automatic protocol selection:
`.ai-governor/dev-workflow/4-quality-audit.md --mode [MODE]`

The router will automatically:
1. **Detect** if `custom/` folder exists
2. **Check** if specific protocol file exists
3. **Select** appropriate protocol (custom → generic fallback)
4. **Execute** via 4-quality-audit.md orchestrator
```

## Router Logic Summary

| Mode | Custom Protocol | Generic Fallback | Stack Features |
|------|-----------------|------------------|----------------|
| `quick` | `custom/custom_code-review.md` | `code-review.md` | Stack-specific patterns + Service Bindings |
| `security` | `custom/custom_security-check.md` | `security-check.md` | Stack-specific security + data protection |
| `architecture` | `custom/custom_architecture-review.md` | `architecture-review.md` | Stack-specific architecture patterns |
| `design` | `custom/custom_design-system.md` | `design-system.md` | Stack-specific design system + optimization |
| `ui` | `custom/custom_ui-accessibility.md` | `ui-accessibility.md` | Stack-specific UI/UX + accessibility |
| `deep-security` | `custom/custom_pre-production.md` | `pre-production.md` | Stack-specific full security assessment |
| `comprehensive` | `4-quality-audit.md` (orchestrator) | `4-quality-audit.md` (same) | All layers with appropriate fallback |

## Implementation Benefits

### ✅ Centralized Logic
- **Single source of truth** for selection algorithm
- **No duplication** across tool adapters
- **Consistent behavior** everywhere

### ✅ Seamless Fallback
- **Automatic detection** of environment capabilities
- **Graceful degradation** when custom protocols unavailable
- **Zero configuration** required

### ✅ Open Source Ready
- **Generic protocols** work standalone
- **Custom protocols** enhance when available
- **Tool-agnostic** implementation

### ✅ Maintenance Optimized
- **One place** to modify selection logic
- **Easy debugging** of protocol selection
- **Clear documentation** of fallback behavior

## Usage Examples

### Claude Code
```bash
# Router automatically selects appropriate protocol
Apply instructions from .ai-governor/dev-workflow/4-quality-audit.md --mode quick
```

### Cursor
```bash
# Router handles selection transparently
@apply .ai-governor/dev-workflow/4-quality-audit.md --mode security
```

### Result
```
🔍 Router Analysis:
✅ Custom protocols directory detected
🎯 Using CUSTOM: custom/custom_security-check.md (Stack-specific security patterns)
🚀 Executing via 4-quality-audit.md --mode security
```

---

**Focus**: The router ensures **intelligent and transparent selection** of protocols according to the environment, eliminating logic duplication and ensuring a **consistent experience** across all tools.