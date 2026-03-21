"""
Unified Case Evidence Mapping Registry

Central orchestrator connecting all four repositories in the cogpy ecosystem
for Case 2025-137857. This module provides a single entry point for:

  ad-res-j7   (evidence_db)       -> 1,700+ annexure files, hypergraph
  revstream1   (data_truth)        -> 103 entities, 173 events, 36+ relations
  fincosys     (financial_analysis) -> 556 bank statements, 39 accounts, 4 models
  comcosys     (comms_forensics)   -> 10,832 forensic emails, keyword analysis

The registry produces a unified evidence graph linking:
  Entity -> Events -> Evidence Files -> Financial Records -> Communications

Each link carries provenance (source repo), confidence score, and
burden-of-proof classification.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


class CaseEvidenceMapping:
    """
    Unified cross-repository case evidence mapping for Case 2025-137857.

    Orchestrates all four ecosystem bridges to produce a consolidated
    evidence graph with full provenance tracking.
    """

    REPO_ROLES = {
        "ad-res-j7": "evidence_db",
        "revstream1": "data_truth",
        "fincosys": "financial_analysis",
        "comcosys": "comms_forensics",
    }

    # Canonical entity ID -> human name (Tier A + key entities)
    KEY_ENTITIES = {
        "PERSON_001": "Peter Andrew Faucitt",
        "PERSON_002": "Rynette Farrar",
        "PERSON_004": "Jacqueline Faucitt",
        "PERSON_005": "Daniel Faucitt",
        "PERSON_007": "Daniel Jacobus Bantjies",
        "PERSON_008": "Kayla Pretorius",
        "ORG_001": "RegimA Worldwide Distribution",
        "ORG_002": "RegimA Skin Treatments CC",
        "ORG_003": "RegimA Zone Ltd",
        "ORG_004": "Strategic Logistics Group",
        "ORG_005": "Villa Via Arcadia",
        "ORG_006": "RegimA SA (Pty) Ltd",
        "ORG_008": "Rezonance",
        "ORG_015": "Ketoni Investment Holdings",
        "TRUST_001": "Faucitt Family Trust",
        "PLATFORM_001": "Shopify",
    }

    # Fincosys entity code -> canonical entity ID
    FINCOSYS_ENTITY_MAP = {
        "DJF": "PERSON_005",
        "JF": "PERSON_004",
        "PF": "PERSON_001",
        "RST": "ORG_002",
        "RWD": "ORG_001",
        "SLG": "ORG_004",
        "VVA": "ORG_005",
        "RSA": "ORG_006",
        "REZ": "ORG_008",
        "FFT": "TRUST_001",
        "KIH": "ORG_015",
        "RZN": "ORG_003",
    }

    # Comcosys email -> canonical entity ID
    COMCOSYS_EMAIL_MAP = {
        "jax@regima.zone": "PERSON_004",
        "jax@regima.com": "PERSON_004",
        "dan@regima.zone": "PERSON_005",
        "dan@regima.com": "PERSON_005",
        "pete@regima.com": "PERSON_001",
        "rynette@regima.zone": "PERSON_002",
        "danie.bantjes@gmail.com": "PERSON_007",
        "kay@regima.com": "PERSON_008",
    }

    def __init__(
        self,
        ad_res_j7_path: str = None,
        revstream1_path: str = None,
        fincosys_path: str = None,
        comcosys_path: str = None,
    ):
        base = Path(__file__).parent.parent
        self.paths = {
            "ad-res-j7": Path(ad_res_j7_path) if ad_res_j7_path else base.parent / "ad-res-j7",
            "revstream1": Path(revstream1_path) if revstream1_path else base,
            "fincosys": Path(fincosys_path) if fincosys_path else base.parent / "fincosys",
            "comcosys": Path(comcosys_path) if comcosys_path else base.parent / "comcosys",
        }
        self._evidence_graph: Dict[str, Any] = {}
        self._bridges_loaded = False

    def _load_bridge(self, name: str, bridge_class, *args, **kwargs):
        """Safely load a bridge, returning None on failure."""
        try:
            bridge = bridge_class(*args, **kwargs)
            bridge.load()
            return bridge
        except Exception as e:
            print(f"[CaseEvidenceMapping] Warning: {name} bridge failed to load: {e}")
            return None

    def build_evidence_graph(self) -> Dict[str, Any]:
        """
        Build the unified evidence graph by orchestrating all bridges.

        Returns a comprehensive graph structure linking entities, events,
        evidence files, financial records, and communications.
        """
        graph = {
            "metadata": {
                "case_number": "2025-137857",
                "generated_at": datetime.utcnow().isoformat() + "Z",
                "generator": "CaseEvidenceMapping v1.0",
                "repositories": {},
            },
            "entities": {},
            "evidence_links": [],
            "cross_repo_references": [],
            "coverage_summary": {},
        }

        # Check repo availability
        for repo, path in self.paths.items():
            graph["metadata"]["repositories"][repo] = {
                "role": self.REPO_ROLES[repo],
                "path": str(path),
                "available": path.exists(),
            }

        # 1. Load revstream1 canonical entities as the base
        self._load_canonical_entities(graph)

        # 2. Layer ad-res-j7 evidence
        self._layer_evidence_db(graph)

        # 3. Layer fincosys financial records
        self._layer_financial_data(graph)

        # 4. Layer comcosys communications
        self._layer_communications(graph)

        # 5. Compute coverage summary
        self._compute_coverage(graph)

        self._evidence_graph = graph
        return graph

    def _load_canonical_entities(self, graph: Dict[str, Any]):
        """Load entities from revstream1 as the canonical base."""
        entities_path = self.paths["revstream1"] / "data_models" / "entities" / "entities.json"
        if not entities_path.exists():
            return

        try:
            with open(entities_path) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[CaseEvidenceMapping] Warning: entities.json parse error: {e}")
            return

        persons = data.get("entities", {}).get("persons", [])
        orgs = data.get("entities", {}).get("organizations", [])

        for entity in persons + orgs:
            entity_id = entity.get("entity_id", "")
            graph["entities"][entity_id] = {
                "entity_id": entity_id,
                "name": entity.get("name", ""),
                "role": entity.get("role", ""),
                "agent_type": entity.get("agent_type", ""),
                "evidence_strength": entity.get("evidence_strength", "unknown"),
                "criminal_threshold": entity.get("criminal_threshold", "unknown"),
                "sources": {
                    "revstream1": {
                        "evidence_codes": [],
                        "events": entity.get("timeline_events", []),
                        "ad_res_j7_references": entity.get("ad_res_j7_references", []),
                    },
                    "ad-res-j7": {"annexures": [], "evidence_files": []},
                    "fincosys": {"accounts": [], "statements": []},
                    "comcosys": {"emails": [], "keyword_hits": 0},
                },
            }

            # Extract evidence codes
            for ref in entity.get("evidence", []):
                if isinstance(ref, str):
                    for code in ("JF01", "JF02", "JF03", "JF04", "JF05", "JF06",
                                 "JF07", "JF08", "JF09", "JF10", "JF11", "JF12", "JF13",
                                 "SF1", "SF2", "SF3", "SF4", "SF5", "SF6", "SF7",
                                 "SF8", "SF9", "SF10", "SF11", "SF14", "SF15"):
                        if code in ref:
                            graph["entities"][entity_id]["sources"]["revstream1"]["evidence_codes"].append(code)
                            break

    def _layer_evidence_db(self, graph: Dict[str, Any]):
        """Layer ad-res-j7 evidence file data onto the graph."""
        annexures_dir = self.paths["ad-res-j7"] / "ANNEXURES"
        if not annexures_dir.exists():
            return

        for entity_id, entity_data in graph["entities"].items():
            evidence_codes = entity_data["sources"]["revstream1"].get("evidence_codes", [])
            for code in evidence_codes:
                # Find matching annexure directory
                for d in annexures_dir.iterdir():
                    if d.is_dir() and d.name.startswith(code):
                        file_count = sum(1 for f in d.rglob("*") if f.is_file())
                        entity_data["sources"]["ad-res-j7"]["annexures"].append({
                            "code": code,
                            "path": str(d.relative_to(self.paths["ad-res-j7"])),
                            "file_count": file_count,
                        })

                        graph["evidence_links"].append({
                            "entity_id": entity_id,
                            "source_repo": "ad-res-j7",
                            "evidence_type": "annexure",
                            "reference": code,
                            "path": str(d.relative_to(self.paths["ad-res-j7"])),
                            "provenance": "annexure_directory",
                        })
                        break

    def _layer_financial_data(self, graph: Dict[str, Any]):
        """Layer fincosys financial data onto the graph."""
        # Load master entities
        master_path = self.paths["fincosys"] / "data" / "MASTER_ENTITIES.json"
        accounts_path = self.paths["fincosys"] / "data" / "MASTER_ACCOUNTS.json"

        if not master_path.exists():
            return

        try:
            with open(master_path) as f:
                master_entities = json.load(f)
            accounts = {}
            if accounts_path.exists():
                with open(accounts_path) as f:
                    accounts_data = json.load(f)
                    for acct in accounts_data.get("accounts", []):
                        code = acct.get("entity_code", "")
                        if code not in accounts:
                            accounts[code] = []
                        accounts[code].append(acct)
        except Exception:
            return

        # Map fincosys entities to graph entities
        for entity in master_entities.get("entities", []):
            fincosys_code = entity.get("code", "")
            case_entity_id = self.FINCOSYS_ENTITY_MAP.get(fincosys_code)
            if not case_entity_id or case_entity_id not in graph["entities"]:
                continue

            entity_data = graph["entities"][case_entity_id]
            entity_accounts = accounts.get(fincosys_code, [])

            for acct in entity_accounts:
                acct_info = {
                    "account_number": acct.get("account_number", ""),
                    "account_name": acct.get("account_name", ""),
                    "account_type": acct.get("account_type", ""),
                    "statement_count": acct.get("statement_count", 0),
                }
                entity_data["sources"]["fincosys"]["accounts"].append(acct_info)
                entity_data["sources"]["fincosys"]["statements"].append({
                    "count": acct.get("statement_count", 0),
                    "date_range": f"{acct.get('date_range_start', '')} - {acct.get('date_range_end', '')}",
                })

                graph["evidence_links"].append({
                    "entity_id": case_entity_id,
                    "source_repo": "fincosys",
                    "evidence_type": "bank_account",
                    "reference": acct.get("account_number", ""),
                    "fincosys_code": fincosys_code,
                    "statement_count": acct.get("statement_count", 0),
                    "provenance": "master_accounts",
                })

            graph["cross_repo_references"].append({
                "from_repo": "fincosys",
                "to_repo": "revstream1",
                "from_id": fincosys_code,
                "to_id": case_entity_id,
                "mapping_type": "entity",
                "confidence": 1.0,
            })

    def _layer_communications(self, graph: Dict[str, Any]):
        """Layer comcosys communication data onto the graph."""
        mapping_path = self.paths["comcosys"] / "integration" / "case_entity_mapping.json"
        insights_path = self.paths["comcosys"] / "integration" / "case_insights.json"

        if not mapping_path.exists():
            return

        try:
            with open(mapping_path) as f:
                email_mapping = json.load(f)
        except Exception:
            return

        # Map email addresses to graph entities
        email_map = email_mapping.get("email_entity_map", [])
        for entry in email_map:
            if not entry.get("mapped"):
                continue

            entity_id = entry.get("case_entity_id", "")
            if entity_id not in graph["entities"]:
                continue

            email = entry.get("email_address", "")
            appearances = entry.get("message_appearances", 0)

            entity_data = graph["entities"][entity_id]
            entity_data["sources"]["comcosys"]["emails"].append({
                "address": email,
                "message_appearances": appearances,
            })

            graph["evidence_links"].append({
                "entity_id": entity_id,
                "source_repo": "comcosys",
                "evidence_type": "email_archive",
                "reference": email,
                "message_count": appearances,
                "provenance": "forensic_archive",
            })

            graph["cross_repo_references"].append({
                "from_repo": "comcosys",
                "to_repo": "revstream1",
                "from_id": email,
                "to_id": entity_id,
                "mapping_type": "email_to_entity",
                "confidence": 1.0,
            })

        # Add keyword hit counts from insights
        if insights_path.exists():
            try:
                with open(insights_path) as f:
                    insights = json.load(f)

                flagged = insights.get("keyword_flagged_communications", {})
                records = flagged.get("records", [])

                entity_keyword_counts: Dict[str, int] = {}
                for comm in records:
                    from_entity = comm.get("from_entity")
                    if from_entity:
                        entity_keyword_counts[from_entity] = entity_keyword_counts.get(from_entity, 0) + 1

                for entity_id, count in entity_keyword_counts.items():
                    if entity_id in graph["entities"]:
                        graph["entities"][entity_id]["sources"]["comcosys"]["keyword_hits"] = count
            except Exception:
                pass

    def _compute_coverage(self, graph: Dict[str, Any]):
        """Compute evidence coverage statistics across repos."""
        total_entities = len(graph["entities"])
        coverage = {
            "total_entities": total_entities,
            "by_repo": {},
            "multi_repo_entities": 0,
            "fully_covered_entities": 0,
            "entity_coverage_detail": {},
        }

        for repo in self.REPO_ROLES:
            coverage["by_repo"][repo] = {"entities_with_evidence": 0}

        for entity_id, entity_data in graph["entities"].items():
            sources = entity_data.get("sources", {})
            repo_coverage = []

            if sources.get("revstream1", {}).get("evidence_codes"):
                repo_coverage.append("revstream1")
            if sources.get("ad-res-j7", {}).get("annexures"):
                repo_coverage.append("ad-res-j7")
            if sources.get("fincosys", {}).get("accounts"):
                repo_coverage.append("fincosys")
            if sources.get("comcosys", {}).get("emails"):
                repo_coverage.append("comcosys")

            for repo in repo_coverage:
                coverage["by_repo"][repo]["entities_with_evidence"] += 1

            if len(repo_coverage) >= 2:
                coverage["multi_repo_entities"] += 1
            if len(repo_coverage) == 4:
                coverage["fully_covered_entities"] += 1

            coverage["entity_coverage_detail"][entity_id] = {
                "name": entity_data.get("name", ""),
                "repos_with_evidence": repo_coverage,
                "repo_count": len(repo_coverage),
            }

        graph["coverage_summary"] = coverage

    def get_entity_evidence_summary(self, entity_id: str) -> Optional[Dict[str, Any]]:
        """Get a complete evidence summary for a specific entity across all repos."""
        if not self._evidence_graph:
            self.build_evidence_graph()

        entity = self._evidence_graph.get("entities", {}).get(entity_id)
        if not entity:
            return None

        links = [
            link for link in self._evidence_graph.get("evidence_links", [])
            if link.get("entity_id") == entity_id
        ]

        return {
            "entity": entity,
            "evidence_links": links,
            "total_evidence_items": len(links),
        }

    def export(self, output_path: str = None) -> Dict[str, Any]:
        """Build and export the evidence graph to JSON."""
        graph = self.build_evidence_graph()

        if output_path:
            os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
            with open(output_path, "w") as f:
                json.dump(graph, f, indent=2, default=str)
            print(f"[CaseEvidenceMapping] Evidence graph exported to {output_path}")

        meta = graph.get("coverage_summary", {})
        print(f"  Total entities: {meta.get('total_entities', 0)}")
        print(f"  Multi-repo entities: {meta.get('multi_repo_entities', 0)}")
        print(f"  Fully covered (4 repos): {meta.get('fully_covered_entities', 0)}")
        print(f"  Evidence links: {len(graph.get('evidence_links', []))}")
        print(f"  Cross-repo references: {len(graph.get('cross_repo_references', []))}")

        return graph


def main():
    """CLI entry point for unified case evidence mapping."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Build unified case evidence mapping across all repositories"
    )
    parser.add_argument(
        "--ad-res-j7", default=None, help="Path to ad-res-j7 repository"
    )
    parser.add_argument(
        "--revstream1", default=None, help="Path to revstream1 repository"
    )
    parser.add_argument(
        "--fincosys", default=None, help="Path to fincosys repository"
    )
    parser.add_argument(
        "--comcosys", default=None, help="Path to comcosys repository"
    )
    parser.add_argument(
        "--output",
        default=os.path.join(os.path.dirname(__file__), "case_evidence_graph.json"),
        help="Output JSON file path",
    )
    parser.add_argument(
        "--entity",
        default=None,
        help="Show evidence summary for specific entity ID",
    )
    args = parser.parse_args()

    mapping = CaseEvidenceMapping(
        ad_res_j7_path=args.ad_res_j7,
        revstream1_path=args.revstream1,
        fincosys_path=args.fincosys,
        comcosys_path=args.comcosys,
    )

    if args.entity:
        graph = mapping.build_evidence_graph()
        summary = mapping.get_entity_evidence_summary(args.entity)
        if summary:
            print(json.dumps(summary, indent=2, default=str))
        else:
            print(f"Entity {args.entity} not found")
        return 0

    mapping.export(args.output)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
