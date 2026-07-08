# Supplementary Founding Affidavit Refinement Report (2026-04-21)

**Source integrated:** `F-supplementary-founding-affidavit.pdf` (9 pages)  
**Repository surface:** `revstream1` with cross-reference implications for `ad-res-j7`

## Executive Summary

A newly received **supplementary founding affidavit** for **Part B of the Notice of Motion** has now been transcribed and integrated into the March 2026 chronology as **EVENT_178**. The affidavit was sworn by **Peter Andrew Faucitt** at **Bedfordview** on **16 March 2026**. Its immediate value is not that it proves the underlying allegations, but that it directly evidences a **new March 2026 litigation layer**: the applicant was pursuing **delinquency-director / probation relief** against the first and second respondents while the contempt sequence was still live.

The document also exposes an important pleading weakness. The opening caption identifies **Regima Worldwide Distribution (Pty) Ltd** as the **third respondent** and **Regima Skin Treatments CC** as the **fourth respondent**, but paragraphs **2.3** and **2.4** of the body reverse those ordinal mappings. That internal inconsistency materially strengthens the repository's existing recommendation that all filing-ready surfaces should use **legal name + entity code + registration number** rather than bare respondent ordinals.

## What the affidavit directly proves

| Proposition | Supported? | Source anchor |
|---|---|---|
| A supplementary founding affidavit for Part B exists | Yes | Page 2 heading |
| The affidavit was sworn on 16 March 2026 at Bedfordview | Yes | Page 9 jurat |
| Part B seeks delinquency-director / probation relief | Yes | Page 6 paragraph 4.2 |
| The applicant says a 19 August 2025 order allowed the filing of the affidavit | Yes | Page 6 paragraph 3.3 |
| The applicant relies on a forensic report marked PF37 | Yes | Page 7 paragraph 5.1 |
| PF37 itself is proved by this affidavit alone | No | Not attached in the present intake |
| The alleged R10,847,862.00 "computer" expenses are proved by this affidavit alone | No | They are only pleaded here |

## Chronology implications

The affidavit sits in a narrow but important window between the **13 March 2026** Rule 30/30A deadline expiry and the **26 March 2026** contempt judgment. This has three practical consequences.

First, the applicant's March 2026 litigation posture was not singular. The case was not only about contempt. It also included an active **Companies Act delinquency / probation** layer. Second, the **16 March 2026** jurat date aligns with the same week later referenced in the contempt judgment as the urgent-enrolment week of **16–20 March 2026**. Third, the affidavit shows that company-control allegations and expense-justification allegations were being escalated at the same time as procedural pressure remained intense.

## Entity-normalization implications

| Surface inside the affidavit | Mapping shown | Risk created |
|---|---|---|
| Caption | 3rd = RWD; 4th = RST | Baseline respondent map |
| Body para 2.3 | 3rd = RST | Internal contradiction |
| Body para 2.4 | 4th = RWD | Internal contradiction |
| Paras 2.5-2.6 | 5th = VVA; 6th = Strategic Logistics | Stable, but depends on earlier numbering clarity |

This inconsistency is significant for both legal drafting and GitHub Pages navigation. Any page that refers only to the "third respondent" or "fourth respondent" without naming the company gives an opponent a clean precision attack. The safest repository practice remains:

> On first mention, always use the legal name, the internal entity code where helpful, and the registration number.

## Red-team consequences already visible from the document

The affidavit creates several foreseeable attack vectors.

1. **Ordinal ambiguity attack:** the respondent side can argue that the pleading itself is internally confused about which company is the third or fourth respondent.
2. **Attachment gap attack:** unless **PF36** and **PF37** are independently exhibited and cross-referenced, the affidavit proves only that the applicant relied on them, not that their contents are accurate.
3. **Accounting-expertise attack:** the pleaded **R10,847,862.00** "computer expenses" figure will attract scrutiny on methodology, source data, accounting period, and classification logic.
4. **Relevance drift attack:** the applicant's shift toward delinquency/probation relief can be portrayed as an attempt to widen the litigation after earlier procedural failures.

## Refinements applied in this cycle

| File | Refinement |
|---|---|
| `docs/events/EVENT_178.md` | New event created for the 16 March 2026 affidavit |
| `docs/timeline.md` | Master timeline updated with EVENT_178 |
| `docs/timeline/phase7_procedural_battle.md` | March 2026 procedural sequence updated |
| `docs/events/index.md` | Judgment-and-appeal stage now includes the new affidavit event |

## Recommended next filing refinements

1. In all March 2026 filing families, replace naked ordinal references to the corporate respondents with **full legal-name references**.
2. Where the **R10,847,862.00** expense allegation is used, explicitly distinguish between **pleaded allegation** and **independently proved accounting fact**.
3. Add a rebuttal paragraph explaining that the affidavit's own numbering inconsistency is why the respondent-side record uses company names and registration numbers for precision.
4. Preserve and, if available, separately integrate **PF36** and **PF37** as direct evidence rather than assuming their content from this affidavit alone.

## Bottom line

The affidavit is important because it adds a **new procedural and substantive layer** to March 2026. It is also important because it gives the case model a concrete drafting vulnerability to neutralise. Properly used, this document strengthens the chronology and improves filing precision. Used carelessly, it would give an opponent a strong attack on internal pleading coherence.
