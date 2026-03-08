---
name: hyper-holmes
description: Convergent investigation mode for hypothesis validation, evidence verification, burden of proof assessment, and legal document generation. Use for validating leads from Super-Sleuth, updating entity-relation models, calculating evidence weights, and generating legal filings when thresholds are met.
---

# Hyper-Holmes Turbo-Solve Mode

Convergent investigation agent for hypothesis validation and case resolution. Operates in verification mode to validate leads, assess burden of proof, and generate legal documents when evidence thresholds are met.

**Required companion skills:** When generating legal filings, always consult `uniform-rules-of-court` for procedural rule citations. Use `sa-entity-intel` for entity enrichment and `sa-vat-search` for VAT verification.

## Core Philosophy

> **Convergent Thinking**: Narrow down to validated conclusions from hypotheses.
> **Verification**: Every claim must be traced to primary source evidence.
> **Threshold-Driven**: Generate documents only when burden of proof is met.

## Algorithmic Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    HYPER-HOLMES PIPELINE                        │
├─────────────────────────────────────────────────────────────────┤
│  1. RECEIVE       → Accept handoff from Super-Sleuth            │
│  2. VALIDATE      → Verify each lead against sources            │
│  3. WEIGHT        → Calculate evidence weights                  │
│  4. UPDATE        → Modify entity-relation model                │
│  5. ASSESS        → Check burden of proof thresholds            │
│  6. GENERATE      → Create legal documents if thresholds met    │
│  7. ARCHIVE       → Package and sync to repositories            │
│  8. REPORT        → Deliver findings and documents              │
└─────────────────────────────────────────────────────────────────┘
```

## Phase 1: Receive Handoff

### 1.1 Handoff Validation

Verify handoff package from Super-Sleuth:

```python
# Validate handoff package
python /home/ubuntu/skills/hyper-holmes/scripts/validate_handoff.py <handoff_dir>
```

Required components:
- `manifest.json` - Package metadata
- `leads/` - Hypothesis files
- `entities/hypergraph.json` - Entity-relation model
- `timeline/timeline.json` - Event timeline
- `evidence_index/evidence_index.json` - Source mapping

### 1.2 Lead Prioritization

Process leads by priority:

| Priority | Category | Action |
|----------|----------|--------|
| P1 | Critical | Validate immediately |
| P2 | Strong | Validate in sequence |
| P3 | Moderate | Validate if time permits |
| P4 | Weak | Flag for future investigation |

## Phase 2: Lead Validation

### 2.1 Validation Algorithm

For each lead:

```
1. Extract claimed facts
2. Locate source documents
3. Verify fact against source
4. Check for contradicting evidence
5. Calculate confidence score
6. Update lead status (validated/rejected/partial)
```

### 2.2 Validation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| **Source Authenticity** | 0.30 | Document is genuine and unaltered |
| **Direct Evidence** | 0.25 | Fact directly stated in source |
| **Corroboration** | 0.20 | Multiple independent sources agree |
| **No Contradiction** | 0.15 | No conflicting evidence exists |
| **Chain of Custody** | 0.10 | Evidence provenance is clear |

### 2.3 Validation Script

```python
# Validate leads against evidence
python /home/ubuntu/skills/hyper-holmes/scripts/validate_leads.py <leads_dir> <evidence_dir>
```

### 2.4 Validation Output

```json
{
  "lead_id": "LEAD-001",
  "status": "validated",
  "confidence": 0.87,
  "validation_details": {
    "facts_verified": 5,
    "facts_rejected": 0,
    "facts_partial": 1,
    "contradictions": [],
    "corroborations": ["DC_003", "DC_007"]
  },
  "legal_elements_supported": ["fraud", "breach_of_duty"]
}
```

## Phase 3: Evidence Weighting

### 3.1 Weight Calculation

Calculate evidence weight for each legal element:

```
Element_Weight = Σ(Evidence_Weight × Relevance × Reliability)
```

### 3.2 Evidence Reliability Scale

| Reliability | Score | Examples |
|-------------|-------|----------|
| **Conclusive** | 1.0 | Signed contracts, bank records |
| **Strong** | 0.8 | Official documents, certified copies |
| **Moderate** | 0.6 | Emails, correspondence |
| **Weak** | 0.4 | Witness statements, hearsay |
| **Speculative** | 0.2 | Inferences, patterns |

### 3.3 Legal Element Mapping

| Element | Required Evidence | Threshold |
|---------|-------------------|-----------|
| **Fraud** | Misrepresentation + Intent + Reliance + Damage | Civil: 50%, Criminal: 95% |
| **Breach of Fiduciary Duty** | Duty + Breach + Causation + Damage | Civil: 50% |
| **Money Laundering** | Predicate offense + Concealment + Knowledge | Criminal: 95% |
| **Forgery** | False document + Intent to defraud | Criminal: 95% |
| **Tax Fraud** | False return + Intent + Material amount | Criminal: 95% |

### 3.4 Weight Calculator

```python
# Calculate evidence weights
python /home/ubuntu/skills/hyper-holmes/scripts/calculate_weights.py <validated_leads.json>
```

## Phase 4: Entity-Relation Update

### 4.1 Update Protocol

Update entity-relation model based on validated findings:

```
1. Add new entities discovered
2. Add new relations confirmed
3. Update confidence scores
4. Mark contradicted facts
5. Link evidence to entities
6. Recalculate hypergraph metrics
```

### 4.2 Update Script

```python
# Update entity-relation model
python /home/ubuntu/skills/hyper-holmes/scripts/update_model.py <hypergraph.json> <validated_leads.json>
```

### 4.3 Model Verification

After updates, verify model consistency:

- No orphan entities
- All relations have valid source/target
- All facts have source documents
- No circular dependencies (unless intentional)
- Confidence scores within bounds

## Phase 5: Burden of Proof Assessment

### 5.1 Threshold Definitions

| Standard | Threshold | Application |
|----------|-----------|-------------|
| **Balance of Probabilities** | 50% | Civil claims |
| **Clear and Convincing** | 75% | Some civil matters |
| **Beyond Reasonable Doubt** | 95% | Criminal charges |

### 5.2 Assessment Algorithm

```
1. For each legal claim:
   a. Identify required elements
   b. Sum weighted evidence for each element
   c. Calculate overall claim strength
   d. Compare to applicable threshold
   e. Flag if threshold exceeded
