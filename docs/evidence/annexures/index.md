# Forensic Email Annexures: Intercompany Transactions & Stock Adjustments

This directory contains cryptographically verifiable forensic email renderings extracted directly from the Microsoft 365 Exchange Online tenant via the Microsoft Graph API.

Each PDF annexure includes:
1. **Email Content**: Rendered in standard Outlook format.
2. **Forensic Metadata Page**: Includes SPF/DKIM/DMARC authentication results, transport routing hops, Exchange transport metadata, and EML file integrity hashes.

## Annexure Index

| Annexure | Date | From | Subject / Description | Filing References |
|----------|------|------|-----------------------|-------------------|
| **[Annexure A](ANNEXURE_A_2025-06-05_SARS_query_re_the_two_big_inter_company.pdf)** | 5 Jun 2025 | Rynette Farrar | Initial SARS query about two big intercompany invoices | SARS [1][2], SAICA [4], CIPC [4], NPA [3] |
| **[Annexure B](ANNEXURE_B_2025-06-06_RE__SARS_query_re_the_two_big_inter_comp.pdf)** | 6 Jun 2025 | Rynette Farrar | "Done on your request, for which I have no answer" | SARS [1], SAICA [4], NPA [3] |
| **[Annexure C](ANNEXURE_C_2025-06-08_Re__SARS_query_re_the_two_big_inter_comp.pdf)** | 8 Jun 2025 | Danie Bantjes | Bantjes drafts SARS response | SARS [3], SAICA [5] |
| **[Annexure D](ANNEXURE_D_2025-04-04_TB_s_after_stock_adjustments_-_February.pdf)** | 4 Apr 2025 | Rynette Farrar | R4.2M stock discrepancy — "Bernadine gogga" | SARS [4], SAICA [2], CIPC [2], NPA [1] |
| **[Annexure E](ANNEXURE_E_2025-04-07_Re__TB_s_after_stock_adjustments_-_Febru.pdf)** | 7 Apr 2025 | Danie Bantjes | Bantjes admits "huge gaps building up over many years" | SARS [5], SAICA [1], CIPC [3], NPA [2] |
| **[Annexure F1](ANNEXURE_F1_2021-08-17_Intercompany_loan_accounts.pdf)** | 17 Aug 2021 | Rynette Farrar | Rynette directs Bantjes — Intercompany loan accounts | SARS [6], SAICA [3], CIPC [1], NPA [4] |
| **[Annexure F2](ANNEXURE_F2_2021-08-17_Loan_account_between_Strategic_and_Regim.pdf)** | 17 Aug 2021 | Rynette Farrar | Loan account between Strategic and RWD | SARS [6], SAICA [3], CIPC [1], NPA [4] |
| **[Annexure G](ANNEXURE_G_2020-09-28_Intercompany_transfers_-_End_September_2.pdf)** | 28 Sep 2020 | Rynette Farrar | Intercompany transfers End September 2020 (R1.5M transfer) | NPA [Peter involvement] |
| **[Annexure H](ANNEXURE_H_2025-06-09_Re__SARS_query_re_the_two_big_inter_comp.pdf)** | 9 Jun 2025 | Danie Bantjes | Bantjes SARS response with revised draft | SARS [3], SAICA [5] |
| **[Annexure I](ANNEXURE_I_2025-06-30_RE__SARS_query_re_the_two_big_inter_comp.pdf)** | 30 Jun 2025 | Rynette Farrar | Rynette confirms SARS documentation uploaded | SARS [supporting] |

## Chain of Custody

All emails in this annexure package were extracted using the following pipeline:
1. **Source**: Microsoft 365 Exchange Online (Tenant: `89727f2e-27c2-4f69-893c-f30d821bc83d`)
2. **Extraction**: Microsoft Graph API v1.0 (client credentials flow)
3. **Storage**: Neon PostgreSQL (`exchange_sync` schema)
4. **Verification**: SPF/DKIM/DMARC authentication via internet message headers
5. **Integrity**: SHA-256 hash of generated EML file

*Generated 2026-03-15 — Forensic Annexure Pipeline v1.0*
