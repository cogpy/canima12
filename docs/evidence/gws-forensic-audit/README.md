# Google Workspace Forensic Audit Evidence

This directory contains forensic transport audit JSON files extracted from Gmail messages via the Gmail API. Each `.audit.json` file provides a complete chain-of-custody record including route hops, authentication verdicts (SPF/DKIM/DMARC/ARC), origin identification, and all raw internet message headers.

## Skill Reference

The `google-workspace-forensic-audit` skill is the Gmail API equivalent of the `exchange-forensic-audit` skill. Both produce compatible `.audit.json` output for cross-platform forensic analysis.

## Output Schema

Each audit file contains:

| Section | Description |
|---------|-------------|
| `message_identity` | Gmail ID, thread ID, internet message ID, labels |
| `envelope` | From, to, cc, bcc, subject, date |
| `origin` | Client IP, mailer, user agent, return path |
| `authentication` | SPF, DKIM, DMARC, ARC, Received-SPF verdicts |
| `transport_hops[]` | Chronological relay chain with IPs, servers, TLS |
| `google_transport` | Google-specific headers and properties |
| `transport_summary` | Hop count, origin IP, auth verdicts |
| `raw_headers[]` | Complete header array |

## Test Results (2026-03-10)

| Scope | User | Messages | SPF | DKIM | DMARC | Hops |
|-------|------|----------|-----|------|-------|------|
| from:fnb | dan@regima.com | 5/5 | pass | N/A | pass | 2 |
| from:rynette | dan@regima.com | 3/3 | pass | pass | N/A | 6 |
| all-users from:fnb | domain-wide | 2/2 | pass | N/A | pass | 2 |
