# EXECUTION FORMAT: REASONING VARIANT

**Source**: EXECUTION-FORMATS.md  
**Use Case**: Decision-heavy workflows requiring explicit rationale documentation  
**When to Use**: Complex decision-making, strategic choices, or high-risk operations

---

## TEMPLATE STRUCTURE

```markdown
# PROTOCOL {NUMBER}: {PROTOCOL_NAME}

## AI ROLE AND MISSION

{Persona definition with decision-making authority and reasoning responsibilities}

## WORKFLOW

### PHASE 1: {Phase_Name - Analysis}

<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: {Explanation of why this phase requires reasoning} -->

**Reasoning Pattern:** {Heuristic or principle guiding decisions}

**Example Scenario:** {Concrete example of reasoning application}

**Strategy Rationale:** {Why this strategy was chosen over alternatives}

**Decision Tree:** {IF/THEN logic for key decisions}
- **IF** {condition} → {action}
- **ELSE IF** {condition} → {action}
- **THEN** {result}

**[STRICT]** {Critical requirement based on reasoning}

### 1.1 {Step_Title}
1. **Step 1: {Action_Name}**
   - Input: {Required inputs}
   - Action: {Detailed instructions}
   - Evidence: {Output artifact}
   - Validation: {Success criteria}

2. **Step 2: {Action_Name}**
   - Input: {Required inputs}
   - Action: {Detailed instructions}
   - Evidence: {Output artifact}
   - Validation: {Success criteria}

**[REASONING]**
{Detailed rationale explaining why specific decisions were made in this phase, including:
- Premises: What facts or assumptions guided the decision
- Constraints: What limitations influenced the choice
- Alternatives Considered: What other options were evaluated
- Decision: What was chosen and why
- Evidence: How past experience or data supports this choice
- Risks & Mitigations: What could go wrong and how to address it
- Acceptance Link: How this connects to requirements or standards}

**Halt-and-await**: {Confirmation requirement before proceeding}

---

### PHASE 2: {Phase_Name - Strategic Decisions}

<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: {Explanation of why this phase requires reasoning} -->

**Reasoning Pattern:** {Heuristic or principle guiding decisions}

**[STRICT]** {Critical requirement based on reasoning}

### 2.1 {Step_Title}
1. **Step 1: {Action_Name}**
   - Input: {Required inputs}
   - Action: {Detailed instructions}
   - Evidence: {Output artifact}
   - Validation: {Success criteria}

**[REASONING]**
{Detailed rationale for strategic decisions in this phase}

**Halt-and-await**: {Confirmation requirement before proceeding}

---

### PHASE 3: {Phase_Name - Implementation}

<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: {Explanation of why this phase can use basic format} -->

1. **Step 1: {Action_Name}**
   - Input: {Required inputs}
   - Action: {Detailed instructions}
   - Evidence: {Output artifact}
   - Validation: {Success criteria}

---

### PHASE 4: {Phase_Name - Validation}

<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: {Explanation of why this phase requires reasoning} -->

**Reasoning Pattern:** {Heuristic or principle guiding decisions}

**[STRICT]** {Critical requirement based on reasoning}

### 4.1 {Step_Title}
1. **Step 1: {Action_Name}**
   - Input: {Required inputs}
   - Action: {Detailed instructions}
   - Evidence: {Output artifact}
   - Validation: {Success criteria}

**[REASONING]**
{Detailed rationale for validation decisions and go/no-go criteria}

**Success Criteria**: {What defines completion with decision justification}
```

---

## KEY FEATURES

### Reasoning Block Structure
```markdown
**[REASONING]**
- **Premises**: {Facts or assumptions}
- **Constraints**: {Limitations influencing choice}
- **Alternatives Considered**: {Options evaluated}
- - A) {Option A} (rejected - reason)
- - B) {Option B} (selected - reason)
- **Decision**: {What was chosen and why}
- **Evidence**: {Supporting data or experience}
- **Risks & Mitigations**: {Potential issues and solutions}
- **Acceptance Link**: {Connection to requirements}
```

### Category Annotations
```markdown
<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: This phase involves critical decisions about {specific domain} -->
```

### Decision Tree Logic
```markdown
**Decision Tree:** When {making decision type}:
- **IF** {condition} → {action}
- **ELSE IF** {condition} → {action}
- **THEN** {verification step}
```

---

## USAGE EXAMPLE

### Protocol 10: Feature Engineering & Transformation (REASONING Variant)

