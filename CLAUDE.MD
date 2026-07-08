# CLAUDE.MD -- Revenue Stream Hijacking Case Repository

> **Case 2025-137857: Peter Faucitt v. Jacqueline Faucitt et al.**
> High Court of South Africa | Revenue Stream Hijacking, Trust Capture & Racketeering

---

## Repository Overview

This repository (`cogpy/revstream1`) is the **evidence analysis, legal documentation, and prosecution preparation** system for Case 2025-137857. It contains structured data models, legal filings, forensic analysis, and evidence cataloging for a multi-layered fraud and conspiracy case involving revenue stream hijacking, trust capture, perjury, and abuse of court process.

**Total documented losses:** R10.27M+ direct theft; **R63M+** total financial impact (including the R18.685M Ketoni payout at stake and R34.9M annual revenue destroyed).

### Related Repositories

| Repository | Purpose | Relationship |
|---|---|---|
| **cogpy/ad-res-j7** | Legal case management + Lex inference engine (transformer-based legal reasoning) | Primary evidence base (1,700+ files in 20 annexures), ARENA/AGENT/RELATIONS framework |
| **rzonedevops/analysis** | Extended analysis (private) | Supplementary analytical work |
| **cogpy/revstream1** (this repo) | Evidence analysis, legal filings, prosecution preparation, GitHub Pages site | Synthesizes findings from ad-res-j7 into prosecution-ready documents |

---

## Three-Dimensional Organization (from ad-res-j7)

This case is organized along three axes that mirror the ad-res-j7 framework:

| Dimension | What It Contains | Local Equivalent |
|---|---|---|
| **ARENA** (Legal Framework) | 60+ legal principles from `lex/lv1/known_laws.scm` | `M-REF/`, `docs/COMBINED_LEGAL_NARRATIVE.md` |
| **AGENT** (Evidence Base) | 1,700+ evidence files (JF01-JF13, SF1-SF14) | `evidence/`, `Revenue_Stream/05_Evidence/` |
| **RELATIONS** (Arena-Agent Connections) | How legal principles connect to evidence | `provable-foreknowledge/`, `docs/CONSPIRACY_EVIDENCE_CROSS_REFERENCE*.md` |
| **GRIP** (System Workflows) | Optimization and integration workflows | `scripts/`, data model validation pipelines |

---

## Directory Structure

