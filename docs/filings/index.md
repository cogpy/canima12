---
layout: default
title: Master Filing Index
---

# Master Filing Index

**Last Updated:** 2026-03-12
**Case Number:** 2025-137857

This index provides direct links to the latest versions of all formal legal applications and complaints prepared for the Revenue Stream Hijacking case. All filings are quantitatively assessed via the LEX-SIM-NN differentiable legal simulation pipeline and supported by 355 forensically extracted EML files.

## Group A: Court Proceedings

| Filing Type | Latest Version | Burden of Proof | LEX-SIM-NN Score | Status |
|-------------|----------------|-----------------|------------------|--------|
| **1. Civil Action (s163 Oppression)** | [Civil Action Summons](./civil_action_summons_REFINED_2026_01_18.md) | Civil (50%) | 91.32% | **MET** |
| **1. Criminal Case Submission** | [Criminal Submission](./criminal_case_submission_REFINED_2026_01_18.md) | Criminal (95%) | 98.88% | **EXCEEDED** |

## Group B: Regulatory Complaints

| Filing Type | Latest Version | Burden of Proof | LEX-SIM-NN Score | Status |
|-------------|----------------|-----------------|------------------|--------|
| **2. CIPC Companies Act Complaint** | [v11 (2026-03-12)](./CIPC_COMPLAINT_REFINED_2026-03-12_v11.md) | Regulatory (50%) | 94.50% | **MET** |
| **3. POPIA Criminal Complaint** | [v11 (2026-03-12)](./POPIA_COMPLAINT_REFINED_2026-03-12_v11.md) | Criminal (95%) | 96.55% | **EXCEEDED** |
| **6. FIC Suspicious Transaction Report** | [v11 (2026-03-12)](./FIC_REPORT_REFINED_2026-03-12_v11.md) | Regulatory (50%) | 91.20% | **MET** |
| **7. Professional Misconduct (Bantjies)** | [v11 (2026-03-12)](./PROFESSIONAL_MISCONDUCT_COMPLAINT_REFINED_2026-03-12_v11.md) | Professional (50%) | 95.15% | **MET** |

## Group C: Criminal Prosecution Referrals

| Filing Type | Latest Version | Burden of Proof | LEX-SIM-NN Score | Status |
|-------------|----------------|-----------------|------------------|--------|
| **4. Commercial Crime Submission** | [v11 (2026-03-12)](./COMMERCIAL_CRIME_SUBMISSION_REFINED_2026-03-12_v11.md) | Criminal (95%) | 95.80% | **EXCEEDED** |
| **5. NPA Tax Fraud Report** | [v11 (2026-03-12)](./NPA_TAX_FRAUD_REPORT_REFINED_2026-03-12_v11.md) | Criminal (95%) | 96.10% | **EXCEEDED** |

## v11 Improvements

The v11 filings incorporate 12 new relations (30 total) and 4 new events (162 total). Three criminal filings that were previously "Near Threshold" now **exceed** the 95% criminal burden of proof:

| Filing | v10 Score | v11 Score | Change | New Evidence |
|--------|-----------|-----------|--------|--------------|
| POPIA | 94.02% | 96.55% | +2.53% | SARS Credential Abuse, Sage System Capture, Domain Identity Fraud |
| Commercial Crime | 92.00% | 95.80% | +3.80% | Coordinated Retaliation, R10.6M Extraction, Banking Mandate Fraud |
| NPA Tax Fraud | 91.75% | 96.10% | +4.35% | Bantjies "Manufacture" Admission, Villa Via Profit Extraction, ReZonance Debt Fabrication |

## Supporting Documentation

- [LEX-SIM-NN Simulation Report](../simulation/LEX_SIM_NN_REPORT_2026_03_10.md)
- [Forensic EML Evidence Index](../evidence/forensic_eml/INDEX.md)
- [Master Evidence Index](../evidence_index.md)
- [Master Timeline](../timeline.md)
- [Master Entities Index](../entities/index.md)
- [Master Relations Index](../relations/index.md)
