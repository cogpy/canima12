#!/usr/bin/env python3
"""
Gap Analysis: Cross-check all uploaded evidence files against current hypergraph mesh.
Identifies missing entities, relations, events, and evidence references.
"""
import json
import os
import glob

BASE = '/home/ubuntu/revstream1'

def load_json(path):
    with open(path) as f:
        return json.load(f)

# Load canonical data models
entities = load_json(f'{BASE}/data_models/entities/entities.json')
relations = load_json(f'{BASE}/data_models/relations/relations.json')
events = load_json(f'{BASE}/data_models/events/events.json')
timeline = load_json(f'{BASE}/data_models/timelines/timeline.json')

# Handle different formats
if isinstance(entities, list):
    entity_ids = set(e.get('id','') for e in entities if isinstance(e, dict))
elif isinstance(entities, dict):
    entity_ids = set(entities.keys())
else:
    entity_ids = set()

if isinstance(relations, list):
    relation_ids = set(r.get('id','') for r in relations if isinstance(r, dict))
elif isinstance(relations, dict):
    relation_ids = set(relations.keys())
else:
    relation_ids = set()

if isinstance(events, list):
    event_ids = set(e.get('id','') for e in events if isinstance(e, dict))
elif isinstance(events, dict):
    event_ids = set(events.keys())
else:
    event_ids = set()

if isinstance(timeline, list):
    timeline_ids = set(t.get('id','') if isinstance(t, dict) else '' for t in timeline)
elif isinstance(timeline, dict):
    timeline_ids = set(timeline.keys())
else:
    timeline_ids = set()

print(f"=== CURRENT MODEL STATE ===")
print(f"Entities: {len(entity_ids)}")
print(f"Relations: {len(relation_ids)}")
print(f"Events: {len(event_ids)}")
print(f"Timeline: {len(timeline_ids) if timeline_ids else len(timeline)}")
print()

# Categorize events
h_events = sorted([e for e in event_ids if e.startswith('EVENT_H')])
d_events = sorted([e for e in event_ids if e.startswith('EVENT_D')])
numbered = sorted([e for e in event_ids if e.startswith('EVENT_') and e[6:].isdigit()], key=lambda x: int(x.split('_')[1]))

print(f"EVENT_H series: {len(h_events)} -> {h_events[:5]}...")
print(f"EVENT_D series: {len(d_events)} -> {d_events[:5]}...")
print(f"Numbered events: {len(numbered)} (range: {numbered[0] if numbered else 'none'} to {numbered[-1] if numbered else 'none'})")
print()

# Check gaps in numbered events
if numbered:
    nums = [int(e.split('_')[1]) for e in numbered]
    max_num = max(nums)
    missing_nums = [n for n in range(1, max_num+1) if n not in nums]
    print(f"Missing numbered events (gaps in sequence): {len(missing_nums)}")
    if missing_nums:
        print(f"  Gaps: {missing_nums[:30]}{'...' if len(missing_nums) > 30 else ''}")
    print()

# === BURDEN OF PROOF CROSS-CHECK ===
print("=== BURDEN OF PROOF CROSS-CHECK ===")
bop_file = '/home/ubuntu/upload/BURDEN_OF_PROOF_ENHANCED_2025_12_04.json'
if os.path.exists(bop_file):
    bop = load_json(bop_file)
    bop_event_ids = set()
    for category in bop.get('filing_categories', {}).values():
        for evt in category.get('events', []):
            if isinstance(evt, dict):
                bop_event_ids.add(evt.get('event_id', ''))
    
    missing_from_bop = bop_event_ids - event_ids
    print(f"Events in burden-of-proof JSON: {len(bop_event_ids)}")
    print(f"Missing from current model: {len(missing_from_bop)}")
    for m in sorted(missing_from_bop):
        print(f"  MISSING: {m}")
    print()

# === CONSPIRACY TIMELINE CROSS-CHECK ===
print("=== CONSPIRACY TIMELINE CROSS-CHECK ===")
conspiracy_events = [
    ("2023-02-20", "Ketoni incorporated", "EVENT_H_KETONI_INC"),
    ("2023-02-28", "R1.035M owed to ReZonance", "EVENT_D001"),
    ("2023-04-24", "FFT receives KIH shares", "EVENT_H_KIH_SHARES"),
    ("2023-05-01", "Bantjies joins George Group", "EVENT_H_BANTJIES_GEORGE"),
    ("2023-07-13", "Kayla murdered", "EVENT_H010"),
    ("2023-07-31", "Cards expire except RWD", "EVENT_H_CARDS_EXPIRE"),
    ("2024-02-14", "ReZonance dissolution pressure", "EVENT_H_REZONANCE_PRESSURE"),
    ("2024-07-01", "Bantjies appointed Trustee", "EVENT_H_BANTJIES_TRUSTEE"),
    ("2025-06-06", "Daniel reports fraud to Bantjies", "EVENT_011"),
    ("2025-06-10", "Bantjies impartiality email", "EVENT_H_BANTJIES_IMPARTIAL"),
    ("2025-06-11", "Email domain hijacking letter", "EVENT_H_DOMAIN_HIJACK"),
    ("2025-06-20", "Sage screenshot email control", "EVENT_090"),
    ("2025-07-01", "Trustee appointment backdated", "EVENT_H_TRUSTEE_BACKDATE"),
    ("2025-07-06", "Email hijacking notification", "EVENT_H_EMAIL_HIJACK_NOTIF"),
    ("2025-08-11", "Trustee appointment signed", "EVENT_H_TRUSTEE_SIGNED"),
    ("2025-08-12", "Jax forwards Phishing", "EVENT_H_JAX_PHISHING"),
    ("2025-08-13", "Interdict filed", "EVENT_012"),
    ("2025-08-25", "Sage subscription control", "EVENT_H_SAGE_SUB"),
    ("2025-08-27", "Bantjies impartiality request", "EVENT_H_BANTJIES_IMPARTIAL2"),
    ("2025-09-11", "R1.73M bank transfer", "EVENT_H_R173M_TRANSFER"),
]

