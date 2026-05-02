import json, os
from pathlib import Path

ROOT = Path('/home/ubuntu/case-work/revstream1')
OUT = ROOT / 'analysis/ksm-cycle5'
FILINGS = ROOT / 'docs/filings/cycle5'

# 1. Generate PILLAR XI: Independent Forensic Audit Anchor
pillar_xi = """# PILLAR XI: INDEPENDENT FORENSIC AUDIT ANCHOR
**Case:** 2025-137857
**Date:** 2 May 2026

## Threshold Statement
The evidentiary field contains multiple contested admissions and inferred quantums (e.g., the R5.4M stock discrepancy, the R10.8M "computer expenses", the R2.85M post-interdict extraction). To close the criminal burden gap (95%), these must be converted into third-party expert findings.

## The Anchor
The Independent Forensic Audit Anchor is instantiated via Prayer 5 of the Civil Reconsideration Application:
*\"Appoint an independent, court-funded forensic auditor to audit the entities for the period 1 January 2020 to date.\"*

## Verification Matrix
| Contested Issue | Current Evidence | Audit Output Required |
|-----------------|------------------|-----------------------|
| R5.4M Stock Discrepancy | Bantjies email admission | Expert finding of transfer pricing manipulation |
| R10.8M "Computer Expenses" | Applicant's own affidavit | Expert finding of expense dumping / misallocation |
| R2.85M Post-Interdict Extraction | FNB Statements | Expert finding of s.76(3)(b) breach |
| Revenue Diversion | Shopify Invoices | Expert finding of s.28/s.29 breach |
"""
with open(OUT / 'PILLAR_XI_FORENSIC_AUDIT_ANCHOR.md', 'w') as f:
    f.write(pillar_xi)

# 2. Generate Rule 35(3) Discovery Package
rule35 = """# RULE 35(3) DISCOVERY NOTICE
**In re:** Faucitt v Faucitt & Others, Case No. 2025-137857
**Date:** 2 May 2026 (Cycle 5)

## Notice to Produce Documents
Take notice that the Respondent requires the Applicant to produce for inspection the following documents referred to in the pleadings or affidavits, or relevant to the matters in question:

1. **The Implicated Attorneys' File:** All attendance notes, file notes, and correspondence recording the source of instructions for the *ex parte* application of 19 August 2025, specifically for the period 1 June 2025 to 19 August 2025. (Relevance: PILLAR IX - Attorney Complicity).
2. **Commissioner-of-Oaths Records:** The register maintained by the Commissioner of Oaths who commissioned the founding affidavit of Peter Andrew Faucitt dated 13 August 2025. (Relevance: PILLAR XII - Signature Forgery).
3. **Ketoni Investment Holdings Correspondence:** All correspondence and board minutes relating to the R18.685M payout option exercisable in May 2026. (Relevance: PILLAR XII - Foreknowledge Convergence Lattice).
"""
with open(FILINGS / 'RULE_35_3_DISCOVERY_NOTICE_2026-05-02.md', 'w') as f:
    f.write(rule35)

# 3. Generate Document Examiner Brief
doc_examiner = """# FORENSIC DOCUMENT EXAMINER BRIEF
**Case:** 2025-137857
**Date:** 2 May 2026 (Cycle 5)

## Objective
To determine the authenticity of the signature purporting to be that of Peter Andrew Faucitt on the founding affidavit dated 13 August 2025.

## Materials Provided
1. **Questioned Document (Q1):** Founding affidavit dated 13 August 2025.
2. **Known Specimens (K1-K10):** Verified signatures of Peter Andrew Faucitt from the period 2020-2026 (bank mandates, trust deeds, CIPC filings).

## Specific Instructions
1. Compare Q1 against K1-K10.
2. Identify any signs of simulation, tracing, or digital manipulation.
3. Provide a sworn expert report suitable for High Court and criminal proceedings.
"""
with open(FILINGS / 'DOCUMENT_EXAMINER_BRIEF_2026-05-02.md', 'w') as f:
    f.write(doc_examiner)

print("Cycle 5 artifacts generated successfully.")
