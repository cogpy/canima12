#!/usr/bin/env python3
"""
Execute the LEX Encode Workflow with the comprehensive Case 2025-137857 scenario.
"""
import json
import sys
import os
import importlib
from datetime import datetime
from pathlib import Path

# Add workflow steps to path
WORKFLOW_DIR = "/home/ubuntu/skills/lex-encode-workflow/scripts/workflow"
sys.path.insert(0, WORKFLOW_DIR)

# Output directory
OUTPUT_DIR = "/home/ubuntu/revstream1/lex_encode_output"
SCM_DIR = os.path.join(OUTPUT_DIR, "scm")
CERT_DIR = os.path.join(OUTPUT_DIR, "certificates")
os.makedirs(SCM_DIR, exist_ok=True)
os.makedirs(CERT_DIR, exist_ok=True)

# Load scenario
with open(os.path.join(OUTPUT_DIR, "scenario_comprehensive.json")) as f:
    scenario = json.load(f)

# Build context
context = {
    "_pipeline": {
        "start_time": datetime.now().isoformat(),
        "output_dir": SCM_DIR,
    },
    "scenario": scenario,
}

# Define steps
steps = [
    "steps.stage_1_domain_classification_corpus_selection__configure_corpus_paths_and_load_api",
    "steps.stage_1_domain_classification_corpus_selection__classify_legal_domain_from_scenario_facts",
    "steps.stage_1_domain_classification_corpus_selection__extract_relevant_principles_from_corpus",
    "steps.stage_1_domain_classification_corpus_selection__validate_corpus_selection_completeness",
    "steps.stage_2_evidence_encoding_defense_enumeration__configure_lexrex_engine_and_contradiction_oracle",
    "steps.stage_2_evidence_encoding_defense_enumeration__encode_entities_and_relations_as_s_expressions",
    "steps.stage_2_evidence_encoding_defense_enumeration__encode_evidence_trees_at_correct_matula_prime_orders",
    "steps.stage_2_evidence_encoding_defense_enumeration__enumerate_defense_morphisms_and_generate_blocks",
    "steps.stage_2_evidence_encoding_defense_enumeration__classify_interlock_patterns_order_35",
    "steps.stage_2_evidence_encoding_defense_enumeration__validate_evidence_tree_structural_integrity",
    "steps.stage_3_procedural_compliance_evaluation__load_relevant_procedural_rule_scm_files",
    "steps.stage_3_procedural_compliance_evaluation__construct_procedural_timeline_with_deadlines",
    "steps.stage_3_procedural_compliance_evaluation__evaluate_compliance_predicates_against_evidence",
    "steps.stage_3_procedural_compliance_evaluation__classify_procedural_violations_severity",
    "steps.stage_3_procedural_compliance_evaluation__validate_procedural_evaluation_completeness",
    "steps.orchestration_proof_certificate_generation__pipeline_assembly",
    "steps.orchestration_proof_certificate_generation__ml_feedback_loop",
    "steps.orchestration_proof_certificate_generation__final_validation",
]

print(f"{'='*70}")
print(f"LEX ENCODE WORKFLOW — Case 2025-137857")
print(f"{'='*70}")
print(f"Scenario: {scenario['title']}")
print(f"Entities: {len(scenario['entities'])}")
print(f"Relations: {len(scenario['relations'])}")
print(f"Evidence items: {len(scenario['evidence'])}")
print(f"Events: {len(scenario['events'])}")
print(f"Legal domains: {len(scenario['legal_domains'])}")
print(f"{'='*70}\n")

for i, mod_name in enumerate(steps):
    short_name = mod_name.split(".")[-1]
    print(f"[{i+1}/{len(steps)}] {short_name}")
    try:
        mod = importlib.import_module(mod_name)
        context = mod.run(context)
        if hasattr(mod, "validate"):
            valid = mod.validate(context)
            print(f"  Validation: {'PASS' if valid else 'FAIL'}")
            if not valid:
                print(f"  WARNING: Validation failed, continuing...")
        print(f"  Status: OK")
    except Exception as e:
        print(f"  ERROR: {e}")
        import traceback
        traceback.print_exc()
        print(f"  Continuing to next step...")
    print()

# Save final context
context["_pipeline"]["end_time"] = datetime.now().isoformat()
with open(os.path.join(OUTPUT_DIR, "pipeline_result.json"), "w") as f:
    json.dump({k: v for k, v in context.items() if k != "_pipeline"}, f, indent=2, default=str)

print(f"\n{'='*70}")
print(f"Pipeline complete. Output: {OUTPUT_DIR}")
print(f"{'='*70}")
