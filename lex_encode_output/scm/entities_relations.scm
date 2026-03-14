;; ── Entity-Relation Encoding ─────────────────────────────────────
;; Generated: 2026-03-14T16:26:39.816621
;; Entities: 8
;; Relations: 4
;; ────────────────────────────────────────────────────────────────

;; ── Entities ──────────────────────────────────────────────────────
(define entity-peter-andrew-faucitt (make-person-entity (name "Peter Andrew Faucitt") (role applicant) (id "PERSON_001")))
(define entity-rynette-farrar (make-person-entity (name "Rynette Farrar") (role co_conspirator) (id "PERSON_002")))
(define entity-danie-bantjies (make-person-entity (name "Danie Bantjies") (role accountant_and_unknown_trustee) (id "PERSON_006")))
(define entity-daniel-james-faucitt (make-person-entity (name "Daniel James Faucitt") (role respondent) (id "PERSON_004")))
(define entity-jacqueline-faucitt (make-person-entity (name "Jacqueline Faucitt") (role respondent) (id "PERSON_003")))
(define entity-regima-worldwide-distribution-(pty)-ltd (make-organization-entity (name "Regima Worldwide Distribution (PTY) LTD") (role company) (id "ORG_001")))
(define entity-faucitt-family-trust (make-trust-entity (name "Faucitt Family Trust") (role trust) (id "TRUST_001")))
(define entity-ketoni-investment-holdings (make-organization-entity (name "Ketoni Investment Holdings") (role debtor) (id "ORG_002")))

;; ── Relations ─────────────────────────────────────────────────────
(define rel-peter-andrew-faucitt-daniel-james-faucitt (make-opposed-to-relation (source entity-peter-andrew-faucitt) (target entity-daniel-james-faucitt) ))
(define rel-peter-andrew-faucitt-rynette-farrar (make-co_conspirator-relation (source entity-peter-andrew-faucitt) (target entity-rynette-farrar) ))
(define rel-rynette-farrar-danie-bantjies (make-co_conspirator-relation (source entity-rynette-farrar) (target entity-danie-bantjies) ))
(define rel-ketoni-investment-holdings-faucitt-family-trust (make-owes-debt-relation (source entity-ketoni-investment-holdings) (target entity-faucitt-family-trust) ))
