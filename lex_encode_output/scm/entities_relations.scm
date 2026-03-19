;; ── Entity-Relation Encoding v16 ────────────────────────────────────
;; Generated: 2026-03-18T06:21:08
;; Case: 2025-137857 — Revenue Stream Hijacking, Trust Fraud, Corporate Sabotage
;; Pipeline: skillm ( lex-sim-nn [ lex-rex | lexrex ] -> lex-encode-workflow )
;; Entities: 29 | Relations: 14
;; ────────────────────────────────────────────────────────────────

;; ── Persons ─────────────────────────────────────────────────────
(define entity-peter-andrew-faucitt
  (make-person-entity
    (name "Peter Andrew Faucitt")
    (role "primary_perpetrator")
    (id "PERSON_001")
    (criminal-threshold "95%_exceeded")
    (financial-impact "R10,269,727.90")
    
    
  ))
(define entity-rynette-farrar
  (make-person-entity
    (name "Rynette Farrar")
    (role "co_conspirator")
    (id "PERSON_002")
    (criminal-threshold "95%_likely")
    (financial-impact "R4,276,832.85")
    
    
  ))
(define entity-daniel-jacobus-bantjies
  (make-person-entity
    (name "Daniel Jacobus Bantjies")
    (role "co_conspirator_accountant")
    (id "PERSON_007")
    (criminal-threshold "95%_likely")
    
    (dual-role "CFO_George_Group_AND_FFT_Trustee")
    (saica "00105928")
  ))
(define entity-jacqueline-faucitt
  (make-person-entity
    (name "Jacqueline Faucitt")
    (role "first_respondent_victim")
    (id "PERSON_003")
    
    
    
    
  ))
(define entity-daniel-james-faucitt
  (make-person-entity
    (name "Daniel James Faucitt")
    (role "second_respondent_victim")
    (id "PERSON_004")
    
    
    
    
  ))
(define entity-linda-kruger
  (make-person-entity
    (name "Linda Kruger")
    (role "employee_bookkeeper")
    (id "PERSON_005")
    
    
    
    
  ))
(define entity-gayane-williams
  (make-person-entity
    (name "Gayane Williams")
    (role "employee")
    (id "PERSON_006")
    
    
    
    
  ))
(define entity-kevin-michael-derrick
  (make-person-entity
    (name "Kevin Michael Derrick")
    (role "ketoni_director")
    (id "PERSON_008")
    
    
    
    
  ))
(define entity-darren-farrar
  (make-person-entity
    (name "Darren Farrar")
    (role "accomplice_family")
    (id "PERSON_009")
    
    
    
    
  ))
(define entity-marc-yudaken
  (make-person-entity
    (name "Marc Yudaken")
    (role "attorney_baker_mckenzie")
    (id "PERSON_042")
    
    
    
    
  ))
(define entity-david-field
  (make-person-entity
    (name "David Field")
    (role "deal_consultant")
    (id "PERSON_043")
    
    
    
    
  ))
(define entity-marisca-meyer
  (make-person-entity
    (name "Marisca Meyer")
    (role "professional_accountant")
    (id "PERSON_010")
    
    
    
    
  ))
(define entity-oliver-mphande
  (make-person-entity
    (name "Oliver Mphande")
    (role "witness")
    (id "PERSON_011")
    
    
    
    
  ))
(define entity-nick-xenophontos
  (make-person-entity
    (name "Nick Xenophontos")
    (role "independent_attorney_witness")
    (id "PERSON_045")
    
    
    
    
  ))

;; ── Organizations ────────────────────────────────────────────────
(define entity-regima-worldwide-distribution-pty-ltd
  (make-organization-entity
    (name "Regima Worldwide Distribution (Pty) Ltd")
    (role "primary_company")
    (id "ORG_001")
    (reg "2011/005722/07")
    
  ))
(define entity-regima-skin-treatments-cc
  (make-organization-entity
    (name "RegimA Skin Treatments CC")
    (role "close_corporation")
    (id "ORG_002")
    (reg "1992/005371/23")
    
  ))
(define entity-strategic-logistics-cc
  (make-organization-entity
    (name "Strategic Logistics CC")
    (role "logistics_entity")
    (id "ORG_003")
    (reg "2008/136496/23")
    
  ))
(define entity-villa-via-arcadia-no-2-cc
  (make-organization-entity
    (name "Villa Via Arcadia No 2 CC")
    (role "property_entity")
    (id "ORG_004")
    (reg "1996/004451/23")
    
  ))
(define entity-ketoni-investment-holdings-pty-ltd
  (make-organization-entity
    (name "Ketoni Investment Holdings (Pty) Ltd")
    (role "central_financial_motive")
    (id "ORG_005")
    
    (put-option "R28,730,000")
  ))
