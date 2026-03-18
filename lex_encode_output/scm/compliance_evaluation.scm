;; ── Compliance Evaluation v16 ─────────────────────────────────────
;; Generated: 2026-03-18T06:21:08
;; Pipeline: skillm ( lex-sim-nn [ lex-rex | lexrex ] -> lex-encode-workflow )
;; ────────────────────────────────────────────────────────────────

(define compliance-evaluation
  (evaluation
    (ex-parte-disclosure
      (required "full-and-frank-disclosure-of-all-material-facts")
      (actual "12-plus-material-non-disclosures")
      (result "VIOLATED")
      (consequence "order-void-ab-initio"))
    (confirmatory-affidavit
      (required "truthful-confirmation-of-founding-affidavit")
      (actual "false-confirmation-with-68-day-foreknowledge-of-fraud")
      (result "VIOLATED — PERJURY")
      (consequence "criminal-prosecution-s162-CPA"))
    (urgency-requirement
      (required "genuine-urgency-with-no-alternative-remedy")
      (actual "manufactured-urgency-applicant-controlled-all-infrastructure")
      (result "VIOLATED")
      (consequence "costs-de-bonis-propriis"))
    (irregular-proceedings
      (required "compliance-with-all-procedural-rules")
      (actual "order-obtained-through-fraud-on-the-court")
      (result "VOID-AB-INITIO")
      (consequence "fraus-omnia-corrumpit"))
    (contempt-defense
      (required "valid-order-plus-knowledge-plus-wilful-contravention")
      (actual "void-order-cannot-found-contempt")
      (result "DEFENSE-ESTABLISHED")
      (consequence "contempt-application-dismissed-with-costs"))
  ))
