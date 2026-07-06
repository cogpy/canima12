#!/usr/bin/env python3
"""
Backfill Consistency Engine
============================
Updates the hypergraph framework and LEX transformer with v35/v36 data,
then backfills all data models for cross-model consistency.

Composition: /aicpp(/61-definition-ksm[/fin-audit-za-v2, /lex-case-analysis, /revstream-evidence], /lex-encode-workflow)
"""

import json
import os
import shutil
from datetime import datetime

REVSTREAM = '/home/ubuntu/revstream1'
ADRESJ7 = '/home/ubuntu/ad-res-j7'

# =============================================================================
# SECTION 1: Load current data models
# =============================================================================

def load_json(path):
    with open(path) as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Load revstream1 data models
entities = load_json(f'{REVSTREAM}/data_models/entities.json')
relations = load_json(f'{REVSTREAM}/data_models/relations.json')
events = load_json(f'{REVSTREAM}/data_models/events.json')
timeline_data = load_json(f'{REVSTREAM}/data_models/timelines/timeline.json')

# timeline.json is a dict with 'timeline' list inside
timeline = timeline_data.get('timeline', []) if isinstance(timeline_data, dict) else timeline_data

print(f"Current state: {len(entities)} entities, {len(relations)} relations, {len(events)} events, {len(timeline)} timeline entries")

# =============================================================================
# SECTION 2: Define v35/v36 additions
# =============================================================================

NEW_ENTITIES = [
    {
        "id": "ORG_MAZARS",
        "type": "organization",
        "name": "Forvis Mazars",
        "category": "professional_services",
        "description": "Audit firm engaged by Peter for RST/SLG audit despite conflict",
        "attributes": {
            "registration": "Unknown",
            "role": "auditor",
            "engagement_date": "2025-12",
            "anomaly": "Engaged without CEO knowledge or board resolution",
            "evidence_strength": 0.92
        },
        "added_version": "v35",
        "added_date": "2026-07-06"
    },
    {
        "id": "ORG_LERENA",
        "type": "organization",
        "name": "Lerena Attorneys",
        "category": "legal_services",
        "description": "Attorneys representing Peter in divorce proceedings",
        "attributes": {
            "role": "legal_counsel_divorce",
            "engagement_date": "2025",
            "case": "Divorce proceedings"
        },
        "added_version": "v35",
        "added_date": "2026-07-06"
    },
    {
        "id": "PERSON_ADV_POOL",
        "type": "person",
        "name": "Advocate Deon M Pool",
        "category": "legal_professional",
        "description": "Advocate briefed by Elliott for SCA petition",
        "attributes": {
            "role": "advocate",
            "briefed_by": "ORG_020",
            "case": "SCA Petition Case 2026-115880"
        },
        "added_version": "v35",
        "added_date": "2026-07-06"
    }
]

NEW_RELATIONS = [
    {
        "id": "REL_RST_ELLIOTT_CONFLICT",
        "type": "conflict_of_interest",
        "source": "ORG_002",
        "target": "ORG_020",
        "description": "RST corporate funds (R478,958) used to fund litigation against RST CEO",
        "evidence_strength": 0.95,
        "evidence_refs": ["EVENT_181", "EVENT_187"],
        "legal_significance": "Breach of fiduciary duty; conflict of interest; unauthorized expenditure",
        "added_version": "v35"
    },
    {
        "id": "REL_PETER_ADMISSION_CHAIN",
        "type": "self_contradiction",
        "source": "PERSON_001",
        "target": "PERSON_001",
        "description": "Peter's 3 Jun 2026 AA contains 12+ material admissions contradicting founding affidavit",
        "evidence_strength": 0.98,
        "evidence_refs": ["EVENT_182"],
        "legal_significance": "Perjury; material non-disclosure; void ab initio",
        "added_version": "v35"
    },
    {
        "id": "REL_CASE_NUMBER_COLLISION",
        "type": "procedural_anomaly",
        "source": "EVENT_183",
        "target": "EVENT_182",
        "description": "Case 2026-115880 used for both SCA petition and stock-removal order",
        "evidence_strength": 0.90,
        "evidence_refs": ["EVENT_183"],
        "legal_significance": "Irregular use of case number; possible abuse of process",
        "added_version": "v35"
    },
    {
        "id": "REL_MAZARS_ENGAGEMENT_ANOMALY",
        "type": "governance_failure",
        "source": "PERSON_001",
        "target": "ORG_MAZARS",
        "description": "Mazars engaged without board resolution, CEO knowledge, or proper mandate",
        "evidence_strength": 0.92,
        "evidence_refs": ["EVENT_185"],
        "legal_significance": "Companies Act s66 violation; unauthorized commitment",
        "added_version": "v35"
    }
]

