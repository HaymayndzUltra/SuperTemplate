#!/usr/bin/env python3
"""
Enhance AUTOMATION HOOKS sections with detailed specifications
"""

import json
import re
from pathlib import Path

def load_registry():
    """Load script registry"""
    registry_file = Path("/home/haymayndz/SuperTemplate/scripts/script-registry.json")
    with open(registry_file, 'r') as f:
        return json.load(f)

def get_protocol_scripts(protocol_num, registry):
    """Get scripts for a specific protocol"""
    scripts = []
    
    # Check protocol-specific validators
    key = f"protocol-{protocol_num:02d}-validators"
    if key in registry.get("protocol-gates", {}):
        scripts.extend(registry["protocol-gates"][key])
    
    # Add evidence aggregation if available
    evidence_scripts = registry.get("protocol-gates", {}).get("evidence-aggregation", [])
    for script in evidence_scripts:
        if f"aggregate_evidence_{protocol_num:02d}" in script:
            scripts.append(script)
    
    # Add gate runner
    scripts.append("scripts/run_protocol_gates.py")
    
    return list(set(scripts))

def build_commands_section(protocol_num, scripts):
    """Build automation commands section"""
    
    commands = f"""#### Command 1: Pre-Execution Validation
```bash
python3 scripts/validate_prerequisites_{protocol_num:02d}.py \\
  --protocol {protocol_num:02d} \\
  --workspace . \\
  --strict
```
**Flags:**
- `--protocol {protocol_num:02d}` - Protocol ID to validate
- `--workspace .` - Workspace root directory
- `--strict` - Enforce strict validation

**Output:** `.artifacts/protocol-{protocol_num:02d}/prerequisites-validation.json`
**Exit Codes:** 0=success, 1=validation failed, 2=prerequisites missing

#### Command 2: Protocol Execution
```bash
python3 scripts/run_protocol_gates.py \\
  --protocol {protocol_num:02d} \\
  --input .artifacts/protocol-{protocol_num:02d}/input/ \\
  --output .artifacts/protocol-{protocol_num:02d}/output/ \\
  --log-file .artifacts/protocol-{protocol_num:02d}/execution.log \\
  --error-handling retry
```
**Flags:**
- `--protocol {protocol_num:02d}` - Protocol ID
- `--input DIR` - Input artifacts directory
- `--output DIR` - Output artifacts directory
- `--log-file FILE` - Execution log file path
- `--error-handling {{retry|escalate|halt}}` - Error handling strategy

**Output:** `.artifacts/protocol-{protocol_num:02d}/output/`
**Exit Codes:** 0=success, 1=execution error, 2=validation gate failed

#### Command 3: Evidence Aggregation
```bash
python3 scripts/aggregate_evidence_{protocol_num:02d}.py \\
  --protocol {protocol_num:02d} \\
  --artifacts-dir .artifacts/protocol-{protocol_num:02d}/ \\
  --output-manifest \\
  --checksum sha256
```
**Flags:**
- `--protocol {protocol_num:02d}` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--output-manifest` - Generate manifest file
- `--checksum {{md5|sha256}}` - Checksum algorithm

**Output:** `.artifacts/protocol-{protocol_num:02d}/EVIDENCE-MANIFEST.json`
**Exit Codes:** 0=success, 1=aggregation failed

#### Command 4: Post-Execution Validation
```bash
python3 scripts/validate_protocol_{protocol_num:02d}.py \\
  --protocol {protocol_num:02d} \\
  --artifacts-dir .artifacts/protocol-{protocol_num:02d}/ \\
  --quality-gates strict \\
  --report json
```
**Flags:**
- `--protocol {protocol_num:02d}` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--quality-gates {{strict|standard|relaxed}}` - Gate strictness
- `--report {{json|html|text}}` - Report format

**Output:** `.artifacts/protocol-{protocol_num:02d}/validation-report.json`
**Exit Codes:** 0=all gates pass, 1=gate failure, 2=critical error
"""
    
    return commands

def build_error_handling_section():
    """Build error handling section"""
    
    return """**If Command 1 (Prerequisites) Fails:**
1. Check log: `.artifacts/protocol-XX/prerequisites-validation.json`
2. Verify all input artifacts exist
3. Ensure all environment variables are set
4. **Fallback:** Run with `--strict=false`
5. **Escalate:** Notify Protocol Owner if still failing

**If Command 2 (Execution) Fails:**
1. Check log: `.artifacts/protocol-XX/execution.log`
2. Review error code and message
3. **Retry:** Re-run with `--error-handling retry` (up to 3 times)
4. **Fallback:** Run with `--error-handling escalate`
5. **Escalate:** Notify supervisor with logs

**If Command 3 (Aggregation) Fails:**
1. Verify all artifacts present in output directory
2. Check artifact file formats and integrity
3. **Fallback:** Run without `--output-manifest`
4. **Escalate:** If artifacts corrupted, restart from Command 2

**If Command 4 (Validation) Fails:**
1. Review validation report
2. Identify which quality gates failed
3. **Fallback:** Run with `--quality-gates relaxed`
4. **Escalate:** Return to Command 2 and remediate"""

