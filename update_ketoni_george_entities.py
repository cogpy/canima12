import json
import os
from datetime import datetime

ENTITIES_FILE = 'data_models/entities/entities.json'
RELATIONS_FILE = 'data_models/relations/relations.json'

def update_entities():
    with open(ENTITIES_FILE, 'r') as f:
        data = json.load(f)
    
    entities = data.get('entities', {})
    
    # 1. Update Bantjies
    for person in entities.get('persons', []):
        if person.get('entity_id') == 'PERSON_007':
            person['role'] = 'cfo_george_group_and_trustee_fft'
            person['conflict_of_interest'] = {
                'description': 'Massive conflict of interest: Serves as CFO of The George Group (which generates Ketoni returns) while simultaneously serving as Trustee of FFT (which owns 100% of Ketoni A-Shares and receives 90% of distributions).',
                'financial_stake': 'R18.75M - R28.73M Ketoni payout to FFT dependent on George Group performance',
                'loyalty_conflict': 'Professional loyalty to George Group CEO (Kevin Derrick) vs fiduciary duty to FFT beneficiaries (Jacqueline & Daniel Faucitt)',
                'appointment_issue': 'Appointed as FFT Trustee by Rynette Farrar in July 2024, creating a controlled network'
            }
            if 'evidence' not in person:
                person['evidence'] = []
            person['evidence'].append('Ketoni Shareholder Agreement (Signed 24 April 2023)')
            person['evidence'].append('Ketoni AFS 2024 (Note 2)')
            person['refinement_date'] = datetime.now().isoformat()
            
    # 2. Update Ketoni
    for org in entities.get('organizations', []):
        if org.get('entity_id') == 'ORG_KETONI_001' or org.get('entity_id') == 'ORG_KETONI':
            org['name'] = 'Ketoni Investment Holdings Proprietary Limited'
            org['registration_number'] = '2023/562189/07'
            org['incorporation_date'] = '2023-02-20'
            org['type'] = 'investment_holding_company'
            org['role'] = 'pass_through_investment_vehicle'
            org['shareholding_structure'] = {
                'A_Ordinary_Shares': {
                    'holder': 'Faucitt Family Trust (FFT)',
                    'shares': 5000,
                    'percentage': '100% of class',
                    'investment_amount': 'R9,800,000',
                    'rights': '90% of all distributions (Dividend Sweep) for 5 years 2 months'
                },
                'Ordinary_Shares': {
                    'holder': 'The Kevin Derrick Trust',
                    'shares': 100,
                    'percentage': '100% of class',
                    'investment_amount': 'R1,000',
                    'rights': '10% of distributions, full voting rights'
                }
            }
            org['assets'] = {
                'The_George_Group': {
                    'ownership_percentage': '8.14%',
                    'shares_held': 456,
                    'valuation': 'R9,800,000'
                }
            }
            org['director'] = 'Kevin Michael Derrick'
            org['evidence'] = ['Ketoni Shareholder Agreement (Signed 24 April 2023)', 'Ketoni AFS 2024']
            org['refinement_date'] = datetime.now().isoformat()
            
    # 3. Update George Group
    for org in entities.get('organizations', []):
        if org.get('entity_id') == 'ORG_GEORGE_GROUP':
            org['name'] = 'The George Group Proprietary Limited'
            org['registration_number'] = '2018/618716/07'
            org['incorporation_date'] = '2018'
            org['type'] = 'holding_company'
            org['role'] = 'revenue_generator_for_ketoni'
            org['key_personnel'] = {
                'ceo': {
                    'name': 'Kevin Michael Derrick',
                    'also_director_of': 'Ketoni Investment Holdings',
                    'also_shareholder_of': 'Ketoni Investment Holdings (via Trust)'
                },
                'cfo': {
                    'name': 'Danie Bantjies',
                    'also_trustee_of': 'Faucitt Family Trust (unlawfully appointed July 2024)'
                }
            }
            org['shareholders'] = [
                {'name': 'Ketoni Investment Holdings', 'percentage': '8.14%', 'shares': 456}
            ]
            org['acquisitions'] = ['Quatro (valuation basis for Ketoni shares)']
            org['evidence'] = ['Ketoni Shareholder Agreement (Signed 24 April 2023)', 'Ketoni AFS 2024']
            org['refinement_date'] = datetime.now().isoformat()
            
    # 4. Update FFT
    for trust in entities.get('trusts', []):
        if trust.get('entity_id') == 'TRUST_001':
            trust['ketoni_investment'] = {
                'vehicle': 'Ketoni Investment Holdings',
                'shares_held': '5,000 A Ordinary Shares',
                'investment_amount': 'R9,800,000',
                'expected_return': 'R28,730,000 (at end year 5)',
                'distribution_rights': '90% of all distributions',
                'underlying_asset': '8.14% of The George Group'
            }
            trust['refinement_date'] = datetime.now().isoformat()

    with open(ENTITIES_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Updated {ENTITIES_FILE}")

def update_relations():
    with open(RELATIONS_FILE, 'r') as f:
        data = json.load(f)
        
    relations = data.get('relations', data)
    
    # Add new conflict relation for Bantjies
    new_conflict = {
        "relation_id": "REL_CONFLICT_002",
        "relation_type": "fiduciary_conflict_of_interest",
        "source_entity": "PERSON_007",
        "target_entity": "TRUST_001",
        "conflict_description": "Bantjies serves as CFO of The George Group (which generates returns for Ketoni) while simultaneously serving as Trustee of FFT (which owns 100% of Ketoni A-Shares and receives 90% of distributions).",
        "financial_stake": "R18.75M - R28.73M Ketoni payout to FFT",
        "evidence": ["Ketoni Shareholder Agreement", "Ketoni AFS 2024"],
        "legal_implication": "Breach of fiduciary duty under Trust Property Control Act"
    }
    
    # Add ownership relations
    new_ownership_1 = {
        "relation_id": "REL_OWN_001",
        "relation_type": "owns_shares_in",
        "source_entity": "TRUST_001",
        "target_entity": "ORG_KETONI_001",
        "details": "100% of A Ordinary Shares (5,000 shares) for R9.8M",
        "rights": "90% of distributions"
    }
    
    new_ownership_2 = {
        "relation_id": "REL_OWN_002",
        "relation_type": "owns_shares_in",
        "source_entity": "ORG_KETONI_001",
        "target_entity": "ORG_GEORGE_GROUP",
        "details": "8.14% of Ordinary Shares (456 shares) valued at R9.8M"
    }
    
    if isinstance(relations, dict) and 'conflict_relations' in relations:
        relations['conflict_relations'].append(new_conflict)
        if 'ownership_relations' not in relations:
            relations['ownership_relations'] = []
        relations['ownership_relations'].extend([new_ownership_1, new_ownership_2])
    elif isinstance(relations, list):
        relations.extend([new_conflict, new_ownership_1, new_ownership_2])
        
    with open(RELATIONS_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Updated {RELATIONS_FILE}")

if __name__ == '__main__':
    update_entities()
    update_relations()
