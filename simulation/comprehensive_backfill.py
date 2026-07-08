#!/usr/bin/env python3
"""
Comprehensive Backfill: Reconcile all data layers and add missing evidence
from uploaded historical filings into the canonical data models.

Composition: /iterative-micro-improvement + /fincosys-account-perfect

Steps:
1. Load all canonical data models (entities, relations, events, timeline)
2. Extract missing events from burden-of-proof, conspiracy timeline, and uploaded filings
3. Add v35/v36 events to canonical events.json
4. Reconcile timeline across all layers
5. Sync canonical → docs/data_models/
6. Generate consistency report
"""
import json
import os
import copy
from datetime import datetime

BASE = '/home/ubuntu/revstream1'
UPLOAD = '/home/ubuntu/upload'

def load_json(path):
    with open(path) as f:
        return json.load(f)

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Saved: {path}")

# ============================================================
# STEP 1: Load canonical data models
# ============================================================
print("=" * 70)
print("STEP 1: Loading canonical data models")
print("=" * 70)

ent_data = load_json(f'{BASE}/data_models/entities/entities.json')
rel_data = load_json(f'{BASE}/data_models/relations/relations.json')
evt_data = load_json(f'{BASE}/data_models/events/events.json')
tl_data = load_json(f'{BASE}/data_models/timelines/timeline.json')

# Extract working lists
persons = ent_data.get('entities', {}).get('persons', [])
orgs = ent_data.get('entities', {}).get('organizations', [])
entity_ids = set(p.get('entity_id', '') for p in persons) | set(o.get('entity_id', '') for o in orgs)

if isinstance(rel_data, dict) and 'relations' in rel_data:
    relations_container = rel_data['relations']
    if isinstance(relations_container, dict):
        relations = relations_container  # dict of relation_id -> relation_obj
        relation_ids = set(relations.keys())
    else:
        relations = relations_container  # list
        relation_ids = set(r.get('relation_id', r.get('id', '')) for r in relations if isinstance(r, dict))
elif isinstance(rel_data, list):
    relations = rel_data
    relation_ids = set(r.get('relation_id', r.get('id', '')) for r in relations if isinstance(r, dict))
else:
    relations = {}
    relation_ids = set()
relations_is_dict = isinstance(relations, dict)

events = evt_data.get('events', [])
event_ids = set(e.get('event_id', e.get('id', '')) for e in events if isinstance(e, dict))

if isinstance(tl_data, dict) and 'timeline' in tl_data:
    timeline = tl_data['timeline']
elif isinstance(tl_data, list):
    timeline = tl_data
else:
    timeline = []

print(f"  Entities: {len(entity_ids)} ({len(persons)} persons + {len(orgs)} orgs)")
print(f"  Relations: {len(relations)}")
print(f"  Events: {len(events)} (unique IDs: {len(event_ids)})")
print(f"  Timeline: {len(timeline)} entries")

# ============================================================
# STEP 2: Add v35/v36 events to canonical events.json
# ============================================================
print("\n" + "=" * 70)
print("STEP 2: Adding v35/v36 events to canonical events.json")
print("=" * 70)

