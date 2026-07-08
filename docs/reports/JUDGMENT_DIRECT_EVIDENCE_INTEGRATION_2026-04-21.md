# Direct Judgment Evidence Integration — 26 March 2026 Contempt Judgment

**Case:** 2025/137857  
**Court:** High Court of South Africa, Gauteng Division, Pretoria  
**Judge:** Labuschagne J  
**Integration date:** 2026-04-21  
**Primary sources:** `evidence_documents/LABUSCHAGNE_CONTEMPT_JUDGMENT_2026-03-26.pdf`; `evidence_documents/LABUSCHAGNE_CONTEMPT_JUDGMENT_2026-03-26_TRANSCRIPTION.md`

## Executive Summary

The repository previously modeled the **26 March 2026 contempt judgment** indirectly from the later **30 March 2026 leave-to-appeal notice**. The direct judgment now closes that evidence gap. It confirms, expressly and not inferentially, that the contempt application failed, that the court found the applicant had **not established breach or wilfulness**, and that the matter warranted a **punitive costs order on the attorney-and-client scale**.

The judgment materially strengthens the respondent-side chronology in three ways. First, it anchors the appellate layer to the court's own reasoning rather than to an applicant-side characterization of that reasoning. Second, it sharpens the distinction between **business conflict** and **proven contempt**, especially in relation to stock control, training attendance, and operational authority. Third, it gives direct judicial language for resisting any attempt to convert disputed management interactions into quasi-criminal contempt findings.

## Direct Findings Confirmed by the Judgment

| Issue | Direct finding from judgment | Repository impact |
|---|---|---|
| Procedural outcome | The contempt application failed | Confirms EVENT_176 as an adverse first-instance outcome for the applicant |
| Burden of proof | Applicant had to establish contempt beyond reasonable doubt in motion proceedings | Strengthens appellate rebuttal and contempt-opposition language |
| Clause 2.5 | The court treated clause 2.5 as the operative paragraph of the 19 Aug 2025 order | Supports narrower, text-based interpretation analysis |
| Stock incidents | The court accepted that the evidence did not show disruption of stocktake or delivery by the first respondent | Weakens applicant's practical-control theory |
| Training incidents | The court accepted the respondent version as showing supervision / operational role rather than proved contempt | Supports management-dispute framing |
| Witnesses | Affidavits by Mr Mphande and Mr Tshabalala supported the respondent version | Elevates corroboration value of those witnesses |
| Costs | Punitive costs were expressly justified by repeated urgent relief that could not be substantiated | Strengthens abuse-of-process / escalation critique |
| Divorce linkage | Court recorded that contempt proceedings appeared to bolster the applicant's forfeiture claim in the divorce | Strengthens motive and legal-weaponisation framing |

## Clause 2.5 Anchor

The judgment records the relevant paragraph of the 19 August 2025 order as follows:

> "2.5 The first and second respondents are interdicted and restrained from dealing with the business (and the administration thereof) of the third to sixth respondents, and/or their employees, and/or their partners, and/or their clientele, in any manner in which any may sustain any prejudice."

This wording matters because any contempt case still had to prove, with precision, that a specific act fell within this prohibition, that the prohibition was sufficiently clear for penal consequences, and that the conduct was wilful.

## Event-Level Refinements Required

| Event | Refinement now justified by direct evidence |
|---|---|
| `EVENT_176` | Upgrade source base from inferred appeal-notice reconstruction to direct judgment evidence |
| 2026-03-26 master timeline entry | Replace leave-to-appeal-only sourcing with direct judgment source |
| phase7 procedural timeline entry | Same upgrade; note attorney-client punitive costs expressly |
| appellate critique layer | Remove the open evidence-gap status for the full judgment and replace it with judgment-anchored analysis |

## Entity and Relation Implications

No new core perpetrator entity is created by the judgment, but the document clarifies role usage and should tighten how several existing entities are referenced.

| Entity / role | Judgment contribution |
|---|---|
| Peter Andrew Faucitt | Applicant in failed contempt application; judicial criticism tied to repeated urgent relief and forfeiture context |
| Jacqueline Faucitt | First respondent whose version the court did not reject on paper; central to stock/training incident analysis |
| Daniel James Faucitt | Second respondent listed in the caption and in clause 2.5 scope |
| Regima Worldwide Distribution (Pty) Ltd / Regima Skin Treatments CC / Villa Via Arcadia No. 2 CC / Strategic Logistics CC | Confirmed as the third to sixth respondents in the business-control prohibition layer |
| Elliott Attorneys Inc | Applicant-side attorneys tied to the failed contempt push and subsequent appeal step |
| Mr Mphande / Mr Tshabalala / Ms Farrar / Ms Gayane Williams / Cherie Smith | Witness and operational participants whose roles should be cross-linked more explicitly in event narratives |

## Timeline Consequences

The direct judgment makes the March 2026 sequence more precise:

| Date | Event | Why it matters |
|---|---|---|
| 2026-02-09 | Contempt application launched on the papers later sought to be enrolled urgently | Anchors the exact application date cited by the court |
| 2026-03-16 to 2026-03-20 week | Urgent enrolment effort | Confirms the judgment was addressing urgent enrolment of the contempt matter |
| 2026-03-26 | Contempt application dismissed with punitive costs | Now directly evidenced |
| 2026-03-30 | Leave-to-appeal notice filed | Clearly follows a merits defeat already described by the court |

## Filing and Red-Team Consequences

The direct judgment defeats several loopholes previously available to the applicant-side appeal framing.

1. The applicant can no longer characterize the first-instance outcome only through the leave-to-appeal notice. The court itself recorded that **neither breach nor wilfulness had been established**.
2. The stock and training allegations must now be answered against the court's direct factual treatment, not against abstract appellate complaint language.
3. The punitive-costs issue can now be defended by citing the court's own concern that repeated urgent applications were being used to advance the applicant's divorce-forfeiture posture.
4. Any future respondent-side filing should emphasize that the judgment treated the matter as an evidential failure, not merely as a procedural technicality.

## Recommended Documentation Actions

1. Update `docs/events/EVENT_176.md` to cite the direct judgment PDF and transcription.
2. Update `docs/timeline.md` and `docs/timeline/phase7_procedural_battle.md` to record the direct judgment source and attorney-client punitive costs.
3. Update `docs/filings/APPEAL_RED_TEAM_CRITIQUE_2026-04-20.md` to close the "full judgment missing" evidence gap.
4. Update `docs/filings/APPEAL_REBUTTAL_ADDENDUM_2026-04-20.md` so the rebuttal matrix quotes the actual judgment findings.
5. Surface this report on the main GitHub Pages landing pages in both `revstream1` and `ad-res-j7`.

## Bottom Line

The newly transcribed judgment does not merely add another document. It converts an **inferred appellate-stage model** into a **directly evidenced first-instance judicial model**. That strengthens the event layer, improves timeline integrity, sharpens red-team critique, and materially improves the respondent-side ability to defeat appellate mischaracterization with the court's own words.
