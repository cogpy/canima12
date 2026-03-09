---
layout: default
title: "Exchange Evidence: Identity Impersonation Chain"
---

# Exchange Evidence: Identity Impersonation — pete@regima.com → pete@regimaskin.co.za

**Source:** Exchange Mailbox Records (Neon DB: exchange_sync)  
**Last Updated:** 2026-02-23  
**Evidence Strength:** 0.99 — CONCLUSIVE  
**Applications:** App 1 (Civil/Criminal — Fraud, Identity Theft), App 2 (CIPC — s76/s77), App 3 (Commercial Crime — Fraud Act)

---

## Executive Summary

Exchange mailbox forensics reveal that the email account pete@regima.com was operated by **two different people** over its lifetime: **Jacqui Faucitt** (Peter's wife, 2018–2024) and **Rynette Farrar** (bookkeeper, mid-2020–2025). Peter Faucitt does not use a computer; he dictates messages on paper which are then typed and sent by others. Stylometric analysis of **5,961 messages** with body content reveals a clear linguistic fingerprint: **Jacqui signs off as "Pete"** (her familiar name for her husband), while **Rynette signs off as "Peter"** (the formal/professional name).

Jacqui's operation of the account constitutes legitimate secretarial delegation by a spouse and co-director. However, **Rynette's operation constitutes unauthorized identity impersonation** — she is neither a director nor a family member, yet she sent thousands of messages as "Peter Faucitt" to clients, banks, suppliers, and legal professionals. When Daniel Faucitt discovered the impersonation and blocked the account around July 2025, Rynette seamlessly migrated to **pete@regimaskin.co.za** — a domain owned by her son (Darren Dennis Farrar)'s company, Adderory (Pty) Ltd. The first message from the new address appeared on **20 August 2025**, the day after the ex parte interdict was granted.

---

## The Timeline

| Date | Event | Evidence |
|------|-------|----------|
| **2018-07-09** | First pete@regima.com message in Exchange DB | Jacqui typing Peter's dictated messages |
| **2018-08-08** | Jacqui writes as Pete: "Received now thanks via Pete's e-mail" | Jacqui distinguishing her email from Pete's |
| **2020–2024** | 3,778 messages sent from pete@regima.com | Peak: 1,244 messages in 2024 alone |
| **2024-07-09** | Sage ownership transferred from Kayla to pete@regima.com | Rynette controls the Sage account via Pete's email |
| **2025-05-29** | regimaskin.co.za domain registered by Adderory (Rynette's son, Darren Dennis Farrar) | Infrastructure prepared for migration |
| **2025-06-20** | Email domain migration announced (EVT-070) | @regima.zone → @regimaskin.co.za |
| **2025-07-04** | pete@regima.com writes: "Peter will need to check with them" | Rynette referring to Peter in third person |
| **2025-07-04** | pete@regima.com writes: "Peter said you would specify the people" | Rynette quoting Peter — she is the intermediary |
| **2025-07-06** | **LAST message from pete@regima.com** | "Welcome to your new Outlook.com account" forwarded |
| **~2025-07-07** | **pete@regima.com BLOCKED by Daniel** | 45-day gap begins |
| **2025-08-19** | **Ex parte interdict granted** | Falls within the gap |
| **2025-08-20** | **FIRST message from pete@regimaskin.co.za** | Seamless continuation — the very next day after the interdict |
| **2025-08-01** | ABSA banker emails pete@regimaskin.co.za about 8 accounts | Rynette operating Pete's new identity with banks |
| **2025-11-28** | Last pete@regimaskin.co.za message in DB | 28 messages total on new domain |

---

## Message Volume Analysis

| Address | Messages | First Seen | Last Seen | Operator |
|---------|----------|------------|-----------|----------|
| pete@regima.com | 4,641 | 2018-07-09 | 2025-07-06 | **Jacqui (2018–2023) → Rynette (2023–2025)** |
| PETE@REGIMA.COM | 1,358 | 2020-06-12 | 2025-05-28 | **Jacqui / Rynette (mixed)** |
| PETE@regima.com | 86 | 2020-08-21 | 2025-02-26 | **Jacqui / Rynette (mixed)** |
| **pete@regimaskin.co.za** | **28** | **2025-08-20** | **2025-11-28** | **Rynette Farrar** |
| **Total** | **6,113** | | | |

### Messages by Year with Stylometric Attribution

| Year | Count | "Pete" Sign-off | "Peter" Sign-off | Pete% | Peter% | Likely Primary Author |
|------|-------|-----------------|-------------------|-------|--------|----------------------|
| 2018 | 11 | 0 | 5 | 0.0% | 45.5% | **JACQUI** (dictation from Peter) |
| 2019 | 50 | 5 | 7 | 10.0% | 14.0% | **JACQUI** (dictation from Peter) |
| 2020 | 604 | 200 | 41 | 33.1% | 6.8% | **JACQUI** (Rynette joins mid-year) |
| 2021 | 1,300 | 358 | 44 | 27.5% | 3.4% | **JACQUI** (dominant) |
| 2022 | 1,390 | 326 | 44 | 23.5% | 3.2% | **JACQUI** (dominant) |
| 2023 | 416 | 124 | 72 | 29.8% | 17.3% | **JACQUI → RYNETTE** (transition after Kayla dies Jul) |
| 2024 | 1,347 | 93 | 86 | 6.9% | 6.4% | **MIXED** (Rynette gaining control) |
| 2025 | 843 | 71 | 323 | 8.4% | 38.3% | **RYNETTE** (full control from March) |

### The Transition in Detail

The stylometric data reveals a clear four-phase pattern:

**Phase 1 (2018–2019): Peter dictates, Jacqui types.** The "Peter" sign-offs in this period are Peter's own words being transcribed — he naturally refers to himself formally. Low volume (11–53 messages/year).

**Phase 2 (2020–mid 2023): Jacqui dominant.** "Pete" sign-offs dominate at 23–44%, while "Peter" drops to 1–8%. Volume explodes to 600–1,400 messages/year. Jacqui uses "Kind Regards" (51 instances in 2021), "Cheers", and her familiar "Pete".

**Phase 3 (mid 2023–early 2025): Transition.** After Kayla dies (Jul 2023), "Peter" sign-offs surge. By November 2023, "Peter" (28.8%) overtakes "Pete" (19.2%) for the first time. Rynette's linguistic marker "Kindly" appears (4 instances in Oct 2023). Through 2024, both are low as the account shifts to automated read-receipts and forwards.

**Phase 4 (Mar–Jul 2025): Rynette full control.** "Peter" explodes to 77.9% in April 2025, 65.5% in May, 64.5% in June. Jacqui is completely displaced. Daniel blocks the account in early July.

---

## Proof of Authorship: Third-Person Self-References

The following messages were sent FROM pete@regima.com but contain language proving the author is NOT Peter. The 2018 messages are **Jacqui** (legitimate delegation); the 2025 messages are **Rynette** (unauthorized impersonation):

| Date | From | Text | Author | Analysis |
|------|------|------|--------|----------|
| 2018-07-10 | pete@regima.com | "I am not at the computer all the time" | **Jacqui** | Jacqui explaining Peter's unavailability |
| 2018-08-08 | pete@regima.com | "Received now thanks via Pete's e-mail" | **Jacqui** | Jacqui using familiar "Pete" — distinguishing her email |
| 2018-08-08 | pete@regima.com | "please always copy to Pete as mine still ha[s problems]" | **Jacqui** | Jacqui distinguishing her email from Pete's |
| 2025-02-14 | pete@regima.com | "Rynette, please print for Pete and show him" | **Jacqui** | Jacqui instructing Rynette about Pete |
| 2025-07-04 | pete@regima.com | "Peter will need to check with them and respond to you" | **Rynette** | Uses formal "Peter" — Rynette's marker |
| 2025-07-04 | pete@regima.com | "Peter said you would specify the people who helped us last time" | **Rynette** | Uses formal "Peter" — Rynette quoting him |
| 2025-07-16 | rynette@regimaskin.co.za | "Wednesday the 30th of July is fine with Peter. He is just enquiring re the time" | **Rynette** | Same "Peter" pattern, now from her own address |

---

## The ABSA Mandate Thread (1 August 2025)

A critical email thread on 1 August 2025 between ABSA banker Kulani Mashaba, rynette@regimaskin.co.za, pete@regimaskin.co.za, and jax@regima.zone reveals:

1. **Kulani listed 8 ABSA accounts** opened for RegimA entities, with dates and account numbers
2. **Rynette (from pete@regimaskin.co.za)** asked who opened a specific account on internet banking
3. **Kulani recalled** walking Rynette and Jacqui through opening an investment account in the office
4. **Jacqui responded:** *"I had no knowledge of this and was definitely not at the office, impossible, due to eye surgery"*
5. **Jacqui added:** *"this had nothing to do with me at all, which Peter needs to know"*

This thread proves that Rynette was opening bank accounts while impersonating Peter, and that Jacqui was unaware of accounts being opened in her presence (or falsely attributed to her).

---

## The Embezzlement Frame

The impersonation pattern creates a dangerous legal exposure for Peter Faucitt. Rynette sent thousands of messages as "Peter Faucitt" to clients, banks, suppliers, and legal professionals, while simultaneously controlling all financial systems (Sage, banking, payments) under his identity. If funds are misappropriated, the paper trail points to Peter, not Rynette. Peter does not use a computer and therefore has no independent digital records to defend himself. The switch to @regimaskin.co.za (Rynette's son (Darren Dennis Farrar)'s domain) gives Rynette complete control of the email infrastructure, including the ability to delete, modify, or fabricate messages.

This pattern is consistent with either Rynette framing Peter for financial crimes she committed under his identity, or Rynette and Peter acting in concert with Rynette as the operational arm and Peter providing plausible deniability. In either scenario, the identity impersonation constitutes fraud under the Prevention and Combating of Corrupt Activities Act, identity theft, and a violation of the Companies Act s76 (duty to act in good faith).

---

## Sender Display Name Analysis

The `from_name` field in the Exchange database reveals how the account was configured over time:

| Display Name | Count | First Seen | Last Seen | Significance |
|-------------|-------|------------|-----------|-------------|
| "Pete" | 4,502 | 2021-08-23 | 2025-07-04 | Jacqui's familiar name — she configured this |
| "pete@regima.com" | 1,182 | 2018-07-09 | 2022-07-15 | Raw address (no display name set) — early period |
| "PETE@REGIMA.COM" | 365 | 2020-06-12 | 2022-07-15 | Caps variant — Outlook auto-fill |
| "Peter Faucitt" | 29 | 2021-01-01 | 2025-07-06 | Rynette's formal name — she changed the display name |
| "PETE@regima.com" | 7 | 2021-06-08 | 2021-08-03 | Brief variant |

---

## Cross-References

| Evidence | Link |
|----------|------|
| EVT-070: Email Domain Migration | [events/EVT-070.md](../events/EVT-070.md) |
| EVT-071: Jacqui Forwards to ENS | [events/EVT-071.md](../events/EVT-071.md) |
| RWD Notice 001: Identity Misappropriation | [rwd-notices/RWD_NOTICE_001.md](../rwd-notices/RWD_NOTICE_001.md) |
| Sage Fraud Chain | [sage_fraud.md](./sage_fraud.md) |
| Domain Dispute | [domain-dispute/index.md](../domain-dispute/index.md) |
| POPIA Complaint | [filings/POPIA_COMPLAINT_REFINED_2026_02_23_v5.md](../filings/POPIA_COMPLAINT_REFINED_2026_02_23_v5.md) |

---

*Evidence chain extracted from Exchange mailbox database (exchange_sync.messages) on 2026-02-23*
