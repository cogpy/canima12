import os
from pathlib import Path

ROOT = Path('/home/ubuntu/case-work/revstream1')
IN_DIR = ROOT / 'docs/filings/cycle6'
OUT_DIR = ROOT / 'docs/filings/cycle7'

for filename in os.listdir(IN_DIR):
    if not filename.endswith('.md') or 'RED_TEAM' in filename or 'RULE_35' in filename or 'DOCUMENT_EXAMINER' in filename:
        continue
        
    with open(IN_DIR / filename, 'r') as f:
        content = f.read()
        
    # Update version and cycle
    content = content.replace('v27', 'v28').replace('Cycle 6', 'Cycle 7')
    
    # Inject Annexure C reference if not present
    if 'Annexure C' not in content:
        content += "\n\n## Annexure C: Reciprocal Liability Correspondence Map\nSee `ANNEXURE_C_CORRESPONDENCE_MAP.md` for the temporal echo diagram demonstrating the mutually reinforcing channel between the Implicated Attorneys and the complicit Accountant."
            
    new_filename = filename.replace('v27', 'v28')
    with open(OUT_DIR / new_filename, 'w') as f:
        f.write(content)

print("Filings refined to v28.")