v35_events = [
    {
        "event_id": "EVENT_182",
        "title": "Peter's 149-Page Answering Affidavit with 12+ Material Admissions",
        "date": "2026-06-03",
        "category": "legal_proceedings",
        "description": "Peter swears answering affidavit (SAPS Bedfordview, Elliott ref KF0019) containing admissions at paras 39.3, 45.6, 53.3, 62.4, 63.5, 63.8, 64.2, 65.3, 75.4, 77.2, 83.2, 84.9, 185.2 that contradict the founding narrative",
        "actors": ["PERSON_001"],
        "entities_involved": ["PERSON_001", "ORG_020"],
        "financial_impact": "N/A",
        "evidence_refs": ["F-first-respondents-answering-affidavit.pdf"],
        "legal_significance": "fatal_admissions_destroying_founding_narrative",
        "significance_level": 10,
        "added_version": "v35"
    },
    {
        "event_id": "EVENT_183",
        "title": "Stock Order Case 2026-115880 Filed — Same Case Number Collision",
        "date": "2026-06-05",
        "category": "legal_proceedings",
        "description": "Peter files stock order application that receives same case number 2026-115880 as Jax's reconsideration — creating procedural collision",
        "actors": ["PERSON_001"],
        "entities_involved": ["PERSON_001", "PERSON_004"],
        "financial_impact": "N/A",
        "evidence_refs": ["Case 2026-115880 stock order papers"],
        "legal_significance": "case_number_collision_procedural_anomaly",
        "significance_level": 7,
        "added_version": "v35"
    },
    {
        "event_id": "EVENT_184",
        "title": "Reconsideration Struck from Roll for Want of Urgency",
        "date": "2026-06-10",
        "category": "legal_proceedings",
        "description": "Case 2026-115880 reconsideration struck from roll — no order as to costs, merits not determined, interim order stands",
        "actors": ["PERSON_004"],
        "entities_involved": ["PERSON_004"],
        "financial_impact": "N/A",
        "evidence_refs": ["Pool email 10 Jun 18:04", "LETTER TO ELLIOT 10.06.2026.doc"],
        "legal_significance": "reconsideration_struck_interim_order_stands",
        "significance_level": 7,
        "added_version": "v35"
    },
    {
        "event_id": "EVENT_185",
        "title": "Rynette Farrar / Danie Bantjies Forensic Review Completed",
        "date": "2026-06-13",
        "category": "forensic_analysis",
        "description": "Comprehensive forensic review of Rynette Farrar and Danie Bantjies completed — documents full control structure",
        "actors": ["PERSON_002", "PERSON_007"],
        "entities_involved": ["PERSON_002", "PERSON_007"],
        "financial_impact": "R18,750,000",
        "evidence_refs": ["Rynette_Farrar_Danie_Bantjes_Forensic_Review.docx/pdf"],
        "legal_significance": "comprehensive_forensic_proof_of_conspiracy",
        "significance_level": 8,
        "added_version": "v35"
    },
    {
        "event_id": "EVENT_186",
        "title": "Divorce Enrolled — Jax Under Notice of Bar",
        "date": "2026-06-15",
        "category": "legal_proceedings",
        "description": "Divorce proceedings (case 2026-034662) enrolled with Jax under notice of bar",
        "actors": ["PERSON_001", "PERSON_004"],
        "entities_involved": ["PERSON_001", "PERSON_004"],
        "financial_impact": "N/A",
        "evidence_refs": ["07_JUNE_FILINGS_ANALYSIS §2.6"],
        "legal_significance": "divorce_weaponization_pattern",
        "significance_level": 6,
        "added_version": "v35"
    },
    {
        "event_id": "EVENT_187",
        "title": "Elliott Attorneys RST Conflict-Funding Pattern Documented",
        "date": "2026-06-08",
        "category": "forensic_analysis",
        "description": "Full R478,957.93 payment schedule from RST ABSA account to Elliott Attorneys documented and analyzed — 11 payments Aug 2025 to Apr 2026",
        "actors": ["PERSON_001", "ORG_020"],
        "entities_involved": ["PERSON_001", "ORG_020", "ORG_001"],
        "financial_impact": "R478,957.93",
        "evidence_refs": ["RST_ABSA_4112241409_ELLIOTT_ATTORNEYS_PAYMENTS_2025-08_2026-04.txt"],
        "legal_significance": "conflict_of_interest_funding_proof",
        "significance_level": 9,
        "added_version": "v35"
    }
]

added_v35 = 0
for evt in v35_events:
    if evt['event_id'] not in event_ids:
        events.append(evt)
        event_ids.add(evt['event_id'])
        added_v35 += 1
        print(f"  Added: {evt['event_id']} - {evt['title'][:60]}")

print(f"  Total v35 events added: {added_v35}")

# ============================================================
# STEP 3: Add conspiracy timeline events missing from model
# ============================================================
print("\n" + "=" * 70)
print("STEP 3: Adding conspiracy timeline events")
print("=" * 70)

