import os

DOC_PATH = 'docs/KETONI_CONFLICT_ANALYSIS.md'

content = """# Ketoni Investment Structure & Conflict of Interest Analysis

## Executive Summary
Recent analysis of the signed **Ketoni Shareholder Agreement (24 April 2023)** and **Ketoni AFS 2024** has definitively established the ownership chain and exposed a massive conflict of interest involving Danie Bantjies.

## The Ownership Chain
The evidence confirms the following structure:
1. **Faucitt Family Trust (FFT)** holds 100% of the A Ordinary Shares in Ketoni Investment Holdings (investing R9.8 million).
2. **The Kevin Derrick Trust** holds 100% of the Ordinary Shares in Ketoni (investing R1,000).
3. **Ketoni Investment Holdings** holds 8.14% (456 shares) of **The George Group Proprietary Limited**, valued at R9.8 million.

## Financial Mechanics
- **Dividend Sweep:** FFT is entitled to 90% of all distributions from Ketoni for the first 5 years and 2 months.
- **Expected Return:** The agreement forecasts an IRR of not less than 24%, with a redemption value of R28.73 million by year 5.
- **Pass-Through Vehicle:** Ketoni is purely a pass-through vehicle. The agreement explicitly states that corporate tax is incurred and payable by The George Group, not Ketoni.

## The Bantjies Conflict of Interest
This structure creates an irreconcilable conflict of interest for Danie Bantjies:
- **Role 1 (Professional):** Bantjies serves as the CFO of The George Group. In this capacity, he manages the finances of the entity that generates the returns for Ketoni.
- **Role 2 (Fiduciary):** Bantjies was appointed as a Trustee of FFT by Rynette Farrar in July 2024. In this capacity, he has a fiduciary duty to the trust beneficiaries (Jacqueline and Daniel Faucitt).

**The Conflict:** Bantjies' professional loyalty to the CEO of George Group (Kevin Derrick, who also directs Ketoni) directly conflicts with his fiduciary duty to maximize and protect the returns for FFT's beneficiaries. He is simultaneously managing the source of the funds and acting as the guardian of the destination of those funds.

## Evidence Sources
- `Ketoni_Shareholder_Agreement_signed.pdf` (Clauses 2.1.2, 2.1.17, 2.1.21, 7.1, Annexure B)
- `Ketoni_AFS_2024.pdf` (Notes 2, 4, 5)

## Structural Diagram
![Ketoni Conflict Structure](../slide_images/ketoni_conflict_structure.png)
"""

with open(DOC_PATH, 'w') as f:
    f.write(content)
    
# Update README to link to this new analysis
with open('docs/README.md', 'a') as f:
    f.write("\n- [Ketoni Conflict Analysis](KETONI_CONFLICT_ANALYSIS.md)\n")

print(f"Created {DOC_PATH} and updated docs/README.md")
