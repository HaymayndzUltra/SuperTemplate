#!/bin/bash
# Script to add --protocol-dir support to all validator scripts

VALIDATORS=(
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

for validator in "${VALIDATORS[@]}"; do
    echo "Updating $validator..."
    
    # Add protocol_dir parameter to __init__ if using get_protocol_file
    sed -i 's/def __init__(self, workspace_root: Path) -> None:/def __init__(self, workspace_root: Path, protocol_dir: Path = None) -> None:/' "$validator"
    
    # Store protocol_dir if __init__ exists
    sed -i '/self.workspace_root = workspace_root/a\        self.protocol_dir = protocol_dir' "$validator"
    
    # Update get_protocol_file calls to include protocol_dir
    sed -i 's/get_protocol_file(self.workspace_root, protocol_id)/get_protocol_file(self.workspace_root, protocol_id, self.protocol_dir)/g' "$validator"
    
    # Add --protocol-dir argument before the closing args = parser.parse_args()
    sed -i '/parser.add_argument/{N; /parser.add_argument.*--workspace/a\    parser.add_argument(\n        "--protocol-dir",\n        help="Custom protocol directory path (default: .cursor/ai-driven-workflow)"\n    )
}' "$validator"
    
    # Add protocol_dir parsing and pass to validator init
    sed -i '/workspace_root = Path(args.workspace).resolve()/a\    protocol_dir = Path(args.protocol_dir).resolve() if hasattr(args, "protocol_dir") and args.protocol_dir else None' "$validator"
    
    # Update validator instantiation
    sed -i 's/validator = \([A-Za-z]*\)Validator(workspace_root)/validator = \1Validator(workspace_root, protocol_dir)/g' "$validator"
    
    echo "✓ Updated $validator"
done

echo "All validators updated!"
