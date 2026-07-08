# Forensic Fund Flow Analysis: Missing Bank Statements Report

**Date:** 23 February 2026
**Analysis Type:** acc-fund-flow / Statement Gap Identification
**Scope:** All FNB accounts across Regima Group entities

---

## Executive Summary

A comprehensive forensic analysis of all available bank statements across the fincosys repository, uploaded ZIP archives (7FN, Ent, Stat, Interim, Other, PMT), and standalone uploaded files reveals **significant gaps** in statement coverage. The uploaded image of statement #144 for account 55270035642 (Regima Skin Treatments CC) dated February-March 2014 confirms that the account has been active since at least 2002, yet the earliest statement in the system is #226 (January 2020). This represents approximately **225 missing monthly statements spanning ~18.75 years** for this account alone.

Across all accounts, the analysis identifies **over 200 missing statement periods** within the ranges we have, plus entire historical periods before the earliest available statements.

---

## Account-by-Account Gap Analysis

### TIER 1: Primary Operating Accounts (Highest Priority)

#### 55270035642 — Regima Skin Treatments CC (RST) — Day-to-Day
| Metric | Value |
|--------|-------|
| **Entity** | RST — Regima Skin Treatments CC |
| **Earliest in system** | #226 (2 Jan 2020 – 2 Jan 2021) |
| **Latest in system** | #248 (25 Oct 2022 – 25 Nov 2022) |
| **Uploaded image shows** | #144 (25 Feb 2014 – 25 Mar 2014) |
| **Statements available** | 23 of 23 (within range 226–248) |
| **Status within range** | COMPLETE |
| **Pre-range gap** | **#1 to #225 — ENTIRELY MISSING (~225 statements, ~2002 to Jan 2020)** |
| **Post-range gap** | **#249 onwards — MISSING (Nov 2022 to present)** |
| **Interim CSV coverage** | Oct–Dec 2022 (partial overlap with post-248 period) |

