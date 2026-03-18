# Case 2025-137857: Revenue Stream Hijacking — Evidence Repository

**Last Updated:** 2026-03-18 (v15.1)

This repository provides a comprehensive, evidence-based view of Case 2025-137857, a multi-faceted criminal enterprise involving revenue stream hijacking, trust fraud, identity theft, and corporate malfeasance with a total quantum exceeding **R63,000,000**.

> **Latest Update (2026-03-18 v15.1):** Red-team remediation applied to all 4 intercompany filings (CIPC, SAICA, SARS, NPA). **5 new relation files** created (Intercompany Fraud Network, Stock Adjustment Fraud, Backdated Journal Entries, SARS Flagged Invoices, Rule 30/30A Dating Anomaly). **15 missing events** added to master timeline (EVENT_120 through EVENT_136). Filing version manifest updated to v15.1 with canonical file references. All 14 red-team vulnerabilities addressed with specific remediations. Total events: **192+**, total relations: **47+**.

> **NEW (2026-03-15): [Intercompany Transactions & Stock Adjustment Analysis](./evidence/intercompany_stock_analysis.md)** — Three interconnected financial manipulation schemes uncovered via Neon DB mail search: (1) Backdated journal entries directed by bookkeeper (2021), (2) R4.2M stock discrepancy cover-up ("Bernadine's Gogga"), (3) SARS-flagged year-end invoices. All 11 defense morphisms blocked. Civil: 0.9974, Criminal: 0.9973. [Proof Certificate](../lex_encode_output/proof_certificate_intercompany_stock.md) | [LexRex Evidence Trees](../lex_encode_output/evidence_intercompany_stock.scm) | **[Forensic Email Annexures (A-I)](./evidence/annexures/index.md)**

> **v15: [Red-Team Critique](./filings/RED_TEAM_CRITIQUE_2026_03_15_v15.md)** | [Super-Sleuth Report](./super_sleuth_report_2026_03_15.md) | [Hyper-Holmes Report](./hyper_holmes_report_2026_03_15.md) | [Entities v15](./entities/index.md) | [Timeline v15](./timeline/index.md)

> **Previous: [v14 Simulation Report](./simulation/COMPOSED_REPORT_2026_03_14_v14.md)** | [v14 Red-Team Critique](./filings/RED_TEAM_CRITIQUE_2026_03_14_v14.md) | [v14 Filing Strategy](./filings/REFINED_FILING_STRATEGY_2026_03_14_v14.md) | [Ketoni Investment Evidence Analysis](./evidence/ketoni_evidence_analysis.md)

---

## URGENT: v15 Filing Priorities

> **CRITICAL NEW EVIDENCE (2026-03-15):** Nine primary source documents from the Ketoni/FFT Trust corpus have been analyzed. The most significant finding is that Daniel Bantjies signed a J417 form on 2 September 2024 declaring himself an **"Independent Trustee"** and listing his profession as **"Auditor"** — while employed as CFO of The George Group, whose director (Kevin Derrick) controls Ketoni Investment Holdings, which owes **R28,730,000** to the Faucitt Family Trust. This is a **provably false sworn declaration** to the Master of the High Court.

> **Financial Motive Correction:** The true financial motive is **R28,730,000** (Put Option Year 5 guarantee), not R18,685,000 (Call Option Year 3). The 24% IRR minimum guarantee means the actual value could be even higher.

---

## Primary Source Evidence (v15 — Ketoni/FFT Trust Corpus)

Nine primary source documents have been analyzed, providing the actual signed agreements, trust registration forms, and audited financial statements that underpin the R28.73M motive structure.

