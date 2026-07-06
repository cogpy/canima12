#!/usr/bin/env python3
"""
Generate Improved Legal Filings
===============================
Applies the simulation recommendations to update existing filings and generate new ones.
1. Updates SCA Opposition with Peter's 3 Jun 2026 AA admissions
2. Creates new Legal Practice Council (LPC) complaint against Elliott Attorneys
3. Updates Part B counter-application strategy
"""

import json
import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
DOCS_DIR = BASE_DIR / "docs"
FILINGS_DIR = DOCS_DIR / "filings"
SCA_BUNDLE_DIR = FILINGS_DIR / "2026-06-01-sca-response-bundle"


def update_sca_opposition():
    """Update CIVIL_SCA_OPPOSITION.md with new admissions"""
    file_path = SCA_BUNDLE_DIR / "CIVIL_SCA_OPPOSITION.md"
    
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
        
    with open(file_path, "r") as f:
        content = f.read()
    
    # Check if already updated
    if "Peter's 3 Jun 2026 AA admissions" in content or "EVENT_182" in content:
        print("SCA Opposition already updated.")
        return
        
    # We'll append a new section before the oath block or at the end of the evidence section
    insertion_point = "## 5. Evidence Schedule"
    
    new_section = """
## 4A. Fatal Admissions in Petitioner's 3 June 2026 Answering Affidavit

The Petitioner's subsequent answering affidavit in the main action (sworn 3 June 2026, EVENT_182) contains material admissions that directly contradict the narrative advanced in this petition:

1. **Admission of Unilateral Platform Interference:** At paragraph 63.5, the Petitioner admits "Halting the use thereof [Shopify] was well justified," directly contradicting the founding narrative that the platform failure was a system error or the Respondents' fault.
2. **Admission of Withholding Financial Records:** At paragraph 75.4, the Petitioner admits financial statements were withheld "pending a final decision," contradicting claims of transparent governance.
3. **Admission of Factional Agency:** At paragraph 64.2, the Petitioner states "Ms Farrar acts on my instructions only," legally binding the Petitioner to the bookkeeper's actions (including the 8 July 2024 forged Sage transfer and 17 June 2025 fraudulent loan creation).
4. **Contradiction of Foundation Interdict:** At paragraphs 77.2, 83.2, and 185.2, the Petitioner claims the Respondents were "merely interdicted… not excluded," which directly contradicts the express wording of his own 19 August 2025 order (para 2.6: "to the exclusion of").

These sworn admissions fundamentally undermine the prospects of success on appeal, as the Petitioner's own subsequent evidence defeats the case advanced in the petition.

"""
    
    if insertion_point in content:
        updated_content = content.replace(insertion_point, new_section + insertion_point)
        with open(file_path, "w") as f:
            f.write(updated_content)
        print(f"Updated: {file_path.name}")
    else:
        # Append to end if insertion point not found
        with open(file_path, "a") as f:
            f.write(new_section)
        print(f"Appended to: {file_path.name}")


def create_lpc_complaint():
    """Create a new LPC complaint against Elliott Attorneys"""
    file_path = SCA_BUNDLE_DIR / "LPC_COMPLAINT_ELLIOTT_ATTORNEYS.md"
    
    content = f"""# COMPLAINT TO THE LEGAL PRACTICE COUNCIL

**Date:** {datetime.now().strftime('%Y-%m-%d')}  
**Complainant:** Jacqueline Faucitt (CEO, RegimA Skin Treatments CC)  
**Respondent Legal Practitioner:** Elliott Attorneys Inc (Ref: KF0019)  
**Related High Court Case:** 2025-137857  

## 1. Nature of Complaint

This complaint addresses a severe conflict of interest, potential breach of fiduciary duty, and improper funding arrangement. Between 25 August 2025 and 15 April 2026, Elliott Attorneys received **R478,957.93** directly from the ABSA bank account (4112241409) of RegimA Skin Treatments CC (RST). 

During this exact period, Elliott Attorneys was acting as the applicant-side law firm for Peter Andrew Faucitt in litigation proceedings *adverse* to Jacqueline Faucitt, the CEO of RST. 

## 2. Factual Basis

1. **The Funding Source:** The ABSA payment extract (EVENT_181) records 16 distinct payments from RST to Elliott Attorneys totalling R478,957.93.
2. **The Conflict:** Elliott Attorneys appears in the litigation record acting for Peter Faucitt and advancing litigation pressure against Jacqueline Faucitt.
3. **The Corporate Anomaly:** There is no known member resolution authorizing RST to fund litigation against its own CEO.
4. **The Prejudice:** This arrangement created an extreme inequality of arms, where the CEO was forced to fund her defence personally while the applicant's litigation costs were secretly subsidized by the very company the CEO manages.

## 3. Violations of the Code of Conduct

The conduct *prima facie* violates the Legal Practice Council Code of Conduct regarding:
- **Conflict of Interest:** Acting against a corporate officer while accepting fees from that corporation without proper independent board authorization.
- **Proper Purpose:** Accepting corporate funds to finance a factional shareholder dispute.
- **Independence:** Failing to maintain professional independence from internal corporate disputes.

## 4. Relief and Investigation Requested

The Complainant requests that the Legal Practice Council investigate this matter and compel Elliott Attorneys to produce:
1. The formal engagement letter and terms of reference for the KF0019 mandate.
2. The conflict-check records performed before accepting the mandate.
3. The corporate resolutions (if any) relied upon to accept payment from RST CC.
4. Unredacted invoices corresponding to the 16 payments from the RST ABSA account.

## 5. Evidence Schedule

| Item | Description | Reference |
|---|---|---|
| 1 | RST ABSA 4112241409 Payment Extract (Aug 2025 - Apr 2026) | EVENT_181 |
| 2 | High Court Case 2025-137857 Pleadings | EVENT_080 |
| 3 | Peter Faucitt Answering Affidavit (3 Jun 2026) | EVENT_182 |

---
*Signed at Johannesburg on this _____ day of ____________ 2026.*

___________________________
**JACQUELINE FAUCITT**
"""
    
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Created: {file_path.name}")


