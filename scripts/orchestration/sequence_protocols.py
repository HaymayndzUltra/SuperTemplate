#!/usr/bin/env python3
"""
Sequence Protocols
Determines optimal execution sequence based on dependency graph.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

def topological_sort(graph: dict) -> list:
    """Perform topological sort on dependency graph."""
    
    nodes = {n['id']: n for n in graph.get('nodes', [])}
    
    # Build adjacency list and in-degree
    adj = {node_id: [] for node_id in nodes}
    in_degree = {node_id: 0 for node_id in nodes}
    
    for edge in graph.get('edges', []):
        from_node = edge['from']
        to_node = edge['to']
        if from_node in adj and to_node in in_degree:
            adj[from_node].append(to_node)
            in_degree[to_node] += 1
    
    # Kahn's algorithm
    queue = [node_id for node_id, degree in in_degree.items() if degree == 0]
    sorted_order = []
    
    while queue:
        # Sort by level for consistent ordering
        queue.sort(key=lambda x: nodes[x].get('level', 0))
        node = queue.pop(0)
        sorted_order.append(node)
        
        for neighbor in adj.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

def group_by_phase(sorted_protocols: list, graph: dict) -> list:
    """Group protocols into execution phases."""
    
    nodes = {n['id']: n for n in graph.get('nodes', [])}
    
    phases = []
    current_phase = []
    current_level = 0
    
    for protocol_id in sorted_protocols:
        node = nodes.get(protocol_id, {})
        level = node.get('level', 0)
        
        if level != current_level and current_phase:
            phases.append({
                "phase_number": len(phases) + 1,
                "level": current_level,
                "protocols": current_phase
            })
            current_phase = []
            current_level = level
        
        current_phase.append({
            "id": protocol_id,
            "name": node.get('name', f'Protocol {protocol_id}'),
            "track": node.get('track', 'generic'),
            "level": level
        })
    
    if current_phase:
        phases.append({
            "phase_number": len(phases) + 1,
            "level": current_level,
            "protocols": current_phase
        })
    
    return phases

def generate_sequence(sorted_protocols: list, graph: dict) -> list:
    """Generate detailed execution sequence."""
    
    nodes = {n['id']: n for n in graph.get('nodes', [])}
    
    # Build dependency lookup
    dependencies = {}
    for edge in graph.get('edges', []):
        to_node = edge['to']
        if to_node not in dependencies:
            dependencies[to_node] = []
        dependencies[to_node].append(edge['from'])
    
    sequence = []
    for i, protocol_id in enumerate(sorted_protocols):
        node = nodes.get(protocol_id, {})
        
        sequence.append({
            "sequence_number": i + 1,
            "protocol_id": protocol_id,
            "protocol_name": node.get('name', f'Protocol {protocol_id}'),
            "track": node.get('track', 'generic'),
            "level": node.get('level', 0),
            "dependencies": dependencies.get(protocol_id, []),
            "can_start_after": dependencies.get(protocol_id, [])[-1] if dependencies.get(protocol_id) else None
        })
    
    return sequence

def main():
    parser = argparse.ArgumentParser(description='Sequence protocols for execution')
    parser.add_argument('--graph', required=True, help='Path to dependency-graph.json')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 5] Sequencing protocols...")
    
    # Load graph data
    graph_path = Path(args.graph)
    if not graph_path.is_absolute():
        graph_path = workspace / graph_path
    
    with open(graph_path, 'r', encoding='utf-8') as f:
        graph_data = json.load(f)
    
    graph = graph_data.get('graph', {})
    
    # Check for cycles
    if graph_data.get('has_cycles'):
        print(f"[ERROR] Cannot sequence - dependency graph has cycles")
        return 1
    
    # Perform topological sort
    sorted_protocols = topological_sort(graph)
    
    # Group into phases
    phases = group_by_phase(sorted_protocols, graph)
    
    # Generate detailed sequence
    sequence = generate_sequence(sorted_protocols, graph)
    
    # Build output
    output = {
        "timestamp": datetime.now().isoformat(),
        "execution_order": sorted_protocols,
        "phases": phases,
        "sequence": sequence,
        "summary": {
            "total_protocols": len(sorted_protocols),
            "total_phases": len(phases),
            "estimated_execution_units": len(sorted_protocols)
        },
        "input_files": {
            "graph": str(graph_path)
        }
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'protocol-sequence.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 5] Protocol sequencing complete")
    print(f"  - Total protocols: {output['summary']['total_protocols']}")
    print(f"  - Execution phases: {output['summary']['total_phases']}")
    print(f"  - Order: {' -> '.join(sorted_protocols)}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
