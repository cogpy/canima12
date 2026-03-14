# LEX Encode Workflow Output

**Case**: 2025-137857 — Revenue Stream Hijacking, Trust Fraud, and Corporate Sabotage

**Generated**: 2026-03-14

This directory contains the output of the LEX Encode Workflow, which encodes the legal matter into formal Scheme (`.scm`) files using the LexRex legal fixed-point theorem framework, the ChainLex legal corpus, and the Uniform Rules of Court procedural predicates.

## Directory Structure

```
lex_encode_output/
├── README.md                          # This file
├── scenario_enhanced.json             # Input scenario with all evidence items
├── certificates/
│   ├── proof_certificate.md           # Pipeline-generated summary
│   ├── proof_certificate.scm          # S-expression proof certificate
│   ├── proof_certificate.json         # Structured data certificate
│   └── PROOF_CERTIFICATE_COMPREHENSIVE.md  # Full analysis with red-team critique
└── scm/
    ├── entities_relations.scm         # 8 entities, 4 relations encoded
    ├── evidence_trees.scm             # 8 evidence items at Matula orders 2-35
    ├── defenses_blocks.scm            # 14 defenses enumerated, all blocked
    ├── procedural_timeline.scm        # 5 events with rule mappings
    ├── compliance_evaluation.scm      # Procedural compliance assessment
    └── proof_certificate.scm          # Certificate as S-expression
```

## Key Results

| Metric | Value |
|--------|-------|
| Evidence Items Encoded | 8 |
| Matula Orders Covered | 2, 3, 4, 7, 35 |
| Defense Morphisms Enumerated | 14 |
| Defenses Blocked | 14 |
| Unblocked Defenses | 0 |
| Fixed Point Reached | **Yes** |
| Order 35 Interlocks | 1 |

## How to Use

The `.scm` files can be loaded into any Scheme interpreter or used with the LexRex prover to verify the fixed-point property. The comprehensive proof certificate provides a human-readable analysis with red-team critiques and counter-strategies for each proposed filing.

## Related Files

- [`RED_TEAM_CRITIQUE.md`](../RED_TEAM_CRITIQUE.md) — Detailed red-team analysis of all proposed filings
- [`data_models/entity_relation_framework_v50_bantjies_farrar.scm`](../data_models/entity_relation_framework_v50_bantjies_farrar.scm) — Latest entity-relation framework
- [`scenario_enhanced.json`](./scenario_enhanced.json) — Full scenario input with all evidence items
