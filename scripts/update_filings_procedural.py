import os

PROCEDURAL_TEXT = """
## Procedural Hierarchy for Setting Aside Ex Parte Interdicts

The granting of an *ex parte* interdict is a drastic departure from the fundamental legal principle of *audi alteram partem*. The law imposes strict duties on the applicant and provides robust mechanisms for the respondent to challenge the order.

### 1. The Foundational Principle: Uberrima Fides
In *ex parte* applications, the applicant bears a duty of utmost good faith (*uberrima fides*). They must place all material facts before the court. As established in *Schlesinger v Schlesinger* 1979 (4) SA 342 (W):
1. All material facts must be disclosed which might influence a Court.
2. Non-disclosure need not be wilful or mala fide to incur the penalty of rescission.
3. The Court has a discretion to set aside the former order.

When non-disclosure rises to deliberate perjury with provable foreknowledge, fraud vitiates the entire proceeding (*fraus omnia corrumpit*).

### 2. The Five-Tier Procedural Hierarchy

**Tier 1: Rule 6(12)(c) Reconsideration (The Primary Remedy)**
Any person against whom an order was granted *ex parte* in an urgent application may set the matter down for reconsideration upon no less than 24 hours' notice. This is a *de novo* hearing where the court considers the matter afresh. It applies to both interim and final orders.

**Tier 2: Rule 6(8) Anticipation of the Return Day**
Allows any person against whom an order is granted *ex parte* to anticipate the return day upon 24 hours' notice. This applies **only** to interim orders (rules *nisi*) that have a scheduled return date.

**Tier 3: Rule 42(1)(a) Rescission**
Empowers a court to rescind or vary an order "erroneously sought or erroneously granted in the absence of any party affected thereby". A material non-disclosure renders the order "erroneously sought". No need to show "good cause" or a *bona fide* defence.

**Tier 4: Common Law Rescission for Fraud**
If obtained through deliberate perjury or fraud, the respondent may seek rescission under the common law (*Childerley Estate Stores v Standard Bank*). Not subject to strict time limits. Proven fraud vitiates the entire proceeding, rendering the order a nullity from its inception.

**Tier 5: Section 173 Inherent Jurisdiction**
The High Courts have the inherent power to protect and regulate their own process. This is a residual mechanism used when other remedies are procedurally unavailable or inadequate to prevent a grave injustice.
"""

filepath = '/home/ubuntu/revstream1/docs/filings/CIVIL_CONTEMPT_ANALYSIS_2026_02_09.md'
with open(filepath, 'r') as f:
    content = f.read()

if 'Procedural Hierarchy' not in content:
    content += '\n\n' + PROCEDURAL_TEXT
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated {filepath}")
else:
    print("Already updated.")
