;; ── Evidence Tree Encoding ────────────────────────────────────────
;; Generated: 2026-03-15T00:00:00
;; Case: 2025-137857 — Revenue Stream Hijacking, Trust Fraud, Corporate Sabotage
;; Items: 14
;; Order distribution: {2: 3, 3: 4, 4: 2, 5: 2, 7: 1, 35: 2}
;; ────────────────────────────────────────────────────────────────


;; ── Order 2 (Binary Contradictions) ─────────────────────────────
;; Each contradiction is grounded in specific documentary evidence.

(define sole-mandate-contradiction
  ;; Matula order 2 — Peter's founding affidavit claims Daniel made
  ;; "unauthorized transactions." FNB's own FICA/KYC records confirm
  ;; Daniel held "Administrator with SOLE General Powers."
  (contradiction
    unauthorized-transactions-by-daniel
    sole-transactional-authority-confirmed
    (FNB-FICA-KYC-sole-mandate-letter-18-June-2025)))

(define material-non-disclosure
  ;; Matula order 2 — Ex parte application requires full disclosure.
  ;; Peter concealed: (1) sole mandate, (2) fraud reports received by
  ;; Bantjies, (3) card cancellation retaliation, (4) R500K context.
  (contradiction
    full-disclosure-to-court
    concealed-sole-mandate-fraud-reports-card-sabotage
    (founding-affidavit-vs-FNB-letter-and-fraud-reports)))

(define perjury-bantjies-affidavit
  ;; Matula order 2 — Bantjies swore confirmatory affidavit 13 Aug 2025,
  ;; 68 days after receiving Daniel's detailed fraud report on 6 June 2025.
  ;; He forwarded the fraud report to his own work email, proving receipt.
  (contradiction
    confirmatory-affidavit-truthful
    received-fraud-reports-68-days-prior
    (fraud-report-6-June-2025-plus-bantjies-email-forward)))


;; ── Order 3 (Temporal Chains) ───────────────────────────────────
;; Each chain establishes an irreversible temporal sequence.

(define trust-forgery-timeline
  ;; Matula order 3 — Premeditation chain: murder → trust doc request → forgery
  (chain
    (kayla-murdered
      (date "2023-07-13")
      (then (rynette-requests-trust-docs
        (date "2023-07-27")
        (then (trust-forged-bantjies-installed
          (date "2024-06-28"))))))))

(define interdict-timeline
  ;; Matula order 3 — Retaliation chain: fraud report → card cancellation → perjured affidavit → interdict
  (chain
    (daniel-reports-fraud-to-bantjies
      (date "2025-06-06")
      (then (cards-cancelled-retaliation
        (date "2025-06-07")
        (then (bantjies-swears-false-affidavit
          (date "2025-08-13")
          (then (interdict-granted-ex-parte
            (date "2025-08-19"))))))))))

(define revenue-diversion-timeline
  ;; Matula order 3 — Revenue hijacking chain: SARS banking change → client emails → mass diversion
  (chain
    (SARS-eFiling-banking-changed-to-ABSA
      (date "2024-04-26")
      (then (bank-detail-change-emails-begin
        (date "2025-05-02")
        (then (39-plus-emails-sent-by-linda
          (date "2025-06-18"))))))))

(define sage-sabotage-timeline
  ;; Matula order 3 — Accounting sabotage chain: false affidavit → account transfer → pipeline broken
  (chain
    (peter-swears-false-sage-affidavit
      (date "2024-07-08")
      (then (sage-account-transferred
        (date "2024-07-09")
        (then (stock2shop-pipeline-broken
          (date "2024-07-10"))))))))


;; ── Order 4 (Entity-Relation Structures) ────────────────────────
;; Each structure encodes conflicting roles that prove motive.

(define corporate-structure-conflict
  ;; Matula order 4 — Bantjies holds dual roles creating irreconcilable conflict:
  ;; CFO of George Group (whose CEO Kevin Derrick directs Ketoni) AND
  ;; fraudulently installed trustee of FFT (creditor of Ketoni R18.685M).
  (corporate-structure
    (entity Danie-Bantjies
      (role CFO-George-Group)
      (role fraudulent-trustee-FFT)
      (conflict insider-access-to-R18.685M-payout-mechanism))
    (entity Ketoni-Investment-Holdings
      (role debtor-to-FFT)
      (amount "R18,685,000")
      (due-date "2026-05")
      (director Kevin-Derrick)
      (ceo-of George-Group))))

(define farrar-family-self-dealing
  ;; Matula order 4 — Rynette's family companies form a closed-loop extraction:
  ;; Adderory (packaging supplier + domain registrant), Luxury Products Online
  ;; (distribution), Luxuré (direct competitor to RegimA).
  (corporate-structure
    (entity Rynette-Farrar
      (role bookkeeper-identity-operator))
    (entity Adderory-Pty-Ltd
      (role sons-company)
      (action registered-regimaskin-co-za "2025-05-29")
      (action packaging-supplier-to-RegimA))
    (entity Luxury-Products-Online
      (role sons-company)
      (action distribution-channel))
    (entity Luxure
      (role sons-company)
      (action direct-competitor-to-RegimA))
    (relation closed-loop-self-dealing)))


;; ── Order 5 (Foreknowledge Chains) ──────────────────────────────
;; Each chain proves provable foreknowledge through temporally indexed evidence.