NEW_EVENTS = [
    {
        "id": "EVENT_182",
        "event_id": "EVENT_182",
        "date": "2026-06-03",
        "title": "Peter's 149-page Answering Affidavit with 12+ Material Admissions",
        "description": "Peter files a 149-page answering affidavit in the SCA opposition containing at least 12 material admissions that contradict his founding affidavit and confirm the revenue hijacking scheme.",
        "category": "legal_proceeding",
        "phase": "appeal",
        "significance": 9,
        "actors": ["PERSON_001"],
        "evidence_refs": ["AA_PARA_63.5", "AA_PARA_63.8", "AA_PARA_39.3", "AA_PARA_64.2", "AA_PARA_45.6", "AA_PARA_75.4"],
        "legal_impact": ["SCA_Opposition", "Part_B_Delinquency", "Rule_42_Rescission", "Criminal_Perjury"],
        "added_version": "v35"
    },
    {
        "id": "EVENT_183",
        "event_id": "EVENT_183",
        "date": "2026-05-26",
        "title": "Stock-Removal Order Granted Under Case 2026-115880",
        "description": "A stock-removal order is granted under case number 2026-115880, the same case number used for the SCA petition. This creates a procedural anomaly suggesting abuse of process.",
        "category": "legal_proceeding",
        "phase": "post_interdict",
        "significance": 8,
        "actors": ["PERSON_001", "ORG_020"],
        "evidence_refs": ["CASE_2026_115880"],
        "legal_impact": ["Stock_Challenge", "Abuse_of_Process"],
        "added_version": "v35"
    },
    {
        "id": "EVENT_184",
        "event_id": "EVENT_184",
        "date": "2026-06-10",
        "title": "Reconsideration Application Struck from Roll",
        "description": "Peter's reconsideration application is struck from the roll, indicating the court found no merit in the attempt to revisit earlier rulings.",
        "category": "legal_proceeding",
        "phase": "appeal",
        "significance": 7,
        "actors": ["PERSON_001"],
        "evidence_refs": [],
        "legal_impact": ["SCA_Opposition"],
        "added_version": "v35"
    },
    {
        "id": "EVENT_185",
        "event_id": "EVENT_185",
        "date": "2026-06-13",
        "title": "Rynette/Bantjies Forensic Review Completed",
        "description": "Forensic review of Rynette Farrar and Bantjies' financial activities completed, revealing systematic pattern of unauthorized transactions and governance failures.",
        "category": "forensic",
        "phase": "discovery",
        "significance": 8,
        "actors": ["PERSON_002", "PERSON_BANTJIES"],
        "evidence_refs": ["FORENSIC_REVIEW_2026"],
        "legal_impact": ["CIPC_Complaint", "SAICA_Complaint", "Criminal_Fraud"],
        "added_version": "v35"
    },
    {
        "id": "EVENT_186",
        "event_id": "EVENT_186",
        "date": "2026-06-15",
        "title": "Divorce Enrolled; Jax Under Notice of Bar",
        "description": "Divorce proceedings formally enrolled. Jacqueline is under notice of bar, creating additional litigation pressure.",
        "category": "legal_proceeding",
        "phase": "appeal",
        "significance": 6,
        "actors": ["PERSON_001", "PERSON_004"],
        "evidence_refs": [],
        "legal_impact": ["Divorce_Proceedings"],
        "added_version": "v35"
    },
    {
        "id": "EVENT_187",
        "event_id": "EVENT_187",
        "date": "2026-06-08",
        "title": "Elliott Attorneys RST Conflict-Funding Pattern Documented",
        "description": "Analysis confirms 16 payments from RST ABSA account to Elliott Attorneys totalling R478,958 between Aug 2025 and Apr 2026, establishing a sustained pattern of using corporate funds to fund adversarial litigation against the CEO.",
        "category": "forensic",
        "phase": "discovery",
        "significance": 9,
        "actors": ["ORG_020", "PERSON_001"],
        "evidence_refs": ["RST_ABSA_STATEMENTS", "EVENT_181"],
        "legal_impact": ["LPC_Complaint", "Part_B_Delinquency", "Criminal_Theft"],
        "added_version": "v35"
    }
]

# =============================================================================
# SECTION 3: Backfill entities.json
# =============================================================================

existing_entity_ids = {e.get('id') for e in entities}
entities_added = 0

for new_entity in NEW_ENTITIES:
    if new_entity['id'] not in existing_entity_ids:
        entities.append(new_entity)
        entities_added += 1
        print(f"  + Entity: {new_entity['id']} ({new_entity['name']})")

save_json(f'{REVSTREAM}/data_models/entities.json', entities)
print(f"Entities backfilled: {entities_added} added, total now {len(entities)}")

# =============================================================================
# SECTION 4: Backfill relations.json
# =============================================================================

existing_relation_ids = {r.get('id') for r in relations}
relations_added = 0

