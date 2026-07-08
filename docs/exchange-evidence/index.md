---
layout: default
title: Exchange Evidence Search Results
---

# Exchange Evidence Search Results

**Source:** Exchange Mailbox Records (Neon DB: exchange_sync)
**Last Updated:** 2026-03-08
**Database Range:** 2014-12-07 to 2026-03-08
**Total Messages in DB:** ~1M across 112 users

---

## Evidence Chains

| Chain | Messages | Description | Application |
|-------|----------|-------------|-------------|
| [sage_fraud](./sage_fraud.md) | 50 | Sage ownership transfer via false death claim | App 1 (Civil/Criminal), App 2 (CIPC), App 3 (Commercial Crime) |
| [shopify_hijacking](./shopify_hijacking.md) | 50 | Shopify revenue stream diversion | App 1 (Civil/Criminal), App 3 (Commercial Crime/Tax Fraud) |
| [rynette_denovo](./rynette_denovo.md) | 50 | Rynette-De Novo fabricated accounts | App 2 (CIPC), App 3 (Commercial Crime) |
| [trust_forgery](./trust_forgery.md) | 50 | Trust amendment forgery & backdated appointment | App 1 (Civil/Criminal), App 2 (CIPC) |
| [card_cancellation](./card_cancellation.md) | 50 | Card cancellation retaliation pattern | App 1 (Civil/Criminal) |
| [contempt](./contempt.md) | 12 | Contempt application based on void order | App 1 (Civil/Criminal) |
| [ketoni_motive](./ketoni_motive.md) | 37 | R18.75M Ketoni payout motive | App 1 (Civil/Criminal), App 3 (NPA Tax Fraud) |
| [popia](./popia.md) | 30 | POPIA violation & retaliation evidence | App 2 (POPIA Criminal Complaint) |
| [email_domain_migration](./email_domain_migration.md) | 18+1 | Email domain migration @regima.zone to @regimaskin.co.za | App 1, App 2, App 3 |
| [fund_flow_analysis](./fund_flow_analysis.md) | -- | Forensic fund flow: hidden R5M, black hole, account stripping | App 1, App 2, App 3 |
| [identity_impersonation](./identity_impersonation.md) | 6,113 | Rynette operates pete@regima.com (7 years) | App 1, App 2, App 3 |
| **[attorney_conduct](./attorney_conduct.md)** | **30** | **Elliott Attorneys: contempt threats, fund withholding, legal intimidation** | **App 1 (Civil/Criminal)** |

---

## NEW: March 2026 Evidence Update (2026-03-08)

### Attorney Conduct & Correspondence Chain

Thirty messages and nineteen attachments were extracted from the Neon DB involving Elliott Attorneys (keegan@elliottattorneys.co.za, secretary@elliottattorneys.co.za) and related legal actors (Ian Levitt Attorneys, ENS Africa, Pottas Attorneys). The correspondence reveals a pattern of legal intimidation, including explicit threats of contempt proceedings against Jacqueline Faucitt for attempting to attend her own company's training session, and the withholding of funds despite repeated demands from her legal representatives.

Key documents recovered from Cloudflare R2 include the ENS Notice of Withdrawal (41KB PDF), the ENS Settlement Agreement (397KB PDF), the Ian Levitt "WP Letter to KE" (482KB PDF), and the Ian Levitt "Letter to KE IRO Payment" (1.7MB PDF). These documents are cross-referenced against the Uniform Rules of Court (Rules 6, 7, 30, 35, 42, and 45A) to assess procedural compliance and the validity of the underlying *ex parte* interdict.

---

## February 2026 Evidence Update (2026-02-23)

### Email Domain Migration Chain

Eighteen copies of the "Important Update: Change of Email Address" email (20 June 2025) were found in the Exchange database, distributed across 10+ mailboxes. An additional EML file shows Jacqui Faucitt forwarded the same email to ENS Africa attorney S Munga on 28 August 2025 under the subject "E-MAILS CANCELLED." Follow-up emails confirm the migration was enforced, with Gayane Williams stating "regima.zone email could possibly go down anytime."

### Forensic Fund Flow Analysis

Cross-referencing bank statements, the PETEFNBDOCUMENT.pdf, and the fincosys database reveals a hidden R5 million transfer (16 November 2023), a 16-month statement "black hole" (November 2022 -- April 2024), and the stripping of approximately ZAR 10 million from all company accounts by 11 September 2025. Entity funds were used to pay legal costs (VVA: ZAR 300k to ENS, RST: ~ZAR 90k to Elliott Attorneys).

### Validation Report

The [Hyper-Holmes Validation Report](./hyper_holmes_validation_2026_02_23.md) validates 8 investigative leads from the Exchange evidence analysis.

---

## How to Use This Evidence

1. **Each chain** contains chronologically ordered email messages extracted from the Exchange mailbox database.
2. **Message IDs** can be used to retrieve full message content from the Neon DB (`exchange_sync.messages`).
3. **Cross-reference** with existing evidence in the `evidence/` directory for corroboration.
4. **Legal relevance** is mapped to the three applications (Civil/Criminal, CIPC/POPIA, Commercial Crime/Tax Fraud).

## Database Connection

Evidence is stored in Neon PostgreSQL:
- **Project:** `b2bkp-exchange-sync` (square-butterfly-04468397)
- **Schema:** `exchange_sync`
- **Table:** `messages` (~1M rows)
- **Connection:** Use `CONNECT` environment variable (neonexo1)
