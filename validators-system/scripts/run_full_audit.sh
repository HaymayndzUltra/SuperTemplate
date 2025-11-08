#!/bin/bash
#  Script to run all 10 validators on specified protocols

# Check arguments
if [ $# -lt 2 ]; then
    echo "Usage: $0 <workspace_root> <protocol_dir> [protocol_ids...]"
    echo "Example: $0 /home/user/SuperTemplate /home/user/SuperTemplate/.cursor/AI-project-workflow 06 07 08 09"
    exit 1
fi

WORKSPACE=$1
PROTOCOL_DIR=$2
shift 2
PROTOCOLS=("$@")

# If no protocols specified, prompt
if [ ${#PROTOCOLS[@]} -eq 0 ]; then
    echo "No protocols specified. Please provide protocol IDs."
    exit 1
fi

VALIDATORS=(
    "validate_protocol_identity.py"
    "validate_protocol_role.py"
    "validate_protocol_workflow.py"
    "validate_protocol_gates.py"
    "validate_protocol_scripts.py"
    "validate_protocol_communication.py"
    "validate_protocol_evidence.py"
    "validate_protocol_handoff.py"
    "validate_protocol_reasoning.py"
    "validate_protocol_reflection.py"
)

echo "================================================================"
echo "  MASTER RAY™ Protocol Quality Audit"
echo "================================================================"
echo "Workspace: $WORKSPACE"
echo "Protocol Dir: $PROTOCOL_DIR"
echo "Protocols: ${PROTOCOLS[@]}"
echo "================================================================"
echo ""

for protocol_id in "${PROTOCOLS[@]}"; do
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  Protocol $protocol_id - Running All Validators"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    for validator in "${VALIDATORS[@]}"; do
        validator_name=$(basename "$validator" .py)
        echo -n "  ├─ ${validator_name}..."
        
        output=$(python3 "$validator" \
            --protocol "$protocol_id" \
            --workspace "$WORKSPACE" \
            --protocol-dir "$PROTOCOL_DIR" 2>&1)
        
        exit_code=$?
        
        if [ $exit_code -eq 0 ]; then
            echo " ✅ PASS"
        elif [ $exit_code -eq 1 ]; then
            echo " ❌ FAIL"
        else
            echo " ⚠️  ERROR"
            echo "$output" | grep -i "error" | head -2
        fi
    done
    
    echo ""
done

echo "================================================================"
echo "Validation reports saved to: $WORKSPACE/.artifacts/validation/"
echo "================================================================"
