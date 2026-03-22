# Rynette Emails Backdated "Main Trustee" Appointment to Bantjies (EVENT_104)

## Event Metadata
- **Type:** Unknown
- **Entities Involved:** Unknown
- **Source:** Unknown


**Date:** 2025-08-11  
**Backdated To:** 2025-07-01  
**Category:** Fraud / Backdating / Trust Manipulation  
**Criminal Threshold:** 95% EXCEEDED  
**Phase:** PHASE_4 — Control Seizure

## Description

On 11 August 2025, Rynette Farrar emailed Danie Bantjies his actual appointment communication as trustee — contained in a "Main Trustee" agreement that was **backdated to 1 July 2025**. Two days later, on 13 August 2025, Bantjies swore his confirmatory (supporting) affidavit for Peter's ex parte interdict application. Three days after that, on 14 August 2025, the interdict application was filed via Court Online.

## Distinction from EVENT_103 (28 June 2024)

There are **two dates in play**, and the distinction is legally critical:

| Date | Document | Significance |
|------|----------|-------------|
| **28 June 2024** (EVENT_103) | Trust Amendment Resolution with forged "pp Peter" signature | The **forgery date** — Rynette forges Peter's signature to install Bantjies as trustee |
| **11 August 2025** (THIS EVENT) | "Main Trustee" appointment communication emailed to Bantjies, backdated to 1 July 2025 | The **backdated appointment communication** — sent 2 days before Bantjies swears his affidavit |

## The Backdating

The "Main Trustee" agreement was backdated to **1 July 2025** — six weeks before it was actually communicated on 11 August 2025. The backdating served to:

1. Create a false paper trail suggesting the appointment was established well before the interdict
2. Disguise the true coordination timeline between the appointment and the litigation
3. Give Bantjies apparent authority predating the interdict application

## Coordinated Interdict Timeline (August 2025)

| Date | Event | Actor | Days Before Filing |
|------|-------|-------|--------------------|
| **2025-08-11** | **Rynette emails "Main Trustee" agreement to Bantjies** | Rynette Farrar | **3 days** |
| 2025-08-11 | Settlement agreement signed | Peter Faucitt | 3 days |
| **2025-08-13** | **Bantjies swears confirmatory affidavit** | Danie Bantjies | **1 day** |
| **2025-08-14** | **Interdict filed via Court Online (08:16:25 SAST)** | Elliott Attorneys | **0 days** |
| 2025-08-19 | Interdict heard and granted ex parte | Court | - |

## Bantjies' Provable Foreknowledge

When Bantjies received the "Main Trustee" appointment email on 11 August 2025, he already knew:

1. **He was installed via forgery** (EVENT_103) — Rynette had signed "pp Peter" on 28 June 2024
2. **He owed R18.685M to the trust** via Ketoni — a massive conflict of interest
3. **He was being asked to support an interdict** against the other beneficiaries
4. **The appointment was backdated** — the document said 1 July 2025 but was only sent 11 August 2025

Despite this knowledge, Bantjies swore his confirmatory affidavit two days later, constituting **perjury with provable foreknowledge**.

## Evidence

| Document | Source | Significance |
|----------|--------|-------------|
| "Main Trustee" agreement (backdated 1 July 2025) | Trust records | The backdated document |
| Email: Rynette to Bantjies (11 August 2025) | Exchange mailbox | Proves actual communication date |
| Bantjies confirmatory affidavit (13 August 2025) | MAT4719 pp. 69-71 | Sworn 2 days after receiving appointment |
| Court Online filing (14 August 2025, 08:16:25) | Court records | Filed 3 days after appointment email |
| Trust Amendment with forged "pp Peter" (28 June 2024) | SF15 | The underlying forgery |

## Legal Framework

- **Fraud (Common Law):** Backdating a legal document to create a false impression
- **Perjury (Common Law):** Bantjies swearing affidavit with knowledge of forgery and conflict
- **Uttering (Common Law):** Using the backdated document in court proceedings
- **Trust Property Control Act 57 of 1988:** Breach of fiduciary duty
- **POCA s 2(1)(e):** Pattern of racketeering activity

## Cross-References

- **[EVENT_103](./EVENT_103.md)** — The underlying forgery (28 June 2024)
- **[EVENT_049](./EVENT_049.md)** — Bantjies certifies Peter's affidavit (13 August 2025)
- **[EVENT_059](./EVENT_059.md)** — Settlement agreement timing (11 August 2025)
- **[EVENT_060](./EVENT_060.md)** — Peter files interdict (13-14 August 2025)
- **[Void Ab Initio Report](../filings/FINAL_VOID_AB_INITIO_REPORT_2026_02_09.md)** — Interdict nullity analysis

```json
{
  "event_id": "EVENT_104",
  "date": "2025-08-11",
  "backdated_to": "2025-07-01",
  "title": "Rynette Emails Backdated 'Main Trustee' Appointment to Bantjies",
  "category": "fraud",
  "event_type": "backdated_appointment_communication",
  "perpetrators": ["PERSON_002", "PERSON_001"],
  "co_conspirators": ["PERSON_007"],
  "victims": ["PERSON_003", "PERSON_004", "PERSON_005"],
  "entities_involved": ["Faucitt Family Trust"],
  "description": "Rynette Farrar emails Danie Bantjies his 'Main Trustee' appointment communication, backdated to 1 July 2025. Two days later Bantjies swears his confirmatory affidavit for the ex parte interdict. The underlying trust amendment with forged 'pp Peter' signature is dated 28 June 2024 (EVENT_103).",
  "legal_significance": "fraud_backdating_perjury_facilitation",
  "evidence": [
    "Main_Trustee_Agreement_backdated_2025-07-01",
    "Email_Rynette_to_Bantjies_2025-08-11",
    "Bantjies_Confirmatory_Affidavit_2025-08-13",
    "Court_Online_Filing_2025-08-14"
  ],
  "pattern": "control_seizure",
  "critical": true,
  "timeline_phase": "PHASE_4",
  "t_months": "T-9",
  "ad_res_j7_evidence": [
    "ANNEXURES/JF10 - Trust documents",
    "MAT4719 pp. 69-71"
  ],
  "burden_of_proof": "criminal_95",
  "criminal_threshold": "yes",
  "related_events": ["EVENT_103", "EVENT_049", "EVENT_059", "EVENT_060"],
  "two_date_distinction": {
    "forgery_date": "2024-06-28",
    "appointment_communication_date": "2025-08-11",
    "backdated_to": "2025-07-01"
  }
}
```

---
*Created: 2026-02-18 — Two-date distinction integration*
