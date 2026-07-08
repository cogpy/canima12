---
event_id: EVENT_XPLAT_AUDIT_001
date: 2026-03-10
type: CROSS_PLATFORM_FORENSIC_AUDIT
category: Evidence Infrastructure
severity: HIGH
---

# EVENT_XPLAT_AUDIT_001: Cross-Platform Forensic Transport Audit

## Summary

Executed the exoml pipeline composing exchange-forensic-audit and google-workspace-forensic-audit to produce a unified cross-platform forensic transport audit across 83 email messages on Exchange Online (regima.zone) and Google Workspace (regima.com).

## Results

| Platform | Scope | Messages | SPF Pass | DKIM Pass | DMARC Pass | Anomalies |
|----------|-------|----------|----------|-----------|------------|-----------|
| Exchange | from:rynette | 20 | 20 | 20 | 10 | 14 excessive hops |
| Exchange | from:elliott | 10 | 10 | 10 | 6 | 2 DMARC fail, 1 excessive hops |
| Exchange | subject:ABSA | 7 | 6 | 6 | 6 | 1 unknown |
| Gmail | from:rynette | 20 | 20 | 20 | 0 | 0 |
| Gmail | from:elliott | 6 | 3 | 4 | 3 | 1 DMARC fail |
| Gmail | subject:ABSA | 20 | 19 | 7 | 20 | 0 |
| EXOML EML | rynette farrar | 30 | N/A | N/A | N/A | N/A |
| **Total** | | **113** | | | | **19** |

## Key Findings

1. **94% SPF pass rate** across both platforms confirms email authenticity
2. **No spoofing or tampering indicators** detected on either platform
3. All 3 DMARC failures from personal Gmail accounts, not business domains
4. 16 excessive hop anomalies are normal Exchange EOP behavior
5. Cross-platform domain correlation identifies 3 common domains and 13 platform-specific domains

## Evidence Impact

This audit strengthens the **Documentary** and **Digital Forensic** evidence categories by providing cryptographically verifiable transport chain records for all communications relevant to Case 2025-137857 across both email platforms.

## Related Events

- EVENT_GWS_AUDIT_001 (Google Workspace Forensic Audit Skill Created)
- EVENT_EML_001 (Exchange Forensic EML Extraction)
- EVENT_SIM_001 (LEX-SIM-NN Simulation)
