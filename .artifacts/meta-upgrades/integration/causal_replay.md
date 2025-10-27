# Causal Replay (Mock)

This is a dry-run description of how the Causal Ledger would reconstruct decision traces across protocols. No runtime execution performed.

- Inputs: protocol_catalog.json, upgrade_protocol_graph.json
- Replay approach: Walk handoffs P01→...→P23 and annotate decision points where gates evaluate
- Expected: Deterministic reconstruction of gate outcomes using recorded evidence pointers
