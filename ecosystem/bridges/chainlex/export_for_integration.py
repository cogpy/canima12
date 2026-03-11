#!/usr/bin/env python3
"""
ChainLex Export for Integration

Exports ChainLex principles, rules, and inference chains to JSON files
for consumption by LexRexHGNN and ad-res-j7 integration layers.

Usage:
    python export_for_integration.py
"""

import json
import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

# Add parent directory to path so we can import chainlex_api
_parent_dir = str(Path(__file__).resolve().parent.parent)
if _parent_dir not in sys.path:
    sys.path.insert(0, _parent_dir)

try:
    from chainlex_api import ChainLex
except ImportError as e:
    print(f"Warning: Could not import ChainLex API: {e}")
    print(f"Looked in: {_parent_dir}")
    print("Falling back to stub mode - exports will contain empty data.")
    ChainLex = None


EXPORTS_DIR = Path(__file__).resolve().parent

# Domains relevant to case 2025-137857
CASE_DOMAINS = ["criminal", "civil", "trust", "fiduciary"]

# Sample inference chain endpoints per domain for pre-computation
DOMAIN_CHAIN_ENDPOINTS = {
    "criminal": [
        ("nulla-poena-sine-lege", "criminal-liability?"),
        ("presumption-of-innocence", "guilt-proven?"),
    ],
    "civil": [
        ("pacta-sunt-servanda", "contract-valid?"),
        ("neminem-laedere", "delict-established?"),
    ],
    "trust": [
        ("fiduciary-duty", "trust-breach?"),
        ("bona-fides", "good-faith-met?"),
    ],
    "fiduciary": [
        ("fiduciary-duty", "duty-breach?"),
        ("uberrimae-fidei", "disclosure-met?"),
    ],
}


def format_principle(raw: Dict[str, Any], index: int) -> Dict[str, Any]:
    """
    Format a raw principle dict from ChainLex API into the standard
    integration schema.
    """
    name = raw.get("name", f"principle-{index}")
    return {
        "id": raw.get("id", f"p-{index:04d}"),
        "name": name,
        "description": raw.get("docstring", raw.get("description", "")),
        "domains": raw.get("domains", []),
        "confidence": raw.get("confidence", 1.0),
        "provenance": raw.get("provenance", raw.get("framework", "lv1")),
        "related_principles": raw.get("related_principles", raw.get("cross_references", [])),
        "inference_type": raw.get("inference_type", "deductive"),
        "application_context": raw.get("application_context", ""),
    }


def export_principles(chainlex: Any) -> List[Dict[str, Any]]:
    """Export all Level 1 principles to standard format."""
    raw_principles = chainlex.principles.all()
    formatted = []
    for i, p in enumerate(raw_principles):
        formatted.append(format_principle(p, i))
    return formatted


def export_rules_by_domain(chainlex: Any) -> Dict[str, List[Dict[str, Any]]]:
    """Export rules grouped by domain."""
    stats = chainlex.stats()
    domains = list(stats.get("domains", {}).keys())

    rules_by_domain = {}
    for domain in domains:
        raw_rules = chainlex.rules.by_domain(domain)
        domain_rules = []
        for r in raw_rules:
            domain_rules.append({
                "id": r.get("id", f"{domain}:{r.get('name', 'unknown')}"),
                "name": r.get("name", ""),
                "description": r.get("docstring", r.get("description", "")),
                "domain": domain,
                "framework": r.get("framework", ""),
                "cross_references": r.get("cross_references", []),
                "confidence": r.get("confidence", 0.95),
            })
        if domain_rules:
            rules_by_domain[domain] = domain_rules

    return rules_by_domain


def export_inference_chains(chainlex: Any) -> Dict[str, List[Dict[str, Any]]]:
    """
    Pre-compute inference chains for domains relevant to case 2025-137857.
    """
    chains = {}

    for domain, endpoints in DOMAIN_CHAIN_ENDPOINTS.items():
        domain_chains = []
        for start_principle, end_conclusion in endpoints:
            chain = chainlex.inference.chain(start_principle, end_conclusion)
            chain_entry = {
                "from_principle": start_principle,
                "to_conclusion": end_conclusion,
                "domain": domain,
                "chain": chain if chain else [],
                "confidence": (
                    chainlex.inference.confidence(chain) if chain else 0.0
                ),
                "explanation": (
                    chainlex.inference.explain(chain) if chain else "No chain found"
                ),
            }
            domain_chains.append(chain_entry)
        chains[domain] = domain_chains

    return chains


def write_json(data: Any, filename: str) -> Path:
    """Write data to a JSON file in the exports directory."""
    filepath = EXPORTS_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"  Exported: {filepath} ({os.path.getsize(filepath)} bytes)")
    return filepath


def main():
    """Run the full export pipeline."""
    print("=" * 70)
    print("ChainLex Export for Integration")
    print("=" * 70)

    # Ensure exports directory exists
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

    if ChainLex is None:
        print("\nChainLex API not available. Writing empty export files.")
        write_json([], "principles.json")
        write_json({}, "rules_by_domain.json")
        write_json({}, "inference_chains.json")
        print("\nDone (stub mode).")
        return 1

    print("\nInitializing ChainLex API...")
    try:
        chainlex = ChainLex(base_path=_parent_dir)
    except Exception as e:
        print(f"Error initializing ChainLex: {e}")
        print("Writing empty export files.")
        write_json([], "principles.json")
        write_json({}, "rules_by_domain.json")
        write_json({}, "inference_chains.json")
        return 1

    # Export principles
    print("\n[1/3] Exporting principles...")
    principles = export_principles(chainlex)
    write_json(principles, "principles.json")

    # Export rules by domain
    print("\n[2/3] Exporting rules by domain...")
    rules = export_rules_by_domain(chainlex)
    write_json(rules, "rules_by_domain.json")

    # Export inference chains
    print("\n[3/3] Exporting inference chains for case 2025-137857...")
    chains = export_inference_chains(chainlex)
    write_json(chains, "inference_chains.json")

    # Summary
    print("\n" + "-" * 70)
    print("Export Summary:")
    print(f"  Principles: {len(principles)}")
    print(f"  Domain groups: {len(rules)}")
    total_rules = sum(len(v) for v in rules.values())
    print(f"  Total rules: {total_rules}")
    total_chains = sum(len(v) for v in chains.values())
    print(f"  Inference chains: {total_chains}")
    print(f"  Case domains: {', '.join(CASE_DOMAINS)}")
    print("=" * 70)
    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
