@#$#@#$#@
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
"avg-stress" 1.0 0 -2674135 true "" "plot mean [stress-level] of turtles with [entity-type = \"person\"]"
"avg-knowledge" 1.0 0 -13796971 true "" "plot mean [knowledge-level] of turtles with [entity-type = \"person\"]"

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

  create-turtles 1 [
    set shape "person"
    set color red
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_001"
    set entity-name "Peter Andrew Faucitt"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color red
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_002"
    set entity-name "Rynette Farrar"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_003"
    set entity-name "Darren Dennis Farrar"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color blue
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_004"
    set entity-name "Jacqueline Faucitt"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color blue
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_005"
    set entity-name "Daniel James Faucitt"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color orange
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_006"
    set entity-name "Linda Kruger"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color red
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_007"
    set entity-name "Daniel Jacobus Bantjies"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_008"
    set entity-name "Kayla"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_009"
    set entity-name "Gee"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_010"
    set entity-name "Bernadine Wright"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_011"
    set entity-name "Chantal"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_012"
    set entity-name "Marisca Meyer"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_013"
    set entity-name "Kayla Pretorius"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_014"
    set entity-name "Kevin Michael Derrick"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_015"
    set entity-name "Chantal"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_016"
    set entity-name "PERSON_016: Nondu Motlhala"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_017"
    set entity-name "PERSON_017: Mpumi Netshipale"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_018"
    set entity-name "PERSON_018: Michelle Habig"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_019"
    set entity-name "PERSON_019: Oliver"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color orange
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_020"
    set entity-name "Linda Kruger"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_021"
    set entity-name "Gayane Williams"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_037"
    set entity-name "PERSON_037 - Kent"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_038"
    set entity-name "PERSON_038 - EL"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_039"
    set entity-name "PERSON_039: Anton Hechter"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_040"
    set entity-name "PERSON_040: Clare Payne"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_041"
    set entity-name "PERSON_041: Kent Rault"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_042"
    set entity-name "PERSON_042: Marc Yudaken"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_043"
    set entity-name "PERSON_043: David Field"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_044"
    set entity-name "PERSON_044: Denny Da Silva"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_045"
    set entity-name "Nick Xenophontos"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "person"
    set color gray
    set size 1.5
    setxy random-xcor random-ycor
    set entity-id "PERSON_XENOPHONTOS"
    set entity-name "Nicos Xenophontos"
    set entity-type "person"
    set knowledge-level random-float 1.0
    set stress-level random-float 0.5
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_001"
    set entity-name "Regima Worldwide Distribution"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_002"
    set entity-name "Regima Skin Treatments CC"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 103
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_003"
    set entity-name "RegimA Zone Ltd"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_004"
    set entity-name "Strategic Logistics Group"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 13
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_005"
    set entity-name "Villa Via"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_006"
    set entity-name "RegimA SA"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_007"
    set entity-name "Ian Levitt Attorneys"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 103
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_008"
    set entity-name "ReZonance"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 13
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_009"
    set entity-name "Adderory"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 13
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_010"
    set entity-name "Adderory Skin"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_011"
    set entity-name "Entity Profile: Elliott Attorneys"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_012"
    set entity-name "RegimaSA"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_013"
    set entity-name "Unicorn Dynamics"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_014"
    set entity-name "RegimA SA"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_015"
    set entity-name "Ketoni Investment Holdings"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_016"
    set entity-name "ORG_017: Ketoni Investment Holdings (Pty) Ltd"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_017"
    set entity-name "ORG_017: Ketoni Investment Holdings (Pty) Ltd"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_018"
    set entity-name "ORG_018: The George Group"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_019"
    set entity-name "ORG_019: Pottas Attorneys"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_020"
    set entity-name "ORG_020: Elliott Attorneys Inc"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_021"
    set entity-name "ORG_021: Pottas Attorneys"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_022"
    set entity-name "ORG_022: ENS Africa"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_023"
    set entity-name "ORG_023: De Novo Business Services"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_024"
    set entity-name "ORG_024: Corporate and Merchant Administrators"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_025"
    set entity-name "ORG_025: Baker McKenzie"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_026"
    set entity-name "ORG_026: Unidentified Financial Entity"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_027"
    set entity-name "ORG_027: Kaylovest Three (Pty) Ltd"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_028"
    set entity-name "Elliott Attorneys Incorporated"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_029"
    set entity-name "Nick Xenophontos Attorneys"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "ORG_030"
    set entity-name "Forvis Mazars"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
  create-turtles 1 [
    set shape "house"
    set color 55
    set size 2.0
    setxy random-xcor random-ycor
    set entity-id "TRUST_001"
    set entity-name "Faucitt Family Trust"
    set entity-type "organization"
    set knowledge-level 0
    set stress-level 0
  ]
end

to setup-network
  ;; Auto-generated from relations.json

  ask turtle 0 [
    create-link-to turtle 1 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 56 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 57 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 58 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 32 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 1 [
    create-link-to turtle 56 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 1 [
    create-link-to turtle 57 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 1 [
    create-link-to turtle 58 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 1 [
    create-link-to turtle 32 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 56 [
    create-link-to turtle 57 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 56 [
    create-link-to turtle 58 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 56 [
    create-link-to turtle 32 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 57 [
    create-link-to turtle 58 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 57 [
    create-link-to turtle 32 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 58 [
    create-link-to turtle 32 [
      set color red
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 4 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 1 [
    create-link-to turtle 4 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 35 [
    create-link-to turtle 57 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 1 [
    create-link-to turtle 6 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 6 [
    create-link-to turtle 0 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 6 [
    create-link-to turtle 1 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 6 [
    create-link-to turtle 14 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 6 [
    create-link-to turtle 46 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 6 [
    create-link-to turtle 61 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 14 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 46 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 61 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 1 [
    create-link-to turtle 14 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 1 [
    create-link-to turtle 46 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 1 [
    create-link-to turtle 61 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 14 [
    create-link-to turtle 46 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 14 [
    create-link-to turtle 61 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 46 [
    create-link-to turtle 61 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 1 [
    create-link-to turtle 19 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 1 [
    create-link-to turtle 20 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 1 [
    create-link-to turtle 0 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 19 [
    create-link-to turtle 20 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 19 [
    create-link-to turtle 0 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 19 [
    create-link-to turtle 6 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 20 [
    create-link-to turtle 0 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 20 [
    create-link-to turtle 6 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 6 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 35 [
    create-link-to turtle 0 [
      set color red
      set thickness 0.297
      set relation-strength 0.99
    ]
  ]
  ask turtle 57 [
    create-link-to turtle 0 [
      set color red
      set thickness 0.297
      set relation-strength 0.99
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 31 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 34 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 36 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 3 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 33 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 38 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 12 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 13 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 47 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 0 [
    create-link-to turtle 48 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 0 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 32 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 34 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 36 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 3 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 4 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 33 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 38 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 12 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 13 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 47 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 48 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 0 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 34 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 36 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 3 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 31 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 4 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 33 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 38 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 12 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 13 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 47 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 48 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 34 [
    create-link-to turtle 0 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 34 [
    create-link-to turtle 36 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 34 [
    create-link-to turtle 3 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 34 [
    create-link-to turtle 31 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 34 [
    create-link-to turtle 4 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 34 [
    create-link-to turtle 33 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 34 [
    create-link-to turtle 38 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 34 [
    create-link-to turtle 12 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 34 [
    create-link-to turtle 13 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 34 [
    create-link-to turtle 47 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 34 [
    create-link-to turtle 48 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 36 [
    create-link-to turtle 3 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 36 [
    create-link-to turtle 31 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 36 [
    create-link-to turtle 4 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 36 [
    create-link-to turtle 33 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 36 [
    create-link-to turtle 38 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 36 [
    create-link-to turtle 12 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 36 [
    create-link-to turtle 13 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 36 [
    create-link-to turtle 47 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 36 [
    create-link-to turtle 48 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 3 [
    create-link-to turtle 31 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 3 [
    create-link-to turtle 4 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 3 [
    create-link-to turtle 33 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 3 [
    create-link-to turtle 38 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 3 [
    create-link-to turtle 12 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 3 [
    create-link-to turtle 13 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 3 [
    create-link-to turtle 47 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 3 [
    create-link-to turtle 48 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 4 [
    create-link-to turtle 31 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 4 [
    create-link-to turtle 33 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 4 [
    create-link-to turtle 38 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 4 [
    create-link-to turtle 12 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 4 [
    create-link-to turtle 13 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 4 [
    create-link-to turtle 47 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 4 [
    create-link-to turtle 48 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 33 [
    create-link-to turtle 4 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 33 [
    create-link-to turtle 38 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 33 [
    create-link-to turtle 12 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 33 [
    create-link-to turtle 13 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 33 [
    create-link-to turtle 47 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 33 [
    create-link-to turtle 48 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 38 [
    create-link-to turtle 12 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 38 [
    create-link-to turtle 13 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 38 [
    create-link-to turtle 47 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 38 [
    create-link-to turtle 48 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 12 [
    create-link-to turtle 38 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 12 [
    create-link-to turtle 13 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 12 [
    create-link-to turtle 47 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 12 [
    create-link-to turtle 48 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 13 [
    create-link-to turtle 47 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 13 [
    create-link-to turtle 48 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 47 [
    create-link-to turtle 13 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 47 [
    create-link-to turtle 48 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 61 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 38 [
    create-link-to turtle 61 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 38 [
    create-link-to turtle 31 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 47 [
    create-link-to turtle 61 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 47 [
    create-link-to turtle 31 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 61 [
    create-link-to turtle 31 [
      set color red
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 61 [
    create-link-to turtle 47 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 61 [
    create-link-to turtle 4 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 61 [
    create-link-to turtle 33 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 61 [
    create-link-to turtle 38 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 61 [
    create-link-to turtle 12 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 31 [
    create-link-to turtle 61 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 47 [
    create-link-to turtle 4 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 47 [
    create-link-to turtle 33 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 47 [
    create-link-to turtle 38 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 47 [
    create-link-to turtle 12 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 61 [
    create-link-to turtle 3 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 61 [
    create-link-to turtle 6 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 3 [
    create-link-to turtle 61 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 3 [
    create-link-to turtle 6 [
      set color white
      set thickness 0.15
      set relation-strength 0.5
    ]
  ]
  ask turtle 32 [
    create-link-to turtle 50 [
      set color white
      set thickness 0.285
      set relation-strength 0.95
    ]
  ]
  ask turtle 38 [
    create-link-to turtle 7 [
      set color gray
      set thickness 0.1
      set relation-strength 0.3
    ]
  ]
  ask turtle 40 [
    create-link-to turtle 39 [
      set color gray
      set thickness 0.1
      set relation-strength 0.3
    ]
  ]
  ask turtle 10 [
    create-link-to turtle 7 [
      set color gray
      set thickness 0.1
      set relation-strength 0.3
    ]
  ]
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
