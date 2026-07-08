;; ── Evidence Tree Encoding v16 ─────────────────────────────────────
;; Generated: 2026-03-18T06:21:08
;; Case: 2025-137857 — Revenue Stream Hijacking, Trust Fraud, Corporate Sabotage
;; Pipeline: skillm ( lex-sim-nn [ lex-rex | lexrex ] -> lex-encode-workflow )
;; Items: 14
;; Order distribution: {'2': 4, '3': 4, '4': 2, '5': 2, '7': 0, '35': 2}
;; ────────────────────────────────────────────────────────────────

;; ── Order 2 (Binary Contradictions) ─────────────────────────────
(define sole-mandate-contradiction
  ;; Matula order 2 — Binary contradiction grounded in documentary evidence
  (contradiction
    unauthorized-transactions-by-daniel
    sole-transactional-authority-confirmed
    (FNB-FICA-KYC-sole-mandate-letter-18-June-2025)))

(define material-non-disclosure
  ;; Matula order 2 — Binary contradiction grounded in documentary evidence
  (contradiction
    full-disclosure-to-court
    concealed-sole-mandate-fraud-reports-card-sabotage
    (founding-affidavit-vs-FNB-letter-and-fraud-reports)))

(define perjury-bantjies-affidavit
  ;; Matula order 2 — Binary contradiction grounded in documentary evidence
  (contradiction
    confirmatory-affidavit-truthful
    received-fraud-reports-68-days-prior
    (fraud-report-6-June-2025-plus-bantjies-email-forward)))

;; ── Order 3 (Temporal Chain) ──────────────────────────────────────
(define trust-forgery-timeline
  ;; Matula order 3 — Irreversible temporal sequence
  (chain
    (kayla-murdered
      (date "2023-07-13")
      (then (rynette-requests-trust-docs
        (date "2023-07-27"))
      (then (trust-forged-bantjies-installed
        (date "2024-06-28")))))))))

;; ── Order 3 (Temporal Chain) ──────────────────────────────────────
(define interdict-timeline
  ;; Matula order 3 — Irreversible temporal sequence
  (chain
    (daniel-reports-fraud-to-bantjies
      (date "2025-06-06")
      (then (cards-cancelled-retaliation
        (date "2025-06-07"))
      (then (bantjies-swears-false-affidavit
        (date "2025-08-13"))
      (then (interdict-granted-ex-parte
        (date "2025-08-19")))))))))))

;; ── Order 3 (Temporal Chain) ──────────────────────────────────────
(define revenue-diversion-timeline
  ;; Matula order 3 — Irreversible temporal sequence
  (chain
    (SARS-eFiling-banking-changed-to-ABSA
      (date "2024-04-26")
      (then (bank-detail-change-emails-begin
        (date "2025-05-02"))
      (then (39-plus-emails-sent-by-linda
        (date "2025-06-18")))))))))

;; ── Order 3 (Temporal Chain) ──────────────────────────────────────
(define sage-sabotage-timeline
  ;; Matula order 3 — Irreversible temporal sequence
  (chain
    (peter-swears-false-sage-affidavit
      (date "2024-07-08")
      (then (sage-account-transferred
        (date "2024-07-15"))
      (then (stock2shop-pipeline-broken
        (date "2024-08-01")))))))))

;; ── Order 4 (Entity Relation) ─────────────────────────────────────
(define corporate-structure-fraud
  ;; Matula order 4 — Structural entity-relation proof
  (entity-relation
    (entity daniel-jacobus-bantjies (role CFO_George_Group))
    (entity ketoni-investment-holdings (role debtor_to_FFT))
    (binding undisclosed-conflict-of-interest)))

;; ── Order 4 (Entity Relation) ─────────────────────────────────────
(define bantjies-false-independence
  ;; Matula order 4 — Structural entity-relation proof
  (entity-relation
    (entity daniel-jacobus-bantjies (role declared_independent_trustee))
    (entity the-george-group (role employer_of_bantjies))
    (binding J417-false-declaration)))

;; ── Order 5 (Foreknowledge Chain) ─────────────────────────────────
(define foreknowledge-chain-bantjies
  ;; Matula order 5 — Provable foreknowledge chain
  (foreknowledge-chain
    (knew (who daniel-jacobus-bantjies)
      (when "2025-06-06") (what received-fraud-report-from-daniel)
      (prior-to (knew
      (when "2025-06-06") (what forwarded-to-own-work-email)
      (prior-to (knew
      (when "2025-08-13") (what swore-false-confirmatory-affidavit)))))))))

;; ── Order 5 (Foreknowledge Chain) ─────────────────────────────────
(define foreknowledge-chain-peter
  ;; Matula order 5 — Provable foreknowledge chain
  (foreknowledge-chain
    (knew (who peter-andrew-faucitt)
      (when "2025-06-18") (what FNB-confirmed-sole-mandate-to-daniel)
      (prior-to (knew
      (when "2025-08-19") (what swore-founding-affidavit-concealing-sole-mandate)))))))

;; ── Order 35 ({5,7} Interlock) ──────────────────────────────────
(define intercompany-stock-interlock
  ;; Matula order 35 — Cross-term attack binding temporal and structural dimensions
  (interlock
    (temporal-dimension stock-discrepancy-timeline-2019-2025)
    (structural-dimension bantjies-rynette-peter-triangle)
    (binding R4.2M-phantom-stock-plus-negative-stock)))

;; ── Order 35 ({5,7} Interlock) ──────────────────────────────────
(define trust-ketoni-interlock
  ;; Matula order 35 — Cross-term attack binding temporal and structural dimensions
  (interlock
    (temporal-dimension trust-forgery-to-ketoni-payout-timeline)
    (structural-dimension bantjies-george-group-ketoni-FFT-circular)
    (binding J417-false-independence-plus-R28.73M-motive)))

(define j417-perjury-evidence
  ;; Matula order 2 — Binary contradiction grounded in documentary evidence
  (contradiction
    independent-trustee-declaration
    employed-as-CFO-George-Group
    (J417-form-plus-George-Group-employment-records)))

