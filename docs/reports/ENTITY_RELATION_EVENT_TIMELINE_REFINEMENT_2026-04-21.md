**Date:** 2026-04-21  
**Scope:** `revstream1` with cross-reference to `ad-res-j7` and the shared case workspace  
**Purpose:** Refine the live GitHub Pages case model after the 2026-04-20 appeal layer by tightening canonical entity usage, improving relation pages, extending the phase timeline, and recording evidence-intake discipline for newly received material.

## Executive Summary

The 2026-04-20 appeal-stage refresh substantially improved the live `revstream1` surface, but four issues remained material on 2026-04-21. First, the public documentation still needed a more explicit **account-to-entity normalization layer** grounded in the verified FNB/CIPC mapping now available in the shared workspace. Second, the **June 2025 retaliation cluster** and the **August 2025 procedural control-seizure cluster** were not equally mature as cross-reference pages, which made the chronology more difficult to traverse from GitHub Pages. Third, the phase timeline page lagged behind the master timeline by omitting the **26 March 2026 contempt judgment** and the **30 March 2026 leave-to-appeal notice**. Fourth, a newly received **Johannesburg opposed-summary-judgment court-roll PDF** required disciplined treatment: preserve it, transcribe it, and only integrate it into the event layer if a party-linked relevance showing exists.

The immediate refinement actions taken in this cycle are therefore intentionally conservative. Rather than inflating the event model, the cycle strengthens **reference discipline**, **cluster visibility**, and **evidence-intake hygiene**.

## Concrete Refinements Applied on 2026-04-21

| Surface | Action taken | Effect |
|---|---|---|
| `docs/relations/COORDINATED_RETALIATION.md` | Rewritten with a fuller 5–20 June 2025 chronology | Makes the retaliation chain easier to cite across civil, criminal, POPIA, and tax narratives |
| `docs/relations/PROCEDURAL_CONTROL_SEIZURE_CLUSTER_2025-08.md` | New relation note created | Fills the missing GitHub Pages bridge between August backdating / affidavit / filing / order events and later extraction prejudice |
| `docs/timeline/phase7_procedural_battle.md` | Added 26 Mar 2026 judgment and 30 Mar 2026 leave-to-appeal entries | Synchronizes the phase view more closely with the master timeline |
| `docs/timeline/phase7_procedural_battle.md` | Added April 2026 evidence-intake note for the external court-roll PDF | Preserves newly received material without chronology inflation |

## Canonical Entity and Account Normalization Notes

The shared `ACCOUNT_REFERENCE.md` materially strengthens the identity layer because it ties **account numbers**, **entity codes**, **legal names**, and **CIPC formats** together from verified sources. Even where these details are not yet copied into every entity page, the following canonical normalizations should now guide all future filing and timeline language.

| Entity code | Canonical legal name | Key account / registration note | Why this matters |
|---|---|---|---|
| `RWD` | Regima Worldwide Distribution (Pty) Ltd | CIPC 2011/005722/07; FNB 62323196362 and 62836164880 | Core victim-stream entity in the extraction narrative |
| `RST` | Regima Skin Treatments CC | CIPC 1992/005371/23; VAT 4590131043; multiple FNB/CFC accounts | Important for VAT/tax, trading history, and post-order extraction prejudice |
| `SLG` | Strategic Logistics CC | CIPC 2008/136496/23; FNB 62432501494 and 62593375829 | Crucial to the inter-company, stock, and control narrative |
| `RSA` | Regima SA (Pty) Ltd | CIPC 2017/087935/07; FNB 62707308252 plus trust/call accounts | Prevents drift between operating references and formal legal-company references |
| `REZ` | Rezonance (Pty) Ltd | CIPC 2017/081396/07; FNB 62707312310 and 62826022577 | Relevant to infrastructure, Sage, and governance context |
| `VVA` | Villa Via Arcadia No 2 CC | CIPC 1996/004451/23; VAT 4790157558 | Central to the June 2025 fraud-exposure trigger sequence |
| `RZI` | Regima Zone Impact (Pty) Ltd | CIPC 2017/109415/07 | Important when mapping the wider entity perimeter |
| `RZA` | Regima Zone Academy (Pty) Ltd | CIPC 2017/113134/07 | Same |

### Immediate entity-discipline recommendation

Future filing revisions should prefer the **legal-name + entity-code + CIPC-format** combination on first mention, especially when dealing with bank-control events, extraction schedules, and SARS/CIPC-facing complaints. This will reduce the risk that a respondent attack reframes the case as loose trading-style nomenclature rather than entity-specific misconduct.

