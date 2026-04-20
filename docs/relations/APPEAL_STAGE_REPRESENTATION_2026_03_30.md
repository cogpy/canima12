# Appeal-Stage Representation Mapping — 30 March 2026

**Last Updated:** 2026-04-20

## Purpose

This relation page records the legal-representation posture evidenced by the **Notice of Application for Leave to Appeal** dated 30 March 2026 in Case 2025/137857.

## Core Representation Edges

| From | Relation | To | Evidence |
|---|---|---|---|
| [Peter Andrew Faucitt](../entities/PERSON_001.md) | represented_by | [ORG_020: Elliott Attorneys Inc](../entities/ORG_020.md) | KF0019 Leave to Appeal Notice |
| [Jacqueline Faucitt](../entities/PERSON_004.md) | represented_on_service_by | [ORG_031: Burger Huyser Attorneys – Bedfordview Inc](../entities/ORG_031.md) | KF0019 Leave to Appeal Notice |
| [Daniel James Faucitt](../entities/PERSON_005.md) | aligned_respondent_with | [Jacqueline Faucitt](../entities/PERSON_004.md) | Case caption in Leave to Appeal Notice |
| [ORG_020: Elliott Attorneys Inc](../entities/ORG_020.md) | serves_appeal_notice_on | [ORG_031: Burger Huyser Attorneys – Bedfordview Inc](../entities/ORG_031.md) | Service block in Leave to Appeal Notice |
| [ORG_019: Pottas Attorneys](../entities/ORG_019.md) | earlier_documented_as | respondent-side legal representative | Existing contempt-sequence records |
| [ORG_031: Burger Huyser Attorneys – Bedfordview Inc](../entities/ORG_031.md) | later_visible_as | respondent-side legal representative | Leave to Appeal Notice |

## Why This Relation Matters

The case repositories previously emphasized **Pottas Attorneys** in the contempt sequence. The appeal notice adds a new procedural data point showing **Burger Huyser Attorneys – Bedfordview Inc** in the respondent service block. Even if the full substitution history still needs independent reconstruction, the new evidence is sufficient to refine the relation model from a single-firm snapshot into a time-sensitive representation sequence.

## Caution

This page does **not** infer the exact date of mandate substitution. It only records what the filing visibly proves on **30 March 2026**.

## Evidence

- `evidence_documents/KF0019-NoticeofApplicationforLeavetoAppeal-2026-03-30.pdf`
- `evidence_documents/KF0019-NoticeofApplicationforLeavetoAppeal-2026-03-30_PAGE1_TRANSCRIPTION.md`
