# LEX-SIM-NN Evidence Attribution Relations

## Updated: 2026-03-10

## Source: Differentiable Legal Simulation — Gradient-Based Attribution

---

## Relation Summary

The LEX-SIM-NN differentiable legal simulation pipeline provides a quantitative, gradient-based attribution of evidence strength across 6 categories and 7 legal filings. This relation maps the evidence categories to the specific filings they most strongly support, identifying both strengths and gaps.

---

## Evidence → Filing Attribution Map

```
EVIDENCE CATEGORIES                    FILING TYPES
═══════════════════                    ════════════

Relational/Intentional ──[0.0797]──→  CIPC Complaint (92.49%)
  (Conspiracy networks,               Professional Misconduct (92.91%)
   entity links, mens rea)            POPIA Criminal (94.02%)

Documentary ──────────[0.0791]──→     CIPC Complaint (92.49%)
  (Emails, CIPC records,              Commercial Crime (92.00%)
   contracts, affidavits)             Civil Action (91.32%)

Temporal ─────────────[0.0761]──→     All filings (timeline corroboration)
  (Dates, sequences,
   registration timelines)

Forensic ─────────────[0.0733]──→     POPIA Criminal (94.02%)
  (Digital traces,                    FIC Report (89.58%)
   metadata, stylometry)

Financial ────────────[0.0699]──→     NPA Tax Fraud (91.75%)
  (Amounts, flows,                    Commercial Crime (92.00%)
   transaction volumes)               FIC Report (89.58%)

Testimonial ──────────[0.0517]──→     WEAKEST CATEGORY
  (Witness statements,                All criminal filings need strengthening
   corroboration)                     Gap: ~3-5% to close criminal burden
```

---

## Per-Filing Evidence Composition

### Civil Filings (50% Burden — ALL MET)

| Filing | Strongest Evidence | Score | Status |
|--------|-------------------|-------|--------|
| Professional Misconduct | Documentary + Relational | 92.91% | **MET** |
| CIPC Complaint | Documentary + Relational | 92.49% | **MET** |
| Civil Action | Financial + Documentary | 91.32% | **MET** |
| FIC Report | Financial + Forensic | 89.58% | **MET** |

### Criminal Filings (95% Burden — NEAR THRESHOLD)

| Filing | Strongest Evidence | Score | Gap | Action Required |
|--------|-------------------|-------|-----|-----------------|
| POPIA Criminal | Forensic + Documentary | 94.02% | 0.98% | Strengthen testimonial: formal expert opinion on identity impersonation |
| Commercial Crime | Financial + Forensic | 92.00% | 3.00% | Strengthen testimonial: forensic accounting expert affidavit |
| NPA Tax Fraud | Financial + Documentary | 91.75% | 3.25% | Strengthen testimonial: SARS whistleblower report + expert tax opinion |

---

## Recommendations to Close Criminal Burden Gaps

### Priority 1: Expert Affidavits (closes ~2-3% gap)
1. **Forensic Accounting Expert**: Formal opinion on R10.27M+ fund flows, R5.4M stock disappearance, R900K unauthorized transfers
2. **Digital Forensics Expert**: Formal opinion on stylometry analysis (Rynette-as-Peter), email metadata, Sage audit trails
3. **Tax Expert**: Formal opinion on SARS "manufacture" admission and tax implications

### Priority 2: Witness Statements (closes ~1-2% gap)
1. **Customer Statements**: Customers who received unauthorized bank detail change notifications
2. **Staff Statements**: Former employees who witnessed Rynette's control over systems
3. **FNB Legal**: Formal statement confirming SOLE authority mandate

### Priority 3: Institutional Reports (corroboration)
1. **SARS Whistleblower Report**: File with "manufacture" email as primary evidence
2. **FIC STR**: Suspicious transaction report for ABSA account diversions
3. **CIPC Investigation Request**: Dual corporate identity investigation

---

## Cross-References

- [EVENT_SIM_001](../events/EVENT_SIM_001.md): LEX-SIM-NN simulation execution
- [EVENT_EML_001](../events/EVENT_EML_001.md): Forensic EML extraction
- [LEX-SIM-NN Report](../simulation/LEX_SIM_NN_REPORT_2026_03_10.md): Full simulation report
- [Forensic EML Index](../evidence/forensic_eml/INDEX.md): Email evidence archive
