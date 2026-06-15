# Court Online Forensic Search Report

**Date:** 15 June 2026  
**Source:** Court Online API (`www.courtonline.judiciary.org.za`)  
**Method:** `/api/v1/Invoke` → `GetCourtRoll` operation  
**Locations searched:** Pretoria (Gauteng Division), Johannesburg  
**Period:** 1 August 2025 – 16 June 2026  
**Key dates probed:** 36 (Pretoria) + 5 (Johannesburg)

---

## Critical Findings

### 5 Court Roll Appearances Found

| # | Date | Case Number | Reference | Proceeding | Court Room | Location |
|---|------|-------------|-----------|------------|------------|----------|
| 1 | **2025-08-19** | 2025-137857 | KF0019 | Urgent Court | — | Pretoria |
| 2 | **2026-03-17** | 2025-137857 | KF0019 | Urgent Court | — | Pretoria |
| 3 | **2026-05-04** | **2026-034662** | **KF0021** | Motion | — | Pretoria |
| 4 | **2026-05-26** | **2026-115880** | KF0019 | Urgent Court | — | Pretoria |
| 5 | **2026-06-15** | **2026-034662** | **KF0021** | Motion | — | Pretoria |

---

## Key Discoveries

### 1. Case 2026-034662 (Divorce) — NEW REFERENCE: KF0021

The divorce matter uses a **different Elliott file reference: KF0021** (not KF0019).

- **KF0019** = the interdict/contempt/stock stream (2025-137857 and 2026-115880)
- **KF0021** = the divorce stream (2026-034662)

This confirms Elliott Attorneys maintains **two separate files** for the Faucitt matters.

### 2. Case 2026-034662 — First Court Appearance: 4 May 2026

The divorce was **enrolled on the motion roll as early as 4 May 2026** (not just 15 June). This is the first court roll appearance. It appears again today (15 June 2026) — confirming the June filing analysis that the divorce is enrolled today.

### 3. Case 2026-115880 — CONFIRMED as Stock/Urgent Application

The court roll confirms 2026-115880 appeared on **26 May 2026** as an **"Urgent Court"** proceeding with reference **KF0019**. This is the stock-removal order date.

**Critical resolution:** The reconsideration (Jax, Lerena Attorneys) was e-issued on 25 May under 2026-115880 but does NOT appear on the court roll for 9 June (the hearing date). This suggests either:
- (a) The reconsideration was enrolled under a different mechanism (not the daily roll), or
- (b) It was struck before being formally enrolled on the roll, or
- (c) The court roll data for 9 June is incomplete.

The **stock order** (Peter, KF0019) IS on the roll for 26 May — confirming it was Peter's application under KF0019, not Jax's.

### 4. No Johannesburg Appearances

Zero matches in Johannesburg across all checked dates. The matter is **exclusively Pretoria** — corrects the WIP drafts that incorrectly stated "Johannesburg".

### 5. Court Roll Classification

| Case | Proceeding Type | Implication |
|------|----------------|-------------|
| 2025-137857 | **Urgent Court** | Enrolled on the urgent roll (not motion roll) |
| 2026-034662 | **Motion** | Enrolled on the ordinary motion roll |
| 2026-115880 | **Urgent Court** | Enrolled on the urgent roll |

---

## Case Number Collision — PARTIALLY RESOLVED

The collision between Jax's reconsideration and Peter's stock order under 2026-115880 is now **partially resolved**:

- **Peter's stock application** (KF0019) appears on the court roll for 26 May 2026 under 2026-115880 as "Urgent Court"
- **Jax's reconsideration** (Lerena) does NOT appear on the roll for 9 June (the hearing date)

**Working hypothesis:** 2026-115880 was originally Peter's stock-removal case number. Jax's reconsideration was brought as a counter-application or linked application within the same case number (common for related urgent applications). The reconsideration hearing on 9 June may have been enrolled under the main number 2025-137857 or was a chambers matter not on the public roll.

---

## Timeline Corrections Required

| Previous Understanding | Corrected by Court Roll |
|---|---|
| KF0019 covers all Faucitt matters | KF0019 = interdict/stock; **KF0021 = divorce** |
| Divorce enrolled 15 Jun 2026 (first appearance) | First appearance was **4 May 2026** (motion roll) |
| 2026-115880 = reconsideration (Jax) | 2026-115880 = **Peter's stock application** (KF0019, Urgent); Jax's recon is linked |
| Division possibly Johannesburg | **Exclusively Pretoria** — zero JHB appearances |
| Reconsideration hearing 9 Jun on roll | **NOT on the public roll** for 9 Jun |

---

## Raw Data

```json
{
  "appearances": [
    {
      "date": "2025-08-19",
      "Case": "PETER ANDREW FAUCITT  v. JACQUELINE  FAUCITT # 2025-137857 # KF0019",
      "Proceeding": "Urgent Court",
      "CourtRoom": null
    },
    {
      "date": "2026-03-17",
      "Case": "PETER ANDREW FAUCITT  v. JACQUELINE  FAUCITT # 2025-137857 # KF0019",
      "Proceeding": "Urgent Court",
      "CourtRoom": null
    },
    {
      "date": "2026-05-04",
      "Case": "PETER ANDREW FAUCITT  v. JACQUELINE  FAUCITT # 2026-034662 # KF0021",
      "Proceeding": "Motion",
      "CourtRoom": null
    },
    {
      "date": "2026-05-26",
      "Case": "PETER ANDREW FAUCITT  v. JACQUELINE  FAUCITT # 2026-115880 # KF0019",
      "Proceeding": "Urgent Court",
      "CourtRoom": null
    },
    {
      "date": "2026-06-15",
      "Case": "PETER ANDREW FAUCITT  v. JACQUELINE  FAUCITT # 2026-034662 # KF0021",
      "Proceeding": "Motion",
      "CourtRoom": null
    }
  ]
}
```

---

## Methodology Notes

- The Court Online API uses a dispatch pattern: `POST /api/v1/Invoke` with `GetCourtRoll` operation
- Location must be passed as a GUID (not name); other fields must be empty strings (not "string")
- The API returns all cases enrolled for a given date at a given location
- Rate limiting disconnects after ~30 rapid requests; 2-second delays between calls are stable
- The `minDate: new Date()` restriction in the UI is client-side only; the API accepts historical dates
- Some dates return HTTP 400/404 (likely public holidays or non-sitting days)
