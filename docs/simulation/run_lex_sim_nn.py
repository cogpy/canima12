#!/usr/bin/env python3
"""
LEX-SIM-NN: Differentiable Legal Simulation for Case 2025-137857
Revenue Stream Hijacking — Evidence Strength Assessment & Attribution

Encodes the 6-phase criminal enterprise as case events with 24-dim evidence vectors,
trains the LEXPipeline with VES modulation, and produces:
  1. Burden of proof assessment (civil 50% / criminal 95%)
  2. Evidence attribution per category
  3. Per-filing evidence strength scores
  4. Simulation report in Markdown
"""

import sys, json, os
sys.path.insert(0, "/home/ubuntu/skills/lex-sim-nn/scripts")

import torch
import numpy as np
from lex_pipeline import (LEXPipeline, GripOptimizer, VirtualEndocrineSystem,
                          CaseEvent, compute_evidence_attribution, EVIDENCE_CATEGORIES)

# ── 6-Phase Case Events with 24-dim evidence vectors ──────────────────
# Dims: [0-3] Temporal, [4-7] Financial, [8-11] Documentary,
#        [12-15] Testimonial, [16-19] Forensic, [20-23] Relational/Intentional

CASE_EVENTS = [
    # Phase 1: Entity Establishment & Trust Capture
    CaseEvent(
        phase=1, name="Entity Establishment & Trust Capture",
        description="Rynette Farrar forges 'pp Peter' on trust amendment (28 Jun 2024) to install "
                    "Bantjies as trustee. Bantjies has undisclosed conflict as CFO of George Group "
                    "(parent of Ketoni debtor). Villa Via/Kaylovest dual identity established.",
        evidence_vector=[
            0.95, 0.85, 0.90, 0.80,  # Temporal: CIPC dates, forgery date, trust timeline, registration
            0.70, 0.60, 0.65, 0.55,  # Financial: trust assets, Ketoni R18.75M, dual entity flows
            0.95, 0.90, 0.92, 0.88,  # Documentary: CIPC records, forged trust doc, Bantjies COI
            0.60, 0.55, 0.50, 0.45,  # Testimonial: witness statements, Jacqui corroboration
            0.85, 0.80, 0.78, 0.75,  # Forensic: digital signatures, metadata, stylometry
            0.90, 0.92, 0.88, 0.95,  # Relational: Bantjies-Derrick-Ketoni network, mens rea
        ],
        endocrine_event="entity_compromised", intensity=0.8
    ),
    # Phase 2: Client Diversion & Revenue Hijacking
    CaseEvent(
        phase=2, name="Client Diversion & Revenue Hijacking",
        description="Systematic diversion of R10.27M+ revenue through unauthorized ABSA account changes. "
                    "Rynette Farrar impersonates Peter Faucitt across Sage, email, banking systems. "
                    "100+ emails prove premeditated campaign. Shopify revenue redirected.",
        evidence_vector=[
            0.92, 0.88, 0.85, 0.90,  # Temporal: bank change dates, email timestamps, revenue shift dates
            0.95, 0.92, 0.90, 0.88,  # Financial: R10.27M diverted, ABSA accounts, Shopify revenue
            0.90, 0.88, 0.92, 0.85,  # Documentary: bank change forms, emails, Shopify config
            0.65, 0.60, 0.55, 0.50,  # Testimonial: customer confirmations, staff statements
            0.88, 0.85, 0.82, 0.80,  # Forensic: email headers, IP logs, Sage audit trail
            0.92, 0.90, 0.88, 0.95,  # Relational: Rynette-Peter coordination, Adderory involvement
        ],
        endocrine_event="revenue_diverted", intensity=0.9
    ),
    # Phase 3: Revenue Capture & Financial Extraction
    CaseEvent(
        phase=3, name="Revenue Capture & Financial Extraction",
        description="R900K unauthorized transfers from RegimA SA. R5.4M stock disappearance from "
                    "Strategic Logistics. R5.2M SLG stock adjustment fraud. Accounts systematically emptied.",
        evidence_vector=[
            0.90, 0.85, 0.88, 0.82,  # Temporal: transfer dates, stock dates, account emptying timeline
            0.98, 0.95, 0.92, 0.90,  # Financial: R900K, R5.4M, R5.2M, account balances
            0.88, 0.85, 0.90, 0.82,  # Documentary: bank statements, stock records, invoices
            0.55, 0.50, 0.45, 0.40,  # Testimonial: limited direct testimony
            0.82, 0.80, 0.78, 0.75,  # Forensic: FNB records, Sage entries, transaction traces
            0.88, 0.85, 0.90, 0.92,  # Relational: coordinated extraction pattern, entity links
        ],
        endocrine_event="fraud_detected", intensity=0.9
    ),
    # Phase 4: Concealment & Obstruction
    CaseEvent(
        phase=4, name="Concealment & Obstruction",
        description="Bantjies admits 'I will manufacture an answer' for SARS query. "
                    "Card cancellation sabotage. Sage lockout. Domain hijacking. "
                    "Perjured affidavit filed with material non-disclosures.",
        evidence_vector=[
            0.88, 0.85, 0.82, 0.80,  # Temporal: manufacture email date, card cancel date, affidavit date
            0.75, 0.70, 0.65, 0.60,  # Financial: indirect financial concealment
            0.95, 0.92, 0.90, 0.88,  # Documentary: manufacture email, affidavit, FNB letter
            0.70, 0.65, 0.60, 0.55,  # Testimonial: FNB legal confirmation, ENS acknowledgment
            0.90, 0.88, 0.85, 0.82,  # Forensic: email metadata, card cancellation records
            0.92, 0.90, 0.95, 0.88,  # Relational: coordinated concealment, perjury with foreknowledge
        ],
        endocrine_event="fraud_detected", intensity=0.85
    ),
    # Phase 5: Discovery & Investigation
    CaseEvent(
        phase=5, name="Discovery & Investigation",
        description="100,000+ emails analyzed revealing conspiracy networks. Stylometry confirms "
                    "Rynette authored emails as Peter. 1,632 Rynette-Bantjies communications analyzed. "
                    "Forensic fund flow tracing. Provable foreknowledge audit trail established.",
        evidence_vector=[
            0.92, 0.90, 0.88, 0.85,  # Temporal: analysis dates, discovery timeline
            0.85, 0.82, 0.80, 0.78,  # Financial: fund flow traces, reconciliation
            0.95, 0.92, 0.90, 0.95,  # Documentary: email corpus, forensic reports, analysis docs
            0.75, 0.70, 0.72, 0.68,  # Testimonial: expert analysis, corroboration
            0.95, 0.92, 0.90, 0.88,  # Forensic: stylometry, email headers, digital forensics
            0.90, 0.88, 0.92, 0.95,  # Relational: conspiracy network maps, entity-relation models
        ],
        endocrine_event="evidence_discovered", intensity=0.9
    ),
    # Phase 6: Legal Action & Filing
    CaseEvent(
        phase=6, name="Legal Action & Filing",
        description="6 formal applications prepared: Civil Action, CIPC Complaint, POPIA Criminal, "
                    "Commercial Crime, NPA Tax Fraud, FIC Report. RWD governance notices issued. "
                    "Void ab initio argument established. R63M formal demand.",
        evidence_vector=[
            0.90, 0.88, 0.85, 0.82,  # Temporal: filing dates, notice dates, demand dates
            0.90, 0.88, 0.85, 0.82,  # Financial: R63M demand, quantified damages
            0.92, 0.90, 0.88, 0.95,  # Documentary: complete filing package, cross-references
            0.72, 0.68, 0.65, 0.60,  # Testimonial: affidavit evidence, expert opinions
            0.88, 0.85, 0.82, 0.80,  # Forensic: complete forensic package
            0.92, 0.90, 0.88, 0.95,  # Relational: complete entity-relation model, burden assessment
        ],
        endocrine_event="case_filed", intensity=0.8
    ),
]

