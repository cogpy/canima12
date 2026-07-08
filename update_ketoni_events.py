import json
import os
from datetime import datetime

EVENTS_FILE = 'data_models/events/events.json'

def update_events():
    with open(EVENTS_FILE, 'r') as f:
        data = json.load(f)
        
    events = data.get('events', data)
    
    new_event = {
        "event_id": "EVT_KETONI_AGREEMENT_2023_04_24",
        "date": "2023-04-24",
        "type": "corporate_structuring",
        "title": "Ketoni Shareholder Agreement Signed",
        "description": "The Ketoni Shareholder Agreement was signed, establishing the ownership chain where FFT holds 100% of A Ordinary Shares (investing R9.8M) and Kevin Derrick Trust holds 100% of Ordinary Shares. Ketoni's purpose is to invest in The George Group.",
        "entities_involved": ["TRUST_001", "ORG_KETONI_001", "ORG_GEORGE_GROUP", "PERSON_DERRICK_001"],
        "evidence": ["Ketoni Shareholder Agreement (Signed 24 April 2023)"],
        "significance": "Establishes the financial structure that creates the massive conflict of interest for Danie Bantjies (CFO of George Group and Trustee of FFT)."
    }
    
    if isinstance(events, list):
        events.append(new_event)
    elif isinstance(events, dict) and 'corporate_events' in events:
        events['corporate_events'].append(new_event)
        
    with open(EVENTS_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Updated {EVENTS_FILE}")

if __name__ == '__main__':
    update_events()
