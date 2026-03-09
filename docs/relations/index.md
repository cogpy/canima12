# Relations

```json
{
  "metadata": {
    "version": "9.0_MAILBOX_EVIDENCE_ENHANCED",
    "created_date": "2025-11-10",
    "description": "Relation model for Revenue Stream Hijacking case 2025-137857",
    "case_number": "2025-137857",
    "modeling_approach": "hypergraph_compatible_relations",
    "last_updated": "2026-03-08T16:10:00.000000",
    "changes": "LEX-RECON reconciliation v2. Integrated Uniform Rules of Court citations, Kaylovest/Villa Via dual identity (EVENT_124), Bantjies manufacture admission (EVENT_119), 100+ banking change emails (EVENT_121), and Rynette-Bantjies conspiracy analysis (1,632 emails)."
  },
  "relations": {
    "ownership_relations": [
      {
        "relation_id": "REL_OWN_001",
        "relation_type": "owns",
        "source_entity": "PERSON_005",
        "target_entity": "ORG_003",
        "strength": "complete_ownership",
        "legal_status": "legitimate",
        "evidence": [
          "company_registration_uk",
          "payment_records_28_months"
        ],
        "evidence_verified": "2025-12-14T05:36:53.168355",
        "ad_res_j7_evidence": [
          "ANNEXURES/JF04 - CIPC registration documents",
          "ANNEXURES/JF01 - Shopify ownership evidence"
        ],
        "evidence_repository": "https://github.com/cogpy/ad-res-j7",
        "comprehensive_evidence_index": "https://github.com/cogpy/ad-res-j7/blob/main/docs/evidence/COMPREHENSIVE_EVIDENCE_INDEX.md"
      }
    ],
    "control_relations": [
      {
        "relation_id": "REL_CTRL_001",
        "relation_type": "controls",
        "source_entity": "PERSON_001",
        "target_entity": "ORG_001",
        "control_type": "directorial_control",
        "legal_status": "disputed",
        "evidence": [
          "director_appointment",
          "operational_decisions"
        ],
        "evidence_verified": "2025-12-14T05:36:53.168372"
      },
      {
        "relation_id": "REL_CTRL_002",
        "relation_type": "controls_financial_systems",
        "source_entity": "PERSON_002",
        "target_entity": "ORG_001",
        "control_type": "financial_controller",
        "legal_status": "fraudulent",
        "evidence": [
          "MAILBOX_SAGE_NOTIFICATIONS",
          "MAILBOX_RYNETTE_FINANCIAL_EMAILS",
          "bank_account_changes"
        ],
        "timeline_events": [
          "KE_004",
          "KE_007",
          "KE_008"
        ],
        "evidence_verified": "2026-02-09T04:52:00.000000"
      },
      {
        "relation_id": "REL_CTRL_009",
        "relation_type": "instructed_email_diversion",
        "source_entity": "PERSON_004",
        "target_entity": "PERSON_002",
        "evidence": ["MAILBOX_JAX_DIVERT_EMAIL_2020"],
        "significance": "Enabled Rynette's information control.",
        "evidence_verified": "2026-02-09T04:52:00.000000"
      },
      {
        "relation_id": "REL_CTRL_010",
        "relation_type": "instructed_payment_redirection",
        "source_entity": "PERSON_002",
        "target_entity": "PERSON_LINDA",
        "evidence": ["MAILBOX_RYNETTE_BANKING_DETAILS_EMAIL"],
        "significance": "Rynette initiated the payment redirection campaign.",
        "evidence_verified": "2026-02-09T04:52:00.000000"
      },
      {
        "relation_id": "REL_CTRL_011",
        "relation_type": "instructed_domain_change",
        "source_entity": "PERSON_002",
        "target_entity": "PERSON_GAYANE",
        "evidence": ["MAILBOX_GAYANE_EMAIL_CHANGE_2025"],
        "significance": "Rynette orchestrated the email domain change.",
        "evidence_verified": "2026-02-09T04:52:00.000000"
      }
    ],
    "conspiracy_relations": [
      {
        "relation_id": "REL_CONSP_001",
        "relation_type": "co_conspirator",
        "source_entity": "PERSON_001",
        "target_entity": "PERSON_002",
        "conspiracy_type": "coordinated_criminal_activity",
        "evidence_strength": "conclusive",
        "shared_events": 12,
        "evidence": [
          "payment_redirection_scheme_2025_04_01",
          "unauthorized_beneficiary_changes_2025_05_02",
          "coordinated_fund_diversions_2025_06_30",
          "MAILBOX_EVIDENCE"
        ],
        "pattern": "systematic_coordination",
        "evidence_verified": "2026-02-09T04:52:00.000000"
      },
      {
        "relation_id": "REL_CONSP_004",
        "relation_type": "co_conspirator",
        "source_entity": "PERSON_007",
        "target_entity": "PERSON_001",
        "conspiracy_type": "coordinated_fraud_concealment",
        "evidence_strength": "conclusive",
        "shared_events": [
          "EVENT_H005",
          "EVENT_H006",
          "EVENT_025",
          "EVENT_026",
          "KE_010",
          "KE_011",
          "KE_012"
        ],
        "evidence": [
          "trial_balance_manipulation_2020",
          "stock_adjustment_fraud_concealment_2025",
          "audit_dismissal_2025_06_10",
          "MAILBOX_BANTJIES_BANK_STATEMENTS_2020"
        ],
        "pattern": "systematic_coordination",
        "motive": "R18.75M (Ketoni debt to FFT)_debt_concealment",
        "evidence_verified": "2026-02-09T04:52:00.000000"
      }
    ],
    "access_relations": [
        {
            "relation_id": "REL_ACCESS_001",
            "relation_type": "had_financial_access_since_2020",
            "source_entity": "PERSON_007",
            "target_entity": "ORG_001",
            "evidence": ["MAILBOX_BANTJIES_BANK_STATEMENTS_2020"],
            "significance": "Bantjies had deep financial access four years before his trustee appointment.",
            "evidence_verified": "2026-02-09T04:52:00.000000"
        },
        {
            "relation_id": "REL_ACCESS_002",
            "relation_type": "controlled_sage_since_2020",
            "source_entity": "PERSON_002",
            "target_entity": "ORG_001",
            "evidence": ["MAILBOX_SAGE_NOTIFICATIONS"],
            "significance": "Rynette had long-term control over the financial system.",
            "evidence_verified": "2026-02-09T04:52:00.000000"
        }
    ],
    "insider_relations": [
        {
            "relation_id": "REL_INSIDER_001",
            "relation_type": "had_insider_knowledge_via_george_group",
            "source_entity": "PERSON_007",
            "target_entity": "ORG_017",
            "evidence": ["MAILBOX_BANTJIES_KETONI_GEORGE_GROUP"],
            "significance": "Bantjies had insider knowledge of the Ketoni deal through his connection to Kevin Derrick.",
            "evidence_verified": "2026-02-09T04:52:00.000000"
        }
    ]
  }
}
```

