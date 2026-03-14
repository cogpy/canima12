# Ketoni Evidence Analysis Report
**Date:** 2026-03-14
**Case Number:** 2025-137857
**Source:** ketoni_evidence_archive.zip (624 messages, 154 forensic EMLs, 9 OCR documents)

---

## 1. Executive Summary

The Ketoni evidence archive provides comprehensive documentation of the Faucitt Family Trust's (FFT) R9.8 million investment into Ketoni Investment Holdings (Pty) Ltd, which in turn holds 8.14% (456 shares) of The George Group (Pty) Ltd. The investment creates a structured exit mechanism with call/put options valued between **R18,685,000** (Year 1) and **R28,730,000** (Year 5), with the first option window opening in **May 2026**.

The evidence establishes that **Danie Bantjies** (referred to as "Bantjies" throughout) is the CFO of The George Group, where **Kevin Michael Derrick** is CEO and sole director of Ketoni Investment Holdings. This creates a direct conflict of interest when Bantjies was appointed as Trustee of the FFT in July 2024 -- T-10 months before the first option window.

---

## 2. New Entities Identified

### 2.1 Organizations

| Entity ID | Name | Type | Registration | Key Details |
|-----------|------|------|-------------|-------------|
| ORG_NEW_01 | Ketoni Investment Holdings (Pty) Ltd | Company | 2023/562189/07 | SPV holding 8.14% of George Group; sole director KM Derrick; Standard Bank acct 420469494 |
| ORG_NEW_02 | The George Group (Pty) Ltd | Company | (to verify) | Operating company; 456 shares held by Ketoni; Bantjies is CFO, Derrick is CEO |
| ORG_NEW_03 | Baker McKenzie (SA) | Law Firm | N/A | Acted for Ketoni/FFT on shareholder agreement; Marc Yudaken partner |
| ORG_NEW_04 | Forvis Mazars | Audit Firm | N/A | Prepared and reviewed Ketoni AFS 2024 |
| ORG_NEW_05 | N Xenophontos Trust (Attorneys) | Law Firm | N/A | nixenlaw@xenophontos.co.za; involved in FFT matters from Oct 2024 |

### 2.2 Persons

| Entity ID | Name | Role | Key Details |
|-----------|------|------|-------------|
| PERSON_NEW_01 | Kevin Michael Derrick | Director/CEO | Sole director of Ketoni; CEO of George Group; Kevin Derrick Trust (IT 107716/98) is existing shareholder |
| PERSON_NEW_02 | Marc Yudaken | Attorney | Baker McKenzie partner; handled Ketoni shareholder agreement |
| PERSON_NEW_03 | David Field | Associate | Attended meeting with Pete, Bantjies, and Kevin Derrick (2023-03-15) |
| PERSON_NEW_04 | Denny Da Silva | Associate | Meeting with Pete re Faucitt Trust (2023-05-30) |
| PERSON_NEW_05 | Liezel | Employee | liezel@regima.zone account created 2023-04-24; credentials shared via email |

### 2.3 Trusts

| Entity ID | Name | Trust Number | Key Details |
|-----------|------|-------------|-------------|
| TRUST_NEW_01 | Kevin Derrick Trust | IT 107716/98 | Existing/Ordinary shareholder of Ketoni (100 Ordinary Shares = R1,000); R49,000 loan to Ketoni |

---

## 3. New Relations Identified

