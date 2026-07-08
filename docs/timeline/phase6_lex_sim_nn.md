# Phase 6: LEX-SIM-NN Analysis & Forensic Evidence Extraction (March 2026)

**Last Updated:** 2026-03-10

This phase documents the application of the LEX-SIM-NN differentiable legal simulation pipeline to the complete body of evidence, the extraction of 355 forensic EML files from the Exchange database, and the resulting refinements to all legal filings.

---

## Key Events

| Date | Event ID | Event | Significance | Evidence |
|:-----|:---------|:------|:-------------|:---------|
| 2026-03-10 | EVENT_SIM_001 | **LEX-SIM-NN Simulation Executed** | Differentiable legal pipeline trained on 6-phase case events with VES modulation. Civil burden (50%) met at 98.86%. Criminal burden (95%) met at 98.88%. | [Simulation Report](../simulation/LEX_SIM_NN_REPORT_2026_03_10.md) |
| 2026-03-10 | EVENT_EML_001 | **Forensic EML Extraction: Bantjies** | 99 forensic EML files extracted from Exchange database for all communications mentioning Bantjies, with SHA-256 integrity hashes and forensic JSON sidecars. | [Forensic EML Index](../evidence/forensic_eml/INDEX.md) |
| 2026-03-10 | EVENT_EML_002 | **Forensic EML Extraction: Rynette** | 100 forensic EML files extracted covering Rynette Farrar communications across 28 sender domains, documenting identity impersonation and financial control. | [Forensic EML Index](../evidence/forensic_eml/INDEX.md) |
| 2026-03-10 | EVENT_EML_003 | **Forensic EML Extraction: Elliott Attorneys** | 6 forensic EML files from keegan@elliottattorneys.co.za documenting legal correspondence and threats. | [Forensic EML Index](../evidence/forensic_eml/INDEX.md) |
| 2026-03-10 | EVENT_EML_004 | **Forensic EML Extraction: ABSA/Bank Details** | 100 forensic EML files documenting bank detail changes and ABSA account references — critical evidence for revenue diversion. | [Forensic EML Index](../evidence/forensic_eml/INDEX.md) |
| 2026-03-10 | EVENT_ATTR_001 | **Evidence Attribution Analysis** | Gradient-based attribution identified Relational/Intentional and Documentary evidence as strongest categories. Testimonial identified as weakest — primary area for strengthening criminal filings. | [Simulation Report](../simulation/LEX_SIM_NN_REPORT_2026_03_10.md) |
| 2026-03-10 | EVENT_FILING_V10 | **All Filings Refined to v10** | All 7 filing types updated with LEX-SIM-NN evidence attribution scores, forensic EML cross-references, and strengthened testimonial evidence sections. | [Filings Index](../filings/index.md) |

---

## LEX-SIM-NN Key Findings

### Evidence Attribution Rankings

| Rank | Category | Civil Score | Criminal Score |
|:-----|:---------|:------------|:---------------|
| 1 | Relational/Intentional | 0.078102 | 0.079674 |
| 2 | Documentary | 0.077566 | 0.079127 |
| 3 | Temporal | 0.074615 | 0.076117 |
| 4 | Forensic | 0.071891 | 0.073338 |
| 5 | Financial | 0.068544 | 0.069924 |
| 6 | Testimonial | 0.050660 | 0.051679 |

### Per-Filing Burden Assessment

| Filing | Evidence Strength | Burden | Status |
|:-------|:------------------|:-------|:-------|
| POPIA Criminal Complaint | 94.02% | 95% | Near threshold — strengthened in v10 |
| Professional Misconduct | 92.91% | 50% | **MET** |
| CIPC Companies Act | 92.49% | 50% | **MET** |
| Commercial Crime | 92.00% | 95% | Near threshold — strengthened in v10 |
| NPA Tax Fraud | 91.75% | 95% | Near threshold — strengthened in v10 |
| Civil Action | 91.32% | 50% | **MET** |
| FIC Report | 89.58% | 50% | **MET** |

### Forensic EML Evidence Summary

| Extraction Scope | Files | Domains | Key Findings |
|:-----------------|:------|:--------|:-------------|
| Bantjies communications | 99 | 15+ | Coordinated financial control, SARS manipulation, trust capture |
| Rynette communications | 100 | 28 | Identity impersonation across all systems, operational control |
| Elliott Attorneys | 6 | 1 | Legal threats, contempt proceedings |
| ABSA/Bank details | 100 | 20+ | Revenue diversion evidence, unauthorized bank changes |
| **Total** | **355** | **28+** | **Complete forensic email archive with SHA-256 integrity** |

---

## Recommendations for Phase 7

1. **Strengthen Testimonial Evidence**: Obtain formal witness statements from customers who can confirm bank detail changes were unauthorized
2. **Expert Affidavit**: Commission forensic accounting expert report on fund flows
3. **Stylometry Expert**: Formal expert opinion on Rynette-as-Peter email authorship
4. **SARS Whistleblower**: File formal SARS whistleblower report with "manufacture" email evidence

---

*Cross-references: [LEX-SIM-NN Report](../simulation/LEX_SIM_NN_REPORT_2026_03_10.md) | [Forensic EML Index](../evidence/forensic_eml/INDEX.md) | [Filings Index](../filings/index.md)*
