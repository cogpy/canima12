#!/usr/bin/env python3
"""
Apply Iterative Micro-Improvement Results to Data Models
=========================================================
Reads the IMPROVEMENT_REPORT.json and applies:
1. New events to events.json and timeline.json
2. New relations to relations.json
3. New entities to entities.json
4. Updates event/entity/relation indexes in docs/
"""

import json
import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data_models"
DOCS_DIR = BASE_DIR / "docs"
REPORT_PATH = Path(__file__).parent / "IMPROVEMENT_REPORT.json"


def load_json(path):
    with open(path) as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"  Saved: {path}")


def apply_new_events(report):
    """Add new events to events.json and timeline.json"""
    events_path = DATA_DIR / "events.json"
    timeline_path = DATA_DIR / "timelines" / "timeline.json"
    
    events = load_json(events_path)
    timeline = load_json(timeline_path)
    
    existing_ids = {e["id"] for e in events}
    new_events = report.get("new_events_suggested", [])
    
    added = 0
    for ev in new_events:
        if ev["id"] not in existing_ids:
            # Add to events.json
            event_entry = {
                "id": ev["id"],
                "title": ev["title"],
                "date": ev["date"],
                "description": ev["description"],
                "entities_involved": ev.get("actors", []),
                "evidence_refs": ev.get("evidence_refs", []),
                "significance_level": ev.get("significance_level", 7),
                "phase": ev.get("phase", "appeal_and_response"),
                "added_date": datetime.now().strftime("%Y-%m-%d"),
                "source": "iterative-micro-improvement-v1"
            }
            events.append(event_entry)
            
            # Add to timeline
            timeline_entry = {
                "date": ev["date"],
                "event_ref": ev["id"],
                "title": ev["title"],
                "description": ev["description"],
                "category": "legal_proceedings",
                "significance_level": ev.get("significance_level", 7),
                "actors": ev.get("actors", []),
                "entities_involved": ev.get("actors", []),
                "added_date": datetime.now().strftime("%Y-%m-%d"),
                "evidence_refs": ev.get("evidence_refs", [])
            }
            timeline["timeline"].append(timeline_entry)
            added += 1
    
    # Sort timeline by date
    timeline["timeline"].sort(key=lambda x: x.get("date", ""))
    
    # Update metadata
    timeline["metadata"]["version"] = "30.0_SIMULATION_REFINED_" + datetime.now().strftime("%Y_%m_%d")
    timeline["metadata"]["description"] = f"Timeline of Revenue Stream Hijacking Case 2025-137857 — {len(timeline['timeline'])} events (refined by iterative-micro-improvement simulation)"
    
    save_json(events_path, events)
    save_json(timeline_path, timeline)
    print(f"  Added {added} new events (total: {len(events)} events, {len(timeline['timeline'])} timeline entries)")
    return added


def apply_new_relations(report):
    """Add new relations to relations.json"""
    relations_path = DATA_DIR / "relations.json"
    relations = load_json(relations_path)
    
    existing_ids = {r["id"] for r in relations}
    new_relations = report.get("new_relations_suggested", [])
    
    added = 0
    for rel in new_relations:
        if rel["id"] not in existing_ids:
            relation_entry = {
                "id": rel["id"],
                "title": rel["title"],
                "entities_involved": [rel["source"], rel["target"]],
                "type": rel["type"],
                "evidence_strength": rel.get("evidence_strength", 0.0),
                "description": rel["description"],
                "evidence_refs": rel.get("evidence_refs", []),
                "added_date": datetime.now().strftime("%Y-%m-%d"),
                "source": "iterative-micro-improvement-v1"
            }
            relations.append(relation_entry)
            added += 1
    
    save_json(relations_path, relations)
    print(f"  Added {added} new relations (total: {len(relations)})")
    return added


def apply_new_entities(report):
    """Add new entities to entities.json"""
    entities_path = DATA_DIR / "entities.json"
    entities = load_json(entities_path)
    
    existing_ids = {e["id"] for e in entities}
    new_entities = report.get("new_entities_suggested", [])
    
    added = 0
    for ent in new_entities:
        if ent["id"] not in existing_ids:
            entity_entry = {
                "id": ent["id"],
                "name": ent["name"],
                "type": ent["type"],
                "role": ent.get("role", ""),
                "evidence_codes": ent.get("evidence_refs", []),
                "significance": ent.get("significance", ""),
                "added_date": datetime.now().strftime("%Y-%m-%d"),
                "source": "iterative-micro-improvement-v1"
            }
            entities.append(entity_entry)
            added += 1
    
    save_json(entities_path, entities)
    print(f"  Added {added} new entities (total: {len(entities)})")
    return added