# ── Per-Filing Evidence Strength Assessment ────────────────────────────

FILING_TYPES = {
    "Civil Action (s163 Oppression)": {
        "burden": 0.50, "weight_categories": {
            "Financial": 0.30, "Documentary": 0.25, "Relational/Intentional": 0.20,
            "Temporal": 0.10, "Forensic": 0.10, "Testimonial": 0.05
        }
    },
    "CIPC Companies Act Complaint": {
        "burden": 0.50, "weight_categories": {
            "Documentary": 0.30, "Relational/Intentional": 0.25, "Financial": 0.20,
            "Temporal": 0.10, "Forensic": 0.10, "Testimonial": 0.05
        }
    },
    "POPIA Criminal Complaint": {
        "burden": 0.95, "weight_categories": {
            "Forensic": 0.30, "Documentary": 0.25, "Relational/Intentional": 0.20,
            "Temporal": 0.10, "Financial": 0.10, "Testimonial": 0.05
        }
    },
    "Commercial Crime Submission": {
        "burden": 0.95, "weight_categories": {
            "Financial": 0.30, "Forensic": 0.25, "Documentary": 0.20,
            "Relational/Intentional": 0.10, "Temporal": 0.10, "Testimonial": 0.05
        }
    },
    "NPA Tax Fraud Report": {
        "burden": 0.95, "weight_categories": {
            "Financial": 0.35, "Documentary": 0.25, "Forensic": 0.20,
            "Temporal": 0.10, "Relational/Intentional": 0.05, "Testimonial": 0.05
        }
    },
    "FIC Suspicious Transaction Report": {
        "burden": 0.50, "weight_categories": {
            "Financial": 0.35, "Forensic": 0.25, "Documentary": 0.20,
            "Temporal": 0.10, "Relational/Intentional": 0.05, "Testimonial": 0.05
        }
    },
    "Professional Misconduct (Bantjies)": {
        "burden": 0.50, "weight_categories": {
            "Documentary": 0.30, "Relational/Intentional": 0.25, "Forensic": 0.20,
            "Financial": 0.10, "Temporal": 0.10, "Testimonial": 0.05
        }
    },
}


