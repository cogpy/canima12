---
layout: default
title: Exchange Evidence — Forensic Fund Flow Analysis
---

# Exchange Evidence: Forensic Fund Flow Analysis

**Source:** FNB Bank Statements, PETEFNBDOCUMENT.pdf, Fincosys Database  
**Date:** 23 February 2026  
**Analysis Type:** acc-fund-flow / Statement Gap Identification + Evidence Cross-Reference

---

## Summary

A comprehensive forensic analysis of all available bank statements across the fincosys repository reveals over 1,500 missing statements, a critical 16-month "black hole" period (November 2022 – April 2024), and a hidden R5 million transfer to an undocumented account.

## Critical Findings

### Finding 1: Hidden R5 Million Transfer

On 16 November 2023, Peter Faucitt transferred ZAR 5,000,000 from his Platinum Business Account (55270018789) to a newly opened Money Maximiser account (63077691682). The new account has zero statements anywhere in the system. See [EVT-075](../events/EVT-075.md) and [BANK_ACCOUNT_004](../entities/BANK_ACCOUNT_004.md).

### Finding 2: 16-Month Statement Black Hole

Six primary accounts simultaneously show no statements from approximately November 2022 to April 2024. This gap encompasses the hidden R5M transfer and follows Kayla Pretorius's death. See [EVT-076](../events/EVT-076.md).

### Finding 3: Undiscovered Accounts

| Account | Type | Entity | Statements | Status |
|---|---|---|---|---|
| 63077691682 | Money Maximiser | PF | 0 | COMPLETELY HIDDEN |
| 63176874808 | Platinum Business | Unknown | 3 (Sep–Nov 2025) | New, entity unidentified |
| 4483810003374006 | FNB Private Wealth Credit Card | PF | 1 (Jan 2021) | History missing |
| 4790812427545003 | Business Gold Credit Card | RST | 1 (Aug 2021) | History missing |
| 8812710044279003 | Business Credit Card | RST | 1 (Jul 2021) | History missing |

### Finding 4: Entity Legal Cost Payments

FNB statements confirm entity funds were used for legal costs, contradicting the applicant's later position:

| Date | Entity | Recipient | Amount |
|---|---|---|---|
| 26 Aug 2025 | VVA (62423540807) | S Munga / ENS Africa | ZAR 300,000 |
| 11 Sep 2025 | RST (55270035642) | Elliot Attorneys | ~ZAR 90,000 |

### Finding 5: Account Stripping

Between 2 July 2025 (RWD balance ~ZAR 5.3M) and 11 September 2025 (consolidated report), approximately ZAR 10 million was removed from ALL company current accounts.

## Fincosys Database Status

The Neon PostgreSQL database (synced 22 February 2026) contains:

| Schema | Records |
|---|---|
| entity_relation.entities | 1,267 |
| entity_relation.relations | 2,074 |
| event_timeline.events | 15,749 |
| hypergraph.nodes | 7,204 |
| hypergraph.hyperedges | 8,864 |

## New Data Integrated

The following Excel files have been analyzed and cross-referenced:

| File | Records | Content |
|---|---|---|
| nodes.xlsx | 548 | Statement period nodes and account entities |
| hyperedges.xlsx | 22,055 | Transaction hyperedges linking accounts to periods |
| events(1).xlsx | 2,428 | Payment, credit, transfer, and fee events |

## Application Relevance

| Application | Relevance |
|---|---|
| **App 1 (Civil/Criminal)** | Hidden assets, financial sabotage, breach of fiduciary duty |
| **App 2 (CIPC)** | Director misconduct, failure to maintain proper financial records |
| **App 3 (Commercial Crime / NPA Tax Fraud)** | R5M declared as "SALARY", undocumented accounts, asset concealment |