# Check which conspiracy events exist in model (by date match or ID)
event_dates = {}
if isinstance(events, list):
    for e in events:
        if isinstance(e, dict):
            event_dates[e.get('date','')] = event_dates.get(e.get('date',''), [])
            event_dates[e.get('date','')].append(e.get('id',''))

missing_conspiracy = []
for date, title, suggested_id in conspiracy_events:
    found = suggested_id in event_ids
    if not found:
        # Check by date
        if date in event_dates:
            found = True
    if not found:
        missing_conspiracy.append((date, title, suggested_id))

print(f"Conspiracy timeline events: {len(conspiracy_events)}")
print(f"Missing from model: {len(missing_conspiracy)}")
for date, title, sid in missing_conspiracy:
    print(f"  MISSING: {date} - {title} ({sid})")
print()

# === ENTITY CROSS-CHECK ===
print("=== ENTITY CROSS-CHECK ===")
# Entities mentioned in conspiracy/burden-of-proof that should exist
required_entities = [
    "PERSON_001",  # Peter
    "PERSON_002",  # Rynette
    "PERSON_003",  # Daniel
    "PERSON_004",  # Jacqueline
    "PERSON_005",  # Kayla
    "PERSON_006",  # Linda Kruger
    "PERSON_007",  # Danie Bantjies
    "PERSON_008",  # Kevin Derrick
    "PERSON_013",  # Kayla Pretorius
    "ORG_001",     # RST
    "ORG_002",     # RWW/RWD
    "ORG_003",     # Villa Via
    "ORG_004",     # SLG
    "ORG_005",     # RegimA SA
    "ORG_006",     # ReZonance
    "ORG_007",     # Ian Levitt Attorneys
    "ORG_008",     # FFT
    "ORG_009",     # Ketoni
    "ORG_010",     # Addarory/Adderory
    "ORG_011",     # Elliott Attorneys
    "PLATFORM_001", # Shopify
]
missing_entities = [e for e in required_entities if e not in entity_ids]
print(f"Required entities: {len(required_entities)}")
print(f"Missing: {len(missing_entities)}")
for m in missing_entities:
    print(f"  MISSING: {m}")
print()

# === EVIDENCE FILE CROSS-CHECK ===
print("=== EVIDENCE FILE COVERAGE ===")
evidence_mapping_file = '/home/ubuntu/upload/AD_RES_J7_KEY_EVIDENCE_MAPPING_2026_01_03.json'
if os.path.exists(evidence_mapping_file):
    evidence_map = load_json(evidence_mapping_file)
    all_evidence_entities = set()
    all_evidence_events = set()
    for key, val in evidence_map.items():
        if isinstance(val, dict):
            for eid in val.get('entities', []):
                all_evidence_entities.add(eid)
            for eid in val.get('events', []):
                all_evidence_events.add(eid)
    
    missing_ev_entities = all_evidence_entities - entity_ids
    missing_ev_events = all_evidence_events - event_ids
    print(f"Evidence mapping references {len(all_evidence_entities)} entities, {len(all_evidence_events)} events")
    print(f"Missing entities from evidence map: {missing_ev_entities}")
    print(f"Missing events from evidence map: {missing_ev_events}")
    print()

# === DOCS vs DATA_MODELS SYNC CHECK ===
print("=== DOCS vs DATA_MODELS SYNC ===")
docs_events_path = f'{BASE}/docs/data_models/events.json'
docs_entities_path = f'{BASE}/docs/data_models/entities/entities.json'
if os.path.exists(docs_events_path):
    docs_events = load_json(docs_events_path)
    if isinstance(docs_events, list):
        docs_event_ids = set(e.get('id','') for e in docs_events if isinstance(e, dict))
    elif isinstance(docs_events, dict):
        docs_event_ids = set(docs_events.keys())
    else:
        docs_event_ids = set()
    
    only_in_canonical = event_ids - docs_event_ids
    only_in_docs = docs_event_ids - event_ids
    print(f"Canonical events: {len(event_ids)}, Docs events: {len(docs_event_ids)}")
    print(f"Only in canonical (not synced to docs): {len(only_in_canonical)}")
    if only_in_canonical:
        print(f"  {sorted(only_in_canonical)[:10]}...")
    print(f"Only in docs (orphaned): {len(only_in_docs)}")
    if only_in_docs:
        print(f"  {sorted(only_in_docs)[:10]}...")
else:
    print(f"Docs events file not found at expected path")
    # Try alternate
    alt = f'{BASE}/docs/data_models/events.json'
    if os.path.exists(alt):
        print(f"  Found at: {alt}")

print()
print("=== SUMMARY ===")
print(f"Total gaps identified for backfill")
