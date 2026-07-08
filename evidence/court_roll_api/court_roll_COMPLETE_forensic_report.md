# Court Online Complete Forensic Report

**Date:** 15 June 2026  
**Source:** Court Online API (`www.courtonline.judiciary.org.za`)  
**Method:** `POST /api/v1/Invoke` → `GetCourtRoll` operation  
**Locations searched:** Pretoria (Gauteng Division), Johannesburg  
**Period covered:** 1 August 2025 – 31 December 2026  
**Total API calls:** ~322 (36 targeted key dates + 286 forward scan)

---

## Complete Court Roll Appearances — All Streams

### 6 Total Appearances Found

| # | Date | Case Number | Reference | Proceeding Type | Event Title | Location |
|---|------|-------------|-----------|-----------------|-------------|----------|
| 1 | **2025-08-19** | 2025-137857 | KF0019 | Urgent Court | Urgent Applications | Pretoria |
| 2 | **2026-03-17** | 2025-137857 | KF0019 | Urgent Court | Urgent Applications | Pretoria |
| 3 | **2026-05-04** | 2026-034662 | KF0021 | Motion | Motion | Pretoria |
| 4 | **2026-05-26** | 2026-115880 | KF0019 | Urgent Court | Urgent Applications | Pretoria |
| 5 | **2026-06-15** | 2026-034662 | KF0021 | Motion | Motion | Pretoria |
| 6 | **2026-08-12** | 2025-137857 | KF0019 | Motion | **Unopposed Motion** | Pretoria |

---

## Critical Discovery: 12 August 2026 — Unopposed Motion

The forward scan reveals a **future hearing enrolled for 12 August 2026**:

> **Case:** PETER ANDREW FAUCITT v. JACQUELINE FAUCITT # 2025-137857 # KF0019  
> **Proceeding:** Motion  
> **Event Title:** Unopposed Motion

This is significant:

1. **The case has moved from "Urgent Court" to "Motion" roll** — indicating it is no longer being treated as urgent
2. **It is enrolled as "Unopposed"** — meaning either:
   - (a) Peter expects no opposition (perhaps a default judgment application), or
   - (b) The parties have reached agreement on the relief sought, or
   - (c) It is a procedural/housekeeping application (e.g., substituted service, condonation)
3. **The reference remains KF0019** — confirming this is the interdict/contempt stream, not the divorce

### Strategic Implications

- If this is a **delinquency application** (s.162 Companies Act) being brought unopposed, it would suggest Jax has not filed opposition
- If this is a **default judgment** on the interdict, it may relate to the leave to appeal being refused
- The 12 August date gives **~8 weeks** from today to prepare a response if opposition is intended

---

## Consolidated Case Map

### Stream 1: Interdict/Contempt/Delinquency (KF0019)

| Date | Roll Type | Significance |
|------|-----------|--------------|
| 19 Aug 2025 | Urgent Court | Ex parte interdict granted (Kumalo J) |
| 17 Mar 2026 | Urgent Court | Combined hearing — contempt dismissed (Labuschagne J) |
| **12 Aug 2026** | **Unopposed Motion** | **FUTURE — nature TBD** |

### Stream 2: Divorce (KF0021)

| Date | Roll Type | Significance |
|------|-----------|--------------|
| 4 May 2026 | Motion | First enrollment (not 15 Jun as previously thought) |
| 15 Jun 2026 | Motion | Re-enrolled (today) |

### Stream 3: Stock Removal / Reconsideration (KF0019)

| Date | Roll Type | Significance |
|------|-----------|--------------|
| 26 May 2026 | Urgent Court | Stock order granted (Peter's application) |

---

## File Reference Map (Elliott Attorneys)

| Reference | Matters | Case Numbers |
|-----------|---------|--------------|
| **KF0019** | Interdict, contempt, delinquency, stock removal | 2025-137857, 2026-115880 |
| **KF0021** | Divorce | 2026-034662 |

---

## Negative Findings (Equally Important)

| What was NOT found | Implication |
|---|---|
| No appearance for 9 Jun 2026 (reconsideration hearing) | Jax's recon was not on the public roll; may have been a chambers matter |
| No Johannesburg appearances at all | Exclusively Pretoria — WIP drafts citing JHB are wrong |
| No future divorce dates beyond 15 Jun | Divorce may have been postponed or settled |
| No 2026-115880 beyond 26 May | Stock matter concluded or consolidated |
| No appearances Nov–Dec 2026 | Court roll not yet populated for that period |

---

## Methodology

- **API endpoint:** `POST https://www.courtonline.judiciary.org.za/api/v1/Invoke`
- **Operation:** `GetCourtRoll`
- **Authentication:** Token-based (`/api/v1/GetToken` → `RequestVerificationToken` + `RequestVerificationIdentifier` headers)
- **Location format:** GUID (Pretoria: `fd87450c-779d-ec11-a81d-0022481361ac`)
- **Rate limiting:** ~1.5s between calls; connection drops after ~30 rapid requests
- **Coverage:** All weekdays scanned; weekends skipped (courts don't sit)
- **Limitations:** Court roll data appears to be populated ~2–3 months ahead; dates beyond Oct 2026 returned 0 entries or 404

---

## Appendix: All Locations Available

| Location | GUID |
|----------|------|
| Bhisho High Court | f279db57-e149-ef11-a87e-0022481347c4 |
| Bloemfontein High Court | fa6b376a-4959-ef11-a888-0022481345e7 |
| Durban High Court | 16fcd45d-dd49-ef11-a886-0022481345e7 |
| Johannesburg | fb87450c-779d-ec11-a81d-0022481361ac |
| Pretoria | fd87450c-779d-ec11-a81d-0022481361ac |
| Western Cape High Court | 7725345a-1f44-ef11-a87e-0022481347c4 |

*(Full list of 22 locations available via GetLookupDetails API)*
