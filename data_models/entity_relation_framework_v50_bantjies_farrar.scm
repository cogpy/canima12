;;; =============================================================================
;;; ENTITY-RELATION FRAMEWORK V50 - BANTJIES-FARRAR COMMUNICATIONS INTEGRATED
;;; =============================================================================
;;; Version: 50.0
;;; Date: 2026-03-07
;;; Purpose: Entity-relation model with 1,632 Bantjies-Farrar communications
;;; Source: rynette_bantjies_all(2).json — Exchange + Gmail 2015-2026
;;; SMOKING GUN: EVENT_119 — "I will manufacture an answer" (2025-06-06)
;;; =============================================================================

;;; -----------------------------------------------------------------------------
;;; SECTION 1: CENTRAL MOTIVE (UNCHANGED FROM V49)
;;; -----------------------------------------------------------------------------
(define-motive ketoni-payout-capture
  (description "Scheme to capture 100% of R18.685M Ketoni payout through curatorship fraud")
  (amount 18685000)
  (currency "ZAR")
  (due-date "2026-05")
  (debtor "Ketoni Investment Holdings (Pty) Ltd")
  (creditor "Faucitt Family Trust")
  (beneficiary-split
    (peter-share 0.50 9342500)
    (jax-share 0.50 9342500))
  (scheme-goal "Peter captures Jax's share via curatorship + Bantjies as trustee")
  (confidence 0.99)
  (source "V49 + Bantjies-Farrar communications 2026-03-07"))

;;; -----------------------------------------------------------------------------
;;; SECTION 2: NEW ENTITIES (2026-03-07)
;;; -----------------------------------------------------------------------------
(define-entity marc-yudaken
  (type natural-person)
  (entity-id "PERSON_042")
  (role "Attorney — Baker McKenzie")
  (role-in-scheme "Drafted Ketoni SHA/MOI on instructions from Bantjies")
  (involvement-events ("EVENT_116"))
  (evidence-strength 0.95)
  (source "Bantjies-Farrar communications"))

(define-entity david-field
  (type natural-person)
  (entity-id "PERSON_043")
  (role "Deal Consultant — Kevin Derrick")
  (role-in-scheme "Finalized Ketoni SHA/MOI with Bantjies")
  (involvement-events ("EVENT_116"))
  (evidence-strength 0.90)
  (source "Bantjies-Farrar communications"))

(define-entity denny-da-silva
  (type natural-person)
  (entity-id "PERSON_044")
  (role "Attorney — Baker McKenzie")
  (role-in-scheme "Coordinated Ketoni meetings")
  (involvement-events ("EVENT_116"))
  (evidence-strength 0.85)
  (source "Bantjies-Farrar communications"))

(define-entity baker-mckenzie
  (type organization)
  (entity-id "ORG_025")
  (role "International Law Firm — Ketoni SHA/MOI")
  (key-personnel ("PERSON_042" "PERSON_044"))
  (involvement-events ("EVENT_116"))
  (evidence-strength 0.95)
  (source "Bantjies-Farrar communications"))

;;; -----------------------------------------------------------------------------
;;; SECTION 3: UPDATED ENTITY EVIDENCE STRENGTHS
;;; -----------------------------------------------------------------------------
(update-entity rynette-farrar
  (entity-id "PERSON_002")
  (evidence-strength-previous 0.95)
  (evidence-strength-current 0.99)
  (new-events
    ("EVENT_114" "Anton Hechter removal from VAT portal")
    ("EVENT_115" "eFiling credential sharing")
    ("EVENT_117" "Ketoni payment to shareholder loan")
    ("EVENT_119" "Facilitated SARS answer manufacturing")
    ("EVENT_120" "Proof of address for trustee appointment"))
  (new-actions
    "Removed Anton Hechter from VAT portal"
    "Shared eFiling credentials with Bantjies"
    "Provided proof of address for trustee appointment"
    "Facilitated SARS answer manufacturing")
  (communication-volume 1632)
  (source "1,632 email communications 2015-2026"))

