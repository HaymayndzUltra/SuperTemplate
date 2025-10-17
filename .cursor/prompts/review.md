# ⚡ UNIFIED @review PROMPT (Cursor Integration)

## Revolutionary Interactive Selection with Enhanced Static Review

**IMPORTANT**: This is the **unified @review prompt** that provides interactive protocol selection with **intelligent targeting** and automatic custom/generic fallback.

**Primary Execution**: Apply the Enhanced Static Review orchestrator:

```
@apply .cursor/ai-driven-workflow/review-protocols/review.md
```

**Direct Mode Execution**: For specific targeted reviews:

```
@apply .cursor/ai-driven-workflow/4-quality-audit.md --mode [MODE]
```

The **Enhanced Static Review** system will automatically:
1. **Analyze git changes** for intelligent context detection
2. **Provide smart recommendations** based on detected changes
3. **Present interactive selection** with confidence scoring
4. **Filter relevant rules** for 40% more efficiency
5. **Execute with custom/generic fallback** seamlessly

## Enhanced Context-Aware Usage

### Smart Quick Reviews
```
@review
# → System analyzes changes and provides intelligent recommendations
# → User selects from context-aware suggestions
```

### Targeted Protocol Execution
```
@apply .cursor/ai-driven-workflow/4-quality-audit.md --mode security
# → Enhanced security review with targeted rules
```

### Context-Specific Examples
```
@review @recent-changes
# → Analyzes recent git changes and suggests optimal protocols

@apply .cursor/ai-driven-workflow/4-quality-audit.md --mode quick
# → Fast DDD compliance check with rule filtering
```

## Context Integration for Enhanced Intelligence

When using this prompt in Cursor:

1. **@codebase** - Architectural context for comprehensive analysis
2. **@recent-changes** - Git change analysis for focused scope  
3. **@filename** - File-specific targeted validation
4. **Composer mode** - For applying suggested modifications
5. **Smart recommendations** - Context-aware protocol suggestions

## Enhanced Static Review Benefits

This Enhanced Static Review ensures:
- **Context-aware rule filtering** (40% more efficient)
- **Smart protocol recommendations** with confidence scoring
- **Targeted validation** based on actual changes
- **Maintained reliability** with static protocol foundation
- **Graceful degradation** when enhancement fails

## Example Enhanced Usage Patterns

```
@review
# Git changes detected: auth/, security/ files modified
# 🧠 Smart recommendation: Security Check + Pre-Production Security (95% confidence)
# ⏱️ Estimated duration: 5-8 minutes (focused validation)

@apply .cursor/ai-driven-workflow/4-quality-audit.md --mode design
# UI components modified - enhanced design system compliance validation

@apply .cursor/ai-driven-workflow/review-protocols/review.md
# Full Enhanced Static Review with interactive protocol selection
```