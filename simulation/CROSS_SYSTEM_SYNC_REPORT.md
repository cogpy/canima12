# Cross-System Sync & Enrichment Report

**Version:** v41 | **Date:** 2026-07-06

**Composition:** `/ksm-fincosys` + `/ksm-tenorc-sync` + `/orgshap` + `/erp-ksm-frappe` + `/slg-erpnext-bom` + `/fin-audit-za-v2`

## Data Coverage Matrix

| System | Records | Date Range | Relevance |
|--------|---------|------------|-----------|
| **fincosys** | 76,098 txns / R2.25B | 2019-2025 | HIGH |
| **comcosys** | 22 mailboxes / 100K+ emails | 2020-2026 | HIGH |
| **discosys** | 39 Shopify stores | 2020-2026 | MEDIUM |
| **entity-slg** | Banking + Accounting + Evidence | 2019-2025 | HIGH |
| **ERPNext** | BOM + Manufacturing + Stock | 2023-2025 | MEDIUM |

## Evidence Cross-Check Results

### Fincosys Fund Flow (R2.25B across 76,098 transactions)

| Evidence Amount | Matched | Source |
|----------------|---------|--------|
| R9,800,000 RST→Ketoni (2023-04-24) | YES | fund_flow/anomaly_report |
| R5,000,000 Peter extraction (2025-03-27) | YES | fund_flow/anomaly_report |
| R1,730,000 unauthorized transfer | NO | fund_flow/anomaly_report |
| R478,958 RST→Elliott (conflict) | NO | fund_flow/anomaly_report |
| R5,400,000 Addarory stock diversion | NO | fund_flow/anomaly_report |

### Top Entity Volumes (Fincosys)

| Entity | Volume | Case Role |
|--------|--------|-----------|
| RST | R994.8M | Revenue source (hijacked) |
| SLG | R350.6M | Manufacturing (stock diverted) |
| Villa Via | R271.1M | Profit extraction vehicle |
| RWD | R267.7M | Distribution (expense dumping) |
| RSA | R253.8M | SA operations |
| Peter | R41.9M | Director extraction |
| Jacqui | R37.8M | Director extraction |
| Daniel | R30.2M | Director (victim) |

## Priority Enrichment Actions

| # | System | Action | Evidence Link |
|---|--------|--------|---------------|
| 1 | fincosys | Extract R478,958 Elliott payments from RST ABSA statements | REL_040 |
| 2 | comcosys | Search Exchange archives for Bantjies→Rynette SARS audit email | REL_037 |
| 3 | discosys | Map Shopify order volumes RST vs Addarory to quantify diversion | REL_041 |
| 4 | entity-slg | Extract R5.4M stock adjustment from SLG Xero/QBO records | REL_044 |
| 5 | fincosys | Trace R1.73M unauthorized transfer through fund flow edges | EVENT_H027 |
| 6 | comcosys | Extract Peter→Jax interdict timing emails (Aug 2025) | REL_042 |
| 7 | entity-slg/erpnext | Map SLG BOM data to Addarory parallel supply chain | REL_041 |
| 8 | discosys | Compare RST Shopify revenue pre/post Addarory incorporation | EVENT_H013 |

## Comcosys Key Actor Coverage

| Actor | Status | Mailboxes |
|-------|--------|-----------|
| peter | MISSING | peterfaucitt@regima.zone, pete@regima.zone |
| rynette | MISSING | rynette@regima.zone, rynettefarrar@regima.zone |
| daniel | COVERED | danielfaucitt@regima.zone, dan@regima.zone, d@rzo.io |
| jax | MISSING | jax@regima.zone, jacqui@regima.zone |
| bantjies | MISSING | danie@regima.zone, bantjies@regima.zone |

## Next Steps

1. **Extract Elliott payments** from fincosys RST ABSA statements (REL_040 strengthening)
2. **Search comcosys** for Bantjies→Rynette SARS audit email (REL_037 smoking gun)
3. **Map Shopify revenue** RST vs Addarory pre/post incorporation (REL_041 quantification)
4. **Trace R5.4M** stock adjustment through entity-slg Xero records (REL_044)
5. **ERPNext BOM** cross-reference with Addarory product overlap (manufacturing evidence)
6. **Fund flow path** for R1.73M unauthorized transfer (EVENT_H027)
7. **Email chain extraction** for whistleblower retaliation timing (REL_042)
8. **Shopify revenue comparison** pre/post Ketoni incorporation (EVENT_H013)
