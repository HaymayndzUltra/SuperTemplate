# Instruction Creator Meta-System Usage Guide

## Overview

The Instruction Creator Meta-System enables you to generate specialized protocol-generator instructions for any protocol format. This solves the limitation where the original `protocol-generator-instructions.md` only works for 01/02 format protocols.

## Command Interface

### Basic Usage
```
apply instruction from instruction-creator to protocol-{target-name}
```

### Examples

**Generate Bootstrap-Specific Instructions:**
```
apply instruction from instruction-creator to protocol-0-bootstrap
```
**Output:** 
- `generators/protocol-generator-instructions-bootstrap.md`
- `generators/protocol-input-form-bootstrap.yaml`

**Generate PRD-Specific Instructions:**
```
apply instruction from instruction-creator to protocol-1-create-prd
```
**Output:**
- `generators/protocol-generator-instructions-prd.md`
- `generators/protocol-input-form-prd.yaml`

**Generate Tasks-Specific Instructions:**
```
apply instruction from instruction-creator to protocol-2-generate-tasks
```
**Output:**
- `generators/protocol-generator-instructions-tasks.md`
- `generators/protocol-input-form-tasks.yaml`

## Supported Protocol Formats

### Format A: 01/02 Structure (6-Section)
- **Example:** `01-client-proposal-generation.md`, `02-client-discovery-initiation.md`
- **Structure:** AI ROLE → WORKFLOW → INTEGRATION → QUALITY GATES → COMMUNICATION → HANDOFF
- **Use Case:** Client-facing protocols with formal quality gates

### Format B: Bootstrap Structure (Step-Based)
- **Example:** `0-bootstrap-your-project.md`
- **Structure:** AI ROLE → MAIN PROCESS (STEPS) → FINALIZATION
- **Use Case:** Project initialization and setup protocols

### Format C: PRD Structure (Phase-Based)
- **Example:** `1-create-prd.md`
- **Structure:** AI ROLE → PREREQUISITES → PHASES → FINAL TEMPLATE
- **Use Case:** Requirements and specification protocols

### Format D: Custom Structure
- **Example:** Any protocol with unique structure
- **Structure:** Extracted dynamically from target protocol
- **Use Case:** Specialized protocols with custom requirements

## How It Works

### 1. Protocol Analysis
The instruction creator analyzes your target protocol to extract:
- **Structural Elements**: Header format, section hierarchy, required sections
- **Content Patterns**: Action formats, communication templates, validation patterns
- **Unique Characteristics**: Markers used, evidence collection, automation hooks

### 2. Format Classification
Automatically classifies the protocol into one of the supported formats or creates a custom classification.

### 3. Specialized Generator Creation
Generates format-specific instructions that include:
- **Format-Specific Template**: Exact structure matching your target protocol
- **Aligned Input Form**: Captures all requirements for your format
- **Validation Criteria**: Ensures generated protocols match your format exactly

### 4. Circular Validation
Ensures generated protocols are analyzable by the Meta-Analysis Generator, maintaining compatibility across all formats.

## Generated Files

### Specialized Generator Instructions
**File:** `protocol-generator-instructions-{target-name}.md`
**Purpose:** Complete instructions for generating protocols in your specific format
**Contents:**
- Format-specific template structure
- Aligned generation algorithm
- Format-specific validation criteria
- Usage protocol and examples

### Format-Specific Input Form
**File:** `protocol-input-form-{target-name}.yaml`
**Purpose:** Input form tailored to your protocol format
**Contents:**
- Format-specific fields and structure
- Required vs optional sections
- Validation requirements
- Example values and patterns

## Usage Workflow

### Step 1: Identify Target Protocol
Choose the protocol format you want to generate protocols in:
- Existing protocol in `.cursor/ai-driven-workflow/`
- Custom protocol with unique structure

### Step 2: Run Instruction Creator
Execute the command:
```
apply instruction from instruction-creator to protocol-{target-name}
```

