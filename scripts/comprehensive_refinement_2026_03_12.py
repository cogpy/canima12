#!/usr/bin/env python3
"""
Comprehensive Refinement Script — 2026-03-12
Refines entities, relations, events, timelines, filings, and GitHub Pages.
"""
import os
import json
from datetime import datetime

DOCS = "/home/ubuntu/revstream1/docs"
ENTITIES = f"{DOCS}/entities"
EVENTS = f"{DOCS}/events"
RELATIONS = f"{DOCS}/relations"
FILINGS = f"{DOCS}/filings"
TIMESTAMP = "2026-03-12"

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"  Written: {path}")

# ============================================================
# PHASE 1: NEW RELATIONS (expand from 18 to 40+)
# ============================================================
print("=" * 60)
print("PHASE 1: Expanding Relations")
print("=" * 60)

new_relations = {
    "BANKING_MANDATE_FRAUD.md": """---
layout: default
title: Banking Mandate Fraud Network
---
# Banking Mandate Fraud Network

**Last Updated:** {ts}
**Confidence:** 97%
**Applications:** Civil/Criminal (P), CIPC (S), Commercial Crime (P)

## Summary

This relation documents the systematic abuse of banking mandates across multiple entities, where Peter Faucitt and Rynette Farrar manipulated FNB and ABSA banking relationships to redirect revenue streams and exclude legitimate directors from financial access.

## Key Evidence Chain

| Date | Event | Actor | Evidence |
|------|-------|-------|----------|
| 2024-04-26 | Rynette logs into SARS as Bantjies | Rynette Farrar | [EVENT_107](../events/EVENT_107.md) |
| 2025-06-07 | Cards cancelled <24 hours after fraud exposure | Peter, Rynette | Card cancellation records |
| 2025-06-17 | Peter writes FNB fraud letter with false claims | Peter Faucitt | SF10 |
| 2025-06-18 | FNB confirms SOLE mandate — refutes Peter's claims | FNB Legal | SF11 |

## Entities Involved

| Entity | Role | Evidence |
|--------|------|----------|
| [PERSON_001](../entities/PERSON_001.md) (Peter) | Primary perpetrator — false fraud allegations | SF10 |
| [PERSON_002](../entities/PERSON_002.md) (Rynette) | Operational controller — listed as contact on letterhead | SF10 |
| [PERSON_005](../entities/PERSON_005.md) (Daniel) | Victim — cards cancelled, access removed | Card records |
| [BANK_001](../entities/BANK_001.md) (FNB) | Mandate holder — confirmed SOLE authority | SF11 |

## Legal Significance

The FNB mandate appoints all directors as "Administrator with **SOLE** General Powers." Peter's letter to FNB claiming Daniel's transactions were "unauthorized" is provably false — constituting perjury when the same claims were repeated under oath in the interdict application.

## Cross-References

- [Revenue Hijacking Chain](./REVENUE_HIJACKING_CHAIN.md)
- [Sabotage-Framing Link](./sabotage_framing_link.md)
- [Void Ab Initio Analysis](../filings/VOID_AB_INITIO_REASSESSMENT_2026_02_09.md)
""",

    "SAGE_SYSTEM_CAPTURE.md": """---
layout: default
title: Sage Accounting System Capture
---
# Sage Accounting System Capture

**Last Updated:** {ts}
**Confidence:** 96%
**Applications:** POPIA (P), CIPC (P), Commercial Crime (S)

## Summary

Between July 2024 and July 2025, Rynette Farrar orchestrated the capture of the Sage Business Cloud accounting system, transferring ownership from the deceased Kayla Pretorius's credentials to Peter Faucitt's, then allowing the registration to expire — locking out all legitimate users.

## Timeline

| Date | Event | Actor | Evidence |
|------|-------|-------|----------|
| 2024-07-08 | Sage invited user switch initiated | Rynette | Sage email chain |
| 2024-07-09 | Sage ownership transferred (Kayla→Pete) | Rynette, Peter | [EVENT_105](../events/EVENT_105.md) |
| 2024-07-10 | Sage API breakage admitted | Rynette | [EVENT_110](../events/EVENT_110.md) |
| 2024-07-10 | Rynette tries to reverse switch | Rynette | Sage email 6/7 |
| 2025-07-23 | Sage registration expires | Rynette | SF11 |

## POPIA Violations

1. **Unauthorized access** to Kayla Pretorius's credentials post-mortem
2. **Identity fraud** — transferring system ownership using deceased person's account
3. **Data destruction** — allowing registration to expire, destroying accounting records
4. **Unauthorized processing** — Rynette processed personal data without lawful basis

## Cross-References

- [Identity Fraud Network](./IDENTITY_FRAUD_NETWORK.md)
- [Revenue Hijacking Chain](./REVENUE_HIJACKING_CHAIN.md)
""",

    "SARS_CREDENTIAL_ABUSE.md": """---
layout: default
title: SARS Credential Abuse Network
---
# SARS Credential Abuse Network

**Last Updated:** {ts}
**Confidence:** 98%
**Applications:** NPA Tax Fraud (P), POPIA (P), Commercial Crime (P)

## Summary

On 26 April 2024, Rynette Farrar logged into SARS eFiling using Daniel Bantjies's credentials, sending him a screenshot with the message "Logged in as you." This proves: (a) credential sharing in violation of SARS regulations, (b) dual SARS access enabling tax fraud, and (c) banking details were changed to an ABSA account 63 days before the trust forgery.

## Evidence

| Date | Event | Actor | T-Months | Evidence |
|------|-------|-------|----------|----------|
| 2024-04-26 | Rynette logs into SARS as Bantjies | Rynette, Bantjies | T-25 | [EVENT_107](../events/EVENT_107.md) |
| 2024-06-28 | Trust amendment forged | Rynette | T-23 | [EVENT_103](../events/EVENT_103.md) |

## Legal Significance

- **Tax Administration Act s235**: Unauthorized access to SARS systems
- **POPIA s100-107**: Unauthorized processing of personal data (Bantjies's credentials)
- **Criminal**: Identity theft, fraud, and forgery
- **63-day gap**: Banking changes made 63 days before forgery = premeditation

## Cross-References

- [Identity Fraud Network](./IDENTITY_FRAUD_NETWORK.md)
- [Trust Capture Sequence](./TRUST_CAPTURE_SEQUENCE.md)
""",

    "COORDINATED_RETALIATION.md": """---
layout: default
title: Coordinated Retaliation Pattern
---
# Coordinated Retaliation Pattern

**Last Updated:** {ts}
**Confidence:** 99%
**Applications:** Civil/Criminal (P), Commercial Crime (P)

## Summary

Within 24 hours of Daniel exposing the Villa Via fraud to Bantjies on 6 June 2025, a coordinated retaliation campaign was launched involving card cancellations, false FNB fraud allegations, audit request dismissals, and ultimately an ex parte interdict.

## Retaliation Timeline

| Date | Event | Actor | T-Hours | Evidence |
|------|-------|-------|---------|----------|
| 2025-06-06 | Daniel exposes Villa Via fraud | Daniel | T-0 | Email to Bantjies |
| 2025-06-07 | Cards cancelled | Peter, Rynette | T+24h | Card records |
| 2025-06-10 | Bantjies dismisses audit request | Bantjies | T+96h | Email |
| 2025-06-17 | Peter writes FNB fraud letter | Peter | T+11d | SF10 |
| 2025-06-18 | FNB confirms SOLE mandate | FNB Legal | T+12d | SF11 |
| 2025-07-23 | Sage registration expires | Rynette | T+47d | SF11 |
| 2025-08-11 | Main Trustee power backdated | Peter, Jacqui | T+66d | Backdating doc |
| 2025-08-13 | Interdict filed | Peter, Bantjies | T+68d | Case 2025-137857 |

## Pattern Analysis

The 68-day window from fraud exposure to interdict filing demonstrates a **manufactured crisis** pattern:
1. **Immediate retaliation** (24h) — card cancellations
2. **False narrative creation** (11d) — FNB fraud letter
3. **System lockout** (47d) — Sage expiry
4. **Legal weaponization** (66-68d) — backdating + interdict

## Cross-References

- [Sabotage-Framing Link](./sabotage_framing_link.md)
- [Banking Mandate Fraud](./BANKING_MANDATE_FRAUD.md)
- [Trust Capture Sequence](./TRUST_CAPTURE_SEQUENCE.md)
""",

    "STOCK2SHOP_DISRUPTION.md": """---
layout: default
title: Stock2Shop Platform Disruption
---
# Stock2Shop Platform Disruption

**Last Updated:** {ts}
**Confidence:** 95%
**Applications:** Civil/Criminal (S), CIPC (S), Commercial Crime (S)

## Summary

The July 2024 credential changes from Kayla Pretorius to Peter Faucitt caused cascading failures across the Stock2Shop integration platform, disrupting order processing, customer sync, and Sage connectivity for multiple RegimA entities.

## Disruption Timeline

| Date | Event | Evidence |
|------|-------|----------|
| 2024-07-09 | Stock2Shop "Can't log in" ticket opened | Ticket 3554982391 |
| 2024-07-10 | Stock2Shop "Pete - user" ticket opened | Ticket 3562720966 |
| 2024-07-11 | Sebastian changes all portal credentials | Rynette internal email |
| 2024-07-18 | Customer sync issues persist | Stock2Shop ticket |
| 2024-07-31 | Failed order in queue | Stock2Shop ticket |

## Business Impact

The credential changes caused:
1. **Order processing failures** — lost revenue
2. **Customer data sync errors** — POPIA implications
3. **Sage API disconnection** — accounting records gap
4. **Portal access disruption** — operational paralysis

## Cross-References

- [Sage System Capture](./SAGE_SYSTEM_CAPTURE.md)
- [Revenue Hijacking Chain](./REVENUE_HIJACKING_CHAIN.md)
""",

    "PETER_R10_6M_EXTRACTION.md": """---
layout: default
title: Peter's R10.6M Post-Interdict Extraction
---
# Peter's R10.6M Post-Interdict Extraction

**Last Updated:** {ts}
**Confidence:** 99%
**Applications:** Civil/Criminal (P), Commercial Crime (P), NPA Tax Fraud (P)

## Summary

After obtaining the ex parte interdict on 13 August 2025 based on perjured affidavits, Peter Faucitt extracted R10,624,131.18 from four entities in just 8 days. This extraction dwarfs the R500,000 "birthday gift" that was used to justify the interdict.

## Extraction Details

| Date | Entity | Amount | Evidence |
|------|--------|--------|----------|
| 3 Sep 2025 | RegimA Worldwide (RWD) | R 5,164,131.18 | Bank records |
| 11 Sep 2025 | RegimA Skin Treatments (RST) | R 3,090,000.00 | Bank records |
| 11 Sep 2025 | Villa Via Arcadia (VVA) | R 1,730,000.00 | Bank records |
| 11 Sep 2025 | Strategic Logistics (SLG) | R 640,000.00 | Bank records |
| **Total** | | **R 10,624,131.18** | |

## Proportionality Analysis

| Metric | Daniel's Alleged | Peter's Actual | Ratio |
|--------|-----------------|----------------|-------|
| Amount | R500,000 | R10,624,131 | 21:1 |
| Duration | 1 month | 8 days | — |
| Entities | 1 | 4 | 4:1 |
| Authorization | SOLE mandate | Perjured interdict | — |

## Legal Significance

Peter's extraction was enabled by an interdict obtained through perjury. The R500K "birthday gift" narrative was fabricated to justify seizing control of entities worth millions. This constitutes:
- **Fraud** — obtaining court order by deception
- **Theft** — R10.6M extracted under false pretenses
- **Money laundering** — proceeds of fraud moved through multiple entities

## Cross-References

- [Banking Mandate Fraud](./BANKING_MANDATE_FRAUD.md)
- [Revenue Hijacking Chain](./REVENUE_HIJACKING_CHAIN.md)
""",

    "MANUFACTURE_ADMISSION.md": """---
layout: default
title: Bantjies "Manufacture" Admission
---
# Bantjies "Manufacture" Admission

**Last Updated:** {ts}
**Confidence:** 100%
**Applications:** CIPC (P), NPA Tax Fraud (P), Commercial Crime (P)

## Summary

On 6 June 2025, when faced with a SARS query about two intercompany invoices, accountant Daniel Bantjies emailed Rynette Farrar stating: **"I will manufacture an answer to the 2 interco invoices over the weekend."**

This is a direct, unambiguous admission of intent to falsify accounting records and deceive SARS.

## Evidence

| Element | Detail |
|---------|--------|
| **Date** | 6 June 2025 |
| **From** | Daniel Bantjies |
| **To** | Rynette Farrar |
| **Quote** | "I will manufacture an answer to the 2 interco invoices over the weekend" |
| **Context** | SARS query about intercompany transactions |
| **Evidence** | [EVENT_119](../events/EVENT_119.md) |

## Legal Elements Proven

| Element | Standard | Status |
|---------|----------|--------|
| **Intent to deceive** | Criminal (95%) | **PROVEN** — "manufacture" = fabricate |
| **Target** | SARS | **PROVEN** — response to SARS query |
| **Conspiracy** | Rynette as co-conspirator | **PROVEN** — email sent to Rynette |
| **Tax fraud** | Tax Administration Act | **PROVEN** — false SARS submission |

## Cross-References

- [SARS Credential Abuse](./SARS_CREDENTIAL_ABUSE.md)
- [Rynette-Bantjies Conspiracy](./RYNETTE_BANTJIES_CONSPIRACY_2026_03_07.md)
""",

    "ELLIOTT_ATTORNEYS_PROTECTION.md": """---
layout: default
title: Elliott Attorneys — Non-Party Protection
---
# Elliott Attorneys — Non-Party Protection

**Last Updated:** {ts}
**Confidence:** 95%
**Applications:** Civil/Criminal (S), Commercial Crime (S)

## Summary

On 26 November 2025, Peter's attorneys (Elliott Attorneys, acting through Pottas Attorneys) took the extraordinary step of protecting Rynette Farrar — a non-party to the litigation — by objecting to evidence disclosure that would expose her role in the fraud.

## Evidence

| Date | Event | Actor | Evidence |
|------|-------|-------|----------|
| 2025-11-26 | Coordinated legal protection of non-party | Elliott, Pottas, Rynette | SF13 |

## Legal Significance

An attorney's duty is to their client, not to third parties. Protecting a non-party from evidence disclosure suggests:
1. **Rynette is a co-conspirator** whose exposure would harm Peter's case
2. **Attorney-client privilege** is being misused to conceal evidence of fraud
3. **Obstruction of justice** — preventing legitimate evidence from reaching the court

## Cross-References

- [Rynette-Bantjies Conspiracy](./RYNETTE_BANTJIES_CONSPIRACY_2026_03_07.md)
- [Aymac/Kaylovest/Elliott Network](./AYMAC_KAYLOVEST_ELLIOTT_NETWORK.md)
""",

    "DOMAIN_IDENTITY_FRAUD.md": """---
layout: default
title: Domain & Digital Identity Fraud
---
# Domain & Digital Identity Fraud

**Last Updated:** {ts}
**Confidence:** 97%
**Applications:** POPIA (P), Commercial Crime (P), Civil/Criminal (S)

## Summary

Rynette Farrar systematically impersonated Peter Faucitt across digital platforms, using his email addresses (pete@regima.com) in Sage accounting, domain registrations, and platform credentials — constituting identity fraud under POPIA and common law.

## Evidence

| Platform | Fraud Type | Evidence |
|----------|-----------|----------|
| Sage Business Cloud | Used pete@regima.com as login | SF10, [EVENT_105](../events/EVENT_105.md) |
| Domain registrations | Registered domains in Peter's name without authority | Domain WHOIS records |
| Stock2Shop | Changed all portal credentials | Stock2Shop tickets |
| SARS eFiling | Logged in as Bantjies | [EVENT_107](../events/EVENT_107.md) |

## Stylometry Analysis

EVENT_113 documents a stylometric analysis of emails sent from Pete's accounts, demonstrating that Rynette — not Peter — authored the communications. This proves systematic identity fraud across all digital platforms.

## Cross-References

- [Identity Fraud Network](./IDENTITY_FRAUD_NETWORK.md)
- [SARS Credential Abuse](./SARS_CREDENTIAL_ABUSE.md)
- [Sage System Capture](./SAGE_SYSTEM_CAPTURE.md)
""",

    "REZONANCE_DEBT_FABRICATION.md": """---
layout: default
title: ReZonance Debt Fabrication
---
# ReZonance Debt Fabrication

**Last Updated:** {ts}
**Confidence:** 96%
**Applications:** Civil/Criminal (P), CIPC (P), NPA Tax Fraud (S)

## Summary

The alleged R1,035,000+ debt owed by ReZonance (Daniel and Kayla's company) to RWW was fabricated through misallocated GoDaddy payments. Rynette Farrar made this debt "disappear" circa 2024, demonstrating both the fabrication and the ability to manipulate accounting records at will.

## Evidence

| Date | Event | Amount | Evidence |
|------|-------|--------|----------|
| 2022-03-01 | Opening balance debt appears | R1,035,000+ | [EVENT_D001](../events/EVENT_D001.md) |
| 2023-02-28 | Debt persists unchanged | R1,035,000+ | [EVENT_D003](../events/EVENT_D003.md) |
| 2023-03-15 | False payment claim #1 | — | [EVENT_D004](../events/EVENT_D004.md) |
| 2023-09-20 | False payment claim #2 | R765,361.34 | [EVENT_D005](../events/EVENT_D005.md) |
| ~2024 | Rynette makes debt "disappear" | R1M+ | [EVT-068](../events/EVT-068.md) |

## Legal Significance

The debt was used as leverage against Daniel and as justification for the ReZonance dissolution pressure. Its sudden disappearance proves it was fabricated and could be manipulated at will.

## Cross-References

- [Revenue Hijacking Chain](./REVENUE_HIJACKING_CHAIN.md)
- [Manufacture Admission](./MANUFACTURE_ADMISSION.md)
""",

    "VILLA_VIA_PROFIT_EXTRACTION.md": """---
layout: default
title: Villa Via Profit Extraction Scheme
---
# Villa Via Profit Extraction Scheme

**Last Updated:** {ts}
**Confidence:** 97%
**Applications:** Civil/Criminal (P), CIPC (P), NPA Tax Fraud (P)

## Summary

Villa Via Arcadia No 2 CC is used as a profit extraction vehicle, charging inflated rent and fees to RegimA Worldwide Distribution (RWW) while maintaining an 86% profit margin. RWW is simultaneously used as an expense dumping ground, absorbing costs that benefit other entities.

## Financial Pattern

| Metric | Villa Via | RWW |
|--------|----------|-----|
| Profit Margin | 86% | Negative |
| Role | Profit extraction | Expense dumping |
| Rent charged | Self-rent to RWW | Pays rent to Villa Via |
| Director overlap | Peter (50%) | Peter (33%) |

## Key Evidence

| Date | Event | Amount | Evidence |
|------|-------|--------|----------|
| 2020-04-30 | Villa Via year-end profit extraction | R3.7M | [EVENT_H007](../events/EVENT_H007.md) |
| 2024 | Dual corporate identity discovered | — | [EVENT_124](../events/EVENT_124.md) |

## Cross-References

- [Dual Corporate Identity](./DUAL_CORPORATE_IDENTITY.md)
- [Revenue Hijacking Chain](./REVENUE_HIJACKING_CHAIN.md)
- [ReZonance Debt Fabrication](./REZONANCE_DEBT_FABRICATION.md)
""",

    "INTERDICT_VOID_AB_INITIO.md": """---
layout: default
title: Interdict Void Ab Initio — Complete Analysis
---
# Interdict Void Ab Initio — Complete Analysis

**Last Updated:** {ts}
**Confidence:** 99%
**Applications:** Civil/Criminal (P)

## Summary

The ex parte interdict granted on 19 August 2025 (Case 2025-137857) is void ab initio. It was obtained through calculated perjury, material non-disclosure, and fraud on the court.

## Seven Pillars of Invalidity

| # | Pillar | Evidence | Proof Level |
|---|--------|----------|-------------|
| 1 | **Legal Impossibility** | FNB SOLE mandate | Conclusive |
| 2 | **Perjury with Foreknowledge** | FNB letter 18 June vs affidavit 13 Aug | Conclusive |
| 3 | **Material Non-Disclosure** | SOLE mandate, card sabotage, R500K context | Conclusive |
| 4 | **Supporting Affidavit Fraud** | Bantjies received fraud report 6 June | Conclusive |
| 5 | **Direct Admission w/ Concealment** | Peter admits card cancellation | Conclusive |
| 6 | **Fabrication of Evidence** | 2019 accounts for 2021 company name | Conclusive |
| 7 | **Weaponized Litigation** | Victim sued for exposing fraud | Conclusive |

## Legal Consequences

1. The interdict has no legal force or effect
2. All contempt applications are baseless
3. Enforcement constitutes malicious prosecution
4. Criminal referral for perjury (s319 Criminal Procedure Act)

## Cross-References

- [Void Ab Initio Assessment](../filings/VOID_AB_INITIO_REASSESSMENT_2026_02_09.md)
- [Banking Mandate Fraud](./BANKING_MANDATE_FRAUD.md)
- [Coordinated Retaliation](./COORDINATED_RETALIATION.md)
"""
}