> **Critical finding:** The account has been active for over 20 years, but only ~2 years of formal statements (2020–2022) are available. The uploaded image proves statements existed as far back as 2014 (stmt #144). Approximately 18 years of transaction history is unaccounted for.

#### 55270018789 — Pete Platinum Acct (PF) — Day-to-Day
| Metric | Value |
|--------|-------|
| **Entity** | PF — MR PETER A FAUCITT |
| **Range in system** | #226 to #280 |
| **Statements available** | 34 of 55 |
| **MISSING within range** | **21 statements** |
| **Missing numbers** | #228, #229, #230, #231, #248, #250–#265 |
| **Pre-range gap** | #1 to #225 ENTIRELY MISSING |

> **Note:** Statement #249 is available only in the uploaded ZIPs, not in the repository. The gap from #248 to #266 (18 statements) represents approximately 18 months of missing history.

#### 62323196362 — Regima Worldwide Distribution (RWD) — Platinum Business
| Metric | Value |
|--------|-------|
| **Entity** | RWD — Regima Worldwide Distribution (Pty) Ltd |
| **Range in system** | #109 to #163 |
| **Statements available** | 40 of 55 |
| **MISSING within range** | **15 statements** |
| **Missing numbers** | #131–#140 (10 consecutive), #142–#147 (with gaps), #149 |
| **Date gap** | Sep 2022 (#130) to Jul 2023 (#141) — **10 months missing** |
| **Pre-range gap** | #1 to #108 ENTIRELY MISSING |

> **Critical:** The 10-month gap (Oct 2022 – Jul 2023) coincides with the period when Interim CSVs show activity through Dec 2022. Statements #131–#140 cover approximately Oct 2022 to Aug 2023 — a forensically significant period.

#### 62432501494 — Strategic Logistics CC (SLG) — Platinum Business
| Metric | Value |
|--------|-------|
| **Entity** | SLG — Strategic Logistics CC |
| **Range in system** | #89 to #112 (repo) + #101–#112 (ZIPs) |
| **Statements available** | 48 in repo |
| **Status** | Appears complete within available range |
| **Pre-range gap** | #1 to #88 ENTIRELY MISSING |

#### 62423540807 — Villa Via Arcadia No 2 CC (VVA) — Platinum Business
| Metric | Value |
|--------|-------|
| **Entity** | VVA — Villa Via Arcadia No 2 CC |
| **Range in system** | #92 to #146 |
| **Statements available** | 42 of 55 |
| **MISSING within range** | **13 statements** |
| **Missing numbers** | #116, #118, #119, #121–#126, #128–#131 |
| **Date gaps** | Nov 2022 (#115) to Dec 2022 (#117) — 1 month; Jan 2023 (#117) to Apr 2023 (#120) — 3 months; Apr 2023 (#120) to Oct 2023 (#127) — 6 months |
| **Pre-range gap** | #1 to #91 ENTIRELY MISSING |

---

### TIER 2: Savings & Investment Accounts

#### 62134839127 — RST Money On Call (BS9127)
| Metric | Value |
|--------|-------|
| **Entity** | RST — Regima Skin Treatments CC |
| **Range in system** | #166 to #219 |
| **Statements available** | 37 of 54 |
| **MISSING within range** | **17 statements** |
| **Missing numbers** | #182 (in ZIPs only), #188 (in ZIPs only), #189–#205 (17 consecutive) |
| **Date gap** | Oct 2022 (#187) to Apr 2024 (#206) — **18 months missing** |
| **Pre-range gap** | #1 to #165 ENTIRELY MISSING |

> **Critical:** 18 consecutive months missing (Oct 2022 – Apr 2024). Statements #182 and #188 exist in the uploaded ZIPs but are not in the repository.

#### 62812835744 — VVA Money On Call (BS5744)
| Metric | Value |
|--------|-------|
| **Range in system** | #7 to #25 |
| **Statements available** | 13 of 19 |
| **MISSING** | #15–#20 (6 statements) |
| **Pre-range gap** | #1 to #6 MISSING |

#### 62593375829 — SLG Money On Call (BS5829)
| Metric | Value |
|--------|-------|
| **Range in system** | #21 to #27 |
| **Statements available** | 9 |
| **Status** | Complete within range |
| **Pre-range gap** | #1 to #20 MISSING |

#### 62742245617 — PF Money Maximiser (BS5617)
| Metric | Value |
|--------|-------|
| **Range in system** | #15 only |
| **Status** | Only 1 statement available |
| **ZIPs contain** | #16–#19 (NOT in repo) |
| **Pre-range gap** | #1 to #14 MISSING |

#### 62836164880 — RWD Worldwide Savings
| Metric | Value |
|--------|-------|
| **Range in system** | #5 to #9 |
| **Statements available** | 5 of 5 |
| **Status** | Complete within range |
| **Pre-range gap** | #1 to #4 MISSING |

---

### TIER 3: Foreign Currency (CFC) Accounts

#### 62839603819 — RST EUR (BG3819)
| Metric | Value |
|--------|-------|
| **Range** | #3 to #5 |
| **Available** | 2 of 3 |
| **MISSING** | #4 |

#### 62839603827 — RST GBP (BG3827)
| Metric | Value |
|--------|-------|
| **Range** | #5 to #9 |
| **Available** | 4 of 5 |
| **MISSING** | #7 |

#### 62839603835 — RST USD (BG3835)
| Metric | Value |
|--------|-------|
| **Range** | #5 to #19 |
| **Available** | 13 of 15 |
| **MISSING** | #8, #10 |

#### 62839612323 — SLG EUR (BG2323)
| Metric | Value |
|--------|-------|
| **Range** | #4 to #46 |
| **Available** | 42 of 43 |
| **MISSING** | #5 |

#### 62839612331 — SLG GBP (BG2331)
| Metric | Value |
|--------|-------|
| **Range** | #5 to #9 |
| **Available** | 4 of 5 |
| **MISSING** | #7 |

#### 62839612349 — SLG USD (BG2349)
| Metric | Value |
|--------|-------|
| **Range** | #5 to #8 |
| **Available** | 3 of 4 |
| **MISSING** | #7 |

---

### TIER 4: Other Entity Accounts

#### 62027933606 — JF Fusion Private Wealth (BP3606)
| Metric | Value |
|--------|-------|
| **Entity** | JF — Jacqueline Faucitt |
| **Range** | #135 to #189 |
| **Available** | 28 of 55 |
| **MISSING** | **27 statements** |
| **Missing numbers** | #137–#139, #150–#174 (25 consecutive) |
| **Date gap** | Mar 2022 (#149) to Apr 2024 (#175) — **25 months missing** |

> **Critical:** 25 consecutive months missing from Jacqueline's personal account.

#### 62012990132 — Aymac International CC (AYM) — Platinum Business
| Metric | Value |
|--------|-------|
| **Range** | #225 to #275 |
| **Available** | 32 of 51 |
| **MISSING** | **19 statements** |
| **Missing numbers** | #227–#229 (3), #249–#264 (16 consecutive) |
| **Date gap** | Nov 2022 (#248) to Mar 2024 (#265) — **16 months missing** |

#### 62060760404 — Corpclo 2065 CC (COR) — Platinum Business
| Metric | Value |
|--------|-------|
| **Range** | #217 to #229 |
| **Available** | 13 of 13 |
| **Status** | COMPLETE (within range) |
| **Note** | #218 available in ZIPs but not in repo |

#### 62089474309 — VVA (BD0807) — Platinum Business
| Metric | Value |
|--------|-------|
| **Range** | #65 to #115 |
| **Available** | 14 of 63 |
| **MISSING** | **51 statements** |
| **Note** | Statements #104–#115 are in ZIPs only, not in repo |

---

### TIER 5: Regima SA (RSA) Accounts (Date-based, not numbered)

#### 62896474196 — RSA Current Account
| Metric | Value |
|--------|-------|
| **Range** | Oct 2024 to Nov 2025 |
| **Available** | 41 statements (weekly/bi-weekly) |
| **Gaps** | Some weeks missing within range |

#### 62896473974 — RSA Trust Account
| Metric | Value |
|--------|-------|
| **Range** | Oct 2024 to Oct 2025 |
| **Available** | 29 statements |
| **Gaps** | Some periods missing |

#### 62896474972 — RSA Business Call Account
| Metric | Value |
|--------|-------|
| **Range** | Oct 2024 to Jan 2026 |
| **Available** | 9 statements (quarterly) |

#### 62897307015 — RSA Trust Account 7015
| Metric | Value |
|--------|-------|
| **Range** | Oct 2024 to Aug 2025 |
| **Available** | 9 statements (monthly) |

#### 62897307031 / 62897307073 — RSA Trust Accounts
| Metric | Value |
|--------|-------|
| **Range** | Oct 2024 to Jan 2025 |
| **Available** | 4 statements each |

---

## Summary of Missing Statements

### By Priority

| Priority | Account | Entity | Missing (in range) | Missing (pre-range) | Forensic Significance |
|----------|---------|--------|--------------------:|--------------------:|----------------------|
| **CRITICAL** | 55270035642 | RST | 0 | ~225 | 18+ years of primary operating account |
| **CRITICAL** | 62323196362 | RWD | 15 | ~108 | 10-month gap during key period |
| **CRITICAL** | 62027933606 | JF | 27 | ~134 | 25-month gap in personal account |
| **CRITICAL** | 62134839127 | RST | 17 | ~165 | 18-month gap in savings |
| **HIGH** | 55270018789 | PF | 21 | ~225 | 18-month gap in personal account |
| **HIGH** | 62012990132 | AYM | 19 | ~224 | 16-month gap |
| **HIGH** | 62423540807 | VVA | 13 | ~91 | Multiple gaps |
| **HIGH** | 62089474309 | VVA | 51 | ~64 | Massive gap, ZIPs not in repo |
| **MEDIUM** | 62812835744 | VVA | 6 | ~6 | Savings account gap |
| **MEDIUM** | 62839603819 | RST EUR | 1 | ~2 | CFC gap |
| **MEDIUM** | 62839603827 | RST GBP | 1 | ~4 | CFC gap |
| **MEDIUM** | 62839603835 | RST USD | 2 | ~4 | CFC gap |
| **LOW** | 62839612323 | SLG EUR | 1 | ~3 | CFC gap |
| **LOW** | 62839612331 | SLG GBP | 1 | ~4 | CFC gap |
| **LOW** | 62839612349 | SLG USD | 1 | ~4 | CFC gap |

### Totals

| Metric | Count |
|--------|------:|
| Total accounts analyzed | 38 |
| Accounts with gaps (in range) | 18 |
| Total missing statements (in range) | ~200 |
| Estimated missing pre-range statements | ~1,300+ |
| **Total estimated missing** | **~1,500+** |

---

## Forensically Significant Gaps

### Gap Pattern 1: The Nov 2022 – Mar/Apr 2024 Black Hole

Multiple accounts show a consistent gap from approximately November 2022 to March/April 2024. This pattern appears across:

- **55270035642** (RST): No statements after #248 (Nov 2022)
- **62323196362** (RWD): Gap from #130 (Sep 2022) to #141 (Jul 2023), then to #148 (Feb 2024)
- **62134839127** (RST Money On Call): Gap from #187 (Oct 2022) to #206 (Apr 2024)
- **62027933606** (JF): Gap from #149 (Mar 2022) to #175 (Apr 2024)
- **62012990132** (AYM): Gap from #248 (Nov 2022) to #265 (Mar 2024)
- **55270018789** (PF): Gap from #247 to #266

> **This 16–18 month gap (Nov 2022 – Apr 2024) is consistent across nearly all accounts and represents a period where no bank statements were obtained or preserved.** This coincides with the period described in the revenue stream hijacking timeline.

### Gap Pattern 2: Pre-2020 Historical Void

No account has statements before approximately January 2020, despite the uploaded image proving account 55270035642 was active since at least 2002 (statement #144 in Feb 2014). This represents approximately **18+ years of missing financial history** for the primary operating account.

### Gap Pattern 3: ZIPs Not Synced to Repository

Several statements exist in the uploaded ZIP archives but are NOT in the fincosys repository:

| Account | Statements in ZIPs only |
|---------|------------------------|
| 55270035642 | #247, #248 |
| 55270018789 | #249 |
| 62060760404 | #218 |
| 62134839127 | #182, #188 |
| 62323196362 | #131, #132 |
| 62089474309 | #104–#115 (12 statements) |
| 62027933606 | #158 |

---

## Uploaded Files Not Yet in Repository

### Standalone PDFs
- **55270035642.pdf** / **55270035642pdf.pdf** — Transaction history (Sep 2020), not a formal statement
- **OnlineBankingDownload(68-71).pdf** — Payment confirmations (Dec 2022)
- **Payment_Notification(3-5, BP-Morninghill, Huge-Telecom).pdf** — Payment notifications
- **ADDADORYPMTFORCONTAINERS10.2.2022.pdf** — Adderory payment (Feb 2022)

### DOCX Files
- **ACCOUNTSTOPAYENDOFMONTH.docx** / **ACCOUNTSTOPAYENDOFMONTH-NEWJULY2022.docx** — Accounts payable lists
- **BANKINGDETAILS.docx** — Banking details document
- **BANKERDETAILSAUG2023.docx** — Banker details (Aug 2023)
- **BANKMANDATEFORAYMACINTERNATIONAL.docx** — Aymac bank mandate
- **BANKFORMTOLINKPETERACCOUNTTOPROFILEMAY2019.docx** — Peter account linking form (May 2019)

### Interim Transaction Histories (CSVs)
These cover Oct–Dec 2022 for multiple accounts and partially fill the post-statement gap:

| Account | CSV Period |
|---------|-----------|
| 55270035642 | Oct–Dec 2022 |
| 62323196362 | Oct–Dec 2022 |
| 62423540807 | Oct–Dec 2022 |
| 62432501494 | Oct–Dec 2022 |
| 62134839127 | Oct–Nov 2022 |
| 62812835744 | Oct–Nov 2022 |
| 62593375829 | Oct–Nov 2022 |
| 62742245617 | Oct–Nov 2022 |
| 62836164880 | Oct–Nov 2022 |
| 62839612323 | Nov 2022 |

---

## Recommendations

### Immediate Actions
1. **Sync ZIPs to repository** — 20+ statements exist in uploaded ZIPs but are not in the fincosys repo
2. **Process Interim CSVs** — These fill partial gaps for the Nov 2022+ period
3. **Request FNB statement archives** — The 16–18 month gap (Nov 2022 – Apr 2024) must be filled

### Historical Recovery
4. **Request historical statements from FNB** — Statements #1–#225 for account 55270035642 (and equivalent ranges for other accounts) should be requested from FNB. Banks typically retain records for 5–7 years, so statements from 2019 onwards should be obtainable.
5. **SARS records** — Tax returns may contain financial summaries that can partially reconstruct missing periods.
6. **Sage/Xero accounting records** — The accounting system may have bank feed data that predates the available statements.

### Forensic Priority
7. **Focus on the Nov 2022 – Apr 2024 gap** — This period is forensically critical and coincides with the described revenue diversion timeline. Every effort should be made to obtain these statements.
8. **Cross-reference with Xero** — The xero_import_files.zip contains pre-coded CSVs that may help identify transactions during gap periods.

---

## Appendix: Complete Statement Inventory by Account

### 55270035642 (RST Day-to-Day)
**Available:** 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247*, 248*
(*in ZIPs only)

### 55270018789 (PF Day-to-Day)
**Available:** 226, 227, 232–247, 249*, 266–280
**Missing:** 228–231, 248, 250–265

### 62323196362 (RWD Platinum Business)
**Available:** 109–130, 131*, 132*, 141, 148, 150–163
**Missing:** 133–140, 142–147, 149

### 62027933606 (JF Fusion Private Wealth)
**Available:** 135, 136, 140–149, 158*, 175–189
**Missing:** 137–139, 150–157, 159–174

### 62012990132 (AYM Platinum Business)
**Available:** 225, 226, 230–248, 265–275
**Missing:** 227–229, 249–264

### 62423540807 (VVA Platinum Business)
**Available:** 92–115, 117, 120, 127, 132–146
**Missing:** 116, 118–119, 121–126, 128–131

### 62432501494 (SLG Platinum Business)
**Available:** 89–112 (complete within range)

### 62134839127 (RST Money On Call)
**Available:** 166–181, 182*, 183–187, 188*, 206–219
**Missing:** 189–205

### 62089474309 (VVA BD0807)
**Available:** 65, 66, 104*–115*
**Missing:** 67–103 (37 statements)

### 62060760404 (COR Platinum Business)
**Available:** 217, 218*, 219–229 (complete)