def compute_filing_scores(attribution):
    """Compute per-filing evidence strength from attribution."""
    results = {}
    for filing, config in FILING_TYPES.items():
        score = 0.0
        for cat, weight in config["weight_categories"].items():
            attr_val = attribution.get("civil_attribution" if config["burden"] <= 0.50 
                                        else "criminal_attribution", {}).get(cat, 0.0)
            score += weight * attr_val
        # Normalize to 0-1 range
        max_possible = max(max(attribution.get("civil_attribution", {}).values(), default=0.001),
                          max(attribution.get("criminal_attribution", {}).values(), default=0.001))
        norm_score = min(1.0, score / max_possible) if max_possible > 0 else 0.0
        results[filing] = {
            "evidence_strength": round(norm_score, 4),
            "burden_threshold": config["burden"],
            "burden_met": norm_score >= config["burden"],
            "gap": round(max(0, config["burden"] - norm_score), 4),
        }
    return results


def generate_report(log, attribution, filing_scores, final_verdict):
    """Generate Markdown simulation report."""
    report = []
    report.append("# LEX-SIM-NN Simulation Report")
    report.append(f"## Case 2025-137857 — Revenue Stream Hijacking")
    report.append(f"*Generated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
    
    report.append("## 1. Pipeline Architecture")
    report.append("```")
    report.append("lex-sim-nn = nn ⊗ (echosim-engine ⊕ (lex ⊕ revstream))")
    report.append("Linear(24→128) → 7-Lens Attention(128→224) → Inference(224→64→32) → Output(32→2) → BurdenOfProof")
    report.append("```\n")
    
    report.append("## 2. Training Convergence")
    report.append("| Epoch | Loss | Civil Prob | Criminal Prob | Civil Met | Criminal Met | Cognitive Mode |")
    report.append("|-------|------|------------|---------------|-----------|--------------|----------------|")
    for entry in log[::5]:  # Every 5th epoch
        report.append(f"| {entry['epoch']} | {entry['loss']:.4f} | {entry['civil_prob']:.4f} | "
                      f"{entry['criminal_prob']:.4f} | {'YES' if entry['civil_met'] else 'NO'} | "
                      f"{'YES' if entry['criminal_met'] else 'NO'} | {entry['mode']} |")
    # Always include last
    last = log[-1]
    report.append(f"| **{last['epoch']}** | **{last['loss']:.4f}** | **{last['civil_prob']:.4f}** | "
                  f"**{last['criminal_prob']:.4f}** | **{'YES' if last['civil_met'] else 'NO'}** | "
                  f"**{'YES' if last['criminal_met'] else 'NO'}** | **{last['mode']}** |")
    report.append("")
    
    report.append("## 3. Final Verdict Assessment")
    report.append(f"| Metric | Value |")
    report.append(f"|--------|-------|")
    report.append(f"| Civil Probability | **{final_verdict['civil_probability']:.4f}** |")
    report.append(f"| Criminal Probability | **{final_verdict['criminal_probability']:.4f}** |")
    report.append(f"| Civil Threshold (50%) | {final_verdict['civil_threshold']:.4f} |")
    report.append(f"| Criminal Threshold (95%) | {final_verdict['criminal_threshold']:.4f} |")
    report.append(f"| Civil Burden Met | **{'YES' if final_verdict['civil_met'] else 'NO'}** |")
    report.append(f"| Criminal Burden Met | **{'YES' if final_verdict['criminal_met'] else 'NO'}** |")
    report.append("")
    
    report.append("## 4. Evidence Attribution (Gradient-Based)")
    report.append("### 4.1 Civil Attribution (Balance of Probabilities)")
    report.append("| Category | Attribution Score | Rank |")
    report.append("|----------|-------------------|------|")
    civil = sorted(attribution['civil_attribution'].items(), key=lambda x: -x[1])
    for rank, (cat, score) in enumerate(civil, 1):
        report.append(f"| {cat} | {score:.6f} | {rank} |")
    report.append("")
    
    report.append("### 4.2 Criminal Attribution (Beyond Reasonable Doubt)")
    report.append("| Category | Attribution Score | Rank |")
    report.append("|----------|-------------------|------|")
    criminal = sorted(attribution['criminal_attribution'].items(), key=lambda x: -x[1])
    for rank, (cat, score) in enumerate(criminal, 1):
        report.append(f"| {cat} | {score:.6f} | {rank} |")
    report.append("")
    
    report.append("## 5. Per-Filing Evidence Strength")
    report.append("| Filing Type | Evidence Strength | Burden | Met | Gap |")
    report.append("|-------------|-------------------|--------|-----|-----|")
    for filing, scores in sorted(filing_scores.items(), key=lambda x: -x[1]['evidence_strength']):
        met_str = "**YES**" if scores['burden_met'] else "NO"
        gap_str = f"{scores['gap']:.4f}" if scores['gap'] > 0 else "—"
        report.append(f"| {filing} | {scores['evidence_strength']:.4f} | "
                      f"{scores['burden_threshold']:.0%} | {met_str} | {gap_str} |")
    report.append("")
    
    report.append("## 6. Recommendations")
    report.append("")
    # Identify weakest categories
    weakest_civil = min(attribution['civil_attribution'].items(), key=lambda x: x[1])
    weakest_criminal = min(attribution['criminal_attribution'].items(), key=lambda x: x[1])
    
    report.append(f"### Strengthen Weakest Evidence Categories")
    report.append(f"- **Civil weakest:** {weakest_civil[0]} (score: {weakest_civil[1]:.6f})")
    report.append(f"- **Criminal weakest:** {weakest_criminal[0]} (score: {weakest_criminal[1]:.6f})")
    report.append("")
    
    # Filing-specific recommendations
    report.append("### Filing-Specific Improvements")
    for filing, scores in filing_scores.items():
        if not scores['burden_met']:
            report.append(f"- **{filing}**: Gap of {scores['gap']:.4f} — needs additional "
                          f"evidence to meet {scores['burden_threshold']:.0%} threshold")
        elif scores['evidence_strength'] < 0.85:
            report.append(f"- **{filing}**: Meets burden but marginal ({scores['evidence_strength']:.4f}) — "
                          f"consider strengthening for robustness")
    report.append("")
    
    report.append("## 7. 7-Lens Attention Scores")
    report.append("The 7-Lens Attention mechanism reveals which evidence dimensions the pipeline "
                  "weighted most heavily during inference.\n")
    
    return "\n".join(report)


def main():
    print("=" * 60)
    print("LEX-SIM-NN: Case 2025-137857 Simulation")
    print("=" * 60)
    
    # Build pipeline
    pipeline = LEXPipeline(evidence_dim=24)
    optimizer = GripOptimizer(pipeline, base_lr=0.005)
    
    # Target: both civil and criminal burdens met
    target = torch.tensor([1.0, 1.0])
    
    # Train
    print("\n[1/4] Training pipeline on 6-phase case events...")
    log = optimizer.train_on_case(CASE_EVENTS, target, epochs=100)
    print(f"  Final loss: {log[-1]['loss']:.4f}")
    print(f"  Civil prob: {log[-1]['civil_prob']:.4f} (met: {log[-1]['civil_met']})")
    print(f"  Criminal prob: {log[-1]['criminal_prob']:.4f} (met: {log[-1]['criminal_met']})")
    print(f"  Cognitive mode: {log[-1]['mode']}")
    
    # Compute final verdict with combined evidence
    print("\n[2/4] Computing final verdict with combined evidence...")
    combined = np.mean([ev.evidence_vector for ev in CASE_EVENTS], axis=0)
    combined_tensor = torch.tensor(combined, dtype=torch.float32).unsqueeze(0)
    pipeline.eval()
    final_result = pipeline(combined_tensor)
    final_verdict = final_result['verdict']
    print(f"  Civil: {final_verdict['civil_probability']:.4f} (threshold: {final_verdict['civil_threshold']:.4f})")
    print(f"  Criminal: {final_verdict['criminal_probability']:.4f} (threshold: {final_verdict['criminal_threshold']:.4f})")
    
    # Attribution
    print("\n[3/4] Computing evidence attribution via backpropagation...")
    attribution = compute_evidence_attribution(pipeline, combined_tensor)
    for cat in EVIDENCE_CATEGORIES:
        c_score = attribution['civil_attribution'][cat]
        k_score = attribution['criminal_attribution'][cat]
        print(f"  {cat:25s} | Civil: {c_score:.6f} | Criminal: {k_score:.6f}")
    
    # Filing scores
    print("\n[4/4] Computing per-filing evidence strength...")
    filing_scores = compute_filing_scores(attribution)
    for filing, scores in sorted(filing_scores.items(), key=lambda x: -x[1]['evidence_strength']):
        status = "MET" if scores['burden_met'] else f"GAP: {scores['gap']:.4f}"
        print(f"  {filing:40s} | {scores['evidence_strength']:.4f} / {scores['burden_threshold']:.0%} | {status}")
    
    # Generate report
    report = generate_report(log, attribution, filing_scores, final_verdict)
    report_path = os.path.join(os.path.dirname(__file__), "LEX_SIM_NN_REPORT_2026_03_10.md")
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"\nReport saved to: {report_path}")
    
    # Save raw results as JSON
    results = {
        "training_log": log,
        "final_verdict": final_verdict,
        "attribution": {k: {ck: float(cv) for ck, cv in v.items()} 
                       for k, v in attribution.items()},
        "filing_scores": filing_scores,
    }
    json_path = os.path.join(os.path.dirname(__file__), "LEX_SIM_NN_RESULTS_2026_03_10.json")
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to: {json_path}")
    
    return results


if __name__ == "__main__":
    main()
