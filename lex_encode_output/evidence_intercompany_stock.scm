;; ═══════════════════════════════════════════════════════════════════
;; evidence_intercompany_stock.scm
;; LexRex Evidence Trees — Intercompany Transactions & Stock Adjustments
;; Case 2025-137857: Revenue Stream Hijacking
;; Generated: 2026-03-14
;; Pipeline: lex-sim-nn ( lexrex ) -> lex-encode-workflow
;; ═══════════════════════════════════════════════════════════════════

;; ── Entities ─────────────────────────────────────────────────────────

(define rynette-farrar
  (person-entity
    (name "Rynette Farrar")
    (role bookkeeper)
    (email "rynette@regima.zone")
    (access-level (sage-system pastel-system sars-efiling banking-systems))
    (evidence-source "Exchange mailbox ~1M messages")))

(define danie-bantjes
  (person-entity
    (name "Danie Bantjes")
    (role external-accountant)
    (saica-number "00105928")
    (email "danie.bantjes@gmail.com")
    (dual-role (cfo-george-group trustee-fft-fraudulent))
    (evidence-source "Exchange mailbox correspondence")))

(define pete-faucitt
  (person-entity
    (name "Peter Faucitt")
    (role founder-director)
    (email "pete@regima.com")
    (note "Does not use electronic communication — all digital comms authored by Rynette")))

(define strategic-logistics
  (organization-entity
    (name "Strategic Logistics CC")
    (registration "2008/136496/23")
    (type close-corporation)
    (accounts (fnb-platinum "62432501494") (fnb-savings "62593375829"))))

(define regima-skin-treatments
  (organization-entity
    (name "Regima Skin Treatments CC")
    (registration "1992/005371/23")
    (vat "4590131043")
    (type close-corporation)
    (accounts (fnb-platinum "55270035642") (fnb-money-market "62134839127"))))

(define regima-worldwide
  (organization-entity
    (name "Regima Worldwide Distribution (Pty) Ltd")
    (registration "2011/005722/07")
    (type private-company)
    (accounts (fnb-platinum "62323196362") (fnb-savings "62836164880"))))

(define villa-via
  (organization-entity
    (name "Villa Via Arcadia No 2 CC")
    (registration "1996/004451/23")
    (vat "4790157558")
    (type close-corporation)
    (accounts (fnb-current "62423540807") (fnb-money-on-call "62812835744"))))

(define regima-sa
  (organization-entity
    (name "Regima SA (Pty) Ltd")
    (registration "2017/087935/07")
    (type private-company)
    (accounts (fnb-platinum "62707308252"))))

(define sars
  (organization-entity
    (name "South African Revenue Service")
    (role tax-authority)
    (type government-body)))

;; ── Relations ────────────────────────────────────────────────────────

(define rel-rynette-directs-bantjes
  (conspiracy-relation
    (source rynette-farrar)
    (target danie-bantjes)
    (type "bookkeeper-directs-accountant")
    (description "Rynette instructed Bantjes on journal entries, reversing proper controls")
    (evidence "Exchange email 2021-08-17: Intercompany loan accounts")))

(define rel-bantjes-misstates-financials
  (evidential-relation
    (source danie-bantjes)
    (target strategic-logistics)
    (type "signed-misstated-financials")
    (description "Signed off on financials despite knowing of 'huge gaps building up over many years'")
    (evidence "Exchange email 2025-04-07: Re: TB's after stock adjustments")))

(define rel-intercompany-flow-rst-rsa
  (financial-relation
    (source regima-skin-treatments)
    (target regima-sa)
    (amount 35174935.48)
    (count 64)
    (type "intercompany-transfer")
    (note "Largest intercompany flow — revenue redirection vehicle")))

(define rel-intercompany-flow-rwd-rst
  (financial-relation
    (source regima-worldwide)
    (target regima-skin-treatments)
    (amount 12439605.00)
    (count 103)
    (type "intercompany-transfer")))

(define rel-intercompany-flow-vva-rst
  (financial-relation
    (source villa-via)
    (target regima-skin-treatments)
    (amount 8104000.00)
    (count 12)
    (type "intercompany-transfer")))

;; ── Evidence Trees (Matula-Godsil Prime Orders) ──────────────────────

;; ── ORDER 2: Simple Contradictions (Binary) ──────────────────────────

(define contradiction-stock-valuation
  ;; TB shows R1,443,217.78 finished goods; stock valuation shows ZERO
  (contradiction
    stock-on-trial-balance
    stock-on-valuation-zero
    (evidence (pastel-tb-feb-2024 "R1,443,217.78")
              (pastel-stock-valuation-feb-2024 "R0.00"))))

(define contradiction-negative-stock
  ;; Finished goods in CREDIT by R2,756,321.85 — physical impossibility
  (contradiction
    positive-stock-balance
    negative-stock-balance
    (evidence (pastel-tb-feb-2024-credit "R2,756,321.85 CR")
              (physical-impossibility "Stock cannot be negative"))))

(define contradiction-rynette-no-answer
  ;; Rynette processed invoices but has "no answer" for them
  (contradiction
    bookkeeper-understands-transactions
    bookkeeper-has-no-answer
    (evidence (exchange-email-2025-06-06
      "The two big invoices were done on your request, for which I have no answer"))))

;; ── ORDER 3: Temporal Chains ─────────────────────────────────────────

