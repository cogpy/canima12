#!/usr/bin/env python3
"""Write all application index pages for GitHub Pages."""
import os

DOCS = "/home/ubuntu/revstream1/docs"

pages = {
    "application-2-cipc-complaint/index.md": """---
layout: default
title: "Application 2: CIPC Companies Act Complaint"
---

# Application 2: CIPC Companies Act Complaint

**Case:** 2025-137857 | **Group:** B (Regulatory Complaints) | **Updated:** 2026-03-12

## Burden of Proof

| Standard | Threshold | LEX-SIM-NN Score | Status |
|----------|-----------|------------------|--------|
| Regulatory | 50% | 94.50% | **MET** |

## Key Violations

| Section | Violation | Perpetrators | Evidence |
|---------|-----------|-------------|----------|
| s28 | Failure to keep accounting records | Bantjies, Rynette | [Sage System Capture](../relations/SAGE_SYSTEM_CAPTURE.md) |
| s76 | Breach of fiduciary duty | Peter, Bantjies | [Trust Capture](../relations/TRUST_CAPTURE_SEQUENCE.md) |
| s162 | Director delinquency | Peter | [Coordinated Retaliation](../relations/COORDINATED_RETALIATION.md) |
| s163 | Oppressive conduct | Peter, Bantjies | [R10.6M Extraction](../relations/PETER_R10_6M_EXTRACTION.md) |
| s214 | False statements | Bantjies | [Manufacture Admission](../relations/MANUFACTURE_ADMISSION.md) |

## Key Relations

| Relation | Confidence | Link |
|----------|------------|------|
| Dual Corporate Identity | 95% | [View](../relations/DUAL_CORPORATE_IDENTITY.md) |
| Manufacture Admission | 100% | [View](../relations/MANUFACTURE_ADMISSION.md) |
| Trust Capture Sequence | 99% | [View](../relations/TRUST_CAPTURE_SEQUENCE.md) |
| Sage System Capture | 96% | [View](../relations/SAGE_SYSTEM_CAPTURE.md) |

## Filing

- [CIPC Complaint v11](../filings/CIPC_COMPLAINT_REFINED_2026-03-12_v11.md)

[Back to Main Index](../index.md)
""",

    "application-3-popia-complaint/index.md": """---
layout: default
title: "Application 3: POPIA Criminal Complaint"
---

# Application 3: POPIA Criminal Complaint

**Case:** 2025-137857 | **Group:** B (Regulatory Complaints) | **Updated:** 2026-03-12

## Burden of Proof

| Standard | Threshold | LEX-SIM-NN Score | Status |
|----------|-----------|------------------|--------|
| Criminal | 95% | 96.55% | **EXCEEDED** |

## Key POPIA Violations

| Section | Violation | Perpetrators | Evidence |
|---------|-----------|-------------|----------|
| s100-107 | Unauthorized processing of personal data | Rynette | [SARS Credential Abuse](../relations/SARS_CREDENTIAL_ABUSE.md) |
| s100-107 | Identity fraud across digital platforms | Rynette | [Domain Identity Fraud](../relations/DOMAIN_IDENTITY_FRAUD.md) |
| s100-107 | Unauthorized Sage system transfer | Rynette | [Sage System Capture](../relations/SAGE_SYSTEM_CAPTURE.md) |
| s100-107 | Post-mortem credential abuse (Kayla Pretorius) | Rynette | [Identity Fraud Network](../relations/IDENTITY_FRAUD_NETWORK.md) |

## v11 Evidence Strengthening (+2.53%)

| New Relation | Significance |
|-------------|--------------|
| SARS Credential Abuse | Direct proof of identity fraud and credential sharing |
| Sage System Capture | Unauthorized transfer and destruction of accounting data |
| Domain Identity Fraud | Systematic impersonation across multiple platforms |

## Key Relations

| Relation | Confidence | Link |
|----------|------------|------|
| Identity Fraud Network | 98% | [View](../relations/IDENTITY_FRAUD_NETWORK.md) |
| SARS Credential Abuse | 98% | [View](../relations/SARS_CREDENTIAL_ABUSE.md) |
| Sage System Capture | 96% | [View](../relations/SAGE_SYSTEM_CAPTURE.md) |
| Domain Identity Fraud | 97% | [View](../relations/DOMAIN_IDENTITY_FRAUD.md) |

## Filing

- [POPIA Complaint v11](../filings/POPIA_COMPLAINT_REFINED_2026-03-12_v11.md)

[Back to Main Index](../index.md)
""",

    "application-4-commercial-crime/index.md": """---
layout: default
title: "Application 4: Commercial Crime Submission"
---

# Application 4: Commercial Crime Submission

**Case:** 2025-137857 | **Group:** C (Criminal Prosecution Referrals) | **Updated:** 2026-03-12

## Burden of Proof

| Standard | Threshold | LEX-SIM-NN Score | Status |
|----------|-----------|------------------|--------|
| Criminal | 95% | 95.80% | **EXCEEDED** |

## Criminal Charges

| Charge | Legal Basis | Perpetrators | Evidence |
|--------|-------------|-------------|----------|
| Fraud | Common law | Peter, Rynette, Bantjies | [Banking Mandate Fraud](../relations/BANKING_MANDATE_FRAUD.md) |
| Theft | Common law | Peter | [R10.6M Extraction](../relations/PETER_R10_6M_EXTRACTION.md) |
| Forgery & Uttering | Common law | Rynette, Peter | [Trust Capture](../relations/TRUST_CAPTURE_SEQUENCE.md) |
| Racketeering | POCA | Peter, Rynette, Bantjies | [Revenue Hijacking Chain](../relations/REVENUE_HIJACKING_CHAIN.md) |
| Perjury | s319 CPA | Peter, Bantjies | [Interdict Void Ab Initio](../relations/INTERDICT_VOID_AB_INITIO.md) |

## v11 Evidence Strengthening (+3.80%)

| New Relation | Significance |
|-------------|--------------|
| Coordinated Retaliation | Clear pattern of conspiracy and malice after fraud exposure |
| Peter's R10.6M Extraction | Quantifies financial damage and true motive for interdict |
| Banking Mandate Fraud | Proves core interdict claims were based on false premise |
| Elliott Attorneys Protection | Evidence of obstruction and co-conspiracy |

## Key Relations

| Relation | Confidence | Link |
|----------|------------|------|
| Coordinated Retaliation | 99% | [View](../relations/COORDINATED_RETALIATION.md) |
| Peter's R10.6M Extraction | 99% | [View](../relations/PETER_R10_6M_EXTRACTION.md) |
| Banking Mandate Fraud | 97% | [View](../relations/BANKING_MANDATE_FRAUD.md) |
| Revenue Hijacking Chain | 99% | [View](../relations/REVENUE_HIJACKING_CHAIN.md) |

## Filing

- [Commercial Crime Submission v11](../filings/COMMERCIAL_CRIME_SUBMISSION_REFINED_2026-03-12_v11.md)

[Back to Main Index](../index.md)
""",

    "application-5-npa-tax-fraud/index.md": """---
layout: default
title: "Application 5: NPA Tax Fraud Report"
---

# Application 5: NPA Tax Fraud Report

**Case:** 2025-137857 | **Group:** C (Criminal Prosecution Referrals) | **Updated:** 2026-03-12

## Burden of Proof

| Standard | Threshold | LEX-SIM-NN Score | Status |
|----------|-----------|------------------|--------|
| Criminal | 95% | 96.10% | **EXCEEDED** |

## Tax Fraud Elements

| Violation | Legal Basis | Perpetrators | Evidence |
|-----------|-------------|-------------|----------|
| SARS record falsification | Tax Admin Act s235 | Bantjies | [Manufacture Admission](../relations/MANUFACTURE_ADMISSION.md) |
| Transfer pricing manipulation | Income Tax Act | Peter, Rynette | [Villa Via Profit Extraction](../relations/VILLA_VIA_PROFIT_EXTRACTION.md) |
| Fabricated intercompany debt | Companies Act s28 | Rynette | [ReZonance Debt Fabrication](../relations/REZONANCE_DEBT_FABRICATION.md) |
| SARS credential abuse | Tax Admin Act s235 | Rynette, Bantjies | [SARS Credential Abuse](../relations/SARS_CREDENTIAL_ABUSE.md) |
| Exchange Control violations | Exchange Control Act | Peter | FNB Fraud Letter (SF10) |

## v11 Evidence Strengthening (+4.35%)

| New Relation | Significance |
|-------------|--------------|
| Bantjies "Manufacture" Admission | Smoking gun: direct admission of intent to deceive SARS |
| Villa Via Profit Extraction | Transfer pricing and profit extraction schemes |
| ReZonance Debt Fabrication | Pattern of fabricating accounting records for leverage |

## Key Relations

| Relation | Confidence | Link |
|----------|------------|------|
| Manufacture Admission | 100% | [View](../relations/MANUFACTURE_ADMISSION.md) |
| Villa Via Profit Extraction | 97% | [View](../relations/VILLA_VIA_PROFIT_EXTRACTION.md) |
| ReZonance Debt Fabrication | 96% | [View](../relations/REZONANCE_DEBT_FABRICATION.md) |
| SARS Credential Abuse | 98% | [View](../relations/SARS_CREDENTIAL_ABUSE.md) |

## Filing

- [NPA Tax Fraud Report v11](../filings/NPA_TAX_FRAUD_REPORT_REFINED_2026-03-12_v11.md)

[Back to Main Index](../index.md)
""",

    "application-6-fic-report/index.md": """---
layout: default
title: "Application 6: FIC Suspicious Transaction Report"
---

# Application 6: FIC Suspicious Transaction Report

**Case:** 2025-137857 | **Group:** B (Regulatory Complaints) | **Updated:** 2026-03-12

## Burden of Proof

| Standard | Threshold | LEX-SIM-NN Score | Status |
|----------|-----------|------------------|--------|
| Regulatory | 50% | 91.20% | **MET** |

## Suspicious Transactions

| Date | Entity | Amount | Type | Evidence |
|------|--------|--------|------|----------|
| 3 Sep 2025 | RWD | R5,164,131.18 | Post-interdict extraction | [R10.6M Extraction](../relations/PETER_R10_6M_EXTRACTION.md) |
| 11 Sep 2025 | RST | R3,090,000.00 | Post-interdict extraction | Bank records |
| 11 Sep 2025 | VVA | R1,730,000.00 | Post-interdict extraction | Bank records |
| 11 Sep 2025 | SLG | R640,000.00 | Post-interdict extraction | Bank records |
| Various | ABSA account | R10,269,727.90 | Revenue diversion | [Revenue Hijacking Chain](../relations/REVENUE_HIJACKING_CHAIN.md) |

## Key Relations

| Relation | Confidence | Link |
|----------|------------|------|
| Peter's R10.6M Extraction | 99% | [View](../relations/PETER_R10_6M_EXTRACTION.md) |
| Revenue Hijacking Chain | 99% | [View](../relations/REVENUE_HIJACKING_CHAIN.md) |
| Ketoni Insider Trading | 98% | [View](../relations/KETONI_INSIDER_TRADING_NETWORK.md) |

## Filing

- [FIC Report v11](../filings/FIC_REPORT_REFINED_2026-03-12_v11.md)

[Back to Main Index](../index.md)
"""
}

for path, content in pages.items():
    full_path = os.path.join(DOCS, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f"Written: {full_path}")

print("All application index pages written.")
