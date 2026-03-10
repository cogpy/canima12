# Simulation Models

**Last Updated:** 2026-03-09

The dynamics of Revenue Stream Hijacking Case 2025-137857 have been formally modeled using multi-paradigm simulation. These models demonstrate the systemic nature of the fraud, the financial flows, and the burden of proof thresholds across the 6 phases of the criminal enterprise.

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
