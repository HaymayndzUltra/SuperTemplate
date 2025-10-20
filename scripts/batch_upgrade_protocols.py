#!/usr/bin/env python3
"""
Batch Protocol Upgrade Script
Applies standard validation improvements to multiple protocols.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List

# Standard section templates
PURPOSE_TEMPLATE = """
**Purpose:** {purpose_description}
"""

REASONING_SECTION = """
## REASONING & COGNITIVE PROCESS

### Reasoning Patterns

**Primary Reasoning Pattern: {primary_pattern}**
- {primary_description}

**Secondary Reasoning Pattern: {secondary_pattern}**
- {secondary_description}

**Pattern Improvement Strategy:**
- Track pattern effectiveness via quality gate pass rates and downstream protocol feedback
- Quarterly review identifies pattern weaknesses and optimization opportunities
- Iterate patterns based on empirical evidence from completed executions

### Decision Logic

{decision_points}

### Root Cause Analysis Framework

When protocol execution encounters blockers or quality gate failures:

1. **Identify Symptom:** What immediate issue prevented progress?
2. **Trace to Root Cause:**
   - Was prerequisite artifact missing or incomplete?
   - Did upstream protocol deliver inadequate inputs?
   - Were instructions ambiguous or insufficient?
   - Did environmental conditions fail?
3. **Document in Protocol Execution Log:**
   ```markdown
   **Blocker:** [Description]
   **Root Cause:** [Analysis]
   **Resolution:** [Action taken]
   **Prevention:** [Process/template update to prevent recurrence]
   ```
4. **Implement Fix:** Update protocol, re-engage stakeholders, adjust execution
5. **Validate Fix:** Re-run quality gates, confirm resolution

### Learning Mechanisms

#### Feedback Loops
**Purpose:** Establish continuous feedback collection to inform protocol improvements.

- **Execution feedback:** Collect outcome data after each protocol execution
- **Quality gate outcomes:** Track gate pass/fail patterns in historical logs
- **Downstream protocol feedback:** Capture issues reported by dependent protocols
- **Continuous monitoring:** Automated alerts for anomalies and degradation

#### Improvement Tracking
**Purpose:** Systematically track protocol effectiveness improvements over time.

- **Metrics tracking:** Monitor key performance indicators in quarterly dashboards
- **Template evolution:** Log all protocol template changes with rationale and impact
- **Effectiveness measurement:** Compare before/after metrics for each improvement
- **Continuous monitoring:** Automated alerts when metrics degrade

#### Knowledge Base Integration
**Purpose:** Build and leverage institutional knowledge to accelerate protocol quality.

- **Pattern library:** Maintain repository of successful execution patterns
- **Best practices:** Document proven approaches for common scenarios
- **Common blockers:** Catalog typical issues with proven resolutions
- **Industry templates:** Specialized variations for specific domains

#### Adaptation Mechanisms
**Purpose:** Enable protocol to automatically adjust based on context and patterns.

- **Context adaptation:** Adjust execution based on project type, complexity, constraints
- **Threshold tuning:** Modify quality gate thresholds based on risk tolerance
- **Workflow optimization:** Streamline steps based on historical efficiency data
- **Tool selection:** Choose optimal automation based on available resources

### Meta-Cognition

#### Self-Awareness and Process Awareness
**Purpose:** Enable AI to maintain explicit awareness of execution state and limitations.

**Awareness Statement Protocol:**
At each major execution checkpoint, generate awareness statement:
- Current phase and step status
- Artifacts completed vs. pending
- Identified blockers and their severity
- Confidence level in current outputs
- Known limitations and assumptions
- Required inputs for next steps

#### Process Monitoring and Progress Tracking
**Purpose:** Continuously track execution status and detect anomalies.

- **Progress tracking:** Update execution status after each step
- **Velocity monitoring:** Flag execution delays beyond expected duration
- **Quality monitoring:** Track gate pass rates and artifact completeness
- **Anomaly detection:** Alert on unexpected patterns or deviations

#### Self-Correction Protocols
**Purpose:** Enable autonomous detection and correction of execution issues.

- **Halt condition detection:** Recognize blockers and escalate appropriately
- **Quality gate failure handling:** Generate corrective action plans
- **Anomaly response:** Diagnose and propose fixes for unexpected conditions
- **Recovery procedures:** Maintain execution state for graceful resume

#### Continuous Improvement Integration
**Purpose:** Systematically capture lessons and evolve protocol effectiveness.

- **Retrospective execution:** Conduct after-action reviews post-completion
- **Template review cadence:** Scheduled protocol enhancement cycles
- **Gate calibration:** Periodic adjustment of pass criteria
- **Tool evaluation:** Assessment of automation effectiveness
"""

REFLECTION_SECTION = """
## REFLECTION & LEARNING

### Retrospective Guidance

After completing protocol execution (successful or halted), conduct retrospective:

**Timing:** Within 24-48 hours of completion

