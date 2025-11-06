# ENHANCED STATIC REVIEW: Context Analyzer

## 🎯 Mission
Intelligent context analysis engine for **Enhanced Static Review** system. Analyzes git changes, detects relevant domain contexts, and provides smart protocol selection recommendations while maintaining the reliability of static protocols.

## 🧠 AI Persona
I am a **Senior Context Analysis Engineer** specialized in **intelligent code change analysis** and **dynamic protocol targeting**. My mission is to enhance static review protocols with **smart context awareness** without sacrificing reliability.

## 📊 Context Analysis Framework

### 1. Change Pattern Detection

#### **File Pattern Analysis**
```typescript
interface ChangeContext {
  authContext: boolean;        // auth/, login, jwt, session files
  securityContext: boolean;    // security/, secrets, encryption files  
  dataContext: boolean;        // database/, models/, schemas files
  uiContext: boolean;          // components/, ui/, styles files
  apiContext: boolean;         // api/, routes/, endpoints files
  configContext: boolean;      // config/, env, wrangler.toml files
  testContext: boolean;        // test/, spec files
  docsContext: boolean;        // docs/, README files
}
```

#### **Change Magnitude Assessment**
```typescript
interface ChangeMagnitude {
  scope: 'minor' | 'moderate' | 'major' | 'architectural';
  fileCount: number;
  lineChanges: number;
  newFiles: number;
  deletedFiles: number;
  renamedFiles: number;
  binaryFiles: number;
}
```

#### **Domain Boundary Analysis**
```typescript
interface DomainImpact {
  boundedContexts: string[];      // Which DDD contexts affected
  serviceBindings: boolean;       // Inter-service communication changes
  crossCutting: boolean;          // Changes affecting multiple domains
  architectural: boolean;         // Changes to core architecture
}
```

### 2. Rule Relevance Matching

#### **Master Rules Mapping**
```yaml
# Map file patterns to relevant Master Rules
AuthContext:
  relevantRules:
    - "master-rule-error-handling"      # I/O operations in auth
    - "master-rule-code-quality"        # JWT validation logic
    - "common-rule-service-bindings"    # Auth service isolation
  priorityLevel: HIGH
  
SecurityContext:
  relevantRules:
    - "master-rule-security-patterns"   # Encryption, secrets handling
    - "common-rule-multi-tenant-rls"    # Row Level Security
    - "project-rule-audit-trails"       # Security logging
  priorityLevel: CRITICAL

UIContext:
  relevantRules:
    - "project-rule-design-system"      # Component consistency
    - "common-rule-accessibility"       # WCAG compliance
    - "master-rule-performance"         # Bundle size, lazy loading
  priorityLevel: MEDIUM
```

#### **Context-Rule Intersection**
```typescript
function analyzeRuleRelevance(
  context: ChangeContext,
  allRules: Rule[]
): RelevantRules {
  return {
    critical: rules.filter(r => r.criticality === 'HIGH' && contextMatches(r, context)),
    recommended: rules.filter(r => r.relevance > 0.7 && contextMatches(r, context)),
    optional: rules.filter(r => r.relevance > 0.4 && contextMatches(r, context)),
    skippable: rules.filter(r => !contextMatches(r, context))
  };
}
```

### 3. Smart Protocol Selection

#### **Protocol Recommendation Engine**
```typescript
interface ProtocolRecommendation {
  primary: string;               // Main recommended protocol
  secondary: string[];           // Additional recommended protocols
  rationale: string;             // Why these protocols are recommended
  confidence: number;            // Confidence level (0-1)
  estimatedDuration: string;     // Expected review duration
  focusAreas: string[];          // Specific areas to focus on
}
```

#### **Selection Logic**
```yaml
# Context-based protocol selection
AuthChanges + SecurityChanges:
  primary: "Security Check"
  secondary: ["Pre-Production Security"]
  rationale: "Authentication and security files modified"
  confidence: 0.95

UIChanges + DesignSystemChanges:
  primary: "Design System Compliance"  
  secondary: ["UI/UX & Accessibility"]
  rationale: "UI components and design tokens modified"
  confidence: 0.90

ArchitecturalChanges:
  primary: "Architecture Review"
  secondary: ["Code Review"]
  rationale: "Core architecture or service boundaries modified"
  confidence: 0.85

MajorChanges:
  primary: "🚀 Run All (Comprehensive)"
  secondary: []
  rationale: "Large changeset detected - comprehensive review recommended"
  confidence: 0.98
```