def update_bundle_readme():
    """Update the SCA response bundle README to include the new LPC complaint"""
    file_path = SCA_BUNDLE_DIR / "README.md"
    
    if not file_path.exists():
        return
        
    with open(file_path, "r") as f:
        content = f.read()
        
    if "LPC_COMPLAINT_ELLIOTT_ATTORNEYS.md" in content:
        return
        
    # Add to the Master action matrix
    insertion_point = "| [`POPIA_COMPLAINT.md`](POPIA_COMPLAINT.md)"
    
    new_row = "| [`LPC_COMPLAINT_ELLIOTT_ATTORNEYS.md`](LPC_COMPLAINT_ELLIOTT_ATTORNEYS.md) | Legal Practice Council complaint regarding conflict of interest and improper corporate funding. | Legal Practice Council | Formal complaint statement requesting investigation into R478,958 in RST-funded payments. |\n"
    
    if insertion_point in content:
        updated_content = content.replace(insertion_point, new_row + insertion_point)
        with open(file_path, "w") as f:
            f.write(updated_content)
        print(f"Updated: {file_path.name}")


def create_part_b_counter():
    """Create the Part B Counter-Application framework"""
    file_path = FILINGS_DIR / "PART_B_COUNTER_APPLICATION_DELINQUENCY.md"
    
    content = f"""# PART B COUNTER-APPLICATION: DECLARATION OF DELINQUENCY

**Date:** {datetime.now().strftime('%Y-%m-%d')}  
**Case:** 2025-137857 (Part B)  
**Nature:** Counter-application under s162(5)(c) of the Companies Act 71 of 2008  

## 1. Purpose

This counter-application seeks an order declaring Peter Andrew Faucitt a delinquent director in terms of section 162(5)(c) of the Companies Act 71 of 2008, based on gross abuses of the position of director, taking personal advantage of information or opportunities, and intentionally inflicting harm upon the companies (RST, RWD, SLG) and a co-director (Jacqueline Faucitt).

## 2. Evidentiary Foundation (The 3 June 2026 Admissions)

The applicant's own answering affidavit (sworn 3 June 2026, EVENT_182) provides the conclusive evidentiary foundation for this counter-application through formal admissions:

1. **Admission of Unilateral Harm:** The applicant admits to "Halting the use thereof [Shopify]" (para 63.5), an act of deliberate sabotage against the company's primary revenue channel.
2. **Admission of Financial Obfuscation:** The applicant admits withholding financial statements "pending a final decision" (para 75.4), violating fundamental statutory duties of transparency and accounting.
3. **Admission of Absolute Agency:** The applicant states "Ms Farrar acts on my instructions only" (para 64.2), thereby accepting direct legal responsibility for the 8 July 2024 forged Sage transfer, the 17 June 2025 fraudulent loan creation, and the systemic identity fraud ("pp Peter").
4. **Admission of Unauthorized Asset Sweeps:** The applicant admits moving funds from FNB to entity savings to ABSA "to Safety" (paras 53.3, 62.4, 65.3) without board authorization.

## 3. Statutory Breaches

These admitted actions constitute gross violations of:
- **Section 76(2)(b):** Using the position of director to gain a personal advantage or knowingly cause harm to the company.
- **Section 76(3)(c):** Failing to act in good faith and for proper purpose.
- **Section 29:** Falsification of accounting records (via the admitted agent, Rynette Farrar).

## 4. The Funding Conflict Anomaly

The delinquency application is further supported by EVENT_181, which demonstrates the applicant utilizing R478,957.93 of RST corporate funds to finance his personal litigation against the RST CEO (Elliott Attorneys payments). This constitutes an improper extraction of corporate assets for personal factional advantage.

## 5. Relief Sought

1. Declaring Peter Andrew Faucitt a delinquent director in terms of s162(5)(c) of the Companies Act.
2. Removing Peter Andrew Faucitt from all directorships within the RegimA group of companies.
3. Directing the applicant to repay the R478,957.93 improperly extracted from RST for personal legal fees.
4. Costs on an attorney and client scale.
"""
    
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Created: {file_path.name}")


def main():
    print("=" * 70)
    print("GENERATING IMPROVED LEGAL FILINGS")
    print("=" * 70)
    
    update_sca_opposition()
    create_lpc_complaint()
    update_bundle_readme()
    create_part_b_counter()
    
    print("=" * 70)
    print("FILING GENERATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
