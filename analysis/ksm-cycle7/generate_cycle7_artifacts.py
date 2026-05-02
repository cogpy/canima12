import json, os
from pathlib import Path

ROOT = Path('/home/ubuntu/case-work/revstream1')
OUT = ROOT / 'analysis/ksm-cycle7'
FILINGS = ROOT / 'docs/filings/cycle7'

# 1. Generate Pillar XV
pillar_xv = """# PILLAR XV: THE ECHO CHAMBER OF LIABILITY
**Case:** 2025-137857
**Date:** 2 May 2026

## The Reciprocal Channel
The false authority of Bantjies (the unlawfully-appointed Trustee, July 2024) and the false authority of the Implicated Attorneys (acting on Bantjies's instructions) were each impossible without the other. They amplified each other at every material decision point.

## The Four Echoes
| # | Bantjies → Attorneys | Attorneys → Bantjies | Material Effect |
|---|---|---|---|
| Echo α | "I am Trustee, instruct accordingly" (Jul 2024) | "Per our client Bantjies, Trustee" (Aug 2024 onwards) | Authority laundered into legitimate-looking practice |
| Echo β | Sage user-switch instruction (June 2025) | Cover letter validating Sage access (June 2025) | Bookkeeper-level audit trail destroyed |
| Echo γ | Exchange tenant zero-comm directive (July 2025) | Compliance opinion on tenant lock-out (July 2025) | Communication channels neutralized |
| Echo δ | "Founder is Main Trustee from 1 Jul 2025" backdating (11 Aug 2025) | Ex parte application based on "Main Trustee" status (13 Aug 2025) | Backdated authority weaponized against Beneficiary |
"""
with open(OUT / 'PILLAR_XV_ECHO_CHAMBER.md', 'w') as f:
    f.write(pillar_xv)

# 2. Generate Annexure C
annexure_c = """# ANNEXURE C: RECIPROCAL LIABILITY CORRESPONDENCE MAP
**Case:** 2025-137857
**Date:** 2 May 2026

This map demonstrates the mutually reinforcing channel between the Implicated Attorneys and the complicit Accountant (Bantjies).

## Temporal Echo Diagram
```mermaid
sequenceDiagram
    participant B as Bantjies (Accountant)
    participant A as Implicated Attorneys
    
    Note over B,A: Echo α (Jul-Aug 2024)
    B->>A: "I am Trustee, instruct accordingly"
    A->>B: "Per our client Bantjies, Trustee"
    
    Note over B,A: Echo β (Jun 2025)
    B->>A: Sage user-switch instruction
    A->>B: Cover letter validating Sage access
    
    Note over B,A: Echo γ (Jul 2025)
    B->>A: Exchange tenant zero-comm directive
    A->>B: Compliance opinion on tenant lock-out
    
    Note over B,A: Echo δ (Aug 2025)
    B->>A: "Founder is Main Trustee" backdating
    A->>B: Ex parte application based on status
```
"""
with open(OUT / 'ANNEXURE_C_CORRESPONDENCE_MAP.md', 'w') as f:
    f.write(annexure_c)

print("Cycle 7 artifacts generated successfully.")
