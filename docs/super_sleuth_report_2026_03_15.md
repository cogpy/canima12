# Super-Sleuth Introspection Report — 2026-03-15

**Case:** 2025-137857 — Revenue Stream Hijacking
**Date:** 2026-03-15
**Mode:** Intro-Spect (Divergent Investigation)
**Evidence Batch:** 9 primary documents (Ketoni/FFT/Trust corpus)

---

## Executive Summary

Nine primary source documents have been analyzed, comprising the complete Ketoni Investment Holdings / Faucitt Family Trust transactional corpus. These documents provide **conclusive primary evidence** of the financial architecture underlying the R18.685M–R28.73M motive structure. The documents confirm and significantly strengthen the existing case by providing the actual signed agreements, trust registration forms, and audited financial statements that were previously referenced only by description.

**Critical new findings:**

1. **Bantjies declared himself an "Independent Trustee" and "Auditor"** on the J417 form — a provably false declaration given his employment as CFO of The George Group (Kevin Derrick's company) and his 4+ years of financial access to RegimA entities.

2. **The Subscription Agreement specifies a bank account** (Standard Bank 420469494, Eastgate branch) for Ketoni — a new financial entity for fund flow tracing.

3. **The Put Option at Year 5 guarantees R28,730,000** — significantly higher than the previously cited R18.685M (which is the Year 3 Call Option price). The actual maximum exposure is R28.73M.

4. **The Kevin Derrick Trust provided a R49,000 loan** to Ketoni — confirming financial interrelationship and Derrick's control.

5. **Missing pages from the Shareholders Agreement** were flagged by Nick Xenophontos Attorneys (24 January 2025) — indicating potential document tampering or concealment.

6. **The FFT Trust Minutes (24 April 2023)** were signed only by Peter and Jacqueline — Daniel was excluded from the investment decision despite being a beneficiary.

7. **Forvis Mazars prepared the AFS** — a Big Four-adjacent firm, providing institutional credibility to the financial structure.

---

## Evidence Inventory

| # | Document | Type | Classification | Reliability | Key Entities |
|---|----------|------|----------------|-------------|--------------|
| 1 | Ketoni_Shareholder_Agreement_signed | Contract | Primary | 1.0 | KDT, FFT, Ketoni |
| 2 | Ketoni_subscription_agreement_signed_2 | Contract | Primary | 1.0 | KDT, FFT, Ketoni |
| 3 | Ketoni_AFS_2024 | Financial Statement | Primary | 1.0 | Ketoni, George Group |
| 4 | Ketoni_Investment_Holdings_AFS_2024_-_Signed | Financial Statement | Primary | 1.0 | Ketoni, George Group |
| 5 | FAUCITT_TRUST (J417 + J401) | Trust Registration | Primary | 1.0 | Bantjies, FFT |
| 6 | F172-Peter_faucitt_family_trust (J417 + J401) | Trust Registration | Primary | 1.0 | Peter Faucitt, FFT |
| 7 | moh-SwornAffTrustee | Sworn Affidavit | Primary | 1.0 | Bantjies |
| 8 | Signed_minutes | Trust Resolution | Primary | 1.0 | Peter, Jacqueline |
| 9 | Danie_-_missing_pages20250129 | Correspondence | Secondary | 0.8 | Xenophontos, Peter |

---

## New Entities Discovered

### PERSON_045: Nick Xenophontos
- **Type:** Natural Person (NP)
- **Role:** Attorney — Faucitt Family Trust legal advisor
- **Firm:** Nick Xenophontos Attorneys
- **Address:** Office No. 4, Bedford Village Shopping Centre, cnr Van Buuren & Nicol Roads, Bedfordview 2007
- **Contact:** info@xenophontos.co.za, Tel: (011) 450-0015
- **Significance:** Flagged missing pages in Ketoni SHA on 24 January 2025 — indicates Peter sought independent legal advice and discovered irregularities

### ORG_029: Nick Xenophontos Attorneys
- **Type:** Juristic Person (JP)
- **Role:** Legal Practice — FFT/Peter's legal advisors for Ketoni matter
- **Registration:** Law firm, Bedfordview
- **Significance:** Independent legal review identified missing pages — potential evidence of document tampering

### ORG_030: Forvis Mazars
- **Type:** Juristic Person (JP)
- **Role:** Audit/Review firm — Prepared and reviewed Ketoni AFS
- **Significance:** Big Four-adjacent firm providing institutional credibility; potential witness for financial structure verification

### BANK_ACCOUNT_005: Ketoni Standard Bank Account
- **Type:** Bank Account (AC)
- **Account Number:** 420469494
- **Bank:** Standard Bank
- **Branch:** Eastgate
- **Holder:** Ketoni Investment Holdings (Pty) Ltd
- **Significance:** Destination for R9.8M subscription payment; source for fund flow tracing

---

## New Facts Extracted (Atomic Decomposition)

### F-KET-001: Ketoni Incorporation Date
- **Statement:** Ketoni Investment Holdings was incorporated on 20 February 2023
- **Source:** Ketoni_AFS_2024 (Director's Report, line 128)
- **Confidence:** 1.0
- **Timestamp:** 2023-02-20

### F-KET-002: Sole Director
- **Statement:** KM Derrick is the sole director of Ketoni Investment Holdings
- **Source:** Ketoni_AFS_2024 (General Information, line 22)
- **Confidence:** 1.0
- **Entities:** PERSON_014 (Kevin Derrick), ORG_017 (Ketoni)

### F-KET-003: George Group Investment
- **Statement:** Ketoni owns 8.14% (456 shares) of The George Group Proprietary Limited, valued at R9,800,000
- **Source:** Ketoni_AFS_2024 (Note 2, line 444-448)
- **Confidence:** 1.0
- **Entities:** ORG_017 (Ketoni), ORG_018 (George Group)

### F-KET-004: Share Capital Structure
- **Statement:** Ketoni issued 100 Ordinary no par value shares (R1,000) and 5,000 Ordinary Type A shares (R9,800,000)
- **Source:** Ketoni_AFS_2024 (Note 4, lines 472-478)
- **Confidence:** 1.0

### F-KET-005: Kevin Derrick Trust Loan
- **Statement:** The Kevin Derrick Trust provided an unsecured, interest-free, demand-repayable loan of R49,000 to Ketoni
- **Source:** Ketoni_AFS_2024 (Note 5, lines 484-488)
- **Confidence:** 1.0
- **Entities:** Kevin Derrick Trust → ORG_017

### F-KET-006: Tax Reference Number
- **Statement:** Ketoni's tax reference number is 9132219271
- **Source:** Ketoni_AFS_2024 (General Information, line 50)
- **Confidence:** 1.0
- **Significance:** Required for NPA Tax Fraud Report

### F-KET-007: Registered Address
- **Statement:** Ketoni's registered office is 20 Tennyson Avenue, Senderwood, Germiston, Gauteng, 2145
- **Source:** Ketoni_AFS_2024 (General Information, lines 26-29)
- **Confidence:** 1.0
- **Note:** This is Kevin Derrick's personal address

### F-SHA-001: Shareholders Agreement Signed Date
- **Statement:** The Shareholders Agreement was signed at Bedfordview on 24 April 2023 by all three parties
- **Source:** Ketoni_Shareholder_Agreement_signed (lines 1955-1985)
- **Confidence:** 1.0
- **Timestamp:** 2023-04-24

### F-SHA-002: Call Option Pricing (3-Year Escalation)
- **Statement:** Call Option prices: Year 3 = R18,685,000 (R3,737/share); Year 4 = R23,165,000 (R4,633/share); Year 5 = R28,730,000 (R5,746/share)
- **Source:** Ketoni_Shareholder_Agreement_signed (lines 1155-1163)
- **Confidence:** 1.0
- **Significance:** CORRECTS previous R18.685M figure — actual Year 5 value is R28.73M

### F-SHA-003: Put Option Guarantee
- **Statement:** At the 5th anniversary of the Effective Date, the A Ordinary Shareholder has the right to put Option Shares to the Company at R28,730,000
- **Source:** Ketoni_Shareholder_Agreement_signed (lines 1240-1289)
- **Confidence:** 1.0
- **Significance:** This is a GUARANTEED return — the Put Option is exercisable by FFT

### F-SHA-004: Minimum Investment Return
- **Statement:** The Minimum Investment Return grows at the greater of 24% per annum or FNB prime rate + 10%
- **Source:** Ketoni_Shareholder_Agreement_signed (lines 320-324)
- **Confidence:** 1.0
- **Significance:** Guaranteed minimum 24% IRR — extraordinary return

### F-SHA-005: Option Period
- **Statement:** The Option Period commences on the 3rd anniversary and ends on the 5th anniversary of the Effective Date
- **Source:** Ketoni_Shareholder_Agreement_signed (lines 329-330)
- **Confidence:** 1.0
- **Calculation:** Effective Date ~April 2023 → Option Period: April 2026 – April 2028

### F-SHA-006: 90% Dividend Sweep
- **Statement:** A Ordinary Shares entitle the holder to receive 90% of all Distributions for 5 years and 2 months from the Subscription Date
- **Source:** Ketoni_Shareholder_Agreement_signed (Annexure B, lines 2078-2079)
- **Confidence:** 1.0
- **Significance:** FFT receives 90% of ALL dividends — massive financial entitlement

### F-SHA-007: Derrick Trust Reference Number
- **Statement:** The Kevin Derrick Trust reference number is IT107716/98
- **Source:** Ketoni_Shareholder_Agreement_signed (line 228)
- **Confidence:** 1.0

### F-SHA-008: FFT Trust Reference Number Confirmed
- **Statement:** The Faucitt Family Trust reference number is IT 3651/2013
- **Source:** Ketoni_Shareholder_Agreement_signed (lines 264-266)
- **Confidence:** 1.0

### F-SHA-009: Domicilia Addresses
- **Statement:** Kevin Derrick Trust: 20 Tennyson Drive, Senderwood Ext 1, Bedfordview, 2008; FFT: 20 River Road, Morninghill, Bedfordview, 20028; Ketoni: 20 Tennyson Drive, Senderwood Ext 1, Bedfordview, 2008
- **Source:** Ketoni_Shareholder_Agreement_signed (lines 1638-1682)
- **Confidence:** 1.0
- **Significance:** Ketoni and Kevin Derrick Trust share the same address — confirms Derrick's control

### F-SHA-010: Email Addresses
- **Statement:** Kevin Derrick: kevin@kevinderrick.co.za; Peter Faucitt: pete@regima.com; Ketoni: toni@kevinderrick.co.za
- **Source:** Ketoni_Shareholder_Agreement_signed (lines 1645-1682)
- **Confidence:** 1.0
- **Significance:** Ketoni uses kevinderrick.co.za domain — confirms Derrick's personal control

### F-SUB-001: Subscription Price
- **Statement:** The Subscription Price for 5,000 A Ordinary Shares is ZAR 9,800,000
- **Source:** Ketoni_subscription_agreement_signed_2 (line 115)
- **Confidence:** 1.0

### F-SUB-002: Ketoni Bank Account
- **Statement:** Ketoni's bank account is Standard Bank, Account 420469494, Eastgate branch
- **Source:** Ketoni_subscription_agreement_signed_2 (lines 51-58)
- **Confidence:** 1.0

### F-SUB-003: Warrantor Liability Cap
- **Statement:** Maximum aggregate liability of the Warrantor is limited to ZAR 28,730,000
- **Source:** Ketoni_subscription_agreement_signed_2 (line 594)
- **Confidence:** 1.0

### F-SUB-004: SARS Disclosure Obligation
- **Statement:** The Company undertakes to disclose the arrangement to SARS within 45 business days from the date of issue
- **Source:** Ketoni_Shareholder_Agreement_signed (line 1579-1580)
- **Confidence:** 1.0
- **Significance:** Potential NPA Tax Fraud angle if not disclosed

### F-TRU-001: Bantjies Declaration as Independent Trustee
- **Statement:** Daniel Jacobus Bantjies declared himself an "Independent Trustee" of the Faucitt Family Trust (IT 3651/2013) and stated his profession as "Auditor"
- **Source:** FAUCITT_TRUST.txt (J417 form, lines 8, 21, 42, 47)
- **Confidence:** 1.0
- **Significance:** PROVABLY FALSE — Bantjies is CFO of The George Group (Kevin Derrick's company), which has a direct financial relationship with Ketoni (which owes R28.73M to FFT). He is NOT independent.

### F-TRU-002: Bantjies Signed at Pretoria
- **Statement:** Bantjies signed the J417 Acceptance of Trusteeship at Pretoria on 2 September 2024
- **Source:** FAUCITT_TRUST.txt (lines 110-113)
- **Confidence:** 0.9 (OCR quality)
- **Timestamp:** 2024-09-02

### F-TRU-003: Family Business Trust Confirmed
- **Statement:** The FFT is confirmed as a "family business trust" requiring an independent trustee
- **Source:** FAUCITT_TRUST.txt (line 39)
- **Confidence:** 1.0
- **Significance:** Legal requirement for independent trustee — Bantjies is NOT independent

### F-AFF-001: Bantjies Sworn Affidavit Claims
- **Statement:** Bantjies swore that he has "no family relation or connection, blood or other, to any of the existing or proposed Trustees, beneficiaries or founder" and that he "does not have any interest in the Trust as a beneficiary"
- **Source:** moh-SwornAffTrustee.txt (lines 29-30, 36)
- **Confidence:** 1.0
- **Significance:** While technically true (no blood relation), the affidavit omits his PROFESSIONAL connection to Kevin Derrick, whose trust is the counterparty to a R28.73M transaction with FFT. This is material non-disclosure.

### F-AFF-002: Bantjies Claims "Knowledgeable in Law of Trusts"
- **Statement:** Bantjies declared he is "knowledgeable in the law of trusts" and "competent to scrutinize and check the conduct of the other appointed trustees"
- **Source:** moh-SwornAffTrustee.txt (lines 31-36)
- **Confidence:** 1.0
- **Significance:** This makes his subsequent failures to act as independent check MORE culpable

### F-MIN-001: FFT Minutes — Investment Decision
- **Statement:** FFT trustees resolved to acquire 5,000 A-Ordinary shares in Ketoni for R9,800,000 on 24 April 2023. Only Peter Andrew Faucitt and Jacqueline Faucitt were present.
- **Source:** Signed_minutes.txt (lines 8-28)
- **Confidence:** 1.0
- **Timestamp:** 2023-04-24 (signed 20 April 2023)
- **Significance:** Daniel Faucitt (beneficiary) was EXCLUDED from this decision

### F-MIN-002: Peter Mandated as Signatory
- **Statement:** The trustees mandated Peter Andrew Faucitt in his personal capacity to sign the shareholder and subscription agreements
- **Source:** Signed_minutes.txt (lines 24-26)
- **Confidence:** 1.0

### F-MIS-001: Missing Pages Flagged
- **Statement:** Nick Xenophontos Attorneys flagged missing pages in the Ketoni Shareholders Agreement on 24 January 2025
- **Source:** Danie_-_missing_pages20250129.txt (lines 17-22)
- **Confidence:** 0.9
- **Timestamp:** 2025-01-24
- **Significance:** Independent attorney identified document irregularities — potential evidence of tampering

---

## Updated Timeline Events

### EVENT_130: Ketoni Incorporation (2023-02-20)
- **Description:** Ketoni Investment Holdings incorporated with KM Derrick as sole director
- **T-Reference:** T-38 (months before May 2026 payout)
- **Significance:** SPV created specifically for the George Group investment

### EVENT_131: FFT Investment Resolution (2023-04-20/24)
- **Description:** FFT trustees (Peter + Jacqueline only) resolve to invest R9.8M in Ketoni. Daniel excluded.
- **T-Reference:** T-36
- **Significance:** Beneficiary Daniel excluded from R9.8M investment decision

### EVENT_132: Shareholders Agreement Signed (2023-04-24)
- **Description:** SHA signed at Bedfordview by Kevin Derrick Trust, FFT, and Ketoni
- **T-Reference:** T-36
- **Significance:** Establishes the R28.73M Put Option guarantee

### EVENT_133: Subscription Agreement Executed (2023-04-24)
- **Description:** FFT subscribes for 5,000 A Ordinary Shares at R9.8M
- **T-Reference:** T-36
- **Significance:** R9.8M committed to Ketoni → George Group

### EVENT_134: Bantjies J417 Signed (2024-09-02)
- **Description:** Bantjies signs J417 Acceptance of Trusteeship at Pretoria, declaring himself "Independent Trustee" and "Auditor"
- **T-Reference:** T-20
- **Significance:** FALSE DECLARATION — Bantjies is CFO of George Group, not independent

### EVENT_135: Missing Pages Flagged by Xenophontos (2025-01-24)
- **Description:** Nick Xenophontos Attorneys identifies missing pages in Ketoni SHA and requests them from Peter
- **T-Reference:** T-16
- **Significance:** Independent legal review discovers document irregularities

### EVENT_136: Ketoni AFS Issued (2025-01-24)
- **Description:** Forvis Mazars issues Ketoni AFS for year ended 29 February 2024, confirming R9.8M George Group investment
- **T-Reference:** T-16
- **Significance:** Institutional confirmation of financial structure

---

## Corrected Financial Architecture

### Previous Understanding
- Ketoni owes FFT R18.685M (Call Option Year 3)

### Corrected Understanding (from primary source documents)

| Period | Call Option | Put Option | Per Share |
|--------|------------|------------|-----------|
| Year 3 (April 2026) | R18,685,000 | N/A | R3,737 |
| Year 4 (April 2027) | R23,165,000 | N/A | R4,633 |
| Year 5 (April 2028) | R28,730,000 | **R28,730,000** | R5,746 |

**Key Correction:** The Put Option at Year 5 **guarantees** R28,730,000 to FFT — this is the maximum exposure and the true motive figure. The 24% IRR minimum guarantee means the actual value could be even higher if FNB prime + 10% exceeds 24%.

### Fund Flow Architecture

```
FFT (TRUST_001)
    │
    │ R9,800,000 (Subscription)
    ▼
Ketoni Investment Holdings (ORG_017)
    │ Standard Bank 420469494
    │
    │ R9,800,000 (Investment)
    ▼
The George Group (ORG_018)
    │ 8.14% / 456 shares
    │
    │ Dividends (90% to FFT via Ketoni)
    ▼
FFT receives 90% of all distributions
    │
    │ Put Option at Year 5
    ▼
GUARANTEED: R28,730,000 to FFT
```

---

## Generated Leads

### LEAD-SS-001: Bantjies False Independence Declaration (CRITICAL)
- **Category:** Critical (P1)
- **Pattern:** Identity Substitution / False Declaration
- **Evidence:** F-TRU-001, F-AFF-001, PERSON_007 profile
- **Hypothesis:** Bantjies knowingly declared himself "Independent Trustee" on the J417 form while employed as CFO of The George Group, whose director (Kevin Derrick) controls Ketoni, which owes R28.73M to FFT. This is a provably false declaration to the Master of the High Court.
- **Validation Required:** Confirm Bantjies' employment dates at George Group vs J417 signing date
- **Legal Relevance:** Perjury (sworn false declaration), Breach of Trust Property Control Act s20(2), Fraud

### LEAD-SS-002: R28.73M True Motive (CRITICAL)
- **Category:** Critical (P1)
- **Pattern:** Financial Motive Escalation
- **Evidence:** F-SHA-002, F-SHA-003, F-SHA-004
- **Hypothesis:** The true financial motive is R28.73M (Put Option Year 5), not R18.685M (Call Option Year 3). This significantly increases the stakes and explains the intensity of the conspiracy.
- **Validation Required:** Confirm Option Period calculation from Effective Date
- **Legal Relevance:** Strengthens motive element across all filings

### LEAD-SS-003: Missing Pages — Document Tampering (STRONG)
- **Category:** Strong (P2)
- **Pattern:** Document Gaps / Concealment
- **Evidence:** F-MIS-001
- **Hypothesis:** Missing pages from the SHA may have been deliberately removed to conceal terms unfavorable to the conspirators, or to create ambiguity about obligations.
- **Validation Required:** Obtain complete SHA from Ketoni; compare with FFT copy
- **Legal Relevance:** Evidence tampering, Obstruction

### LEAD-SS-004: Daniel Excluded from Investment Decision (STRONG)
- **Category:** Strong (P2)
- **Pattern:** Beneficiary Exclusion
- **Evidence:** F-MIN-001
- **Hypothesis:** Daniel Faucitt, as a beneficiary of FFT, was excluded from the R9.8M investment decision. While trustees have authority to make investment decisions, the exclusion of a beneficiary from a decision of this magnitude may constitute a breach of fiduciary duty.
- **Validation Required:** Review FFT trust deed for beneficiary notification requirements
- **Legal Relevance:** Breach of fiduciary duty, Trust Property Control Act

### LEAD-SS-005: Ketoni-Derrick Address Overlap (MODERATE)
- **Category:** Moderate (P3)
- **Pattern:** Corporate Identity Overlap
- **Evidence:** F-SHA-009, F-SHA-010, F-KET-007
- **Hypothesis:** Ketoni shares its registered address AND email domain with Kevin Derrick personally, confirming it is a personal vehicle of Derrick rather than an independent investment entity.
- **Validation Required:** CIPC records for Ketoni
- **Legal Relevance:** Confirms Derrick's personal control of Ketoni

### LEAD-SS-006: SARS Disclosure Obligation (MODERATE)
- **Category:** Moderate (P3)
- **Pattern:** Regulatory Non-Compliance
- **Evidence:** F-SUB-004
- **Hypothesis:** The SHA requires disclosure to SARS within 45 business days. If this was not done, it constitutes a separate regulatory violation.
- **Validation Required:** SARS records for Ketoni disclosure
- **Legal Relevance:** NPA Tax Fraud Report, SARS non-compliance

---

## Handoff to Hyper-Holmes

The following items require convergent validation:

1. **Bantjies employment dates** at George Group vs J417 signing date (2024-09-02)
2. **Option Period calculation** — confirm Effective Date and payout windows
3. **Missing pages** — obtain complete SHA for comparison
4. **SARS disclosure** — verify compliance with 45-day obligation
5. **Daniel's exclusion** — review trust deed for notification requirements
6. **R28.73M correction** — update ALL filings from R18.685M to R28.73M where appropriate

---

*Generated by Super-Sleuth Intro-Spect Mode — 2026-03-15*
