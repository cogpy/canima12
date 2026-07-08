---
layout: default
title: "EVENT_EML_001: Forensic EML Evidence Extraction"
event_id: EVENT_EML_001
date: 2026-03-10
category: Evidence Collection
type: Forensic Extraction
burden_of_proof: verified_forensic
evidence_strength: 99
---

# EVENT_EML_001: Forensic EML Evidence Extraction from Exchange Database

## Summary

On 10 March 2026, 355 forensic EML files were extracted from the Exchange Online database (Neon PostgreSQL `exchange_sync` schema) covering key perpetrators and evidence categories. Each EML file is accompanied by a `.forensic.json` sidecar containing SHA-256 integrity hashes, message identity, envelope metadata, mailbox context, and attachment manifests.

## Extraction Summary

| Scope | Files Extracted | Sender Domains | Key Evidence |
|-------|----------------|----------------|--------------|
| Bantjies communications | 99 | 15+ | SARS manipulation, trust capture, financial control |
| Rynette Farrar communications | 100 | 28 | Identity impersonation, operational control |
| Elliott Attorneys | 6 | 1 | Legal threats, contempt proceedings |
| ABSA/Bank details | 100 | 20+ | Revenue diversion, unauthorized bank changes |
| Manufacturing subject | 50 | 10+ | Product manufacturing (context) and SARS "manufacture" admission |
| **Total** | **355** | **28+** | **Complete forensic archive** |

## Forensic Integrity

Each file includes:
- **SHA-256 hash** for tamper detection
- **MD5 and SHA-1** for cross-verification
- **Internet Message ID** for RFC 5322 traceability
- **Conversation ID** for thread reconstruction
- **Attachment manifest** with R2 storage keys

## Significance

This extraction provides a forensically sound, integrity-verified email evidence archive that can be presented in legal proceedings. The domain-organized structure allows rapid identification of communications by sender organization, supporting the conspiracy network analysis.

## Entities Involved

PERSON_002 (Rynette Farrar), PERSON_007 (Daniel Bantjies), PERSON_001 (Peter Faucitt)

## Evidence Files

- [Forensic EML Index](../evidence/forensic_eml/INDEX.md)
- [Forensic EML Manifest](../evidence/forensic_eml/MANIFEST.json)
