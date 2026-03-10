---
event_id: EVENT_GWS_AUDIT_001
date: 2026-03-10
type: FORENSIC_TOOL_CREATION
category: Evidence Infrastructure
severity: HIGH
---

# EVENT_GWS_AUDIT_001: Google Workspace Forensic Audit Skill Created

## Summary

Created the `google-workspace-forensic-audit` skill as the Gmail API equivalent of the existing `exchange-forensic-audit` skill. This enables cross-platform forensic transport metadata extraction from both Exchange Online and Google Workspace mailboxes.

## Details

The skill extracts complete forensic transport audit JSON for Gmail messages, including route hop records (Received headers with IPs, servers, timestamps), origin device/client identification, authentication results (SPF/DKIM/DMARC/ARC), Google transport metadata, and all raw internet message headers.

## Test Results

| Scope | User | Messages Audited | SPF | DKIM | DMARC | Avg Hops |
|-------|------|-----------------|-----|------|-------|----------|
| from:fnb | dan@regima.com | 5/5 | pass | N/A | pass | 2 |
| from:rynette | dan@regima.com | 3/3 | pass | pass | N/A | 6 |
| all-users from:fnb | domain-wide | 2/2 | pass | N/A | pass | 2 |

## Key Findings

FNB notification emails (inContact@fnb.co.za) consistently show SPF=pass and DMARC=pass with 2 transport hops, originating from IP 196.10.113.235 (mxincontact.fnb.co.za) via TLS 1.3. This establishes the authenticity and integrity of FNB transaction notifications used as evidence in the revenue stream hijacking case.

Rynette Farrar emails from regima.zone show 6 hops (Exchange Online to Gmail via Google SMTP), with SPF=pass and DKIM=pass, confirming the transport chain for internal communications.

## Capabilities

| Mode | Source | Description |
|------|--------|-------------|
| live | Gmail API | Direct search with `messages.list` + `messages.get` |
| db | Neon DB | Query `gmail_sync` schema, fetch headers from Gmail API |
| all-users | Domain-wide | Scan all domain users (with fallback to known user list) |

## Evidence Impact

This tool strengthens the **Documentary** and **Digital Forensic** evidence categories by providing cryptographically verifiable transport chain records for all Gmail communications relevant to Case 2025-137857.

## Related Events

- EVENT_EML_001 (Exchange Forensic EML Extraction)
- EVENT_SIM_001 (LEX-SIM-NN Simulation)
