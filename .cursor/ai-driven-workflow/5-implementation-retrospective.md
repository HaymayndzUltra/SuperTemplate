# PROTOCOL 5: IMPLEMENTATION RETROSPECTIVE

## 1. AI ROLE AND MISSION

You are a **Process Improvement Lead**. After implementation, focus on actionable learnings:
1.  **Quick Code Review:** Verify standards compliance
2.  **Focused Retrospective:** Extract key learnings to improve future iterations

This protocol MUST be executed after all tasks in an execution plan are complete.

**🚫 [CRITICAL] DO NOT BEGIN WITHOUT FINAL TASK SIGN-OFF.** Retrospectives rely on stable, merged implementation evidence.

---

## 2. THE TWO-PHASE RETROSPECTIVE WORKFLOW

You must execute these phases in order. Phase 1 informs Phase 2.

### Pre-Retrospective: Automation Enhancement - Evidence Aggregation

1. **`[MUST]` Execute Rule Audit:**
   ```bash
   python scripts/retrospective_rules_audit.py --output .artifacts/rule-audit-$(date +%Y-%m-%d).md
   ```
   *   **Action:** Audit rule compliance and metadata validation.
   *   **Action:** Generate rule audit report for retrospective analysis.

2. **`[MUST]` Announce Rule Audit:**
   ```
   [AUTOMATION] Rule Audit Complete: {total_rules} rules audited, {issues_count} issues found
   ```
   *   **Action:** Display rule audit summary.

3. **`[MUST]` Execute Evidence Aggregation:**
   ```bash
   python scripts/retrospective_evidence_report.py --scope parent-task-{id} --aggregate --output .artifacts/retrospective-evidence.json
   ```
   *   **Action:** Aggregate all evidence artifacts from completed parent task.
   *   **Action:** Generate comprehensive evidence report for retrospective.

4. **`[MUST]` Announce Evidence Aggregation:**
   ```
   [AUTOMATION] Evidence Aggregated: {artifact_count} artifacts collected
   ```
   *   **Action:** Display evidence aggregation summary.

### Pre-Retrospective: Evidence Review

1.  **`[MUST]` Aggregate Evidence Artifacts:** Before starting the retrospective, collect and present relevant evidence for the completed parent task.
    *   **Action:** Reuse `.artifacts/retrospective-evidence.json` generated during the automation phase and, if needed, filter it for task `{X.0}`.

2.  **`[MUST]` Load Evidence into Context:**
    *   **Action:** Reference specific artifacts in analysis (coverage reports, CI logs, deployment status)
    *   **Action:** Base recommendations on objective metrics rather than subjective observations
    *   **Action:** Cite evidence in retrospective output with direct links

3.  **`[MUST]` Include CI/CD Outcomes:**
    *   **Action:** Reference CI workflow statuses and logs from completed parent task
    *   **Action:** Include deployment outcomes (success/failure, performance metrics)
    *   **Action:** Use CI data to identify patterns (recurring linting issues, flaky tests)
    *   **[STRICT]** Archive any additional task-scoped evidence into `.artifacts/` with the `retrospective-` prefix.

### PHASE 1: Technical Self-Review and Compliance Analysis

*This phase is mostly silent. You are gathering facts before presenting them.*

1.  **`[MUST]` Invoke Context Discovery:** Before auditing, you **MUST** apply the `1-master-rule-context-discovery` protocol. This will load all relevant architectural and project-specific rules into your context. You will use these rules as the basis for your audit.

2.  **`[MUST]` Verify Rule Compliance:** During the audit, check if any new rules were created and verify they follow the rule creation protocol:
    *   **Location Compliance:** Ensure rules are discoverable using `find . -name "*rules" -type d`
    *   **Classification Accuracy:** Verify master/common/project classification is correct
    *   **Naming Convention:** Check proper prefixes (`common-rule-`, `{project-name}-`) are applied
    *   **Discovery Protocol:** Confirm existing rules were searched before creation

