# Forensic Audit Program & Extraction Plan
**Date:** March 28, 2026
**Prepared by:** Manus AI
**Framework:** fin-audit-za-v2 (SOX 404 / ICFR / SA Regulatory)
**Scope:** 96,472 Discovered Financial Documents

## 1. Executive Summary & Risk Assessment

An analysis of the 96,472 financial documents discovered in the Exchange/Gmail archives reveals severe anomalies that corroborate the findings from the Strategic Logistics (SLG) workpaper. The data demonstrates a systematic breakdown of internal controls, particularly during the 2025 "fraud period," characterized by a collapse in standard procurement channels and the emergence of parallel, unauthorized entities.

**Key Risk Indicators:**
1. **Purchase Order Collapse:** PO volume dropped from 385 in 2020 to just 7 in 2025. This indicates that procurement moved entirely off-book or to unmonitored channels, bypassing all authorization controls.
2. **Parallel Entity Operations:** The entity `regimaskin.co.za` (flagged as fraudulent) is actively issuing purchase orders and preparing trial balances for SLG.
3. **Credit Note Spike:** An anomalous spike of 718 credit notes occurred in 2022 (468 from The Courier Guy), suggesting massive product returns, dispatch failures, or revenue reversal manipulation.
4. **Bank Statement Gaps:** Critical FNB cheque accounts for RegimA Worldwide Distribution (RWW) and Villa Via have multi-month gaps, specifically during the 2023-2024 period, obstructing fund flow tracing.

## 2. SOX 404 Deficiency Classifications

Based on the metadata analysis, the following control deficiencies are classified:

| Process Area | Finding | Classification | Rationale |
|---|---|---|---|
| **Procurement (Expenditure)** | Complete cessation of formal Purchase Orders in 2025 while manufacturing continued. | **Material Weakness** | Complete bypass of authorization controls. High likelihood of unauthorized or fraudulent expenditure. |
| **Revenue / Returns** | Unexplained spike of 718 credit notes in 2022, primarily courier returns. | **Significant Deficiency** | Indicates failure in dispatch controls or potential manipulation of recognized revenue. |
| **Entity Segregation** | `regimaskin.co.za` (unauthorized entity) issuing POs and preparing TBs for SLG. | **Material Weakness** | Total failure of entity segregation and IT access controls. Parallel entity has infiltrated the financial reporting process. |
| **Record Keeping** | 20 missing months of FNB statements for RWW; 12 missing months for Villa Via. | **Deficiency** | Impedes timely reconciliation and forensic fund flow tracing. |

## 3. Prioritized Evidence Extraction Plan

To close the evidence gaps and build a court-ready forensic file, the following extraction plan must be executed via the `financial-doc-sync` pipeline.

### PRIORITY 1: CRITICAL (Execute Immediately)
**Objective:** Secure evidence of parallel entity operations and unauthorized procurement.
- **Target 1:** All Purchase Orders from 2025 and 2026 (11 documents).
  - *Rationale:* These are the only formal POs during the fraud period. Must identify who authorized them and to which suppliers.
- **Target 2:** All documents where sender is `regimaskin.co.za` (252 Invoices, 1 PO).
  - *Rationale:* Direct evidence of the parallel entity operating within the group's financial ecosystem.
- **Target 3:** Rynette's "Gatekeeping" emails (e.g., "Do not email information meant for Strategic to Karen").
  - *Rationale:* Establishes intent to conceal information and bypass standard communication channels.

### PRIORITY 2: HIGH (Execute Batch 1)
**Objective:** Reconstruct the intercompany loan balloon and revenue hijacking.
- **Target 1:** Intercompany Invoices (SLG, Villa Via, RWW, DERM) from 2021-2025.
  - *Rationale:* To trace the origin of the R41.7M intercompany debt identified in the SLG TB.
- **Target 2:** All Raw Material records (864 documents).
  - *Rationale:* To reconcile the negative R2.76M finished goods balance in SLG by proving what was actually purchased vs. what was recorded.

### PRIORITY 3: MEDIUM (Execute Batch 2)
**Objective:** Investigate the 2022 revenue/return anomaly.
- **Target 1:** The 718 Credit Notes from 2022.
  - *Rationale:* Determine if these were legitimate courier returns or fictitious credits used to reverse revenue or extract funds.
- **Target 2:** Customs/Trade documents (93 documents).
  - *Rationale:* Verify international shipments, especially given the UK pension redirection allegations.

## 4. Audit Program: Next Steps

1. **Execute Priority 1 Extraction:** Run the GitHub Actions workflow for the 2025/2026 POs and all `regimaskin.co.za` documents.
2. **Bank Statement Subpoena:** The missing FNB statements for RWW (20 months) and Villa Via (12 months) cannot be recovered from the mail archive. A formal request or subpoena must be issued directly to FNB to reconstruct the fund flow.
3. **Supplier Verification:** Cross-reference the suppliers on the 2025 POs against the approved vendor list to identify potential shell companies.
4. **Legal Preparation:** Compile the extracted `regimaskin.co.za` documents into an affidavit annexure to support the "fraudulent website" and "void ab initio" legal claims.