```
revstream1/
|
|-- CLAUDE.MD                          # This file -- AI assistant guide
|-- _config.yml                        # Jekyll site configuration (GitHub Pages)
|-- LICENSE                            # AGPL-3.0
|
|-- data_models/                       # Structured case data (YAML/JSON)
|   |-- entities/                      # 86 entities (36 persons, 50 organizations)
|   |-- events/                        # 130 events (49 meet criminal threshold)
|   |-- relations/                     # 123 relations between entities/events
|   |-- timelines/                     # 125 timeline entries (1982-2026)
|
|-- docs/                              # Jekyll GitHub Pages documentation (18 subdirs)
|   |-- index.md                       # Main site index
|   |-- EXECUTIVE_SUMMARY.md           # Prosecution-ready overview
|   |-- FORENSIC_CAUSAL_MAP.md         # Actor hierarchy and causal chains
|   |-- COMBINED_LEGAL_NARRATIVE.md    # Seven-stage conspiracy narrative
|   |-- TRUST_CAPTURE_MAP.md           # Trust capture analysis
|   |-- R18_75M_KETONI_PAYOUT_*.md     # Central motive analysis
|   |-- CONSPIRACY_EVIDENCE_*.md       # Evidence cross-reference with timeline
|   |-- super_sleuth_report_*.md       # Divergent analysis (new leads)
|   |-- hyper_holmes_report_*.md       # Convergent validation (confirmation)
|   |-- ketoni-timeline.md             # Ketoni R18.685M payout timeline
|   |-- filings/                       # Refined legal filings (CIPC, POPIA, NPA)
|   |-- entities/                      # Entity profile pages
|   |-- timeline.md                    # Master chronological timeline
|
|-- evidence/                          # Case evidence organized by type
|   |-- bank_records/                  # FNB statements (SLG, RST, RWD, VVA, personal)
|   |-- emails/                        # Key correspondence (FNB, Rynette, Bantjies)
|   |-- cipc/                          # Companies and Intellectual Property Commission docs
|   |-- rsa_documents/                 # RegimA SA setup, Kachan AOD, trust closures
|   |-- accounting/                    # Financial records and audit data
|   |-- fabricated_accounts/           # De Novo 2019 fabricated statements
|   |-- sage/                          # Sage screenshots (identity fraud evidence)
|   |-- FNB_FRAUD_LETTER_2025_06_17/   # Peter's written admission of fraud knowledge
|   |-- FNB_RESPONSE_EMAIL_2025_06_18/ # FNB confirming SOLE authority
|
|-- M-REF/                             # Master Reference Index (6 documents)
|   |-- 00_MASTER_INDEX.md             # Navigation guide
|   |-- 01_LEGAL_CONCEPTS_EXPLAINED.md # Setting Down vs Setting Aside, Contempt, Costs
|   |-- 02_SOLE_AUTHORITY_*.md         # Banking mandate analysis (SOLE vs ANY TWO)
|   |-- 03_PERJURY_ANALYSIS_*.md       # R500K "birthday gift" deconstruction
|   |-- 04_FINANCIAL_SABOTAGE_*.md     # Seven-phase sabotage timeline
|   |-- 05_OVERSIGHT_CHAIN_*.md        # Four oversight layers and conflicts
|   |-- 06_REGIMA_SA_MANDATE_*.md      # Impersonation fraud analysis
|
|-- MR/                                # Master Records (markdown summaries)
|   |-- Entities.md                    # All 86 entities with roles and impact
|   |-- Events.md                      # All 130+ events with classifications
|   |-- Accounts.md                    # Financial accounts analysis
|   |-- Exchanges.md                   # Transaction records
|
|-- Revenue_Stream/                    # Revenue hijacking documentation
|   |-- INDEX.md                       # 158-day hijacking timeline
|   |-- 01_POPIA/                      # POPIA-compliant vs opaque system analysis
|   |-- 02_Hijacking/                  # Financial extraction, Shopify revelation
|   |-- 05_Evidence/                   # Affidavit with 50+ evidence annexures
|
|-- FOREKNOWLEDGE_REFINED_FILINGS_2026_02_08/  # Latest legal filings
|   |-- README.md                      # Overview
|   |-- FOREKNOWLEDGE_CLASSIFICATION_FRAMEWORK.md  # Tier A/B/C/D system
|   |-- CIPC_COMPLAINT_*.md            # Companies Act violations
|   |-- POPIA_COMPLAINT_*.md           # Identity fraud, data destruction
|   |-- COMMERCIAL_CRIME_*.md          # Fraud, theft, insider trading
|   |-- NPA_TAX_FRAUD_*.md             # Income tax evasion, VAT fraud
|   |-- PROFESSIONAL_MISCONDUCT_*.md   # SAICA referral for Bantjies
|
|-- provable-foreknowledge/            # Foreknowledge audit trail system
|   |-- README.md                      # Overview
|   |-- classification_report.md       # Per-agent tier classification with evidence
|   |-- knowledge_matrix.md            # 24 material facts x 7 agents cross-reference
|   |-- per_agent_audit_trail.md       # Chronological log per agent
|
|-- scripts/                           # Python analysis and refinement scripts (170+)
|   |-- analyze_*.py                   # Evidence analysis scripts
|   |-- refine_*.py                    # Data model refinement scripts
|   |-- generate_*.py                  # Document generation scripts
|   |-- update_*.py                    # GitHub Pages update scripts
|
|-- evidence_documents/                # Additional evidence repositories
|-- TODO-SEARCH/                       # Search results and parsed outputs
|-- SUPER_REFINED_FILINGS_2026_02_08/  # Previous filing versions
```

---

## Evidence Cataloging System

### Primary Annexures (JF01-JF13)

| Code | Description | Files | Strength |
|---|---|---|---|
| JF01 | Shopify Plus Email (forensic time capsule) | 1 | Conclusive |
| JF02 | Banking Mandates | - | Conclusive |
| JF03 | FNB FICA/KYC Documents | - | Conclusive |
| JF04 | Company Card Records | - | Strong |
| JF05 | Personal Bank Statements | - | Conclusive |
| JF06 | Court Documents | 99 | Conclusive |
| JF07 | Screenshots | 186 | Strong |
| JF08 | Evidence Packages (5 dated) | 5 | Conclusive |
| JF09 | Email Correspondence | - | Strong |
| JF10 | CIPC Records | - | Conclusive |
| JF11 | Trust Documents | - | Strong |
| JF12 | Financial Statements | - | Moderate |
| JF13 | Additional Evidence | - | Strong |

### Supplementary Files (SF1-SF14)