conspiracy_events = [
    {
        "event_id": "EVENT_H013",
        "title": "Ketoni Investment Holdings Incorporated",
        "date": "2023-02-20",
        "category": "conspiracy_preparation",
        "description": "Ketoni Investment Holdings incorporated — vehicle for R18.75M debt to FFT",
        "actors": ["PERSON_008"],
        "entities_involved": ["ORG_009", "PERSON_008"],
        "financial_impact": "R18,750,000",
        "evidence_refs": ["CIPC registration documents"],
        "legal_significance": "vehicle_for_r18_75m_debt",
        "significance_level": 9,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H014",
        "title": "FFT Receives Ketoni Share Certificate #3",
        "date": "2023-04-24",
        "category": "conspiracy_preparation",
        "description": "Faucitt Family Trust receives Ketoni Investment Holdings share certificate #3 — R18.75M claim established",
        "actors": ["PERSON_007"],
        "entities_involved": ["ORG_008", "ORG_009"],
        "financial_impact": "R18,750,000",
        "evidence_refs": ["Share Certificate #3"],
        "legal_significance": "r18_75m_claim_established",
        "significance_level": 10,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H015",
        "title": "Bantjies Joins George Group (Kevin Derrick Connection)",
        "date": "2023-05-01",
        "category": "conspiracy_preparation",
        "description": "Bantjies joins George Group establishing connection to Kevin Derrick (Ketoni director)",
        "actors": ["PERSON_007", "PERSON_008"],
        "entities_involved": ["PERSON_007", "PERSON_008", "ORG_009"],
        "financial_impact": "N/A",
        "evidence_refs": ["George Group records"],
        "legal_significance": "bantjies_ketoni_connection_established",
        "significance_level": 8,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H016",
        "title": "Bank Cards Expire Except RWD — Expense Dumping Begins",
        "date": "2023-07-31",
        "category": "financial_manipulation",
        "description": "All bank cards expire EXCEPT RegimA Worldwide Distribution — forces all expenses to Daniel's company. 18 days after Kayla's murder.",
        "actors": ["PERSON_002"],
        "entities_involved": ["ORG_002", "PERSON_003"],
        "financial_impact": "Unknown (systematic)",
        "evidence_refs": ["Bank card expiry records", "RWD statements"],
        "legal_significance": "expense_dumping_mechanism_activated",
        "significance_level": 8,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H017",
        "title": "ReZonance Dissolution Pressure Meeting",
        "date": "2024-02-14",
        "category": "conspiracy_execution",
        "description": "Meeting to pressure Daniel to dissolve ReZonance (R1.035M creditor) — all three conspirators present",
        "actors": ["PERSON_001", "PERSON_002", "PERSON_007"],
        "entities_involved": ["PERSON_001", "PERSON_002", "PERSON_007", "ORG_006"],
        "financial_impact": "R1,035,000",
        "evidence_refs": ["Meeting notes Feb 14 2024"],
        "legal_significance": "creditor_elimination_attempt",
        "significance_level": 9,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H019",
        "title": "Bantjies Appointed Trustee of FFT (Covert)",
        "date": "2024-07-01",
        "category": "conspiracy_execution",
        "description": "Bantjies covertly appointed as Trustee of Faucitt Family Trust — creates 2-vs-1 majority (Peter + Bantjies vs Jax)",
        "actors": ["PERSON_007", "PERSON_002"],
        "entities_involved": ["PERSON_007", "ORG_008"],
        "financial_impact": "R18,750,000 (control)",
        "evidence_refs": ["Trust amendment documents"],
        "legal_significance": "majority_control_created_over_trust",
        "significance_level": 9,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_090",
        "title": "Sage Screenshot — Rynette Controls Pete@regima.com",
        "date": "2025-06-20",
        "category": "evidence_documentation",
        "description": "Sage account screenshot shows Rynette Farrar logged in as Pete@regima.com — proves she controls Peter's email identity",
        "actors": ["PERSON_002"],
        "entities_involved": ["PERSON_002", "PERSON_001"],
        "financial_impact": "N/A",
        "evidence_refs": ["SF2_Sage_Screenshots_Rynette_Control.md", "Sage screenshot 2025-06-20"],
        "legal_significance": "identity_fraud_proof_rynette_controls_peter",
        "significance_level": 10,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_091",
        "title": "Addarory Company Registration and Stock Supply Arrangement",
        "date": "2021-04-01",
        "category": "conspiracy_preparation",
        "description": "Addarory (Rynette's company) registered and stock supply arrangement established — parallel supply chain created",
        "actors": ["PERSON_002"],
        "entities_involved": ["PERSON_002", "ORG_010"],
        "financial_impact": "R5,400,000",
        "evidence_refs": ["SF5_Adderory_Company_Registration_Stock_Supply.md", "CIPC records"],
        "legal_significance": "parallel_supply_chain_for_revenue_diversion",
        "significance_level": 9,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H020",
        "title": "Bantjies Impartiality Email — False Neutrality Claim",
        "date": "2025-06-10",
        "category": "conspiracy_execution",
        "description": "Bantjies sends 'impartiality' email claiming neutrality while concealing Trustee status (appointed July 2024)",
        "actors": ["PERSON_007"],
        "entities_involved": ["PERSON_007", "PERSON_003", "PERSON_001", "PERSON_004"],
        "financial_impact": "N/A",
        "evidence_refs": ["Email 2025-06-10 09:58", "JUNE_6_10_EMAILS_DANIE_BANTJIES.txt"],
        "legal_significance": "false_impartiality_concealing_trustee_status",
        "significance_level": 9,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H021",
        "title": "Email Domain Hijacking Letter to Clients",
        "date": "2025-06-11",
        "category": "conspiracy_execution",
        "description": "Rynette sends letter to clients instructing them not to use regima.zone emails — ONE DAY after Bantjies creates delay",
        "actors": ["PERSON_002"],
        "entities_involved": ["PERSON_002", "PERSON_003"],
        "financial_impact": "Revenue diversion",
        "evidence_refs": ["Client letter 2025-06-11"],
        "legal_significance": "communication_severance_coordinated_with_bantjies",
        "significance_level": 9,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H022",
        "title": "Trustee Appointment Backdated 41 Days",
        "date": "2025-07-01",
        "category": "fraud",
        "description": "Peter's Main Trustee appointment letter dated July 1 but actually signed August 11 — 41-day backdating",
        "actors": ["PERSON_001", "PERSON_002"],
        "entities_involved": ["PERSON_001", "ORG_008"],
        "financial_impact": "R18,750,000 (control)",
        "evidence_refs": ["LetterofAppointment11082025.pdf"],
        "legal_significance": "fraudulent_backdating_of_legal_document",
        "significance_level": 9,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H023",
        "title": "Email Hijacking Notification — Impersonation of Daniel",
        "date": "2025-07-06",
        "category": "identity_fraud",
        "description": "Fraudulent email sent from dan@regima.zone claiming Daniel is changing to dan@regima.com — social engineering attack",
        "actors": ["PERSON_002"],
        "entities_involved": ["PERSON_002", "PERSON_003"],
        "financial_impact": "N/A",
        "evidence_refs": ["Email 2025-07-06 06:05:40 UTC"],
        "legal_significance": "identity_fraud_impersonation",
        "significance_level": 8,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H024",
        "title": "Trustee Appointment Signed — Sent to Bantjies as PRIMARY",
        "date": "2025-08-11",
        "category": "conspiracy_execution",
        "description": "Rynette sends trustee appointment to Bantjies as PRIMARY recipient (Peter only CC'd) — proves Bantjies is real controller",
        "actors": ["PERSON_002", "PERSON_007"],
        "entities_involved": ["PERSON_002", "PERSON_007", "PERSON_001"],
        "financial_impact": "N/A",
        "evidence_refs": ["Email 2025-08-11 11:00:24 UTC from rynette@regimaskin.co.za"],
        "legal_significance": "proves_bantjies_is_ultimate_controller",
        "significance_level": 10,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H025",
        "title": "Jax Forwards Trustee Email with 'Phishing' Label",
        "date": "2025-08-12",
        "category": "whistleblowing",
        "description": "Jax forwards trustee appointment email to Daniel labelled 'Phishing' — suspects fraud. ONE DAY before interdict filed against her.",
        "actors": ["PERSON_004"],
        "entities_involved": ["PERSON_004", "PERSON_003"],
        "financial_impact": "N/A",
        "evidence_refs": ["Email 2025-08-12 13:05:07 UTC"],
        "legal_significance": "whistleblower_retaliation_trigger",
        "significance_level": 9,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H026",
        "title": "Sage Subscription Control — Rynette is Subscription Owner",
        "date": "2025-08-25",
        "category": "evidence_documentation",
        "description": "Sage screenshot shows 'To activate your account, please contact Rynette Farrar who is the subscription owner'",
        "actors": ["PERSON_002"],
        "entities_involved": ["PERSON_002", "ORG_002"],
        "financial_impact": "N/A",
        "evidence_refs": ["Sage screenshot 2025-08-25"],
        "legal_significance": "proves_rynette_controls_all_accounting",
        "significance_level": 10,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_H027",
        "title": "R1.73M Unauthorized Bank Transfer",
        "date": "2025-09-11",
        "category": "theft",
        "description": "R1.73M transferred from company account without authorization — fund extraction during 'delay' period",
        "actors": ["PERSON_002", "PERSON_007"],
        "entities_involved": ["PERSON_002", "PERSON_007", "ORG_002"],
        "financial_impact": "R1,730,000",
        "evidence_refs": ["Bank statement 2025-09-11"],
        "legal_significance": "unauthorized_fund_extraction",
        "significance_level": 9,
        "added_version": "v40"
    },
    {
        "event_id": "EVENT_089",
        "title": "Bantjies R18.685M Debt Documentation",
        "date": "2023-04-24",
        "category": "conspiracy_preparation",
        "description": "Documentation establishing Bantjies' connection to R18.685M Ketoni debt and conflict of interest as Trustee",
        "actors": ["PERSON_007"],
        "entities_involved": ["PERSON_007", "ORG_009", "ORG_008"],
        "financial_impact": "R18,685,000",
        "evidence_refs": ["SF1_Bantjies_Debt_Documentation.md"],
        "legal_significance": "establishes_bantjies_conflict_of_interest",
        "significance_level": 10,
        "added_version": "v40"
    }
]

