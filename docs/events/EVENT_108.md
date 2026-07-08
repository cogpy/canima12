# EVENT_108: Faucitt Trust Meeting Coordination — Rynette as Gatekeeper

## Event Metadata
- **Type:** Unknown
- **Entities Involved:** Unknown
- **Source:** Unknown


**Event ID:** EVENT_108  
**Date:** 2023-05-03 to 2023-05-31  
**Category:** Trust Manipulation / Information Gatekeeping  
**Severity:** HIGH  
**Status:** CONFIRMED — Email evidence in Neon database

## Summary

In May 2023, a series of emails reveals Rynette Farrar acting as the **sole intermediary** between Bantjies and Peter regarding Faucitt Family Trust matters. Rynette coordinated the signing of amended trustees meeting minutes and arranged a trust meeting with attorney Denny Da Silva — all while **excluding Jax and Daniel** from communications. When Jax discovered the exclusion, she objected, revealing the pattern of information gatekeeping.

## Email Evidence Chain

### Phase 1: Trustees Meeting Minutes (3 May 2023)

**Email 1:** Jax asks Bantjies to send signature pages to Rynette
- **Date:** 2023-05-03T06:22:48Z
- **From:** jax@regima.zone (Jacqui Faucitt)
- **Subject:** RE: 5079150_v(1)_MINUTES OF A TRUSTEES MEETING OF THE FAUCITT TRUST amended

> "Hi Danie. My scanner is still not working as most of the staff have been on leave with all the public holidays. Please can I ask you to send the couple of pages that need signature through to Rynette and Pete can collect and sign them."

**Email 2:** Bantjies sends to Rynette directly
- **Date:** 2023-05-03T07:22:58Z
- **From:** danieb@thegeorgegroup.co.za (Danie Bantjes)
- **To:** rynette@regima.zone
- **Subject:** FW: 5079150_v(1)_MINUTES OF A TRUSTEES MEETING OF THE FAUCITT TRUST amended

> "Hi Rynette. Please could you print this document for Pete and Jaqui to sign and then scan back to me urgently."

**Email 3:** Rynette returns signed documents
- **Date:** 2023-05-03T13:47:00Z
- **From:** rynette@regima.zone (Rynette Farrar)

> "Hi Danie. Aangeheg is die getekende minutes of meeting." (Attached are the signed minutes of meeting.)

### Phase 2: Trust Meeting Arrangement (29-31 May 2023)

**Email 4:** Rynette arranges meeting — excludes Jax and Daniel
- **Date:** 2023-05-29T08:34:00Z
- **From:** rynette@regima.zone (Rynette Farrar)
- **To:** danie.bantjes@gmail.com
- **Subject:** Meeting re Faucitt Trust

> "Good morning Danie. Pete say a meeting tomorrow at 1pm with Denny Da Silva will be fine."

**Email 5:** Bantjies postpones
- **Date:** 2023-05-29T12:05:18Z
- **From:** danie.bantjes@gmail.com

> "Can we move this meeting to next week please? The month end over here at the new company is proving to be a handful!"

**Email 6:** Rynette confirms rescheduled meeting
- **Date:** 2023-05-30T12:47:00Z
- **From:** rynette@regima.zone

> "Pete is good with next Wednesday at 14H00."

**Email 7:** Jax discovers exclusion and objects
- **Date:** 2023-05-31T07:13:05Z
- **From:** jax@regima.zone (Jacqui Faucitt)

> "Rynette, Pete cannot do next Wednesday as it is my birthday. He should have copied me in on the mail as it is the Faucitt Family Trust, ha ha, and I could have told him. **Please ask him to always copy me and Danny**"

## Critical Analysis

### Information Gatekeeping Pattern
1. Rynette communicates with Bantjies about trust matters **without copying beneficiaries**
2. Rynette relays Pete's instructions to Bantjies — Pete does not communicate directly
3. Jax and Daniel are systematically excluded from trust communications
4. When caught, Jax has to explicitly request inclusion: "Please ask him to always copy me and Danny"

### Attorney Involvement: Denny Da Silva
- The meeting was arranged with attorney **Denny Da Silva** regarding the Faucitt Trust
- This is significant because it shows legal advice was being sought about the trust in May 2023
- The trust amendment with the forged "pp Peter" signature came 13 months later (28 June 2024)

### Rynette's Role as Document Handler
- Rynette printed, obtained signatures, scanned, and returned trust documents
- This gave her physical access to trust documents and signature pages
- This access was later exploited when she forged "pp Peter" on the trust amendment (EVENT_103)

### Timeline to Forgery

| Date | Event | Months Before Forgery |
|---|---|---|
| **2023-05-03** | Rynette handles trust meeting minutes signatures | **13 months** |
| **2023-05-29** | Rynette arranges trust meeting with attorney | **13 months** |
| **2023-08-31** | Xenophontos attorneys send trust correspondence | **10 months** |
| **2024-04-26** | Rynette logs into SARS as Bantjies (EVENT_107) | **2 months** |
| **2024-06-28** | Rynette forges "pp Peter" on trust amendment | **0** |

## Cross-References

- **EVENT_103:** Trust Amendment Forgery (28 June 2024)
- **EVENT_107:** Rynette Logs Into SARS as Bantjies (26 April 2024)
- **PERSON_002:** Rynette Farrar — gatekeeper and document handler
- **PERSON_007:** Danie Bantjies — coordinated with Rynette on trust matters

## Evidence Location

- **Neon Database:** exchange_sync.messages
  - subject ILIKE '%TRUSTEES MEETING%FAUCITT%' (May 3, 2023)
  - subject ILIKE '%Meeting re Faucitt Trust%' (May 29-31, 2023)
  - subject = 'Faucitt Family Trust' (Aug 31, 2023)
