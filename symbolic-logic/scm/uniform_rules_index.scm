;; ══════════════════════════════════════════════════════════════════════
;; UNIFORM RULES INDEX — Complete Rule Catalogue with Workflow Patterns
;; ══════════════════════════════════════════════════════════════════════
;; Each rule is indexed with:
;;   - Rule number (u_i)
;;   - Category (procedural domain)
;;   - Angular displacement (procedural impact)
;;   - Success/failure archetypes
;;   - Prerequisite and successor rules
;; ══════════════════════════════════════════════════════════════════════

;; ── §1. Rule Catalogue ──────────────────────────────────────────────

(define (make-rule id number title category displacement prereqs successors)
  (list 'rule
    (list 'id id)
    (list 'number number)
    (list 'title title)
    (list 'category category)
    (list 'angular-displacement displacement)
    (list 'prerequisites prereqs)
    (list 'successors successors)))

;; Applications (Rule 6)
(define u_6-1   (make-rule 'u_6-1   "6(1)"   "Form of applications"         'applications 30  '() '(u_6-4 u_6-5)))
(define u_6-4   (make-rule 'u_6-4   "6(4)"   "Ex parte disclosure duty"     'applications 180 '(u_6-1) '(u_6-5)))
(define u_6-5-a (make-rule 'u_6-5-a "6(5)(a)" "Confirmatory affidavit"      'applications 90  '(u_6-4) '()))
(define u_6-12-a (make-rule 'u_6-12-a "6(12)(a)" "Urgent application"       'applications 135 '(u_6-1) '(u_6-12-b)))
(define u_6-12-b (make-rule 'u_6-12-b "6(12)(b)" "Urgency justification"    'applications 135 '(u_6-12-a) '()))

;; Power of Attorney (Rule 7)
(define u_7-1   (make-rule 'u_7-1   "7(1)"   "Power of attorney"            'authority 45 '() '()))

;; Irregular Proceedings (Rule 30)
(define u_30-1  (make-rule 'u_30-1  "30(1)"  "Irregular proceedings"         'irregularity 120 '() '(u_42-1-a)))

;; Rescission (Rule 42)
(define u_42-1-a (make-rule 'u_42-1-a "42(1)(a)" "Rescission of erroneous order" 'rescission -180 '(u_30-1) '()))

;; Contempt (Rule 45A)
(define u_45A   (make-rule 'u_45A   "45A"    "Contempt of court"             'enforcement 90 '() '()))

;; ── §2. Workflow Pattern Library ────────────────────────────────────
;; Standard sequences observed in South African case law

;; Pattern: VOID-AB-INITIO-DEFENSE
;; Sequence: u_30 → u_7 → u_42
;; Description: Identify irregularity, challenge authority, seek rescission
;; Success rate: HIGH when material non-disclosure is proven
(define pattern-void-ab-initio
  (list 'workflow-pattern
    (list 'name "void-ab-initio-defense")
    (list 'sequence '(u_30-1 u_7-1 u_42-1-a))
    (list 'total-displacement (+ 120 45 -180))  ; net = -15 (slight reversal)
    (list 'archetype 'successful-defense)
    (list 'triggers '("material-non-disclosure" "perjury" "fraud-on-court"))
    (list 'success-criteria '("documentary-proof-of-concealment"
                               "temporal-chain-of-foreknowledge"
                               "independent-witness-corroboration"))))

;; Pattern: FRAUDULENT-EX-PARTE
;; Sequence: u_6-12-b → u_6-12-a → u_6-4 → u_6-5-a
;; Description: Fabricate urgency, file urgent, conceal facts, perjure
;; Success rate: TEMPORARY — collapses when fraud exposed
(define pattern-fraudulent-ex-parte
  (list 'workflow-pattern
    (list 'name "fraudulent-ex-parte")
    (list 'sequence '(u_6-12-b u_6-12-a u_6-4 u_6-5-a))
    (list 'total-displacement (+ 135 135 180 90))  ; net = 540 (massive rotation)
    (list 'archetype 'temporary-success-then-collapse)
    (list 'triggers '("urgency-fabrication" "concealment-of-facts" "false-oath"))
    (list 'collapse-criteria '("respondent-discovers-fraud"
                                "independent-evidence-surfaces"
                                "confirmatory-affiant-exposed"))))

;; Pattern: CONTEMPT-TRAP
;; Sequence: [fraudulent-ex-parte] → u_45A
;; Description: Weaponize void order to threaten contempt
;; Success rate: FAILS when underlying order is void
(define pattern-contempt-trap
  (list 'workflow-pattern
    (list 'name "contempt-trap")
    (list 'sequence '(pattern-fraudulent-ex-parte u_45A))
    (list 'total-displacement (+ 540 90))  ; net = 630 (extreme rotation)
    (list 'archetype 'abuse-of-process)
    (list 'triggers '("void-order-enforcement" "intimidation" "coercion"))
    (list 'defeat-criteria '("underlying-order-void-ab-initio"
                              "no-wilful-non-compliance"
                              "no-mala-fide"))))

;; ── §3. Sequence Composition Algebra ────────────────────────────────
;; Sequences can be composed using ⊕ (additive/parallel) and ⊗ (multiplicative/serial)

(define (compose-sequences-serial . sequences)
  "Serial composition ⊗: execute sequences in order.
   Total displacement = sum of individual displacements."
  (list 'serial-composition
    (list 'operator '⊗)
    (list 'sequences sequences)
    (list 'total-displacement
      (apply + (map (lambda (s) (cadr (assq 'total-displacement (cdr s)))) sequences)))))

(define (compose-sequences-parallel . sequences)
  "Parallel composition ⊕: execute sequences simultaneously.
   Total displacement = max of individual displacements."
  (list 'parallel-composition
    (list 'operator '⊕)
    (list 'sequences sequences)
    (list 'max-displacement
      (apply max (map (lambda (s) (cadr (assq 'total-displacement (cdr s)))) sequences)))))