def get_automation_hooks_template(protocol_num, registry):
    """Generate automation hooks content for protocol"""
    
    scripts = get_protocol_scripts(protocol_num, registry)
    commands = build_commands_section(protocol_num, scripts)
    error_handling = build_error_handling_section()
    
    template = f"""## AUTOMATION HOOKS

### Pre-Execution Setup

**Environment Variables:**
- `PROTOCOL_ID={protocol_num:02d}` - Protocol identifier
- `WORKSPACE_ROOT=.` - Root workspace directory
- `ARTIFACTS_DIR=.artifacts/protocol-{protocol_num:02d}/` - Artifacts storage location
- `LOG_LEVEL=INFO` - Logging verbosity (DEBUG, INFO, WARNING, ERROR)

**Required Permissions:**
- Read access to: `.cursor/ai-driven-workflow/{protocol_num:02d}-*.md`, `.artifacts/`
- Write access to: `.artifacts/protocol-{protocol_num:02d}/`, `scripts/logs/`
- Execute access to: `scripts/validate_*.py`, `scripts/aggregate_*.py`

**System Dependencies:**
- Python 3.8+
- bash/sh shell
- Standard Unix utilities (grep, sed, awk)

### Automation Commands

{commands}

### Error Handling & Fallback Procedures

{error_handling}

### Scheduling & Execution Context

**Execution Timing:**
- Pre-execution: 5 minutes (setup + prerequisites validation)
- Main execution: 15-45 minutes (depends on protocol complexity)
- Post-execution: 10 minutes (aggregation + validation)
- Total: 30-60 minutes per protocol

**Parallel Execution:** Can run up to 4 protocols in parallel (if resources allow)

**CI/CD Integration:**
- Trigger on: Protocol file changes, manual trigger
- Timeout: 90 minutes per protocol
- Retry policy: 2 retries on transient failures
- Notification: Slack/Email on success/failure

### Monitoring & Logging

**Log Files:**
- `.artifacts/protocol-{protocol_num:02d}/execution.log` - Main execution log
- `.artifacts/protocol-{protocol_num:02d}/validation.log` - Validation log
- `.artifacts/protocol-{protocol_num:02d}/error.log` - Error log (if any)

**Status Files:**
- `.artifacts/protocol-{protocol_num:02d}/workflow-status.json` - Real-time status
- `.artifacts/protocol-{protocol_num:02d}/workflow-metrics.json` - Performance metrics

**Checkpoints:**
- After prerequisites validation
- After each command execution
- Before handoff to next protocol

### Success Criteria

✅ All commands execute successfully (exit code 0)
✅ All quality gates pass (validation report shows PASS)
✅ Evidence manifest generated and checksums verified
✅ All artifacts stored in `.artifacts/protocol-{protocol_num:02d}/`
✅ No errors in execution, validation, or aggregation logs
✅ Protocol ready for handoff to next protocol

---"""
    
    return template

def enhance_protocol(file_path, protocol_num, registry):
    """Enhance protocol's AUTOMATION HOOKS section"""
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find AUTOMATION HOOKS section
    if "## AUTOMATION HOOKS" not in content:
        print(f"Protocol {protocol_num:02d}: No AUTOMATION HOOKS section found")
        return False
    
    # Find the section boundaries
    start = content.find("## AUTOMATION HOOKS")
    
    # Find the next section (## or end of file)
    next_section = content.find("\n## ", start + 1)
    if next_section == -1:
        next_section = len(content)
    
    # Replace the section
    old_section = content[start:next_section]
    new_section = get_automation_hooks_template(protocol_num, registry)
    
    content = content.replace(old_section, new_section)
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    return True

def main():
    """Process all protocols"""
    registry = load_registry()
    workflow_dir = Path("/home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow")
    
    for protocol_num in range(1, 24):
        files = list(workflow_dir.glob(f"{protocol_num:02d}-*.md"))
        if not files:
            print(f"Protocol {protocol_num:02d}: File not found")
            continue
        
        file_path = files[0]
        print(f"Enhancing Protocol {protocol_num:02d}: {file_path.name}")
        
        if enhance_protocol(file_path, protocol_num, registry):
            print(f"✅ Protocol {protocol_num:02d} automation hooks enhanced")
        else:
            print(f"⏭️  Protocol {protocol_num:02d} skipped")
    
    print("\n✅ All protocols automation hooks enhanced!")

if __name__ == "__main__":
    main()
