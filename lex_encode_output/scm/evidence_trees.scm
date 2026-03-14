;; ── Evidence Tree Encoding ────────────────────────────────────────
;; Generated: 2026-03-14T16:26:39.816972
;; Items: 8
;; Order distribution: {2: 2, 3: 3, 4: 1, 5: 0, 7: 1, 35: 1}
;; ────────────────────────────────────────────────────────────────


;; ── Order 2 ──────────────────────────────────────────────────
(define non-disclosure-evidence
  ;; Matula order 2
  (contradiction full-disclosure material-concealment (founding-affidavit-para-12)))
(define sole-mandate-evidence
  ;; Matula order 2
  (contradiction unauthorized-transactions sole-transactional-authority (fnb-fica-kyc-sole-mandate)))

;; ── Order 3 ──────────────────────────────────────────────────
(define trust-forgery-timeline
  ;; Matula order 3
  (chain (kayla-murdered (date "2023-07-13") (then (trust-docs-requested (date "2023-07-27") (then (trust-forged (date "2024-06-28"))))))))
(define interdict-timeline
  ;; Matula order 3
  (chain (fraud-reported (date "2025-06-06") (then (cards-cancelled (date "2025-06-07") (then (interdict-granted (date "2025-08-19"))))))))
(define foreknowledge-chain-evidence
  ;; Matula order 3
  (chain (fraud-reported-to-bantjies (date "2025-06-06") (then (bantjies-swears-affidavit (date "2025-08-13") (then (interdict-granted (date "2025-08-19"))))))))

;; ── Order 4 ──────────────────────────────────────────────────
(define corporate-structure-evidence
  ;; Matula order 4
  (corporate-structure (entity Danie Bantjies (role CFO-George-Group)) (entity Ketoni Investment Holdings (role debtor-to-trust))))

;; ── Order 7 ──────────────────────────────────────────────────
(define irreconcilable-conflicts-evidence
  ;; Matula order 7
  (irreconcilable-conflicts-evidence ;; order-7 — requires manual encoding))

;; ── Order 35 ──────────────────────────────────────────────────
(define interlock-evidence
  ;; Matula order 35
  (interlock (temporal-dimension trust-forgery-timeline) (structural-dimension corporate-structure-evidence) (binding ketoni-payout-capture)))
