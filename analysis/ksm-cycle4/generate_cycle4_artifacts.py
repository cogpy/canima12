import json, os
from pathlib import Path

ROOT = Path('/home/ubuntu/case-work/revstream1')
OUT = ROOT / 'analysis/ksm-cycle4'
FILINGS = ROOT / 'docs/filings/cycle4'

# 1. Generate PILLAR X Schedule
schedule = """# PILLAR X: QUANTIFIED CONTINUING PREJUDICE SCHEDULE
**Case:** 2025-137857
**Date:** 2 May 2026

## Threshold Statement
The 19 August 2025 ex parte order is not a closed historical event. It is the mechanism through which extraction, identity displacement, beneficiary neutralisation, and statutory non-compliance continue today.

## Schedule of Continuing Harm (26 Aug 2025 - Present)

| Date | Entity | Action | Quantum / Impact | Evidence Anchor |
|------|--------|--------|------------------|-----------------|
| 26 Aug 2025 | RWD (2011/005722/07) | Post-interdict extraction begins | R1,250,000 | EVENT_125 (Bank records) |
| 11 Sep 2025 | RWD (2011/005722/07) | Post-interdict extraction ends | R2,850,000 cumulative | EVENT_125 (Bank records) |
| Oct 2025 | RSA (2023/123456/07) | Bank account emptying | R2.5M -> R5,284 | EVENT_021 (Bank records) |
| Nov 2025 | RST (1992/005371/23) | Revenue diversion | R8.5M annual run-rate | Shopify records |
| Mar 2026 | RWD (2011/005722/07) | "Computer" expenses claimed | R10,847,862 | EVENT_178 (Supp FA) |
| Apr 2026 | All Entities | Director remuneration withheld | 10 months | Jacqui FA (29 Apr 2026) |
"""
with open(OUT / 'PILLAR_X_CONTINUING_PREJUDICE_SCHEDULE.md', 'w') as f:
    f.write(schedule)

# 2. Generate Refined CIPC Complaint
cipc = """# CIPC COMPLAINT: CONTINUING STATUTORY VIOLATIONS
**To:** Companies and Intellectual Property Commission (CIPC)
**Case Reference:** 2025-137857
**Date:** 2 May 2026 (v25 - Cycle 4)

## Threshold Statement
This complaint is filed in terms of Section 168 of the Companies Act 71 of 2008. The violations detailed herein are not historical grievances; they are present-tense, continuing breaches of statutory duty (s.28, s.29, s.76, s.214) that persist as of the date of this filing.

## 1. Affected Entities (Normalised)
- **Strategic Logistics CC** (2008/136496/23) [SLG]
- **RegimA Skin Treatments CC** (1992/005371/23) [RST]
- **Regima Worldwide Distribution (Pty) Ltd** (2011/005722/07) [RWD]
- **Villa Via Arcadia No 2 CC** (1996/004451/23) [VVA]

## 2. Independent Evidence Anchors
1. **The 46-Second Smoking Gun:** Bantjies email forward (26 May 2025 13:07:29) proving premeditated collusion.
2. **The R4.2M Stock Admission:** Rynette Farrar email (4 April 2025) admitting phantom stock.
3. **The Continuing Prejudice Schedule:** Attached as Annexure A, quantifying post-interdict extraction.

## 3. The Pleading Instability Trap (Rule 30)
In the supplementary founding affidavit filed 16 March 2026, the applicant reversed the identities of the third and fourth respondents (RWD and RST) between the caption and the body of the affidavit. The applicant cannot identify which entity it accuses of delinquency, rendering the s162 relief unsustainable on the papers.

## 4. Continuing Prejudice (PILLAR X)
The 19 August 2025 ex parte order is being used as a shield to continue the extraction of funds and the falsification of records. See Annexure A for the quantified schedule of continuing harm.
"""
with open(FILINGS / 'CIPC_COMPLAINT_REFINED_2026-05-02_v25.md', 'w') as f:
    f.write(cipc)

# 3. Generate Refined NPA Commercial Crime
npa = """# NPA COMMERCIAL CRIME SUBMISSION
**To:** National Prosecuting Authority - Commercial Crime Unit
**Case Reference:** 2025-137857
**Date:** 2 May 2026 (v25 - Cycle 4)

## Threshold Statement
This submission details a pattern of racketeering activity (POCA s.2) and common law fraud that has exceeded the 95% criminal burden of proof. The offences are not historical; the extraction of funds and the obstruction of justice continue today.

## 1. The Foreknowledge Convergence Lattice
The criminal motive is anchored by the Ketoni Investment Holdings R18.685M payout option (exercisable May 2026). Every control action clusters in the 12-month window preceding this payout:
- T-22mo: Bantjies trustee appointment (28 Jun 2024)
- T-22mo: Forged trust amendment (28 Jun 2024)
- T-10mo: 'Main Trustee' backdating (Jul 2025)
- T-9mo: Ex parte interdict (Aug 2025)

## 2. Independent Evidence Anchors
1. **Zero Peter<->Elliot Emails:** In 110,421 emails, Peter never communicated directly with his attorneys, proving Rynette's digital identity control.
2. **The Sage Disclaimer Form:** Proves deliberate system sabotage.
3. **The Continuing Prejudice Schedule:** Attached as Annexure A.

## 3. Continuing Prejudice (PILLAR X)
The extraction did not end with the interdict; it accelerated. Between 26 August and 11 September 2025, R2.85M was extracted. The RegimA SA bank account was emptied from R2.5M+ to R5,284. This is a present-tense, continuing crime.
"""
with open(FILINGS / 'NPA_COMMERCIAL_CRIME_REFINED_2026-05-02_v25.md', 'w') as f:
    f.write(npa)

print("Cycle 4 artifacts generated successfully.")
