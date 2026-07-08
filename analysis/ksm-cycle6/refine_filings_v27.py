import os
from pathlib import Path

ROOT = Path('/home/ubuntu/case-work/revstream1')
IN_DIR = ROOT / 'docs/filings/cycle5'
OUT_DIR = ROOT / 'docs/filings/cycle6'

for filename in os.listdir(IN_DIR):
    if not filename.endswith('.md') or 'RED_TEAM' in filename or 'RULE_35' in filename or 'DOCUMENT_EXAMINER' in filename:
        continue
        
    with open(IN_DIR / filename, 'r') as f:
        content = f.read()
        
    # Update version and cycle
    content = content.replace('v26', 'v27').replace('Cycle 5', 'Cycle 6')
    
    # Inject Gradient Schedule reference if not present
    if 'Annexure B' not in content:
        content += "\n\n## Annexure B: Gradient Ladder of Escalation\nSee `GRADIENT_SCHEDULE_ANNEXURE.md` for the full escalation chain from procedural irregularity to organised criminal enterprise."
            
    new_filename = filename.replace('v26', 'v27')
    with open(OUT_DIR / new_filename, 'w') as f:
        f.write(content)

print("Filings refined to v27.")