### [Mailbox Evidence Relations (2026-02-09)](./MAILBOX_EVIDENCE_RELATIONS_2026_02_09.md)
This document outlines key relationships and communication patterns discovered through the analysis of the RegimA Exchange mailbox data.

### [Contempt Relations (2026-02-09)](./CONTEMPT_RELATIONS_2026_02_09.md)
This document outlines the relationships relevant to the contempt of court application (brought under Uniform Rule 45A).

### [Rynette-Bantjies Conspiracy (2026-03-07)](./RYNETTE_BANTJIES_CONSPIRACY_2026_03_07.md)
Comprehensive analysis of 1,632 email communications revealing the coordinated conspiracy between Rynette Farrar and Daniel Bantjies.

### [Villa Via / Kaylovest Identity (2026-03-07)](./VILLA_VIA_KAYLOVEST_IDENTITY.md)
Dual corporate identity discovery: Villa Via Arcadia No 2 CC and Kaylovest Three (Pty) Ltd share base registration number 1996/004451.

### [Aymac / Kaylovest / Elliott Network (2026-03-07)](./AYMAC_KAYLOVEST_ELLIOTT_NETWORK.md)
Triple corporate identity confusion across three entities controlled by Peter Faucitt.

### [Forgery Backdating Relations (2026-02-18)](./FORGERY_BACKDATING_RELATIONS_2026_02_18.md)
Two-date distinction between the 28 June 2024 trust amendment forgery and the 11 August 2025 backdated appointment.

---

*Last updated: 2026-03-08 | LEX-RECON Cross-Repository Reconciliation Engine*


### 4. Employee Collusion (KF0019 Evidence)
* **Rynette Farrar & Peter Faucitt:** Farrar provided confirmatory affidavit (PF19) supporting Peter's contempt application against Jax.
* **Gayane Williams & Peter Faucitt:** Williams provided confirmatory affidavit (PF20) supporting Peter's contempt application against Jax.
* **Oliver Mphande & Peter Faucitt:** Mphande provided stock sheets (PF18) to Peter while Peter was attempting to assert control over Jax's business.
