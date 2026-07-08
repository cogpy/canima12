---
name: ksm-lex-dgen-alexander
description: "A specialized skill that composes KSM (Knowledge Sharing Mechanism) evolution cycles with the LEX legal framework and DreamGen narrative generation. It implements all 12 steps of Christopher Alexander's structure-preserving transformation and evaluates his 15 qualities of living structure within the legal-evidence context. Use when you need to evolve a legal case, evaluate the 'life' (coherence and strength) of evidence structures, or generate introspective DreamGen narratives about the legal strategy's evolution. Triggers on mentions of Alexander's 15 properties, structure-preserving transformation, KSM-LEX-DGen, or living legal structure."
---

# KSM-LEX-DGen-Alexander

This specialized skill integrates the Knowledge Sharing Mechanism (KSM) evolution cycle, the LEX legal framework, and DreamGen (DGen) narrative generation. It applies Christopher Alexander's 12-step structure-preserving transformation process and evaluates his 15 fundamental properties of living structure within a legal-evidence context.

## Composition Topology

```
/ksm-lex-dgen-alexander = /workflow-creator (
  /ksm-evolve [
    /lex-digitwin-nn ⊗ /apl253 (15-qualities)
  ] -> /dte-dgen-narrative ( /dgenkey )
)
```

This composition wraps the LEX legal simulation (`lex-digitwin-nn`) and Alexander's pattern language (`apl253`) inside a KSM evolution cycle (`ksm-evolve`), piping the resulting structural transformations into DreamGen (`dte-dgen-narrative`) to generate an introspective narrative of the legal strategy's evolution.

## The 12-Step Structure-Preserving Transformation

The skill executes a 12-step pipeline that maps Alexander's generative process to legal case evolution:

1. **OBSERVE**: Scan the current evidentiary field (wholeness).
2. **IDENTIFY**: Locate the strongest and weakest legal centers (arguments/evidence).
3. **DETECT**: Find the latent center where a new legal argument wants to emerge.
4. **THINK**: Analyze which transformation would most intensify the existing case.
5. **DISCOVER**: Determine which of the 15 properties could be strengthened.
6. **INSPECT**: Verify the proposed filing preserves existing legal structure.
7. **MUTATE**: Apply the transformation (draft/refine the filing).
8. **CREATE**: Instantiate the new legal center (concrete evidence integration).
9. **OBSERVE**: Apply the "mirror of the self" test (does this serve justice/truth?).
10. **OBSERVE**: Re-evaluate the entire evidentiary field after the change.
11. **CREATE**: Record the iteration in organizational memory.
12. **ORCHESTRATE**: Generate the DreamGen narrative of the evolution and prepare for the next cycle.

## The 15 Qualities of Living Legal Structure

The skill evaluates the legal case against Alexander's 15 properties:

1. **Levels of Scale**: Evidence at micro (email), meso (pattern), and macro (conspiracy) levels.
2. **Strong Centers**: Core allegations with overwhelming documentary proof.
3. **Boundaries**: Clear delineation between entities, roles, and responsibilities.
4. **Alternating Repetition**: Patterns of repeated fraud across multiple channels.
5. **Positive Space**: Every element of the case serves a specific legal purpose.
6. **Good Shape**: Each filing is well-formed and internally coherent.
7. **Local Symmetries**: Each sub-argument has its own internal balance.
8. **Deep Interlock**: Evidence categories reinforce each other.
9. **Contrast**: Clear distinction between lawful and unlawful conduct.
10. **Gradients**: Escalation patterns from minor to major violations.
11. **Roughness**: Adaptation to specific facts (not template-driven).
12. **Echoes**: Recurring patterns across different fraud categories.
13. **The Void**: The central truth that anchors the entire case.
14. **Simplicity**: Despite complexity, the core narrative remains clear.
15. **Not-Separateness**: Connection to broader legal frameworks and precedent.

## Quick Start

```bash
# Run the full 12-step Alexander transformation cycle on a legal case
python3 /home/ubuntu/skills/ksm-lex-dgen-alexander/scripts/run_alexander_cycle.py \
  --case /path/to/case_spec.json \
  --narrative-style "introspective-legal"
```

## Bundled Resources

| Path | Description |
|------|-------------|
| `scripts/run_alexander_cycle.py` | The core 12-step executable pipeline |
| `references/alexander_legal_mapping.md` | Detailed mapping of the 15 properties to legal concepts |
| `templates/alexander_workflow.yaml` | The workflow-creator specification |
| `templates/scenario_alexander.json` | DreamGen scenario template for structural evolution |
