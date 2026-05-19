---
layout: default
title: "Relation: Shopify Order Rerouting to Pastel"
---
# Relation: Shopify Order Rerouting to Pastel

**Relation ID:** `SHOPIFY_PASTEL_ROUTING_2026_05_19`  
**Primary event:** [EVENT_009 — Shopify Order Rerouting to Pastel](../events/EVENT_009.md)  
**Cycle:** KSM-LEX-DGen-Alexander Cycle 15  
**Canonical correction:** The live evidence model treats the 22 May 2025 incident as **order rerouting and practical audit-trail severance**, not as a bare claim of literal Shopify deletion unless later forensic logs prove deletion.[1] [2]

## Relation Summary

This relation connects the Shopify platform, the Pastel/Sage accounting pathway, the RegimA Zone Ltd platform-ownership evidence, the legitimate directors’ audit-access impairment, and the downstream filing surfaces. It is intended to prevent the event from being misread as a single-platform deletion allegation. The stronger structure is that the order stream was moved or concealed through Pastel in a way that severed the directors’ practical audit continuity and coincided with the collapse of the visible Shopify revenue stream.[1]

| Node | Role in Relation | Evidence Function |
|---|---|---|
| `EVENT_009` | Primary event | Establishes the 22 May 2025 order-routing break and monthly revenue impact. |
| `PLATFORM_001` | Shopify/e-commerce platform | Platform from which the visible order stream and audit trail were impaired. |
| Pastel/Sage accounting pathway | Destination / concealment pathway | System to subpoena or reconcile against Shopify, bank, VAT, and accounting records. |
| RegimA Zone Ltd (UK) | Platform owner/payer/operator | Establishes that the e-commerce platform was not an independent RWD ZA revenue stream. |
| Legitimate directors | Audit-access victims | Their practical ability to audit Shopify orders and revenue was severed. |
| Filing stack | Legal use surface | Civil, CIPC, POPIA, Commercial Crime, NPA, and SARS theories draw on the same corrected event shape. |

## Relation Edges

| Edge ID | From | Relation | To | Current Strength | Notes |
|---|---|---|---|---|---|
| `SPR-001` | RegimA Zone Ltd | paid/operated | `PLATFORM_001` | Strong | Use platform invoices, Shopify account records, and operating history. |
| `SPR-002` | `PLATFORM_001` | visible order stream impaired by | `EVENT_009` | Strong | Existing event record frames R1M+ monthly to R0 impact. |
| `SPR-003` | `EVENT_009` | rerouted/concealed orders into | Pastel/Sage accounting pathway | Investigative-strong | Requires Pastel/Sage exports and logs to quantify destination flow. |
| `SPR-004` | Pastel/Sage accounting pathway | should reconcile with | bank/VAT/accounting records | Investigative-strong | Supports SARS/NPA and civil accounting reconciliation. |
| `SPR-005` | `EVENT_009` | impaired audit access of | legitimate directors | Strong | The live claim is practical audit severance, not necessarily literal data deletion. |
| `SPR-006` | `EVENT_009` | triggers preservation request to | Shopify, Pastel/Sage, banks, email systems | Strong | Preservation is needed to determine whether any literal deletion also occurred. |

## Burden-of-Proof Gradient

| Burden Layer | Threshold Use | Formulation to Use |
|---|---|---|
| Civil / regulatory balance | More likely than not | “The order stream was rerouted to Pastel or made inaccessible from the legitimate directors’ Shopify audit path.” |
| Professional / CIPC / POPIA complaint | Prima facie misconduct or unlawful processing | “The rerouting created an undisclosed data/accounting path requiring formal investigation and disclosure.” |
| Criminal investigation | Reasonable suspicion / investigation trigger | “The platform and accounting logs should be preserved and compelled to test revenue diversion, computer misuse, concealment, and possible deletion.” |
| Criminal proof | Beyond reasonable doubt | “Literal deletion” should only be pleaded as proved if logs, exports, or expert evidence establish deletion rather than rerouting/concealment alone. |

## References

[1]: ../events/EVENT_009.md "EVENT_009 — Shopify Order Rerouting to Pastel"  
[2]: ../analysis/ksm-cycle15/SHOPIFY_PASTEL_GOOD_SHAPE_CORRECTION_MATRIX_2026-05-19.md "Cycle 15 Good Shape Correction Matrix"