**Participants:** Protocol executor, downstream consumers, stakeholders

**Agenda:**
1. **What went well:**
   - Which steps executed smoothly and efficiently?
   - Which quality gates were well-calibrated?
   - Which artifacts provided high value to downstream protocols?

2. **What went poorly:**
   - Which steps encountered blockers or delays?
   - Which quality gates were too strict or too lenient?
   - Which artifacts required rework or clarification?

3. **Action items:**
   - Protocol template updates needed?
   - Quality gate threshold adjustments?
   - New automation opportunities?

**Output:** Retrospective report stored in protocol execution artifacts

### Continuous Improvement Opportunities

#### Identified Improvement Opportunities
{improvement_opportunities}

#### Process Optimization Tracking
- Track key performance metrics over time
- Monitor quality gate pass rates and execution velocity
- Measure downstream satisfaction and rework requests
- Identify automation opportunities

#### Tracking Mechanisms and Metrics
- Quarterly metrics dashboard with trends
- Improvement tracking log with before/after comparisons
- Evidence of improvement validation

#### Evidence of Improvement and Validation
- Metric trends showing improvement trajectories
- A/B testing results for protocol changes
- Stakeholder feedback scores
- Downstream protocol satisfaction ratings

### System Evolution

#### Version History
- Current version with implementation date
- Previous versions with change descriptions
- Deprecation notices for obsolete approaches

#### Rationale for Changes
- Documented reasons for each protocol evolution
- Evidence supporting the change decision
- Expected impact assessment

#### Impact Assessment
- Measured outcomes of protocol changes
- Comparison against baseline metrics
- Validation of improvement hypotheses

#### Rollback Procedures
- Process for reverting to previous protocol version
- Triggers for initiating rollback
- Communication plan for rollback events

### Knowledge Capture and Organizational Learning

#### Lessons Learned Repository
Maintain lessons learned with structure:
- Project/execution context
- Insight or discovery
- Action taken based on insight
- Outcome and applicability

#### Knowledge Base Growth
- Systematic extraction of patterns from executions
- Scheduled knowledge base updates
- Quality metrics for knowledge base content

#### Knowledge Sharing Mechanisms
- Internal distribution channels
- Onboarding integration
- Cross-team learning sessions
- Access controls and search tools

### Future Planning

#### Roadmap
- Planned enhancements with timelines
- Integration with other protocols
- Automation expansion plans

#### Priorities
- Ranked list of improvement initiatives
- Resource requirements
- Expected benefits

#### Resource Requirements
- Development effort estimates
- Tool or infrastructure needs
- Team capacity planning

#### Timeline
- Milestone dates for major enhancements
- Dependencies on other work
- Risk buffers and contingencies
"""


def extract_protocol_metadata(content: str) -> Dict[str, str]:
    """Extract protocol number and title."""
    match = re.search(r'# PROTOCOL (\d+):\s+(.+?)(?:\s+\(|$)', content, re.IGNORECASE)
    if match:
        return {'number': match.group(1), 'title': match.group(2).strip()}
    return {'number': '00', 'title': 'Unknown Protocol'}


def has_section(content: str, section_name: str) -> bool:
    """Check if protocol already has a section."""
    pattern = rf'^##\s+(?:\d+\.\s+)?{re.escape(section_name)}'
    return bool(re.search(pattern, content, re.MULTILINE | re.IGNORECASE))


def add_purpose_statement(content: str, purpose: str) -> str:
    """Add Purpose statement after protocol title."""
    if '**Purpose:**' in content:
        return content  # Already has purpose
    
    # Find title line and add purpose after it
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('# PROTOCOL'):
            lines.insert(i + 1, f'\n**Purpose:** {purpose}')
            return '\n'.join(lines)
    
    return content


def add_reasoning_section(content: str, reasoning_config: Dict) -> str:
    """Add REASONING & COGNITIVE PROCESS section."""
    if has_section(content, 'REASONING & COGNITIVE PROCESS'):
        return content  # Already has section
    
    # Format decision points
    decision_points_text = ""
    for i, dp in enumerate(reasoning_config.get('decision_points', []), 1):
        decision_points_text += f"""
#### Decision Point {i}: {dp['name']}
**Context:** {dp['context']}

**Decision Criteria:**
{dp['criteria']}

**Outcomes:**
{dp['outcomes']}

**Logging:** {dp['logging']}

