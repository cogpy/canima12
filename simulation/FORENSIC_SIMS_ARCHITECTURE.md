# Forensic Sims — Hybrid Multi-Paradigm Simulation Architecture

## Composition Expression

```
ForensicSims = /vorticog ⊗ /skillm ⊗ /ai-env-grp-dyn ⊗ /acc-fund-flow ⊗ /virtual-endocrine-system
             ⊕ /cogsim-pml ⊕ /scm-des ⊕ /lex-sim-nn
```

Where `⊗` = pipeline (multiplicative/tensorial) and `⊕` = choice/additive (parallel subsystems).

## Architecture: 5 Subsystems + 1 Integration Layer

| # | Subsystem | Skill Source | Paradigm | Role |
|---|-----------|-------------|----------|------|
| 1 | **Economic Engine** | /vorticog + /acc-fund-flow | ABM + SD | Fund flows, revenue streams, financial stocks |
| 2 | **Supply Chain** | /scm-des + /cogsim-pml | DES | Material/product/document flows through entities |
| 3 | **Legal Reasoning** | /lex-sim-nn | NN (differentiable) | 7-lens attention, burden of proof, evidence attribution |
| 4 | **Persona & Group** | /ai-env-grp-dyn + /vorticog | ABM | Agent personas, group dynamics, social network |
| 5 | **Endocrine Bus** | /virtual-endocrine-system | Continuous | 16-channel hormone modulation of all subsystems |
| 6 | **Hypergraph Linker** | /lex-sim-nn dynamic dict | Integration | Cross-references as LEX transformer vocabulary entries |

## Subsystem 1: Economic Engine (Vorticog + Fund Flow)

**Paradigm**: Agent-Based + System Dynamics hybrid

**Stocks** (from SF_SDM_SPEC):
- `legitimate_revenue` — Revenue flowing through proper channels
- `diverted_revenue` — Revenue captured by unauthorized entities
- `trust_assets` — FFT asset pool
- `litigation_funding` — Funds allocated to legal actions
- `operational_capital` — Working capital for RegimA entities

**Flows** (from acc-fund-flow):
- `revenue_diversion_rate` — R/month diverted from legitimate to shadow
- `litigation_burn_rate` — R/month spent on adversarial litigation
- `trust_extraction_rate` — R/month extracted from FFT
- `platform_revenue_rate` — Shopify/Sage transaction volume

**Agents** (Vorticog pattern):
- Each entity (78 total) modeled as a Vorticog agent with:
  - Financial state (balance, revenue, expenses)
  - Motivational levels (Big Five personality)
  - Emotional state (happiness, stress, loyalty, trust)
  - Needs (financial, security, recognition, autonomy)

**Fund Flow Tracing**:
- Transaction graph from RST/RWD/FFT bank statements
- Anomaly detection: circular flows, structuring, layering
- Visualization: D2/Mermaid flow diagrams

## Subsystem 2: Supply Chain (CogSim PML + SCM-DES)

**Paradigm**: Discrete Event Simulation

**Process Flow** (RegimA product/revenue supply chain):
```
Supplier(Ingredients) → Producer(RegimA SA) → Distributor(RWD/RST)
  → Wholesaler(Zone Ltd) → Retailer(Salons/B2B) → Customer(End User)
```

**PML Blocks**:
- `Source`: Customer orders arriving (Shopify)
- `Service`: Order processing (Sage)
- `ResourceTask`: Fulfillment (warehouse operations)
- `SelectOutput`: Routing (legitimate vs diverted channel)
- `Sink`: Revenue collection (bank accounts)

**Key Metrics**:
- Throughput: Orders/month through legitimate vs shadow channel
- Lead time: Order-to-delivery (normal vs blocked)
- Utilization: Platform access (Shopify uptime vs blocked)
- Queue length: Unfulfilled orders during platform lockout

## Subsystem 3: Legal Reasoning (LEX-Sim-NN)

**Paradigm**: Differentiable Neural Network

**Architecture** (from lex-sim-nn):
```
Evidence(24D) → Linear(24→128) → 7-Lens Attention(128→224)
  → Inference(224→64→32) → Output(32→2) → BurdenOfProof
```

**7 Attention Lenses**:
1. Temporal sequence (event ordering)
2. Financial magnitude (amounts, ratios)
3. Documentary (contracts, filings)
4. Testimonial (affidavits, admissions)
5. Forensic (digital traces, metadata)
6. Relational (entity links, control)
7. Intentional (mens rea, knowledge state)

**Training Target**: `[civil_burden_met, criminal_burden_met]`

**Evidence Attribution**: Gradient-based — identifies which evidence categories drive each filing's strength.

## Subsystem 4: Persona & Group Dynamics (AI-Env-Grp-Dyn)

**Paradigm**: Agent-Based (Generative Agents / Smallville pattern)

**Agent State** (7 dimensions from hypergraph v63):
- Knowledge, Capability, Motive, Opportunity, Behavioral, Strategic, Network

