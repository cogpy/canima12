;; ── Defense Morphisms & Blocks ────────────────────────────────────
;; Generated: 2026-03-14T16:26:39.817266
;; Defenses: 14
;; Blocks: 14
;; ────────────────────────────────────────────────────────────────

(define defense-2-simple-denial-0
  ;; Order 2: Deny the factual claim outright
  (morphism (pattern simple-denial) (order 2)))

(define defense-2-simple-denial-1
  ;; Order 2: Deny the factual claim outright
  (morphism (pattern simple-denial) (order 2)))

(define defense-3-temporal-reframing-0
  ;; Order 3: Argue events occurred in different order
  (morphism (pattern temporal-reframing) (order 3)))

(define defense-3-temporal-reframing-1
  ;; Order 3: Argue events occurred in different order
  (morphism (pattern temporal-reframing) (order 3)))

(define defense-3-temporal-reframing-2
  ;; Order 3: Argue events occurred in different order
  (morphism (pattern temporal-reframing) (order 3)))

(define defense-3-temporal-gap-0
  ;; Order 3: Argue insufficient time between events
  (morphism (pattern temporal-gap) (order 3)))

(define defense-3-temporal-gap-1
  ;; Order 3: Argue insufficient time between events
  (morphism (pattern temporal-gap) (order 3)))

(define defense-3-temporal-gap-2
  ;; Order 3: Argue insufficient time between events
  (morphism (pattern temporal-gap) (order 3)))

(define defense-4-structural-reconfiguration-0
  ;; Order 4: Argue entity relationships differ
  (morphism (pattern structural-reconfiguration) (order 4)))

(define defense-4-role-dispute-0
  ;; Order 4: Dispute the assigned roles
  (morphism (pattern role-dispute) (order 4)))

(define defense-7-pattern-denial-0
  ;; Order 7: Deny the comparison pattern holds
  (morphism (pattern pattern-denial) (order 7)))

(define defense-7-false-equivalence-0
  ;; Order 7: Argue the compared items are not comparable
  (morphism (pattern false-equivalence) (order 7)))

(define defense-35-interlock-severance-0
  ;; Order 35: Attack temporal or structural dimension independently
  (morphism (pattern interlock-severance) (order 35)))

(define defense-35-binding-challenge-0
  ;; Order 35: Challenge the binding evidence connecting dimensions
  (morphism (pattern binding-challenge) (order 35)))

;; ── Blocks ───────────────────────────────────────────────────────
(block defense-2-simple-denial-0 (evidence-contradicts simple-denial))
(block defense-2-simple-denial-1 (evidence-contradicts simple-denial))
(block defense-3-temporal-reframing-0 (evidence-contradicts temporal-reframing))
(block defense-3-temporal-reframing-1 (evidence-contradicts temporal-reframing))
(block defense-3-temporal-reframing-2 (evidence-contradicts temporal-reframing))
(block defense-3-temporal-gap-0 (evidence-contradicts temporal-gap))
(block defense-3-temporal-gap-1 (evidence-contradicts temporal-gap))
(block defense-3-temporal-gap-2 (evidence-contradicts temporal-gap))
(block defense-4-structural-reconfiguration-0 (evidence-contradicts structural-reconfiguration))
(block defense-4-role-dispute-0 (evidence-contradicts role-dispute))
(block defense-7-pattern-denial-0 (evidence-contradicts pattern-denial))
(block defense-7-false-equivalence-0 (evidence-contradicts false-equivalence))
(block defense-35-interlock-severance-0 (evidence-contradicts interlock-severance))
(block defense-35-binding-challenge-0 (evidence-contradicts binding-challenge))