| Source | Target | Relation Type | Evidence | Significance |
|--------|--------|--------------|----------|-------------|
| Bantjies | George Group | CFO/Employee | Email domain danieb@thegeorgegroup.co.za; correspondence | Direct employment link |
| Kevin Derrick | Ketoni Investment Holdings | Sole Director | AFS 2024; CIPC registration | Controls the SPV |
| Kevin Derrick Trust | Ketoni Investment Holdings | Ordinary Shareholder (100%) | Subscription Agreement; AFS | Controls voting rights |
| FFT | Ketoni Investment Holdings | A-Ordinary Shareholder (100%) | Subscription Agreement; AFS | Holds R9.8M investment; entitled to put/call option |
| Ketoni Investment Holdings | George Group | 8.14% Shareholder | AFS Note 2; Shareholder Agreement cl.11 | R9.8M invested in 456 shares |
| Bantjies | Kevin Derrick | Colleague/CFO-CEO | George Group employment; meeting coordination | Establishes conflict of interest |
| Rynette Farrar | Bantjies | Operational Coordinator | Extensive email correspondence; prints/scans documents | Rynette acts as intermediary for all trust/company matters |
| Baker McKenzie | Ketoni/FFT | Legal Advisor | Shareholder Agreement preparation | Drafted the investment structure |
| Bantjies | FFT | Trustee (from Jul 2024) | Trust resolution; unlawful appointment by Rynette | Appointed T-10 months before R18.685M option |
| Bantjies | FFT | Accountant (all companies) | Email correspondence; financial instructions | Pre-existing role before trustee appointment |
| Jax (Jacqui) | Bantjies | Document Requestor | Jan 2026 emails demanding Ketoni/George docs | Jax becoming aware of investment details |

---

## 4. New Events / Timeline Items

### 4.1 Pre-Investment Phase

| Date | Event | T-Months | Evidence | Category |
|------|-------|----------|----------|----------|
| 2023-02-20 | Ketoni Investment Holdings incorporated (Reg 2023/562189/07) | T-39 | AFS; CIPC records | Corporate |
| 2023-03-14 | SARS notification forwarded by Pete to Rynette re outstanding tax audit | T-38 | Msg 64 | Tax |
| 2023-03-15 | Bantjies arranges meeting: Pete, Kevin Derrick, David Field (Thu 23 Mar @ 15h00) | T-38 | Msg 64 body | Meeting |
| 2023-04-19 | Baker McKenzie (Marc Yudaken) sends Ketoni Investment Holdings documents to Kayla, Rynette, and via Slack | T-37 | Msgs 65-67; Forensic EML | Legal |
| 2023-04-19 | Dan receives auto-forwarded Ketoni documents (via postmaster@regima.zone) | T-37 | Msgs 68-70 | Information |

### 4.2 Investment Execution Phase

| Date | Event | T-Months | Evidence | Category |
|------|-------|----------|----------|----------|
| 2023-04-24 | FFT subscribes for 5,000 A-Ordinary Shares in Ketoni for R9,800,000 | T-37 | Subscription Agreement; Shareholder Agreement | Investment |
| 2023-04-24 | liezel@regima.zone account created (credentials emailed to Kayla) | T-37 | Msg 71 | IT/Access |
| 2023-04-27 | Bantjies sends amended Trust Minutes to Pete and Jax for signature (from thegeorgegroup.co.za) | T-37 | Msg 79 body chain | Trust |
| 2023-04-28 | Jax reports scanner not working; will wait for Kayla on Tuesday | T-37 | Msg 79 body chain | Admin |
| 2023-05-03 | Bantjies sends Trust Minutes to Rynette for printing/signing "urgently" | T-36 | Msgs 80-81 | Trust |
| 2023-05-03 | Rynette returns signed Trust Minutes to Bantjies | T-36 | Msg 82; Attachment: Signed minutes.pdf | Trust |
| 2023-05-08 | Bantjies emails Rynette, Jax, Pete re Villa Via tax assessment (R495,349.53 owed to SARS) | T-36 | Msg 83 body chain | Tax |
| 2023-05-09 | Rynette asks Bantjies where to post Ketoni Investment total | T-36 | Msg 83 | Accounting |
| 2023-05-09 | **Bantjies instructs: "allocate the Ketoni payment to Pete's shareholder loan account"** | T-36 | Msg 84 | **Accounting Irregularity** |
| 2023-05-29 | Rynette arranges meeting: Pete with Denny Da Silva re Faucitt Trust (30 May @ 1pm) | T-36 | Msg 85 | Meeting |
| 2023-05-29 | Bantjies requests postponement citing "month end at the new company" (George Group) | T-36 | Msg 86 | Meeting |

### 4.3 George Group Correspondence Phase

