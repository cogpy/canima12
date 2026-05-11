---
layout: default
title: Leave-to-Appeal Judgment Integration Report - 2026-05-11
---

# Leave-to-Appeal Judgment Integration Report

**Source integrated:** `139F-faucitt-v-faucitt-leave-to-appeal-judgment.pdf`  
**Judgment date:** 4 May 2026  
**Repository integration date:** 11 May 2026  
**Pipeline:** `/identical-transcribe -> /evidence-process(/skillm) -> /ksm-evolve(/regima-org-self) -> /optimal-cognitive-grip`

## Executive Integration Finding

The newly transcribed leave-to-appeal judgment creates a confirmed appellate-outcome event for the contempt litigation sequence. The March 2026 model previously contained a contempt judgment node and a leave-to-appeal notice node; the 4 May 2026 judgment now closes that sequence by confirming that Labuschagne J was not persuaded that there were reasonable prospects of another court reaching a different conclusion or that there was any other compelling reason for an appeal.

## Court Findings Now Available as Direct Evidence

| Issue | Court finding | Model update |
|---|---|---|
| Clause 2.5 | The clause prohibits prejudicial conduct and does not remove all business involvement by Mrs Faucitt. | The relation model should narrow “control/interference” allegations to demonstrable prejudice, not mere presence or participation. |
| Stock and training incidents | The respondent version was accepted; no prejudicial dealing was established. | The event model should mark the operational allegations as court-rejected for leave-to-appeal purposes. |
| Plascon-Evans | The court applied ordinary motion-proceedings principles to disputed facts. | Filing drafts should avoid treating applicant say-so as proof and should foreground objective source records. |
| November 2025 affidavits | Their relevance to the later urgent application was not established. | Recycled affidavit reliance should be flagged as weak unless independently tied to subsequent events. |
| Section 17 threshold | No reasonable prospects and no compelling reason were found. | The leave-to-appeal opposition layer is materially vindicated by the judgment outcome. |
| Costs | Leave to appeal dismissed with Scale C costs, with wasted 16 April costs allocated to Mrs Faucitt. | Costs chronology now needs a nuanced two-part entry. |

## Immediate Repository Updates Made

| Surface | Update |
|---|---|
| Evidence artifacts | PDF and identical Markdown transcription preserved under `docs/evidence/court/judgments/`. |
| Events | Added `EVENT_179` as the 4 May 2026 appellate-outcome node. |
| Timeline | Added the 4 May 2026 row to the judgment and appeal stage. |
| Filings | Added a leave-to-appeal outcome note to the filings index and created a filing-ready status note. |
| ad-res-j7 | Mirrored the source PDF/transcription under `evidence/court-orders/` and added a companion event note. |

## Filing Consequences

The court outcome materially improves the posture of respondent-side civil, regulatory, and cost-recovery materials. It should be used as a **direct judicial finding** that the applicant failed to show breach, wilfulness, reasonable prospects, or compelling reasons. For criminal filings, the judgment is not by itself proof of a criminal offence, but it is strong corroborative evidence that repeated litigation claims concerning the operational incidents were not accepted by the court.

## Recommended Next Iteration

The next refinement pass should update the March 2026 contempt-to-appeal relation cluster, the leave-to-appeal opposition note, and any CourtOnline appeal-response templates so that they distinguish between the pre-outcome opposition posture and the post-judgment closure posture. The key drafting correction is to replace “the opposition should argue” with “the court has now held” wherever the 4 May judgment has resolved the point.

---

*Prepared by Manus AI for repository synchronization on 2026-05-11.*