| Code | Description | Strength |
|---|---|---|
| SF1 | Ketoni R18.685M Payout Documentation | Conclusive |
| SF2 | Sage Screenshots (Rynette Control) | Conclusive |
| SF3 | Stock Adjustment R5.4M | Strong |
| SF4 | ReZonance Dissolution Records | Strong |
| SF5 | SARS Communication Records | Strong |
| SF6 | Kayla Pretorius Estate R1.035M | Conclusive |
| SF7 | Adderory Domain Registration | Strong |
| SF8 | De Novo Fabricated Financials | Conclusive |
| SF9 | Elliott Attorneys Demand Letter | Strong |
| SF10 | Sage User Access Screenshot (pete@regima.com) | Conclusive |
| SF11 | Sage Registration Expired (evidence concealment) | Conclusive |
| SF12 | ReZonance Supplier Ledger | Conclusive |
| SF13 | Elliott Attorneys Demand (coordinated conspiracy) | Strong |
| SF14 | Debt Structure Correction (Ketoni-Bantjies scheme) | Conclusive |

---

## Foreknowledge Classification Framework

Agents are classified into four tiers based on independently provable documentary evidence:

| Tier | Classification | Criteria | Agents |
|---|---|---|---|
| **A** | Premeditated Conspirator | 3+ independent documentary proofs | Peter Faucitt (11), Rynette Farrar (5), Danie Bantjies (4) |
| **B** | Active Participant with Proven Knowledge | 1-2 direct documentary proofs | Adderory/Rynette's Son (2), ENS Africa (1) |
| **C** | Knowledge Unproven | Participated but no proof of knowledge | Kevin Derrick, De Novo/Marisca Meyer, Elliott Attorneys |
| **D** | Structural Connection Only | Connected but no active participation | -- |

**Evidentiary discipline:** Tier C agents have ZERO documentary evidence of foreknowledge. Accusing them without evidence would undermine case credibility. They should be treated as potential witnesses or affected parties.

**Note:** Adderory was upgraded from Tier C to Tier B based on the void ab initio analysis (Feb 2026) -- documentary proof of competing domain registration (29 May 2025) and connection to fabricated financials.

---

## The Gestalt: How Everything Fits Together

### Central Motive: R18.685M Ketoni Payout (May 2026)

Ketoni Investment Holdings owes **R18.685M to the Faucitt Family Trust** under a Call Option Agreement, first exercise window **May 2026**. Trustee **Danie Bantjies** controls both ends of the transaction:
- As **Trustee of FFT**: controls how the Trust receives and distributes payment
- As **CFO of George Group**: has insider access to Ketoni (the debtor) through Kevin Derrick

Every event in the case, from trust restructuring to audit trail destruction to interdict filings, is strategically timed to ensure Peter and Bantjies control 100% of the R18.685M distribution by neutralizing all other beneficiaries before the payout date.

### Actor Hierarchy

```
DANIE BANTJIES -- "The Financial Architect" (Tier A: 8 proofs)
    |  Trustee of FFT, CFO of George Group, 6 conflicts of interest
    |  Swore his own false affidavit, dismissed fraud reports
    |  "Bantjies instructed her to make those huge payments" (SARS audit email)
    |
    |-- (instructs) -->
    |
RYNETTE FARRAR -- "The Chief Operator" (Tier A: 12 proofs)
    |  Controls all financial systems, operates as Peter's digital identity
    |  Sage owner, Shopify audit trail deleter, identity fraudster
    |  Forged Peter's signature to install Bantjies as Trustee
    |
    |-- (controls/impersonates) -->
    |
PETER FAUCITT -- "The Figurehead/Directing Mind" (Tier A: 10 proofs)
    |  Does not use computers; either a puppet or a liar (both criminal)
    |  Filed perjured interdict, wrote FNB fraud letter (own admission)
    |  Orchestrated R10.6M extraction after obtaining court order
```

### The Seven-Phase Conspiracy