| Date | Event | T-Months | Evidence | Category |
|------|-------|----------|----------|----------|
| 2023-05-31 | Bantjies (from thegeorgegroup.co.za) corresponds re Ketoni Investment Holdings | T-35 | Forensic EML 0011, 0012 | Corporate |
| 2023-06-02 | Bantjies (from thegeorgegroup.co.za) continues Ketoni correspondence | T-35 | Forensic EML 0014 | Corporate |

### 4.4 Trust Document Phase (2024)

| Date | Event | T-Months | Evidence | Category |
|------|-------|----------|----------|----------|
| 2024-07-xx | Bantjies appointed as Trustee of FFT (by Rynette, unlawfully) | T-10 | Trust resolution; existing evidence | **Conflict of Interest** |
| 2024-08-28 | Rynette forwards "PETER FAUCITT FAMILY TRUST" documents | T-9 | Msgs 160-161 | Trust |
| 2024-09-02 | Rynette forwards more FFT documents | T-9 | Msgs 164-165 | Trust |
| 2024-09-05 | Bantjies and Rynette exchange FFT correspondence | T-9 | Msgs 166-169 | Trust |
| 2024-09-25 | Pete forwards FFT documents | T-8 | Msg 173 | Trust |
| 2024-09-26 | Bantjies (gmail) sends "Re: Documents" to Jax | T-8 | Forensic EML 0015-0020 | Trust |
| 2024-10-15 | Pete sends "PETER FAUCITT FAMILY TRUST" email | T-7 | Msg 189 | Trust |
| 2024-10-16 | Bantjies responds; Jax and Rynette exchange FFT messages | T-7 | Msgs 190-196 | Trust |
| 2024-10-21 | Rynette forwards "Notice of Payment: N Xenophontos Trust - NX/DP/F127 Faucitt Trust" | T-7 | Msgs 197-201 | Legal/Financial |
| 2024-11-08 | Rynette sends "Faucitt Family Trust" email | T-6 | Msgs 205-206 | Trust |
| 2024-11-11 | N Xenophontos Trust (nixenlaw@xenophontos.co.za) responds re FFT | T-6 | Msg 207 | Legal |

### 4.5 Agreement Phase (Jan 2025)

| Date | Event | T-Months | Evidence | Category |
|------|-------|----------|----------|----------|
| 2025-01-29 | Rynette sends "Faucitt family trust - agreement" | T-4 | Msgs 211-212 | Trust |
| 2025-01-29 | Bantjies responds re FFT agreement | T-4 | Msgs 213-214, 217-218; Forensic EML 0023-0024 | Trust |
| 2025-01-29 | Jax forwards FFT agreement correspondence | T-4 | Msgs 215-216, 219-220 | Trust |

### 4.6 Document Discovery Phase (Jan 2026)

| Date | Event | T-Months | Evidence | Category |
|------|-------|----------|----------|----------|
| 2026-01-02 | Bantjies sends "Faucitt Trust document" to Jax | T-4 (before May) | Msg 357 | Trust |
| 2026-01-07 | Jax forwards Faucitt Trust documents to multiple parties | T-4 | Msgs 358-362 | Trust |
| 2026-01-07 | **Jax demands: "KETONI AND GEORGE FULL DOCUMENTS PLEASE SEND TO ME"** | T-4 | Msg 363; Forensic EML 0025 | **Discovery** |
| 2026-01-07 | Bantjies responds to Jax's Ketoni/George document request | T-4 | Msg 364; Forensic EML 0026 | Discovery |
| 2026-01-07 | Jax forwards Ketoni/George request | T-4 | Msg 365 | Discovery |
| 2026-01-13 | Jax follows up on Ketoni/George documents | T-4 | Msg 366 | Discovery |
| 2026-01-15 | Bantjies responds to Ketoni/George document request | T-4 | Msg 370; Forensic EML 0029 | Discovery |
| 2026-01-15 | Jax forwards Ketoni/George correspondence | T-4 | Msgs 372-373 | Discovery |
| 2026-01-16 | Bantjies sends documents; Jax says "not helpful" | T-4 | Msgs 374-384; Forensic EML 0032-0042 | Discovery |
| 2026-01-16 | **Jax requests share certificates: "I have never been given" share certificates** | T-4 | Msg 383 body | **Beneficiary Exclusion** |
| 2026-01-16 | **Jax: "Not to the office for obvious reasons. Send me an address where I can collect"** | T-4 | Msg 383 body | **Secrecy** |
| 2026-01-16 | Bantjies: "Will get our driver to drop it off at 20 River Road" | T-4 | Msg 384 | Discovery |

