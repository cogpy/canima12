# Ketoni Standard Bank Account (BANK_ACCOUNT_005)

**Type:** Bank Account
**Last Updated:** 2026-03-15

## Account Details

```json
{
  "entity_id": "BANK_ACCOUNT_005",
  "account_number": "420469494",
  "bank": "Standard Bank",
  "branch": "Eastgate",
  "holder": "Ketoni Investment Holdings (Pty) Ltd",
  "holder_entity": "ORG_017",
  "type": "business_account",
  "balance_at_29_feb_2024": 48727,
  "significance": "Destination for R9.8M subscription payment from FFT. Source for fund flow tracing to George Group investment.",
  "evidence": [
    "Ketoni_subscription_agreement_signed_2.txt (clause 2.1.6)",
    "Ketoni_AFS_2024.txt (Note 3)"
  ],
  "fund_flows": [
    {
      "direction": "inbound",
      "amount": 9800000,
      "source": "TRUST_001 (FFT)",
      "description": "Subscription price for 5,000 A Ordinary Shares",
      "date": "~April 2023"
    },
    {
      "direction": "inbound",
      "amount": 49000,
      "source": "Kevin Derrick Trust (IT107716/98)",
      "description": "Unsecured interest-free loan",
      "date": "~2023"
    },
    {
      "direction": "outbound",
      "amount": 9800000,
      "destination": "ORG_018 (The George Group)",
      "description": "Investment in 456 shares (8.14%)",
      "date": "~2023"
    }
  ]
}
```

## Fund Flow Summary

The Ketoni Standard Bank account received R9,800,000 from the Faucitt Family Trust as subscription payment for 5,000 A Ordinary Shares, plus R49,000 as an unsecured loan from the Kevin Derrick Trust. The R9,800,000 was then invested in 456 shares (8.14%) of The George Group Proprietary Limited. As at 29 February 2024, the account held a balance of R48,727, with the R9,800,000 classified as a non-current financial asset (the George Group investment).

---

*Added: 2026-03-15 — Super-Sleuth Evidence Batch*
