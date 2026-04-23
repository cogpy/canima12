;; ══════════════════════════════════════════════════════════════════════
;; MOTION/ACTION ALGEBRA — Angular & Linear Moment Framework
;; ══════════════════════════════════════════════════════════════════════
;; Motions (↻) = Angular moments (rotational, procedural maneuvers)
;; Actions (→) = Linear moments (translational, substantive events)
;; 
;; The legal state space is a manifold where:
;;   - Angular moments change the ORIENTATION (procedural posture)
;;   - Linear moments change the POSITION (factual state)
;;   - The cross product (↻ × →) yields TORQUE (legal leverage)
;; ══════════════════════════════════════════════════════════════════════

;; ── §1. Angular Moment (Motion) Algebra ─────────────────────────────
;; A motion M_θ applied by actor α at time t with angular displacement θ:
;;   M_θ(α, t) = (α, θ, ω, L)
;; where:
;;   α = actor (role symbol)
;;   θ = angular displacement (procedural shift magnitude)
;;   ω = angular velocity (urgency/speed of procedural change)
;;   L = angular momentum (procedural inertia, resistance to reversal)

(define (angular-moment actor time motion-type displacement velocity)
  "Construct an angular moment (procedural motion).
   displacement: 0-360 degrees (0=no change, 180=complete reversal)
   velocity: rate of procedural change (higher = more urgent)"
  (let ((momentum (* displacement velocity)))
    (list 'angular-moment
      (list 'actor actor)
      (list 'time time)
      (list 'type motion-type)
      (list 'displacement displacement)    ; θ
      (list 'velocity velocity)            ; ω
      (list 'momentum momentum)            ; L = θ·ω
      (list 'reversible? (< momentum 100)) ; high momentum = hard to reverse
      )))

;; Standard angular displacements for common motions
(define angular-displacements
  '((ex-parte       . 180)  ; Maximum rotation — bypasses adversarial process entirely
    (urgent         . 135)  ; Near-maximum — compresses timeline drastically
    (interdict      . 120)  ; Large rotation — freezes opposing party's actions
    (contempt       . 90)   ; Right angle — enforcement perpendicular to main dispute
    (rescission     . -180) ; Full reversal — undoes prior rotation
    (joinder        . 45)   ; Moderate — adds new dimension to proceedings
    (amendment      . 30)   ; Small — modifies existing trajectory
    (appeal         . 90)   ; Elevation — shifts to higher plane
    (review         . 60)   ; Re-examination — partial reorientation
    (stay           . 0)    ; Zero — freezes angular momentum
    ))

;; ── §2. Linear Moment (Action) Algebra ──────────────────────────────
;; An action F_x applied by actor α at time t with linear displacement x:
;;   F_x(α, t) = (α, x, v, p)
;; where:
;;   α = actor (role symbol)
;;   x = displacement (factual change magnitude)
;;   v = velocity (speed of factual change)
;;   p = linear momentum (factual inertia, weight of evidence)

(define (linear-moment actor time action-type displacement velocity)
  "Construct a linear moment (substantive action).
   displacement: magnitude of factual state change
   velocity: rate of factual change"
  (let ((momentum (* displacement velocity)))
    (list 'linear-moment
      (list 'actor actor)
      (list 'time time)
      (list 'type action-type)
      (list 'displacement displacement)    ; x
      (list 'velocity velocity)            ; v
      (list 'momentum momentum)            ; p = x·v
      (list 'evidence-weight momentum)     ; higher momentum = stronger evidence
      )))

;; Standard linear displacements for common actions
(define linear-displacements
  '((fraud          . 100)  ; Maximum — fundamental misrepresentation
    (theft          . 95)   ; Near-maximum — unlawful appropriation
    (perjury        . 90)   ; Very high — false oath
    (forgery        . 85)   ; High — fabricated documents
    (conspiracy     . 80)   ; High — coordinated scheme
    (diversion      . 75)   ; Significant — revenue stream redirection
    (non-disclosure . 70)   ; Significant — concealment of material facts
    (breach         . 60)   ; Moderate — contractual violation
    (impersonation  . 55)   ; Moderate — identity fraud
    (destruction    . 50)   ; Moderate — evidence destruction
    ))

;; ── §3. Cross Product: Torque (Legal Leverage) ─────────────────────
;; τ = M_θ × F_x = angular × linear
;; Torque represents the combined procedural-substantive leverage
;; High torque = strong legal position (both procedure AND substance favor)
;; Low torque = weak position (procedure OR substance is deficient)

(define (legal-torque angular-m linear-m)
  "Compute the legal torque (cross product of angular and linear moments).
   Returns the magnitude and direction of combined legal leverage."
  (let* ((L (cadr (assq 'momentum (cdr angular-m))))
         (p (cadr (assq 'momentum (cdr linear-m))))
         (tau (* L p))
         (direction (cond
           ((and (> L 0) (> p 0)) 'favorable)
           ((and (< L 0) (> p 0)) 'procedural-weakness)
           ((and (> L 0) (< p 0)) 'substantive-weakness)
           (else 'unfavorable))))
    (list 'torque
      (list 'magnitude tau)
      (list 'direction direction)
      (list 'angular-component L)
      (list 'linear-component p))))

;; ── §4. Orthogonality Analysis ──────────────────────────────────────
;; When motions and actions are orthogonal, they operate in independent
;; dimensions. A strong linear action (clear fraud evidence) cannot be
;; defeated by an orthogonal angular motion (jurisdictional challenge).

(define (orthogonality-test motion action)
  "Test whether a motion and action are orthogonal (independent dimensions).
   Returns the dot product — 0 means perfectly orthogonal."
  (let* ((motion-type (cadr (assq 'type (cdr motion))))
         (action-type (cadr (assq 'type (cdr action))))
         ;; Orthogonality matrix: 0 = orthogonal, 1 = parallel, -1 = anti-parallel
         (dot-product (orthogonality-lookup motion-type action-type)))
    (list 'orthogonality
      (list 'motion-type motion-type)
      (list 'action-type action-type)
      (list 'dot-product dot-product)
      (list 'orthogonal? (= dot-product 0))
      (list 'parallel? (= dot-product 1))
      (list 'anti-parallel? (= dot-product -1)))))

;; Orthogonality lookup table
;; Key insight: procedural motions are generally orthogonal to substantive actions
;; EXCEPT when the procedure directly enables or blocks the substance
(define orthogonality-matrix
  '(;; motion-type    action-type       dot-product
    (ex-parte        fraud              1)   ; ex parte ENABLES fraud (parallel)
    (ex-parte        non-disclosure     1)   ; ex parte REQUIRES non-disclosure
    (rescission      fraud             -1)   ; rescission OPPOSES fraud (anti-parallel)
    (rescission      perjury           -1)   ; rescission OPPOSES perjury
    (contempt        breach             0)   ; contempt is orthogonal to breach
    (interdict       diversion          1)   ; interdict can enable diversion
    (urgent          conspiracy         1)   ; urgency can enable conspiracy
    (appeal          fraud              0)   ; appeal is orthogonal to fraud
    (stay            destruction        0)   ; stay is orthogonal to destruction
    ))

(define (orthogonality-lookup motion-type action-type)
  (let ((entry (assq motion-type
                 (filter (lambda (e) (eq? (cadr e) action-type))
                   orthogonality-matrix))))
    (if entry (caddr entry) 0))) ; default: orthogonal

;; ── §5. Case-Specific Moment Encoding ───────────────────────────────
;; Encode the actual motions and actions in Case 2025-137857

;; === MOTIONS (Angular Moments) ===

;; a_1(ex_parte): Applicant files ex parte urgent interdict
(define M1-ex-parte
  (angular-moment 'a_1 "2025-08-19" 'ex-parte 180 10))
;; θ=180 (maximum rotation), ω=10 (very fast) → L=1800 (massive momentum)

;; a_1(contempt): Applicant threatens contempt via attorney
(define M2-contempt
  (angular-moment 'a_1 "2025-09-30" 'contempt 90 5))
;; θ=90 (perpendicular enforcement), ω=5 (moderate) → L=450

;; r_2(rescission): Respondent seeks rescission of void order
(define M3-rescission
  (angular-moment 'r_2 "2026-01-01" 'rescission -180 3))
;; θ=-180 (full reversal), ω=3 (measured) → L=-540 (counter-rotation)

;; === ACTIONS (Linear Moments) ===

;; a_1(fraud): Revenue stream hijacking
(define F1-fraud
  (linear-moment 'a_1 "2015-01-01" 'fraud 100 8))
;; x=100 (maximum), v=8 (sustained over years) → p=800

;; c_2(perjury): False confirmatory affidavit
(define F2-perjury
  (linear-moment 'c_2 "2025-08-13" 'perjury 90 10))
;; x=90 (very high), v=10 (immediate) → p=900

;; a_1(diversion): Revenue stream diversion
(define F3-diversion
  (linear-moment 'a_1 "2021-01-01" 'diversion 75 7))
;; x=75 (significant), v=7 (sustained) → p=525

;; c_1(conspiracy): Financial manipulation with c_2
(define F4-conspiracy
  (linear-moment 'c_1 "2015-01-01" 'conspiracy 80 6))
;; x=80 (high), v=6 (long-running) → p=480

;; a_1(non-disclosure): Material non-disclosure in founding affidavit
(define F5-non-disclosure
  (linear-moment 'a_1 "2025-08-19" 'non-disclosure 70 10))
;; x=70 (significant), v=10 (immediate) → p=700

;; === TORQUE CALCULATIONS ===

;; The ex parte motion combined with fraud action
(define tau-1 (legal-torque M1-ex-parte F1-fraud))
;; τ = 1800 × 800 = 1,440,000 (massive favorable torque for applicant)
;; BUT this is FRAUDULENT torque — it collapses when fraud is exposed

;; The rescission motion combined with perjury evidence
(define tau-2 (legal-torque M3-rescission F2-perjury))
;; τ = -540 × 900 = -486,000 (strong counter-torque for respondent)
;; This is LEGITIMATE torque — rescission is proper remedy for perjury