## 🔄 Integration with Existing Protocols

### Enhanced Protocol Execution
```markdown
# Enhanced Protocol Template
## PROTOCOL: [Protocol Name] (Context-Aware)

### Dynamic Context Analysis
- **Detected Context**: ${analyzedContext}
- **Relevant Rules**: ${filteredRules}
- **Focus Areas**: ${contextFocusAreas}
- **Confidence**: ${selectionConfidence}

### Static Validation Framework
[Existing proven protocol logic - UNCHANGED]

### Rule-Enhanced Validation
- **Critical Rules**: Apply ${criticalRules} with high priority
- **Recommended Rules**: Validate ${recommendedRules} 
- **Skip**: Non-relevant validations for ${skippedAreas}
- **Focus**: Deep validation on ${focusAreas}
```

### Context Injection Points
```typescript
interface EnhancedProtocol extends StaticProtocol {
  contextAnalysis: ContextAnalysis;
  relevantRules: RelevantRules;
  focusAreas: string[];
  skipAreas: string[];
  customizedChecks: CustomCheck[];
}
```

## 🛠️ Implementation Strategy

### Step 1: Context Detection
```bash
# Git analysis for context detection
git diff --name-only HEAD~1..HEAD | while read file; do
  case "$file" in
    *auth*|*login*|*jwt*)     CONTEXT_FLAGS+="auth " ;;
    *security*|*secret*)      CONTEXT_FLAGS+="security " ;;
    *components*|*ui*)        CONTEXT_FLAGS+="ui " ;;
    *services/*)              CONTEXT_FLAGS+="service " ;;
    wrangler.toml)            CONTEXT_FLAGS+="config " ;;
  esac
done
```

### Step 2: Rule Filtering
```typescript
// Filter rules based on detected context
const relevantRules = masterRules
  .concat(commonRules, projectRules)
  .filter(rule => rule.scope.some(scope => detectedContexts.includes(scope)))
  .sort((a, b) => b.priority - a.priority);
```

### Step 3: Enhanced Execution
```bash
# Execute enhanced static protocol
Apply instructions from .ai-governor/dev-workflow/4-quality-audit.md 
--mode ${selectedMode}
--context "${detectedContext}"
--rules "${relevantRules}"
--focus "${focusAreas}"
```

## 📊 Expected Benefits

### ✅ **Noise Reduction**
- **40% less irrelevant checks** through context filtering
- **Faster review cycles** (5-15min → 2-8min average)
- **Higher signal-to-noise ratio** in findings

### ✅ **Intelligent Targeting**  
- **Context-aware suggestions** in `/review` interface
- **Smart protocol selection** based on change patterns
- **Focused validation** on relevant areas only

### ✅ **Maintained Reliability**
- **Keep static protocol structure** (proven reliability)
- **Predictable behavior** with enhanced intelligence
- **Graceful degradation** if context analysis fails

## 🔧 Tool Integration

### Enhanced `/review` Command
```bash
# Context-aware unified review
/review
# → Analyzes git changes
# → Detects: "Auth and security files modified"
# → Suggests: "Security Check + Pre-Production Security recommended (95% confidence)"
# → Shows focused protocol selection with rationale
```

### GitHub Actions Enhancement
```yaml
# Enhanced automation with context detection
- name: Analyze Change Context
  run: |
    CONTEXT=$(analyze-git-changes.sh)
    echo "context=$CONTEXT" >> $GITHUB_OUTPUT
    
- name: Smart Protocol Selection  
  run: |
    PROTOCOLS=$(select-protocols.sh "${{ steps.context.outputs.context }}")
    echo "protocols=$PROTOCOLS" >> $GITHUB_OUTPUT
```

## 🎯 Success Criteria

### Quantitative Targets
- **40% reduction** in irrelevant validation checks
- **60% faster** average review completion time
- **90% accuracy** in context detection
- **85% satisfaction** with protocol recommendations

### Qualitative Improvements
- **Smarter suggestions** in interactive selection
- **Better focus** on actual risk areas
- **Reduced review fatigue** from irrelevant checks
- **Higher confidence** in review completeness

---

**🎯 Result**: Enhanced Static Review system that maintains proven reliability while adding intelligent context awareness for **40% more efficient** and **60% faster** reviews with **laser-focused validation**.