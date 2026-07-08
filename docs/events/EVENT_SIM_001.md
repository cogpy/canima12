---
layout: default
title: "EVENT_SIM_001: LEX-SIM-NN Differentiable Legal Simulation"
event_id: EVENT_SIM_001
date: 2026-03-10
category: Legal Analysis
type: Simulation Analysis
burden_of_proof: verified_simulation
evidence_strength: 99
---

# EVENT_SIM_001: LEX-SIM-NN Differentiable Legal Simulation Executed

## Summary

On 10 March 2026, the LEX-SIM-NN differentiable legal simulation pipeline was executed against the complete body of evidence for Case 2025-137857. The pipeline encodes evidence as 24-dimensional vectors across 6 categories (Temporal, Financial, Documentary, Testimonial, Forensic, Relational/Intentional) and trains a neural network with Virtual Endocrine System (VES) modulation to assess burden of proof thresholds.

## Key Results

| Metric | Value |
|--------|-------|
| Civil Probability | **98.86%** |
| Criminal Probability | **98.88%** |
| Civil Burden (50%) | **MET** |
| Criminal Burden (95%) | **MET** |
| Training Loss (final) | 0.0023 |
| Cognitive Mode | THREAT |

## Evidence Attribution (Strongest → Weakest)

1. **Relational/Intentional** (0.0797) — Conspiracy networks, entity links, mens rea
2. **Documentary** (0.0791) — Emails, CIPC records, contracts, affidavits
3. **Temporal** (0.0761) — Dates, sequences, registration timelines
4. **Forensic** (0.0733) — Digital traces, metadata, stylometry
5. **Financial** (0.0699) — Amounts, flows, transaction volumes
6. **Testimonial** (0.0517) — Witness statements, corroboration

## Significance

The simulation confirms that the evidence base is sufficient to meet both civil (balance of probabilities) and criminal (beyond reasonable doubt) burdens of proof. The weakest category is Testimonial, indicating that formal witness statements and expert affidavits would further strengthen the case.

## Entities Involved

PERSON_001 (Peter Faucitt), PERSON_002 (Rynette Farrar), PERSON_007 (Daniel Bantjies), ORG_002 (RegimA Skin Treatments), ORG_006 (RegimA SA), TRUST_001 (Faucitt Family Trust)

## Evidence Files

- [LEX-SIM-NN Report](../simulation/LEX_SIM_NN_REPORT_2026_03_10.md)
- [LEX-SIM-NN Results (JSON)](../simulation/LEX_SIM_NN_RESULTS_2026_03_10.json)
- [Simulation Script](../simulation/run_lex_sim_nn.py)