---

## 5. Critical Findings

### 5.1 Accounting Irregularity: Ketoni Payment Allocation

On 2023-05-09 (Msg 84), Bantjies instructed Rynette:

> "For now, please allocate the Ketoni payment to Pete's shareholder loan account."

This is significant because:
- The R9.8M investment was made **by the FFT** (Trust money), not by Pete personally
- Allocating a Trust investment to Pete's personal shareholder loan account is a **misallocation of Trust assets**
- This effectively treats Trust property as Peter's personal asset
- This instruction came from Bantjies in his capacity as accountant, before his trustee appointment

### 5.2 Conflict of Interest: Bantjies as CFO and Trustee

The evidence establishes:
1. Bantjies uses **danieb@thegeorgegroup.co.za** email for trust/Ketoni business (Msgs 79-82, Forensic EMLs 0011-0014)
2. Bantjies is CFO of George Group, where Kevin Derrick is CEO
3. Kevin Derrick Trust is the controlling shareholder of Ketoni (100 Ordinary Shares = voting control)
4. FFT holds 5,000 A-Ordinary Shares (investment/preference shares, no voting control)
5. Bantjies was appointed Trustee of FFT in July 2024, T-10 months before the R18.685M option window
6. As Trustee, Bantjies would have authority over whether the FFT exercises its put option

**This creates a direct conflict**: Bantjies' employer (George Group) would need to fund the R18.685M+ payout if the FFT exercises its put option. As Trustee, Bantjies has the power to delay or prevent the FFT from exercising this option, directly benefiting his employer.

### 5.3 Option Structure Analysis

From the Shareholder Agreement:

| Option | Year | Price per Share | Total Value | Window |
|--------|------|----------------|-------------|--------|
| Call Option (Yr 1) | May 2026 | R3,737 | R18,685,000 | 3rd anniversary of Effective Date |
| Call Option (Yr 2) | May 2027 | R4,633 | R23,165,000 | 4th anniversary |
| Call Option (Yr 3) | May 2029 | R5,746 | R28,730,000 | 5th anniversary |
| Put Option | May 2028 | R5,746 | R28,730,000 | 5th anniversary |

**Critical**: The Call Option is exercised by the **Company** (Ketoni, controlled by Kevin Derrick Trust). The Put Option is exercised by the **A-Ordinary Shareholder** (FFT). This means:
- Kevin Derrick controls when/whether the Call Option is exercised
- The FFT Trustees control when/whether the Put Option is exercised
- With Bantjies as Trustee, the George Group/Derrick effectively controls BOTH sides

### 5.4 Jax's Discovery of Exclusion (Jan 2026)

The January 2026 correspondence reveals:
1. Jax had **never been given share certificates** (Msg 383)
2. Jax demanded documents be sent **"not to the office for obvious reasons"** -- indicating awareness of surveillance/control
3. Bantjies was evasive, initially suggesting office pickup
4. Jax had to escalate repeatedly over 9 days (Jan 7-16) to obtain documents

### 5.5 Financial Structure Summary

| Item | Amount | Notes |
|------|--------|-------|
| FFT Subscription Price | R9,800,000 | 5,000 A-Ordinary Shares |
| Kevin Derrick Trust Subscription | R1,000 | 100 Ordinary Shares (voting control) |
| Ketoni Investment in George Group | R9,800,000 | 8.14% (456 shares) |
| Kevin Derrick Trust Loan to Ketoni | R49,000 | Unsecured, interest-free, on demand |
| Ketoni Operating Expenses (FY2024) | R1,273 | Minimal -- SPV with no operations |
| Year 1 Call Option Value | R18,685,000 | 90.7% return on R9.8M investment |
| Year 5 Put Option Value | R28,730,000 | 193.2% return on R9.8M investment |

