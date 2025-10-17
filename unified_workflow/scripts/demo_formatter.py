#!/usr/bin/env python3
"""
Demo script for System Instruction Formatter
Shows how to integrate the formatter with phase protocols
"""

import sys
import os
from pathlib import Path

# Add the automation directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "automation"))

from system_instruction_formatter import SystemInstructionFormatter, InstructionType

def demo_phase_formatting():
    """Demonstrate phase protocol formatting"""
    print("=== System Instruction Formatter Demo ===\n")
    
    # Initialize formatter
    formatter = SystemInstructionFormatter()
    
    # Demo content for different phases
    phase_examples = {
        0: {
            "name": "Bootstrap",
            "content": """---
description: "Bootstrap phase protocol"
alwaysApply: true
---

# Phase 0: Bootstrap & Context Engineering

## AI Role
**Context Architect** - Analyze repository structure

## Mission
Perform initial analysis and configure AI Governor Framework

## Process

### Step 1: Tooling Configuration
1. **Detect Tooling & Configure Rules**
   - Ask user about Cursor usage
   - Locate rules directories
   - Configure metadata

### Step 2: Initial Codebase Mapping
1. **Map Codebase Structure**
   - Perform recursive file listing
   - Identify key files
   - Propose analysis plan
"""
        },
        2: {
            "name": "Task Generation", 
            "content": """---
description: "Task generation phase protocol"
---

# Phase 2: Task Generation

## AI Role
**Tech Lead** - Transform PRD into actionable plan

## Mission
Transform PRD into granular technical execution plan

## Process

### Phase 1: Rule Indexing
1. **Build Rule Index**
   - Locate rule directories
   - Parse rule metadata
   - Create compliance index

### Phase 2: High-Level Task Generation
1. **Create Task File**
   - Structure with parent/child hierarchy
   - Focus on MVP features
   - Add WHY context
"""
        },
        4: {
            "name": "Quality Audit",
            "content": """---
description: "Quality audit phase protocol"
---

# Phase 4: Quality Audit

## AI Role
**Quality Engineer** - Execute comprehensive validation

## Mission
Conduct systematic quality audit using specialized protocols

## Execution Flow

### 1. Mode Determination
Activated with specific mode flag

### 2. Context Analysis & Protocol Routing
- Use Centralized Router
- Handle intelligent fallback
- Load appropriate protocol

### 3. Protocol Execution
- Execute validation logic
- Apply checklists
- Generate reports
"""
        }
    }
    
    # Format each phase
    for phase_num, phase_info in phase_examples.items():
        print(f"--- Formatting Phase {phase_num}: {phase_info['name']} ---")
        
        # Format the phase protocol
        formatted_content, validation_result = formatter.format_phase_protocol(
            phase_info['content'], 
            phase_num
        )
        
        print(f"Validation: {'PASSED' if validation_result.is_valid else 'FAILED'}")
        if validation_result.errors:
            print(f"Errors: {validation_result.errors}")
        if validation_result.warnings:
            print(f"Warnings: {validation_result.warnings}")
        
        print(f"Formatted content length: {len(formatted_content)} characters")
        print(f"Enhanced with phase-specific formatting: {'Yes' if 'Rule Formatting Protocol' in formatted_content or 'Quality Gate Formatting' in formatted_content else 'No'}")
        print()
    
    # Demo instruction type classification
    print("--- Instruction Type Classification ---")
    test_contents = [
        "This is a governance rule about compliance and standards",
        "This is a process workflow with steps and procedures", 
        "This is a technical policy about code implementation",
        "This is about formatting and parsing validation structure"
    ]
    
    for content in test_contents:
        instruction_type = formatter.classify_instruction_type(content)
        print(f"'{content[:50]}...' → {instruction_type.value}")
    
    print()
    
    # Demo directive normalization
    print("--- Directive Normalization ---")
    content_with_aliases = """
### [MUST] Do something
- This is required

### [IMPORTANT] Consider this  
- This is a guideline

### [SHOULD] Maybe do this
- This is optional
"""
    
    normalized = formatter.normalize_directives(content_with_aliases)
    print("Original:")
    print(content_with_aliases)
    print("Normalized:")
    print(normalized)
    print()
    
    # Demo validation
    print("--- Structure Validation ---")
    valid_content = """---
description: "Test rule"
---

# Test Rule

## AI Persona
Test persona

## Core Principle
Test principle

## Protocol
Test protocol
"""
    
    validation_result = formatter.validate_structure(valid_content, InstructionType.GOVERNANCE)
    print(f"Validation: {'PASSED' if validation_result.is_valid else 'FAILED'}")
    if validation_result.errors:
        print(f"Errors: {validation_result.errors}")
    if validation_result.warnings:
        print(f"Warnings: {validation_result.warnings}")
    
    print("\n=== Demo Complete ===")

def demo_cli_usage():
    """Demonstrate CLI usage"""
    print("\n=== CLI Usage Examples ===")
    print("Format a file:")
    print("  python3 automation/system_instruction_formatter.py input.md --output formatted.md")
    print()
    print("Validate only:")
    print("  python3 automation/system_instruction_formatter.py input.md --validate-only")
    print()
    print("Force instruction type:")
    print("  python3 automation/system_instruction_formatter.py input.md --instruction-type governance")

if __name__ == "__main__":
    demo_phase_formatting()
    demo_cli_usage()
