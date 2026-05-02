import json, os
from pathlib import Path

ROOT = Path('/home/ubuntu/case-work/revstream1')
OUT = ROOT / 'analysis/ksm-cycle6'
FILINGS = ROOT / 'docs/filings/cycle6'

# 1. Generate Gradient Schedule Annexure
gradient_schedule = """# ANNEXURE B: GRADIENT LADDER OF ESCALATION
**Case:** 2025-137857
**Date:** 2 May 2026

This schedule demonstrates the seamless escalation of the Applicant's conduct from minor procedural irregularity to organised criminal enterprise. Each rung of the ladder triggers a specific statutory provision and is proven by a specific evidentiary Pillar.

| Rung | Conduct | Statutory Provision | Burden | Proving Pillar |
|------|---------|---------------------|--------|----------------|
| 1 | Caption Inversion (EVENT_178) | Rule 30 (Irregular Proceedings) | 50% | PILLAR X-bis |
| 2 | Material Non-Disclosure | Common Law (Set-aside ex parte) | 50% | PILLARS III, V |
| 3 | Perjury (J417 Declaration) | s.319 CPA / Justices of Peace Act | 95% | PILLAR II |
| 4 | Forgery (13 Aug 2025 Signature) | s.13 Common Law / ECA | 95% | PILLAR XII |
| 5 | Identity Fraud (Sage/Exchange) | POPIA s.74 + Common Law | 95% | PILLARS VI, VIII, IX |
| 6 | Theft / Conversion (R2.85m) | s.96 General Law Amendment | 95% | PILLAR X |
| 7 | Organised Criminal Enterprise | POCA s.2(1)(e) / s.2(1)(f) | 95% | PILLARS I-IX (Pattern) |
"""
with open(OUT / 'GRADIENT_SCHEDULE_ANNEXURE.md', 'w') as f:
    f.write(gradient_schedule)

# 2. Generate Rule 35(7) Compel Application
rule35_7 = """# RULE 35(7) APPLICATION TO COMPEL DISCOVERY
**In re:** Faucitt v Faucitt & Others, Case No. 2025-137857
**Date:** 2 May 2026 (Cycle 6)

## Notice of Motion
Take notice that the Respondent intends to apply to this Court for an order in the following terms:
1. Compelling the Applicant to comply with the Rule 35(3) Notice served on 2 May 2026 within 5 days.
2. In the event of non-compliance, striking out the Applicant's claim and dismissing the *ex parte* application with costs *de bonis propriis*.

## Founding Affidavit (Extract)
The Applicant has failed to produce the Implicated Attorneys' file, the Commissioner-of-Oaths register, and the Ketoni board minutes. This failure is not merely procedural; it is evidence of consciousness of guilt regarding the forgery (PILLAR XII) and attorney complicity (PILLAR XIII) anchors.
"""
with open(FILINGS / 'RULE_35_7_COMPEL_APPLICATION_2026-05-02.md', 'w') as f:
    f.write(rule35_7)

# 3. Generate Named Examiner Brief
named_examiner = """# FORENSIC DOCUMENT EXAMINER BRIEF (NAMED)
**To:** Cecil Greenfield Forensic Document Examiners, Pretoria
**Case:** 2025-137857
**Date:** 2 May 2026 (Cycle 6)

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
with open(FILINGS / 'NAMED_EXAMINER_BRIEF_2026-05-02.md', 'w') as f:
    f.write(named_examiner)

# 4. Generate Conditional Pillar XIV
pillar_xiv = """# PILLAR XIV: FOREKNOWLEDGE CONVERGENCE LATTICE (CONDITIONAL)
**Case:** 2025-137857
**Date:** 2 May 2026

## Threshold Statement
This Pillar is conditionally instantiated pending the production of the Ketoni board minutes via Rule 35(3) discovery.

## The Anchor
The Ketoni R18.685M payout option (exercisable May 2026) provides the financial motive for the *ex parte* interdict. If the board minutes confirm that the payout was contingent on the removal of the Respondent, the Foreknowledge Convergence Lattice is proven.
"""
with open(OUT / 'PILLAR_XIV_FOREKNOWLEDGE_LATTICE.md', 'w') as f:
    f.write(pillar_xiv)

print("Cycle 6 artifacts generated successfully.")