added_conspiracy = 0
for evt in conspiracy_events:
    if evt['event_id'] not in event_ids:
        events.append(evt)
        event_ids.add(evt['event_id'])
        added_conspiracy += 1
        print(f"  Added: {evt['event_id']} - {evt['title'][:60]}")
    else:
        print(f"  Exists: {evt['event_id']}")

print(f"  Total conspiracy events added: {added_conspiracy}")

# ============================================================
# STEP 4: Add missing entities (Mazars, Lerena, Adv Pool, Elliott as ORG_020)
# ============================================================
print("\n" + "=" * 70)
print("STEP 4: Adding missing entities")
print("=" * 70)

new_persons = [
    {
        "entity_id": "PERSON_014",
        "name": "Kevin Derrick",
        "role": "ketoni_director",
        "agent_type": "complicit",
        "involvement_events": 2,
        "primary_actions": ["ketoni_management", "bantjies_connection"],
        "relationships": ["director_of_ketoni", "george_group_connection_to_bantjies"],
        "added_version": "v40"
    },
    {
        "entity_id": "PERSON_015",
        "name": "Advocate Pool",
        "role": "legal_counsel_jax",
        "agent_type": "neutral",
        "involvement_events": 3,
        "primary_actions": ["reconsideration_application", "urgency_argument"],
        "relationships": ["counsel_for_PERSON_004"],
        "added_version": "v40"
    }
]

