# Supplementary Founding Affidavit Red-Team Critique (2026-04-21)

**Applies to:** Part B delinquency-director / probation narrative, civil-response architecture, CIPC-facing company-law analysis, commercial-crime framing, tax-fraud framing, and any filing that cites the new **16 March 2026** supplementary founding affidavit.  
**Primary source under test:** `F-supplementary-founding-affidavit.pdf` / [EVENT_178](../events/EVENT_178.md)

## Executive Summary

The newly integrated supplementary founding affidavit is useful chronology evidence, but it also gives an opponent several clean attack lines if it is used carelessly. The affidavit proves that **Peter Andrew Faucitt** swore a **Part B** affidavit on **16 March 2026** and that he advanced a **delinquency-director / probation** case supported by a referenced forensic report (**PF37**). It does **not**, by itself, prove the truth of the accounting allegations in that report.

The strongest adversarial point is the affidavit's own **internal respondent-number instability**. The caption identifies **Regima Worldwide Distribution (Pty) Ltd** as the **third respondent** and **Regima Skin Treatments CC** as the **fourth respondent**, but the body reverses those ordinal assignments in paragraphs **2.3** and **2.4**. If later filings import those ordinals without legal-name normalization, the defence can argue that the applicant's own pleading is internally confused about the corporate subjects of the allegations.

## Attack Surface 1: Internal respondent-number contradiction

### Red-team critique

The defence will argue that the affidavit is materially unreliable on company identity because it cannot keep the third and fourth respondents straight within the same document.

### Why it matters

This attack is especially dangerous wherever the filing alleges company-specific misconduct, account depletion, tax exposure, or director/member misconduct. A court or regulator does not need to decide the whole case to be troubled by ambiguity on which company is being discussed.

### Evidence anchor

| Location in affidavit | What it says |
|---|---|
| Caption pages | 3rd = Regima Worldwide Distribution (Pty) Ltd; 4th = Regima Skin Treatments CC |
| Para 2.3 | 3rd = Regima Skin Treatments CC |
| Para 2.4 | 4th = Regima Worldwide Distribution (Pty) Ltd |

## Attack Surface 2: PF36 / PF37 dependency gap

### Red-team critique

The defence will argue that the affidavit relies on annexures **PF36** and **PF37** but that the present filing surface does not yet independently prove the contents of those annexures. On that basis, they will say the affidavit proves only that the applicant **made** the allegations, not that the allegations are true.

### Why it matters

This is a classic attachment-gap problem. It can be used to weaken not only the Part B narrative, but also any downstream attempt to treat the **R10,847,862.00** figure as if it were already verified accounting fact.

### Safe conclusion

The affidavit is direct proof of **reliance on PF36/PF37**, but not yet direct proof of the annexures' underlying truth.

## Attack Surface 3: Accounting-methodology challenge

### Red-team critique

The defence will target the alleged **R10,847,862.00** in "computer" expenses by asking:

1. what date range was used;
2. what ledger codes were included;
3. whether the category was stable across years;
4. whether duplication or misclassification was independently tested;
5. and whether turnover/profit comparisons were normalized across entities.

### Why it matters

A single large accounting number attracts scrutiny. If used as a headline accusation without methodological guardrails, it gives the defence a route to characterize the broader case as speculative or sensational.

## Attack Surface 4: Litigation-overreach framing

### Red-team critique

The defence will argue that by March 2026 the applicant was layering **interdict**, **contempt**, and **delinquency-director / probation** theories onto the same business-family conflict, thereby turning the proceedings into an overloaded advocacy campaign rather than a disciplined legal case.

### Why it matters

This argument does not require the defence to disprove every allegation. It only needs to persuade the audience that the procedural spread signals overreach.

## Filing-family specific red-team pressure

| Filing family | Most likely attack using the affidavit |
|---|---|
| Civil / answering architecture | The applicant's own corporate-identity mapping is unstable. |
| CIPC / Companies Act | The alleged delinquency case is undercut if the corporate respondents are not named consistently. |
| Commercial crime | The headline accounting number is unverified and methodologically opaque. |
| SARS / tax fraud | Expense allegations cannot simply be imported from a pleading without ledger-level support. |
| POPIA | Limited direct relevance unless linked to identity misuse or systems abuse elsewhere. |

## What must not be overstated

1. Do **not** say the affidavit proves the **PF37** forensic conclusions unless PF37 itself is independently in evidence.
2. Do **not** rely on bare references to the "third respondent" or "fourth respondent" when discussing this document.
3. Do **not** treat the March 2026 affidavit as if it collapses the distinction between the **Part B** delinquency theory and the separate **contempt** track.
4. Do **not** convert pleaded suspicions about duplicate payments into final findings unless separate accounting evidence supports that move.

## Bottom-line red-team conclusion

The affidavit is valuable as **chronology evidence** and as a record of the applicant's March 2026 litigation theory. It is dangerous if used as a shortcut for proving the underlying accounting allegations. The defence's best move is to attack **identity precision**, **annexure proof**, **methodology**, and **procedural overreach**. Any response layer must therefore neutralize those four points explicitly.