### Step 3: Use Generated Instructions
Use the generated specialized instructions to create new protocols:
1. Fill the format-specific input form
2. Run the specialized generator
3. Validate with Meta-Analysis Generator

### Step 4: Verify Output
Ensure generated protocols:
- Match your target format exactly
- Pass Meta-Analysis Generator validation
- Integrate with existing workflow

## Benefits

### Format Flexibility
- Generate protocols in any structure, not just 01/02 format
- Support for bootstrap, PRD, tasks, and custom formats
- Easy to add new protocol formats

### Consistency
- Generated protocols match target format exactly
- Maintains structural integrity across all formats
- Preserves unique characteristics of each format

### Scalability
- Single meta-system creates all specialized generators
- Easy to create generators for new protocol formats
- Maintains circular validation compatibility

### Quality Assurance
- All generated protocols are meta-analyzable
- Maintains 4-layer architecture compatibility
- Preserves cognitive role identification

## Examples

### Example 1: Bootstrap Format Generator
**Input:** `protocol-0-bootstrap`
**Analysis:** Step-based structure with FINALIZATION section
**Output:** Bootstrap-specific generator that creates protocols with:
- AI ROLE AND MISSION section
- Main process with numbered STEPS
- FINALIZATION section
- Step-based input form

### Example 2: PRD Format Generator
**Input:** `protocol-1-create-prd`
**Analysis:** Phase-based structure with architectural matrix
**Output:** PRD-specific generator that creates protocols with:
- AI ROLE section
- Prerequisites and architectural matrix
- Numbered PHASES with subsections
- Question templates and validation
- Final template structure

### Example 3: Custom Format Generator
**Input:** `protocol-custom-security`
**Analysis:** Unique structure with security-specific sections
**Output:** Custom generator that creates protocols with:
- Security-specific template structure
- Custom validation criteria
- Specialized input form
- Security-focused automation hooks

## Integration with Existing Workflow

### Meta-Analysis Compatibility
All generated protocols maintain compatibility with the Meta-Analysis Generator:
- **Layer 1**: System-Level Decisions (mission, role, constraints)
- **Layer 2**: Behavioral Control (validation, checkpoints, gates)
- **Layer 3**: Procedural Logic (steps, tools, data flow)
- **Layer 4**: Communication Grammar (templates, prompts, narratives)

### Workflow Integration
Generated protocols integrate seamlessly with existing workflow:
- Protocol numbering follows sequence
- Integration points connect to existing protocols
- Automation hooks integrate with existing scripts
- Handoff transitions to next protocol

## Troubleshooting

### Common Issues

**Issue:** Generated instructions don't match target format
**Solution:** Verify target protocol structure is correctly analyzed
**Check:** Ensure target protocol file exists and is readable

**Issue:** Generated protocols fail meta-analysis validation
**Solution:** Check that all 4 layers are present in generated protocol
**Check:** Verify structural compliance and line-referenceability

**Issue:** Input form doesn't capture all requirements
**Solution:** Review target protocol for missing patterns
**Check:** Ensure all sections and subsections are analyzed

### Validation Checklist

Before using generated instructions:
- [ ] Target protocol structure correctly analyzed
- [ ] Format classification accurate
- [ ] Generated instructions complete
- [ ] Input form captures all requirements
- [ ] Circular validation compatibility maintained
- [ ] Generated protocols match target format exactly

## Next Steps

1. **Test with Your Protocols**: Try the instruction creator with your existing protocols
2. **Create Specialized Generators**: Generate format-specific instructions for your workflow
3. **Validate Output**: Ensure generated protocols meet your requirements
4. **Integrate with Workflow**: Use specialized generators in your development process

---

**The Instruction Creator Meta-System provides format flexibility, consistency, and quality assurance for protocol generation across all structural patterns in your AI-driven workflow.**