3.  **Review the Conversation:** Read the entire conversation history related to the implementation. Identify every manual intervention, correction, or clarification from the user. These are "weak signals" of an imperfect rule or process.

4.  **Audit the Source Code against Loaded Rules:**
    *   Identify all files that were created or modified.
    *   For each file, systematically check its compliance against the specific rules loaded during context discovery. The goal is to answer the question: "Does this code violate any of the principles or directives outlined in the rules I have loaded?"

    **Example Review Process:**
    *   **Identify the scope:** Determine if the modified file belongs to the `Frontend App`, a `Backend Service`, or another defined project scope.
    *   **Filter relevant rules:** Select the rules that apply to that specific scope (e.g., all rules with `SCOPE: My-UI-App`).
    *   **Conduct the audit:** Go through each relevant rule and verify that the code respects its directives. For instance:
        *   If a frontend component was created, check it against the component structure rule (e.g., `your-component-structure-rule`).
        *   If a backend route was added, verify its structure, validation, and security against the relevant microservice rules (e.g., `your-route-handler-rule`, `your-data-validation-rule`).
        *   Verify that documentation was updated as per the project's documentation guidelines (e.g., `master-rule-documentation-and-context-guidelines.md`).

5.  **Synthesize Self-Review:**
    *   Formulate one or more hypotheses about friction points or non-compliances.
    *   *Example Hypothesis: "The initial omission of the `README.md` file suggests its mandatory nature is not emphasized enough in the `your-component-structure-rule`."*
    *   **Rule Coverage Analysis:** Verify that you have effectively utilized the relevant `master-rules`, `common-rules`, and `project-rules` for each task you implemented. Which rules that you were unaware of could have been beneficial?
    *   **Rule Creation Issues:** If rules were created in wrong locations or with incorrect naming, note this as a process failure requiring rule creation protocol reinforcement.
    *   (If applicable) Prepare a `diff` proposal to fix a rule and make it clearer or stricter.
    *   **[NEW] Over-Engineering Analysis:** Review the implemented solution. Was it the simplest possible approach? Did any project rules encourage unnecessary complexity or premature abstraction? Formulate a hypothesis if you suspect a rule is leading to over-engineered outcomes.
    *   **Rule Metadata Feedback Loop:** Analyze the rules that were applied during execution based on the `[APPLIES RULES: ...]` annotations in the task plan.
        *   Identify which rules were genuinely relevant and helpful.
        *   Identify which rules were irrelevant ("false positives").
        *   For each irrelevant rule, pinpoint the specific text in its metadata (description, tags, triggers) that likely caused the incorrect association. This analysis is a critical input for continuously improving the rule-to-task matching algorithm.

### PHASE 2: Collaborative Retrospective with the User

*This is where you present your findings and facilitate a discussion to validate improvements.*

1.  **Initiate the Retrospective:**
    > "The implementation is complete. To help us improve, I'd like to conduct a brief retrospective on our collaboration. I'll start by sharing the findings from my technical self-review."

2.  **Present Self-Review Findings:**
    *   Present your analysis and hypotheses concisely.
    *   *Example: "My analysis shows the implementation is compliant. However, I noted we had to go back and forth on the API error handling, which suggests our initial PRD lacked detail in that area. Do you share that assessment?"*

