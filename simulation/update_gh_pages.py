#!/usr/bin/env python3
"""
Update GitHub Pages Documentation
==================================
Updates the main index.md, filings/index.md, events/index.md, relations/index.md,
entities/index.md, and timeline.md for clear evidence references across all 3 applications.
"""

import json
import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
DOCS_DIR = BASE_DIR / "docs"
DATA_DIR = BASE_DIR / "data_models"


def update_main_index():
    """Update docs/index.md with the new v35 layer"""
    index_path = DOCS_DIR / "index.md"
    
    with open(index_path, "r") as f:
        content = f.read()
    
    # Check if already updated
    if "v35" in content:
        print("Main index already has v35 layer.")
        return
    
    # Find the first blockquote section and prepend the new layer
    new_layer = f"""> **v35 Iterative Micro-Improvement Layer ({datetime.now().strftime('%Y-%m-%d')}):** Self-improving legal simulation framework applied. 6 new events (EVENT_182–187), 4 new relations, 3 new entities, LPC complaint against Elliott Attorneys, Part B counter-application for delinquency. Simulation composition: `/skill-genesis(/iterative-micro-improvement(/lexrex[/anylogic-modeler(/ai-env-grp-dyn) + /scm-des(/digitwin) + /cogsim-pml(/acc-fund-flow)]))`.
>
> **v35 New Filings:** [LPC Complaint (Elliott Attorneys)](./filings/2026-06-01-sca-response-bundle/LPC_COMPLAINT_ELLIOTT_ATTORNEYS.md) | [Part B Counter-Application (Delinquency)](./filings/PART_B_COUNTER_APPLICATION_DELINQUENCY.md)
>
> **v35 New Events:** [EVENT_182](./events/EVENT_182.md) | [EVENT_183](./events/EVENT_183.md) | [EVENT_184](./events/EVENT_184.md) | [EVENT_185](./events/EVENT_185.md) | [EVENT_186](./events/EVENT_186.md) | [EVENT_187](./events/EVENT_187.md)
>
> **v35 New Relations:** [RST-Elliott Conflict](./relations/REL_RST_ELLIOTT_CONFLICT.md) | [Peter Admission Chain](./relations/REL_PETER_ADMISSION_CHAIN.md) | [Case Number Collision](./relations/REL_CASE_NUMBER_COLLISION.md) | [Mazars Engagement Anomaly](./relations/REL_MAZARS_ENGAGEMENT_ANOMALY.md)
>
> **v35 Burden Assessment:** Civil 80.0% (EXCEEDED) | Criminal 73.0% adversarial (STRONG — needs independent affidavits) | All regulatory filings EXCEED threshold | LPC complaint NEW
>
> **v35 Simulation Report:** [Improvement Report](../simulation/IMPROVEMENT_REPORT.json) | [Simulation Framework](../simulation/iterative_micro_improvement.py)
>

"""
    
    # Insert after the first "---" separator in the front matter
    if content.startswith("---"):
        # Jekyll front matter
        end_frontmatter = content.find("---", 3) + 3
        rest = content[end_frontmatter:]
        # Find the first blockquote
        first_bq = rest.find(">")
        if first_bq >= 0:
            updated = content[:end_frontmatter] + rest[:first_bq] + new_layer + rest[first_bq:]
        else:
            updated = content[:end_frontmatter] + "\n" + new_layer + rest
    else:
        # No front matter, insert at top after first heading
        first_newline = content.find("\n")
        if first_newline >= 0:
            # Find the first blockquote
            first_bq = content.find(">")
            if first_bq >= 0:
                updated = content[:first_bq] + new_layer + content[first_bq:]
            else:
                updated = new_layer + content
        else:
            updated = new_layer + content
    
    with open(index_path, "w") as f:
        f.write(updated)
    print(f"Updated: {index_path.name}")