(define temporal-chain-backdated-journals
  ;; Entries dated 01/08/2020 created in August 2021 — over 1 year backdated
  (chain
    (journal-entry-date
      (date "2020-08-01")
      (then
        (instruction-date
          (date "2021-08-17")
          (then
            (email-from rynette-farrar)
            (email-to danie-bantjes)
            (subject "Intercompany loan accounts")
            (instruction "Debit account 5466/000 and credit supplier account for R300,000.00 date 01/08/20")))))))

(define temporal-chain-sars-query
  ;; Invoices pushed Feb 2025 → SARS query Jun 2025 → Response drafted Jun 2025
  (chain
    (invoices-pushed
      (date "2025-02-28")
      (actor danie-bantjes)
      (then
        (sars-notice-received
          (date "2025-06-05")
          (then
            (rynette-attributes-to-bantjes
              (date "2025-06-06")
              (quote "The two big invoices were done on your request")
              (then
                (bantjes-drafts-response
                  (date "2025-06-08")
                  (conflict-of-interest "Drafted response for own transactions"))))))))))

(define temporal-chain-stock-accumulation
  ;; Stock discrepancy building up over "many years" → discovered Apr 2025
  (chain
    (bernadine-manufacturing-system-introduced
      (date "2018-01-01")  ;; approximate
      (description "Manufacturing bills system for Proficos/Prime stock")
      (then
        (gaps-accumulate
          (duration "many years")
          (bantjes-admission "I suspect there are huge gaps by now, building up over many years")
          (then
            (rynette-discovers-discrepancy
              (date "2025-04-04")
              (amount-phantom "R1,443,217.78")
              (amount-negative "R2,756,321.85")
              (then
                (cover-up-proposed
                  (date "2025-04-04")
                  (quote "permanently remove this Bernadine gogga for good"))))))))))

;; ── ORDER 4: Entity-Relation Structures ──────────────────────────────

(define entity-structure-intercompany-web
  ;; R58.58M total intercompany volume across 364 transactions
  (corporate-structure
    (entity regima-skin-treatments (role "central-hub" flow-in 47518581.48 flow-out 35809370.06))
    (entity regima-worldwide (role "revenue-source" flow-out 12439605.00))
    (entity strategic-logistics (role "logistics-conduit" flow-in 1704040.56))
    (entity villa-via (role "property-vehicle" flow-in 8104000.00 flow-out 398366.00))
    (entity regima-sa (role "new-capture-entity" flow-in 35174935.48))
    (total-volume 58580962.89)
    (transaction-count 364)))

(define entity-structure-control-inversion
  ;; Bookkeeper directing external accountant — inversion of controls
  (corporate-structure
    (entity rynette-farrar (role bookkeeper actual-role "financial-controller"))
    (entity danie-bantjes (role external-accountant actual-role "instruction-taker"))
    (inversion "Bookkeeper instructs accountant on journal entries")
    (evidence "Exchange email 2021-08-17")))

;; ── ORDER 5: Foreknowledge Chains ────────────────────────────────────

(define foreknowledge-bantjes-stock-gaps
  ;; Bantjes knew of financial gaps for years but continued signing off
  (foreknowledge-chain
    (knew
      (who danie-bantjes)
      (when "2025-04-07")
      (what "huge gaps building up over many years in stock valuation")
      (prior-to
        (knew
          (who danie-bantjes)
          (when "2025-02-28")
          (what "pushed through two big intercompany invoices at year-end")
          (prior-to
            (knew
              (who danie-bantjes)
              (when "2021-08-17")
              (what "accepted backdated journal entry instructions from bookkeeper")
              (prior-to
                (established
                  (conclusion "Pattern of knowing participation in financial manipulation"))))))))))

(define foreknowledge-rynette-control
  ;; Rynette's progressive takeover of financial controls
  (foreknowledge-chain
    (knew
      (who rynette-farrar)
      (when "2025-04-04")
      (what "R4.2M stock discrepancy exists — proposed cover-up")
      (prior-to
        (knew
          (who rynette-farrar)
          (when "2024-04-26")
          (what "Logged into SARS eFiling as Bantjes to change banking details")
          (prior-to
            (knew
              (who rynette-farrar)
              (when "2021-08-17")
              (what "Directed specific backdated journal entries")
              (prior-to
                (knew
                  (who rynette-farrar)
                  (when "2020-09-28")
                  (what "Planned to 'clear loan accounts with one another'")
                  (prior-to
                    (established
                      (conclusion "Systematic financial control takeover"))))))))))))

;; ── ORDER 7: Structured Comparisons ─────────────────────────────────

(define irreconcilable-bantjes-roles
  ;; Bantjes as accountant vs. Bantjes as transaction initiator
  (irreconcilable-conflicts
    (conflict-accountant-vs-initiator
      (role-1 "External accountant who signs off on financials")
      (role-2 "Person who pushes through big intercompany invoices"))
    (conflict-auditor-vs-coverup
      (role-1 "Professional who should detect and report discrepancies")
      (role-2 "Person who admits gaps and plans to 'remove' them"))))

;; ── ORDER 35: {5,7} Interlock ──────────────────────────────────────

(define interlock-financial-manipulation
  ;; Temporal foreknowledge chain interlocked with structural role conflicts
  (interlock
    (temporal-dimension
      foreknowledge-bantjes-stock-gaps)
    (structural-dimension
      irreconcilable-bantjes-roles)
    (binding
      (exchange-email-2025-04-07
        "I suspect there are huge gaps by now, building up over many years"))))