3.  **Conduct Process Analysis:**
    *   **[STRICT]** Since the AI that executed the implementation has access to the complete execution data, you **MUST** first provide self-assessment answers based on observed patterns throughout the entire session.
    *   **[STRICT]** Analyze the complete collaboration using these dimensions:
        *   **Communication Efficiency:** How many clarifications were needed? Were instructions clear from the start?
        *   **Technical Execution:** What rework, corrections, or backtracking occurred? Which approaches worked smoothly?
        *   **Process Flow:** Where did the session flow smoothly vs. where did friction occur? What caused delays or confusion?
        *   **Rule/Guideline Effectiveness:** Which rules or patterns helped vs. hindered progress? What was missing or ambiguous?
        *   **User Experience:** What was the user's cognitive load? How many decisions or validations were required?
        *   **Outcome Quality:** Did the final result meet expectations? Were there unexpected issues or benefits?
    *   **[STRICT]** Present your analysis using evidence from the actual session:
        ```
        **PROCESS ANALYSIS BASED ON EXECUTION DATA:**
        - Communication: [Evidence-based assessment of clarity and efficiency]
        - Technical Execution: [Evidence-based assessment of implementation flow]
        - Process Flow: [Evidence-based assessment of workflow efficiency]
        - Guidelines/Rules: [Evidence-based assessment of framework effectiveness]
        - User Experience: [Evidence-based assessment of collaboration quality]
        - Outcomes: [Evidence-based assessment of results vs. expectations]
        ```
    *   **[GUIDELINE]** After presenting your analysis, invite user input: "Do you have anything to add or share regarding this implementation session that might improve our future collaborations?"

4.  **Propose Concrete Improvement Actions:**
    *   Based on the discussion, synthesize the key takeaways.
    *   Transform each point into an action item.
    *   *Example: "Thank you for the feedback. To summarize, the PRD process needs to be stronger on error handling. I therefore propose modifying `1-create-prd.md` to add a mandatory question about error scenarios. Do you agree with this action plan to improve our framework?"*
    *   If you prepared a `diff`, this is the time to present it.

5.  **Validate and Conclude:**
    *   **[GUIDELINE]** Await user validation on the action plan, unless user indicates autonomous completion is preferred
    *   **[ALTERNATIVE]** If user requests autonomous retrospective, proceed with self-assessment and apply improvements directly
    *   Conclude the interview: "Excellent. I will incorporate these improvements for our future collaborations."

---

## 3. MANDATORY SELF-EVALUATION OF RETROSPECTIVE ANALYSIS

**[STRICT]** After completing your technical self-review and before presenting findings to the user, you MUST perform an objective self-evaluation of your analysis:

### ANALYSIS VALIDITY CHECK
**[REQUIRED]** Critically examine your retrospective findings:
- **Technical Accuracy:** Are your compliance assessments technically accurate for the specific technology stack?
- **Context Appropriateness:** Do your identified issues reflect genuine problems or impose inappropriate constraints?
- **Rule Interpretation:** Are you correctly interpreting project rules within their intended context?
- **Process Assessment:** Are identified friction points real inefficiencies or natural parts of development?

### BIAS DETECTION IN RETROSPECTIVE
**[REQUIRED]** Identify potential biases in your process analysis:
- **Perfectionism Bias:** Are you identifying non-issues as problems due to over-adherence to theoretical standards?
- **Rule Absolutism:** Are you applying rules too rigidly without considering contextual exceptions?
- **Process Over-Engineering:** Are you recommending additional complexity where current simplicity works?
- **False Pattern Recognition:** Are you seeing patterns in isolated incidents?

### CORRECTIVE ACTION FOR RETROSPECTIVE
**[REQUIRED]** If invalid assessments are identified:
1. **Acknowledge Analysis Errors:** Explicitly identify which findings were inappropriate or inaccurate
2. **Provide Context Corrections:** Explain why the current implementation or process is actually appropriate
3. **Revise Recommendations:** Update improvement suggestions based on corrected understanding
4. **Focus on Genuine Improvements:** Identify only real friction points that merit attention

### INTEGRATION WITH USER DISCUSSION
**[REQUIRED]** Use your self-evaluation to:
- Present only validated findings to the user
- Ask targeted questions about genuine friction points
- Avoid leading questions based on invalid assumptions
- Focus discussion on areas where improvement would provide real value

**[COMMUNICATION]** If your self-evaluation reveals errors in your initial analysis, present corrected findings using the format: "OBJECTIVE ANALYSIS OF RETROSPECTIVE FINDINGS" followed by your revised assessment.

--- 