# 🤖 Cursor Slash Commands & AI Agent Integration Guide

## Overview

This document explains how **Cursor's slash commands** work with the **AI-driven workflow system** in this repository. Slash commands provide a powerful way to trigger specific AI behaviors and workflows directly from Cursor's chat interface.

## How Slash Commands Work

### Basic Mechanism
- **Trigger**: Type `/` in Cursor's chat input box
- **Auto-detection**: Cursor automatically scans `.cursor/commands/` directory
- **Execution**: Select from available commands to execute specific workflows
- **Integration**: Commands integrate with the AI-driven workflow protocols

### File Structure
```
.cursor/commands/
├── AGENTS.md                    # This guide
├── elaborate.md                 # Elaboration specialist command
├── generate-cursor-rules.md     # Rule generation command
└── protocol-orchestrator.md     # Protocol orchestration command
```

## Available Slash Commands

### `/elaborate` - Elaboration Specialist
**Purpose**: Convert unclear instructions into detailed, actionable requirements

**Usage**:
```
/elaborate [your unclear instruction]
```

**Example**:
```
/elaborate make the app faster
# → Converts to detailed performance optimization requirements
```

**Integration**: Uses `.cursor/commands/elaborate.md` protocol

### `/generate-cursor-rules` - Rule Generation
**Purpose**: Generate project-specific Cursor rules based on codebase analysis

**Usage**:
```
/generate-cursor-rules [target-directory]
```

**Example**:
```
/generate-cursor-rules apps/frontend
# → Analyzes frontend codebase and generates tailored rules
```

**Integration**: Uses `.cursor/commands/generate-cursor-rules.md` protocol

### `/protocol-orchestrator` - Workflow Orchestration
**Purpose**: Analyze project briefs and generate optimal protocol sequences

**Usage**:
```
/protocol-orchestrator [brief-file]
```

**Example**:
```
/protocol-orchestrator PROJECT-BRIEF.md
# → Generates customized workflow commands
```

**Integration**: Uses `.cursor/commands/protocol-orchestrator.md` protocol

## AI Agent Behavior Integration

### Core Principles Applied to Slash Commands

1. **"Why Before How"**: Each command explains its purpose before execution
2. **Developer Cognitive Loop**: Commands follow natural developer thinking patterns
3. **Reasoning Integrity**: Commands extend human reasoning, never replace it
4. **Evidence-Based**: All commands collect and validate evidence

### Command Execution Flow

```
User Input (/command) 
    ↓
Command Detection
    ↓
Protocol Loading
    ↓
Context Analysis
    ↓
Execution with Evidence Collection
    ↓
Validation & Feedback
```

## Integration with AI-Driven Workflow

### Workflow Protocol Integration
Slash commands seamlessly integrate with the 5-phase AI-driven workflow:

1. **Bootstrap** (`/protocol-orchestrator`) - Project initialization
2. **PRD Creation** (`/elaborate`) - Requirements clarification
3. **Task Generation** (`/generate-cursor-rules`) - Rule-based task planning
4. **Task Processing** - Execution with evidence collection
5. **Quality Audit** - Validation and retrospective

### Context Awareness
Commands automatically leverage:
- **@codebase** - Full project context
- **@recent-changes** - Git change analysis
- **@filename** - File-specific context
- **Master Rules** - Project-specific guidelines

## Creating New Slash Commands

### Step 1: Create Command File
Create a new `.md` file in `.cursor/commands/` directory:

```markdown
# Command Name

## Purpose
Brief description of what this command does.

## Usage
```
/command-name [parameters]
```

## Examples
```
/command-name example-usage
```

## Integration Points
- Which workflow protocols this integrates with
- What evidence it collects
- How it validates outcomes
```

### Step 2: Follow AI Agent Principles
Ensure your command follows:
- **Reasoning Integrity**: Extends human thinking
- **Evidence Collection**: Validates all outputs
- **Context Awareness**: Leverages available context
- **Cognitive Continuity**: Feels natural to developers

### Step 3: Test Integration
- Test with `@codebase` context
- Verify evidence collection
- Validate output quality
- Ensure seamless workflow integration

## Best Practices

### Command Design
- **Clear Purpose**: Each command should have a single, well-defined purpose
- **Natural Language**: Use developer-friendly terminology
- **Contextual**: Leverage available context automatically
- **Evidence-Based**: Always collect and validate evidence

### Integration Guidelines
- **Workflow Alignment**: Commands should align with the 5-phase workflow
- **Rule Compliance**: Follow master rules and common rules
- **Quality Gates**: Include validation checkpoints
- **Feedback Loops**: Provide clear feedback and next steps

### Performance Considerations
- **Efficient Context**: Only load necessary context
- **Incremental Processing**: Break complex tasks into steps
- **Caching**: Cache analysis results when appropriate
- **Parallel Processing**: Use parallel execution when possible

## Troubleshooting

### Common Issues

**Command Not Detected**:
- Ensure file is in `.cursor/commands/` directory
- Check file extension is `.md`
- Verify file syntax is valid Markdown

**Context Not Loading**:
- Use `@codebase` to provide full context
- Check if master rules are properly loaded
- Verify workflow protocols are accessible

**Integration Failures**:
- Ensure commands follow AI agent principles
- Check evidence collection mechanisms
- Validate workflow protocol integration

### Debug Commands
```
/elaborate debug-issue
# → Converts unclear issues into actionable debug steps

/generate-cursor-rules debug
# → Generates debugging-specific rules
```

## Advanced Usage

### Composer Mode Integration
Slash commands work seamlessly with Cursor's Composer mode:

```
/elaborate implement user authentication
# → Generates detailed requirements
# → Composer applies suggestions automatically
```

### Multi-File Analysis
Commands can analyze multiple files simultaneously:

```
/generate-cursor-rules apps/* services/*
# → Analyzes entire application stack
```

### Custom Context Integration
Commands can leverage custom context:

```
/protocol-orchestrator @PROJECT-BRIEF.md @recent-changes
# → Combines brief analysis with recent changes
```

## Conclusion

Cursor's slash commands provide a powerful interface for interacting with the AI-driven workflow system. By following the principles outlined in this guide, you can create commands that seamlessly integrate with the existing workflow protocols while maintaining the cognitive continuity and reasoning integrity that makes the system effective.

The key is to remember that slash commands are **extensions of human reasoning**, not replacements. They should feel like natural next steps in a developer's thought process, providing intelligent automation that enhances rather than replaces human decision-making.

---

**Next Steps**: 
- Try the existing commands: `/elaborate`, `/generate-cursor-rules`, `/protocol-orchestrator`
- Create custom commands following the guidelines above
- Integrate commands with your specific workflow needs
- Provide feedback to improve command effectiveness
