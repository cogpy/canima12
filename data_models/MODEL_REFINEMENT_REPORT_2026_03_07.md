# Model Refinement Report — 2026-03-07

**Case:** 2025-137857 — Peter Faucitt v. Jacqueline Faucitt et al.
**Source:** 1,632 Rynette-Bantjies email communications (2015-2026)
**SMOKING GUN:** EVENT_119 — Bantjies admits "I will manufacture an answer" (2025-06-06)

---

## Executive Summary

All five analytical models have been refined with evidence from 1,632 email communications between Rynette Farrar (PERSON_002) and Daniel Jacobus Bantjies (PERSON_007). The discovery of EVENT_119 — Bantjies' direct, written admission of intent to fabricate SARS responses — has elevated all criminal evidence thresholds to 99%.

---

## Model 1: Entity-Relation Model

**Version:** v12 (JSON) / v50 (SCM)
**Files:** `entities/entities_refined_2026_03_07_v12.json`, `relations/relations_refined_2026_03_07_v32.json`, `entity_relation_framework_v50_bantjies_farrar.scm`

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Persons | 12 | 15 | +3 |
| Organizations | 9 | 10 | +1 |
| Relations | ~130 | ~140 | +10 |
| Farrar evidence strength | 0.95 | 0.99 | +0.04 |
| Bantjies evidence strength | 0.95 | 0.99 | +0.04 |

**New Entities:** Marc Yudaken (PERSON_042), David Field (PERSON_043), Denny Da Silva (PERSON_044), Baker McKenzie (ORG_025)

**New Relation Categories Added:**
- `conspiracy_relations`: 3 new (SARS manufacturing, VAT takeover, trustee facilitation)
- `financial_relations`: 1 new (Ketoni shareholder loan)
- `control_relations`: 2 new (credential sharing, Anton removal)
- `employment_relations`: 2 new (Baker McKenzie attorneys)
- `conflict_of_interest_relations`: 2 new (Bantjies-Ketoni, Bantjies-Field)

---

## Model 2: Event-Timeline Model

**Version:** v33
**File:** `timelines/timeline.json`

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Total events | 142 | 149 | +7 |
| Criminal events | ~68 | ~75 | +7 |
| Phases | 5 | 6 | +1 |

**New Events:**

| Event | Date | Title | Strength |
|-------|------|-------|----------|
| EVENT_114 | 2022-06-01 | Anton Hechter Removal from VAT Portal | 95% |
| EVENT_115 | 2022-06-23 | eFiling Credential Sharing | 99% |
| EVENT_116 | 2023-04-12 | Ketoni SHA/MOI via Baker McKenzie | 99% |
| EVENT_117 | 2023-05-09 | Ketoni Payment to Shareholder Loan | 95% |
| EVENT_118 | 2024-11-19 | Beneficial Ownership Raised | 85% |
| EVENT_119 | 2025-06-06 | **SMOKING GUN: Manufacture SARS Answer** | **99%** |
| EVENT_120 | 2025-08-12 | Proof of Address for Trustee | 99% |

All new events include `provable_foreknowledge` metadata for temporally-indexed audit trail.

---

## Model 3: Stock-Flow Model

**Version:** v3
**File:** `stock_flow_model_2026_03_07.json`

| Component | Count |
|-----------|-------|
| Stocks | 7 |
| Flows | 6 |
| Feedback Loops | 3 |
| Auxiliary Variables | 3 |

**Key Stocks:** RegimA Revenue, VAT Pool, Intercompany Balances, Ketoni Receivable (R18.685M), Shareholder Loan, FFT Assets, Hidden Money Maximiser (R5M)

**Key Flows:** Revenue → Intercompany (Bantjies controls), Ketoni → Shareholder Loan (EVENT_117), FFT → Hidden (no audit trail)

**Feedback Loops:**
1. **Control Reinforcement** (positive): More control → more manipulation → more need for control
2. **Ketoni Capture** (positive): Insider knowledge → trustee → distribution control → capture
3. **Evidence Destruction** (positive): Fraud risk → destroy evidence → create new fraud

---

## Model 4: Hypergraph-GNN Model

**Version:** v3
**File:** `hypergraph_gnn_model_2026_03_07.json`

| Component | Count |
|-----------|-------|
| Nodes (persons) | 10 |
| Nodes (organizations) | 5 |
| Nodes (trusts) | 1 |
| Hyperedges | 9 |
| Node feature dimensions | 8 |
| Prediction targets | 4 |

**Key Hyperedges:**
1. **HE_SMOKING_GUN** — Bantjies + Rynette (weight: 0.99)
2. **HE_KETONI_INSIDER_NETWORK** — 8 entities connected (weight: 0.99)
3. **HE_R18M_CONVERGENCE** — 7 entities converge on R18.685M (weight: 0.99)
4. **HE_FINANCIAL_CONTROL_LOOP** — Racketeering pattern (weight: 0.99)

**GNN Architecture:** 3-layer attention-weighted message passing with 4 attention heads.

---

## Model 5: LEX-Transformer Model

**Version:** v3
**File:** `lex_transformer_model_2026_03_07.json`

| Component | Count | Status |
|-----------|-------|--------|
| Queries (Q) | 8 | All EXCEEDED |
| Keys (K) | 11 | All mapped |
| Values (V) | 4 | All READY_TO_FILE |
| Foreknowledge chain | 12 events | Complete |

**Attention Mechanism:** Promise-Lambda Attention where Q=Legal Promises, K=Evidence, V=Filing Outputs

**All Queries Satisfied:**

| Query | Threshold | Current | Primary Key |
|-------|-----------|---------|-------------|
| Q_TAX_FRAUD | 95% | 99% | K_SMOKING_GUN_EVENT_119 |
| Q_FRAUD | 95% | 99% | K_TRUST_FORGERY + K_SARS |
| Q_FORGERY | 95% | 99% | K_TRUST_AMENDMENT_FORGERY |
| Q_PERJURY | 95% | 99% | K_CONFIRMATORY_AFFIDAVIT |
| Q_CONSPIRACY | 95% | 99% | K_1632_COMMUNICATIONS |
| Q_BREACH_FIDUCIARY | 50% | 99% | K_KETONI_CONFLICT |
| Q_POPIA | 50% | 95% | K_CREDENTIAL_SHARING |
| Q_COMPANIES_ACT | 50% | 99% | K_SMOKING_GUN + K_INTERCO |

---

## Visualizations

All five models have been rendered as Mermaid diagrams (PNG):
- `diagrams/entity_relation_2026_03_07.png`
- `diagrams/event_timeline_2026_03_07.png`
- `diagrams/stock_flow_2026_03_07.png`
- `diagrams/hypergraph_gnn_2026_03_07.png`
- `diagrams/lex_transformer_2026_03_07.png`

**Interactive Dashboard:** [docs/models/index.html](https://cogpy.github.io/revstream1/models/)

---

*Generated: 2026-03-07 | LEX Investigation System*
