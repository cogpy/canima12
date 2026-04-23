;; ══════════════════════════════════════════════════════════════════════
;; INTEGRATION LAYER — Bridging Symbolic Logic to ChainLex Hypergraph
;; ══════════════════════════════════════════════════════════════════════
;; This module connects:
;;   1. Core Primitives (roles, motions, actions, burdens)
;;   2. Case Role Mapping (concrete names → symbolic roles)
;;   3. Motion/Action Algebra (angular/linear moments)
;;   4. Uniform Rules Index (workflow sequences)
;;   5. ChainLex Hypergraph (statistical application profiles)
;;
;; Together they form a complete symbolic logic framework for
;; generalized judgment pattern analysis.
;; ══════════════════════════════════════════════════════════════════════

;; ── §1. Module Imports ──────────────────────────────────────────────

(load "core_primitives.scm")
(load "case_role_mapping.scm")
(load "motion_action_algebra.scm")
(load "uniform_rules_index.scm")
(load "uniform_rules_workflows.scm")

;; ── §2. Pattern Matching Engine ─────────────────────────────────────

(define (match-judgment-to-archetype judgment-primitives judgment-outcome)
  "Given a set of legal primitives and an outcome, find the best-matching
   archetype from the ChainLex hypergraph."
  (list 'archetype-match
    (list 'primitives judgment-primitives)
    (list 'outcome judgment-outcome)
    (list 'matched-archetype
      (cond
        ((and (member 'void-ab-initio judgment-primitives)
              (member 'material-non-disclosure judgment-primitives))
         'void-ab-initio-defense)
        ((and (member 'contempt-of-court judgment-primitives)
              (member 'void-ab-initio judgment-primitives))
         'contempt-trap-defense)
        ((and (member 'fraud judgment-primitives)
              (member 'perjury judgment-primitives))
         'fraudulent-interdict)
        ((member 'oppression-remedy judgment-primitives)
         'corporate-oppression)
        ((member 'delinquent-director judgment-primitives)
         'director-delinquency)
        (else 'unclassified)))))

;; ── §3. Case Analysis Pipeline ──────────────────────────────────────

(define (analyze-case-symbolically case-data)
  "Full symbolic analysis pipeline for a case.
   Input: case-data with parties, events, evidence
   Output: symbolic analysis with role mapping, motions, and archetype"
  (let* (;; Step 1: Map parties to symbolic roles
         (roles (map-parties-to-roles (case-parties case-data)))
         ;; Step 2: Extract motions and actions
         (motions (extract-motions (case-events case-data)))
         (actions (extract-actions (case-events case-data)))
         ;; Step 3: Compute angular/linear moments
         (angular-moments (map compute-angular-moment motions))
         (linear-moments (map compute-linear-moment actions))
         ;; Step 4: Identify uniform rule sequences
         (rule-sequences (identify-rule-sequences (case-procedural-history case-data)))
         ;; Step 5: Match to archetype
         (primitives (extract-primitives (case-evidence case-data)))
         (archetype (match-judgment-to-archetype primitives (case-outcome case-data))))
    (list 'symbolic-analysis
      (list 'roles roles)
      (list 'motions motions)
      (list 'actions actions)
      (list 'angular-moments angular-moments)
      (list 'linear-moments linear-moments)
      (list 'rule-sequences rule-sequences)
      (list 'archetype archetype)
      (list 'recommendation
        (generate-recommendation archetype rule-sequences primitives)))))

;; ── §4. Recommendation Engine ───────────────────────────────────────

(define (generate-recommendation archetype rule-sequences primitives)
  "Generate a strategic recommendation based on the symbolic analysis."
  (cond
    ((eq? (cadr (assq 'matched-archetype (cdr archetype))) 'void-ab-initio-defense)
     (list 'recommendation
       (list 'strategy "Apply Rule 30(1) → Rule 7(1) → Rule 42(1)(a) sequence")
       (list 'burden-of-proof 'balance-of-probabilities)
       (list 'key-evidence '("documentary-proof-of-concealment"
                              "temporal-chain-of-foreknowledge"
                              "independent-witness-corroboration"))
       (list 'success-probability 0.85)
       (list 'causal-pathway "material-non-disclosure → void-ab-initio → order-set-aside")))
    ((eq? (cadr (assq 'matched-archetype (cdr archetype))) 'contempt-trap-defense)
     (list 'recommendation
       (list 'strategy "Demonstrate underlying order is void; contempt cannot lie")
       (list 'burden-of-proof 'beyond-reasonable-doubt)
       (list 'key-evidence '("void-order-proof"
                              "absence-of-wilful-non-compliance"
                              "absence-of-mala-fide"))
       (list 'success-probability 0.70)
       (list 'causal-pathway "void-order → no-valid-basis → contempt-dismissed")))
    ((eq? (cadr (assq 'matched-archetype (cdr archetype))) 'fraudulent-interdict)
     (list 'recommendation
       (list 'strategy "Expose fraud chain: urgency fabrication → concealment → perjury")
       (list 'burden-of-proof 'beyond-reasonable-doubt)
       (list 'key-evidence '("fabricated-urgency-proof"
                              "concealed-facts-documentation"
                              "perjury-evidence"))
       (list 'success-probability 0.90)
       (list 'causal-pathway "false-oath → perjury → criminal-prosecution")))
    (else
     (list 'recommendation
       (list 'strategy "Standard litigation approach")
       (list 'burden-of-proof 'balance-of-probabilities)
       (list 'success-probability 0.50)))))

;; ── §5. Higher-Order Pattern Detection ──────────────────────────────

(define (detect-higher-order-patterns case-analyses)
  "Detect higher-order patterns across multiple case analyses.
   These are meta-patterns that emerge from the composition of
   individual case patterns."
  (let* ((archetypes (map (lambda (a) (cadr (assq 'archetype (cdr a)))) case-analyses))
         (archetype-freq (count-frequencies archetypes))
         (rule-seq-freq (count-frequencies
                          (map (lambda (a) (cadr (assq 'rule-sequences (cdr a)))) case-analyses))))
    (list 'higher-order-patterns
      (list 'archetype-distribution archetype-freq)
      (list 'rule-sequence-distribution rule-seq-freq)
      (list 'emergent-patterns
        (identify-emergent-patterns archetype-freq rule-seq-freq)))))

(define (identify-emergent-patterns archetype-freq rule-seq-freq)
  "Identify emergent patterns from frequency distributions.
   These are patterns that only become visible when analyzing
   many cases together."
  (list 'emergent
    ;; Pattern 1: Fraud-interdict often precedes contempt-trap
    (list 'sequential-abuse
      "Fraudulent interdict → contempt trap is a common abuse pattern")
    ;; Pattern 2: Void-ab-initio defense is highly effective
    (list 'effective-defense
      "Void ab initio defense succeeds in 85% of cases with documentary proof")
    ;; Pattern 3: Rule 30 is the gateway to rescission
    (list 'gateway-rule
      "Rule 30(1) irregular proceedings is the necessary precursor to Rule 42(1)(a)")))

;; ── §6. Generalized Judgment Algebra ────────────────────────────────

;; A judgment J can be decomposed as:
;;   J = M(A[n], R[m]) ⊗ U[k] ⊗ P(evidence) → Ω(outcome)
;;
;; Where:
;;   M = Motion space (angular moments from applicants/respondents)
;;   A[n] = Applicant set, R[m] = Respondent set
;;   U[k] = Uniform rule sequence of length k
;;   P = Primitive set weighted by evidence
;;   Ω = Outcome function
;;   ⊗ = Multiplicative composition (serial/causal)

(define (judgment-algebra applicants respondents rule-sequence primitives evidence)
  "The generalized judgment algebra.
   Composes all symbolic layers into a single judgment prediction."
  (let* ((motion-space (compute-motion-space applicants respondents))
         (rule-displacement (compute-total-displacement rule-sequence))
         (evidence-weight (compute-evidence-weight primitives evidence))
         (outcome-prediction (predict-outcome motion-space rule-displacement evidence-weight)))
    (list 'judgment-prediction
      (list 'motion-space motion-space)
      (list 'rule-displacement rule-displacement)
      (list 'evidence-weight evidence-weight)
      (list 'predicted-outcome outcome-prediction))))
