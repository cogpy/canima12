---
name: lex-case-analysis
description: Analyze legal cases using the LEX Legal Reasoning Framework. Use for South African legal case analysis, entity-relation modeling, evidence chain building, burden of proof assessment, and generating legal filings (CIPC complaints, POPIA complaints, NPA reports, commercial crime submissions).
---

# LEX Case Analysis

Analyze legal cases using the LEX Legal Reasoning Framework from the ad-res-j7 repository.

**Required companion skills:** Always consult `uniform-rules-of-court` for procedural rule citations when drafting legal filings. Use `sa-entity-intel` for entity enrichment and `sa-vat-search` for VAT verification.

## Repository Setup

Clone the repository if not already available:

```bash
GH_TOKEN="$beast" gh repo clone cogpy/ad-res-j7
```

## Framework Structure

```
ad-res-j7/
├── lex/                    # Active LEX framework
│   ├── core/               # Core framework + canonical files
│   ├── skills/             # 128 legal reasoning skills
│   ├── [domain]/za/        # South African law modules
│   └── hypergraph/         # Knowledge graph integration
├── lexarc/                 # Archived versions (rollback)
├── docs/                   # GitHub Pages documentation
└── ANNEXURES/              # Evidence packages (JF01-JF20)
```

## Legal Domains

| Code | Domain | Key Skills |
|------|--------|------------|
| `civ` | Civil Law | Contract breach, delict, damages |
| `cri` | Criminal Law | Fraud elements, money laundering, tax fraud |
| `evid` | Evidence Law | Admissibility, weight, chain building |
| `cmp` | Company Law | Director duties, CIPC compliance |
| `trs` | Trust Law | Trustee duties, beneficiary rights |
| `dat` | Data Protection | POPIA compliance, breach detection |
| `frn` | Forensic | Fraud patterns, timeline reconstruction |

## Core Workflows

### 1. Entity-Relation Analysis

Define entities and relations from verifiable records:

```scheme
;; Load canonical framework
(use-modules (lex core entity-relation-framework-canonical))

;; Create entity
(define entity (make-entity
  "PERSON_001"
  'natural-person
  "Peter Andrew Faucitt"
  '((role . director) (company . "Strategic Logistics"))))
```

Key files:
- `lex/core/entity_relation_framework_canonical.scm` (v72)
- `lex/core/entity_relation_model.scm`

### 2. Evidence Chain Building

Build evidence chains with provenance tracking:

1. Identify evidence files (JF01-JF20, SF1-SF9)
2. Map evidence to legal elements
3. Calculate evidence weight and admissibility
4. Assess burden of proof thresholds

Thresholds:
- **Civil (50%)**: Balance of probabilities
- **Criminal (95%)**: Beyond reasonable doubt

### 3. Timeline Reconstruction

Use forensic skills for temporal analysis:

```
lex/skills/frn/forensic_skills.scm
```

Key patterns to detect:
- **Manufactured crisis** - Artificial urgency creation
- **Coordination patterns** - Multi-actor synchronization
- **Escalation sequences** - Progressive control actions
- **Concealment patterns** - Evidence destruction timing

### 4. Legal Filing Generation

Generate filings using templates and evidence:

| Filing Type | Key Evidence | Threshold |
|-------------|--------------|-----------|
| CIPC Complaint | JF04, JF14, JF15 | Companies Act violations |
| POPIA Complaint | SF1, SF2, SF6, SF7 | Data protection breaches |
| NPA Tax Fraud | JF03, SF3, SF4 | Income/VAT fraud |
| Commercial Crime | JF03, JF08, SF1 | Fraud, theft, forgery |

## Document Standards

When generating legal documents:

1. **Remove**: Hyperbole, speculation, subjective claims
2. **Include**: Hard facts, material evidence, exact figures
3. **Format**: Paragraph-by-paragraph responses (AD → JR/DR numbering)
4. **Narrative**: Gradual evidence-based revelation without overt accusations

## Response Numbering Protocol

For responding to numbered paragraphs (e.g., AD X.Y):
- Jacqui's responses: `JR X.Y.1`, `JR X.Y.2`
- Daniel's responses: `DR X.Y.1`, `DR X.Y.2`

## Skill Application

Apply skills from `lex/skills/` to case analysis:

```python
# Example: Apply fraud element analysis
from lex.rules.south_africa import SouthAfricanRules

rules = SouthAfricanRules()
fraud_elements = rules.analyze_fraud_elements(evidence)
```

## Hypergraph Queries

Query the knowledge graph for entity relationships:

```bash
cd ad-res-j7/lex/hypergraph
python query_hypergraph.py --entity "Peter Faucitt" --depth 2
```

## Sync Protocol

Always sync changes to both repositories:

```bash
cd ad-res-j7 && git add -A && git commit -m "..." && git push origin main
cd ../revstream1 && git add -A && git commit -m "..." && git push origin main
```

## Key Files Reference

| File | Purpose |
|------|---------|
| `lex/core/entity_relation_framework_canonical.scm` | Entity-relation model (v72) |
| `lex/core/high_resolution_agent_models_canonical.scm` | Agent models (v73) |
| `lex/core/legal_aspects_comprehensive_canonical.scm` | Legal aspects (v73) |
| `lex/skills/README.md` | Skills framework documentation |
| `docs/index.md` | GitHub Pages main index |
