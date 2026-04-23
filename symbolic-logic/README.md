# Symbolic Logic Abstraction Layer

A mathematical framework bridging concrete legal case analysis to generalized judgment patterns through symbolic logic with algebraic primitives.

## Architecture

The abstraction layer consists of six interconnected modules that transform specific case facts into generalized symbolic representations suitable for pattern matching across the entire legal corpus.

```
┌─────────────────────────────────────────────────────────────────┐
│                    Integration Layer                             │
│  J = M(A[n], R[m]) ⊗ U[k] ⊗ P(evidence) → Ω(outcome)         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ Core         │  │ Motion/Action│  │ Uniform Rules        │  │
│  │ Primitives   │  │ Algebra      │  │ Workflows            │  │
│  │              │  │              │  │                      │  │
│  │ A[n], R[m]   │  │ μ(m) angular │  │ U[k] = {u_i₁,...}   │  │
│  │ P[n], D[m]   │  │ λ(a) linear  │  │ Displacement Σθ     │  │
│  │ W[n], J[m]   │  │ ⊗ serial     │  │ Pattern library      │  │
│  │ B(π)         │  │ ⊕ parallel   │  │ Success/failure      │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
│         │                  │                    │                │
│         └──────────────────┼────────────────────┘                │
│                            │                                     │
│  ┌─────────────────────────┴─────────────────────────────────┐  │
│  │              Case Role Mapping                             │  │
│  │  Concrete names → Symbolic roles (A[n], R[m], etc.)       │  │
│  └───────────────────────────────────────────────────────────┘  │
│                            │                                     │
├────────────────────────────┼─────────────────────────────────────┤
│              ChainLex Hypergraph (lawlibrary-repo-of-record)    │
│  639 acts + 8,270 judgments → Primitives → Pathways → Profiles  │
└─────────────────────────────────────────────────────────────────┘
```

## Module Reference

| Module | File | Purpose |
|--------|------|---------|
| Core Primitives | `core_primitives.scm` | Role sets A[n], R[m], P[n], D[m]; motions M; actions A; burdens B(pi) |
| Case Role Mapping | `case_role_mapping.scm` | Maps concrete names to symbolic roles for Case 2025-137857 |
| Motion/Action Algebra | `motion_action_algebra.scm` | Angular moments mu(m) for motions, linear moments lambda(a) for actions |
| Uniform Rules Index | `uniform_rules_index.scm` | Complete rule catalogue with displacement values and workflow patterns |
| Uniform Rules Workflows | `uniform_rules_workflows.scm` | Procedural sequences U[k] for common strategies |
| Integration Layer | `integration_layer.scm` | Judgment algebra J = M ot U ot P to Omega, recommendation engine |

## Mathematical Framework

### Role Sets

Parties are represented as indexed sets where each element carries context:

| Symbol | Meaning | Example |
|--------|---------|---------|
| A[n] = {a_1, ..., a_n} | Applicant set | A[2] = {Ketoni Consulting, Sage VIP} |
| R[m] = {r_1, ..., r_m} | Respondent set | R[1] = {Daniel Sobey} |
| a_k(motion) | k-th applicant initiating motion | a_1(ex-parte-interdict) |
| r_k(motion) | k-th respondent responding to motion | r_1(rescission-application) |

### Motion/Action Algebra

Motions and actions are treated as distinct algebraic objects with different geometric properties.

**Motions** (angular moments) initiate rotational change in the procedural state space. They are filed by applicants/respondents and processed by courts. Each motion carries an angular displacement theta measuring its procedural impact.

**Actions** (linear moments) initiate translational change in the substantive state space. They are performed by plaintiffs/defendants and have real-world consequences. Each action carries a linear displacement d measuring its factual impact.

The composition operators are:

| Operator | Symbol | Meaning |
|----------|--------|---------|
| Serial | ot | Execute in sequence (causal chain) |
| Parallel | oplus | Execute simultaneously (independent) |

### Uniform Rules Sequences

Procedural strategies are encoded as ordered sequences of Uniform Rules:

```
U[3] = {u_30, u_7, u_42}
```

This represents: Rule 30(1) irregular proceedings, followed by Rule 7(1) authority challenge, concluded by Rule 42(1)(a) rescission. The total angular displacement is the sum of individual rule displacements.

### Judgment Algebra

The generalized judgment prediction formula:

```
J = M(A[n], R[m]) ⊗ U[k] ⊗ P(evidence) → Ω(outcome)
```

Where M is the motion space, U[k] is the rule sequence, P is the primitive set weighted by evidence, and Omega is the outcome function.

## Integration with ChainLex Hypergraph

The symbolic logic layer connects to the ChainLex hypergraph in `lawlibrary-repo-of-record` through the following pipeline:

```
Case Facts → Role Mapping → Motion/Action Extraction → Rule Sequence ID
     ↓                                                        ↓
Primitive Tagging → Archetype Matching → Hypergraph Query → Recommendation
     ↓                                                        ↓
Evidence Weighting → Success Probability → Strategic Advice → Filing
```

The hypergraph contains 62 nodes (primitives, courts, archetypes, domains) and 59 edges (causal pathways, jurisdictional links, workflow sequences) derived from forensic analysis of 843 judgments across 22 South African courts.

## Usage

Load the integration layer in any Scheme environment:

```scheme
(load "symbolic-logic/scm/integration_layer.scm")

;; Analyze a case
(define result
  (analyze-case-symbolically
    (make-case
      (parties '((applicant "a_1" "Ketoni Consulting")
                 (respondent "r_1" "Daniel Sobey")))
      (events '((motion "ex-parte-interdict" "2024-12-09")
                (motion "rescission-application" "2025-01-15")))
      (evidence '((documentary "email-chain" "2024-11-15")
                  (documentary "sage-access-log" "2024-12-01"))))))
```
