# Relations Index

**Last Updated:** 2026-03-09  
**Total Relations:** 17 documented files + 15 JSON-modeled relations  
**Case Number:** 2025-137857

This index catalogs all entity relationships documented in the Revenue Stream Hijacking case, organized by type and cross-referenced to all 6 applications.

---

## NEW: Conspiracy Network Relations (March 2026)

| Relation | Type | Key Entities | Confidence | Link |
|----------|------|-------------|------------|------|
| **Ketoni Insider Trading Network** | Financial Conspiracy | Bantjies, Peter, Rynette, Kevin Derrick | 99% | [View](./KETONI_INSIDER_TRADING_NETWORK.md) |
| **Revenue Hijacking Chain** | Financial Crime | Rynette, Linda, Gayane, Peter, Bantjies | 99% | [View](./REVENUE_HIJACKING_CHAIN.md) |
| **Trust Capture Sequence** | Trust Fraud | Rynette, Bantjies, Peter | 99% | [View](./TRUST_CAPTURE_SEQUENCE.md) |
| **Identity Fraud Network** | Identity Fraud / POPIA | Rynette (as Peter, as Bantjies) | 99% | [View](./IDENTITY_FRAUD_NETWORK.md) |
| **Dual Corporate Identity** | Corporate Fraud | Villa Via / Kaylovest Three | 95% | [View](./DUAL_CORPORATE_IDENTITY.md) |

## Existing Conspiracy Relations

| Relation | Type | Key Entities | Confidence | Link |
|----------|------|-------------|------------|------|
| **Rynette-Bantjies Conspiracy** | Coordinated Criminal Action | Rynette, Bantjies | 99% | [View](./RYNETTE_BANTJIES_CONSPIRACY_2026_03_07.md) |
| **Aymac/Kaylovest/Elliott Network** | Shell Company Network | Aymac, Kaylovest, Elliott | 95% | [View](./AYMAC_KAYLOVEST_ELLIOTT_NETWORK.md) |
| **Villa Via / Kaylovest Identity** | Corporate Identity Fraud | Villa Via, Kaylovest | 95% | [View](./VILLA_VIA_KAYLOVEST_IDENTITY.md) |
| **Sabotage-Framing Link** | Operational Sabotage | Peter, Rynette | 95% | [View](./sabotage_framing_link.md) |

## Evidence-Based Relations

| Relation | Type | Source | Link |
|----------|------|--------|------|
| **Contempt Relations** | Legal Proceedings | Contempt application analysis | [View](./CONTEMPT_RELATIONS_2026_02_09.md) |
| **Forgery/Backdating Relations** | Documentary Fraud | Two-date distinction analysis | [View](./FORGERY_BACKDATING_RELATIONS_2026_02_18.md) |
| **Mailbox Evidence Relations** | Communication Patterns | 101,215 email analysis | [View](./MAILBOX_EVIDENCE_RELATIONS_2026_02_09.md) |

## Structural Relations

| Relation | Type | Description | Link |
|----------|------|-------------|------|
| **Director Of** | Corporate Governance | Director-company relationships | [View](./director_of.md) |
| **Shareholder Of** | Ownership | Shareholding relationships | [View](./shareholder_of.md) |
| **Trustee Of** | Trust Law | Trustee-trust relationships | [View](./trustee_of.md) |
| **Financial Flow** | Financial | Inter-entity fund flows | [View](./financial_flow.md) |

---

## Relation-to-Application Matrix

This matrix maps each relation to the 6 legal applications, indicating primary (P) and supporting (S) relevance.

| Relation | App 1: Civil/Criminal | App 2: CIPC | App 3: POPIA | App 4: Commercial Crime | App 5: NPA Tax Fraud | App 6: FIC/STR |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| Ketoni Insider Trading | S | S | | **P** | **P** | **P** |
| Revenue Hijacking Chain | **P** | S | S | **P** | **P** | **P** |
| Trust Capture Sequence | **P** | **P** | S | **P** | S | S |
| Identity Fraud Network | S | S | **P** | **P** | S | S |
| Dual Corporate Identity | S | **P** | | S | **P** | **P** |
| Rynette-Bantjies Conspiracy | S | S | S | **P** | S | S |
| Aymac/Kaylovest/Elliott | S | **P** | | S | **P** | **P** |
| Villa Via/Kaylovest Identity | S | **P** | | S | **P** | **P** |
| Sabotage-Framing Link | **P** | S | S | S | | |
| Contempt Relations | **P** | | | S | | |
| Forgery/Backdating | **P** | **P** | **P** | **P** | | |
| Mailbox Evidence | S | S | **P** | **P** | S | S |

**P** = Primary relevance | **S** = Supporting relevance

---

## JSON-Modeled Relations (Structured Data)

The following relations are modeled in structured JSON format within this index for programmatic access:

### Ownership Relations
- **REL_OWN_001:** PERSON_005 (Dan) → ORG_003 (RegimA Zone UK) — Complete ownership, legitimate

### Control Relations
- **REL_CTRL_001:** PERSON_001 (Peter) → ORG_001 (RWW) — Directorial control, disputed
- **REL_CTRL_002:** PERSON_002 (Rynette) → ORG_001 (RWW) — Financial controller, fraudulent
- **REL_CTRL_009:** PERSON_004 (Jax) → PERSON_002 (Rynette) — Email diversion instruction
- **REL_CTRL_010:** PERSON_002 (Rynette) → PERSON_LINDA — Payment redirection instruction
- **REL_CTRL_011:** PERSON_002 (Rynette) → PERSON_GAYANE — Domain change instruction

### Conspiracy Relations
- **REL_CONSP_001:** PERSON_001 (Peter) ↔ PERSON_002 (Rynette) — Coordinated criminal activity, conclusive
- **REL_CONSP_004:** PERSON_007 (Bantjies) ↔ PERSON_001 (Peter) — Fraud concealment, conclusive

### Access Relations
- **REL_ACCESS_001:** PERSON_007 (Bantjies) → ORG_001 — Financial access since 2020
- **REL_ACCESS_002:** PERSON_002 (Rynette) → ORG_001 — Sage control since 2020

### Insider Relations
- **REL_INSIDER_001:** PERSON_007 (Bantjies) → ORG_017 (Ketoni) — Insider knowledge via George Group

### Employee Collusion (KF0019 Evidence)
- **Rynette Farrar & Peter Faucitt:** Farrar provided confirmatory affidavit (PF19) supporting Peter's contempt application against Jax.
- **Gayane Williams & Peter Faucitt:** Williams provided confirmatory affidavit (PF20) supporting Peter's contempt application against Jax.
- **Oliver Mphande & Peter Faucitt:** Mphande provided stock sheets (PF18) to Peter while Peter was attempting to assert control over Jax's business.

---

## Cross-References

- [Entities Index](../entities/index.md)
- [Events Index](../events/index.md)
- [Timeline](../timeline.md)
- [Filings Index](../filings/index.md)
- [Main Index](../index.md)

---

*Last updated: 2026-03-09 | LEX-RECON Cross-Repository Reconciliation + 6-Application Restructure*
