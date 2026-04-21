# Legal Filings Index

**Last Updated:** 2026-04-21 (v21.4 — Direct Judgment Integration Layer)

> **v21 Pipeline:** `/fin-audit-za-v2(/evidence-process)` applied SOX 404/ICFR methodology, SA regulatory overlays (SARS, FICA, POCA, Companies Act 71/2008, PRECCA), and forensic evidence standards to all filings.  
> **v21.1 Refinement Layer (2026-04-14):** Canonical entity references, timeline-anchor discipline, updated red-team critique, and a cross-filing addendum have been added on top of the v21 filing baseline. Use the live refinement artifacts below whenever a filing still points to an older direct version.

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
| **Red Team Critique** | [v22 (2026-04-14)](./RED_TEAM_CRITIQUE_2026-04-14_v22.md) | Vulnerability Analysis | **ACTIVE** |
| **Appeal Red-Team Critique** | [2026-04-20 baseline](./APPEAL_RED_TEAM_CRITIQUE_2026-04-20.md) | Leave-to-appeal loophole analysis | **ACTIVE** |
| **Appeal Rebuttal Addendum** | [2026-04-20 baseline](./APPEAL_REBUTTAL_ADDENDUM_2026-04-20.md) | Evidence-focused response directions | **ACTIVE** |
| **Direct-Judgment Appeal Critique** | [2026-04-21](./APPEAL_RED_TEAM_CRITIQUE_2026-04-21_DIRECT_JUDGMENT.md) | Appeal loophole analysis after integrating the full judgment | **ACTIVE** |
| **Direct-Judgment Appeal Rebuttal** | [2026-04-21](./APPEAL_REBUTTAL_ADDENDUM_2026-04-21_DIRECT_JUDGMENT.md) | Respondent-side answer anchored to the court's actual findings | **ACTIVE** |
| **Leave-to-Appeal Opposition Framework** | [2026-04-20](./LEAVE_TO_APPEAL_OPPOSITION_FRAMEWORK_2026-04-20.md) | Cross-filing impact and integration discipline | **ACTIVE** |
| **Forensic Audit Memorandum** | [2026-04-20](./FORENSIC_AUDIT_MEMORANDUM_2026-04-20.md) | fin-audit-za-v2 control findings, deficiency mapping, filing impact | **ACTIVE** |
| **Filing Refinement Addendum** | [v21.1 (2026-04-14)](./FILING_REFINEMENT_ADDENDUM_2026-04-14.md) | Canonical entities, timeline anchors, rebuttal language | **ACTIVE** |
| **Red-Team Rebuttal Addendum** | [2026-04-21](./RED_TEAM_REBUTTAL_ADDENDUM_2026-04-21.md) | Latest defence-defeat language based on April 21 chronology/entity refinements | **ACTIVE** |
| **Procedural Hierarchy** | [Five-Tier Framework](./CIVIL_CONTEMPT_ANALYSIS_2026_02_09.md) | *Schlesinger* + *Mokweni* + *Dreyer* | **DOCUMENTED** |

---

## v21 / v21.1 Filing Improvements

The v21 update applies the `/fin-audit-za-v2` SA forensic audit methodology to all filings, while the 2026-04-14 v21.1 layer adds GitHub Pages navigation and rebuttal discipline:

| Improvement | Description |
|-------------|-------------|
| **Entity Deduplication** | Resolved 4 duplicate entities (RegimA SA, Ketoni, Chantal, Linda Kruger) |
| **Relation Enrichment** | Added source/target fields to all 38 core relations; expanded to 141 total |
| **Event Date Resolution** | Resolved 29 events with "Unknown" dates where evidence permits |
| **Cross-Reference Integrity** | Fixed 21 undefined entity references in events |
| **Timeline Synchronization** | Aligned 151 timeline entries with 148 events |
| **Canonical Entity References** | Normalized Linda, Ketoni, Pottas Attorneys, and RegimA SA references for filing consistency |
| **Timeline Anchor Discipline** | Added a cross-filing timeline-anchor layer to defeat chronology attacks |
| **Red-Team Refresh** | Replaced the v16.2 critique with a v22 cross-application loophole analysis |
| **Appeal-Stage Layer** | Added leave-to-appeal critique, rebuttal, and cross-filing framework tied to the 26/30 March 2026 chronology |
| **Forensic Audit Refresh (2026-04-20)** | Added a dedicated fin-audit-za-v2 memorandum mapping current evidence to material weaknesses, tax/VAT risk, and filing implications |
| **Coherence Refresh (2026-04-21)** | Added a rebuttal addendum aligned to the updated June retaliation and August control-seizure relation pages, plus the latest case-model refinement report |
| **Direct Judgment Refresh (2026-04-21)** | Added a direct-evidence integration report, a judgment-anchored appeal critique, and a judgment-anchored appellate rebuttal layer |
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
| Main GitHub Pages Home | [View](../index.md) |
| Application 1: Civil and Criminal | [View](../application-1-civil-criminal.md) |
| Application 2: CIPC and POPIA | [View](../application-2-cipc-popia.md) |
| Application 3: Commercial Crime and Tax Fraud | [View](../application-3-commercial-crime-tax-fraud.md) |
| Filing Refinement Addendum | [View](./FILING_REFINEMENT_ADDENDUM_2026-04-14.md) |
| Red-Team Rebuttal Addendum | [View](./RED_TEAM_REBUTTAL_ADDENDUM_2026-04-21.md) |
| Red-Team Critique v22 | [View](./RED_TEAM_CRITIQUE_2026-04-14_v22.md) |
| Appeal Red-Team Critique (baseline) | [View](./APPEAL_RED_TEAM_CRITIQUE_2026-04-20.md) |
| Appeal Rebuttal Addendum (baseline) | [View](./APPEAL_REBUTTAL_ADDENDUM_2026-04-20.md) |
| Direct-Judgment Appeal Critique | [View](./APPEAL_RED_TEAM_CRITIQUE_2026-04-21_DIRECT_JUDGMENT.md) |
| Direct-Judgment Appeal Rebuttal | [View](./APPEAL_REBUTTAL_ADDENDUM_2026-04-21_DIRECT_JUDGMENT.md) |
| Direct Judgment Integration Report | [View](../reports/JUDGMENT_DIRECT_EVIDENCE_INTEGRATION_2026-04-21.md) |
| Leave-to-Appeal Opposition Framework | [View](./LEAVE_TO_APPEAL_OPPOSITION_FRAMEWORK_2026-04-20.md) |
| Forensic Audit Memorandum | [View](./FORENSIC_AUDIT_MEMORANDUM_2026-04-20.md) |
| Case-Model Refinement Report (2026-04-21) | [View](../reports/ENTITY_RELATION_EVENT_TIMELINE_REFINEMENT_2026-04-21.md) |
| Evidence Index | [View](../evidence-index-enhanced.md) |
| Entities Directory | [View](../entities/index.md) |
| Events Directory | [View](../events/index.md) |
| Relations Analysis | [View](../relations/index.md) |
| Master Timeline | [View](../timeline.md) |

---

*Generated by `/fin-audit-za-v2(/evidence-process)` pipeline on 2026-03-25, updated on 2026-04-14 with the timeline / filing refinement layer, updated on 2026-04-20 with the appeal-stage and forensic-audit refinement layers, and updated on 2026-04-21 with the direct-judgment integration layer.*
