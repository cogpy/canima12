#!/usr/bin/env python3
"""
ChainLex Bridge for ad-res-j7

Reads ChainLex exported principles and produces norms.json compatible
with ad-res-j7's lex-inference-engine. Maps chainlex domains to
ad-res-j7 attention heads.

Usage:
    from chainlex_bridge import ChainLexBridge

    bridge = ChainLexBridge("/path/to/chainlex")
    bridge.load()
    bridge.export_norms("norms.json")

    # Get norms for a specific attention head
    causal_norms = bridge.get_norms_for_head("CAUSAL_DIRECT")
"""

import json
import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional


# Mapping from chainlex domains to ad-res-j7 attention heads
DOMAIN_TO_HEADS = {
    "criminal": ["CAUSAL_DIRECT", "INTENTIONALITY"],
    "civil": ["DUTY_VIOLATION"],
    "contract": ["DUTY_VIOLATION"],
    "trust": ["STANDARD_OF_CARE"],
    "fiduciary": ["STANDARD_OF_CARE"],
    "admin": ["NORMATIVE"],
    "administrative": ["NORMATIVE"],
}

# All known attention heads
ALL_HEADS = [
    "CAUSAL_DIRECT",
    "INTENTIONALITY",
    "DUTY_VIOLATION",
    "STANDARD_OF_CARE",
    "NORMATIVE",
]


class ChainLexBridge:
    """
    Bridge between ChainLex exports and ad-res-j7 lex-inference-engine.

    Loads chainlex principles and maps them to ad-res-j7 attention heads,
    producing norms.json compatible with the inference engine.
    """

    def __init__(self, chainlex_path: str):
        """
        Initialize the bridge.

        Args:
            chainlex_path: Path to the chainlex root directory.
                           Expects exports/principles.json to exist.
        """
        self.chainlex_path = Path(chainlex_path)
        self.principles_file = self.chainlex_path / "exports" / "principles.json"
        self.principles: List[Dict[str, Any]] = []
        self.norms: List[Dict[str, Any]] = []
        self._norms_by_head: Dict[str, List[Dict[str, Any]]] = {
            head: [] for head in ALL_HEADS
        }
        self._loaded = False

    def load(self) -> None:
        """
        Load principles from chainlex exports and build norms.

        Raises:
            FileNotFoundError: If the principles export file does not exist.
        """
        if not self.principles_file.exists():
            raise FileNotFoundError(
                f"ChainLex principles export not found: {self.principles_file}\n"
                f"Run: python chainlex/exports/export_for_integration.py"
            )

        with open(self.principles_file, "r", encoding="utf-8") as f:
            self.principles = json.load(f)

        print(f"Loaded {len(self.principles)} principles from {self.principles_file}")

        # Build norms from principles
        self._build_norms()
        self._loaded = True

    def _build_norms(self) -> None:
        """Convert chainlex principles to ad-res-j7 norms format."""
        self.norms = []
        self._norms_by_head = {head: [] for head in ALL_HEADS}

        for principle in self.principles:
            domains = principle.get("domains", [])

            # Determine which attention heads this principle maps to
            mapped_heads = set()
            for domain in domains:
                heads = DOMAIN_TO_HEADS.get(domain, [])
                mapped_heads.update(heads)

            # If no domain mapping found, assign to NORMATIVE as default
            if not mapped_heads:
                mapped_heads.add("NORMATIVE")

            norm = {
                "norm_id": principle.get("id", ""),
                "name": principle.get("name", ""),
                "description": principle.get("description", ""),
                "norm_type": "principle",
                "source": "chainlex",
                "confidence": principle.get("confidence", 1.0),
                "provenance": principle.get("provenance", ""),
                "inference_type": principle.get("inference_type", "deductive"),
                "domains": domains,
                "attention_heads": sorted(mapped_heads),
                "conditions": {
                    "domains": domains,
                    "inference_type": principle.get("inference_type", "deductive"),
                },
                "consequences": {
                    "principle": principle.get("name", ""),
                    "application": principle.get("application_context", ""),
                },
                "priority": principle.get("confidence", 1.0),
                "metadata": {
                    "provenance": principle.get("provenance", ""),
                    "related_principles": principle.get("related_principles", []),
                    "application_context": principle.get("application_context", ""),
                },
            }

            self.norms.append(norm)

            # Index by attention head
            for head in mapped_heads:
                self._norms_by_head[head].append(norm)

    def export_norms(self, output_path: Optional[str] = None) -> str:
        """
        Export norms to JSON file.

        Args:
            output_path: Path for the output file. Defaults to
                         norms.json in the same directory as this script.

        Returns:
            The path to the written file.
        """
        if not self._loaded:
            self.load()

        if output_path is None:
            output_path = str(Path(__file__).resolve().parent / "norms.json")

        export_data = {
            "source": "chainlex",
            "version": "1.0",
            "total_norms": len(self.norms),
            "attention_heads": {
                head: len(norms) for head, norms in self._norms_by_head.items()
            },
            "norms": self.norms,
        }

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=2, default=str)

        file_size = os.path.getsize(output_path)
        print(f"Exported {len(self.norms)} norms to {output_path} ({file_size} bytes)")

        return output_path

    def get_norms_for_head(self, head_name: str) -> List[Dict[str, Any]]:
        """
        Get all norms mapped to a specific attention head.

        Args:
            head_name: One of CAUSAL_DIRECT, INTENTIONALITY,
                       DUTY_VIOLATION, STANDARD_OF_CARE, NORMATIVE.

        Returns:
            List of norm dicts for the given head.
        """
        if not self._loaded:
            self.load()

        if head_name not in ALL_HEADS:
            print(f"Warning: Unknown attention head '{head_name}'. "
                  f"Known heads: {ALL_HEADS}")
            return []

        return self._norms_by_head.get(head_name, [])

    def summary(self) -> Dict[str, Any]:
        """Get a summary of loaded norms."""
        if not self._loaded:
            self.load()

        return {
            "total_principles": len(self.principles),
            "total_norms": len(self.norms),
            "norms_by_head": {
                head: len(norms) for head, norms in self._norms_by_head.items()
            },
            "domains_covered": sorted(set(
                d for n in self.norms for d in n.get("domains", [])
            )),
        }


def main():
    """Run standalone: load chainlex exports and produce norms.json."""
    print("=" * 70)
    print("ChainLex Bridge for ad-res-j7")
    print("=" * 70)

    # Default chainlex path: sibling directory
    default_chainlex = Path(__file__).resolve().parent.parent.parent / "chainlex"

    chainlex_path = sys.argv[1] if len(sys.argv) > 1 else str(default_chainlex)

    print(f"\nChainLex path: {chainlex_path}")

    try:
        bridge = ChainLexBridge(chainlex_path)
        bridge.load()
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        return 1

    # Export norms
    output = bridge.export_norms()

    # Print summary
    summary = bridge.summary()
    print(f"\nSummary:")
    print(f"  Total principles: {summary['total_principles']}")
    print(f"  Total norms: {summary['total_norms']}")
    print(f"  Domains: {', '.join(summary['domains_covered'])}")
    print(f"\n  Norms by attention head:")
    for head, count in summary["norms_by_head"].items():
        print(f"    {head}: {count}")

    print(f"\nOutput: {output}")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(main())
