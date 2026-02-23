---
layout: default
title: Exchange Evidence — Email Domain Migration
---

# Exchange Evidence: Email Domain Migration (@regima.zone → @regimaskin.co.za)

**Source:** Exchange Mailbox Records (Neon DB: exchange_sync) + EML file  
**Extracted:** 2026-02-23  
**Messages Found:** 18 copies in Exchange DB + 1 EML (Proton Mail forward)

---

## Summary

On 20 June 2025, Gayane Williams sent an email titled "Important Update: Change of Email Address" instructing all contacts to migrate from @regima.zone to @regimaskin.co.za. The email was distributed across at least 18 mailboxes in the Exchange tenant. On 28 August 2025, Jacqui Faucitt forwarded the same email to ENS Africa attorney S Munga under the subject "E-MAILS CANCELLED."

## Evidence Chain

| # | Date | Actor | Action | Source |
|---|---|---|---|---|
| 1 | 20 Jun 2025 12:49 UTC | Gayane Williams | Sends first batch of "Change of Email" emails | Exchange DB (Internet-Message-ID: DBBPR08MB1079683772C58993179EC11E6CA7CA) |
| 2 | 20 Jun 2025 12:55 UTC | Gayane Williams | Sends second batch | Exchange DB (DBBPR08MB10796056745D53852D020562ACA7CA) |
| 3 | 20 Jun 2025 12:58 UTC | Gayane Williams | Sends third batch | Exchange DB (DBBPR08MB107960C571300EEF823596C79CA7CA) |
| 4 | 20 Jun 2025 12:59 UTC | Gayane Williams | Sends fourth batch | Exchange DB (DBBPR08MB107965FC2AB19CCB45DF933F0CA7CA) |
| 5 | 20 Jun 2025 13:01 UTC | Gayane Williams | Sends fifth batch | Exchange DB (DBBPR08MB107960A25AFA06B07621EA0E2CA7CA) |
| 6 | 20 Jun 2025 13:04 UTC | Gayane Williams | Sends sixth batch (incl. Linda) | Exchange DB (DBBPR08MB10796572770CA2C30573F8393CA7CA) |
| 7 | 20 Jun 2025 13:08 UTC | Gayane Williams | Sends final batch (incl. Daniel, Emma, Claire, Karen, Vicky, Laura, Australia) | Exchange DB (DBBPR08MB10796722622999A9DB48E88EBCA7CA) |
| 8 | 20 Jun 2025 13:11 UTC | Gayane Williams | Sends additional copy | Exchange DB (DBBPR08MB10796D169E30D4CFD79D5BD9BCA7CA) |
| 9 | 23 Jun 2025 | Gayane (from @regimaskin.co.za) | Tells Karen Morris: "Yes it will be with immediate effect as regima.zone email could possibly go down anytime" | Exchange DB |
| 10 | 23 Jun 2025 | Gayane (from @regimaskin.co.za) | Tells Vicky Lewendon: "Yes you can start using the new emails" | Exchange DB |
| 11 | 28 Aug 2025 | Jacqui Faucitt (jfaucitt@proton.me) | Forwards email to S Munga (ENS Africa) as "E-MAILS CANCELLED" | EML file |
| 12 | 29 Sep 2025 | Gayane (from @regimaskin.co.za) | Tells client: "a notice was sent out on the 20th of June regarding the change of email address" | Exchange DB |
| 13 | 8 Oct 2025 | Gayane (from @regima.zone) | Tells Dr Booysen: "a notice was sent out in June regarding the change of email address" | Exchange DB |

## Mailbox Distribution

| Mailbox | User ID | Received |
|---|---|---|
| Gayane Williams (gayane@regima.zone) | 6755cc9d-b65d-426e-b77d-8ee917543a27 | Multiple copies (sent items) |
| Rynette Farrar (rynette@regima.zone) | 52a423b7-13e7-4599-8d6f-c833ebce69d7 | 12:49 UTC |
| Linda (linda@regima.zone) | 5392e6cc-c2e0-477d-8af1-376579a16aa8 | 13:04 UTC |
| Emma Wallis (emma@regima.zone) | 5374b057-f4c0-42fa-b367-c8496937d6b0 | 13:08 UTC |
| Claire Chandler (claire@regima.zone) | — | 13:08 UTC |
| Daniel Faucitt (dan@regima.zone) | — | 13:08 UTC |
| Karen Morris (karenm@regima.zone) | 06ee2da9-a5ac-4665-a9af-b0fe80208afb | 13:08 UTC |
| Vicky Lewendon (vickyb@regima.zone) | — | 13:08 UTC |
| Laura Puttick (laurap@regima.zone) | dfb6b91a-5eba-4e3c-9b0f-90343328a472 | 13:08 UTC |
| RegimA Australia (australia@regima.zone) | a8519352-3443-4d20-bbfa-b8345a6b4ecc | 13:08 UTC (2 copies) |

## Application Relevance

| Application | Relevance |
|---|---|
| **App 1 (Civil/Criminal)** | Demonstrates systematic infrastructure hijacking — migration of business communications to competitor domain |
| **App 2 (CIPC)** | Shows unauthorized use of company resources and customer relationships |
| **App 3 (Commercial Crime)** | Revenue stream diversion through email redirection |

## Database Query

```sql
SELECT id, subject, from_address, to_recipients, cc_recipients,
       sent_datetime, internet_message_id, user_id
FROM exchange_sync.messages
WHERE subject = 'Important Update: Change of Email Address'
AND from_address = 'gayane@regima.zone'
ORDER BY received_datetime;
```