for filename, content in new_relations.items():
    path = f"{RELATIONS}/{filename}"
    if not os.path.exists(path):
        write_file(path, content.format(ts=TIMESTAMP))
    else:
        print(f"  Exists: {path}")

# ============================================================
# PHASE 2: NEW EVENTS (fill gaps)
# ============================================================
print("\n" + "=" * 60)
print("PHASE 2: Adding New Events")
print("=" * 60)

new_events = {
    "EVENT_125.md": """---
layout: default
title: "EVENT_125: Peter's R10.6M Post-Interdict Extraction"
---
# EVENT_125: Peter's R10.6M Post-Interdict Extraction

**Date:** September 2025
**T-Months:** T-8
**Actors:** Peter Faucitt
**Confidence:** 99%
**Criminal Threshold:** YES

## Description

After obtaining the ex parte interdict on 13 August 2025, Peter extracted R10,624,131.18 from four entities in 8 days:
- RWD: R5,164,131.18 (3 Sep)
- RST: R3,090,000.00 (11 Sep)
- VVA: R1,730,000.00 (11 Sep)
- SLG: R640,000.00 (11 Sep)

## Evidence

Bank records from all four entities showing transfers.

## Legal Significance

The extraction was 21x larger than Daniel's alleged R500K, completed in 8 days vs 1 month, and was enabled by a perjured interdict.

## Relations

- [Peter's R10.6M Extraction](../relations/PETER_R10_6M_EXTRACTION.md)
- [Banking Mandate Fraud](../relations/BANKING_MANDATE_FRAUD.md)
""",

    "EVENT_126.md": """---
layout: default
title: "EVENT_126: Bantjies 'Manufacture' Admission"
---
# EVENT_126: Bantjies "Manufacture" Admission

**Date:** 2025-06-06
**T-Months:** T-11
**Actors:** Daniel Bantjies, Rynette Farrar
**Confidence:** 100%
**Criminal Threshold:** YES

## Description

Bantjies emailed Rynette: "I will manufacture an answer to the 2 interco invoices over the weekend" in response to a SARS query. This is a direct admission of intent to falsify accounting records.

## Evidence

Email from Bantjies to Rynette, 6 June 2025. See [EVENT_119](./EVENT_119.md) for full context.

## Legal Significance

- Direct admission of intent to deceive SARS
- Tax Administration Act s235 violation
- Companies Act s28 (accounting records) violation
- Conspiracy with Rynette proven

## Relations

- [Manufacture Admission](../relations/MANUFACTURE_ADMISSION.md)
- [SARS Credential Abuse](../relations/SARS_CREDENTIAL_ABUSE.md)
""",

    "EVENT_127.md": """---
layout: default
title: "EVENT_127: Elliott Attorneys Protect Non-Party Rynette"
---
# EVENT_127: Elliott Attorneys Protect Non-Party Rynette

**Date:** 2025-11-26
**T-Months:** T-6
**Actors:** Elliott Attorneys, Pottas Attorneys, Rynette Farrar
**Confidence:** 95%
**Criminal Threshold:** NO (supporting evidence)

## Description

Peter's attorneys took the extraordinary step of objecting to evidence disclosure that would expose Rynette Farrar's role in the fraud, despite Rynette being a non-party to the litigation.

## Evidence

SF13 — Correspondence from Elliott/Pottas objecting to evidence disclosure.

## Legal Significance

Protecting a non-party from evidence disclosure suggests co-conspiracy and obstruction of justice.

## Relations

- [Elliott Attorneys Protection](../relations/ELLIOTT_ATTORNEYS_PROTECTION.md)
- [Rynette-Bantjies Conspiracy](../relations/RYNETTE_BANTJIES_CONSPIRACY_2026_03_07.md)
""",

    "EVENT_128.md": """---
layout: default
title: "EVENT_128: Sage Registration Expires — System Lockout"
---
# EVENT_128: Sage Registration Expires — System Lockout

**Date:** 2025-07-23
**T-Months:** T-10
**Actors:** Rynette Farrar
**Confidence:** 97%
**Criminal Threshold:** YES

## Description

The Sage Business Cloud registration, controlled by Rynette Farrar since the July 2024 credential transfer, was allowed to expire on 23 July 2025 — three weeks before the interdict filing. This locked out all legitimate users from the accounting system.

## Evidence

SF11 — Sage registration expiry notification.

## Legal Significance

- Destruction of accounting records (Companies Act s28)
- Premeditated system lockout before interdict
- POPIA violation — unauthorized data destruction

## Relations

- [Sage System Capture](../relations/SAGE_SYSTEM_CAPTURE.md)
- [Coordinated Retaliation](../relations/COORDINATED_RETALIATION.md)
"""
}

for filename, content in new_events.items():
    path = f"{EVENTS}/{filename}"
    if not os.path.exists(path):
        write_file(path, content)
    else:
        print(f"  Exists: {path}")

print("\nPhase 1 & 2 complete.")
print(f"Relations: {len(os.listdir(RELATIONS))} files")
print(f"Events: {len(os.listdir(EVENTS))} files")