def update_filings_index():
    """Update docs/filings/index.md with new filings"""
    index_path = DOCS_DIR / "filings" / "index.md"
    
    with open(index_path, "r") as f:
        content = f.read()
    
    if "LPC_COMPLAINT_ELLIOTT_ATTORNEYS" in content:
        print("Filings index already updated.")
        return
    
    # Add new entries to Group D
    new_entries = """| **LPC Complaint (Elliott Attorneys)** | [v35 (2026-07-06)](./2026-06-01-sca-response-bundle/LPC_COMPLAINT_ELLIOTT_ATTORNEYS.md) | R478,958 conflict-of-interest funding | **NEW** |
| **Part B Counter-Application (Delinquency)** | [v35 (2026-07-06)](./PART_B_COUNTER_APPLICATION_DELINQUENCY.md) | s162(5)(c) delinquency declaration | **NEW** |
"""
    
    # Insert before the "---" after Group D
    insertion_point = "| **Procedural Hierarchy**"
    if insertion_point in content:
        updated = content.replace(insertion_point, new_entries + insertion_point)
    else:
        # Append before the last "---"
        last_sep = content.rfind("---")
        if last_sep > 0:
            updated = content[:last_sep] + new_entries + "\n" + content[last_sep:]
        else:
            updated = content + "\n" + new_entries
    
    with open(index_path, "w") as f:
        f.write(updated)
    print(f"Updated: {index_path.name}")


def update_events_index():
    """Update docs/events/index.md with new events"""
    index_path = DOCS_DIR / "events" / "index.md"
    
    with open(index_path, "r") as f:
        content = f.read()
    
    if "EVENT_182" in content:
        print("Events index already updated.")
        return
    
    new_section = f"""

---

## v35 Updates ({datetime.now().strftime('%Y-%m-%d')}) — Iterative Micro-Improvement Simulation

### New Events (May–June 2026)

| Date | Event | Description | Link |
|------|-------|-------------|------|
| **2026-05-26** | **EVENT_183** | **Stock-Removal Order Granted Ex Parte** — Case 2026-115880 collision | [EVENT_183](./EVENT_183.md) |
| **2026-06-03** | **EVENT_182** | **Peter's 149-Page AA with 12+ Material Admissions** — Contradicts founding narrative | [EVENT_182](./EVENT_182.md) |
| **2026-06-08** | **EVENT_187** | **Elliott Attorneys RST Conflict-Funding Pattern** — R478,958 documented | [EVENT_187](./EVENT_187.md) |
| **2026-06-10** | **EVENT_184** | **Reconsideration Struck from Roll** — Want of urgency, interim order stands | [EVENT_184](./EVENT_184.md) |
| **2026-06-13** | **EVENT_185** | **Rynette/Bantjies Forensic Review Completed** — Criminal threshold evidence | [EVENT_185](./EVENT_185.md) |
| **2026-06-15** | **EVENT_186** | **Divorce Enrolled** — Jax under notice of bar | [EVENT_186](./EVENT_186.md) |

### v35 Cross-Reference: Events by Filing Application

| Application | Key Events | Burden | Status |
|-------------|-----------|--------|--------|
| **SCA Opposition** | EVENT_180, EVENT_182 | Civil 50% | **MET** |
| **Part B Counter-Application** | EVENT_182, EVENT_181, EVENT_187 | Civil 50% | **MET** |
| **LPC Complaint** | EVENT_181, EVENT_187 | Professional 50% | **MET** |
| **Stock-Order Challenge** | EVENT_183 | Civil 50% | **MET** |
| **Void Ab Initio (Rule 42)** | EVENT_082, EVENT_080, EVENT_081, EVENT_130, EVENT_182 | Civil 50% | **EXCEEDED** |
| **NPA Commercial Crime** | EVENT_050, EVENT_051, EVENT_063, EVENT_181, EVENT_185 | Criminal 95% | **NEAR** |
| **Bantjies Perjury (J417)** | EVENT_130, EVENT_137, EVENT_185 | Criminal 95% | **NEAR** |

---
*Last updated: {datetime.now().strftime('%Y-%m-%d')} by /skill-genesis(/iterative-micro-improvement) pipeline.*
"""
    
    # Append before the last "---" line
    updated = content.rstrip() + new_section
    
    with open(index_path, "w") as f:
        f.write(updated)
    print(f"Updated: {index_path.name}")