(update-entity daniel-jacobus-bantjes
  (entity-id "PERSON_007")
  (evidence-strength-previous 0.95)
  (evidence-strength-current 0.99)
  (new-events
    ("EVENT_114" "Anton Hechter removal from VAT portal")
    ("EVENT_115" "eFiling credential sharing")
    ("EVENT_116" "Ketoni SHA/MOI negotiation via Baker McKenzie")
    ("EVENT_117" "Ketoni payment to shareholder loan")
    ("EVENT_118" "Beneficial ownership raised")
    ("EVENT_119" "SMOKING GUN: 'I will manufacture an answer'")
    ("EVENT_120" "Proof of address for trustee appointment"))
  (new-actions
    "Admitted manufacturing SARS answer (SMOKING GUN)"
    "Negotiated Ketoni SHA/MOI via Baker McKenzie"
    "Directed Ketoni payment to shareholder loan"
    "Raised beneficial ownership of trusts")
  (smoking-gun #t)
  (conflicts-of-interest 6)
  (source "1,632 email communications 2015-2026"))

;;; -----------------------------------------------------------------------------
;;; SECTION 4: NEW CONSPIRACY RELATIONS
;;; -----------------------------------------------------------------------------
(define-relation sars-manufacturing-conspiracy
  (from "PERSON_007")
  (to "PERSON_002")
  (type conspiracy-to-defraud-sars)
  (description "Bantjies admits: 'I will manufacture an answer to the 2 interco invoices'")
  (strength conclusive)
  (evidence "EVENT_119")
  (date "2025-06-06")
  (legal-status criminal)
  (evidence-strength 0.99)
  (smoking-gun #t))

(define-relation vat-control-takeover
  (from "PERSON_002")
  (to "PERSON_007")
  (type coordinated-financial-control)
  (description "Farrar removes Anton Hechter, shares eFiling credentials with Bantjies")
  (strength conclusive)
  (evidence ("EVENT_114" "EVENT_115"))
  (date "2022-06-01")
  (legal-status criminal)
  (evidence-strength 0.95))

(define-relation trustee-facilitation
  (from "PERSON_002")
  (to "PERSON_007")
  (type conspiracy-trustee-appointment)
  (description "Farrar provides proof of address for Bantjies' fraudulent trustee appointment")
  (strength conclusive)
  (evidence "EVENT_120")
  (date "2025-08-12")
  (legal-status criminal)
  (evidence-strength 0.99))

(define-relation ketoni-shareholder-loan
  (from "PERSON_007")
  (to "ORG_017")
  (type financial-manipulation)
  (description "Bantjies directs Ketoni payment to Pete's shareholder loan account")
  (strength conclusive)
  (evidence "EVENT_117")
  (date "2023-05-09")
  (amount 18685000)
  (legal-status fraudulent)
  (evidence-strength 0.95))

(define-relation credential-sharing
  (from "PERSON_002")
  (to "PERSON_007")
  (type credential-sharing)
  (description "Farrar shares eFiling credentials via unencrypted email")
  (strength conclusive)
  (evidence "EVENT_115")
  (date "2022-06-23")
  (legal-status criminal)
  (evidence-strength 0.99))

(define-relation ketoni-conflict-of-interest
  (from "PERSON_007")
  (to "ORG_017")
  (type undisclosed-conflict-of-interest)
  (description "Bantjies negotiates Ketoni SHA/MOI as George Group CFO while RegimA accountant")
  (strength conclusive)
  (evidence "EVENT_116")
  (date "2023-04-12")
  (legal-status criminal)
  (evidence-strength 0.99))

;;; -----------------------------------------------------------------------------
;;; SECTION 5: PROVABLE FOREKNOWLEDGE CHAIN
;;; -----------------------------------------------------------------------------
(define-foreknowledge-chain bantjies-farrar-conspiracy
  (chain
    (entry "2020-07" "PERSON_002" "Full access to all company financials" "Email correspondence")
    (entry "2021-08" "PERSON_002" "Intercompany loan account details" "Email to Bantjies")
    (entry "2022-06-01" "PERSON_002" "VAT portal access structure" "EVENT_114")
    (entry "2022-06-23" "PERSON_007" "Full eFiling portal credentials" "EVENT_115")
    (entry "2023-04-12" "PERSON_007" "Ketoni deal terms and structure" "EVENT_116")
    (entry "2023-05-09" "PERSON_002" "Ketoni payment allocation method" "EVENT_117")
    (entry "2024-06-28" "PERSON_002" "Trust amendment execution" "EVENT_103")
    (entry "2024-07-01" "PERSON_007" "Trustee appointment process" "ID document exchange")
    (entry "2024-11-19" "PERSON_007" "Beneficial ownership regulations" "EVENT_118")
    (entry "2025-06-05" "PERSON_002" "SARS verification query" "EVENT_119 thread")
    (entry "2025-06-06" "PERSON_007" "Intent to fabricate SARS response" "EVENT_119 SMOKING GUN")
    (entry "2025-08-12" "PERSON_002" "Trustee appointment timeline" "EVENT_120")))

;;; -----------------------------------------------------------------------------
;;; SECTION 6: BURDEN OF PROOF ASSESSMENT
;;; -----------------------------------------------------------------------------
(define-burden-assessment all-charges-2026-03-07
  (tax-fraud
    (threshold 0.95)
    (current 0.99)
    (status EXCEEDED)
    (primary-evidence "EVENT_119"))
  (common-law-fraud
    (threshold 0.95)
    (current 0.99)
    (status EXCEEDED)
    (primary-evidence ("EVENT_103" "EVENT_119")))
  (forgery
    (threshold 0.95)
    (current 0.99)
    (status EXCEEDED)
    (primary-evidence "EVENT_103"))
  (perjury
    (threshold 0.95)
    (current 0.99)
    (status EXCEEDED)
    (primary-evidence "EVENT_104"))
  (conspiracy
    (threshold 0.95)
    (current 0.99)
    (status EXCEEDED)
    (primary-evidence "1,632 communications"))
  (breach-fiduciary
    (threshold 0.50)
    (current 0.99)
    (status EXCEEDED)
    (primary-evidence "EVENT_116"))
  (popia
    (threshold 0.50)
    (current 0.95)
    (status EXCEEDED)
    (primary-evidence "EVENT_115"))
  (companies-act
    (threshold 0.50)
    (current 0.99)
    (status EXCEEDED)
    (primary-evidence ("EVENT_119" "EVENT_116"))))

;;; =============================================================================
;;; END OF FRAMEWORK V50
;;; =============================================================================