| Phase | Period | Key Actions |
|---|---|---|
| **1. Trust Capture** | Feb 2023 -- Jul 2024 | Ketoni investment, Bantjies installed as Trustee via forged signature |
| **2. Obstacle Elimination** | Jul 2023 -- Feb 2024 | Kayla dies (R1.035M creditor), ReZonance dissolution pressure |
| **3. Revenue Diversion** | Mar -- May 2025 | Shopify revenue hijacked, ABSA account diverted, R5.4M stock vanishes |
| **4. Whistleblower Retaliation** | Jun 2025 | Daniel reports fraud -> cards cancelled next day -> forced personal insolvency |
| **5. Evidence Fabrication** | Jun -- Jul 2025 | R500K "birthday gift" narrative, fabricated 2019 financials, Sage lockout |
| **6. Court Abuse** | Aug 2025 | Interdict filed in Family Court (not Commercial), granted ex parte |
| **7. Asset Extraction** | Sep 2025 | R10.6M drained in 8 days using the court order |
| **Endgame** | May 2026 | Curatorship to seize beneficiary shares before R18.685M payout |

### The Inescapable Paradox

Peter claims he "doesn't use email or computers":

| If TRUE | If FALSE |
|---|---|
| Rynette committed forgery and identity theft | Peter committed perjury |
| All digital "Peter" authorizations are forged | Peter is complicit in excluding Daniel |
| The ABSA diversion was unauthorized | Peter has been lying to the court |

**Either way, crimes have been committed.**

### Banking Mandate Proof

| Entity | Mandate Type | Implication |
|---|---|---|
| Strategic Logistics CC | **SOLE** | Daniel's actions were pre-authorized |
| RegimA Skin Treatments CC | **SOLE** | Daniel's actions were pre-authorized |
| RegimA Worldwide Distribution CC | **SOLE** | Daniel's actions were pre-authorized |
| Villa Via | **SOLE** | Daniel's actions were pre-authorized |
| **RegimA SA (Pty) Ltd** | **ANY TWO TOGETHER** | Daniel's consent was legally required |

