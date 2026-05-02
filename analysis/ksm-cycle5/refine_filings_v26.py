import os
from pathlib import Path

ROOT = Path('/home/ubuntu/case-work/revstream1')
IN_DIR = ROOT / 'docs/filings/cycle4'
OUT_DIR = ROOT / 'docs/filings/cycle5'

# Harmonised anchor format template
ANCHOR_TEMPLATE = """
## Independent Evidence Anchors (Harmonised)

| PILLAR | NAME | THIRD-PARTY SOURCE | DOCUMENT REFERENCE | INDEPENDENT VERIFIABILITY |
|--------|------|--------------------|--------------------|---------------------------|
| XI | Forensic Audit | High Court Order | Prayer 5, Civil Recon | Court-appointed expert |
| XII | Signature Forgery | Commissioner Register | Rule 35(3) Notice | Document Examiner |
| XIII | Attorney Complicity | Implicated Attorneys' File | Rule 35(3) Notice | Subpoena |
| X | Continuing Prejudice | FNB / Shopify | Annexure A | Bank records |
| IX | Zero-Communication | Exchange Tenant | Cycle 3 Report | 110,421 emails |
| VIII | Digital Identity | Sage Africa | User Switch Form | Sage tenant logs |
| III | Legal Impossibility | FNB FICA | Sole Mandate Proof | FNB records |
| II | Perjury (J417) | CIPC / Trust Deed | Bantjies Affidavit | Public records |
"""

for filename in os.listdir(IN_DIR):
    if not filename.endswith('.md') or 'RED_TEAM' in filename:
        continue
        
    with open(IN_DIR / filename, 'r') as f:
        content = f.read()
        
    # Update version and cycle
    content = content.replace('v25', 'v26').replace('Cycle 4', 'Cycle 5')
    
    # Inject harmonised anchors
    if '## 1. Independent Evidence Anchors' in content:
        parts = content.split('## 1. Independent Evidence Anchors')
        # Find the next section
        next_section_idx = parts[1].find('## 2.')
        if next_section_idx != -1:
            content = parts[0] + ANCHOR_TEMPLATE + '\n' + parts[1][next_section_idx:]
            
    elif '## 2. Independent Evidence Anchors' in content:
        parts = content.split('## 2. Independent Evidence Anchors')
        next_section_idx = parts[1].find('## 3.')
        if next_section_idx != -1:
            content = parts[0] + ANCHOR_TEMPLATE + '\n' + parts[1][next_section_idx:]
            
    new_filename = filename.replace('v25', 'v26')
    with open(OUT_DIR / new_filename, 'w') as f:
        f.write(content)

print("Filings refined to v26.")
