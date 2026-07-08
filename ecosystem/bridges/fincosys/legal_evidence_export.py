"""
Legal Evidence Exporter for Fincosys -> Revstream1 Integration

Converts fincosys financial analysis outputs (reconciliation reports,
cash flow analysis, counterparty networks) into revstream1-compatible
event, entity, and relation data structures for legal evidence use.
"""

import json
import os
from datetime import datetime, date
from decimal import Decimal
from typing import Any, Dict, List, Optional, Tuple
from uuid import uuid4

# Entity type mapping from fincosys to revstream1
# Based on contracts/fincosys_entity_mapping.json
FINCOSYS_TO_REVSTREAM1_ENTITY = {
    "NATURAL_PERSON": "PERSON_*",
    "ORGANIZATION": "ORG_*",
    "FINANCIAL_INSTITUTION": "BANK_*",
    "ACCOUNT": "ACCOUNT_*",
    "JURISTIC_PERSON": "ORG_*",
    "REGULATORY_BODY": "REGULATORY_*",
    "TRANSACTION": None,   # Transactions map to events, not entities
    "STATEMENT": None,     # Statements map to evidence references
}

FINCOSYS_TO_REVSTREAM1_RELATION = {
    "OWNS": "owns",
    "OPERATES": "controls",
    "TRANSACTS_WITH": "financial_transaction",
    "CREDITS": "fund_flow",
    "DEBITS": "fund_flow",
    "DIRECTOR_OF": "director_of",
    "SHAREHOLDER_OF": "shareholder_of",
    "HOLDS": "bank_account",
}

# Try to import fincosys types - optional dependency
try:
    from fincosys.fincosys.core.models import (
        ReconciliationReport,
        Discrepancy,
        NetworkGraph,
        ReconciliationStatus,
    )
    FINCOSYS_AVAILABLE = True
except ImportError:
    try:
        from fincosys.core.models import (
            ReconciliationReport,
            Discrepancy,
            NetworkGraph,
            ReconciliationStatus,
        )
        FINCOSYS_AVAILABLE = True
    except ImportError:
        FINCOSYS_AVAILABLE = False


def _serialize(obj: Any) -> Any:
    """JSON-safe serialization helper."""
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if hasattr(obj, "__dict__"):
        return {k: _serialize(v) for k, v in obj.__dict__.items()
                if not k.startswith("_")}
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple, set)):
        return [_serialize(i) for i in obj]
    return obj


def _map_entity_type(fincosys_type: str) -> str:
    """Map a fincosys entity type string to a revstream1 entity pattern."""
    pattern = FINCOSYS_TO_REVSTREAM1_ENTITY.get(fincosys_type)
    if pattern is None:
        return fincosys_type
    return pattern


def _map_relation_type(fincosys_type: str) -> str:
    """Map a fincosys relation type to a revstream1 relation type."""
    return FINCOSYS_TO_REVSTREAM1_RELATION.get(fincosys_type, fincosys_type.lower())


def _severity_to_burden(severity: str) -> str:
    """Map discrepancy severity to legal burden of proof category."""
    mapping = {
        "critical": "beyond_reasonable_doubt",
        "error": "clear_and_convincing",
        "warning": "preponderance_of_evidence",
        "info": "reasonable_suspicion",
    }
    return mapping.get(severity, "preponderance_of_evidence")


