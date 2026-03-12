#!/usr/bin/env python3
"""
Generate ALP and NLogo model files from Case 2025-137857 specification.
Uses the lex-digitwin-nn skill's generator adapters.
"""
import sys, json, os
sys.path.insert(0, "/home/ubuntu/skills/lex-digitwin-nn/scripts")
sys.path.insert(0, "/home/ubuntu/skills/lex-sim-nn/scripts")

# Import the case builder
from run_composed_simulation_v13 import build_case_2025_137857

def case_spec_to_json(case_spec) -> dict:
    """Serialize CaseSpec to JSON-compatible dict."""
    return {
        "case_number": case_spec.case_number,
        "case_name": case_spec.case_name,
        "initial_legitimate_revenue": case_spec.initial_legitimate_revenue,
        "initial_ketoni_receivable": case_spec.initial_ketoni_receivable,
        "agents": [
            {"name": a.name, "role": a.role,
             "initial_valence": a.initial_valence, "initial_arousal": a.initial_arousal}
            for a in case_spec.agents
        ],
        "phases": [
            {"phase_id": p.phase_id, "name": p.name, "months": p.months,
             "events": [
                 {"month": e.month, "event_type": e.event_type, "intensity": e.intensity,
                  "targets": e.targets, "financial": e.financial}
                 for e in p.events
             ]}
            for p in case_spec.phases
        ],
    }

if __name__ == "__main__":
    output_dir = os.path.dirname(os.path.abspath(__file__))
    case = build_case_2025_137857()
    
    # Export CaseSpec JSON
    spec_json = case_spec_to_json(case)
    spec_path = os.path.join(output_dir, "case_spec_v13.json")
    with open(spec_path, 'w') as f:
        json.dump(spec_json, f, indent=2)
    print(f"CaseSpec saved: {spec_path}")
    
    # Generate ALP
    try:
        from generate_lex_alp import generate as gen_alp
        alp_path = gen_alp(spec_path, output_dir)
        print(f"ALP spec saved: {alp_path}")
    except Exception as e:
        print(f"ALP generation: {e}")
    
    # Generate NLogo
    try:
        from generate_lex_nlogo import generate as gen_nlogo
        nlogo_path = gen_nlogo(spec_path, output_dir)
        print(f"NLogo spec saved: {nlogo_path}")
    except Exception as e:
        print(f"NLogo generation: {e}")
    
    print("Done.")
