# ComCoSys Mail Sync Status Report

**Date:** March 28, 2026
**Tenant:** rzo.io (dc24b9a5-3925-471f-b9f9-0a4a5081b8c5)

This report provides a comprehensive overview of the current mail synchronization status across all layers of the ComCoSys architecture, including Exchange Online (Neon DB), Cloudflare R2, and Gmail.

## 1. Exchange Online Sync Status (Neon DB)

The primary synchronization layer captures metadata, body content, and attachments from Exchange Online into the Neon PostgreSQL database.

### Overall Message Coverage

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Messages** | 422,014 | 100.0% |
| **With Body Preview** | 421,882 | 99.9% |
| **With Full Body Content** | 27,397 | 6.5% |
| **With Attachments** | 10,083 | 2.4% |

*Note: The system currently has a significant backlog for full body content backfilling, with only 6.5% of messages having their full body content downloaded.*

### Mailbox Statistics

| Metric | Count |
|--------|-------|
| **Registered Users** | 118 |
| **Active Users (with messages)** | 38 |
| **Mail Folders Synced** | 665 |
| **Date Range** | July 6, 2016 – March 28, 2026 |

### Yearly Breakdown

The following table shows the distribution of messages by year and the corresponding body content coverage:

| Year | Total Messages | With Body Content | Body Coverage % |
|------|----------------|-------------------|-----------------|
| 2026 | 12,101 | 12,090 | 99.9% |
| 2025 | 241,162 | 13,358 | 5.5% |
| 2024 | 139,230 | 848 | 0.6% |
| 2023 | 19,381 | 158 | 0.8% |
| 2022 | 2,945 | 291 | 9.9% |
| 2021 | 1,669 | 88 | 5.3% |
| 2020 | 1,162 | 276 | 23.8% |
| 2019 | 1,269 | 64 | 5.0% |
| 2018 | 2,054 | 145 | 7.1% |
| 2017 | 1,030 | 70 | 6.8% |
| 2016 | 11 | 9 | 81.8% |

*Observation: Recent messages (2026) have near-complete body coverage, while the massive influx of messages in 2024-2025 remains largely un-backfilled.*

## 2. Cloudflare R2 Sync Status

Cloudflare R2 serves as the object storage layer for both message content (Markdown format for AI Search) and binary attachments.

### R2 Upload Coverage (Neon DB Tracking)

According to the `rzo_r2_sync` tracking table in Neon DB, **13,669** messages have been successfully synced to R2. This represents approximately **3.2%** of the total message volume, but covers about **50%** of the messages that have full body content available.

### R2 Bucket Statistics

Direct inspection of the R2 buckets reveals the following storage metrics:

| Bucket Name | Object Count | Total Size | Purpose |
|-------------|--------------|------------|---------|
| `exchange-intelligent-search` | > 200,000 | 117.6 MB | Markdown message exports for AI Search |
| `exchange-attachments` | 11,710 | 3.65 GB | Binary email attachments |
| `gmail-intelligent-search` | > 50,000 | 151.4 MB | Gmail message exports |
| `gmail-attachments` | > 50,000 | 9.25 GB | Gmail binary attachments |

*Note: Object counts marked with ">" indicate that the count exceeded the sampling threshold during inspection.*

## 3. Attachment Sync Status

The attachment synchronization process extracts binary files from messages and stores them in R2.

| Metric | Count |
|--------|-------|
| **Total Attachment Records** | 1,288 |
| **Successfully Downloaded** | 1,287 |
| **Pending Download** | 0 |
| **Failed Download** | 1 |
| **Uploaded to R2** | 1,288 |
| **Total Size (DB Tracked)** | 48.4 MB |

*Discrepancy Note: There is a significant difference between the number of messages flagged with attachments (10,083) and the number of actual attachment records processed (1,288 across 315 distinct messages). Furthermore, the R2 bucket contains 11,710 objects (3.65 GB), suggesting that many attachments exist in storage but are not fully tracked in the Neon DB `attachments` table.*

## 4. Gmail Sync Status

The Gmail integration relies on the `gmail` MCP server for direct access to mailboxes.

**Status: OFFLINE**

Attempts to access Gmail via the MCP server failed with the error: `Mail service not enabled`. This indicates that the Gmail API is not currently enabled or authorized for the configured credentials. Gmail search and sync operations cannot proceed until this is resolved.

## 5. Recent Sync Activity

The synchronization pipeline is actively running. The most recent completed runs are:

1. **rzo-body-backfill**: Completed Mar 28, 2026 04:02 UTC (2,000 messages synced)
2. **rzo-delta**: Completed Mar 28, 2026 03:52 UTC (162 messages synced across 118 users/665 folders)
3. **rzo-body-backfill**: Completed Mar 27, 2026 04:13 UTC (2,000 messages synced)
4. **rzo-delta**: Completed Mar 27, 2026 04:04 UTC (190 messages synced)

Currently, there are multiple `backfill-turbo` processes marked as "running" in the sync log, indicating an ongoing effort to address the body content backlog.

## Summary & Recommendations

1. **Exchange Metadata**: Excellent coverage (99.9% preview availability).
2. **Exchange Body Content**: Significant backlog. Only 6.5% of messages have full bodies, mostly concentrated in 2026. The daily backfill jobs (2,000 msgs/day) are insufficient to clear the 394,000+ message backlog in a reasonable timeframe.
3. **Attachments**: The attachment sync appears fragmented. While the R2 bucket contains 3.65 GB of data, the database only tracks 1,288 attachments. A reconciliation process should be run.
4. **Gmail**: Currently inaccessible. The Gmail API needs to be enabled and re-authenticated.
5. **Next Steps for Search**: Any search operations should rely primarily on `body_preview` and `subject` fields in the Neon DB, as full `body_content` and R2 AI Search will miss ~93% of the historical archive.
