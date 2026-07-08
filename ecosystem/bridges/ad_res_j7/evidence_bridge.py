"""
Evidence Bridge: ad-res-j7 -> revstream1

Maps ad-res-j7 annexure evidence files, hypergraph nodes, and cross-references
into revstream1's entity/event/relation data structures.

Provides structured access to the 1,700+ evidence files organized across
20+ annexures (JF01-JF16, SF1-SF8+) for integration with the canonical
data models in revstream1.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# Annexure-to-evidence category mapping
ANNEXURE_CATEGORIES = {
    "JF01": {"category": "shopify_email", "description": "Shopify Plus email showing business structure"},
    "JF02": {"category": "sales_reports", "description": "Sales and revenue reports"},
    "JF03": {"category": "financial_records", "description": "Financial transaction records"},
    "JF04": {"category": "cipc_records", "description": "CIPC company registration documents"},
    "JF05": {"category": "responsible_person", "description": "Responsible person documentation"},
    "JF06": {"category": "regulatory", "description": "Regulatory compliance documentation"},
    "JF07": {"category": "financial_transactions", "description": "Financial transaction records and bank statements"},
    "JF08": {"category": "correspondence", "description": "Email correspondence and fraud evidence"},
    "JF09": {"category": "court_timeline", "description": "Court order timeline cross-reference"},
    "JF10": {"category": "director_loans", "description": "Director loan accounts"},
    "JF11": {"category": "medical_testing", "description": "Medical testing documentation"},
    "JF12": {"category": "criminal_safety", "description": "Criminal matter safety guide"},
    "JF13": {"category": "additional_evidence", "description": "Additional evidence package"},
    "SF1": {"category": "bantjies_debt", "description": "Bantjies debt documentation"},
    "SF2": {"category": "sage_screenshots", "description": "Sage system screenshots showing Rynette control"},
    "SF3": {"category": "stock_adjustment", "description": "Stock adjustment documentation"},
    "SF4": {"category": "sars_audit", "description": "SARS audit documentation"},
    "SF5": {"category": "adderory", "description": "Adderory registration documentation"},
    "SF6": {"category": "kayla_estate", "description": "Kayla Pretorius estate documentation"},
    "SF7": {"category": "court_order", "description": "Court order documentation"},
    "SF8": {"category": "employment", "description": "Linda employment documentation"},
    "SF9": {"category": "demand_letter", "description": "Ian Levitt R63M demand letter"},
    "SF10": {"category": "fnb_fraud", "description": "FNB fraud letter and banking evidence"},
    "SF11": {"category": "sage_identity", "description": "Sage identity fraud screenshots"},
    "SF14": {"category": "ketoni", "description": "Ketoni investment documentation"},
    "SF15": {"category": "false_report", "description": "False criminal report filed"},
}

# Evidence file types and their legal significance
EVIDENCE_TYPE_WEIGHTS = {
    "bank_statement": 0.95,
    "court_document": 0.98,
    "email": 0.85,
    "screenshot": 0.80,
    "cipc_filing": 0.95,
    "accounting_record": 0.90,
    "affidavit": 0.95,
    "correspondence": 0.80,
    "financial_record": 0.90,
}

# Mapping ad-res-j7 case directories to revstream1 case tracks
CASE_TRACK_MAP = {
    "1-CIVIL-RESPONSE": "civil_rescission",
    "2-CRIMINAL-CASE": "criminal_prosecution",
    "3-EXTERNAL-VALIDATION": "external_validation",
}


class EvidenceBridge:
    """
    Bridges ad-res-j7 evidence repository with revstream1 data models.

    Provides:
    - Annexure evidence inventory with category classification
    - Entity-to-evidence mapping (which evidence supports which entity)
    - Event-to-evidence mapping (which evidence corroborates which event)
    - Cross-reference between ad-res-j7 paths and revstream1 evidence codes
    """

    def __init__(self, ad_res_j7_path: str, revstream1_path: str = None):
        self.ad_res_path = Path(ad_res_j7_path)
        self.revstream1_path = Path(revstream1_path) if revstream1_path else None
        self._entities: Dict[str, Any] = {}
        self._events: List[Dict[str, Any]] = []
        self._loaded = False

    def load(self) -> bool:
        """Load revstream1 data models for cross-referencing."""
        try:
            if self.revstream1_path:
                entities_path = self.revstream1_path / "data_models" / "entities" / "entities.json"
                if entities_path.exists():
                    with open(entities_path) as f:
                        self._entities = json.load(f)

                events_path = self.revstream1_path / "data_models" / "events.json"
                if events_path.exists():
                    with open(events_path) as f:
                        data = json.load(f)
                        self._events = data.get("events", data) if isinstance(data, dict) else data

            self._loaded = True
            return True
        except Exception as e:
            print(f"[EvidenceBridge] Error loading data: {e}")
            return False

    def inventory_annexures(self) -> List[Dict[str, Any]]:
        """
        Build a complete inventory of annexure evidence files in ad-res-j7.

        Returns list of evidence items with metadata, file counts, and
        category classification.
        """
        annexures_dir = self.ad_res_path / "ANNEXURES"
        if not annexures_dir.exists():
            return []

        inventory = []
        for item in sorted(annexures_dir.iterdir()):
            if not item.is_dir():
                continue

            annexure_code = item.name.split(" ")[0].split("-")[0].strip()
            category_info = ANNEXURE_CATEGORIES.get(annexure_code, {
                "category": "uncategorized",
                "description": item.name,
            })

            files = []
            for f in item.rglob("*"):
                if f.is_file() and not f.name.startswith("."):
                    files.append({
                        "path": str(f.relative_to(self.ad_res_path)),
                        "name": f.name,
                        "size_bytes": f.stat().st_size,
                        "extension": f.suffix.lower(),
                    })

            inventory.append({
                "annexure_code": annexure_code,
                "directory_name": item.name,
                "category": category_info["category"],
                "description": category_info["description"],
                "file_count": len(files),
                "files": files,
                "path": str(item.relative_to(self.ad_res_path)),
            })

        return inventory

    def map_entities_to_evidence(self) -> Dict[str, Dict[str, Any]]:
        """
        Map revstream1 entities to their supporting evidence in ad-res-j7.

        Returns dict keyed by entity_id with evidence details.
        """
        if not self._loaded:
            self.load()

        entity_evidence = {}
        all_entities = []

        persons = self._entities.get("entities", {}).get("persons", [])
        orgs = self._entities.get("entities", {}).get("organizations", [])
        all_entities = persons + orgs

        for entity in all_entities:
            entity_id = entity.get("entity_id", "")
            evidence_refs = entity.get("evidence", [])
            ad_res_refs = entity.get("ad_res_j7_references", [])
            enhanced_refs = entity.get("ad_res_j7_evidence_enhanced", [])

            # Deduplicate and normalize references
            all_refs = set()
            for ref in evidence_refs + ad_res_refs + enhanced_refs:
                # Extract annexure code from reference string
                for code in ANNEXURE_CATEGORIES:
                    if code in ref:
                        all_refs.add(code)
                        break

            # Resolve to actual file paths
            resolved_paths = []
            annexures_dir = self.ad_res_path / "ANNEXURES"
            for code in all_refs:
                if annexures_dir.exists():
                    for d in annexures_dir.iterdir():
                        if d.is_dir() and d.name.startswith(code):
                            resolved_paths.append(str(d.relative_to(self.ad_res_path)))
                            break

            entity_evidence[entity_id] = {
                "entity_id": entity_id,
                "entity_name": entity.get("name", ""),
                "evidence_codes": sorted(all_refs),
                "evidence_count": len(all_refs),
                "resolved_paths": resolved_paths,
                "evidence_strength": entity.get("evidence_strength", "unknown"),
                "criminal_threshold": entity.get("criminal_threshold", "unknown"),
                "burden_of_proof": entity.get("burden_of_proof_analysis", {}),
            }

        return entity_evidence

    def map_events_to_evidence(self) -> Dict[str, Dict[str, Any]]:
        """
        Map revstream1 events to their supporting evidence in ad-res-j7.

        Returns dict keyed by event_id with evidence details.
        """
        if not self._loaded:
            self.load()

        event_evidence = {}
        for event in self._events:
            event_id = event.get("event_id", "")
            evidence_refs = event.get("evidence", [])
            if isinstance(evidence_refs, dict):
                evidence_refs = evidence_refs.get("references", [])

            evidence_codes = set()
            for ref in evidence_refs:
                ref_str = ref if isinstance(ref, str) else str(ref)
                for code in ANNEXURE_CATEGORIES:
                    if code in ref_str:
                        evidence_codes.add(code)
                        break

            event_evidence[event_id] = {
                "event_id": event_id,
                "event_title": event.get("title", event.get("description", "")),
                "event_date": event.get("date", ""),
                "evidence_codes": sorted(evidence_codes),
                "evidence_count": len(evidence_codes),
                "criminal_threshold": event.get("criminal_threshold", False),
                "burden_of_proof": event.get("burden_of_proof", ""),
            }

        return event_evidence

    def build_evidence_chain(self, entity_id: str) -> List[Dict[str, Any]]:
        """
        Build a complete evidence chain for a specific entity, linking
        entity -> events -> evidence -> annexure files.
        """
        if not self._loaded:
            self.load()

        entity_map = self.map_entities_to_evidence()
        event_map = self.map_events_to_evidence()

        entity_info = entity_map.get(entity_id, {})
        if not entity_info:
            return []

        # Find all events involving this entity
        chain = []
        for event in self._events:
            event_id = event.get("event_id", "")
            perpetrators = event.get("perpetrators", [])
            entities_involved = event.get("entities_involved", [])

            involved_ids = set(perpetrators)
            for ei in entities_involved:
                if isinstance(ei, str):
                    involved_ids.add(ei)
                elif isinstance(ei, dict):
                    involved_ids.add(ei.get("entity_id", ""))

            if entity_id in involved_ids:
                event_info = event_map.get(event_id, {})
                chain.append({
                    "entity_id": entity_id,
                    "entity_name": entity_info.get("entity_name", ""),
                    "event_id": event_id,
                    "event_title": event_info.get("event_title", ""),
                    "event_date": event_info.get("event_date", ""),
                    "evidence_codes": event_info.get("evidence_codes", []),
                    "criminal_threshold": event_info.get("criminal_threshold", False),
                })

        chain.sort(key=lambda c: c.get("event_date", ""))
        return chain

    def generate_evidence_export(self) -> Dict[str, Any]:
        """
        Generate complete evidence mapping export for cross-repo integration.
        """
        if not self._loaded:
            self.load()

        inventory = self.inventory_annexures()
        entity_map = self.map_entities_to_evidence()
        event_map = self.map_events_to_evidence()

        # Build evidence chains for Tier A entities
        tier_a_chains = {}
        for entity_id in ("PERSON_001", "PERSON_002", "PERSON_007"):
            chain = self.build_evidence_chain(entity_id)
            if chain:
                tier_a_chains[entity_id] = chain

        return {
            "metadata": {
                "generated_at": datetime.utcnow().isoformat() + "Z",
                "source": "ad_res_j7_evidence_bridge",
                "case_number": "2025-137857",
                "total_annexures": len(inventory),
                "total_evidence_files": sum(a["file_count"] for a in inventory),
                "entities_with_evidence": len([e for e in entity_map.values() if e["evidence_count"] > 0]),
                "events_with_evidence": len([e for e in event_map.values() if e["evidence_count"] > 0]),
            },
            "annexure_inventory": inventory,
            "entity_evidence_map": entity_map,
            "event_evidence_map": event_map,
            "tier_a_evidence_chains": tier_a_chains,
        }


def main():
    """CLI entry point for ad-res-j7 evidence bridge."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Bridge ad-res-j7 evidence to revstream1 data models"
    )
    parser.add_argument(
        "--ad-res-j7-path",
        default=os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "ad-res-j7"),
        help="Path to ad-res-j7 repository",
    )
    parser.add_argument(
        "--revstream1-path",
        default=os.path.join(os.path.dirname(__file__), "..", ".."),
        help="Path to revstream1 repository",
    )
    parser.add_argument(
        "--output",
        default=os.path.join(os.path.dirname(__file__), "evidence_export.json"),
        help="Output JSON file path",
    )
    args = parser.parse_args()

    bridge = EvidenceBridge(args.ad_res_j7_path, args.revstream1_path)
    if not bridge.load():
        print("[EvidenceBridge] Failed to load data")
        return 1

    export = bridge.generate_evidence_export()

    with open(args.output, "w") as f:
        json.dump(export, f, indent=2, default=str)

    meta = export["metadata"]
    print(f"[EvidenceBridge] Evidence export written to {args.output}")
    print(f"  Annexures: {meta['total_annexures']}")
    print(f"  Evidence files: {meta['total_evidence_files']}")
    print(f"  Entities with evidence: {meta['entities_with_evidence']}")
    print(f"  Events with evidence: {meta['events_with_evidence']}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