```

### 5.3 Assessment Output

```json
{
  "claim": "Fraud against Peter Faucitt",
  "claim_type": "civil",
  "threshold": 0.50,
  "current_score": 0.78,
  "status": "THRESHOLD_EXCEEDED",
  "elements": {
    "misrepresentation": {"score": 0.85, "met": true},
    "intent": {"score": 0.72, "met": true},
    "reliance": {"score": 0.80, "met": true},
    "damage": {"score": 0.75, "met": true}
  },
  "ready_for_filing": true
}
```

### 5.4 Assessment Script

```python
# Assess burden of proof
python /home/ubuntu/skills/hyper-holmes/scripts/assess_burden.py <weights.json> --standard civil
```

## Phase 6: Document Generation

### 6.1 Document Types

| Document | Trigger | Template |
|----------|---------|----------|
| **CIPC Complaint** | Companies Act violation ≥50% | `templates/cipc_complaint.md` |
| **POPIA Complaint** | Data protection breach ≥50% | `templates/popia_complaint.md` |
| **Affidavit** | Any civil claim ≥50% | `templates/affidavit.md` |
| **NPA Tax Fraud Report** | Tax fraud ≥95% | `templates/npa_tax_fraud.md` |
| **Commercial Crime Submission** | Criminal fraud ≥95% | `templates/commercial_crime.md` |

### 6.2 Document Generation Rules

1. **Only generate when threshold exceeded**
2. **Include only verified facts**
3. **Cite evidence with annexure references**
4. **Follow legal document standards**
5. **Remove speculation and hyperbole**

### 6.3 Generation Script

```python
# Generate legal documents
python /home/ubuntu/skills/hyper-holmes/scripts/generate_documents.py <assessment.json> --type cipc_complaint
```

### 6.4 Document Standards

When generating legal documents:

- **Remove**: Hyperbole, speculation, subjective claims
- **Include**: Hard facts, material evidence, exact figures
- **Format**: Paragraph-by-paragraph with proper numbering
- **Narrative**: Evidence-based revelation without overt accusations
- **Citations**: Every claim linked to annexure reference

## Phase 7: Archive and Sync

### 7.1 Archive Protocol

```
1. Create timestamped archive
2. Include all generated documents
3. Include updated entity-relation model
4. Include evidence index
5. Sync to repositories
```

### 7.2 Repository Sync

```bash
# Sync to ad-res-j7
cd ad-res-j7 && git add -A && git commit -m "feat(case): Update from Hyper-Holmes validation" && git push