new_orgs = [
    {
        "entity_id": "ORG_020",
        "name": "Elliott Attorneys",
        "type": "legal_firm",
        "role": "conflicted_attorneys_for_peter",
        "involvement_events": 5,
        "primary_actions": ["litigation_funding_from_rst", "conflict_of_interest"],
        "relationships": ["attorneys_for_PERSON_001", "paid_by_ORG_001"],
        "financial_impact": "R478,957.93 received from RST",
        "added_version": "v40"
    },
    {
        "entity_id": "ORG_021",
        "name": "Mazars",
        "type": "audit_firm",
        "role": "external_auditor",
        "involvement_events": 2,
        "primary_actions": ["audit_anomaly", "stock_adjustment_approval"],
        "relationships": ["auditor_of_ORG_004"],
        "added_version": "v40"
    },
    {
        "entity_id": "ORG_022",
        "name": "Lerena Attorneys",
        "type": "legal_firm",
        "role": "attorneys_for_daniel",
        "involvement_events": 2,
        "primary_actions": ["civil_response", "rule42_application"],
        "relationships": ["attorneys_for_PERSON_003"],
        "added_version": "v40"
    }
]

added_entities = 0
for p in new_persons:
    if p['entity_id'] not in entity_ids:
        persons.append(p)
        entity_ids.add(p['entity_id'])
        added_entities += 1
        print(f"  Added person: {p['entity_id']} - {p['name']}")

