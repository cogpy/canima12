---
name: void-ab-initio
description: Analyze an ex parte interdict to determine if it is void ab initio (void from the beginning) by applying the provable-foreknowledge principle. Use to establish perjury with provable foreknowledge, material non-disclosure, and fraud on both founding and supporting affidavits. Applicable to any legal case where a court order may have been obtained through fraud on the court. Triggers include mentions of void ab initio, fraudulent interdict, perjured affidavit, material non-disclosure in ex parte applications, or weaponized court orders.
---

# Void Ab Initio Analysis

Systematic, evidence-based workflow to determine if a court order (especially an ex parte interdict) is **void ab initio**. Uses the `provable-foreknowledge` framework to establish perjury, material non-disclosure, and fraud.

**Required companion skills:** Always consult `uniform-rules-of-court` for procedural rule citations (Rule 6 for ex parte requirements, Rule 42 for rescission, Rule 30 for irregular proceedings). Use `sa-entity-intel` for entity enrichment.

## The Pillars & Patterns of Invalidity

An interdict is void ab initio if obtained through one or more of these methods:

| Type | Test | Example |
|---|---|---|
| **Legal Impossibility** | Core premise is legally baseless | Banking mandate grants SOLE authority, making "unauthorized" claim impossible |
| **Perjury with Foreknowledge** | Applicant knew sworn statements were false | Bank letter confirming authority received before affidavit was signed |
| **Material Non-Disclosure** | Critical facts concealed from court | Failure to disclose banking mandate, prior correspondence, or true context |
| **Supporting Affidavit Fraud** | Supporting affiant also knowingly lied | Accountant received fraud report before signing supporting affidavit |
| **Direct Admission w/ Concealment** | Applicant admits an act but hides the context | Admits cancelling a card, but conceals it was done secretly and without authority |
| **Fabrication of Evidence** | Fraudulent documents were created | Fake 2019 financial statements for a company name created in 2021 |
| **Weaponized Litigation** | The court is used as an instrument of fraud | A victim is sued for "harassment" for trying to expose the fraud |
| **Settlement Under Duress** | Agreements are signed under coercion and then weaponized | A party is forced to sign agreements, which are then submitted to court for enforcement |

For detailed legal principles, read:
```bash
cat /home/ubuntu/skills/void-ab-initio/references/legal_framework.md
```

## Workflow

Three steps: **Register** > **Generate** > **Synthesize**.

### Step 1: Create the Foreknowledge Register

Copy the template and populate it with case-specific evidence.

```bash
cp /home/ubuntu/skills/void-ab-initio/templates/register_template.json ./void_ab_initio_register.json
```

Consult the schema for field definitions:
```bash
cat /home/ubuntu/skills/void-ab-initio/references/schema.md
```

Populate the register by reviewing all case material. The template pre-populates the pillars and patterns as material facts. For each agent, create knowledge events linking evidence to facts.

**Example knowledge event (Perjury with Foreknowledge):**
```json
{
  "event_id": "KE_APPLICANT_001",
  "agent_id": "APPLICANT",
  "fact_id": "FACT_PERJURY_FOREKNOWLEDGE",
  "timestamp": "2025-06-18T16:51:00Z",
  "acquisition_type": "email_correspondence",
  "evidence_refs": ["FNB_Legal_Letter_18_June_2025.pdf"],
  "description": "Applicant received email from FNB Legal confirming all directors had independent authority, two months before swearing the opposite under oath.",
  "confidence": "proven"
}
```

**Example knowledge event (Direct Admission w/ Concealment):**
```json
{
  "event_id": "KE_APPLICANT_002",
  "agent_id": "APPLICANT",
  "fact_id": "FACT_DIRECT_ADMISSION_CONCEALMENT",
  "timestamp": "2025-08-13T00:00:00Z",
  "acquisition_type": "direct_admission",
  "evidence_refs": ["Founding_Affidavit.pdf"],
  "description": "Applicant admits in his own affidavit that he cancelled a co-director's business card, but conceals that he did so secretly, without authority under the SOLE mandate, and then weaponized the consequences by characterizing the forced reimbursement as theft.",
  "confidence": "proven"
}
```

**Example knowledge event (Fabrication of Evidence):**
```json
{
  "event_id": "KE_OPERATOR_001",
  "agent_id": "OPERATOR",
  "fact_id": "FACT_FABRICATION_OF_EVIDENCE",
  "timestamp": "2021-05-01T00:00:00Z",
  "acquisition_type": "email_correspondence",
  "evidence_refs": ["Rynette_De_Novo_Email.pdf"],
  "description": "Operator instructed an accountant to create fraudulent 2019 financial statements for a company name that only existed from March 2021. The applicant then signed these fake accounts as director for a year he was not appointed.",
  "confidence": "proven"
}
```