## Relation-Layer Findings

The relation layer is now materially stronger in two places.

### 1. June 2025 retaliation cluster

The updated retaliation page now presents a more disciplined chain:

1. suspicious accounting material reaches Daniel;
2. Daniel reports fraud;
3. cards are cancelled within about 24 hours;
4. FNB mandate and card-replacement issues are escalated;
5. Linda's 39+ bank-detail change emails and the domain/email displacement sequence follow.

This is useful because it turns a loose list of grievances into a **coherent post-exposure retaliation narrative**.

### 2. August 2025 procedural control-seizure cluster

The new August cluster page closes a prior navigation gap by tying together:

- the **11 August 2025** backdated authority step,
- the **13 August 2025** confirmatory affidavit,
- the **14 August 2025** Court Online filing step,
- the **19 August 2025** ex parte order,
- and the **26 August–11 September 2025** downstream extraction window.

This matters because the case is strongest when August is framed as the **procedural bridge** between prior control misconduct and later extraction prejudice.

## Event and Timeline Findings

### Phase-timeline synchronization

The dedicated phase timeline had fallen behind the master timeline by omitting the **26 March 2026 judgment** and **30 March 2026 leave-to-appeal** events. Those two entries have now been inserted. This is a small but important fix because GitHub Pages users often navigate through the shorter phase timeline before they reach the full master chronology.

### External court-roll evidence discipline

A newly received PDF — the **14–17 April 2026 Johannesburg Opposed Summary Judgement Court Roll** — has been transcribed identically for preservation. However, the visible matter names on the roll do not presently match the core parties of Case 2025-137857. The event model therefore records it only as an **evidence-intake note**, not as a substantive case event. This is the correct move under a strict chronology discipline.

> **Rule applied:** preserve first, integrate only after relevance is shown.

## Timeline-Driven Improvement Priorities for the Next Pass

| Priority | Why the timeline makes it important | Improvement direction |
|---|---|---|
| Extraction-after-order schedule | The September 2025 prejudice case remains one of the strongest damages anchors | Build a compact account-linked extraction schedule using the normalized FNB entity mapping |
| Entity-first bank-control references | June and September events repeatedly touch bank mandates and accounts | Add first-mention legal names, entity codes, and account references in filings where money movement is alleged |
| Court-process atomization | August 2025 and March 2026 remain vulnerable to date-collapsing attacks | Keep creation, signature, oath, filing, order, judgment, and appeal dates distinct in every filing family |
| Independent-institution anchors | FNB, CIPC, SARS, law-firm, and court-origin documents carry the most weight | Continue moving narrative claims behind documentary anchors |
| ad-res-j7 / revstream1 surface synchronization | `revstream1` is now materially ahead as a live filing surface | Update `ad-res-j7/docs/index.md` and related landing pages so users are not left on older v20-era summaries |

## Filing Implications

| Filing family | Practical consequence of this refinement cycle |
|---|---|
| Civil action | Stronger causation pathway from fraud exposure to retaliation to extraction |
| Commercial crime / NPA | Better sequencing of exposure, retaliation, procedural weaponization, and extraction |
| CIPC complaint | Clearer use of legal company identity and trust/company control overlap |
| POPIA | Better tie between access misuse, bank-detail redirection, and infrastructure displacement |
| SARS / tax fraud | Cleaner bridge between account-control irregularities and entity-specific consequences |
| Void ab initio / contempt | Better atomization of August 2025 and March 2026 process steps |

## Suggested Next Documentation Actions

1. Update the main `docs/index.md` and `docs/filings/index.md` pages to surface the new 2026-04-21 refinement report and the August control-seizure relation page.
2. Add a short extraction schedule page that maps the **26 August–11 September 2025** payments to normalized entity/account references from the shared workspace.
3. Refresh `ad-res-j7/docs/index.md` so its public navigation points more explicitly to the current `revstream1` live filing surface and no longer leaves the user on an older v20 framing.
4. In the next filing pass, incorporate first-mention account/entity normalization wherever specific company bank accounts are alleged to have been used or depleted.

## Conclusion

The strongest improvement on 2026-04-21 is not raw volume. It is **control of the chronology surface**. The case model is most persuasive when it presents a disciplined progression: motive, preparation, exposure, retaliation, procedural weaponization, extraction, judgment, and appeal. The current cycle therefore improves the public evidentiary architecture by tightening the June and August clusters, synchronizing the March 2026 appeal-stage events, and preserving new material without overstating its relevance.
