# Forgery & Backdating Relations — Two-Date Distinction
**Confidence:** 95% (Estimated)  

**Date:** 2026-02-18  
**Classification:** CRITICAL RELATIONS UPDATE

## New Relations Established

### REL_FORG_001: Rynette → Trust Amendment (Forgery)

| Attribute | Value |
|-----------|-------|
| **Relation ID** | REL_FORG_001 |
| **Type** | forges_document |
| **Source** | PERSON_002 (Rynette Farrar) |
| **Target** | Faucitt Family Trust Amendment Resolution |
| **Date** | 28 June 2024 |
| **Method** | Signs "pp Peter" — forging Peter's signature |
| **Purpose** | Install Bantjies (PERSON_007) as third trustee |
| **Evidence** | SF15, Email Rynette→Bantjies 28 June 2024 |
| **Event** | [EVENT_103](../events/EVENT_103.md) |
| **Criminal Threshold** | 95% EXCEEDED |

### REL_FORG_002: Rynette → Sage Affidavit (Fraud)

| Attribute | Value |
|-----------|-------|
| **Relation ID** | REL_FORG_002 |
| **Type** | submits_fraudulent_document |
| **Source** | PERSON_002 (Rynette Farrar) |
| **Target** | Sage Support (Invited User Switch) |
| **Date** | 8-9 July 2024 |
| **Method** | Submits affidavit for deceased Kayla Pretorius |
| **Purpose** | Transfer Sage ownership to Peter Faucitt |
| **Evidence** | Exchange mailbox, Sage User Switch emails |
| **Event** | [EVENT_063](../events/EVENT_063.md) |
| **Criminal Threshold** | 95% EXCEEDED |

### REL_COORD_001: EA-18 Coordinated Action

| Attribute | Value |
|-----------|-------|
| **Relation ID** | REL_COORD_001 |
| **Type** | coordinated_criminal_action |
| **Source** | REL_FORG_001 (Trust forgery) |
| **Target** | REL_FORG_002 (Sage fraud) |
| **Window** | 10 days (28 June — 9 July 2024) |
| **Significance** | Proves premeditated coordinated conspiracy |
| **Event** | [EVENT_105](../events/EVENT_105.md) |
| **Criminal Threshold** | 95% EXCEEDED — POCA pattern |

### REL_BACK_001: Rynette → Main Trustee Agreement (Backdating)

| Attribute | Value |
|-----------|-------|
| **Relation ID** | REL_BACK_001 |
| **Type** | backdates_document |
| **Source** | PERSON_002 (Rynette Farrar) |
| **Target** | "Main Trustee" Agreement |
| **Actual Date** | 11 August 2025 (email sent) |
| **Backdated To** | 1 July 2025 |
| **Gap** | 6 weeks |
| **Purpose** | Create false paper trail before interdict |
| **Evidence** | Email Rynette→Bantjies 11 August 2025 |
| **Event** | [EVENT_104](../events/EVENT_104.md) |
| **Criminal Threshold** | 95% EXCEEDED |

### REL_PERJ_001: Bantjies → Confirmatory Affidavit (Perjury)

| Attribute | Value |
|-----------|-------|
| **Relation ID** | REL_PERJ_001 |
| **Type** | swears_false_affidavit |
| **Source** | PERSON_007 (Danie Bantjies) |
| **Target** | Confirmatory Affidavit (MAT4719 pp. 69-71) |
| **Date** | 13 August 2025 |
| **Foreknowledge** | Received backdated appointment 2 days earlier; knew of forgery from 28 June 2024 |
| **Evidence** | MAT4719, Email chain, SF15 |
| **Events** | [EVENT_049](../events/EVENT_049.md), [EVENT_104](../events/EVENT_104.md) |
| **Criminal Threshold** | 95% EXCEEDED |

## Relation Chain: Forgery → Backdating → Perjury → Interdict

```
REL_FORG_001 (28 June 2024)
    │ Rynette forges "pp Peter" on trust amendment
    │
    ├── REL_FORG_002 (8-9 July 2024)
    │   │ Rynette submits fraudulent Sage affidavit
    │   │ [10-DAY WINDOW — EA-18]
    │   │
    │   └── REL_COORD_001
    │       Coordinated criminal action proved
    │
    ├── [14-MONTH GAP]
    │
    └── REL_BACK_001 (11 August 2025)
        │ Rynette emails backdated "Main Trustee" to Bantjies
        │
        └── REL_PERJ_001 (13 August 2025)
            │ Bantjies swears confirmatory affidavit
            │ [2 DAYS AFTER RECEIVING BACKDATED APPOINTMENT]
            │
            └── INTERDICT FILED (14 August 2025)
                Void ab initio — obtained through perjury and fraud
```

## Cross-References

- **[Two-Date Distinction Analysis](../evidence/TWO_DATE_DISTINCTION_ANALYSIS.md)**
- **[EVENT_103](../events/EVENT_103.md)** — Trust amendment forgery
- **[EVENT_104](../events/EVENT_104.md)** — Backdated appointment
- **[EVENT_105](../events/EVENT_105.md)** — EA-18 Coordinated action
- **[PERSON_002](../entities/PERSON_002.md)** — Rynette Farrar
- **[PERSON_007](../entities/PERSON_007.md)** — Danie Bantjies

---
*Created: 2026-02-18 — Two-date distinction relations*
