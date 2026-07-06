#!/usr/bin/env python3
"""
Generate NetLogo Model for ForensicSims
=======================================
Reads entities.json and relations.json to generate a complete .nlogo file
visualizing emergent group dynamics, gossip propagation, and social networks.
"""

import json
import os

def generate_nlogo(entities_file, relations_file, output_file):
    # Load data
    with open(entities_file) as f:
        entities = json.load(f)
    with open(relations_file) as f:
        relations = json.load(f)

    # Filter entities
    persons = [e for e in entities if e.get('type') in ['person', 'natural_person', 'Person']]
    orgs = [e for e in entities if e.get('type') in ['company', 'corporate_entity', 'trust', 'Organization', 'Trust']]
    
    # Create entity ID mapping to sequential integers for NetLogo
    id_map = {}
    current_id = 0
    
    # Process agents for NetLogo setup
    agent_setup_code = []
    
    # Persons
    for p in persons:
        eid = p.get('id')
        if not eid: continue
        id_map[eid] = current_id
        name = p.get('name', '').replace('"', "'")
        
        # Determine faction/color based on name
        color = "white"
        if "Peter" in name or "Rynette" in name or "Bantjies" in name:
            color = "red"  # Hostile faction
        elif "Daniel" in name or "Jacqueline" in name:
            color = "blue"  # Defense faction
        elif "Elliott" in name or "Kruger" in name:
            color = "orange"  # Complicit professionals/employees
        else:
            color = "gray"  # Neutral/Unknown
            
        agent_setup_code.append(f"""
  create-turtles 1 [
    set shape "person"
    set color {color}
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "{eid}"
    set entity-name "{name}"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]""")
        current_id += 1

    # Organizations
    for o in orgs:
        eid = o.get('id')
        if not eid: continue
        id_map[eid] = current_id
        name = o.get('name', '').replace('"', "'")
        
        color = "55" # green
        if "RST" in name or "Adderory" in name or "Villa Via" in name:
            color = "13"  # red - 2
        elif "RWW" in name or "Zone" in name or "ReZonance" in name:
            color = "103"  # blue - 2
            
        agent_setup_code.append(f"""
  create-turtles 1 [
    set shape "house"
    set color {color}
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "{eid}"
    set entity-name "{name}"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]""")
        current_id += 1

    # Process relations for NetLogo links
    link_setup_code = []
    link_pairs_seen = set()
    
    for r in relations:
        involved = r.get('entities_involved', [])
        if not isinstance(involved, list) or len(involved) < 2:
            continue
        
        strength = r.get('evidence_strength', r.get('strength', r.get('confidence', 50)))
        if isinstance(strength, (int, float)):
            strength = strength / 100.0 if strength > 1 else strength
        else:
            strength = 0.5
        
        color = "white"
        if "fraud" in str(r.get('legal_categories', [])).lower():
            color = "red"
        elif "conspiracy" in str(r.get('legal_categories', [])).lower():
            color = "orange"
        elif "breach" in str(r.get('legal_categories', [])).lower():
            color = "yellow"
        
        # Create pairwise links between all entities in the relation
        for i in range(len(involved)):
            for j in range(i + 1, len(involved)):
                src = involved[i]
                tgt = involved[j]
                pair = (src, tgt)
                if src in id_map and tgt in id_map and src != tgt and pair not in link_pairs_seen:
                    link_pairs_seen.add(pair)
                    link_setup_code.append(f"""
  ask turtle {id_map[src]} [
    create-link-to turtle {id_map[tgt]} [
      set color {color}
      set thickness {strength * 0.3}
      set relation-strength {strength}
    ]
  ]""")
    
    # Also add inferred links from entity 'relationships' field
    for e in entities:
        eid = e.get('id')
        if eid not in id_map:
            continue
        rels = e.get('relationships', [])
        if isinstance(rels, list):
            for rel_str in rels:
                # Try to find target entity IDs mentioned in relationship strings
                for other_e in entities:
                    other_id = other_e.get('id')
                    if other_id and other_id != eid and other_id in id_map:
                        other_name = other_e.get('name', '').lower()
                        if other_name and len(other_name) > 3 and other_name in rel_str.lower():
                            pair = (eid, other_id)
                            if pair not in link_pairs_seen:
                                link_pairs_seen.add(pair)
                                link_setup_code.append(f"""
  ask turtle {id_map[eid]} [
    create-link-to turtle {id_map[other_id]} [
      set color gray
      set thickness 0.1
      set relation-strength 0.3
    ]
  ]""")
    
    print(f"Total links generated: {len(link_setup_code)} from {len(link_pairs_seen)} unique pairs")

    # NetLogo Model Code
    nlogo_code = f"""@#$#@#$#@
GRAPHICS-WINDOW
210
10
645
445
-1
-1
13.0
1
10
1
1
1
0
1
1
1
-16
16
-16
16
0
0
1
ticks
30.0

BUTTON
10
10
100
43
NIL
setup
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

BUTTON
110
10
200
43
NIL
go
T
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

SLIDER
10
50
200
83
gossip-spread-chance
gossip-spread-chance
0
100
30.0
1
1
NIL
NIL
NIL

SLIDER
10
90
200
123
stress-increase-rate
stress-increase-rate
0
0.1
0.02
0.01
1
NIL
NIL
NIL

PLOT
10
130
200
280
System Stress & Knowledge
time
level
0.0
100.0
0.0
1.0
true
false
"" ""
PENS
"avg-stress" 1.0 0 -2674135 true "" "plot mean [stress-level] of turtles with [entity-type = \\"person\\"]"
"avg-knowledge" 1.0 0 -13796971 true "" "plot mean [knowledge-level] of turtles with [entity-type = \\"person\\"]"

PLOT
10
290
200
440
Tipping Point Detection
time
evidence-mass
0.0
100.0
0.0
100.0
true
false
"" ""
PENS
"critical-mass" 1.0 0 -16777216 true "" "plot sum [knowledge-level * stress-level] of turtles"
"threshold" 1.0 0 -2674135 true "" "plot 50"

@#$#@#$#@
turtles-own [
  entity-id
  entity-name
  entity-type
  knowledge-level  ;; 0 to 1
  stress-level     ;; 0 to 1
  has-gossip?      ;; boolean
]

links-own [
  relation-strength ;; 0 to 1
]

to setup
  clear-all
  setup-agents
  setup-network
  layout-spring turtles links 0.2 5 1
  reset-ticks
end

to setup-agents
  ;; Auto-generated from entities.json
{''.join(agent_setup_code)}
end

to setup-network
  ;; Auto-generated from relations.json
{''.join(link_setup_code)}
end

to go
  if not any? turtles [ stop ]
  
  ;; Layout optimization
  layout-spring turtles links 0.2 5 1
  
  ;; Gossip propagation (Information spreading through network)
  ask turtles with [entity-type = "person"] [
    if random-float 100 < gossip-spread-chance [
      let my-knowledge knowledge-level
      ask out-link-neighbors with [entity-type = "person"] [
        ;; Receive knowledge, modified by relation strength
        let link-strength [relation-strength] of in-link-from myself
        set knowledge-level min list 1.0 (knowledge-level + (my-knowledge * link-strength * 0.1))
        
        ;; Knowledge increases stress if it's high
        if knowledge-level > 0.5 [
          set stress-level min list 1.0 (stress-level + stress-increase-rate)
        ]
      ]
    ]
  ]
  
  ;; Endocrine modulation (Stress decay and visualization)
  ask turtles with [entity-type = "person"] [
    ;; Natural stress decay
    set stress-level max list 0.0 (stress-level - 0.005)
    
    ;; Visual feedback: size pulses with stress, label shows name if high knowledge
    set size 1.5 + (stress-level * 0.5)
    ifelse knowledge-level > 0.8 [
      set label entity-name
    ] [
      set label ""
    ]
  ]
  
  ;; Tipping point event
  let critical-mass sum [knowledge-level * stress-level] of turtles
  if critical-mass > 50 [
    ask turtles [ set color yellow ] ;; Flash when threshold reached
  ]
  
  tick
end
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
default
true
0
Polygon -7500403 true true 150 5 40 250 150 205 260 250

person
true
0
Circle -7500403 true true 30 30 240
Circle -7500403 true true 115 150 70
Polygon -7500403 true true 113 216 58 292 84 300 135 240 185 300 211 292 154 216

house
true
0
Polygon -7500403 true true 150 15 30 135 270 135
Rectangle -7500403 true true 60 135 240 285
@#$#@#$#@
NetLogo 6.3.0
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
"""
    
    with open(output_file, 'w') as f:
        f.write(nlogo_code)
    
    print(f"Generated NetLogo model at {output_file}")
    print(f"Included {current_id} agents and {len(link_setup_code)} links.")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    entities_file = os.path.join(base_dir, 'data_models', 'entities.json')
    relations_file = os.path.join(base_dir, 'data_models', 'relations.json')
    output_file = os.path.join(base_dir, 'simulation', 'ForensicSims_Dynamics.nlogo')
    
    generate_nlogo(entities_file, relations_file, output_file)
