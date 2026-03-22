# Relations from Mailbox Evidence (2026-02-09)
**Confidence:** 95% (Estimated)  

This document outlines key relationships and communication patterns discovered through the analysis of the RegimA Exchange mailbox data.

## Communication & Control Flows

| Relation ID | Source Entity | Target Entity | Relation Type | Significance | Evidence |
|---|---|---|---|---|---|
| REL_CTRL_009 | PERSON_004 (Jacqueline) | PERSON_002 (Rynette) | `instructed_email_diversion` | Jacqueline instructed the diversion of Bernadine Wright's emails to Rynette, enabling Rynette's information control. | `MAILBOX_JAX_DIVERT_EMAIL_2020` |
| REL_CTRL_010 | PERSON_002 (Rynette) | PERSON_LINDA | `instructed_payment_redirection` | Rynette initiated the payment redirection campaign, which was executed by Linda. | `MAILBOX_RYNETTE_BANKING_DETAILS_EMAIL` |
| REL_CTRL_011 | PERSON_002 (Rynette) | PERSON_GAYANE | `instructed_domain_change` | Rynette orchestrated the email domain change, which was announced by Gayane. | `MAILBOX_GAYANE_EMAIL_CHANGE_2025` |
| REL_ACCESS_001 | PERSON_007 (Bantjies) | ORG_001 (RWD) | `had_financial_access_since_2020` | Bantjies received bank statements and financial year-end documents for RegimA companies from July 2020, four years before his trustee appointment. | `MAILBOX_BANTJIES_BANK_STATEMENTS_2020` |
| REL_ACCESS_002 | PERSON_002 (Rynette) | ORG_001 (RWD) | `controlled_sage_since_2020` | Rynette received Sage accounting notifications from May 2020, proving long-term control over the financial system. | `MAILBOX_SAGE_NOTIFICATIONS` |
| REL_INSIDER_001 | PERSON_007 (Bantjies) | ORG_017 (Ketoni) | `had_insider_knowledge_via_george_group` | Bantjies discussed the Ketoni Investment from his George Group email address, proving he had insider knowledge through his connection to Kevin Derrick. | `MAILBOX_BANTJIES_KETONI_GEORGE_GROUP` |

## Key Communication Patterns (Fund Flow Proxies)

The fund flow analysis, based on 28,037 financial communications, reveals the following dominant patterns:

| Source | Target | Transaction Count | Total Amount (ZAR) | Significance |
|---|---|---|---|---|
| Rynette_Farrar | bnortje@icon.co.za | 343 | 1,387,721.04 | Large volume of communication to an external party. |
| Jacqueline_Faucitt | Rynette_Farrar | 2462 | 165,540,971.02 | Massive communication flow from Jacqueline to Rynette, indicating Rynette was the central hub. |
| Rynette_Farrar | Jacqueline_Faucitt | 989 | 64,035,971.16 | Significant communication flow back to Jacqueline. |
| mail-service@accounting.sageon | Rynette_Farrar | 406 | 7,205,453.11 | Rynette was the primary recipient of Sage system emails. |
| Peter_Faucitt | Rynette_Farrar | 340 | 449,977.15 | Peter consistently communicated with Rynette on financial matters. |
| ibreply@absa.co.za | Rynette_Farrar | 370 | 370.00 | Rynette was the primary recipient of Absa bank notifications. |
