## INTEGRATION POINTS

### Protocol Inputs
**Source:** {INPUT_SOURCE}
**Format:** {INPUT_FORMAT}
**Location:** {INPUT_LOCATION}
**Required Fields:**
- {INPUT_FIELD_1}
- {INPUT_FIELD_2}
- {INPUT_FIELD_3}

**Validation:**
- Input completeness check
- Format validation
- Business rule validation

### Protocol Outputs
**Destination:** {OUTPUT_DESTINATION}
**Format:** {OUTPUT_FORMAT}
**Location:** {OUTPUT_LOCATION}
**Delivered Artifacts:**
- {OUTPUT_ARTIFACT_1}
- {OUTPUT_ARTIFACT_2}
- {OUTPUT_ARTIFACT_3}

**Validation:**
- Output completeness check
- Quality gate validation
- Schema compliance

---

## EVIDENCE ARTIFACTS

### Artifact Inventory

| Artifact | Purpose | Format | Location | Validation | Metrics |
|----------|---------|--------|----------|------------|---------|
| {ARTIFACT_1} | {PURPOSE_1} | {FORMAT_1} | {LOCATION_1} | {VALIDATION_1} | {METRICS_1} |
| {ARTIFACT_2} | {PURPOSE_2} | {FORMAT_2} | {LOCATION_2} | {VALIDATION_2} | {METRICS_2} |
| {ARTIFACT_3} | {PURPOSE_3} | {FORMAT_3} | {LOCATION_3} | {VALIDATION_3} | {METRICS_3} |

### Metrics Definitions
- **Coverage:** Percentage of requirements addressed
- **Quality Score:** Automated quality assessment (A/B/C/D/F)
- **Completeness:** Percentage of required fields populated
- **Validation Status:** Pass/Warning/Fail

---

## EVIDENCE ARCHIVAL

### Archival Strategy
**Retention Period:** {RETENTION_PERIOD}
**Compression:** tar.gz format
**Location:** `.artifacts/archive/protocol-{PROTOCOL_ID}/`

### Retrieval Procedure
1. **Locate Evidence:**
   ```bash
   ls -la .artifacts/protocol-{PROTOCOL_ID}/
   ```

2. **Verify Manifest:**
   ```bash
   python3 scripts/verify_evidence_manifest.py --protocol {PROTOCOL_ID}
   ```

3. **Extract Required Evidence:**
   ```bash
   python3 scripts/extract_evidence.py \
     --protocol {PROTOCOL_ID} \
     --artifacts {ARTIFACT_LIST} \
     --output ./evidence-export/
   ```

4. **Validate Integrity:**
   ```bash
   python3 scripts/validate_evidence_integrity.py \
     --manifest .artifacts/protocol-{PROTOCOL_ID}/evidence-manifest.json
   ```

### Cleanup Procedure
1. **Identify Archival Candidates:**
   ```bash
   python3 scripts/identify_archival_candidates.py \
     --age-days {RETENTION_DAYS} \
     --protocol {PROTOCOL_ID}
   ```

2. **Create Archive:**
   ```bash
   python3 scripts/archive_evidence.py \
     --protocol {PROTOCOL_ID} \
     --output .artifacts/archive/protocol-{PROTOCOL_ID}-$(date +%Y%m%d).tar.gz
   ```

3. **Verify Archive:**
   ```bash
   tar -tzf .artifacts/archive/protocol-{PROTOCOL_ID}-*.tar.gz
   ```

4. **Update Manifest:**
   ```bash
   python3 scripts/update_archival_manifest.py \
     --protocol {PROTOCOL_ID} \
     --archive-path .artifacts/archive/protocol-{PROTOCOL_ID}-*.tar.gz
   ```

5. **Remove Originals (after verification):**
   ```bash
   python3 scripts/cleanup_archived_evidence.py \
     --protocol {PROTOCOL_ID} \
     --verify-archive \
     --dry-run  # Remove flag when ready
   ```

### Emergency Recovery
```bash
# Restore from archive
python3 scripts/restore_evidence.py \
  --archive .artifacts/archive/protocol-{PROTOCOL_ID}-{DATE}.tar.gz \
  --destination .artifacts/protocol-{PROTOCOL_ID}/
```
