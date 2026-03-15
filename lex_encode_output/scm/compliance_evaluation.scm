;; ── Procedural Compliance Evaluation ─────────────────────────────
;; Generated: 2026-03-15T00:00:00
;; Case: 2025-137857
;; Rules evaluated: Rule 6 (ex parte/urgent), Rule 30 (irregular proceedings),
;;                  Rule 42 (rescission), Rule 45A (contempt)
;; Predicates: 7
;; Violated: 4, Applicable: 2, Defense-available: 1
;; ────────────────────────────────────────────────────────────────

;; Rule 6(4)(a): Duty of utmost good faith in ex parte applications
(define rule-6-4-a-disclosure-duty
  (predicate
    (rule "6(4)(a)")
    (requirement "applicant must make full disclosure of all material facts")
    (evaluation violated)
    (severity critical)
    (concealed-facts 7)
    (evidence "FNB sole mandate letter, fraud reports, card cancellation, R500K context, Sage sabotage, revenue diversion, trust forgery")))

;; Rule 6(5)(a): Urgency requirements
(define rule-6-5-a-urgency
  (predicate
    (rule "6(5)(a)")
    (evaluation violated)
    (severity major)
    (evidence "69-day delay between fraud report and filing proves no genuine urgency")))

;; Rule 6(12)(a): Ex parte justification
(define rule-6-12-a-ex-parte
  (predicate
    (rule "6(12)(a)")
    (evaluation violated)
    (severity critical)
    (evidence "Daniel held sole mandate — he was protecting accounts, not threatening them")))

;; Rule 30(1): Irregular proceedings
(define rule-30-1-irregular-step
  (predicate
    (rule "30(1)")
    (evaluation applicable)
    (severity critical)
    (evidence "3 irregular steps: non-disclosure, perjured affidavit, false claims")))

;; Rule 42(1)(a): Rescission of erroneously granted order
(define rule-42-1-a-rescission
  (predicate
    (rule "42(1)(a)")
    (evaluation applicable)
    (severity critical)
    (evidence "Order granted on perjured affidavit in absence of affected parties")))

;; Rule 42(1)(b): Void ab initio
(define rule-42-1-b-void-ab-initio
  (predicate
    (rule "42(1)(b)")
    (evaluation applicable)
    (severity critical)
    (evidence "Fraud on court: perjury, forgery, material non-disclosure, foreknowledge")))

;; Rule 45A: Contempt defense
(define rule-45a-contempt-defense
  (predicate
    (rule "45A")
    (evaluation defense-available)
    (severity critical)
    (evidence "Void order cannot ground contempt — Fakie NO v CCII Systems")))

(define procedural-violation-summary
  (summary
    (total-predicates 7)
    (violated 4)
    (applicable 2)
    (defense-available 1)
    (critical 6)
    (major 1)
    (overall-severity critical)
    (conclusion "Interdict void ab initio. Contempt application abuse of process.")))