for o in new_orgs:
    if o['entity_id'] not in entity_ids:
        orgs.append(o)
        entity_ids.add(o['entity_id'])
        added_entities += 1
        print(f"  Added org: {o['entity_id']} - {o['name']}")

print(f"  Total entities added: {added_entities}")

# ============================================================
# STEP 5: Add missing relations from conspiracy evidence
# ============================================================
print("\n" + "=" * 70)
print("STEP 5: Adding missing relations")
print("=" * 70)

new_relations = [
    {
        "relation_id": "REL_037",
        "type": "conspiracy_control",
        "source_entity": "PERSON_007",
        "target_entity": "PERSON_002",
        "description": "Bantjies instructs Rynette — SARS audit email smoking gun",
        "strength": 1.0,
        "evidence_refs": ["SARS audit email", "Trustee appointment email PRIMARY recipient"],
        "legal_significance": "ultimate_controller_relationship",
        "added_version": "v40"
    },
    {
        "relation_id": "REL_038",
        "type": "conspiracy_control",
        "source_entity": "PERSON_002",
        "target_entity": "PERSON_001",
        "description": "Rynette controls Peter — email, accounting, bank access",
        "strength": 1.0,
        "evidence_refs": ["Sage screenshots", "Pete@regima.com control"],
        "legal_significance": "puppet_controller_relationship",
        "added_version": "v40"
    },
    {
        "relation_id": "REL_039",
        "type": "financial_conflict",
        "source_entity": "PERSON_007",
        "target_entity": "ORG_009",
        "description": "Bantjies connected to Ketoni via Kevin Derrick — R18.75M conflict",
        "strength": 0.95,
        "evidence_refs": ["George Group records", "Ketoni share certificate"],
        "legal_significance": "trustee_debtor_conflict_of_interest",
        "added_version": "v40"
    },
    {
        "relation_id": "REL_040",
        "type": "funding_conflict",
        "source_entity": "ORG_001",
        "target_entity": "ORG_020",
        "description": "RST pays Elliott Attorneys R478,957.93 — conflict of interest funding",
        "strength": 0.98,
        "evidence_refs": ["RST ABSA statements", "Elliott payment schedule"],
        "legal_significance": "litigation_funded_by_company_not_director",
        "added_version": "v40"
    },
    {
        "relation_id": "REL_041",
        "type": "parallel_supply_chain",
        "source_entity": "ORG_010",
        "target_entity": "ORG_001",
        "description": "Addarory diverts R5.4M stock from RST/SLG supply chain",
        "strength": 0.95,
        "evidence_refs": ["SLG stock analysis", "Addarory CIPC records"],
        "legal_significance": "revenue_stream_diversion_mechanism",
        "added_version": "v40"
    },
    {
        "relation_id": "REL_042",
        "type": "whistleblower_retaliation",
        "source_entity": "PERSON_001",
        "target_entity": "PERSON_004",
        "description": "Peter files interdict ONE DAY after Jax labels trustee email as 'Phishing'",
        "strength": 0.95,
        "evidence_refs": ["Interdict filing 2025-08-13", "Phishing email 2025-08-12"],
        "legal_significance": "retaliation_against_whistleblower",
        "added_version": "v40"
    },
    {
        "relation_id": "REL_043",
        "type": "identity_fraud",
        "source_entity": "PERSON_002",
        "target_entity": "PERSON_001",
        "description": "Rynette impersonates Peter via Pete@regima.com email control",
        "strength": 1.0,
        "evidence_refs": ["Sage screenshot 2025-06-20"],
        "legal_significance": "identity_fraud_email_impersonation",
        "added_version": "v40"
    },
    {
        "relation_id": "REL_044",
        "type": "audit_anomaly",
        "source_entity": "ORG_021",
        "target_entity": "ORG_004",
        "description": "Mazars approves R5.4M stock adjustment without investigation",
        "strength": 0.92,
        "evidence_refs": ["SLG audit report", "Stock adjustment records"],
        "legal_significance": "professional_negligence_or_complicity",
        "added_version": "v40"
    }
]

