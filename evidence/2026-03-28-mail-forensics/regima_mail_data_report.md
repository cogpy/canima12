# RegimA Mail Data Assessment Report (Neon DB)

**Date:** March 28, 2026
**Target Domains:** `regima.zone` (MS Exchange) and `regima.com` (Google Workspace)

This report details the findings from a comprehensive scan of the Neon PostgreSQL databases to locate and assess the synchronization status of mail data for the RegimA domains.

## Executive Summary

The mail data for RegimA is primarily housed in a dedicated Neon project named **`b2bkp-exchange-sync`**. This database contains a massive, highly-complete archive of both Exchange (`regima.zone`) and Gmail (`regima.com`) communications, totaling over **2.5 million messages**. 

A smaller subset of this data also exists in the default `neondb` project under the `rzo.io` tenant, but the `b2bkp-exchange-sync` project serves as the definitive historical archive.

---

## 1. MS Exchange Data (`regima.zone`)

The Exchange data is stored in the `exchange_sync` schema of the `b2bkp-exchange-sync` database.

### Mailbox Users
- **Total Users:** 149 distinct mailbox users associated with `@regima.zone`.
- **Key Accounts Identified:**
  - `dan@regima.zone` (Daniel Faucitt)
  - `jax@regima.zone` (Jacqui Faucitt)
  - `rynette@regima.zone` (Rynette Farrar)
  - `kayla@regima.zone` (Kayla Pretorius)
  - `pete@regima.zone` (Peter Faucitt)
  - Various departmental accounts (e.g., `info@`, `finadmin@`, `opsman@`) and regional accounts (UK, SA, Australia).

### Message Statistics
| Metric | Count | Coverage |
|--------|-------|----------|
| **Total Messages** | 1,059,437 | 100.0% |
| **With Body Preview** | 1,052,547 | 99.3% |
| **With Full Body Content** | 891,270 | 84.1% |
| **With Attachments** | 227,188 | 21.4% |
| **Synced to R2 Search** | 1,053,726 | 99.5% |

**Date Range:** December 7, 2014 – March 28, 2026

### Attachment Sync Status
- **Total Tracked Attachments:** 35,927
- **Successfully Downloaded:** 27,942 (77.8%)
- **Pending Download:** 7,808 (21.7%)
- **Failed/Skipped:** 159 (0.4%)

*Note: The Exchange archive is highly complete, with 84% of all historical messages having their full body content successfully extracted and 99.5% synced to Cloudflare R2 for AI search.*

---

## 2. Google Workspace / Gmail Data (`regima.com`)

The Gmail data is stored in the `gmail_sync` schema of the `b2bkp-exchange-sync` database.

### Mailbox Users
- **Total Users:** 28 distinct mailbox users associated with `@regima.com`.
- **Key Accounts Identified:**
  - `dan@regima.com` (Daniel Faucitt - Admin)
  - `jax@regima.com` (Jacqui Faucitt)
  - `pete@regima.com` (Peter Faucitt)
  - `rynette@regima.com` (Rynette Farrar - Suspended)
  - `kay@regima.com` (Kayla Pretorius - Admin)
  - `admin@regima.com` (Admin Global)
  - `orders@regima.com` (RegimA Orders)

### Message Statistics
| Metric | Count | Coverage |
|--------|-------|----------|
| **Total Messages** | 1,518,990 | 100.0% |
| **With Snippet (Preview)** | 1,507,935 | 99.3% |
| **With Plain Text Body** | 1,364,983 | 89.9% |
| **With HTML Body** | 1,342,978 | 88.4% |
| **With Attachments** | 220,985 | 14.5% |
| **Synced to R2 Search** | 1,094,224 | 72.0% |

**Date Range:** Up to July 6, 2025

### Attachment Sync Status
- **Total Tracked Attachments:** 228,488
- **Successfully Downloaded:** 85,126 (37.3%)
- **Pending Download:** 143,337 (62.7%)
- **R2 Upload Errors:** 25

*Note: The Gmail archive is massive (1.5 million messages) with excellent body content coverage (~90%). However, there is a significant backlog of pending attachment downloads (over 143,000 attachments totaling ~35 GB).*

---

## 3. Cross-Domain Communication (Default `neondb`)

In the default `neondb` project (which appears to be a newer or more limited sync target for the `rzo.io` tenant), we found evidence of cross-domain communication:

- **Messages from `regima.com`:** 5,528
- **Messages from `regima.zone`:** 3,764
- **Messages to `regima.com`:** 19,643
- **Messages to `regima.zone`:** 34,466

The top senders in this specific dataset are `info@regima.com` (4,891 msgs), `rynette@regima.zone` (1,437 msgs), and `jax@regima.zone` (1,356 msgs).

---

## Conclusion & Recommendations

1. **Primary Data Source:** For any forensic investigation, legal discovery, or historical analysis regarding RegimA, the **`b2bkp-exchange-sync`** Neon project should be used as the primary data source. It contains over 2.5 million highly-complete records spanning both domains.
2. **Gmail Attachments:** If historical attachments from `regima.com` are required, the Gmail attachment sync process needs to be resumed, as 62% of attachments are currently in a "pending" state.
3. **R2 Search Readiness:** Over 2.1 million messages across both domains have been successfully synced to Cloudflare R2, making them available for the `exchange-intelligent-search` and `gmail-intelligent-search` AI pipelines.
