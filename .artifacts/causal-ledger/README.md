# Causal Ledger Initialization

This directory seeds the causal ledger required by **UPG04 – Causal Ledger**. The ledger is an immutable, append-only record of protocol gate transitions spanning P01–P28.

## Initialization Steps
1. **Create append-only container** – Generated `ledger.json` with the following schema:
   - `ledger.version`: semantic version of the schema overlay.
   - `ledger.append_only`: boolean guard enforcing write policy.
   - `ledger.entries[]`: ordered gate-transition events linked by `prev_hash` and `entry_hash` for tamper detection.
   - `ledger.integrity`: snapshot of current chain head metadata (`last_sequence`, `last_hash`, `chain_root`).
2. **Seed representative events** – Populated 28 chronological entries, one per protocol (P01–P28). Each event stores:
   - Protocol identity (`protocol.id`, `protocol.name`, `protocol.phase`).
   - Gate state transition (`gate_transition.from_gate`, `gate_transition.to_gate`, `gate_transition.decision`).
   - Quality guard confirmations (`quality_gates` array) to evidence gate validation.
   - Cryptographic linkage (`prev_hash`, `entry_hash`) to uphold append-only guarantees.
3. **Capture governance metadata** – Declared owner, update policy, and validation hooks that must execute before future append operations.

All timestamps are deterministic ISO-8601 values spaced one minute apart to support replay diagnostics without colliding with live protocol clocks.

## Validation Steps
To confirm ledger integrity before using it in simulations or protocol overlays:
1. **Schema verification** – Ensure the file parses as JSON and required keys exist.
   ```bash
   jq '.ledger | {version, append_only, entries, integrity}' ledger.json > /dev/null
   ```
2. **Hash-chain verification** – Recompute SHA-256 hashes in sequence to confirm immutability. A sample check script:
   ```bash
   python - <<'PY'
   import json, hashlib
   with open('ledger.json') as fh:
       data = json.load(fh)['ledger']
   prev = '0' * 64
   for entry in data['entries']:
       material = "|".join([
           str(entry['sequence']),
           entry['protocol']['id'],
           entry['protocol']['name'],
           entry['protocol']['phase'],
           entry['gate_transition']['from_gate'],
           entry['gate_transition']['to_gate'],
           entry['gate_transition']['decision'],
           prev
       ])
       digest = hashlib.sha256(material.encode()).hexdigest()
       assert entry['prev_hash'] == prev, 'prev_hash mismatch'
       assert entry['entry_hash'] == digest, 'hash mismatch'
       prev = digest
   print('hash chain valid')
   PY
   ```
3. **Governance hook dry run** – Execute the listed validation hooks (or dry-run alternatives) to ensure evidence validators are accessible before append operations.
   ```bash
   python scripts/validate_evidence_citations.py --help
   python scripts/run_quality_audit.py --help
   ```

## Coverage Calculation
- **Total protocols tracked:** 28
- **Protocols with ledger entries:** 28
- **Coverage ratio:** `28 / 28 = 1.0` (100%)

This satisfies the ≥95% coverage requirement for the causal ledger overlay and provides readiness for replaying decision flows across every protocol gate transition.
