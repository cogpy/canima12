;; ══════════════════════════════════════════════════════════════════════
;; UNIFORM RULES WORKFLOWS — Procedural Sequences
;; ══════════════════════════════════════════════════════════════════════
;; Maps Uniform Rules of Court to sequential workflows (U[m]).
;; These sequences represent standard procedural pathways and strategies.
;; ══════════════════════════════════════════════════════════════════════

;; ── §1. Base Rule Definitions ───────────────────────────────────────

(define rules
  '((6-4    . "Ex parte application disclosure duty")
    (6-5-a  . "Confirmatory affidavit requirements")
    (6-12-a . "Urgent application requirements")
    (6-12-b . "Urgency justification")
    (7-1    . "Power of attorney requirements")
    (30-1   . "Irregular proceedings")
    (42-1-a . "Rescission of erroneously granted order")
    (45A    . "Contempt of court")))

;; ── §2. Workflow Sequences (U[m]) ───────────────────────────────────

;; U_fraud_interdict: The sequence used by the applicant to obtain the void order
;; 1. Claim urgency (6-12-b)
;; 2. File urgent application (6-12-a)
;; 3. Fail ex parte disclosure duty (6-4)
;; 4. Submit false confirmatory affidavit (6-5-a)
(define U_fraud_interdict
  (make-rule-sequence "Fraudulent Ex Parte Interdict"
    '((6-12-b . "Fabricate urgency")
      (6-12-a . "File urgent application")
      (6-4    . "Conceal material facts")
      (6-5-a  . "Submit perjured confirmatory affidavit"))))

;; U_rescission_defense: The sequence used by the respondent to defeat the void order
;; 1. Identify irregular step (30-1)
;; 2. Challenge authority of opposing counsel (7-1)
;; 3. Apply for rescission of erroneously granted order (42-1-a)
(define U_rescission_defense
  (make-rule-sequence "Rescission Defense Strategy"
    '((30-1   . "Identify irregular ex parte order")
      (7-1    . "Challenge ENS Africa authority")
      (42-1-a . "Apply for rescission based on fraud"))))

;; U_contempt_trap: The sequence used by the applicant to weaponize the void order
;; 1. Obtain void order (via U_fraud_interdict)
;; 2. Threaten contempt for non-compliance (45A)
(define U_contempt_trap
  (make-rule-sequence "Contempt Trap"
    '((45A . "Threaten contempt based on void order"))))

;; ── §3. Sequence Evaluation ─────────────────────────────────────────

(define (evaluate-sequence sequence evidence-tree)
  "Evaluate a workflow sequence against an evidence tree to determine
   if the sequence was successfully executed or successfully blocked."
  ;; Placeholder for integration with LexRex evaluation engine
  (list 'sequence-evaluation
    (list 'sequence-name (cadr (assq 'name (cdr sequence))))
    (list 'status 'pending-lexrex-integration)))