def generate_event_docs(report):
    """Generate markdown docs for new events"""
    events_dir = DOCS_DIR / "events"
    events_dir.mkdir(exist_ok=True)
    
    new_events = report.get("new_events_suggested", [])
    
    for ev in new_events:
        event_path = events_dir / f"{ev['id']}.md"
        if not event_path.exists():
            content = f"""# {ev['id']}: {ev['title']}

- **Date:** {ev['date']}
- **Event type:** {ev.get('phase', 'appeal_and_response')}
- **Significance level:** {ev.get('significance_level', 7)}/10
- **Criminal threshold:** {'Yes' if ev.get('criminal_threshold') else 'No'}
- **Source:** iterative-micro-improvement simulation framework

## Description

{ev['description']}

## Entities Involved

| Entity | Role |
|--------|------|
"""
            for actor in ev.get("actors", []):
                content += f"| {actor} | Actor |\n"
            
            content += f"""
## Evidence References

"""
            for ref in ev.get("evidence_refs", []):
                content += f"- {ref}\n"
            
            content += f"""
## Filing Impact

"""
            for filing in ev.get("filing_impact", []):
                content += f"- {filing}\n"
            
            content += f"""
---
*Generated: {datetime.now().strftime('%Y-%m-%d')} by iterative-micro-improvement simulation framework*
"""
            with open(event_path, "w") as f:
                f.write(content)
            print(f"  Created: {event_path.name}")


def generate_relation_docs(report):
    """Generate markdown docs for new relations"""
    relations_dir = DOCS_DIR / "relations"
    relations_dir.mkdir(exist_ok=True)
    
    new_relations = report.get("new_relations_suggested", [])
    
    for rel in new_relations:
        # Create a filename from the ID
        filename = rel["id"].upper() + ".md"
        rel_path = relations_dir / filename
        if not rel_path.exists():
            content = f"""# {rel['title']}

- **Relation ID:** {rel['id']}
- **Type:** {rel['type']}
- **Source entity:** {rel['source']}
- **Target entity:** {rel['target']}
- **Evidence strength:** {rel.get('evidence_strength', 0.0):.0%}

## Description

{rel['description']}

## Evidence References

"""
            for ref in rel.get("evidence_refs", []):
                content += f"- {ref}\n"
            
            content += f"""
---
*Generated: {datetime.now().strftime('%Y-%m-%d')} by iterative-micro-improvement simulation framework*
"""
            with open(rel_path, "w") as f:
                f.write(content)
            print(f"  Created: {rel_path.name}")


def generate_entity_docs(report):
    """Generate markdown docs for new entities"""
    entities_dir = DOCS_DIR / "entities"
    entities_dir.mkdir(exist_ok=True)
    
    new_entities = report.get("new_entities_suggested", [])
    
    for ent in new_entities:
        entity_path = entities_dir / f"{ent['id']}.md"
        if not entity_path.exists():
            content = f"""# {ent['id']}: {ent['name']}

- **Type:** {ent['type']}
- **Role:** {ent.get('role', 'Unknown')}

## Significance

{ent.get('significance', '')}

## Evidence References

"""
            for ref in ent.get("evidence_refs", []):
                content += f"- {ref}\n"
            
            content += f"""
---
*Generated: {datetime.now().strftime('%Y-%m-%d')} by iterative-micro-improvement simulation framework*
"""
            with open(entity_path, "w") as f:
                f.write(content)
            print(f"  Created: {entity_path.name}")


def main():
    print("=" * 70)
    print("APPLYING ITERATIVE MICRO-IMPROVEMENT RESULTS")
    print("=" * 70)
    
    # Load report
    report = load_json(REPORT_PATH)
    print(f"Loaded report from cycle {report['metadata']['cycle']}")
    print()
    
    # Apply improvements
    print("1. Applying new events...")
    apply_new_events(report)
    print()
    
    print("2. Applying new relations...")
    apply_new_relations(report)
    print()
    
    print("3. Applying new entities...")
    apply_new_entities(report)
    print()
    
    print("4. Generating event documentation...")
    generate_event_docs(report)
    print()
    
    print("5. Generating relation documentation...")
    generate_relation_docs(report)
    print()
    
    print("6. Generating entity documentation...")
    generate_entity_docs(report)
    print()
    
    print("=" * 70)
    print("IMPROVEMENTS APPLIED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()