class LegalEvidenceExporter:
    """
    Exports fincosys financial analysis data as revstream1-compatible
    legal evidence structures (events, entities, relations).
    """

    def __init__(self, fincosys_instance=None):
        """
        Args:
            fincosys_instance: Optional Fincosys system instance. When
                provided, export_all() can pull data directly.
        """
        self.fincosys = fincosys_instance
        self._events: List[Dict[str, Any]] = []
        self._entities: List[Dict[str, Any]] = []
        self._relations: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    # Public conversion methods
    # ------------------------------------------------------------------

    def reconciliation_to_events(
        self, recon_report: Any
    ) -> List[Dict[str, Any]]:
        """
        Convert reconciliation discrepancies into revstream1 event dicts.

        Each discrepancy becomes an event with:
            event_id, date, event_type, description, entities_involved,
            financial_impact, evidence, burden_of_proof

        Args:
            recon_report: A ReconciliationReport (or plain dict with the
                same shape).

        Returns:
            List of revstream1-compatible event dicts.
        """
        events: List[Dict[str, Any]] = []

        # Normalise input to dict if it is a dataclass
        if hasattr(recon_report, "__dict__") and not isinstance(recon_report, dict):
            report = _serialize(recon_report)
        else:
            report = recon_report

        account_id = report.get("account_id", "unknown")
        account_name = report.get("account_name", "")
        report_id = report.get("id", str(uuid4()))
        generated_at = report.get("generated_at", datetime.utcnow().isoformat())

        discrepancies = report.get("discrepancies", [])

        # Also pull discrepancies nested inside validation results
        for field_name in ("balance_continuity", "transaction_totals"):
            vr = report.get(field_name)
            if isinstance(vr, dict):
                discrepancies.extend(vr.get("discrepancies", []))

        for disc in discrepancies:
            disc_id = disc.get("id", str(uuid4()))
            severity = disc.get("severity", "warning")

            event = {
                "event_id": f"FIN_RECON_{disc_id}",
                "date": disc.get("detected_at", generated_at),
                "event_type": "financial_discrepancy",
                "description": disc.get("description", "Reconciliation discrepancy detected"),
                "entities_involved": [
                    {"entity_id": account_id, "entity_name": account_name, "role": "account"},
                    {"entity_id": disc.get("entity_id", ""), "role": "discrepant_entity"},
                ],
                "financial_impact": {
                    "expected_value": _serialize(disc.get("expected_value")),
                    "actual_value": _serialize(disc.get("actual_value")),
                    "difference": _serialize(disc.get("difference")),
                    "discrepancy_type": disc.get("discrepancy_type", ""),
                },
                "evidence": {
                    "source": "fincosys_reconciliation",
                    "report_id": report_id,
                    "severity": severity,
                    "resolved": disc.get("resolved", False),
                    "resolution_notes": disc.get("resolution_notes"),
                },
                "burden_of_proof": _severity_to_burden(severity),
            }
            events.append(event)

        # Also create an event for sequence gaps (missing statements)
        for gap in report.get("sequence_gaps", []):
            gap_event = {
                "event_id": f"FIN_GAP_{str(uuid4())[:8]}",
                "date": _serialize(gap.get("expected_period_start", generated_at)),
                "event_type": "missing_statement",
                "description": (
                    f"Missing bank statement for account {account_id}: "
                    f"gap of {gap.get('gap_days', '?')} days"
                ),
                "entities_involved": [
                    {"entity_id": account_id, "entity_name": account_name, "role": "account"},
                ],
                "financial_impact": {
                    "gap_days": gap.get("gap_days", 0),
                    "expected_opening_balance": _serialize(
                        gap.get("expected_opening_balance")
                    ),
                },
                "evidence": {
                    "source": "fincosys_reconciliation",
                    "report_id": report_id,
                    "severity": "warning",
                },
                "burden_of_proof": "preponderance_of_evidence",
            }
            events.append(gap_event)

        self._events.extend(events)
        return events

    def cashflow_to_relations(
        self, analysis_results: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Convert cash flow analysis results into revstream1 relation dicts.

        Each significant flow becomes a relation with:
            relation_id, relation_type, source_entity, target_entity,
            financial_details, confidence

        Args:
            analysis_results: Dict from CashFlowAnalyzer (consolidated
                statement, transfer pairs, etc.).

        Returns:
            List of revstream1-compatible relation dicts.
        """
        relations: List[Dict[str, Any]] = []

        # Process detected internal transfers
        transfers = analysis_results.get("transfers", [])
        for tfr in transfers:
            if hasattr(tfr, "__dict__") and not isinstance(tfr, dict):
                tfr = _serialize(tfr)

            relation = {
                "relation_id": f"FIN_FLOW_{tfr.get('id', str(uuid4()))}",
                "relation_type": _map_relation_type("TRANSACTS_WITH"),
                "source_entity": tfr.get("source_account_id", ""),
                "target_entity": tfr.get("target_account_id", ""),
                "financial_details": {
                    "amount": _serialize(tfr.get("amount")),
                    "transfer_date": _serialize(tfr.get("transfer_date")),
                    "match_criteria": tfr.get("match_criteria", []),
                    "source_transaction_id": tfr.get("source_transaction_id", ""),
                    "target_transaction_id": tfr.get("target_transaction_id", ""),
                },
                "confidence": tfr.get("confidence", 0.0),
            }
            relations.append(relation)

        # Process consolidated flows by account
        consolidated = analysis_results.get("consolidated")
        if consolidated:
            if hasattr(consolidated, "__dict__") and not isinstance(consolidated, dict):
                consolidated = _serialize(consolidated)

            by_account = consolidated.get("by_account", {})
            for acct_id, acct_data in by_account.items():
                relation = {
                    "relation_id": f"FIN_CONSOL_{acct_id[:8]}_{str(uuid4())[:8]}",
                    "relation_type": "fund_flow",
                    "source_entity": consolidated.get("organization_id", ""),
                    "target_entity": acct_id,
                    "financial_details": {
                        "total_credits": _serialize(acct_data.get("total_credits")),
                        "total_debits": _serialize(acct_data.get("total_debits")),
                        "net_change": _serialize(acct_data.get("net_change")),
                    },
                    "confidence": 1.0,
                }
                relations.append(relation)

        # Process recurring payments if present
        recurring = analysis_results.get("recurring_payments", [])
        for rp in recurring:
            if hasattr(rp, "__dict__") and not isinstance(rp, dict):
                rp = _serialize(rp)

            relation = {
                "relation_id": f"FIN_RECUR_{rp.get('id', str(uuid4()))}",
                "relation_type": _map_relation_type("DEBITS"),
                "source_entity": rp.get("account_id", ""),
                "target_entity": rp.get("counterparty_id", rp.get("counterparty_name", "")),
                "financial_details": {
                    "amount": _serialize(rp.get("amount")),
                    "frequency": rp.get("frequency", ""),
                    "occurrence_count": rp.get("occurrence_count", 0),
                    "category": rp.get("category"),
                },
                "confidence": rp.get("confidence", 0.0),
            }
            relations.append(relation)

        self._relations.extend(relations)
        return relations

    def network_to_entities_relations(
        self, network_data: Any
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """
        Convert counterparty network data into a tuple of
        (entity_list, relation_list) for revstream1.

        Args:
            network_data: A NetworkGraph or dict with 'nodes' and 'edges'.

        Returns:
            Tuple of (entities, relations).
        """
        if hasattr(network_data, "__dict__") and not isinstance(network_data, dict):
            network_data = _serialize(network_data)

        entities: List[Dict[str, Any]] = []
        relations: List[Dict[str, Any]] = []

        # Process nodes -> entities
        for node in network_data.get("nodes", []):
            node_type = node.get("type", node.get("entity_type", "ORGANIZATION"))
            mapped_type = _map_entity_type(str(node_type).upper().replace(" ", "_"))

            entity = {
                "entity_id": node.get("id", str(uuid4())),
                "entity_type": mapped_type,
                "name": node.get("name", node.get("label", "")),
                "attributes": {
                    k: _serialize(v)
                    for k, v in node.items()
                    if k not in ("id", "type", "entity_type", "name", "label")
                },
                "source": "fincosys_network",
            }
            entities.append(entity)

        # Process edges -> relations
        for edge in network_data.get("edges", []):
            edge_type = edge.get("type", edge.get("edge_type", "TRANSACTS_WITH"))
            mapped_type = _map_relation_type(
                str(edge_type).upper().replace(" ", "_")
            )

            relation = {
                "relation_id": edge.get("id", f"FIN_NET_{str(uuid4())[:8]}"),
                "relation_type": mapped_type,
                "source_entity": edge.get("source", edge.get("source_id", "")),
                "target_entity": edge.get("target", edge.get("target_id", "")),
                "financial_details": {
                    k: _serialize(v)
                    for k, v in edge.items()
                    if k not in ("id", "type", "edge_type", "source", "target",
                                 "source_id", "target_id")
                },
                "confidence": edge.get("weight", edge.get("confidence", 1.0)),
            }
            relations.append(relation)

        self._entities.extend(entities)
        self._relations.extend(relations)
        return entities, relations

    def export_all(self, output_dir: str) -> Dict[str, str]:
        """
        Export all accumulated events, entities, and relations to JSON
        files in *output_dir*.

        If a Fincosys instance was provided at init and no data has been
        accumulated yet, attempt to pull data from the live system first.

        Returns:
            Dict mapping data type to written file path.
        """
        os.makedirs(output_dir, exist_ok=True)

        # If we have a live fincosys instance and no data yet, pull it
        if self.fincosys and not self._events and not self._relations:
            self._pull_from_fincosys()

        written: Dict[str, str] = {}

        events_path = os.path.join(output_dir, "legal_evidence_export_events.json")
        with open(events_path, "w") as f:
            json.dump(
                {"events": self._events, "exported_at": datetime.utcnow().isoformat()},
                f,
                indent=2,
                default=str,
            )
        written["events"] = events_path

        relations_path = os.path.join(output_dir, "legal_evidence_export_relations.json")
        with open(relations_path, "w") as f:
            json.dump(
                {
                    "entities": self._entities,
                    "relations": self._relations,
                    "exported_at": datetime.utcnow().isoformat(),
                },
                f,
                indent=2,
                default=str,
            )
        written["relations"] = relations_path

        print(f"[LegalEvidenceExporter] Exported {len(self._events)} events, "
              f"{len(self._entities)} entities, {len(self._relations)} relations")
        print(f"[LegalEvidenceExporter] Files written to: {output_dir}")

        return written

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _pull_from_fincosys(self):
        """Pull data from the live Fincosys instance."""
        fs = self.fincosys

        # Reconciliation reports for all organizations
        for org in fs.get_organizations():
            reports = fs.reconcile_organization(org.id)
            for _acct_id, report in reports.items():
                self.reconciliation_to_events(report)

            # Cash flow - build analysis results dict
            accounts = fs.get_accounts(org.id)
            transfers = []
            try:
                transfers = fs.detect_internal_transfers(org.id)
            except Exception:
                pass

            analysis = {
                "transfers": transfers,
                "recurring_payments": [],
            }
            for acct in accounts:
                try:
                    recurring = fs.detect_recurring_payments(acct.id)
                    analysis["recurring_payments"].extend(recurring)
                except Exception:
                    pass

            self.cashflow_to_relations(analysis)

            # Counterparty network
            try:
                network = fs.build_counterparty_network(org.id)
                self.network_to_entities_relations(network)
            except Exception:
                pass


def main():
    """CLI entry point for exporting legal evidence data."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Export fincosys financial data as revstream1 legal evidence"
    )
    parser.add_argument(
        "--output-dir",
        default=os.path.join(os.path.dirname(__file__)),
        help="Directory to write export JSON files (default: same as this script)",
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Generate sample data for testing",
    )
    args = parser.parse_args()

    exporter = LegalEvidenceExporter()

    if args.sample:
        # Generate sample data for testing / demonstration
        sample_recon = {
            "id": "sample-recon-001",
            "account_id": "ACCT_001",
            "account_name": "FNB Cheque Account",
            "generated_at": datetime.utcnow().isoformat(),
            "overall_status": "failed",
            "discrepancies": [
                {
                    "id": "disc-001",
                    "discrepancy_type": "balance_mismatch",
                    "severity": "critical",
                    "entity_id": "STMT_2024_01",
                    "expected_value": 150000.00,
                    "actual_value": 125000.00,
                    "difference": 25000.00,
                    "description": "Closing balance does not match calculated balance from transactions",
                    "detected_at": datetime.utcnow().isoformat(),
                    "resolved": False,
                }
            ],
            "sequence_gaps": [
                {
                    "account_id": "ACCT_001",
                    "expected_period_start": "2024-03-01",
                    "expected_period_end": "2024-03-31",
                    "gap_days": 31,
                    "expected_opening_balance": 125000.00,
                }
            ],
            "balance_continuity": {"discrepancies": []},
            "transaction_totals": {"discrepancies": []},
        }
        exporter.reconciliation_to_events(sample_recon)

        sample_cashflow = {
            "transfers": [
                {
                    "id": "tfr-001",
                    "source_account_id": "ACCT_001",
                    "target_account_id": "ACCT_002",
                    "amount": 50000.00,
                    "transfer_date": "2024-02-15",
                    "confidence": 0.95,
                    "match_criteria": ["amount", "date", "reference"],
                    "source_transaction_id": "TXN_001",
                    "target_transaction_id": "TXN_002",
                }
            ],
            "recurring_payments": [
                {
                    "id": "rp-001",
                    "account_id": "ACCT_001",
                    "counterparty_id": "CP_SARS",
                    "counterparty_name": "SARS",
                    "amount": 15000.00,
                    "frequency": "monthly",
                    "occurrence_count": 12,
                    "confidence": 0.9,
                    "category": "tax",
                }
            ],
        }
        exporter.cashflow_to_relations(sample_cashflow)

        sample_network = {
            "nodes": [
                {"id": "ORG_001", "type": "organization", "name": "Acme Holdings"},
                {"id": "BANK_FNB", "type": "financial_institution", "name": "FNB"},
                {"id": "CP_SARS", "type": "regulatory_body", "name": "SARS"},
            ],
            "edges": [
                {
                    "id": "edge-001",
                    "type": "TRANSACTS_WITH",
                    "source": "ORG_001",
                    "target": "CP_SARS",
                    "weight": 0.9,
                    "total_volume": 180000.00,
                }
            ],
        }
        exporter.network_to_entities_relations(sample_network)

    paths = exporter.export_all(args.output_dir)
    for kind, path in paths.items():
        print(f"  {kind}: {path}")


if __name__ == "__main__":
    main()
