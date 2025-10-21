# Protocol Analysis & Validation Tool

## Purpose
Analyze a single protocol file from the AI-Driven Workflow System to verify:
- Instruction clarity and completeness
- Artifact input/output consistency
- Gate logic and halting conditions
- Integration with adjacent protocols

## Required Inputs
Before starting, confirm you have:
1. **Protocol File Path** (e.g., `.cursor/ai-driven-workflow/02-client-discovery-initiation.md`)
2. **Expected Input Artifacts** (list file paths this protocol should consume)
3. **Expected Output Artifacts** (list file paths this protocol should produce)

**Optional Inputs**:
- Previous protocol file path (for flow validation)
- Next protocol file path (for flow validation)

## Analysis Procedure

### Step 1: Protocol Structure Verification
Read the target protocol file and extract:
- Protocol ID/number
- All instruction steps (numbered or bulleted)
- All artifact references (inputs and outputs)
- All decision gates (approval points, conditional logic)

**If the protocol file doesn't exist or is malformed, STOP and report the error.**

### Step 2: Instruction Clarity Assessment
For each instruction step:
- Quote the exact text
- Classify as: [Action | Decision | Validation | Documentation]
- Rate clarity (1-5 scale):
  - **5**: Actionable, specific, measurable
  - **3**: Understandable but vague (e.g., "ensure quality")
  - **1**: Ambiguous or missing critical details
- Flag issues: undefined terms, missing prerequisites, circular references

### Step 3: Artifact Consistency Check
For each artifact mentioned in the protocol:
- Verify it appears in the provided input/output lists
- Check if the artifact path exists in the workspace (use file search)
- Identify orphaned artifacts (referenced but not produced/consumed)
- Note schema mismatches (if artifact templates exist)

### Step 4: Gate Logic Validation
For each decision point:
- Classify gate type:
  - **AI-Automated**: Scriptable validation (e.g., "run linter")
  - **Human-Approval**: Requires stakeholder sign-off
  - **Conditional-Branch**: If/else logic based on prior state
- Verify halting criteria are measurable (e.g., "all tests pass" vs. "code is good")
- Check if gate references actual artifacts or metrics

### Step 5: Flow Integration (if adjacent protocols provided)
- Compare previous protocol's output artifacts to current protocol's input artifacts
- Compare current protocol's output artifacts to next protocol's input artifacts
- Flag format incompatibilities (e.g., JSON vs. Markdown)

### Step 6: Generate Report
Output analysis in this JSON structure:

```json
{
  "protocol_id": "<extracted from file or 'UNKNOWN'>",
  "file_path": "<actual path analyzed>",
  "structure_valid": true|false,
  "step_analysis": [
    {
      "step_number": 1,
      "instruction_text": "<exact quote>",
      "type": "Action|Decision|Validation|Documentation",
      "clarity_score": 1-5,
      "issues": ["Undefined term: 'quality gate'", "Missing prerequisite: API key setup"]
    }
  ],
  "artifact_verification": {
    "inputs": [
      {"name": "job-post.md", "status": "verified|missing|undefined", "path": "<actual path or null>"}
    ],
    "outputs": [
      {"name": "proposal.md", "status": "verified|missing|undefined", "path": "<actual path or null>"}
    ],
    "orphaned": ["artifact referenced but not in input/output lists"]
  },
  "gates": [
    {
      "step_number": 3,
      "type": "Human-Approval",
      "criteria_explicit": true,
      "criteria_text": "<exact quote of success condition>",
      "issues": ["Criteria references undefined metric 'stakeholder satisfaction'"]
    }
  ],
  "flow_validation": {
    "previous_protocol": {
      "compatible": true|false|"not_provided",
      "issues": ["Output 'brief.json' expected but previous protocol produces 'brief.md'"]
    },
    "next_protocol": {
      "compatible": true|false|"not_provided",
      "issues": []
    }
  },
  "critical_issues": [
    "Step 4 references non-existent artifact 'risk-matrix.csv'",
    "Gate at step 7 has no measurable success criteria"
  ],
  "recommendations": [
    "Add explicit artifact schema for 'proposal.md' in protocol header",
    "Replace 'ensure quality' with 'run validation script X and verify exit code 0'"
  ]
}