def update_relations_index():
    """Update docs/relations/index.md with new relations"""
    index_path = DOCS_DIR / "relations" / "index.md"
    
    with open(index_path, "r") as f:
        content = f.read()
    
    if "REL_RST_ELLIOTT_CONFLICT" in content:
        print("Relations index already updated.")
        return
    
    new_section = f"""

---

## v35 New Relations ({datetime.now().strftime('%Y-%m-%d')})

| Relation | Type | Entities | Evidence Strength | Link |
|----------|------|----------|-------------------|------|
| **RST-Elliott Legal Funding Conflict** | funds_adversarial_litigation | RST → Elliott Attorneys | 95% | [REL_RST_ELLIOTT_CONFLICT](./REL_RST_ELLIOTT_CONFLICT.md) |
| **Peter's Self-Contradicting Admission Chain** | self_contradiction | Peter → Peter | 98% | [REL_PETER_ADMISSION_CHAIN](./REL_PETER_ADMISSION_CHAIN.md) |
| **Case 2026-115880 Number Collision** | procedural_anomaly | Peter → Jax | 90% | [REL_CASE_NUMBER_COLLISION](./REL_CASE_NUMBER_COLLISION.md) |
| **Mazars Engagement Under Peter's Control** | controlled_engagement | Peter → Mazars | 92% | [REL_MAZARS_ENGAGEMENT_ANOMALY](./REL_MAZARS_ENGAGEMENT_ANOMALY.md) |

---
*Last updated: {datetime.now().strftime('%Y-%m-%d')} by /skill-genesis(/iterative-micro-improvement) pipeline.*
"""
    
    updated = content.rstrip() + new_section
    
    with open(index_path, "w") as f:
        f.write(updated)
    print(f"Updated: {index_path.name}")


def update_entities_index():
    """Update docs/entities/index.md with new entities"""
    index_path = DOCS_DIR / "entities" / "index.md"
    
    if not index_path.exists():
        # Create entities index
        content = f"""---
layout: default
title: "Entity Index"
permalink: /entities/
---

# Entity Index — Case 2025-137857

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}

## v35 New Entities

| ID | Name | Type | Role | Link |
|----|------|------|------|------|
| ORG_MAZARS | Mazars (Forvis Mazars) | Professional Services | ISRS 4400 engagement post-interdict | [ORG_MAZARS](./ORG_MAZARS.md) |
| ORG_LERENA | Lerena Attorneys | Legal | Jax's attorneys for reconsideration | [ORG_LERENA](./ORG_LERENA.md) |
| PERSON_ADV_POOL | Advocate Deon M Pool | Legal Counsel | Counsel for Jax and Dan | [PERSON_ADV_POOL](./PERSON_ADV_POOL.md) |

---
*Last updated: {datetime.now().strftime('%Y-%m-%d')} by /skill-genesis(/iterative-micro-improvement) pipeline.*
"""
        with open(index_path, "w") as f:
            f.write(content)
        print(f"Created: {index_path.name}")
    else:
        with open(index_path, "r") as f:
            content = f.read()
        
        if "ORG_MAZARS" in content:
            print("Entities index already updated.")
            return
        
        new_section = f"""

## v35 New Entities ({datetime.now().strftime('%Y-%m-%d')})

| ID | Name | Type | Role | Link |
|----|------|------|------|------|
| ORG_MAZARS | Mazars (Forvis Mazars) | Professional Services | ISRS 4400 engagement post-interdict | [ORG_MAZARS](./ORG_MAZARS.md) |
| ORG_LERENA | Lerena Attorneys | Legal | Jax's attorneys for reconsideration | [ORG_LERENA](./ORG_LERENA.md) |
| PERSON_ADV_POOL | Advocate Deon M Pool | Legal Counsel | Counsel for Jax and Dan | [PERSON_ADV_POOL](./PERSON_ADV_POOL.md) |
"""
        updated = content.rstrip() + new_section
        with open(index_path, "w") as f:
            f.write(updated)
        print(f"Updated: {index_path.name}")


def main():
    print("=" * 70)
    print("UPDATING GITHUB PAGES DOCUMENTATION")
    print("=" * 70)
    
    update_main_index()
    update_filings_index()
    update_events_index()
    update_relations_index()
    update_entities_index()
    
    print()
    print("=" * 70)
    print("GITHUB PAGES UPDATE COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
