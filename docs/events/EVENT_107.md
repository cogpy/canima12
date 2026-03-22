# EVENT_107: Rynette Logs Into SARS eFiling as Bantjies

## Event Metadata
- **Type:** Unknown
- **Entities Involved:** Unknown
- **Source:** Unknown


**Event ID:** EVENT_107  
**Date:** 2024-04-26  
**Category:** Identity Fraud / Unauthorized Access / SARS eFiling Abuse  
**Severity:** CRITICAL  
**Status:** CONFIRMED — Email evidence in Neon database

## Summary

On 26 April 2024, Rynette Farrar emailed Bantjies with the subject line **"Logged in as you"**, informing him that she had first attempted to change banking details on SARS eFiling logged in as herself ("me"), and when that failed, she logged in using Bantjies' SARS eFiling credentials to complete the change. She was changing banking details to ABSA. This email proves that Rynette had independent SARS eFiling access under her own profile AND possessed Bantjies' credentials, giving her the ability to operate his tax practitioner profile.

## Email Evidence

### The "Logged in as you" Email
- **Date:** 2024-04-26T07:27:00Z
- **From:** rynette@regima.zone (Rynette Farrar)
- **To:** danie.bantjes@gmail.com (Danie Bantjes)
- **Subject:** Logged in as you

> "Hi Danie. Just to let you know I couldn't come right with SARS logged in as 'me' to change the banking details to ABSA. So, I logged in as you and all is sorted now. Just so you know in case you get notifications from SARS, that it was me ☺"

## Critical Analysis

### What This Email Proves

1. **Rynette had her own SARS eFiling profile** — She first tried "logged in as 'me'"
2. **Rynette possessed Bantjies' SARS credentials** — She then "logged in as you"
3. **She was changing banking details** — Redirecting where SARS sends refunds/payments
4. **Banking details changed to ABSA** — Villa Via's ABSA account (statement ****9664)
5. **Bantjies consented to credential sharing** — No objection to unauthorized access
6. **Casual tone suggests routine practice** — "Just so you know" with smiley face

### Timeline Significance

| Date | Event | Days Before Forgery |
|---|---|---|
| **2024-04-26** | Rynette logs into SARS as Bantjies | **63 days** |
| **2024-06-28** | Rynette forges "pp Peter" on trust amendment | **0 (forgery date)** |
| **2024-07-08** | Peter's fraudulent Sage affidavit | **+10 days** |

The SARS login occurs **63 days before** the trust amendment forgery, placing it within the same operational period where Rynette was actively managing Bantjies' financial and legal affairs.

### Legal Implications

#### Tax Administration Act Violations
- **s234(d):** Unauthorized access to another person's SARS eFiling profile
- **s235(1):** Changing banking details under false identity
- **s236:** Making false representations to SARS

#### Identity Fraud
- Logging into a government system using another person's credentials constitutes identity fraud under the Prevention and Combating of Corrupt Activities Act (PRECCA)

#### Banking Detail Changes
- Changing SARS banking details controls where tax refunds are paid
- This gives Rynette control over Bantjies' tax refund destinations
- Combined with her control of company bank accounts, this creates a complete financial control loop

#### Credential Sharing Pattern
- Rynette used pete@regima.com email identity (SF2: Sage Screenshots)
- Rynette logged into SARS as Bantjies (this event)
- Rynette forged Peter's signature "pp Peter" (EVENT_103)
- Pattern: systematic impersonation of multiple principals

## Connection to Other Evidence

### SF4: SARS Audit Email
The SARS audit email (SF4) showed Rynette claiming Bantjies instructed payments. This event shows she also had direct access to Bantjies' SARS profile — meaning she could both execute instructions AND verify/modify tax records.

### EVENT_103: Trust Amendment Forgery (28 June 2024)
Two months after logging into SARS as Bantjies, Rynette forged Peter's signature to install Bantjies as trustee. The SARS login demonstrates the operational relationship between Rynette and Bantjies was already deeply intertwined.

### EVENT_106: Villa Via Wrong Registration Number
Rynette's comment about "CIPRO and SARS sleeping" (January 2022) shows awareness of regulatory systems. By April 2024, she was actively operating within SARS under Bantjies' identity.

### Bantjies Filing Tax Returns (January 2026)
- 2026-01-22: Bantjies emails Jax: "I have submitted your 2025 Income Tax return on 15th January 2026"
- 2026-01-22: Bantjies emails Dan: "I have submitted your 2025 Income Tax return on 15th January 2026"
- Bantjies continues to file personal tax returns for Jax and Dan while being their undisclosed trustee and R18.685M debtor

## Evidence Location

- **Neon Database:** exchange_sync.messages, subject = 'Logged in as you', from_address = 'rynette@regima.zone', received_datetime = '2024-04-26T07:27:00Z'
- **Mailbox:** pete@regima.zone (Inbox) and dan@regima.zone

## Cross-References

- **EVENT_103:** Trust Amendment Forgery (28 June 2024)
- **EVENT_104:** Backdated Main Trustee Appointment (11 August 2025)
- **EVENT_106:** Villa Via Wrong Registration Number
- **SF2:** Sage Screenshots (Rynette using pete@regima.com)
- **SF4:** SARS Audit Email
- **PERSON_002:** Rynette Farrar
- **PERSON_007:** Danie Bantjies
