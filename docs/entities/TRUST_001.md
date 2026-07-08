# Faucitt Family Trust (TRUST_001)

**Type:** Trust  
**Role:** family_trust_structure_manipulated
**Last Updated:** 2026-03-15 (v15)

## Summary

The Faucitt Family Trust (IT 3651/2013) is the central asset-holding structure in Case 2025-137857. It holds 5,000 A Ordinary Shares in Ketoni Investment Holdings (ORG_017), with a guaranteed Put Option value of **R28,730,000** at Year 5 (April 2028). The trust has been captured through the fraudulent installation of Daniel Bantjies (PERSON_007) as a trustee, who declared himself "Independent" on the J417 form despite being employed as CFO of The George Group — the very company in which Ketoni holds its sole investment.

```json
{
  "entity_id": "TRUST_001",
  "name": "Faucitt Family Trust",
  "trust_number": "IT 3651/2013",
  "entity_type": "family_business_trust",
  "agent_type": "victim_entity",
  "role": "family_trust_structure_manipulated",
  "trustees": [
    "PERSON_001 (Peter Andrew Faucitt)",
    "PERSON_012 (Jacqueline Faucitt — Neutralized via Interdict)",
    "PERSON_007 (Daniel Jacobus Bantjies — FALSE INDEPENDENT)"
  ],
  "beneficiaries": [
    "PERSON_001 (Peter Andrew Faucitt)",
    "PERSON_004 (Jacqueline Faucitt)",
    "PERSON_005 (Daniel James Faucitt)"
  ],
  "founder": "PERSON_001",
  "owned_entities": [
    "ORG_001 (Regima Worldwide Distribution)",
    "ORG_004 (Strategic Logistics Group)"
  ],
  "financial_assets": [
    {
      "asset": "5,000 A Ordinary Shares in Ketoni Investment Holdings",
      "subscription_price": "ZAR 9,800,000",
      "subscription_date": "24 April 2023",
      "call_option_year_3": "ZAR 18,685,000 (R3,737/share)",
      "call_option_year_4": "ZAR 23,165,000 (R4,633/share)",
      "put_option_year_5": "ZAR 28,730,000 (R5,746/share) — GUARANTEED",
      "irr_minimum": "24% per annum",
      "dividend_sweep": "90% of ALL distributions for 5 years + 2 months",
      "significance": "Central financial motive for all trust actions since Apr 2023"
    }
  ],
  "key_characteristics": [
    "family_business_trust_requiring_independent_trustee",
    "independent_trustee_is_NOT_independent",
    "beneficiary_daniel_excluded_from_R9.8M_investment_decision",
    "used_for_attacking_beneficiaries"
  ],
  "legal_significance": "trust_structure_manipulation_and_beneficiary_attack",
  "evidence": [
    "Ketoni_Shareholder_Agreement_signed.txt",
    "Ketoni_subscription_agreement_signed_2.txt",
    "Ketoni_AFS_2024.txt",
    "Ketoni_Investment_Holdings_AFS_2024_-_Signed.txt",
    "FAUCITT_TRUST.txt (J417 + J401)",
    "F172-Peter_faucitt_family_trust.txt (J417 + J401)",
    "moh-SwornAffTrustee.txt",
    "Signed_minutes.txt",
    "Danie_-_missing_pages20250129.txt"
  ],
  "evidence_enhanced": "2026-03-15",
  "evidence_strength": "conclusive"
}
```

## Corrected Financial Architecture (v15)

| Period | Mechanism | Amount | Per Share | Status |
|--------|-----------|--------|-----------|--------|
| Year 3 (April 2026) | Call Option | R18,685,000 | R3,737 | Opening |
| Year 4 (April 2027) | Call Option | R23,165,000 | R4,633 | Mid-range |
| **Year 5 (April 2028)** | **Put Option (GUARANTEED)** | **R28,730,000** | **R5,746** | **Maximum** |

The 90% Dividend Sweep entitles FFT to receive 90% of ALL distributions from Ketoni for 5 years and 2 months from the Subscription Date. The 24% IRR minimum guarantee means the actual value could be even higher if FNB prime + 10% exceeds 24%.

## Evidence Cross-References

- **[PERSON_007](./PERSON_007.md)** — Daniel Bantjies (False Independent Trustee)
- **[ORG_017](./ORG_017.md)** — Ketoni Investment Holdings (Debtor)
- **[ORG_018](./ORG_018.md)** — The George Group (Bantjies' Employer)
- **[BANK_ACCOUNT_005](./BANK_ACCOUNT_005.md)** — Ketoni Standard Bank 420469494
- **[Ketoni Fund Flow Complete](../relations/KETONI_FUND_FLOW_COMPLETE.md)** — Full fund flow architecture
- **[Bantjies False Independence](../relations/BANTJIES_FALSE_INDEPENDENCE.md)** — J417 perjury analysis
- **[Super-Sleuth Report 2026-03-15](../super_sleuth_report_2026_03_15.md)** — Latest analysis

---

*Last updated: 2026-03-15 (v15) — Primary source documents integrated*