(define entity-adderory-pty-ltd
  (make-organization-entity
    (name "Adderory (Pty) Ltd")
    (role "family_company_farrar")
    (id "ORG_006")
    
    
  ))
(define entity-rezonance-pty-ltd
  (make-organization-entity
    (name "ReZonance (Pty) Ltd")
    (role "debt_fabrication_vehicle")
    (id "ORG_007")
    
    
  ))
(define entity-regimasa-pty-ltd
  (make-organization-entity
    (name "RegimaSA (Pty) Ltd")
    (role "shell_company")
    (id "ORG_008")
    (reg "2017/087935/07")
    
  ))
(define entity-de-novo-business-services-pty-ltd
  (make-organization-entity
    (name "De Novo Business Services (Pty) Ltd")
    (role "fabricated_records_provider")
    (id "ORG_009")
    
    
  ))
(define entity-the-george-group
  (make-organization-entity
    (name "The George Group")
    (role "bantjies_employer")
    (id "ORG_010")
    
    
  ))
(define entity-baker-mckenzie
  (make-organization-entity
    (name "Baker McKenzie")
    (role "ketoni_attorneys")
    (id "ORG_025")
    
    
  ))

;; ── Trusts & Platforms ────────────────────────────────────────────
(define entity-faucitt-family-trust
  (make-trust-entity
    (name "Faucitt Family Trust")
    (role "trust_victim")
    (id "TRUST_001")
  ))
(define entity-sage-business-cloud
  (make-platform-entity
    (name "Sage Business Cloud")
    (role "captured_accounting_system")
    (id "PLAT_001")
  ))
(define entity-sars-efiling
  (make-platform-entity
    (name "SARS eFiling")
    (role "impersonated_tax_platform")
    (id "PLAT_002")
  ))
(define entity-fnb-business-banking
  (make-platform-entity
    (name "FNB Business Banking")
    (role "banking_mandate_fraud_target")
    (id "PLAT_003")
  ))

;; ── Relations ────────────────────────────────────────────────────
(define rel-000-conspiracy
  (make-conspiracy-relation
    (source entity-peter-andrew-faucitt)
    (target entity-rynette-farrar)
    (nature "primary_conspiracy")
    (evidence "100+ emails")
  ))
(define rel-001-conspiracy
  (make-conspiracy-relation
    (source entity-rynette-farrar)
    (target entity-daniel-jacobus-bantjies)
    (nature "financial_manipulation")
    (evidence "1632 communications 2015-2026")
  ))
(define rel-002-conspiracy
  (make-conspiracy-relation
    (source entity-peter-andrew-faucitt)
    (target entity-daniel-jacobus-bantjies)
    (nature "trust_forgery_perjury")
    
  ))
(define rel-003-conflict_of_interest
  (make-conflict_of_interest-relation
    (source entity-daniel-jacobus-bantjies)
    (target entity-ketoni-investment-holdings-(pty)-ltd)
    (nature "CFO_George_Group_AND_FFT_Trustee")
    
  ))
(define rel-004-victim_of
  (make-victim_of-relation
    (source entity-daniel-james-faucitt)
    (target entity-peter-andrew-faucitt)
    
    
  ))
(define rel-005-victim_of
  (make-victim_of-relation
    (source entity-jacqueline-faucitt)
    (target entity-peter-andrew-faucitt)
    
    
  ))
(define rel-006-sole_mandate
  (make-sole_mandate-relation
    (source entity-daniel-james-faucitt)
    (target entity-fnb-business-banking)
    
    (evidence "FNB FICA/KYC letter 18 June 2025")
  ))
(define rel-007-family_company
  (make-family_company-relation
    (source entity-rynette-farrar)
    (target entity-adderory-(pty)-ltd)
    
    
  ))
(define rel-008-fabricated_records
  (make-fabricated_records-relation
    (source entity-de-novo-business-services-(pty)-ltd)
    (target entity-regimasa-(pty)-ltd)
    
    
  ))
(define rel-009-director_of
  (make-director_of-relation
    (source entity-kevin-michael-derrick)
    (target entity-ketoni-investment-holdings-(pty)-ltd)
    
    
  ))
(define rel-010-trustee_of
  (make-trustee_of-relation
    (source entity-daniel-jacobus-bantjies)
    (target entity-faucitt-family-trust)
    
    
  ))
(define rel-011-co_director
  (make-co_director-relation
    (source entity-daniel-james-faucitt)
    (target entity-regima-worldwide-distribution-(pty)-ltd)
    
    
  ))
(define rel-012-co_director
  (make-co_director-relation
    (source entity-peter-andrew-faucitt)
    (target entity-regima-worldwide-distribution-(pty)-ltd)
    
    
  ))
(define rel-013-employed_by
  (make-employed_by-relation
    (source entity-daniel-jacobus-bantjies)
    (target entity-the-george-group)
    
    
  ))