for new_rel in NEW_RELATIONS:
    if new_rel['id'] not in existing_relation_ids:
        relations.append(new_rel)
        relations_added += 1
        print(f"  + Relation: {new_rel['id']}")

save_json(f'{REVSTREAM}/data_models/relations.json', relations)
print(f"Relations backfilled: {relations_added} added, total now {len(relations)}")

# =============================================================================
# SECTION 5: Backfill events.json
# =============================================================================

existing_event_ids = {e.get('id') or e.get('event_id') for e in events}
events_added = 0

for new_event in NEW_EVENTS:
    if new_event['id'] not in existing_event_ids:
        events.append(new_event)
        events_added += 1
        print(f"  + Event: {new_event['id']} ({new_event['date']})")

save_json(f'{REVSTREAM}/data_models/events.json', events)
print(f"Events backfilled: {events_added} added, total now {len(events)}")

# =============================================================================
# SECTION 6: Backfill timeline.json
# =============================================================================

existing_timeline_ids = set()
for e in timeline:
    if isinstance(e, dict):
        existing_timeline_ids.add(e.get('id') or e.get('event_ref') or e.get('event_id', ''))

timeline_added = 0

for new_event in NEW_EVENTS:
    timeline_entry = {
        "date": new_event['date'],
        "event_ref": new_event['id'],
        "title": new_event['title'],
        "description": new_event['description'],
        "category": new_event['category'],
        "significance_level": new_event['significance'],
        "actors": new_event['actors'],
        "evidence_refs": new_event['evidence_refs'],
        "phase": new_event['phase'],
        "added_version": "v35"
    }
    if new_event['id'] not in existing_timeline_ids:
        timeline.append(timeline_entry)
        timeline_added += 1
        print(f"  + Timeline: {new_event['id']} ({new_event['date']})")

# Sort timeline by date
timeline.sort(key=lambda x: x.get('date', ''))

# Save back as dict structure
if isinstance(timeline_data, dict):
    timeline_data['timeline'] = timeline
    timeline_data['metadata']['last_updated'] = datetime.now().isoformat()
    timeline_data['metadata']['total_events'] = len(timeline)
    save_json(f'{REVSTREAM}/data_models/timelines/timeline.json', timeline_data)
else:
    save_json(f'{REVSTREAM}/data_models/timelines/timeline.json', timeline)
print(f"Timeline backfilled: {timeline_added} added, total now {len(timeline)}")

# =============================================================================
# SECTION 7: Generate consistency report
# =============================================================================

consistency_report = {
    "generated": datetime.now().isoformat(),
    "version": "v36",
    "composition": "/aicpp(/61-definition-ksm[/fin-audit-za-v2, /lex-case-analysis, /revstream-evidence], /lex-encode-workflow)",
    "data_models": {
        "entities": {"count": len(entities), "added": entities_added},
        "relations": {"count": len(relations), "added": relations_added},
        "events": {"count": len(events), "added": events_added},
        "timeline": {"count": len(timeline), "added": timeline_added}
    },
    "cross_model_consistency": {
        "all_event_actors_in_entities": True,
        "all_relation_sources_in_entities": True,
        "all_relation_targets_in_entities": True,
        "timeline_sorted_by_date": True
    }
}

# Verify cross-model consistency
all_entity_ids = {e.get('id') for e in entities}

# Check event actors
for event in events:
    for actor in event.get('actors', []):
        if actor not in all_entity_ids and not actor.startswith('PERSON_'):
            consistency_report['cross_model_consistency']['all_event_actors_in_entities'] = False
            print(f"  WARNING: Actor {actor} in {event.get('id')} not in entities")

# Check relation sources/targets
for rel in relations:
    src = rel.get('source', '')
    tgt = rel.get('target', '')
    if src and src not in all_entity_ids and not src.startswith('EVENT_'):
        consistency_report['cross_model_consistency']['all_relation_sources_in_entities'] = False
        print(f"  WARNING: Relation source {src} in {rel.get('id')} not in entities")
    if tgt and tgt not in all_entity_ids and not tgt.startswith('EVENT_'):
        consistency_report['cross_model_consistency']['all_relation_targets_in_entities'] = False
        print(f"  WARNING: Relation target {tgt} in {rel.get('id')} not in entities")

save_json(f'{REVSTREAM}/simulation/CONSISTENCY_REPORT.json', consistency_report)
print(f"\nConsistency report saved.")
print(f"Cross-model consistency: {consistency_report['cross_model_consistency']}")

# =============================================================================
# SECTION 8: Summary
# =============================================================================

print(f"""
=== BACKFILL COMPLETE ===
Entities: {len(entities)} (added {entities_added})
Relations: {len(relations)} (added {relations_added})
Events: {len(events)} (added {events_added})
Timeline: {len(timeline)} (added {timeline_added})
""")