added_rels = 0
for rel in new_relations:
    if rel['relation_id'] not in relation_ids:
        if relations_is_dict:
            relations[rel['relation_id']] = rel
        else:
            relations.append(rel)
        relation_ids.add(rel['relation_id'])
        added_rels += 1
        print(f"  Added: {rel['relation_id']} - {rel['description'][:60]}")

print(f"  Total relations added: {added_rels}")

# ============================================================
# STEP 6: Reconcile timeline — merge canonical + docs + v35
# ============================================================
print("\n" + "=" * 70)
print("STEP 6: Reconciling timeline")
print("=" * 70)

# Build unified timeline from all events
timeline_event_refs = set()
for entry in timeline:
    if isinstance(entry, dict):
        ref = entry.get('event_ref', '')
        if ref:
            timeline_event_refs.add(ref)

# Add all events not yet in timeline
added_tl = 0
for evt in events:
    if isinstance(evt, dict):
        eid = evt.get('event_id', evt.get('id', ''))
        if eid and eid not in timeline_event_refs:
            new_entry = {
                "date": evt.get('date', 'unknown'),
                "event_ref": eid,
                "title": evt.get('title', ''),
                "description": evt.get('description', ''),
                "category": evt.get('category', 'unknown'),
                "significance_level": evt.get('significance_level', 5),
                "actors": evt.get('actors', []),
                "entities_involved": evt.get('entities_involved', []),
                "added_date": datetime.now().strftime("%Y-%m-%d"),
                "evidence_refs": evt.get('evidence_refs', [])
            }
            timeline.append(new_entry)
            timeline_event_refs.add(eid)
            added_tl += 1

# Sort timeline by date
timeline.sort(key=lambda x: x.get('date', '9999-99-99') if isinstance(x, dict) else '9999-99-99')

print(f"  Timeline entries added: {added_tl}")
print(f"  Total timeline entries: {len(timeline)}")

# ============================================================
# STEP 7: Save all canonical models
# ============================================================
print("\n" + "=" * 70)
print("STEP 7: Saving canonical models")
print("=" * 70)

# Update metadata
ent_data['metadata']['last_updated'] = datetime.now().isoformat()
ent_data['metadata']['version'] = "40.0_COMPREHENSIVE_BACKFILL_2026_07_06"
ent_data['metadata']['total_entities'] = len(entity_ids)
ent_data['metadata']['total_persons'] = len(persons)
ent_data['metadata']['total_organizations'] = len(orgs)
ent_data['entities']['persons'] = persons
ent_data['entities']['organizations'] = orgs

evt_data['metadata']['last_updated'] = datetime.now().isoformat()
evt_data['metadata']['version'] = "40.0_COMPREHENSIVE_BACKFILL_2026_07_06"
evt_data['events'] = events

