#!/usr/bin/env python3
"""
Build Dependency Graph
Builds protocol dependency graph for execution sequencing.
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

# Protocol dependencies (protocol_id: [depends_on])
PROTOCOL_DEPENDENCIES = {
    "01": [],
    "02": ["01"],
    "03": ["02"],
    "04": ["03"],
    "05": ["04"],
    "05b": ["05"],
    "06": ["05b"],
    "07": ["06"],
    "08": ["07"],
    "09": ["08"],
    "10": ["09"],
    "11": ["10"],
    "12": ["11"],
    "13": ["12"],
    "14": ["13"],
    "15": ["14"],
    "16": ["15"],
    "17": ["16"],
    "18": ["05"],
    "19": ["05"],
    "20": ["18", "19"],
    "21": ["20"],
    "22": ["05"],
    "23": ["05"],
    "AR": ["05"],
    "CR": ["05"],
    "SR": ["05"]
}

def build_graph(selected_protocols: list) -> dict:
    """Build dependency graph from selected protocols."""
    
    # Extract protocol IDs
    protocol_ids = [p.get('id') for p in selected_protocols]
    
    # Build adjacency list
    graph = {
        "nodes": [],
        "edges": []
    }
    
    for protocol in selected_protocols:
        protocol_id = protocol.get('id')
        
        # Add node
        graph['nodes'].append({
            "id": protocol_id,
            "name": protocol.get('name'),
            "track": protocol.get('track'),
            "category": protocol.get('category', 'required')
        })
        
        # Add edges for dependencies
        dependencies = PROTOCOL_DEPENDENCIES.get(protocol_id, [])
        for dep in dependencies:
            if dep in protocol_ids:
                graph['edges'].append({
                    "from": dep,
                    "to": protocol_id,
                    "type": "depends_on"
                })
    
    return graph

def detect_cycles(graph: dict) -> list:
    """Detect cycles in dependency graph using DFS."""
    
    cycles = []
    nodes = {n['id'] for n in graph['nodes']}
    
    # Build adjacency list
    adj = {node: [] for node in nodes}
    for edge in graph['edges']:
        if edge['from'] in adj:
            adj[edge['from']].append(edge['to'])
    
    # DFS for cycle detection
    visited = set()
    rec_stack = set()
    
    def dfs(node, path):
        visited.add(node)
        rec_stack.add(node)
        path.append(node)
        
        for neighbor in adj.get(node, []):
            if neighbor not in visited:
                result = dfs(neighbor, path)
                if result:
                    return result
            elif neighbor in rec_stack:
                # Cycle found
                cycle_start = path.index(neighbor)
                return path[cycle_start:] + [neighbor]
        
        path.pop()
        rec_stack.remove(node)
        return None
    
    for node in nodes:
        if node not in visited:
            cycle = dfs(node, [])
            if cycle:
                cycles.append(cycle)
    
    return cycles

def calculate_levels(graph: dict) -> dict:
    """Calculate execution levels (topological sort with levels)."""
    
    nodes = {n['id'] for n in graph['nodes']}
    
    # Build in-degree map
    in_degree = {node: 0 for node in nodes}
    adj = {node: [] for node in nodes}
    
    for edge in graph['edges']:
        if edge['to'] in in_degree:
            in_degree[edge['to']] += 1
        if edge['from'] in adj:
            adj[edge['from']].append(edge['to'])
    
    # BFS for level assignment
    levels = {}
    current_level = 0
    queue = [node for node in nodes if in_degree[node] == 0]
    
    while queue:
        next_queue = []
        for node in queue:
            levels[node] = current_level
            for neighbor in adj.get(node, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    next_queue.append(neighbor)
        queue = next_queue
        current_level += 1
    
    return levels

def main():
    parser = argparse.ArgumentParser(description='Build protocol dependency graph')
    parser.add_argument('--selection', required=True, help='Path to protocol-selection.json')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--workspace', default='.', help='Workspace root path')
    args = parser.parse_args()
    
    workspace = Path(args.workspace).resolve()
    
    print(f"[PROTOCOL 05B | PHASE 5] Building dependency graph...")
    
    # Load selection data
    selection_path = Path(args.selection)
    if not selection_path.is_absolute():
        selection_path = workspace / selection_path
    
    with open(selection_path, 'r', encoding='utf-8') as f:
        selection_data = json.load(f)
    
    # Get all selected protocols
    selected = selection_data.get('selected_protocols', {})
    all_protocols = (
        selected.get('required', []) +
        selected.get('recommended', [])
    )
    
    # Build graph
    graph = build_graph(all_protocols)
    
    # Detect cycles
    cycles = detect_cycles(graph)
    
    # Calculate execution levels
    levels = calculate_levels(graph)
    
    # Add levels to nodes
    for node in graph['nodes']:
        node['level'] = levels.get(node['id'], 0)
    
    # Build output
    output = {
        "timestamp": datetime.now().isoformat(),
        "graph": graph,
        "levels": levels,
        "cycles_detected": cycles,
        "has_cycles": len(cycles) > 0,
        "summary": {
            "total_nodes": len(graph['nodes']),
            "total_edges": len(graph['edges']),
            "max_level": max(levels.values()) if levels else 0,
            "valid_dag": len(cycles) == 0
        },
        "input_files": {
            "selection": str(selection_path)
        }
    }
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = workspace / '.artifacts' / 'protocol-05b' / 'dependency-graph.json'
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"[PROTOCOL 05B | PHASE 5] Dependency graph built")
    print(f"  - Nodes: {output['summary']['total_nodes']}")
    print(f"  - Edges: {output['summary']['total_edges']}")
    print(f"  - Max level: {output['summary']['max_level']}")
    print(f"  - Valid DAG: {output['summary']['valid_dag']}")
    
    if cycles:
        print(f"[ERROR] Cycles detected in dependency graph!")
        for cycle in cycles:
            print(f"  - Cycle: {' -> '.join(cycle)}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
