# Causal Replay (Dry-Run Simulation)

- Scope: Reconstruct decision transitions across P01→P02→P03... using mock Ledger entries
- Method: For each protocol gate boundary listed in `catalog/protocol_catalog.json`, synthesize a ledger event with timestamp, gate_id, evidence pointers
- Expected: Replay traversal matches documented handoffs; no cycles detected; missing events flagged
- Status: Pending generation after initial instrument scaffolding