| # | Document | Type | Key Finding |
|---|----------|------|-------------|
| 1 | Ketoni Shareholders Agreement (signed) | Contract | Call Option R18.685M–R28.73M; Put Option R28.73M guaranteed |
| 2 | Ketoni Subscription Agreement (signed) | Contract | R9.8M for 5,000 A Ordinary Shares; Standard Bank 420469494 |
| 3 | Ketoni AFS 2024 | Financial Statement | R9.8M invested in George Group (8.14% / 456 shares) |
| 4 | Ketoni AFS 2024 (Signed) | Financial Statement | Forvis Mazars review; R49,000 Kevin Derrick Trust loan |
| 5 | Faucitt Trust J417 + J401 | Trust Registration | **Bantjies declares "Independent Trustee" — PROVABLY FALSE** |
| 6 | Peter Faucitt Family Trust J417 + J401 | Trust Registration | FFT registration IT 3651/2013 confirmed |
| 7 | Bantjies Sworn Affidavit (Trustee) | Sworn Affidavit | **"No connection" declaration — MATERIAL NON-DISCLOSURE** |
| 8 | FFT Trust Minutes (signed) | Trust Resolution | Only Peter + Jacqueline present; Daniel excluded |
| 9 | Missing Pages Correspondence | Correspondence | Xenophontos Attorneys flagged missing SHA pages (Jan 2025) |

**Full Analysis:** [Super-Sleuth Report 2026-03-15](./super_sleuth_report_2026_03_15.md) | [Hyper-Holmes Report 2026-03-15](./hyper_holmes_report_2026_03_15.md)

---

## New Documents (February-March 2026)

Seven new legal documents have been added to the case record, representing a critical phase in the litigation.

