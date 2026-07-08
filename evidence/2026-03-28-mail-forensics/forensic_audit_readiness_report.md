# Forensic Audit Readiness Assessment: RegimA Mail Data Ecosystem

**Date:** March 28, 2026  
**Framework:** SOX 404 / ICFR & South African Regulatory Standards (fin-audit-za-v2)  
**Target Scope:** `regima.zone` (MS Exchange) and `regima.com` (Google Workspace) mail archives in the `b2bkp-exchange-sync` Neon database.

---

## 1. Engagement Scope & Control Objective

This assessment evaluates the completeness, accuracy, and readiness of the RegimA mail synchronization pipeline to serve as a reliable source of digital forensic evidence. 

In the context of South African law (specifically the **Electronic Communications and Transactions Act 25 of 2002, s.15** and the **ACFE SA Digital Forensic Standards**), electronic records must demonstrate integrity to be admissible in court or disciplinary tribunals. Furthermore, under the **Auditing Profession Act 26 of 2005 (APA s.45)**, auditors require timely access to complete records to investigate and report suspected Reportable Irregularities (RIs), such as revenue stream hijacking or unauthorized director extractions.

**Control Objective:** Ensure that the automated mail synchronization pipeline completely and accurately captures all historical email communications, including body content and attachments, to support forensic extraction and e-discovery.

---

## 2. Test Execution & Findings

The audit tested the operating effectiveness of the mail sync pipeline by querying the primary `b2bkp-exchange-sync` database.

### 2.1 MS Exchange (`regima.zone`)
- **Population:** 1,059,437 messages across 149 users (Dec 2014 – Mar 2026).
- **Body Content Coverage:** 891,270 messages (84.1%) have full body content extracted.
- **R2 Search Sync:** 1,053,726 messages (99.5%) successfully synced to Cloudflare R2.
- **Attachment Sync:** Out of 35,927 tracked attachments, 27,942 (77.8%) are successfully downloaded, with 7,808 (21.7%) pending.

### 2.2 Google Workspace / Gmail (`regima.com`)
- **Population:** 1,518,990 messages across 28 users (up to Jul 2025).
- **Body Content Coverage:** 1,364,983 messages (89.9%) have plain text bodies extracted.
- **R2 Search Sync:** 1,094,224 messages (72.0%) successfully synced to Cloudflare R2.
- **Attachment Sync:** Out of 228,488 tracked attachments, only 85,126 (37.3%) are successfully downloaded. A massive backlog of **143,337 attachments (62.7%, ~35 GB)** remains in a "pending" state.

---

## 3. Deficiency Evaluation & Classification

Based on the SOX 404 deficiency evaluation framework, the following control exceptions have been identified and classified based on their potential to impede a forensic investigation or material misstatement detection:

### Exception 1: Gmail Attachment Sync Backlog
- **Description:** Over 143,000 attachments from the `regima.com` domain have not been downloaded to secure storage.
- **Impact:** Attachments often contain critical financial evidence (e.g., bank statements, invoices, contracts). The inability to access these documents in a timely manner severely restricts the auditor's ability to trace fund flows, verify intercompany eliminations (Membrane B2.ee/B2.ae), or investigate potential POCA/FICA violations.
- **Classification:** **Significant Deficiency**. While it does not immediately guarantee a material misstatement, it represents a significant gap in the forensic evidence infrastructure that merits immediate management attention.

### Exception 2: Exchange Body Content Gap
- **Description:** Approximately 15.9% of Exchange messages lack full body content in the database.
- **Impact:** Incomplete body content limits the effectiveness of the AI Search pipeline and keyword-based e-discovery, potentially causing investigators to miss context surrounding key transactions.
- **Classification:** **Deficiency**. The metadata (headers/previews) is 99.3% complete, mitigating the risk of entirely missing a communication thread, but the body extraction process requires remediation.

---

## 4. Recommendations & Remediation Plan

To ensure the mail ecosystem meets the evidentiary standards required for South African courts and regulatory reporting, the following remediation steps are required:

1. **Resume Gmail Attachment Sync:** Immediately restart the `gmail_sync` attachment download pipeline to clear the 143,337 pending files. This is critical for securing historical financial documents.
2. **Execute Exchange Body Backfill:** Run the `rzo-exchange-sync` body backfill process (`--step body`) to retrieve the missing 15.9% of Exchange message bodies via the MS Graph API.
3. **Forensic Extraction Protocol:** When extracting specific emails for legal annexures or RI reporting, investigators must use the `evidence-process` skill to generate RFC 5322 `.eml` files with `.forensic.json` sidecars. This ensures cryptographic hashes (SHA-256) and authentication results (SPF/DKIM/DMARC) are preserved, satisfying the integrity requirements of ECT Act s.15.
4. **Cross-Domain Reconciliation:** Maintain awareness that cross-domain communications (between `.com` and `.zone`) exist. Forensic searches must span both schemas to ensure complete communication chains are captured.

---
*Prepared by: Manus AI (Forensic Audit Module)*
