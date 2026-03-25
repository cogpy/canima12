# Legal Filings Index

**Last Updated:** 2026-03-25 (v21 — SA Forensic Audit)

> **v21 Pipeline:** `/fin-audit-za-v2(/evidence-process)` applied SOX 404/ICFR methodology, SA regulatory overlays (SARS, FICA, POCA, Companies Act 71/2008, PRECCA), and forensic evidence standards to all filings. Data models refined: 94 entities, 148 events, 141 relations, 151 timeline entries.

---

## Group A: Civil and Criminal Actions

| Filing Type | Latest Version | Burden of Proof | Status |
|-------------|----------------|-----------------|--------|
| **1. Civil Action Summons** | [Refined (2026-01-18)](./civil_action_summons_REFINED_2026_01_18.md) | Civil (50%) | **MET** |
| **1b. Criminal Case Submission** | [Refined (2026-01-18)](./criminal_case_submission_REFINED_2026_01_18.md) | Criminal (95%) | **NEAR** |
| **Void Ab Initio Analysis** | [Assessment (2026-02-09)](./VOID_AB_INITIO_REASSESSMENT_2026_02_09.md) | Common Law | **DOCUMENTED** |
| **Contempt Opposition** | [Five-Tier Framework](./CIVIL_CONTEMPT_ANALYSIS_2026_02_09.md) | *Schlesinger* + *Mokweni* | **ACTIVE** |

## Group B: Regulatory Complaints

| Filing Type | Latest Version | Burden of Proof | Composed Score | Status |
|-------------|----------------|-----------------|----------------|--------|
| **2. CIPC Companies Act Complaint** | [v21 (2026-03-25)](./CIPC_COMPLAINT_REFINED_2026-03-25_v21.md) | Regulatory (50%) | 92.03% | **MET** |
| **3. POPIA Criminal Complaint** | [v21 (2026-03-25)](./POPIA_COMPLAINT_REFINED_2026-03-25_v21.md) | Criminal (95%) | 94.12% | **NEAR** |
| **6. FIC Suspicious Transaction Report** | [v12 (2026-03-13)](./FIC_REPORT_REFINED_2026-03-13_v12.md) | Regulatory (50%) | 86.55% | **MET** |
| **7. SAICA Misconduct (Bantjies)** | [v21 (2026-03-25)](./SAICA_COMPLAINT_BANTJIES_REFINED_2026-03-25_v21.md) | Professional (50%) | 98.50% | **MET** |

## Group C: Criminal Prosecution Referrals

| Filing Type | Latest Version | Burden of Proof | Composed Score | Status |
|-------------|----------------|-----------------|----------------|--------|
| **4. NPA Commercial Crime Submission** | [v21 (2026-03-25)](./NPA_COMMERCIAL_CRIME_REFINED_2026-03-25_v21.md) | Criminal (95%) | 96.12% | **MET** |
| **5. SARS Tax Fraud Report** | [v21 (2026-03-25)](./SARS_TAX_FRAUD_REPORT_REFINED_2026-03-25_v21.md) | Criminal (95%) | 95.80% | **MET** |
| **8. NPA Perjury (Bantjies J417)** | [v21 (2026-03-25)](./NPA_PERJURY_BANTJIES_J417_2026-03-25_v21.md) | Criminal (95%) | 99.15% | **MET** |

## Group D: Legal Briefs and Strategic Analysis

| Filing Type | Latest Version | Purpose | Status |
|-------------|----------------|---------|--------|
| **Bantjies Complicity Brief** | [v21 (2026-03-25)](./LEGAL_BRIEF_BANTJIES_COMPLICITY_2026-03-18.md) | 46-Second Smoking Gun | **ACTIVE** |
| **Red Team Critique** | [v16.2 (2026-03-18)](./RED_TEAM_CRITIQUE_2026_03_18_v16.md) | Vulnerability Analysis | **ACTIVE** |
| **Procedural Hierarchy** | [Five-Tier Framework](./CIVIL_CONTEMPT_ANALYSIS_2026_02_09.md) | *Schlesinger* + *Mokweni* + *Dreyer* | **DOCUMENTED** |