rel_data['relations'] = relations
rel_data['metadata'] = rel_data.get('metadata', {})
rel_data['metadata']['last_updated'] = datetime.now().isoformat()
rel_data['metadata']['version'] = "40.0_COMPREHENSIVE_BACKFILL_2026_07_06"

tl_out = {"metadata": {"version": "40.0_COMPREHENSIVE_BACKFILL_2026_07_06", "last_updated": datetime.now().isoformat(), "total_entries": len(timeline)}, "timeline": timeline}

save_json(f'{BASE}/data_models/entities/entities.json', ent_data)
save_json(f'{BASE}/data_models/relations/relations.json', rel_data)
save_json(f'{BASE}/data_models/events/events.json', evt_data)
save_json(f'{BASE}/data_models/timelines/timeline.json', tl_out)

# ============================================================
# STEP 8: Sync canonical → docs/data_models/
# ============================================================
print("\n" + "=" * 70)
print("STEP 8: Syncing canonical → docs/data_models/")
print("=" * 70)

save_json(f'{BASE}/docs/data_models/entities/entities.json', ent_data)
save_json(f'{BASE}/docs/data_models/events.json', evt_data)
save_json(f'{BASE}/docs/data_models/relations.json', rel_data)
save_json(f'{BASE}/docs/data_models/timeline.json', tl_out)

# ============================================================
# STEP 9: Generate consistency report
# ============================================================
print("\n" + "=" * 70)
print("STEP 9: Consistency Report")
print("=" * 70)

# Validate all event actors resolve to entities
unresolved_actors = set()
for evt in events:
    if isinstance(evt, dict):
        for actor in evt.get('actors', []):
            if actor not in entity_ids:
                unresolved_actors.add(actor)

# Validate all relation endpoints resolve
unresolved_endpoints = set()
rel_items = relations.values() if isinstance(relations, dict) else relations
for rel in rel_items:
    if isinstance(rel, dict):
        src = rel.get('source_entity', rel.get('source', ''))
        tgt = rel.get('target_entity', rel.get('target', ''))
        if src and src not in entity_ids:
            unresolved_endpoints.add(src)
        if tgt and tgt not in entity_ids:
            unresolved_endpoints.add(tgt)

report = {
    "version": "v40_COMPREHENSIVE_BACKFILL",
    "timestamp": datetime.now().isoformat(),
    "totals": {
        "entities": len(entity_ids),
        "relations": len(relations),
        "events": len(events),
        "timeline_entries": len(timeline)
    },
    "additions": {
        "v35_events": added_v35,
        "conspiracy_events": added_conspiracy,
        "entities": added_entities,
        "relations": added_rels,
        "timeline_entries": added_tl
    },
    "validation": {
        "unresolved_actors": list(unresolved_actors),
        "unresolved_relation_endpoints": list(unresolved_endpoints),
        "all_actors_resolved": len(unresolved_actors) == 0,
        "all_endpoints_resolved": len(unresolved_endpoints) == 0,
        "timeline_sorted": all(
            timeline[i].get('date', '') <= timeline[i+1].get('date', '')
            for i in range(len(timeline)-1)
            if isinstance(timeline[i], dict) and isinstance(timeline[i+1], dict)
        )
    }
}

save_json(f'{BASE}/simulation/COMPREHENSIVE_BACKFILL_REPORT.json', report)

print(f"\n  Entities: {len(entity_ids)}")
print(f"  Relations: {len(relations)}")
print(f"  Events: {len(events)}")
print(f"  Timeline: {len(timeline)}")
print(f"  Unresolved actors: {unresolved_actors if unresolved_actors else 'NONE'}")
print(f"  Unresolved endpoints: {unresolved_endpoints if unresolved_endpoints else 'NONE'}")
print(f"  Timeline sorted: {report['validation']['timeline_sorted']}")
print(f"\n{'=' * 70}")
print("BACKFILL COMPLETE")
print(f"{'=' * 70}")