```markdown
### PHASE 2: FEATURE SELECTION

<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: Feature selection requires strategic decisions about model performance vs complexity trade-offs -->

**Reasoning Pattern:** Performance-complexity trade-off heuristic — systematically evaluate feature importance against computational cost and interpretability requirements.

**Example Scenario:** When selecting features for a customer churn model, we must balance predictive power (mutual information scores) against business constraints (need for interpretable features for regulatory compliance). If we select only the top 20 features by importance, we achieve 92% of the maximum predictive power while maintaining full interpretability. Therefore, we should use a hybrid approach that prioritizes high-importance features while preserving key business metrics.

**Strategy Rationale:** Because feature selection directly impacts downstream model performance and business adoption, we must consider both statistical significance and business interpretability. Pure statistical selection often yields features that are mathematically optimal but business-unacceptable.

**Decision Tree:** When selecting features:
- **IF** feature importance ≥ 0.05 AND business interpretable → SELECT
- **ELSE IF** feature importance ≥ 0.10 AND critical for accuracy → SELECT WITH DOCUMENTATION
- **ELSE IF** feature importance < 0.01 → REJECT
- **THEN** Validate selected feature set meets completeness threshold

**[STRICT]** Document rationale for every feature selection decision, especially when rejecting high-importance features for business reasons.

### 2.1 Correlation Analysis and Redundancy Removal
1. **Step 1: Calculate Feature Correlation Matrix**
   - Input: Engineered feature dataset
   - Action: Compute pairwise correlation coefficients
   - Evidence: `.artifacts/protocol-10/correlation-matrix.json`
   - Validation: Matrix computed for all numeric features

2. **Step 2: Identify Redundant Feature Pairs**
   - Input: Correlation matrix, redundancy threshold (0.95)
   - Action: Flag feature pairs with correlation ≥ 0.95
   - Evidence: `.artifacts/protocol-10/redundant-features.json`
   - Validation: All high-correlation pairs identified

3. **Step 3: Apply Redundancy Removal Strategy**
   - Input: Redundant feature pairs, business importance scores
   - Action: Remove less important feature from each redundant pair
   - Evidence: `.artifacts/protocol-10/non-redundant-features.parquet`
   - Validation: No remaining feature pairs with correlation ≥ 0.95

**[REASONING]**
The correlation analysis indicates several feature pairs with high redundancy (>0.95 correlation). Based on the business importance scoring from Protocol 07, we must make strategic decisions about which features to retain. For the "customer_age" vs "account_duration" pair (correlation 0.97), both have similar predictive importance, but "customer_age" is more interpretable for business stakeholders and required for regulatory reporting. Therefore, we retain "customer_age" and remove "account_duration" despite both being statistically valuable.

For the "purchase_frequency" vs "purchase_count" pair (correlation 0.98), "purchase_frequency" provides normalized values that are more comparable across customer segments, while "purchase_count" is skewed by customer tenure. We select "purchase_frequency" for better model generalization.

**Risks & Mitigations:**
- Risk: Removing features may reduce model performance slightly
- Mitigation: Validate model performance with reduced feature set
- Risk: Business stakeholders may question removed features
- Mitigation: Document correlation analysis and business rationale

**Acceptance Link:** This approach aligns with Protocol 07 requirements for feature interpretability and regulatory compliance while maintaining the predictive power threshold established in the success criteria.

**Halt-and-await**: Confirm feature selection strategy approved before proceeding to encoding phase.
```

---

## WHEN TO USE THIS VARIANT

### ✅ Perfect For:
- **Strategic Decision Points**: Go/no-go decisions, architecture choices
- **Risk Assessment**: Security, compliance, or operational risk decisions
- **Resource Allocation**: Budget, timeline, or personnel decisions
- **Quality Trade-offs**: Performance vs. cost, speed vs. accuracy decisions

### ❌ Avoid For:
- **Routine Data Processing**: Overkill for standard transformations
- **Simple Validation Steps**: Excessive documentation for basic checks
- **Automated Workflows**: Too manual for fully automated processes
- **Rapid Iteration**: Slows down fast experimentation cycles

---

## CUSTOMIZATION GUIDELINES

### Reasoning Depth
- **Critical decisions**: Full reasoning block with all elements
- **Minor decisions**: Simplified reasoning with key points only
- **Automated decisions**: Brief justification of algorithm choice

### Evidence Integration
- **Decision evidence**: Link reasoning to specific data points
- **Stakeholder input**: Reference business requirements or constraints
- **Technical constraints**: Document system limitations affecting decisions

### Halt Points
- **Major decisions**: Require explicit confirmation before proceeding
- **Minor decisions**: Document and continue
- **Automated decisions**: No halt required, just logging

---

## BENEFITS

### Decision Transparency
- **Complete audit trail**: Every decision documented with rationale
- **Stakeholder alignment**: Business reasoning clearly explained
- **Regulatory compliance**: Decision process meets audit requirements

### Knowledge Transfer
- **Learning capture**: Decision criteria reusable for future projects
- **Pattern recognition**: Common decision scenarios identified
- **Process improvement**: Reasoning patterns reveal optimization opportunities

### Risk Management
- **Assumption tracking**: Explicit documentation of premises
- **Alternative analysis**: Documented evaluation of rejected options
- **Mitigation planning**: Proactive risk identification and response

---

*This REASONING variant provides comprehensive decision documentation for high-stakes workflows requiring transparency and auditability.*
