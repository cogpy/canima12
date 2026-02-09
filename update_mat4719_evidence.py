#!/usr/bin/env python3
"""
Update data models with evidence from MAT4719 - NOM, Founding Affidavit & Annexures.
Case: 2025-137857
Document: 1.MAT4719-NOMandFoundingAffidavitandAnnexures.pdf (162 pages)
"""

import json
import os
from datetime import datetime

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
TIMESTAMP = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
DATE_TAG = "2026_02_09"

def load_json(path):
    with open(os.path.join(REPO_DIR, path)) as f:
        return json.load(f)

def save_json(path, data):
    with open(os.path.join(REPO_DIR, path), 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def backup_file(path):
    import shutil
    backup = path + f".backup_{DATE_TAG}"
    full_path = os.path.join(REPO_DIR, path)
    if os.path.exists(full_path):
        shutil.copy2(full_path, os.path.join(REPO_DIR, backup))
        print(f"  Backed up: {path} -> {backup}")

# ============================================================
# 1. UPDATE ENTITIES
# ============================================================
def update_entities():
    print("\n=== UPDATING ENTITIES ===")
    path = "data_models/entities/entities.json"
    backup_file(path)
    data = load_json(path)

    # Update metadata
    data['metadata']['version'] = f"40.0_MAT4719_EVIDENCE_{DATE_TAG}"
    data['metadata']['last_updated'] = TIMESTAMP
    data['metadata']['changes'] = (
        "Integrated MAT4719 NOM & Founding Affidavit evidence: "
        "Added Elliott Attorneys entity, updated Bantjes confirmatory affidavit details, "
        "added FNB international limit evidence, updated financial totals from PF9/PF10 annexures, "
        "added Gayane Williams entity from PF7 communications"
    )

    # Add Elliott Attorneys if not present
    orgs = data['entities'].get('organizations', [])
    elliott_exists = any(o.get('name', '').lower().startswith('elliott') for o in orgs)
    if not elliott_exists:
        orgs.append({
            "entity_id": f"ORG_{len(orgs)+1:03d}",
            "name": "Elliott Attorneys Inc.",
            "abbreviation": "Elliott Att",
            "entity_type": "law_firm",
            "agent_type": "legal_representative_applicant",
            "registration_details": {
                "address": "Office 12, Garsfontein Office Park, 645 Jacqueline Drive, Garsfontein, Pretoria",
                "telephone": "012 012 5067",
                "email": "keegan@elliottattorneys.co.za",
                "reference": "KRE/MM/KF0019"
            },
            "role": "attorney_for_applicant_peter_faucitt",
            "evidence_references": ["MAT4719_NOM_pages_2-9"],
            "case_involvement": "Filed ex parte application on behalf of Peter Faucitt",
            "added_date": TIMESTAMP,
            "source": "MAT4719 Notice of Motion"
        })
        print("  Added: Elliott Attorneys Inc.")

    # Add Gayane Williams if not present
    persons = data['entities'].get('persons', [])
    gayane_exists = any(p.get('name', '').lower().startswith('gayane') for p in persons)
    if not gayane_exists:
        persons.append({
            "entity_id": f"PERSON_{len(persons)+1:03d}",
            "name": "Gayane Williams",
            "aliases": ["Gee"],
            "role": "employee_bookkeeper",
            "agent_type": "witness",
            "involvement_events": 2,
            "evidence_references": ["MAT4719_PF7_pages_72-101"],
            "communications": {
                "email_to_daniel": "31 March 2025 - Details needed to Log In",
                "attachment": "Application Expenses Analysis.xlsx",
                "cc": "jax@regima.com (Jacqui Faucitt)"
            },
            "added_date": TIMESTAMP,
            "source": "MAT4719 Annexure PF7"
        })
        print("  Added: Gayane Williams")

    # Update Bantjes entity with confirmatory affidavit details
    for p in persons:
        if 'bantj' in p.get('name', '').lower():
            p['mat4719_confirmatory_affidavit'] = {
                "sworn_date": "2025-08-13",
                "location": "Pretoria",
                "commissioner": "Hannelle Evert, Chartered Business Accountant (SA), SAIBA16721",
                "commissioner_address": "Libertas Office Park, Block E, Cnr The Highway and Libertas Roads, Equestria 0184",
                "saica_number": "00105928",
                "id_number": "581004 5103 089",
                "role_in_application": "Confirmatory deponent - confirmed Peter's allegations",
                "evidence_reference": "MAT4719_Confirmatory_Affidavit_pages_69-71",
                "void_ab_initio_relevance": "Received Daniel's fraud report on 6 June 2025; certified false affidavit on 13 August 2025"
            }
            print(f"  Updated: {p['name']} with confirmatory affidavit details")

    # Update Peter Faucitt with founding affidavit details
    for p in persons:
        if p.get('entity_id') == 'PERSON_001' or 'peter' in p.get('name', '').lower():
            p['mat4719_founding_affidavit'] = {
                "sworn_date": "2025-08-13",
                "location": "Bedfordview SAPS, 60 Van Buuren Rd, Bedfordview",
                "hearing_date": "2025-08-19",
                "application_type": "ex_parte_urgent",
                "rule_invoked": "Rule 6(12)(a)",
                "address_stated": "20 River Road, Morning Hill, Bedfordview",
                "evidence_reference": "MAT4719_Founding_Affidavit_pages_10-38",
                "key_allegations": [
                    "Respondents misappropriating funds",
                    "R500,000 transferred to 2nd respondent after cards taken",
                    "Fear of concealment/destruction of documents"
                ]
            }
            print(f"  Updated: {p['name']} with founding affidavit details")
            break

    # Add bank account entities for credit card accounts from PF9
    bank_accounts = data['entities'].get('bank_accounts', [])
    cc_accounts = [
        {
            "entity_id": "BANK_CC_001",
            "account_number": "4910505191",
            "account_type": "credit_card",
            "bank_name": "FNB",
            "entity_type": "bank_account",
            "agent_type": "financial_instrument",
            "role": "business_credit_card_for_platform_expenses",
            "transaction_period": "January 2024 - February 2025",
            "evidence_reference": "MAT4719_PF9_pages_102-137",
            "added_date": TIMESTAMP
        },
        {
            "entity_id": "BANK_CC_002",
            "account_number": "4910505225",
            "account_type": "credit_card",
            "bank_name": "FNB",
            "entity_type": "bank_account",
            "agent_type": "financial_instrument",
            "role": "business_credit_card_for_platform_expenses",
            "transaction_period": "January 2024 - February 2025",
            "evidence_reference": "MAT4719_PF9_pages_102-137",
            "added_date": TIMESTAMP
        }
    ]
    for cc in cc_accounts:
        exists = any(b.get('account_number') == cc['account_number'] for b in bank_accounts)
        if not exists:
            bank_accounts.append(cc)
            print(f"  Added bank account: {cc['account_number']}")

    data['entities']['bank_accounts'] = bank_accounts

    # Update total count
    total = sum(len(v) for v in data['entities'].values() if isinstance(v, list))
    data['metadata']['total_entities'] = total

    save_json(path, data)
    print(f"  Saved entities.json (v{data['metadata']['version']}, {total} entities)")

# ============================================================
# 2. UPDATE EVENTS
# ============================================================
def update_events():
    print("\n=== UPDATING EVENTS ===")
    path = "data_models/events/events.json"
    backup_file(path)
    data = load_json(path)

    data['metadata']['version'] = f"36.0_MAT4719_EVIDENCE_{DATE_TAG}"
    data['metadata']['last_updated'] = TIMESTAMP

    events = data['events']
    existing_ids = {e['event_id'] for e in events}

    new_events = [
        {
            "event_id": "EVT_MAT4719_001",
            "date": "2025-08-13",
            "event_type": "legal_filing",
            "category": "litigation",
            "description": "Peter Faucitt swears founding affidavit at Bedfordview SAPS for ex parte urgent application (Case 2025-137857). Affidavit contains material non-disclosures regarding FNB SOLE mandate and R500K context.",
            "entities_involved": ["PERSON_001", "ORG_001", "ORG_002", "ORG_003", "ORG_004"],
            "perpetrators": ["PERSON_001"],
            "victims": ["PERSON_002", "PERSON_003"],
            "location": "Bedfordview SAPS, 60 Van Buuren Rd, Bedfordview",
            "financial_impact": {"amount": 0, "currency": "ZAR", "description": "Application to seize control of all business finances"},
            "significance": "critical",
            "evidence": {
                "primary": "MAT4719_Founding_Affidavit_pages_10-38",
                "document": "1.MAT4719-NOMandFoundingAffidavitandAnnexures.pdf",
                "pages": "10-38"
            },
            "timeline_phase": "weaponized_litigation",
            "related_events": ["EVT_MAT4719_002", "EVT_MAT4719_003"],
            "burden_of_proof": {"civil": 0.95, "criminal": 0.90},
            "refinement_date": TIMESTAMP
        },
        {
            "event_id": "EVT_MAT4719_002",
            "date": "2025-08-13",
            "event_type": "legal_filing",
            "category": "perjury",
            "description": "Daniel Jacobus Bantjes (SAICA 00105928) swears confirmatory affidavit supporting Peter's application, despite having received Daniel Faucitt's fraud report on 6 June 2025. Commissioner: Hannelle Evert (SAIBA16721).",
            "entities_involved": ["PERSON_BANTJES", "PERSON_001"],
            "perpetrators": ["PERSON_BANTJES"],
            "victims": ["PERSON_002", "PERSON_003"],
            "location": "Libertas Office Park, Block E, Equestria, Pretoria",
            "significance": "critical",
            "evidence": {
                "primary": "MAT4719_Confirmatory_Affidavit_pages_69-71",
                "document": "1.MAT4719-NOMandFoundingAffidavitandAnnexures.pdf",
                "pages": "69-71"
            },
            "timeline_phase": "weaponized_litigation",
            "related_events": ["EVT_MAT4719_001"],
            "burden_of_proof": {"civil": 0.95, "criminal": 0.85},
            "refinement_date": TIMESTAMP
        },
        {
            "event_id": "EVT_MAT4719_003",
            "date": "2025-08-14",
            "event_type": "legal_filing",
            "category": "litigation",
            "description": "Ex parte application filed electronically via Court Online at 08:16:25 SAST. Notice of Motion (Long Form) with Part A (interim) and Part B (final) relief. Filed by Elliott Attorneys Inc. (Ref: KRE/MM/KF0019).",
            "entities_involved": ["PERSON_001", "ELLIOTT_ATT"],
            "perpetrators": ["PERSON_001"],
            "victims": ["PERSON_002", "PERSON_003"],
            "location": "High Court of South Africa, Gauteng Division, Pretoria",
            "significance": "critical",
            "evidence": {
                "primary": "MAT4719_NOM_pages_2-9",
                "document": "1.MAT4719-NOMandFoundingAffidavitandAnnexures.pdf",
                "pages": "2-9"
            },
            "timeline_phase": "weaponized_litigation",
            "related_events": ["EVT_MAT4719_001"],
            "burden_of_proof": {"civil": 1.0, "criminal": 1.0},
            "refinement_date": TIMESTAMP
        },
        {
            "event_id": "EVT_MAT4719_004",
            "date": "2025-08-19",
            "event_type": "court_hearing",
            "category": "litigation",
            "description": "Ex parte hearing at 10h00. Court grants interim interdict (Part A) based on Peter's founding affidavit and Bantjes' confirmatory affidavit. Order subsequently subject to void ab initio challenge.",
            "entities_involved": ["PERSON_001", "PERSON_002", "PERSON_003"],
            "perpetrators": ["PERSON_001"],
            "victims": ["PERSON_002", "PERSON_003"],
            "location": "High Court, Gauteng Division, Pretoria",
            "significance": "critical",
            "evidence": {
                "primary": "MAT4719_NOM_pages_2-9",
                "document": "1.MAT4719-NOMandFoundingAffidavitandAnnexures.pdf"
            },
            "timeline_phase": "weaponized_litigation",
            "related_events": ["EVT_MAT4719_001", "EVT_MAT4719_002", "EVT_MAT4719_003"],
            "burden_of_proof": {"civil": 1.0, "criminal": 0.95},
            "refinement_date": TIMESTAMP
        },
        {
            "event_id": "EVT_MAT4719_005",
            "date": "2025-03-31",
            "event_type": "communication",
            "category": "evidence",
            "description": "Gayane Williams emails Daniel Faucitt via Slack requesting login details. Attachment: 'Application Expenses Analysis.xlsx'. CC: Jacqui Faucitt (jax@regima.com). This communication shows legitimate business operations and expense tracking.",
            "entities_involved": ["PERSON_GAYANE", "PERSON_003", "PERSON_002"],
            "significance": "moderate",
            "evidence": {
                "primary": "MAT4719_PF7_pages_72-101",
                "document": "1.MAT4719-NOMandFoundingAffidavitandAnnexures.pdf",
                "pages": "72"
            },
            "timeline_phase": "normal_operations",
            "burden_of_proof": {"civil": 0.80},
            "refinement_date": TIMESTAMP
        },
        {
            "event_id": "EVT_MAT4719_006",
            "date": "2025-04-03",
            "event_type": "communication",
            "category": "evidence",
            "description": "Jacqui Faucitt emails Gayane Williams: 'WE NEED TO STOP PAYING SOME IF THESE WHO REFUSE TO GIVE INVOICES'. This shows Jacqui's active involvement in financial oversight and cost control, contradicting Peter's narrative of misappropriation.",
            "entities_involved": ["PERSON_002", "PERSON_GAYANE"],
            "significance": "high",
            "evidence": {
                "primary": "MAT4719_PF7_page_101",
                "document": "1.MAT4719-NOMandFoundingAffidavitandAnnexures.pdf",
                "pages": "101"
            },
            "timeline_phase": "normal_operations",
            "burden_of_proof": {"civil": 0.90},
            "refinement_date": TIMESTAMP
        },
        {
            "event_id": "EVT_MAT4719_007",
            "date": "2025-07-31",
            "event_type": "financial",
            "category": "evidence",
            "description": "FNB sends SMS to Pete Faucitt: '80% of international limit reached, transactions not allowed over 100% limit.' This evidences the scale of international platform payments and Peter's awareness of the spending.",
            "entities_involved": ["PERSON_001", "BANK_FNB"],
            "significance": "high",
            "evidence": {
                "primary": "MAT4719_PF11_page_162",
                "document": "1.MAT4719-NOMandFoundingAffidavitandAnnexures.pdf",
                "pages": "162"
            },
            "timeline_phase": "pre_litigation",
            "financial_impact": {
                "description": "International transaction limit nearly exhausted - indicates massive platform spend",
                "pf9_total": 6738007,
                "pf10_total": 2116159.47,
                "combined_total": 8854166.47,
                "currency": "ZAR"
            },
            "burden_of_proof": {"civil": 0.85},
            "refinement_date": TIMESTAMP
        }
    ]

    added = 0
    for evt in new_events:
        if evt['event_id'] not in existing_ids:
            events.append(evt)
            existing_ids.add(evt['event_id'])
            added += 1
            print(f"  Added event: {evt['event_id']} - {evt['date']} - {evt['description'][:60]}...")

    data['events'] = events
    save_json(path, data)
    print(f"  Saved events.json ({added} new events, {len(events)} total)")

# ============================================================
# 3. UPDATE RELATIONS
# ============================================================
def update_relations():
    print("\n=== UPDATING RELATIONS ===")
    path = "data_models/relations/relations.json"
    backup_file(path)
    data = load_json(path)

    data['metadata']['version'] = f"18.0_MAT4719_EVIDENCE_{DATE_TAG}"
    data['metadata']['last_updated'] = TIMESTAMP

    # Add legal relations for Elliott Attorneys
    legal_rels = data['relations'].get('legal_relations', [])
    legal_rels.append({
        "relation_id": "REL_LEGAL_ELLIOTT",
        "type": "attorney_client",
        "from_entity": "ELLIOTT_ATT",
        "to_entity": "PERSON_001",
        "description": "Elliott Attorneys Inc. represents Peter Faucitt in ex parte application (Case 2025-137857)",
        "reference": "KRE/MM/KF0019",
        "evidence": "MAT4719_NOM_pages_2-9",
        "added_date": TIMESTAMP
    })
    data['relations']['legal_relations'] = legal_rels
    print("  Added: Elliott Attorneys -> Peter Faucitt (attorney-client)")

    # Add professional relations for Bantjes confirmatory affidavit
    prof_rels = data['relations'].get('professional_relations', [])
    prof_rels.append({
        "relation_id": "REL_PROF_BANTJES_CONFIRM",
        "type": "confirmatory_deponent",
        "from_entity": "PERSON_BANTJES",
        "to_entity": "PERSON_001",
        "description": "Bantjes swore confirmatory affidavit supporting Peter's ex parte application on 13 Aug 2025, despite receiving Daniel's fraud report on 6 June 2025",
        "evidence": "MAT4719_Confirmatory_Affidavit_pages_69-71",
        "void_ab_initio_relevance": "Perjury with provable foreknowledge - 68 days between fraud report and false affidavit",
        "added_date": TIMESTAMP
    })
    data['relations']['professional_relations'] = prof_rels
    print("  Added: Bantjes -> Peter (confirmatory deponent with foreknowledge)")

    # Add financial relations for credit card accounts
    fin_rels = data['relations'].get('financial_relations', [])
    fin_rels.append({
        "relation_id": "REL_FIN_CC_PF9",
        "type": "credit_card_expenditure",
        "from_entity": "ORG_001",
        "accounts": ["4910505191", "4910505225"],
        "description": "RegimA Worldwide Distribution credit card expenditure on technology platforms (Jan 2024 - Feb 2025). Total: R6,738,007",
        "financial_impact": {"amount": 6738007, "currency": "ZAR"},
        "evidence": "MAT4719_PF9_pages_102-137",
        "vendors_include": ["Shopify", "GitHub", "Cloudflare", "Vercel", "Google Suite", "Microsoft", "Wix", "Auth0", "OpenAI", "Slack", "Notion Labs"],
        "added_date": TIMESTAMP
    })
    fin_rels.append({
        "relation_id": "REL_FIN_LEDGER_PF10",
        "type": "expense_ledger",
        "from_entity": "ORG_001",
        "description": "RegimA Worldwide Distribution categorised expense ledger (Mar - Jul 2025). Total: R2,116,159.47",
        "financial_impact": {"amount": 2116159.47, "currency": "ZAR"},
        "categories": {
            "3300/020_Computer_Platforms": "Primary category",
            "3300/030_Computer_Software": "Software licenses",
            "3300/040_Shopify_Connectors": "E-commerce integrations",
            "3300/050_Computer_Apps": "Application subscriptions",
            "3300/060_Computer_Other": "Miscellaneous tech"
        },
        "monthly_totals": {
            "March_2025": 625764.79,
            "April_2025": 595747.46,
            "May_2025": 510795.53,
            "June_2025": 267392.84,
            "July_2025": 116458.85
        },
        "evidence": "MAT4719_PF10_pages_138-161",
        "added_date": TIMESTAMP
    })
    data['relations']['financial_relations'] = fin_rels
    print("  Added: Credit card expenditure relations (PF9 & PF10)")

    # Add evidence-based relations for communications
    ev_rels = data['relations'].get('evidence_based_relations', [])
    ev_rels.append({
        "relation_id": "REL_EV_PF7_COMMS",
        "type": "communications_evidence",
        "participants": ["PERSON_GAYANE", "PERSON_003", "PERSON_002"],
        "description": "Slack/email communications between Gayane Williams, Daniel Faucitt, and Jacqui Faucitt regarding platform access, expenses, and invoicing (March-April 2025)",
        "evidence": "MAT4719_PF7_pages_72-101",
        "significance": "Shows legitimate business operations and expense oversight, contradicting Peter's misappropriation narrative",
        "added_date": TIMESTAMP
    })
    data['relations']['evidence_based_relations'] = ev_rels
    print("  Added: PF7 communications evidence relation")

    save_json(path, data)
    print(f"  Saved relations.json (v{data['metadata']['version']})")

# ============================================================
# 4. UPDATE TIMELINE
# ============================================================
def update_timeline():
    print("\n=== UPDATING TIMELINE ===")
    path = "data_models/timelines/timeline.json"
    backup_file(path)
    data = load_json(path)

    data['metadata']['version'] = f"33.0_MAT4719_EVIDENCE_{DATE_TAG}"
    data['metadata']['last_updated'] = TIMESTAMP

    timeline = data['timeline']
    existing_dates_events = {(e.get('date', ''), e.get('event', '')[:50]) for e in timeline}

    new_entries = [
        {
            "date": "2025-03-31",
            "event": "Gayane Williams emails Daniel Faucitt requesting login details; attaches 'Application Expenses Analysis.xlsx'; CC: Jacqui Faucitt",
            "entity": "Gayane Williams / Daniel Faucitt / Jacqui Faucitt",
            "source": "MAT4719 Annexure PF7 (page 72)",
            "key_actor_names": ["Gayane Williams", "Daniel Faucitt", "Jacqui Faucitt"],
            "entities_involved": ["PERSON_GAYANE", "PERSON_003", "PERSON_002"],
            "event_ref": "EVT_MAT4719_005",
            "evidence_enhanced_timestamp": TIMESTAMP
        },
        {
            "date": "2025-04-03",
            "event": "Jacqui Faucitt emails Gayane: 'WE NEED TO STOP PAYING SOME IF THESE WHO REFUSE TO GIVE INVOICES' — active financial oversight",
            "entity": "Jacqui Faucitt / Gayane Williams",
            "source": "MAT4719 Annexure PF7 (page 101)",
            "key_actor_names": ["Jacqui Faucitt", "Gayane Williams"],
            "entities_involved": ["PERSON_002", "PERSON_GAYANE"],
            "event_ref": "EVT_MAT4719_006",
            "evidence_enhanced_timestamp": TIMESTAMP
        },
        {
            "date": "2025-07-31",
            "event": "FNB SMS to Pete Faucitt: '80% of international limit reached' — Peter aware of scale of international platform payments",
            "entity": "FNB / Peter Faucitt",
            "source": "MAT4719 Annexure PF11 (page 162)",
            "key_actor_names": ["Peter Faucitt", "FNB"],
            "entities_involved": ["PERSON_001", "BANK_FNB"],
            "event_ref": "EVT_MAT4719_007",
            "evidence_enhanced_timestamp": TIMESTAMP
        },
        {
            "date": "2025-08-13",
            "event": "Peter Faucitt swears founding affidavit at Bedfordview SAPS; Bantjes swears confirmatory affidavit at Equestria, Pretoria — both contain material non-disclosures",
            "entity": "Peter Faucitt / Daniel Bantjes",
            "source": "MAT4719 Founding Affidavit (pages 10-38) & Confirmatory Affidavit (pages 69-71)",
            "key_actor_names": ["Peter Faucitt", "Daniel Bantjes"],
            "entities_involved": ["PERSON_001", "PERSON_BANTJES"],
            "event_ref": "EVT_MAT4719_001",
            "evidence_enhanced_timestamp": TIMESTAMP
        },
        {
            "date": "2025-08-14",
            "event": "Ex parte application filed electronically via Court Online at 08:16:25 SAST by Elliott Attorneys Inc. (Ref: KRE/MM/KF0019)",
            "entity": "Elliott Attorneys / Peter Faucitt",
            "source": "MAT4719 Cover Page (page 1)",
            "key_actor_names": ["Elliott Attorneys", "Peter Faucitt"],
            "entities_involved": ["ELLIOTT_ATT", "PERSON_001"],
            "event_ref": "EVT_MAT4719_003",
            "evidence_enhanced_timestamp": TIMESTAMP
        },
        {
            "date": "2025-08-19",
            "event": "Ex parte hearing at 10h00 — Court grants interim interdict (Part A) based on perjured affidavits; order subsequently challenged as void ab initio",
            "entity": "High Court / Peter Faucitt",
            "source": "MAT4719 Notice of Motion (pages 2-9)",
            "key_actor_names": ["Peter Faucitt"],
            "entities_involved": ["PERSON_001"],
            "event_ref": "EVT_MAT4719_004",
            "evidence_enhanced_timestamp": TIMESTAMP
        }
    ]

    added = 0
    for entry in new_entries:
        key = (entry['date'], entry['event'][:50])
        if key not in existing_dates_events:
            timeline.append(entry)
            existing_dates_events.add(key)
            added += 1
            print(f"  Added: {entry['date']} - {entry['event'][:60]}...")

    # Sort timeline by date
    timeline.sort(key=lambda x: x.get('date', ''))
    data['timeline'] = timeline

    save_json(path, data)
    print(f"  Saved timeline.json ({added} new entries, {len(timeline)} total)")

# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print(f"MAT4719 Evidence Integration - {TIMESTAMP}")
    print(f"Repository: {REPO_DIR}")
    update_entities()
    update_events()
    update_relations()
    update_timeline()
    print("\n=== COMPLETE ===")