### 5.6 Rynette's Central Role

The correspondence demonstrates Rynette Farrar's role as the operational nexus:
- Receives and forwards all Ketoni/FFT documents
- Prints, scans, and returns signed documents
- Acts as intermediary between Bantjies, Pete, and Jax
- Manages Pete's diary and meeting scheduling
- Controls information flow (documents go through her)

---

## 6. Evidence Index (New Items)

| Code | Description | Date | Source | Format |
|------|-------------|------|--------|--------|
| KET-01 | Ketoni Shareholder Agreement (signed) | 2023-04-24 | OCR | PDF/Text |
| KET-02 | Ketoni Subscription Agreement (signed) | 2023-04-24 | OCR | PDF/Text |
| KET-03 | Ketoni AFS 2024 (Forvis Mazars) | 2025-01-24 | OCR | PDF/Text |
| KET-04 | Signed Trust Minutes (Ketoni investment) | 2023-05-03 | Msg 82 attachment | PDF |
| KET-05 | Baker McKenzie correspondence (Yudaken) | 2023-04-19 | Msgs 65-70; EMLs | EML/PDF |
| KET-06 | Bantjies accounting instruction (Pete's loan acct) | 2023-05-09 | Msg 84 | EML |
| KET-07 | George Group correspondence (Bantjies) | 2023-05-31 to 2023-06-02 | EMLs 0011-0014 | EML |
| KET-08 | Jax Ketoni/George document demand | 2026-01-07 to 2026-01-16 | Msgs 363-384; EMLs 0025-0042 | EML |
| KET-09 | FFT Trust Deed | Various | OCR | PDF/Text |
| KET-10 | Peter Faucitt Family Trust (F172) | Various | OCR | PDF/Text |
| KET-11 | Sworn Affidavit of Trusteeship (Bantjies) | Various | OCR | PDF/Text |
| KET-12 | Danie missing pages | 2025-01-29 | OCR | PDF/Text |
| KET-13 | N Xenophontos Trust payment notice | 2024-10-21 | Msgs 197-201 | EML |
| KET-14 | FFT agreement correspondence | 2025-01-29 | Msgs 211-220; EMLs 0023-0024 | EML |

---

## 7. Implications for Applications

### 7.1 Civil/Criminal Actions
- **Breach of Fiduciary Duty**: Bantjies' dual role (George Group CFO + FFT Trustee) constitutes a direct conflict of interest
- **Misallocation of Trust Assets**: Instruction to allocate R9.8M Trust investment to Pete's personal loan account
- **Fraud**: Systematic exclusion of beneficiaries from investment information

### 7.2 CIPC Companies Act Complaints
- **s76 Director Duties**: Bantjies' conflict of interest as Trustee controlling FFT's Ketoni investment while employed by the counterparty
- **s75 Personal Financial Interest**: Bantjies has a personal financial interest (employment) in the outcome of the Ketoni option exercise
- **s162 Delinquency**: Pattern of self-dealing and beneficiary exclusion

### 7.3 POPIA Criminal Complaints
- **Information Asymmetry**: Jax was denied share certificates and investment documents
- **Unauthorized Processing**: Trust financial information processed through personal channels

### 7.4 Commercial Crime / Tax Fraud
- **Misallocation**: R9.8M Trust investment allocated to personal loan account
- **Tax Implications**: If treated as personal loan, different tax treatment applies
- **Transfer Pricing**: George Group structure may facilitate profit extraction

---

## 8. Recommended Next Steps

1. **Update entities.json** with new Ketoni-specific entities (ORG_NEW_01-05, PERSON_NEW_01-05, TRUST_NEW_01)
2. **Update relations.json** with 11 new relations
3. **Update events.json** with 30+ new events
4. **Update timeline.json** with chronological Ketoni events
5. **Create dedicated Ketoni evidence page** for GitHub Pages
6. **Update all filings** (CIPC, POPIA, Commercial Crime, NPA) with Ketoni-specific evidence
7. **Sync to both repositories** (revstream1 and ad-res-j7)
