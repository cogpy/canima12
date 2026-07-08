;; ═══════════════════════════════════════════════════════════════════
;; corpus_intercompany_stock.scm
;; Legal Corpus — Intercompany Transactions & Stock Adjustments
;; Applicable Legal Frameworks
;; ═══════════════════════════════════════════════════════════════════

;; ── Companies Act 71 of 2008 ─────────────────────────────────────────

(define companies-act-s28
  ;; s.28: Accounting records
  (legal-rule
    (domain "corporate")
    (section "28")
    (act "Companies Act 71 of 2008")
    (requirement "A company must keep accurate and complete accounting records")
    (violation-if
      (or (records-materially-misstated)
          (records-not-kept)
          (records-deliberately-falsified)))))

(define companies-act-s29
  ;; s.29: Financial statements
  (legal-rule
    (domain "corporate")
    (section "29")
    (act "Companies Act 71 of 2008")
    (requirement "Financial statements must fairly present the state of affairs")
    (violation-if
      (or (phantom-assets-on-balance-sheet)
          (impossible-negative-stock)
          (material-misstatement-not-corrected)))))

;; ── Tax Administration Act 28 of 2011 ────────────────────────────────

(define taa-s235
  ;; s.235: Tax evasion
  (legal-rule
    (domain "criminal-tax")
    (section "235")
    (act "Tax Administration Act 28 of 2011")
    (offence-if
      (or (wilfully-evade-tax)
          (make-false-statement-to-sars)
          (submit-false-return)
          (fraudulent-intercompany-invoices-to-manipulate-vat)))))

(define taa-s234
  ;; s.234: Fraud, theft, forgery
  (legal-rule
    (domain "criminal-tax")
    (section "234")
    (act "Tax Administration Act 28 of 2011")
    (offence-if
      (or (forge-document-for-tax-purpose)
          (use-forged-document)
          (make-false-entry-in-books)))))

;; ── SAICA Code of Professional Conduct ───────────────────────────────

(define saica-integrity
  (professional-rule
    (domain "professional-conduct")
    (body "SAICA")
    (principle "Integrity")
    (violation-if
      (or (knowingly-associated-with-misleading-information)
          (failed-to-report-material-misstatement)
          (conflict-of-interest-not-disclosed)))))

(define saica-professional-competence
  (professional-rule
    (domain "professional-conduct")
    (body "SAICA")
    (principle "Professional Competence and Due Care")
    (violation-if
      (or (failed-to-detect-material-discrepancy-for-years)
          (accepted-instructions-from-bookkeeper-on-journal-entries)
          (signed-off-on-materially-misstated-financials)))))

;; ── Prevention of Organised Crime Act 121 of 1998 ────────────────────

(define poca-s4
  ;; s.4: Money laundering
  (legal-rule
    (domain "criminal")
    (section "4")
    (act "POCA 121 of 1998")
    (offence-if
      (or (conceals-nature-of-proceeds)
          (disguises-source-of-proceeds)
          (intercompany-transactions-to-obscure-flows)))))

;; ── Anticipated Defense Morphisms ────────────────────────────────────

;; Order 2: Simple Denials
(define defense-no-knowledge
  (defense-morphism
    (order 2)
    (claim "Bantjes had no knowledge of the stock discrepancy")
    (blocked-by contradiction-stock-valuation)))

(define defense-bernadine-fault
  (defense-morphism
    (order 2)
    (claim "The errors were Bernadine's fault, not ours")
    (blocked-by
      (evidence "Bantjes signed off on financials for years without detecting or reporting"
                "Rynette and Bantjes planned to 'remove' rather than properly restate"))))

(define defense-routine-intercompany
  (defense-morphism
    (order 2)
    (claim "The intercompany invoices were routine business transactions")
    (blocked-by contradiction-rynette-no-answer)))

;; Order 3: Temporal Reframings
(define defense-timing-coincidence
  (defense-morphism
    (order 3)
    (claim "The year-end timing of the invoices was coincidental")
    (blocked-by temporal-chain-sars-query)))

(define defense-backdating-correction
  (defense-morphism
    (order 3)
    (claim "The backdated entries were legitimate corrections")
    (blocked-by temporal-chain-backdated-journals)))

;; Order 4: Structural Reconfigurations
(define defense-normal-group-structure
  (defense-morphism
    (order 4)
    (claim "The intercompany flows reflect normal group operations")
    (blocked-by entity-structure-intercompany-web)))

;; Order 5: Sequence Disruptions
(define defense-no-pattern
  (defense-morphism
    (order 5)
    (claim "There was no pattern of deliberate manipulation")
    (blocked-by foreknowledge-bantjes-stock-gaps)))

;; Order 7: Structured Comparisons
(define defense-professional-judgment
  (defense-morphism
    (order 7)
    (claim "Bantjes exercised professional judgment in all matters")
    (blocked-by irreconcilable-bantjes-roles)))

;; Order 6 (2×3): Denial + Temporal Reframing
(define defense-composite-no-knowledge-timing
  (defense-morphism
    (order 6)
    (claim "Had no knowledge AND timing was coincidental")
    (composite (factor-2 defense-no-knowledge) (factor-3 defense-timing-coincidence))
    (blocked-by (rigid-interlock
      contradiction-stock-valuation
      temporal-chain-sars-query
      (binding "Bantjes' own email admissions")))))

;; Order 10 (2×5): Denial + Structural Reconfiguration
(define defense-composite-no-pattern-normal-ops
  (defense-morphism
    (order 10)
    (claim "No deliberate pattern AND normal business operations")
    (composite (factor-2 defense-routine-intercompany) (factor-5 defense-no-pattern))
    (blocked-by (rigid-interlock
      contradiction-rynette-no-answer
      foreknowledge-bantjes-stock-gaps
      (binding "SARS independently flagged the transactions")))))

;; Order 35 ({5,7}): Cross-term Attack
(define defense-composite-interlock
  (defense-morphism
    (order 35)
    (claim "No foreknowledge AND exercised professional judgment")
    (composite (factor-5 defense-no-pattern) (factor-7 defense-professional-judgment))
    (blocked-by interlock-financial-manipulation)))