"""
    
    reasoning = REASONING_SECTION.format(
        primary_pattern=reasoning_config.get('primary_pattern', 'Systematic Execution'),
        primary_description=reasoning_config.get('primary_description', 'Execute protocol steps sequentially with validation at each checkpoint'),
        secondary_pattern=reasoning_config.get('secondary_pattern', 'Quality-Driven Validation'),
        secondary_description=reasoning_config.get('secondary_description', 'Apply quality gates to ensure artifact completeness before handoff'),
        decision_points=decision_points_text.strip()
    )
    
    # Insert before INTEGRATION POINTS or at end
    if '## INTEGRATION POINTS' in content or '## 02. INTEGRATION POINTS' in content:
        pattern = r'(---\s*\n\n)(##\s+(?:\d+\.\s+)?INTEGRATION POINTS)'
        replacement = f'\\1{reasoning}\n\n---\n\n\\2'
        content = re.sub(pattern, replacement, content)
    else:
        content += '\n\n---\n\n' + reasoning
    
    return content


def add_reflection_section(content: str, reflection_config: Dict) -> str:
    """Add REFLECTION & LEARNING section."""
    if has_section(content, 'REFLECTION & LEARNING'):
        return content  # Already has section
    
    opportunities = reflection_config.get('improvement_opportunities', """
**Opportunity 1:** [Description of improvement area]
- Current state: [As-is]
- Opportunity: [Proposed improvement]
- Impact: [Expected benefit]
- Priority: [High/Medium/Low]
- Timeline: [Target quarter]
""")
    
    reflection = REFLECTION_SECTION.format(
        improvement_opportunities=opportunities
    )
    
    # Insert before INTEGRATION POINTS or after REASONING
    if has_section(content, 'REASONING & COGNITIVE PROCESS'):
        pattern = r'(---\s*\n\n)(##\s+(?:\d+\.\s+)?INTEGRATION POINTS)'
        replacement = f'\\1{reflection}\n\n---\n\n\\2'
        content = re.sub(pattern, replacement, content)
    else:
        content += '\n\n---\n\n' + reflection
    
    return content


def upgrade_protocol(protocol_path: Path, config: Dict) -> bool:
    """Apply standard upgrades to a protocol file."""
    try:
        content = protocol_path.read_text()
        original_content = content
        
        # 1. Add Purpose statement
        if config.get('purpose'):
            content = add_purpose_statement(content, config['purpose'])
        
        # 2. Fix WORKFLOW section name (if needed)
        content = re.sub(
            r'^##\s+\d+\.\s+([A-Z\s]+WORKFLOW)',
            r'## WORKFLOW',
            content,
            flags=re.MULTILINE
        )
        
        # 3. Add REASONING section
        if config.get('reasoning'):
            content = add_reasoning_section(content, config['reasoning'])
        
        # 4. Add REFLECTION section
        if config.get('reflection'):
            content = add_reflection_section(content, config['reflection'])
        
        # Only write if changes were made
        if content != original_content:
            protocol_path.write_text(content)
            print(f"✅ Upgraded: {protocol_path.name}")
            return True
        else:
            print(f"⏭️  Skipped: {protocol_path.name} (already complete)")
            return False
            
    except Exception as e:
        print(f"❌ Error upgrading {protocol_path.name}: {e}")
        return False


def main():
    """Main execution."""
    if len(sys.argv) < 2:
        print("Usage: python batch_upgrade_protocols.py <protocol_numbers...>")
        print("Example: python batch_upgrade_protocols.py 08 14 23 12")
        sys.exit(1)
    
    protocols_dir = Path(__file__).parent.parent / '.cursor' / 'ai-driven-workflow'
    protocol_numbers = sys.argv[1:]
    
    upgraded_count = 0
    
    for protocol_num in protocol_numbers:
        protocol_num = protocol_num.zfill(2)
        protocol_files = list(protocols_dir.glob(f"{protocol_num}-*.md"))
        
        if not protocol_files:
            print(f"⚠️  Protocol {protocol_num} not found")
            continue
        
        protocol_file = protocol_files[0]
        
        # Read protocol to determine config
        metadata = extract_protocol_metadata(protocol_file.read_text())
        
        # Standard config (can be customized per protocol)
        config = {
            'purpose': f"Execute {metadata['title']} workflow with quality validation and evidence generation.",
            'reasoning': {
                'primary_pattern': 'Systematic Execution',
                'primary_description': 'Execute protocol steps sequentially with validation at each checkpoint',
                'secondary_pattern': 'Quality-Driven Validation',
                'secondary_description': 'Apply quality gates to ensure artifact completeness before downstream handoff',
                'decision_points': [
                    {
                        'name': 'Execution Readiness',
                        'context': 'Determining if prerequisites are met to begin protocol execution',
                        'criteria': '- All prerequisite artifacts present\n- Required approvals obtained\n- System state validated',
                        'outcomes': '- Proceed: Execute protocol workflow\n- Halt: Document missing prerequisites, notify stakeholders',
                        'logging': 'Record decision and prerequisites status in execution log'
                    }
                ]
            },
            'reflection': {
                'improvement_opportunities': '- Identify based on protocol-specific execution patterns'
            }
        }
        
        if upgrade_protocol(protocol_file, config):
            upgraded_count += 1
    
    print(f"\n📊 Summary: Upgraded {upgraded_count}/{len(protocol_numbers)} protocols")


if __name__ == '__main__':
    main()
