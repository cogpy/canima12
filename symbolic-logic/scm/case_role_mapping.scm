;; ══════════════════════════════════════════════════════════════════════
;; CASE ROLE MAPPING — Case 2025-137857 → Symbolic Roles
;; ══════════════════════════════════════════════════════════════════════
;; Maps concrete entities to parameterized role symbols.
;; This file is the ONLY place where concrete names appear.
;; All other files use role symbols exclusively.
;; ══════════════════════════════════════════════════════════════════════

;; ── §1. Applicant Set A[1] ──────────────────────────────────────────
;; In the ex parte application, there is one applicant.
(define A
  (make-role-set 'applicant 1
    '((1 . "Peter Andrew Faucitt"))))

;; a_1 = Peter Andrew Faucitt (primary perpetrator / applicant)
(define a_1 (list 'role 'applicant 1 "Peter Andrew Faucitt" "PERSON_001"))

;; ── §2. Respondent Set R[2] ────────────────────────────────────────
;; Two respondents in the ex parte application.
(define R
  (make-role-set 'respondent 2
    '((1 . "Jacqueline Faucitt")
      (2 . "Daniel James Faucitt"))))

;; r_1 = Jacqueline Faucitt (first respondent / victim)
(define r_1 (list 'role 'respondent 1 "Jacqueline Faucitt" "PERSON_003"))
;; r_2 = Daniel James Faucitt (second respondent / victim)
(define r_2 (list 'role 'respondent 2 "Daniel James Faucitt" "PERSON_004"))

;; ── §3. Co-Conspirator Set C[3] ────────────────────────────────────
;; Three identified co-conspirators.
(define C
  (make-role-set 'co-conspirator 3
    '((1 . "Rynette Farrar")
      (2 . "Daniel Jacobus Bantjies")
      (3 . "Darren Farrar"))))

;; c_1 = Rynette Farrar (co-conspirator, financial manipulation)
(define c_1 (list 'role 'co-conspirator 1 "Rynette Farrar" "PERSON_002"))
;; c_2 = Daniel Jacobus Bantjies (co-conspirator, accountant, dual-role)
(define c_2 (list 'role 'co-conspirator 2 "Daniel Jacobus Bantjies" "PERSON_007"))
;; c_3 = Darren Farrar (accomplice, family)
(define c_3 (list 'role 'co-conspirator 3 "Darren Farrar" "PERSON_009"))

;; ── §4. Witness Set W[3] ───────────────────────────────────────────
(define W
  (make-role-set 'witness 3
    '((1 . "Oliver Mphande")
      (2 . "Nick Xenophontos")
      (3 . "Marisca Meyer"))))

(define w_1 (list 'role 'witness 1 "Oliver Mphande" "PERSON_011"))
(define w_2 (list 'role 'witness 2 "Nick Xenophontos" "PERSON_045"))
(define w_3 (list 'role 'witness 3 "Marisca Meyer" "PERSON_010"))

;; ── §5. Professional Set (Attorneys, Consultants) ───────────────────
(define professionals
  (make-role-set 'professional 2
    '((1 . "Marc Yudaken")
      (2 . "David Field"))))

;; ── §6. Entity Set E[11] ───────────────────────────────────────────
;; Organizations involved in the case.
(define E
  (make-role-set 'entity 11
    '((1  . "Regima Worldwide Distribution (Pty) Ltd")
      (2  . "RegimA Skin Treatments CC")
      (3  . "Strategic Logistics CC")
      (4  . "Villa Via Arcadia No 2 CC")
      (5  . "Ketoni Investment Holdings (Pty) Ltd")
      (6  . "Adderory (Pty) Ltd")
      (7  . "ReZonance (Pty) Ltd")
      (8  . "RegimaSA (Pty) Ltd")
      (9  . "De Novo Business Services (Pty) Ltd")
      (10 . "The George Group")
      (11 . "Baker McKenzie"))))

;; Key entity aliases
(define e_1  (list 'role 'entity 1  "Regima Worldwide Distribution (Pty) Ltd" "ORG_001"))
(define e_2  (list 'role 'entity 2  "RegimA Skin Treatments CC" "ORG_002"))
(define e_5  (list 'role 'entity 5  "Ketoni Investment Holdings (Pty) Ltd" "ORG_005"))
(define e_6  (list 'role 'entity 6  "Adderory (Pty) Ltd" "ORG_006"))
(define e_7  (list 'role 'entity 7  "ReZonance (Pty) Ltd" "ORG_007"))
(define e_8  (list 'role 'entity 8  "RegimaSA (Pty) Ltd" "ORG_008"))
(define e_9  (list 'role 'entity 9  "De Novo Business Services (Pty) Ltd" "ORG_009"))
(define e_10 (list 'role 'entity 10 "The George Group" "ORG_010"))

;; ── §7. Trust Set T[1] ─────────────────────────────────────────────
(define T
  (make-role-set 'trust 1
    '((1 . "Faucitt Family Trust"))))

(define t_1 (list 'role 'trust 1 "Faucitt Family Trust" "TRUST_001"))

;; ── §8. System/Platform Set S[3] ───────────────────────────────────
(define S
  (make-role-set 'system 3
    '((1 . "Sage Business Cloud")
      (2 . "SARS eFiling")
      (3 . "FNB Business Banking"))))

(define s_1 (list 'role 'system 1 "Sage Business Cloud" "PLAT_001"))
(define s_2 (list 'role 'system 2 "SARS eFiling" "PLAT_002"))
(define s_3 (list 'role 'system 3 "FNB Business Banking" "PLAT_003"))

;; ══════════════════════════════════════════════════════════════════════
;; §9. RELATION MAPPING (Concrete → Symbolic)
;; ══════════════════════════════════════════════════════════════════════

;; Conspiracy relations
(define rel-conspiracy-a1-c1
  (list 'relation 'conspiracy a_1 c_1
    '(nature "primary_conspiracy")
    '(evidence "100+ emails")))

(define rel-conspiracy-c1-c2
  (list 'relation 'conspiracy c_1 c_2
    '(nature "financial_manipulation")
    '(evidence "1632 communications 2015-2026")))

(define rel-conspiracy-a1-c2
  (list 'relation 'conspiracy a_1 c_2
    '(nature "trust_forgery_perjury")))

;; Conflict of interest
(define rel-conflict-c2-e5
  (list 'relation 'conflict-of-interest c_2 e_5
    '(nature "CFO_employer_AND_trust_trustee")
    '(dual-role #t)))

;; Victim relations
(define rel-victim-r2-a1
  (list 'relation 'victim-of r_2 a_1))

(define rel-victim-r1-a1
  (list 'relation 'victim-of r_1 a_1))

;; Sole mandate
(define rel-mandate-r2-s3
  (list 'relation 'sole-mandate r_2 s_3
    '(evidence "FNB FICA/KYC letter 18 June 2025")))

;; Family company
(define rel-family-c1-e6
  (list 'relation 'family-company c_1 e_6))

;; Fabricated records
(define rel-fabricated-e9-e8
  (list 'relation 'fabricated-records e_9 e_8))

;; Director/Trustee
(define rel-trustee-c2-t1
  (list 'relation 'trustee-of c_2 t_1))

;; Co-directors
(define rel-codir-r2-e1
  (list 'relation 'co-director r_2 e_1))

(define rel-codir-a1-e1
  (list 'relation 'co-director a_1 e_1))

;; Employment
(define rel-employed-c2-e10
  (list 'relation 'employed-by c_2 e_10))