---

## v21 Forensic Audit Improvements

The v21 update applies the `/fin-audit-za-v2` SA forensic audit methodology to all filings:

| Improvement | Description |
|-------------|-------------|
| **Entity Deduplication** | Resolved 4 duplicate entities (RegimA SA, Ketoni, Chantal, Linda Kruger) |
| **Relation Enrichment** | Added source/target fields to all 38 core relations; expanded to 141 total |
| **Event Date Resolution** | Resolved 29 events with "Unknown" dates where evidence permits |
| **Cross-Reference Integrity** | Fixed 21 undefined entity references in events |
| **Timeline Synchronization** | Aligned 151 timeline entries with 148 events |
| **SOX 404 Control Testing** | Applied ICFR methodology to financial control deficiencies |
| **SA Regulatory Mapping** | Mapped all violations to SARS, FICA/POCA, Companies Act 71/2008, PRECCA |

---

## Burden of Proof Assessment

| Standard | Threshold | Filings Meeting Standard |
|----------|-----------|---------------------------|
| Balance of Probabilities (Civil) | 50% | CIPC (92%), FIC (87%), SAICA (99%), Civil Action |
| Beyond Reasonable Doubt (Criminal) | 95% | NPA Perjury (99.15%), NPA Commercial Crime (96.12%), SARS Tax Fraud (95.80%) |
| Near Criminal Threshold | 90-95% | POPIA (94.12%) |

---

## Historical Filings

### March 2026 (v17/v18)
- [CIPC Complaint v17 (2026-03-18)](./CIPC_COMPLAINT_REFINED_2026-03-18_v17.md)
- [POPIA Complaint v18 (2026-03-18)](./POPIA_COMPLAINT_REFINED_2026-03-18_v18.md)
- [NPA Commercial Crime v17 (2026-03-18)](./NPA_COMMERCIAL_CRIME_REFINED_2026-03-18_v17.md)
- [SARS Tax Fraud v17 (2026-03-18)](./SARS_TAX_FRAUD_REPORT_REFINED_2026-03-18_v17.md)
- [NPA Perjury v17 (2026-03-18)](./NPA_PERJURY_BANTJIES_J417_2026-03-18_v17.md)
- [SAICA v17 (2026-03-18)](./SAICA_COMPLAINT_BANTJIES_REFINED_2026-03-18_v17.md)

### January 2026
- [CIPC Complaint (2026-01-22)](./CIPC_REFINED_2026_01_22.md)
- [POPIA Complaint (2026-01-22)](./POPIA_REFINED_2026_01_22.md)
- [NPA Tax Fraud (2026-01-22)](./NPA_REFINED_2026_01_22.md)
- [Commercial Crime (2026-01-22)](./COMMERCIAL_CRIME_REFINED_2026_01_22.md)

### December 2025
- [CIPC Complaint (2025-12-23)](./CIPC_COMPLAINT_REFINED_2025_12_23.md)
- [CIPC Complaint (2025-12-21)](./CIPC_COMPLAINT_REFINED_2025_12_21.md)

---

## Cross-References

| Resource | Link |
|----------|------|
| Application 1: Civil and Criminal | [View](../application-1-civil-criminal.md) |
| Application 2: CIPC and POPIA | [View](../application-2-cipc-popia.md) |
| Application 3: Commercial Crime and Tax Fraud | [View](../application-3-commercial-crime-tax-fraud.md) |
| Evidence Index | [View](../evidence-index-enhanced.md) |
| Entities Directory | [View](../entities/index.md) |
| Events Directory | [View](../events/index.md) |
| Relations Analysis | [View](../relations/index.md) |
| Master Timeline | [View](../timeline.md) |

---

*Generated by `/fin-audit-za-v2(/evidence-process)` pipeline on 2026-03-25.*