**Example knowledge event (Weaponized Litigation):**
```json
{
  "event_id": "KE_APPLICANT_003",
  "agent_id": "APPLICANT",
  "fact_id": "FACT_WEAPONIZED_LITIGATION",
  "timestamp": "2025-11-01T00:00:00Z",
  "acquisition_type": "documentary_proof",
  "evidence_refs": ["3rd_Urgent_Application_Nov_2025.pdf"],
  "description": "Perpetrators filed an urgent application against the victim, using her attempt to warn a third party about the fake accounts as a basis to label her as harassing and mentally unstable. The settlement agreement's medical testing clause was cited as a weapon to silence witnesses.",
  "confidence": "proven"
}
```

**Example knowledge event (Settlement Under Duress):**
```json
{
  "event_id": "KE_APPLICANT_004",
  "agent_id": "APPLICANT",
  "fact_id": "FACT_SETTLEMENT_DURESS",
  "timestamp": "2025-09-18T00:00:00Z",
  "acquisition_type": "documentary_proof",
  "evidence_refs": ["ENS_Email_18_Sep_2025.pdf"],
  "description": "Applicant was present at a mediation where a co-director was physically prevented from leaving without signing settlement agreements. An email from the mediation records the co-director's request to file a criminal complaint, proving duress. The applicant then sought to have these duress-tainted agreements made an order of court.",
  "confidence": "proven"
}
```

**Example knowledge event (Supporting Affidavit Fraud):**
```json
{
  "event_id": "KE_SUPPORTING_001",
  "agent_id": "SUPPORTING_AFFIANT",
  "fact_id": "FACT_SUPPORTING_AFFIDAVIT_PERJURY",
  "timestamp": "2025-06-06T13:00:00Z",
  "acquisition_type": "email_correspondence",
  "evidence_refs": ["Daniel_Report_to_Bantjies_6_June_2025.pdf"],
  "description": "Supporting affiant received a comprehensive fraud report weeks before signing the supporting affidavit, yet failed to disclose it.",
  "confidence": "proven"
}
```

### Step 2: Generate the Audit Trail

```bash
mkdir -p ./void_ab_initio_analysis
python3 /home/ubuntu/skills/void-ab-initio/scripts/generate_audit_trail.py ./void_ab_initio_register.json ./void_ab_initio_analysis
```

This produces four files:
- `classification_report.md` — Agent tier classifications (A/B/C/D)
- `per_agent_audit_trail.md` — Chronological knowledge log per agent
- `knowledge_matrix.md` — Who knew what, and when
- `foreknowledge_timeline.mmd` — Mermaid timeline source

Optionally render the timeline:
```bash
manus-render-diagram ./void_ab_initio_analysis/foreknowledge_timeline.mmd ./void_ab_initio_analysis/foreknowledge_timeline.png
```

### Step 3: Synthesize the Final Report

Create `final_void_ab_initio_report.md` structured as follows:

1. **Executive Summary:** State the conclusion (void ab initio) and the tier classifications.
2. **Pillar & Pattern Analysis:** For each of the 7 pillars/patterns, present the evidence from the per-agent trail.
3. **Knowledge Matrix:** Embed the matrix table showing the conspiracy map.
4. **Timeline:** Embed the rendered timeline image.
5. **Legal Consequences:** Explain that the order is void, any contempt applications are baseless, and the act of enforcement constitutes malicious prosecution.
6. **Recommendations:** Formal application to set aside, criminal referrals for perjury, costs orders.

## Applying to Existing Case Material

This skill is designed to be applied iteratively to any new case material:

**New affidavit or court filing?** Extract claims, compare against the register, add new knowledge events if claims contradict known facts.

**New correspondence or evidence?** Add as evidence references to existing knowledge events, or create new events if they prove a new fact.

**Contempt application based on the void order?** The entire contempt application is baseless. Use the report to demonstrate that enforcement of a void order is itself an abuse of process.

**Victim attacked for exposing fraud?** This is the Weaponized Litigation pattern. Document the inversion (victim's lawful act reframed as a crime) and the silencing mechanism (medical testing, mental instability claims, settlement clauses used as weapons).

**Fabricated documents discovered?** Check for temporal impossibilities (company name did not exist, person not yet appointed, dates impossible). These are irrefutable and require no subjective judgment.

**Settlement agreements signed under duress?** Look for contemporaneous evidence of coercion (emails, complaints filed during mediation, physical prevention from leaving). The speed of withdrawal is key evidence: immediate withdrawal on the first business day after receiving copies proves the agreements were never accepted voluntarily. If the perpetrator then seeks to enforce these agreements via court, this is a further act of weaponized litigation.

**"Repudiation" or "bad faith" alleged?** Reframe: a notice of withdrawal from agreements signed under duress is not repudiation. It is a legitimate exercise of a legal right. The word "repudiation" is itself a weapon — it implies bad faith where none exists.
