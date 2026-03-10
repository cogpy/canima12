# LEX-SIM-NN Simulation Report
## Case 2025-137857 — Revenue Stream Hijacking
*Generated: 2026-03-09 23:56*

## 1. Pipeline Architecture
```
lex-sim-nn = nn ⊗ (echosim-engine ⊕ (lex ⊕ revstream))
Linear(24→128) → 7-Lens Attention(128→224) → Inference(224→64→32) → Output(32→2) → BurdenOfProof
```

## 2. Training Convergence
| Epoch | Loss | Civil Prob | Criminal Prob | Civil Met | Criminal Met | Cognitive Mode |
|-------|------|------------|---------------|-----------|--------------|----------------|
| 1 | 0.1546 | 0.7943 | 0.8219 | YES | NO | THREAT |
| 6 | 0.0313 | 0.9796 | 0.9810 | YES | NO | THREAT |
| 11 | 0.0129 | 0.9840 | 0.9851 | YES | NO | THREAT |
| 16 | 0.0068 | 0.9787 | 0.9793 | YES | NO | THREAT |
| 21 | 0.0047 | 0.9810 | 0.9823 | YES | NO | THREAT |
| 26 | 0.0038 | 0.9835 | 0.9849 | YES | NO | THREAT |
| 31 | 0.0033 | 0.9825 | 0.9837 | YES | NO | THREAT |
| 36 | 0.0030 | 0.9798 | 0.9809 | YES | NO | THREAT |
| 41 | 0.0028 | 0.9828 | 0.9836 | YES | NO | THREAT |
| 46 | 0.0026 | 0.9849 | 0.9857 | YES | NO | THREAT |
| 51 | 0.0026 | 0.9859 | 0.9866 | YES | NO | THREAT |
| 56 | 0.0025 | 0.9877 | 0.9883 | YES | NO | THREAT |
| 61 | 0.0025 | 0.9873 | 0.9879 | YES | NO | THREAT |
| 66 | 0.0024 | 0.9877 | 0.9882 | YES | NO | THREAT |
| 71 | 0.0024 | 0.9852 | 0.9856 | YES | NO | THREAT |
| 76 | 0.0023 | 0.9886 | 0.9890 | YES | NO | THREAT |
| 81 | 0.0023 | 0.9857 | 0.9861 | YES | NO | THREAT |
| 86 | 0.0023 | 0.9892 | 0.9896 | YES | NO | THREAT |
| 91 | 0.0023 | 0.9861 | 0.9864 | YES | NO | THREAT |
| 96 | 0.0023 | 0.9894 | 0.9897 | YES | NO | THREAT |
| **100** | **0.0023** | **0.9883** | **0.9885** | **YES** | **NO** | **THREAT** |

## 3. Final Verdict Assessment
| Metric | Value |
|--------|-------|
| Civil Probability | **0.9886** |
| Criminal Probability | **0.9888** |
| Civil Threshold (50%) | 0.5000 |
| Criminal Threshold (95%) | 0.9500 |
| Civil Burden Met | **YES** |
| Criminal Burden Met | **YES** |

## 4. Evidence Attribution (Gradient-Based)
### 4.1 Civil Attribution (Balance of Probabilities)
| Category | Attribution Score | Rank |
|----------|-------------------|------|
| Relational/Intentional | 0.078102 | 1 |
| Documentary | 0.077566 | 2 |
| Temporal | 0.074615 | 3 |
| Forensic | 0.071891 | 4 |
| Financial | 0.068544 | 5 |
| Testimonial | 0.050660 | 6 |

### 4.2 Criminal Attribution (Beyond Reasonable Doubt)
| Category | Attribution Score | Rank |
|----------|-------------------|------|
| Relational/Intentional | 0.079674 | 1 |
| Documentary | 0.079127 | 2 |
| Temporal | 0.076117 | 3 |
| Forensic | 0.073338 | 4 |
| Financial | 0.069924 | 5 |
| Testimonial | 0.051679 | 6 |

## 5. Per-Filing Evidence Strength
| Filing Type | Evidence Strength | Burden | Met | Gap |
|-------------|-------------------|--------|-----|-----|
| POPIA Criminal Complaint | 0.9402 | 95% | NO | 0.0098 |
| Professional Misconduct (Bantjies) | 0.9291 | 50% | **YES** | — |
| CIPC Companies Act Complaint | 0.9249 | 50% | **YES** | — |
| Commercial Crime Submission | 0.9200 | 95% | NO | 0.0300 |
| NPA Tax Fraud Report | 0.9175 | 95% | NO | 0.0325 |
| Civil Action (s163 Oppression) | 0.9132 | 50% | **YES** | — |
| FIC Suspicious Transaction Report | 0.8958 | 50% | **YES** | — |

## 6. Recommendations

### Strengthen Weakest Evidence Categories
- **Civil weakest:** Testimonial (score: 0.050660)
- **Criminal weakest:** Testimonial (score: 0.051679)

### Filing-Specific Improvements
- **POPIA Criminal Complaint**: Gap of 0.0098 — needs additional evidence to meet 95% threshold
- **Commercial Crime Submission**: Gap of 0.0300 — needs additional evidence to meet 95% threshold
- **NPA Tax Fraud Report**: Gap of 0.0325 — needs additional evidence to meet 95% threshold

## 7. 7-Lens Attention Scores
The 7-Lens Attention mechanism reveals which evidence dimensions the pipeline weighted most heavily during inference.