**Group Formation** (emergent, not assigned):
- `Peter_Faction`: {Peter, Bantjies, Elliott, Mazars, Adv Pool}
- `Daniel_Faction`: {Daniel, Jacqueline}
- `Neutral_Professionals`: {Master, CIPC, SARS, NPA}
- `Corporate_Entities`: {RWD, RST, Zone Ltd, Zone SA, FFT}

**Social Network**:
- Weighted directed graph (trust, familiarity, influence)
- Information propagation (gossip model with decay)
- Consensus formation (opinion dynamics)

**Persona Modulation** (Big Five → behavior):
- Peter: Low Agreeableness, High Neuroticism → aggressive litigation
- Bantjies: High Conscientiousness (facade), Low Openness → concealment
- Daniel: High Openness, High Conscientiousness → evidence gathering
- Elliott: Professional (neutral personality, follows instructions)

## Subsystem 5: Virtual Endocrine System

**Paradigm**: Continuous dynamical system (16 hormone channels)

**Mapping to Case Events**:

| Case Event | Hormone Response | Effect on Simulation |
|---|---|---|
| Evidence discovered | Dopamine ↑, Norepinephrine ↑ | Increased attention to related evidence |
| Filing deadline approaching | Cortisol ↑ | Raised scrutiny threshold |
| Admission obtained | Serotonin ↑ | Stabilized conclusions |
| Threat (interdict) | CRH → ACTH → Cortisol cascade | Resource mobilization |
| Social bond (ally found) | Oxytocin ↑ | Trust in corroborating evidence |
| Pattern detected (fraud) | Dopamine (phasic) ↑ | Reward signal, accelerated learning |

**Cognitive Modes** (emergent from hormone state):
- FOCUSED: Deep evidence analysis
- VIGILANT: Threat detection (interdict, deadline)
- EXPLORATORY: New evidence discovery
- STRESSED: Multiple deadlines, resource constraints
- SOCIAL: Group coordination, consensus building

## Integration Layer: Hypergraph Dynamic Dict (LEX-Sim-NN)

**The key insight**: Every cross-reference between subsystems becomes a dynamic dictionary entry in the LEX transformer vocabulary. This means:

1. **Entity → Token**: Each of the 78 entities becomes a token in the LEX transformer vocabulary
2. **Relation → Attention Weight**: Each of the 42 relations becomes a pre-trained attention weight
3. **Event → Positional Encoding**: Each of the 181 events gets a temporal positional encoding
4. **KSM Cell → Bias Term**: Each of the 13 KSM generators adds a bias to the attention computation
5. **Hormone → Learning Rate Modulation**: Each hormone channel modulates the transformer's learning dynamics

**Dynamic Dict Entry Schema**:
```python
class LexDictEntry:
    token_id: str           # Entity/relation/event ID
    embedding: list[float]  # 24D evidence vector
    attention_bias: float   # From KSM center strength
    hormone_modulation: dict[str, float]  # 16 hormone effects
    filing_relevance: dict[str, float]    # Per-filing relevance score
    matula_prime: int       # Proof certificate encoding
    last_updated: str       # Timestamp of last simulation tick
```

**Cross-Reference Protocol**:
- When Subsystem 1 (Economic) detects a fund flow anomaly → creates/updates a LexDictEntry
- When Subsystem 2 (Supply Chain) detects a blocked flow → updates the same entry's attention_bias
- When Subsystem 3 (Legal) evaluates evidence → reads the entry's embedding and hormone_modulation
- When Subsystem 4 (Persona) detects group coordination → updates the entry's social context
- When Subsystem 5 (Endocrine) shifts mode → broadcasts hormone_modulation to all entries

## AnyLogic / NetLogo Extension Points

**AnyLogic (.alp)**:
- Multi-method model combining DES (supply chain) + ABM (personas) + SD (economics)
- GIS-based environment (SA geography for entity locations)
- Optimization experiment for filing strategy

**NetLogo (.nlogo)**:
- Emergent group dynamics visualization
- Information propagation through social network
- Tipping point detection (when does evidence reach critical mass?)

## Implementation Priority

1. **Core Engine** (Python): CogSim PML + fund flow + endocrine bus
2. **LEX Dict Layer** (Python/JS): Dynamic dict entries linking to hypergraph v63
3. **Persona Engine** (Python): Agent state vectors + group dynamics
4. **Legal Pipeline** (Python/PyTorch): LEX-Sim-NN differentiable pipeline
5. **Visualization** (HTML/D3): Interactive simulation dashboard

## Data Available

| Data Source | Records | Status |
|---|---|---|
| Entities (7D state) | 78 | Ready |
| Relations (weighted) | 42 | Ready |
| Events (causal chain) | 181 | Ready |
| Timeline (sorted) | 157 | Ready |
| Fund flows (RST/RWD) | ~200 transactions | Partial (need more bank data) |
| Proof certificate | 3 evidence trees | Ready |
| KSM 61-definitions | 13 generators | Ready |
| Filing evaluations | 10 filings | Ready |

**Verdict: YES, we have enough to build a real simulation.**