# Sync to revstream1
cd ../revstream1 && git add -A && git commit -m "docs: Update evidence and filings" && git push
```

### 7.3 GitHub Pages Update

Update documentation for public access:

```bash
# Update docs
cd revstream1/docs
# Edit relevant files
git add docs/
git commit -m "docs: Update case documentation"
git push origin main
```

## Phase 8: Report Delivery

### 8.1 Report Structure

```markdown
# Hyper-Holmes Validation Report

## Executive Summary
[Validated findings in 2-3 paragraphs]

## Lead Validation Results
[Table of validated/rejected leads]

## Evidence Weight Summary
[Weight calculations per legal element]

## Burden of Proof Assessment
[Threshold analysis per claim]

## Generated Documents
[List of documents ready for filing]

## Entity-Relation Updates
[Changes made to model]

## Recommended Actions
[Next steps for case progression]

---
*Generated by Hyper-Holmes Turbo-Solve Mode*
```

## Integration with Super-Sleuth

### Workflow Integration

```
┌─────────────────┐     ┌─────────────────┐
│  SUPER-SLEUTH   │     │  HYPER-HOLMES   │
│  (Divergent)    │────▶│  (Convergent)   │
│                 │     │                 │
│  • Explore      │     │  • Validate     │
│  • Discover     │     │  • Verify       │
│  • Hypothesize  │     │  • Document     │
└─────────────────┘     └─────────────────┘
        │                       │
        │                       │
        ▼                       ▼
┌─────────────────────────────────────────┐
│           CASE RESOLUTION               │
│  • Legal filings submitted              │
│  • Entity-relation model updated        │
│  • Evidence properly indexed            │
│  • GitHub Pages documentation current   │
└─────────────────────────────────────────┘
```

### Mode Switching

When operating as single agent with mode switching:

```json
{"tool": "set_mode", "mode": "intro_spect"}  // Switch to Super-Sleuth
{"tool": "set_mode", "mode": "turbo_solve"}  // Switch to Hyper-Holmes
```

## Legal Filing Templates

### CIPC Complaint Structure

```markdown
# CIPC COMPLAINT
## Companies Act 71 of 2008

### 1. COMPLAINANT DETAILS
### 2. RESPONDENT DETAILS
### 3. COMPANY DETAILS
### 4. NATURE OF COMPLAINT
### 5. FACTUAL BACKGROUND
### 6. CONTRAVENTIONS
### 7. EVIDENCE SUMMARY
### 8. RELIEF SOUGHT
### 9. ANNEXURES
```

### Affidavit Structure

```markdown
# AFFIDAVIT
## In the matter of [CASE]

### DEPONENT DETAILS
### BACKGROUND
### FACTS (numbered paragraphs)
### EVIDENCE REFERENCES
### CONCLUSION
### OATH
```

## Reference Files

- **Handoff validator**: `scripts/validate_handoff.py`
- **Lead validator**: `scripts/validate_leads.py`
- **Weight calculator**: `scripts/calculate_weights.py`
- **Model updater**: `scripts/update_model.py`
- **Burden assessor**: `scripts/assess_burden.py`
- **Document generator**: `scripts/generate_documents.py`
- **Legal elements**: `references/legal_elements.md`
- **Document templates**: `templates/`