Peter accused Daniel of unauthorized extraction on **SOLE** accounts (where no authorization was needed), while Peter/Rynette diverted revenue on the **ANY TWO TOGETHER** account (where Daniel's consent was legally required but not obtained).

### Burden of Proof Assessment

| Category | Threshold | Status |
|---|---|---|
| Criminal charges (beyond reasonable doubt) | 95% | **7 events exceed** (perjury, fraud, identity fraud, conspiracy) |
| Criminal charges (strong) | 90% | **12 of 13 charges meet 90%+** |
| Civil claims (balance of probabilities) | 50% | **All 6 claims at 100%** |

---

## Legal Strategy -- Parallel Tracks

### Track 1: Rule 42 Rescission Application
Set aside the ex parte interdict on grounds of fraud on the court, material non-disclosure, and abuse of process.

### Track 2: Counter-Application
Delinquency declarations, trustee removal, damages (R5.4M + R1.73M + ongoing), personal costs (de bonis propriis).

### Track 3: Criminal Complaints
CIPC (6 conflicts), POPIA (identity fraud/data destruction), NPA Tax Fraud, Commercial Crime/Hawks (insider trading), Legal Practice Council (Elliott Attorneys), SARB Exchange Control.

### Track 4: Void Domino Effect
Under SA law, if the founding affidavit was perjured, the interdict is void ab initio, which voids the mediation, settlement agreements, and the Main Trustee appointment.

### Track 5: POCA (Organized Crime)
Clear hierarchy, division of labor, common unlawful purpose, use of legitimate entities for illegal purposes.

---

## Void Ab Initio Analysis (Feb 2026 -- LATEST)

The ex parte interdict granted on 19 August 2025 is **void ab initio** (void from the beginning). This is the central legal finding of the Feb 2026 analysis.

### The Eight Pillars of Invalidity

| # | Pillar / Pattern | Evidence |
|---|---|---|
| 1 | **Legal Impossibility** | FNB mandates grant SOLE authority -- "unauthorized" transactions by a sole administrator cannot exist |
| 2 | **Perjury with Foreknowledge** | FNB Legal confirmed SOLE authority 18 Jun 2025; Peter swore the opposite 13 Aug 2025 |
| 3 | **Material Non-Disclosure** | Peter concealed SOLE mandate, FNB letter, card sabotage, R500K reimbursement context |
| 4 | **Supporting Affidavit Fraud** | Bantjies received Daniel's fraud reports 6 Jun; certified false affidavit 13 Aug |
| 5 | **Direct Admission w/ Concealment** | Peter admits cancelling cards but conceals it was secret, unauthorized, retaliatory |
| 6 | **Fabrication of Evidence** | Fake 2019 accounts for company name created in 2021; Peter signed as director for year he wasn't appointed |
| 7 | **Weaponized Litigation** | Jacqui sued for "harassment" for warning De Novo about fake accounts; settlement clauses silence witnesses |
| 8 | **RSA Mandate Fraud** | RegimA SA "ANY TWO TOGETHER" -- ABSA diversion without Daniel's required consent = forgery or perjury |

### The Contempt Application: Weaponizing a Void Order

On **4 February 2026**, Peter filed a Contempt of Court Application seeking **6 months imprisonment** for Jacqueline. This is the use of a fraudulently obtained, void court order to imprison a victim of the fraud. Key documents:

| Document | Location |
|---|---|
| Final Void Ab Initio Report | `docs/filings/FINAL_VOID_AB_INITIO_REPORT_2026_02_09.md` |
| Void Ab Initio Reassessment | `docs/filings/VOID_AB_INITIO_REASSESSMENT_2026_02_09.md` |
| Classification Report | `docs/filings/VOID_AB_INITIO_CLASSIFICATION_REPORT_2026_02_09.md` |
| Knowledge Matrix | `docs/filings/VOID_AB_INITIO_KNOWLEDGE_MATRIX_2026_02_09.md` |
| Per-Agent Audit Trail | `docs/filings/VOID_AB_INITIO_PER_AGENT_AUDIT_TRAIL_2026_02_09.md` |
| Contempt Evidence Summary | `docs/evidence/CONTEMPT_EVIDENCE_SUMMARY_2026_02_09.md` |
| Civil Contempt Analysis | `docs/filings/CIVIL_CONTEMPT_ANALYSIS_2026_02_09.md` |
| Gestalt Analysis | `ANNEXURES/VOID_AB_INITIO_EVIDENCE/GESTALT_ANALYSIS.md` |
| Void Ab Initio Register (JSON) | `void_ab_initio_register.json` |

### Legal Consequences of Void Ab Initio

| Consequence | Effect |
|---|---|
| The interdict is a legal nullity | Has no force or effect; can be disregarded |
| Contempt applications are baseless | Cannot be in contempt of an order that never existed |
| Enforcement is malicious prosecution | Knowing it was obtained through fraud |
| R10.6M extraction was theft | Extracted under authority of a void order |
| All downstream agreements are void | Mediation, settlements, Main Trustee appointment |

### New Events (2026-02-09)

| Event | Date | Description |
|---|---|---|
| EVENT_095 | 2025-09-18 | Mediation and settlement agreements |
| EVENT_096 | 2025-09-22 | Notice of withdrawal from settlements (duress) |
| EVENT_097 | 2025-11-04 | Variation application dismissed |
| EVENT_098 | 2026-01-10 | Stock removal blocked (R200K) |
| EVENT_099 | 2026-01-12 | Attorney correspondence re contempt |
| EVENT_100 | 2025-12-02 | Bank cards, phone removal, body guard |
| EVENT_101 | 2026-02-04 | Contempt application filed |
| EVENT_102 | 2026-02-04 | Void ab initio evidence submitted |

### New Entities (2026-02-09)

| Entity | Type | Role |
|---|---|---|
| ORG_020 | Elliott Attorneys Inc | Applicant's Attorneys |
| ORG_021 | Pottas Attorneys | Respondent's Attorneys |
| PERSON_019 | Oliver ("Arthur") | Employee (Warehouse) |

---

## Smoking Gun Evidence

| # | Evidence | What It Proves |
|---|---|---|
| 1 | **SARS Audit Email** ("Bantjies instructed her to make those huge payments") | Bantjies is the ultimate controller; Rynette executes |
| 2 | **Sage Screenshots (SF10, SF11)** (Rynette operating pete@regima.com + subscription owner) | Identity fraud and absolute system control |
| 3 | **Trustee Appointment Email** (11 Aug 2025: sent BY Rynette, TO Bantjies primary, CC Peter) | Reveals actual hierarchy |
| 4 | **Peter's FNB Fraud Letter** (17 Jun 2025: written admission of fraud and Exchange Control violations) | His own confession |
| 5 | **41-Day Backdating** (Main Trustee dated 1 Jul, signed 11 Aug) | Document fraud |
| 6 | **FNB Legal Response** (18 Jun 2025: confirms SOLE authority) | Destroys the entire interdict premise |
| 7 | **Daniel's personal account at R864.45** (16 Jul 2025) | Proves R500K was reimbursement, not extraction |

---

## Critical Evidence Gaps

| Evidence Needed | Purpose | Priority |
|---|---|---|
| Ketoni Investment Agreement (full text) | Confirms exact R18.685M amount and May 2026 date | CRITICAL |
| Communication records between Bantjies and Derrick | Proves/disproves Derrick's knowledge | HIGH |
| Ketoni board meeting minutes re: FFT payment | Insider dealing evidence | HIGH |
| Sage audit logs (pre-expiration) | Full transaction history | HIGH (may be destroyed) |
| Email server logs | Prove Rynette's impersonation of Peter | MEDIUM |
| Bantjies appointment originals | Shows irregular process | MEDIUM |
| De Novo working papers and engagement letters | Resolves De Novo's knowledge (Tier C -> A or exonerated) | HIGH |
| ABSA account details (8 accounts referenced in FIC) | Maps the money laundering pipeline | HIGH |
| Adderory Pty Ltd (UK) Companies House records | Documents customer diversion beneficiary | MEDIUM |
| Kevin Derrick interview / Section 205 subpoena | Resolves Tier C status; may yield insider dealing evidence | HIGH |

---

## Prosecution Strategy Gaps (Identified Feb 2026)

These are structural gaps in the current filing portfolio that should be addressed:

| # | Gap | Risk | Recommendation |
|---|---|---|---|
| 1 | **No POCA Section 38 preservation order** for R18.685M Ketoni payout | Conspirators intercept payout in May 2026 (~3 months away) | **URGENT:** File preservation order immediately |
| 2 | **No standalone SARB filing** for Exchange Control violations | Peter's own admission (SF10) goes unactioned | File dedicated SARB complaint citing FNB Fraud Letter |
| 3 | **ENS Africa (Tier B) absent from all filings** | Obstruction of justice goes unaddressed | File Legal Practice Council complaint (EVENT_061) |
| 4 | **Adderory not named in any filing** | Customer diversion beneficiary escapes scrutiny | Include in Commercial Crime Submission |
| 5 | **Kevin Derrick completely uninvestigated** | Key witness/potential co-conspirator untapped | Request Section 205 subpoena for communications |
| 6 | **De Novo working papers not subpoenaed** | Cannot resolve Tier C status | Include in discovery requests |
| 7 | **Ketoni payout interception plan unmapped** | Cannot demonstrate endgame to court | Develop step-by-step interception scenario |
| 8 | **ReZonance/Kayla POPIA chain undeveloped** | Data theft after death lacks evidence chain | Investigate server logs, domain transfers |

---

## The R5.4M "Missing Money"

The Sep 2025 extraction analysis reveals a critical discrepancy. Total system funds went from **R13,930,329.92 to R8,555,533.02** -- meaning approximately **R5.4M left the system entirely** and cannot be accounted for in either Current or Savings accounts. This correlates with the **R5.2M SLG stock disappearance** (EVENT_028) and the suspicious R5.2M invoice from SLG to RST. The SARS audit email ("Bantjies instructed her to make those huge payments") may refer to these untraced funds.

---

## The Shopify Ownership Revelation

The Shopify platform was owned by Daniel's UK company **RegimA Zone Ltd** since July 2023, generating **R60.25M in total revenue** over 28 months. Daniel paid **$1,000-$2,000 USD/month** (R140K-R280K total) for the platform. After Peter stripped the accounts, the September 2025 Shopify bill of **$3,495.92 USD (R60,960.11 ZAR)** failed 9 consecutive times. This proves:
- Daniel funded the core revenue infrastructure from his own resources
- RWD ZA had no independent revenue stream -- it issued invoices for sales on Daniel's platform
- Disrupting Daniel = disrupting 100% of the business

---

## The R500K Perjury -- Complete Deconstruction

Peter's Paragraph 7.18 claim that Jacqueline transferred R500K to Daniel as a "birthday gift":

| Peter's Claim | Evidence Reality |
|---|---|
| "She transferred it" | Daniel initiated it himself using SOLE authority |
| "As a birthday gift" | Reimbursement: Daniel had already spent R520K from personal savings on company expenses |
| "I did not authorise" | Irrelevant: SOLE authority mandate requires no authorization |
| "He was not entitled to accept" | False: SOLE authority + personal funds already spent |
| **Daniel's balance on Jul 16:** | **R864.45** (personally insolvent from paying company bills) |
| **Net position after R500K:** | **Still R20K out of pocket** |
| **Peter then extracted:** | **R10.6M in 8 days** (21x Daniel's reimbursement) |

---

## The Four Extraction Mechanisms (R15.6M Total)

| Mechanism | Amount | Method | Beneficiary |
|---|---|---|---|
| Inventory/Stock Manipulation | R5.4M | Fictitious R5.2M inventory adjustment in SLG (10x prior year, 46% of annual sales) | Adderory (Rynette's son) |
| Direct Revenue Hijacking | R3.1M | Shopify order removal, domain fraud, bank account redirection over 85 days | Peter/Rynette |
| Trust Fund Misappropriation | R2.85M | Multi-year unauthorized diversions from FFT | Peter/Bantjies |
| Unaccounted Payments/Transfers | R4.27M | R1.035M unpaid ReZonance debt, R1.73M VVA emptying, misc | Various |

---

## Premeditation Evidence

Rynette created a **PowerPoint presentation on April 11, 2025** (40 days before the Shopify sabotage) documenting that Shopify was central to all business operations. This proves **she knew exactly what she was disrupting** and planned the attack on the revenue infrastructure with full knowledge of its impact.

Additionally, the **fabricated 2019 financial statements for "RegimA SA"** were issued on **June 25, 2025** -- but the company was called **"K OZ CREATIVE"** until March 9, 2021. Financial statements for a company name that didn't exist in 2019 are inherently fraudulent.

---

## Criminal Charges Summary (15-20 charges across 8 statutes)

| Statute | Key Charges | Primary Targets |
|---|---|---|
| POCA (Act 121/1998) | Racketeering (s2), Money Laundering (s4) | All three Tier A |
| Common Law | Fraud, Theft, Forgery, Perjury, Obstruction | Faucitt, Farrar, Bantjies |
| Companies Act | Delinquency (s162), Breach of Duties (s76/77), Reckless Trading (s22) | Faucitt, Bantjies |
| Trust Property Control Act | Breach of Fiduciary Duty (s9) | Faucitt, Bantjies |
| Tax Administration Act | Tax Evasion (s234), Fraudulent Returns (s235) | All three |
| Exchange Control Regs | Unauthorized International Remittances | Faucitt (own admission) |
| POPIA | Identity Fraud (s107(1)), Obstruction (s107(2)), Data Theft (s107(3)) | Farrar, Faucitt |
| FICA | Failure to Report Suspicious Transactions (s29) | Bantjies |

---

## Development Environment

- **Site:** Jekyll (GitHub Pages) at `https://cogpy.github.io/revstream1`
- **Theme:** Minima
- **Analysis scripts:** Python 3.x (170+ scripts in `scripts/`)
- **Data models:** YAML/JSON in `data_models/`
- **License:** AGPL-3.0

### Key Scripts Categories

| Category | Pattern | Purpose |
|---|---|---|
| Analysis | `analyze_*.py` | Evidence analysis and data integrity checks |
| Refinement | `refine_*.py` | Data model and legal filing refinement |
| Generation | `generate_*.py` | Document and filing generation |
| Updates | `update_*.py` | GitHub Pages and filing updates |
| Cross-reference | `cross_reference_*.py` | Evidence-to-entity-to-event linkage |

---

## Working Conventions

1. **Evidence referencing:** Always cite specific annexure codes (JF01-JF13, SF1-SF14) and event codes (EVENT_*) when making claims.
2. **Burden of proof:** Tag assertions with their threshold (criminal 95% or civil 50%) and evidence strength.
3. **Foreknowledge discipline:** Never accuse Tier C agents without new documentary evidence. They may be innocent.
4. **Mandate awareness:** Always specify which banking mandate (SOLE vs ANY TWO TOGETHER) applies when analyzing transactions.
5. **Date precision:** Use exact dates from evidence. The timeline is the backbone of the prosecution.
6. **Cross-repo references:** Evidence files in ad-res-j7 are referenced by annexure code. Always verify against the AGENT_INDEX.md in that repo.
7. **Filing updates:** When new evidence is found, update all five filing tracks (CIPC, POPIA, NPA, Commercial Crime, Professional Misconduct).

---

## Quick Reference: Key Dates

| Date | Event | Significance |
|---|---|---|
| 20 Feb 2023 | Ketoni incorporated | Vehicle for R18.685M |
| 24 Apr 2023 | FFT invests in Ketoni | R18.685M claim established |
| 13 Jul 2023 | Kayla Pretorius dies | R1.035M creditor eliminated |
| 28 Jun 2024 | Rynette forges Bantjies appointment | Trust captured |
| 14 Apr 2025 | Revenue diverted to secret account | Revenue hijacking begins |
| 6 Jun 2025 | Daniel reports fraud to Bantjies | Whistleblower trigger |
| 7 Jun 2025 | 15+ company cards cancelled | Retaliation within 24 hours |
| 17 Jun 2025 | Peter's FNB Fraud Letter | Written admission |
| 18 Jun 2025 | FNB confirms SOLE authority | Destroys interdict premise |
| 19 Aug 2025 | Ex parte interdict granted | Court order obtained by fraud |
| 3-11 Sep 2025 | R10.6M extracted in 8 days | The actual theft |
| **May 2026** | **Ketoni R18.685M payout due** | **THE TARGET** |

---

*Last updated: 2026-02-09*

---

## Current Investigation: Stock Audit & Inventory Forensics (2026-03-23)

### Session Context
Branch: `claude/investigate-stock-audit-issues-zdJeF`
This repo provides the structured data models and BOM cost flow analysis for the stock audit investigation.

### Work Completed This Session

#### BOM Forensic Cost Flow Analysis
- Added `evidence/bom_cost_flow_data.json` — comprehensive Bill of Materials cost flow analysis for SLG stock audit
- Documents the manufacturing-to-distribution cost chain: RST (manufacturing) → RWD (distribution) → SLG (logistics) → RSA (retail)
- Maps how phantom entries in RST manufacturing (via Pastel manufacturing module) propagate through the entire supply chain

#### Entity-Relation Model Updates
- `data_models/entities.json` — 86+ entities including all stock-related entities
- `data_models/events.json` — 130+ events including stock adjustment events
- `data_models/relations.json` — 123+ relations including intercompany stock flows

### Key Data Assets for Stock Investigation

| File | Purpose |
|------|---------|
| `evidence/bom_cost_flow_data.json` | BOM cost flow chain (RST→RWD→SLG→RSA) |
| `evidence/intercompany_stock_analysis.md` | Intercompany stock movement analysis |
| `data_models/entities/` | All entity definitions (companies, persons, accounts) |
| `data_models/events/` | Chronological event records |
| `data_models/stock_flow_model_2026_03_07.json` | Stock flow dynamics model |
| `data_models/entity_relation_framework_v50_bantjies_farrar.scm` | Latest Scheme framework with Bantjies/Farrar roles |
| `evidence/accounting/` | Accounting records and trial balances |
| `evidence/fabricated_accounts/` | Fabricated account evidence (De Novo) |

### Findings Relevant to This Repo

1. **R5.4M SLG stock disappearance** — documented in BOM cost flow analysis showing supply chain break
2. **RST phantom entries** — Pastel manufacturing module used to inflate finished goods (R1,443,217.78)
3. **R58.58M unreconciled intercompany volume** — no reconciliation at any point in the RWD hub
4. **Rynette's sole control** — all stock adjustments across all entities controlled by single person
5. **Bantjies' complicity** — acknowledged "huge gaps" but took no action; dismissed R246K flag

### Next Steps for Next Iteration

#### Priority 1 — Data Model Updates
- [ ] Update `data_models/entities.json` with enriched inventory entity data from ad-res-j7/analysis
- [ ] Add new stock-audit-specific events to `data_models/events.json` (Bantjies Feb 2024 flag, SARS query, Pastel seizure Jul 2025)
- [ ] Create new relations linking Rynette to stock adjustments across all entities
- [ ] Update Scheme framework (v51) with inventory control failure patterns

#### Priority 2 — Evidence Enrichment
- [ ] Cross-reference BOM cost flow data with fincosys transaction records for validation
- [ ] Search comcosys email archive for evidence of stock adjustment instructions
- [ ] Add SARS correspondence regarding year-end intercompany invoices to evidence catalog

#### Priority 3 — Filing Updates
- [ ] Update SARS complaint in `SUPER_REFINED_FILINGS_2026_02_08/` with stock audit quantification
- [ ] Add stock disappearance evidence to NPA referral (PRECCA threshold exceeded at R5.4M)
- [ ] Integrate inventory findings into foreknowledge register (`provable-foreknowledge/`)

#### Priority 4 — Visualization
- [ ] Generate stock flow diagram showing RST→RWD→SLG→RSA chain with loss points
- [ ] Update GitHub Pages documentation with stock audit findings
- [ ] Create Ketoni payout impact diagram showing how stock losses reduce trust assets

### Ecosystem Role
This repo synthesizes evidence from ad-res-j7 (annexures JF01-JF16, SF1-SF8+) into structured data models that feed the lex inference engine. The BOM cost flow analysis is a key new asset that should be referenced by the ad-res-j7 entity files and the analysis repo's consolidated reports.
