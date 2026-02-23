---
layout: default
title: "BANK_ACCOUNT_004: Hidden Money Maximiser (63077691682)"
---

# BANK_ACCOUNT_004: Hidden Money Maximiser Account

| Field | Value |
|-------|-------|
| **Entity ID** | BANK_ACCOUNT_004 |
| **Account Number** | 63077691682 |
| **Account Type** | FNB Money Maximiser |
| **Branch Code** | 250655 |
| **Account Holder** | MR PETER A FAUCITT |
| **Date Opened** | 16 November 2023 |
| **Initial Funding** | ZAR 5,000,000.00 (from 55270018789) |
| **Source of Funds Declared** | SALARY |
| **Statements Available** | **ZERO** |
| **Status** | COMPLETELY HIDDEN |

## Description

This account was opened on 16 November 2023 by Peter Andrew Faucitt (ID: 5204305708185, Email: PETE@REGIMA.COM) with an initial transfer of ZAR 5,000,000.00 from his Platinum Business Account (55270018789). The account has zero statements in the fincosys repository, the uploaded ZIP archives, or the Neon database. Its entire lifecycle is undocumented.

The account appears only once in the broader financial record: as a transfer source in statement #277 of account 55270018789, where a transaction described as "Tel-Banking Trf From Trf From 63077691682" shows money flowing back from this hidden account to the visible account.

## Evidence Source

**Document:** `PETEFNBDOCUMENT.pdf` (referenced in `UPDATED_MISSING_STATEMENTS_ANALYSIS.pdf`)

## Forensic Significance

The account was opened during the 16-month "black hole" period (November 2022 – April 2024) where no bank statements exist for any account. The timing — 4 months after Kayla Pretorius's death — and the complete absence of any statements suggest deliberate concealment of financial activity.

## Relations

| Relation | Entity | Type |
|---|---|---|
| Account Holder | [PERSON_001](./PERSON_001.md) (Peter Faucitt) | OWNS |
| Funded From | [BANK_ACCOUNT_002](./BANK_ACCOUNT_002.md) (55270018789) | TRANSFER_SOURCE |
| Related Event | [EVT-075](../events/EVT-075.md) | EVIDENCE_OF |
