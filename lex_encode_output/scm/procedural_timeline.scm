;; ── Procedural Compliance Evaluation v16 ──────────────────────────
;; Generated: 2026-03-18T06:21:08
;; Pipeline: skillm ( lex-sim-nn [ lex-rex | lexrex ] -> lex-encode-workflow )
;; Rules evaluated: 8
;; Violations found: 6
;; ────────────────────────────────────────────────────────────────

(define rule-6-4
  (procedural-evaluation
    (rule "6(4)")
    (description "Ex parte disclosure duty")
    (violated #t)
    (severity "critical")
    (evidence "12+ material non-disclosures in founding affidavit")))

(define rule-6-5-a
  (procedural-evaluation
    (rule "6(5)(a)")
    (description "Confirmatory affidavit requirements")
    (violated #t)
    (severity "critical")
    (evidence "Bantjies swore false confirmatory affidavit with provable foreknowledge")))

(define rule-6-12-a
  (procedural-evaluation
    (rule "6(12)(a)")
    (description "Urgent application requirements")
    (violated #t)
    (severity "high")
    (evidence "Urgency manufactured — fraud reports received weeks before application")))

(define rule-6-12-b
  (procedural-evaluation
    (rule "6(12)(b)")
    (description "Urgency justification")
    (violated #t)
    (severity "high")
    (evidence "No genuine urgency — applicant controlled all banking and infrastructure")))

(define rule-7-1
  (procedural-evaluation
    (rule "7(1)")
    (description "Power of attorney requirements")
    (violated ##f)
    (severity "medium")
    (evidence "Applicant's attorneys properly authorized")))

(define rule-30-1
  (procedural-evaluation
    (rule "30(1)")
    (description "Irregular proceedings")
    (violated #t)
    (severity "critical")
    (evidence "Ex parte order obtained through fraud — void ab initio")))

(define rule-42-1-a
  (procedural-evaluation
    (rule "42(1)(a)")
    (description "Rescission of erroneously granted order")
    (violated #t)
    (severity "critical")
    (evidence "Order erroneously granted due to material non-disclosure and perjury")))

(define rule-45A
  (procedural-evaluation
    (rule "45A")
    (description "Contempt of court")
    (violated ##f)
    (severity "defense")
    (evidence "Contempt application is abuse of process — underlying order is void")))

;; ── Procedural Timeline ─────────────────────────────────────────
(define procedural-timeline
  (timeline
    (event (date "2025-06-06") (description "Fraud report delivered to Bantjies") (rule "none") (significance "establishes-foreknowledge"))
    (event (date "2025-06-07") (description "Cards cancelled in retaliation") (rule "none") (significance "proves-mala-fide"))
    (event (date "2025-06-18") (description "FNB confirms sole mandate") (rule "none") (significance "destroys-founding-affidavit"))
    (event (date "2025-08-13") (description "Bantjies swears false confirmatory affidavit") (rule "6(5)(a)") (significance "perjury"))
    (event (date "2025-08-19") (description "Ex parte interdict granted") (rule "6(12)(a)") (significance "void-ab-initio"))
    (event (date "2025-09-01") (description "Respondents served") (rule "6(4)") (significance "first-knowledge-of-order"))
    (event (date "2026-01-24") (description "Xenophontos flags missing SHA pages") (rule "none") (significance "independent-witness"))
  ))
