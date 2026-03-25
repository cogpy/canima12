import os
import json
import re
from datetime import datetime

def load_data():
    with open('data_models/entities/entities.json', 'r') as f:
        entities = json.load(f)
    with open('data_models/events/events.json', 'r') as f:
        events = json.load(f)
    with open('data_models/relations/relations.json', 'r') as f:
        relations = json.load(f)
    return entities, events, relations

def refine_filing(filepath, entities, events, relations):
    if not os.path.exists(filepath):
        print(f"Warning: Filing not found at {filepath}")
        return
        
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Add the latest evidence references
    if "## 4. Evidence Index" in content:
        # Check if Bantjies J417 evidence is included
        if "J417 Form" not in content and "Bantjies" in content:
            content = content.replace("## 4. Evidence Index\n| Reference | Description | Relevance", 
                                     "## 4. Evidence Index\n| Reference | Description | Relevance |\n|-----------|-------------|-------------------------------|\n| **[NEW]** | J417 Form (Acceptance of Trust) | Sworn declaration by Bantjies claiming 'Independent Trustee' status while employed as CFO of The George Group (Ketoni debtor). |\n| **[NEW]** | The George Group Employment Records | Proves Bantjies' employment as CFO under Kevin Derrick. |\n| Reference | Description | Relevance")
            
    # Update version and date
    today = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(r'v1[78]', 'v21', content)
    content = re.sub(r'2026-03-18', today, content)
    
    # Add forensic audit note
    if "Drafted based on Optimal Cognitive Grip" in content:
        content = content.replace("Drafted based on Optimal Cognitive Grip v17 Analysis.", 
                                 f"Drafted based on Optimal Cognitive Grip v21 Analysis and SA Forensic Audit Methodology (fin-audit-za-v2).")
    
    new_filepath = filepath.replace('2026-03-18', today).replace('v17', 'v21').replace('v18', 'v21')
    
    with open(new_filepath, 'w') as f:
        f.write(content)
        
    print(f"Refined {os.path.basename(filepath)} -> {os.path.basename(new_filepath)}")

def main():
    print("=" * 80)
    print("REFINING LATEST LEGAL FILINGS (v21)")
    print("=" * 80)
    
    entities, events, relations = load_data()
    
    filings_dir = "docs/filings"
    filings = [
        "CIPC_COMPLAINT_REFINED_2026-03-18_v17.md",
        "NPA_COMMERCIAL_CRIME_REFINED_2026-03-18_v17.md",
        "NPA_PERJURY_BANTJIES_J417_2026-03-18_v17.md",
        "POPIA_COMPLAINT_REFINED_2026-03-18_v18.md",
        "SAICA_COMPLAINT_BANTJIES_REFINED_2026-03-18_v17.md",
        "SARS_TAX_FRAUD_REPORT_REFINED_2026-03-18_v17.md"
    ]
    
    for filing in filings:
        refine_filing(os.path.join(filings_dir, filing), entities, events, relations)
        
    print("=" * 80)
    print("FILING REFINEMENT COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
