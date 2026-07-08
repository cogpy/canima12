# Simulation Models

**Last Updated:** 2026-03-10

The dynamics of Revenue Stream Hijacking Case 2025-137857 have been formally modeled using multi-paradigm simulation. These models demonstrate the systemic nature of the fraud, the financial flows, and the burden of proof thresholds across the 6 phases of the criminal enterprise.

## LEX-SIM-NN Differentiable Legal Simulation (NEW)

The LEX-SIM-NN pipeline is a differentiable neural network that encodes evidence as 24-dimensional vectors and trains with Virtual Endocrine System (VES) modulation to assess burden of proof thresholds.

- **Report:** [LEX_SIM_NN_REPORT_2026_03_10.md](./LEX_SIM_NN_REPORT_2026_03_10.md)
- **Results (JSON):** [LEX_SIM_NN_RESULTS_2026_03_10.json](./LEX_SIM_NN_RESULTS_2026_03_10.json)
- **Script:** [run_lex_sim_nn.py](./run_lex_sim_nn.py)
- **Key Result:** Civil probability 98.86% (MET), Criminal probability 98.88% (MET)

## Available Models

### 1. AnyLogic Multi-Paradigm Model (.alp)
A comprehensive model combining System Dynamics (financial flows), Discrete-Event Simulation (fraud event chain), and Agent-Based Modeling (perpetrator/victim behavior).
- **File:** [RevenueStreamHijacking_Case2025_137857.alp](./RevenueStreamHijacking_Case2025_137857.alp)
- **Key Features:** Models the ZAR 18.75M Ketoni motive, R10.27M revenue diversion, and the accumulation of legal exposure leading to the 95% criminal threshold.

### 2. NetLogo Agent-Based Model (.nlogo)
An interactive agent-based model focusing on the spatial and temporal dynamics of the fraud.
- **File:** [RevenueStreamHijacking_Case2025_137857.nlogo](./RevenueStreamHijacking_Case2025_137857.nlogo)
- **Key Features:** Visualizes perpetrators, victims, and facilitators moving revenue packets from legitimate FNB accounts to fraudulent ABSA accounts. Includes interactive sliders for diversion rates and evidence destruction.

## Integration Documentation

- [CogSim Integration](./cogsim-integration.md): Overview of the simulation framework integration with the evidence repository.
- [Lex Framework Integration](./lex-framework-integration.md): Details on the legal reasoning and analysis framework integration.

## Methodology

These models were generated using the `target-to-anylogic` P49 decomposition methodology, which analyzes the structural, relational, and temporal properties of the case evidence to produce formal simulation architectures.

## LEX Legal Reasoning Framework Models

The LEX Legal Reasoning Framework (from `ad-res-j7/lex`) has also been modeled to demonstrate the automated legal analysis pipeline that processes the case evidence.

### 1. LEX AnyLogic Model (.alp)
A multi-paradigm model of the legal reasoning architecture.
- **File:** [lex.alp](./lex.alp)
- **Key Features:** Models the evidence intake, modal logic qualification, 7-lens attention scoring, inference reasoning, burden of proof assessment, and grip optimization across 8 dimensions.

### 2. LEX NetLogo Model (.nlogo)
An agent-based model of the legal reasoning process.
- **File:** [lex.nlogo](./lex.nlogo)
- **Key Features:** Visualizes evidence items flowing through the analysis pipeline, interacting with 63 Level 1 principles, 7 attention lenses, 4 inference engines, and 128 legal reasoning skills.

## DigiTwin Multi-Paradigm Simulation (NEW)

The DigiTwin framework models the case as a multi-paradigm digital twin with hormone-modulated agent behavior, combining System Dynamics, Discrete-Event Simulation, and Agent-Based Modeling.

- **Report:** [DIGITWIN_REPORT_2026_03_11.md](./DIGITWIN_REPORT_2026_03_11.md)
- **Results (JSON):** [DIGITWIN_RESULTS_2026_03_11.json](./DIGITWIN_RESULTS_2026_03_11.json)
- **Script:** [digitwin_revstream_simulation.py](./digitwin_revstream_simulation.py)
- **Visualizations:**
  - [Agent Cognitive Modes](./digitwin_agent_modes.png)
  - [Stock-Flow Financial Model](./digitwin_stock_flow.png)
  - [Burden of Proof Assessment](./digitwin_burden_of_proof.png)
  - [Phase Analysis](./digitwin_phase_analysis.png)