(define foreknowledge-chain-bantjies
  ;; Matula order 5 — Bantjies' foreknowledge chain (5 steps, each with evidence)
  (foreknowledge-chain
    (knew (who Bantjies) (when "2024-06-28")
      (what accepted-fraudulent-trustee-appointment)
      (evidence rynette-email-pp-peter-copy-of-your-id)
      (prior-to
        (knew (who Bantjies) (when "2025-05-26")
          (what secretly-shared-financial-analysis-with-rynette)
          (evidence email-ek-dink-nie-jy-moet-se-ek-het-hierdie-met-jou-gedeel)
          (prior-to
            (knew (who Bantjies) (when "2025-06-06")
              (what received-daniels-first-fraud-report)
              (evidence email-forward-to-work-email)
              (prior-to
                (knew (who Bantjies) (when "2025-06-10")
                  (what received-daniels-second-detailed-fraud-report)
                  (evidence email-acknowledgment)
                  (prior-to
                    (knew (who Bantjies) (when "2025-08-13")
                      (what swore-confirmatory-affidavit-contradicting-known-facts)
                      (evidence court-filing-68-days-after-fraud-report)
                      (established))))))))))))

(define foreknowledge-chain-rynette
  ;; Matula order 5 — Rynette's foreknowledge chain (6 steps, each with evidence)
  (foreknowledge-chain
    (knew (who Rynette) (when "2021-08-17")
      (what instructed-backdated-journal-entries)
      (evidence email-to-bantjies-journal-entries)
      (prior-to
        (knew (who Rynette) (when "2023-07-27")
          (what requested-trust-documents-14-days-after-kayla-murder)
          (evidence email-to-bantjies-trust-docs)
          (prior-to
            (knew (who Rynette) (when "2024-04-26")
              (what impersonated-bantjies-on-SARS-eFiling-changed-banking-to-ABSA)
              (evidence logged-in-as-you-email-bantjies-replied-all-good)
              (prior-to
                (knew (who Rynette) (when "2024-06-28")
                  (what forged-trust-amendment-signed-as-pp-peter)
                  (evidence email-copy-of-your-id-to-bantjies)
                  (prior-to
                    (knew (who Rynette) (when "2025-05-02")
                      (what initiated-revenue-diversion-bank-detail-changes)
                      (evidence banking-details-email-to-clients)
                      (prior-to
                        (knew (who Rynette) (when "2025-06-18")
                          (what commissioned-de-novo-fabrication-erasing-kayla)
                          (evidence fabricated-2019-accounts-removing-kayla-as-director)
                          (established))))))))))))))


;; ── Order 7 (Structured Comparisons) ────────────────────────────
;; Irreconcilable conflicts proving pattern of coordinated fraud.

(define irreconcilable-conflicts-of-interest
  ;; Matula order 7 — Three interlocking conflicts that cannot coexist with innocence
  (irreconcilable-conflicts
    (conflict-1
      (role-a CFO-George-Group)
      (role-b trustee-FFT)
      (person Danie-Bantjies)
      (nature insider-access-to-R18.685M-payout-mechanism)
      (evidence ketoni-sha-moi-baker-mckenzie-correspondence))
    (conflict-2
      (role-a external-accountant-for-all-companies)
      (role-b confirmatory-affidavit-deponent-against-client)
      (person Danie-Bantjies)
      (nature swore-against-client-who-reported-fraud-to-him-68-days-prior)
      (evidence fraud-report-email-forward-plus-court-filing))
    (conflict-3
      (role-a bookkeeper-employee)
      (role-b identity-operator-of-director-peter)
      (person Rynette-Farrar)
      (nature controlled-all-communications-attributed-to-peter-who-does-not-use-email)
      (evidence formal-notice-cessation-criminal-instructions-plus-pp-peter-emails))))


;; ── Order 35 ({5,7} Interlocks) ─────────────────────────────────
;; Cross-term attacks binding temporal and structural dimensions.

(define interlock-trust-forgery-revenue-capture
  ;; Matula order 35 — The trust forgery (temporal) is bound to the corporate
  ;; structure conflict (structural) by the Ketoni payout (binding evidence).
  ;; This interlock proves the forgery was not opportunistic but was the
  ;; mechanism to capture the R18.685M payout.
  (interlock
    (temporal-dimension trust-forgery-timeline)
    (structural-dimension corporate-structure-conflict)
    (binding ketoni-payout-R18.685M-due-May-2026)
    (evidence-binding
      (bantjies-email-26-Sep-2024-linking-trust-docs-to-ketoni-feedback)
      (baker-mckenzie-sha-moi-correspondence)
      (share-certificate-bantjies-ketoni-fft))))

(define interlock-sabotage-then-frame
  ;; Matula order 35 — The Sage sabotage (temporal) is bound to the Farrar
  ;; family self-dealing structure (structural) by the manufactured financial
  ;; chaos used as interdict evidence (binding).
  ;; This interlock proves the sabotage was deliberate — the chaos was
  ;; engineered to create the "evidence" for the perjured affidavit.
  (interlock
    (temporal-dimension sage-sabotage-timeline)
    (structural-dimension farrar-family-self-dealing)
    (binding manufactured-financial-chaos-used-as-interdict-evidence)
    (evidence-binding
      (rynette-email-orders-not-sinking-with-sage)
      (rynette-email-leave-kayla-as-owner-connectors-connected)
      (stock2shop-10-day-reconfiguration-log)
      (founding-affidavit-citing-financial-mismanagement))))
