# R10.9M Mass Extraction from Entity Accounts (EVENT_135)

## Event Metadata
- **Type:** Unknown
- **Entities Involved:** Unknown
- **Source:** Unknown


**Date:** 2025-09-03 to 2025-09-11

**Description:** Within 8 days of the interdict being granted on 19 August 2025, a total of R10,924,131.18 was extracted from the four corporate entity accounts. The Entity Answering Affidavit (ND-01) documents the specific amounts: R5,164,131.18 from RWD (3 Sep), R3,090,000 from RST (11 Sep), R1,730,000 from VVA (11 Sep), R640,000 from SLG (11 Sep), and R300,000 from VVA to ENS Attorneys (26 Aug). The speed and coordination of the extraction suggests it was pre-planned, awaiting only the legal cover of the court order.

```json
{
  "event_id": "EVENT_135",
  "date": "2025-09-03",
  "title": "R10.9M Mass Extraction from Entity Accounts",
  "category": "fund_extraction",
  "event_type": "financial_transaction",
  "perpetrators": ["PERSON_001"],
  "victims": ["ORG_001", "ORG_002", "ORG_003", "ORG_004"],
  "entities_involved": ["RWD (Pty) Ltd", "RST CC", "VVA CC", "SLG CC", "ENS Africa"],
  "description": "R10,924,131.18 extracted from 4 entity accounts within 8 days of interdict being granted",
  "financial_impact": "R10,924,131.18",
  "legal_significance": "Pre-planned extraction using void court order as legal cover; constitutes theft/fraud if order is void",
  "evidence": ["ND-01", "bank_statements"],
  "breakdown": {
    "RWD": "R5,164,131.18 (2025-09-03)",
    "RST": "R3,090,000.00 (2025-09-11)",
    "VVA": "R1,730,000.00 (2025-09-11)",
    "SLG": "R640,000.00 (2025-09-11)",
    "VVA_to_ENS": "R300,000.00 (2025-08-26)"
  },
  "pattern": "post_interdict_extraction",
  "critical": true,
  "timeline_phase": "PHASE_005",
  "burden_of_proof": "criminal_95",
  "criminal_threshold": "yes"
}
```