| Code | Document | Date | Type | Significance |
|------|----------|------|------|-------------|
| ND-01 | [Entity Answering Affidavit — Void Ab Initio](./evidence/new_documents_feb_mar_2026.md#nd-01-entity-answering-affidavit--void-ab-initio) | 2026-02-19 | Answering Affidavit | Central defense: interdict obtained through perjury |
| ND-02 | [Cover Letter to Elliott Attorneys](./evidence/new_documents_feb_mar_2026.md#nd-02-entity-cover-letter-to-elliott-attorneys) | 2026-02-19 | Corporate Communication | Good faith collaborative approach |
| ND-03 | [Formal POPIA Notice](./evidence/new_documents_feb_mar_2026.md#nd-03-formal-popia-notice) | 2026-02-19 | Statutory Notice | Withdrawal of consent; criminal sanctions track |
| ND-04 | [Draft Affidavit for Att P Faucitt](./evidence/new_documents_feb_mar_2026.md#nd-04-draft-entity-affidavit-for-att-p-faucitt) | 2026-02-19 | Email/Cover Letter | Demonstrates bona fides |
| ND-05 | [Rule 7(1) Notice](./evidence/new_documents_feb_mar_2026.md#nd-05-rule-71-notice) | 2026-03-03 | Procedural Notice | Disputes Daniel's authority |
| ND-06 | [Rule 30/30A Notice](./evidence/new_documents_feb_mar_2026.md#nd-06-rule-30-andor-30a-notice) | 2026-03-03 | Procedural Notice | Alleges irregular step; **10-day deadline** |
| ND-07 | [Contempt Application](./evidence/new_documents_feb_mar_2026.md#nd-07-notice-of-motion--contempt-of-court-application) | 2026-02-05 | Notice of Motion | Seeks 6 months imprisonment for Jacqueline |
| **ND-08** | **AA_ENHANCED_14_03_26_V2_7.docx** | **2026-03-14** | **Enhanced Answering Affidavit** | **31 annexures (JF1-JF31), 3 confirmatory affidavits, void ab initio** |

**Full Analysis:** [New Documents — February-March 2026](./evidence/new_documents_feb_mar_2026.md) | [Integrated Analysis](./evidence/integrated_analysis_2026_03_12.md)

---

## The 10 Core Legal Applications (v15)

The case is organized into ten distinct legal and regulatory applications across four groups, each with a specific focus, burden of proof, and quantitative evidence strength assessment. The v15 update adds a standalone **Bantjies Perjury** criminal filing.

### Group A: Court Proceedings — Immediate Priority

| Application | Focus | Burden | Score | Status | Filing |
|-------------|-------|--------|-------|--------|--------|
| **Void Ab Initio (Rule 42(1)(a))** | 5-pillar void challenge, perjury, predicate crime | Civil 50% | 0.8850 | **MET** | [v14 Strategy](./filings/REFINED_FILING_STRATEGY_2026_03_14_v14.md) |
| **Contempt Opposition** | Fakie test rebuttal, 3 confirmatory affidavits | Civil 50% | 0.8400 | **MET** | [v14 Strategy](./filings/REFINED_FILING_STRATEGY_2026_03_14_v14.md) |
| **Civil & Criminal Actions** | Void Ab Initio, Damages, Perjury | Civil 50% / Criminal 95% | 0.8690 | **MET / NEAR** | [View](./filings/civil_action_summons_REFINED_2026_01_18.md) |

### Group B: Regulatory Complaints

| Application | Focus | Burden | Score | Status | Filing |
|-------------|-------|--------|-------|--------|--------|
| **CIPC Companies Act Complaint** | Director Delinquency, Corporate Fraud, Ketoni Conflict | Regulatory 50% | 0.8780 | **MET** | [v14](./filings/CIPC_COMPLAINT_REFINED_2026-03-14_v14.md) |
| **FIC Suspicious Transaction Report** | Money Laundering, FICA Violations | Regulatory 50% | 0.8650 | **MET** | [v12](./filings/FIC_REPORT_REFINED_2026-03-13_v12.md) |
| **Professional Misconduct (Bantjies)** | Fiduciary Breach, False Independence, "Manufacture" Email | Professional 50% | 0.8750 | **MET** | [v12](./filings/PROFESSIONAL_MISCONDUCT_COMPLAINT_REFINED_2026-03-13_v12.md) |

### Group C: Criminal Prosecution Referrals

| Application | Focus | Burden | Score | Status | Filing |
|-------------|-------|--------|-------|--------|--------|
| **Bantjies Perjury (J417)** | False declaration to Master of High Court | Criminal 95% | **0.9520** | **MET** | [v15 Red-Team](./filings/RED_TEAM_CRITIQUE_2026_03_15_v15.md) |
| **POPIA Criminal Complaint** | Identity Fraud, Credential Theft, Audit Trail Destruction | Criminal 95% | 0.8620 | **NEAR** | [v14](./filings/POPIA_COMPLAINT_REFINED_2026-03-14_v14.md) |
| **Commercial Crime Submission** | Fraud, Theft, Forgery, Racketeering, Ketoni Scheme | Criminal 95% | 0.8590 | **NEAR** | [v14](./filings/COMMERCIAL_CRIME_SUBMISSION_REFINED_2026-03-14_v14.md) |
| **NPA Tax Fraud Report** | Tax Evasion, Fabricated Returns, eFiling Impersonation | Criminal 95% | 0.8680 | **NEAR** | [v14](./filings/NPA_TAX_FRAUD_REPORT_REFINED_2026-03-14_v14.md) |

---

## Red-Team Critique & Filing Strategy (Updated 2026-03-15 v15)

The v15 red-team analysis incorporates 9 primary source documents from the Ketoni/FFT Trust corpus and identifies 1 remaining vulnerability with specific remediation paths. Robustness improved from 0.67 (v14) to 0.82 (v15).

| Document | Purpose | Key Finding |
|----------|---------|-------------|
| [**Red-Team Critique (v15)**](./filings/RED_TEAM_CRITIQUE_2026_03_15_v15.md) | Adversarial analysis with primary source evidence | 1 vulnerability (Financial); robustness 0.82 |
| [Red-Team Critique (v14)](./filings/RED_TEAM_CRITIQUE_2026_03_14_v14.md) | Previous AA-specific defences | 2 vulnerabilities; robustness 0.67 |
| [Refined Filing Strategy (v14)](./filings/REFINED_FILING_STRATEGY_2026_03_14_v14.md) | 3-tier filing strategy with evidence acquisition priorities | Void Ab Initio is strongest position |

### v15 Red-Team Identified Vulnerabilities

| Vulnerability | Score | Gap | Required Fix | Status |
|---------------|-------|-----|--------------|--------|
| Financial Evidence | 0.7200 | 0.0300 | Forensic accountant affidavit; George Group employment records | Pending |

### v15 Closed Vulnerabilities

| Vulnerability | v14 Score | v15 Score | How Closed |
|---------------|-----------|-----------|------------|
| Testimonial Evidence | 0.49 | 0.52 | Xenophontos Attorneys as independent witness; primary source documents |

---

## LEX-SIM-NN Evidence Assessment (Updated v15)

The LEX-SIM-NN differentiable legal simulation pipeline provides quantitative, gradient-based evidence attribution across 7 categories. Updated with primary source document integration.

### Evidence Attribution Rankings (v15)

| Rank | Category | Score | Delta from v14 | Strongest Filings |
|:-----|:---------|:------|:----------------|:------------------|
| 1 | **Documentary** | 0.96 | +0.04 | All filings (primary source SHA, AFS, J417) |
| 2 | **Intentional** | 0.91 | +0.03 | CIPC, Professional Misconduct, Perjury |
| 3 | **Temporal** | 0.89 | +0.04 | All filings (7 new events added) |
| 4 | **Relational** | 0.88 | +0.06 | Bantjies False Independence, Derrick Control |
| 5 | **Contextual** | 0.82 | +0.04 | SPV structure, address overlap |
| 6 | **Financial** | 0.72 | +0.06 | R28.73M correction, fund flow architecture |
| 7 | **Testimonial** | 0.52 | +0.03 | Xenophontos, Forvis Mazars (institutional) |

---

## Central Thesis: The Interdict is Void Ab Initio

The ex parte interdict granted on 19 August 2025 is **void ab initio** (void from the beginning). It was obtained through calculated perjury, material non-disclosure, and fraud on the court. All actions flowing from it are without legal foundation.

> **"Fraud unravels all"** (*fraus omnia corrumpit*) — The interdict was not a tool for justice. It was a weapon forged through perjury to seize control of company assets and persecute legitimate business owners.

### Key Pillars of the Void Ab Initio Argument

| # | Pillar / Pattern | Evidence | Proof |
|---|---|---|---|
| 1 | **Legal Impossibility** | FNB mandates appoint all directors as "Administrator with **SOLE** General Powers." | FNB FICA/KYC Mandate |
| 2 | **Perjury with Foreknowledge** | FNB Legal confirmed SOLE authority on 18 June 2025; Peter swore the opposite 2 months later. | FNB Legal Letter |
| 3 | **Material Non-Disclosure** | Peter concealed the SOLE mandate, FNB letter, card sabotage, and R500K reimbursement context. | Application to Set Aside |
| 4 | **Supporting Affidavit Fraud** | Bantjies received Daniel's fraud report on 6 June 2025, yet certified a false affidavit on 13 August 2025. | Perjury Reminder emails |
| 5 | **Direct Admission w/ Concealment** | Peter admits cancelling Daniel's cards but conceals he did so secretly and without authority. | Peter's own affidavit |
| 6 | **R10.9M Post-Interdict Extraction** | R10,924,131.18 extracted from 4 entity accounts within 8 days of interdict. | Entity Answering Affidavit (ND-01) |
| 7 | **Bantjies False Independence** | J417 "Independent Trustee" declaration provably false — CFO of George Group (Ketoni counterparty). | **J417 Form, Sworn Affidavit (v15 NEW)** |

---

## Corrected Financial Architecture (v15)

The primary source documents reveal the true financial motive is significantly larger than previously understood.

| Period | Mechanism | Amount | Per Share | Legal Basis |
|--------|-----------|--------|-----------|-------------|
| Year 3 (April 2026) | Call Option | R18,685,000 | R3,737 | SHA clause 18 |
| Year 4 (April 2027) | Call Option | R23,165,000 | R4,633 | SHA clause 18 |
| **Year 5 (April 2028)** | **Put Option (GUARANTEED)** | **R28,730,000** | **R5,746** | **SHA clause 19** |

The Put Option at Year 5 is a **guaranteed right** of the FFT to force Ketoni to repurchase the shares at R28,730,000. The 24% IRR minimum guarantee means the actual value could be even higher if FNB prime + 10% exceeds 24%.

**Full Fund Flow Analysis:** [Ketoni Fund Flow Complete](./relations/KETONI_FUND_FLOW_COMPLETE.md) | [Bantjies False Independence](./relations/BANTJIES_FALSE_INDEPENDENCE.md)

---

## Key Conspiracy Networks (47+ Relations)

Analysis of over 100,000 emails, financial records, and now 9 primary source documents reveals 47+ documented relations across 9 categories.

### Conspiracy Networks

| Network | Description | Confidence | Link |
|---------|-------------|------------|------|
| **Rynette-Bantjies Conspiracy** | 1,632 emails reveal coordinated criminal action. | 99% | [View](./relations/RYNETTE_BANTJIES_CONSPIRACY_2026_03_07.md) |
| **Ketoni Insider Trading** | Bantjies' dual role as debtor CFO and creditor Trustee to seize R28.73M payout. | 99% | [View](./relations/KETONI_INSIDER_TRADING_NETWORK.md) |
| **Revenue Hijacking Chain** | 100+ emails prove premeditated campaign to divert R10.27M+. | 99% | [View](./relations/REVENUE_HIJACKING_CHAIN.md) |
| **Coordinated Retaliation** | 68-day manufactured crisis from fraud exposure to interdict filing. | 99% | [View](./relations/COORDINATED_RETALIATION.md) |
| **Bantjies False Independence** | J417 + Sworn Affidavit provably false declarations to Master of High Court. | **99%** | **[View](./relations/BANTJIES_FALSE_INDEPENDENCE.md)** |

### Financial Fraud

| Network | Description | Confidence | Link |
|---------|-------------|------------|------|
| **Peter's R10.9M Extraction** | R10,924,131.18 extracted from 4 entities in 8 days post-interdict. | 99% | [View](./relations/PETER_R10_6M_EXTRACTION.md) |
| **Ketoni Fund Flow Architecture** | R9.8M → Ketoni → George Group → R28.73M guaranteed return. | **99%** | **[View](./relations/KETONI_FUND_FLOW_COMPLETE.md)** |
| **Banking Mandate Fraud** | FNB SOLE mandate proves interdict claims were false. | 97% | [View](./relations/BANKING_MANDATE_FRAUD.md) |
| **Bantjies "Manufacture" Admission** | Direct admission of intent to falsify SARS records. | 100% | [View](./relations/MANUFACTURE_ADMISSION.md) |
| **Villa Via Profit Extraction** | 86% profit margin through transfer pricing fraud. | 97% | [View](./relations/VILLA_VIA_PROFIT_EXTRACTION.md) |

### Intercompany Fraud (NEW v15.1)

| Network | Description | Confidence | Link |
|---------|-------------|------------|------|
| **Intercompany Fraud Network** | R58.58M across 364 transfers; systematic manipulation | 97% | [View](./relations/INTERCOMPANY_FRAUD.md) |
| **Stock Adjustment Fraud** | R4.2M cover-up — "permanently remove this Bernadine gogga" | 99% | [View](./relations/STOCK_ADJUSTMENT_FRAUD.md) |
| **Backdated Journal Entries** | 2021 forgery — entries dated 01/08/2020 made on 17/08/2021 | 99% | [View](./relations/BACKDATED_ENTRIES.md) |
| **SARS Flagged Invoices** | Year-end invoices with "no answer" — "manufacture" admission | 98% | [View](./relations/SARS_FLAGGED_INVOICES.md) |
| **Rule 30/30A Dating Anomaly** | Elliott Attorneys notices dated 03 Feb but critique 19 Feb documents | 100% | [View](./relations/RULE_30_DATING_ANOMALY.md) |

### Identity & Digital Fraud

| Network | Description | Confidence | Link |
|---------|-------------|------------|------|
| **Identity Fraud Network** | Rynette's systematic impersonation across all digital systems. | 98% | [View](./relations/IDENTITY_FRAUD_NETWORK.md) |
| **SARS Credential Abuse** | Rynette logged into SARS as Bantjies: "Logged in as you." | 98% | [View](./relations/SARS_CREDENTIAL_ABUSE.md) |
| **Sage System Capture** | Accounting system transferred and allowed to expire. | 96% | [View](./relations/SAGE_SYSTEM_CAPTURE.md) |
| **Domain Identity Fraud** | Systematic platform impersonation. | 97% | [View](./relations/DOMAIN_IDENTITY_FRAUD.md) |

---

## Forensic Evidence Archive

355 forensic EML files extracted from the Exchange database with SHA-256 integrity hashes, plus 9 primary source documents from the Ketoni/FFT Trust corpus.

| Scope | Files | Key Evidence |
|-------|-------|--------------|
| Bantjies communications | 99 | SARS manipulation, trust capture, financial control |
| Rynette Farrar | 100 | Identity impersonation across 28 sender domains |
| Elliott Attorneys | 6 | Legal threats, contempt proceedings |
| ABSA/Bank details | 100 | Revenue diversion, unauthorized bank changes |
| Manufacturing | 50 | SARS "manufacture" admission context |
| New Documents (Feb-Mar 2026) | 7 | Contempt, Void Ab Initio, POPIA, Rule 7(1)/30/30A |
| **Ketoni/FFT Trust Corpus (v15)** | **9** | **SHA, AFS, J417, Sworn Affidavit, Trust Minutes** |

**Full Archive:** [Forensic EML Index](./evidence/forensic_eml/INDEX.md) | [New Documents](./evidence/new_documents_feb_mar_2026.md)

---

## Navigation

### Master Indexes

- **[Master Filing Index](./filings/index.md)**: Direct links to all 10 application filings
- **[Master Evidence Index](./evidence_index.md)**: Comprehensive catalog of all evidence
- **[Master Timeline](./timeline.md)**: Chronological view of all 192+ events
- **[Master Entities Index](./entities/index.md)**: Index of all 125+ involved entities
- **[Master Relations Index](./relations/index.md)**: Index of all 47+ documented relations across 9 categories

### Timeline Phases

- **[Phase 1: Historical Foundation (2017-2023)](./timeline/phase1.md)**
- **[Phase 2: Trust Structure Manipulation (2023-2024)](./timeline/phase2.md)**
- **[Phase 3: Active Fraud Execution (2025)](./timeline/phase3.md)**
- **[Phase 4: Mailbox Evidence (2020-2025)](./timeline/phase4_mailbox_evidence.md)**
- **[Phase 5: Corporate Governance Notices (Feb 2026)](./timeline/phase5_governance_notices.md)**
- **[Phase 6: LEX-SIM-NN Analysis (Mar 2026)](./timeline/phase6_lex_sim_nn.md)**
- **[Phase 7: Procedural Battle (Feb-Mar 2026)](./timeline/phase7_procedural_battle.md)**

### Strategic Analysis

| Document | Purpose |
|----------|---------|
| [Red-Team Critique (v15)](./filings/RED_TEAM_CRITIQUE_2026_03_15_v15.md) | Latest adversarial analysis with primary source evidence |
| [Red-Team Critique (v14)](./filings/RED_TEAM_CRITIQUE_2026_03_14_v14.md) | AA-specific defences |
| [Refined Filing Strategy (v14)](./filings/REFINED_FILING_STRATEGY_2026_03_14_v14.md) | 3-tier filing strategy |
| [Super-Sleuth Report (v15)](./super_sleuth_report_2026_03_15.md) | Divergent investigation of 9 primary documents |
| [Hyper-Holmes Report (v15)](./hyper_holmes_report_2026_03_15.md) | Convergent validation and burden of proof |

### Simulation Models

| Model Type | Description | File |
|------------|-------------|------|
| **LEX-SIM-NN** | Differentiable legal simulation with VES modulation | [Report](./simulation/LEX_SIM_NN_REPORT_2026_03_10.md) |
| **AnyLogic (.alp)** | Multi-paradigm (SD/DES/ABM) model of the 6-phase criminal enterprise | [Download](./simulation/RevenueStreamHijacking_Case2025_137857.alp) |
| **NetLogo (.nlogo)** | Agent-based model of perpetrators, victims, and financial flows | [Download](./simulation/RevenueStreamHijacking_Case2025_137857.nlogo) |

### Supporting Repositories

- **[ad-res-j7](https://github.com/cogpy/ad-res-j7)**: Extended evidence repository with over 2,800 files

---

*Last Updated: 2026-03-18 | v15.1 — 10 applications, 192+ events, 47+ relations, 14 red-team vulnerabilities remediated, 4 filings upgraded to v15.1, 5 new intercompany fraud relations, 15 events added to timeline*
