"""
Communication Evidence Bridge: comcosys -> revstream1

Converts comcosys forensic email archive data (entity mappings,
keyword-flagged communications, communication patterns) into
revstream1-compatible evidence structures for legal case integration.

Establishes temporal correlations between email communications and
case events from revstream1's event model.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# Entity mapping from comcosys email addresses to revstream1 entity IDs
# Sourced from comcosys/integration/case_entity_mapping.json
EMAIL_TO_ENTITY = {
    "jax@regima.zone": "PERSON_004",
    "jax@regima.com": "PERSON_004",
    "dan@regima.zone": "PERSON_005",
    "dan@regima.com": "PERSON_005",
    "pete@regima.com": "PERSON_001",
    "rynette@regima.zone": "PERSON_002",
    "danie.bantjes@gmail.com": "PERSON_007",
    "kay@regima.com": "PERSON_008",
    "kent@regima.zone": "PERSON_037",
    "trev@regima.com": "STAFF_TREV",
    "emma@regima.com": "STAFF_EMMA",
    "vickyb@regima.zone": "STAFF_VICKY",
    "karenm@regima.zone": "STAFF_KAREN",
}

# Service email addresses that map to organizational entities
SERVICE_EMAIL_TO_ENTITY = {
    "info@regima.com": "ORG_001",
    "info@regimaskincare.com": "ORG_002",
    "org@regima.zone": "ORG_003",
    "uk@regima.zone": "ORG_003",
    "fin@regima.zone": "ORG_001",
    "mailer@shopify.com": "PLATFORM_001",
    "incontact@fnb.co.za": "BANK_FNB",
}

# Forensic keywords organized by evidence category
KEYWORD_CATEGORIES = {
    "financial_fraud": ["fabricat", "fraud", "theft", "unauthorized", "forged"],
    "tax_compliance": ["sars", "vat", "tax", "audit", "provisional"],
    "banking": ["fnb", "bank", "account", "statement", "debit order", "credit"],
    "accounting": ["sage", "xero", "balance", "trial balance", "journal", "financial"],
    "revenue": ["shopify", "revenue", "sales", "invoice", "payment"],
    "trust_related": ["trust", "trustee", "beneficiary", "estate"],
    "payroll": ["payroll", "salary", "salaries"],
}

# Case phases mapped to date ranges (from revstream1 timeline)
CASE_PHASES = {
    "phase_1_foundation": ("2025-03-01", "2025-03-30"),
    "phase_2_initial_theft": ("2025-04-01", "2025-04-14"),
    "phase_3_escalation": ("2025-05-02", "2025-05-29"),
    "phase_4_consolidation": ("2025-06-06", "2025-06-30"),
    "phase_5_control_seizure": ("2025-07-08", "2025-07-25"),
    "phase_6_cover_up": ("2025-08-10", "2025-09-11"),
    "phase_7_duress": ("2025-09-18", "2025-09-22"),
}


class CommunicationEvidenceBridge:
    """
    Bridges comcosys forensic email archive with revstream1 case data.

    Provides:
    - Temporal correlation between emails and case events
    - Entity communication pattern analysis for foreknowledge evidence
    - Keyword-flagged email -> case evidence mapping
    - Communication chain reconstruction for conspiracy proof
    """

    def __init__(self, comcosys_path: str, revstream1_path: str = None):
        self.comcosys_path = Path(comcosys_path)
        self.revstream1_path = Path(revstream1_path) if revstream1_path else None
        self._entity_mapping: Dict[str, Any] = {}
        self._case_insights: Dict[str, Any] = {}
        self._events: List[Dict[str, Any]] = []
        self._loaded = False

    def load(self) -> bool:
        """Load comcosys integration data and optionally revstream1 events."""
        try:
            mapping_path = self.comcosys_path / "integration" / "case_entity_mapping.json"
            if mapping_path.exists():
                with open(mapping_path) as f:
                    self._entity_mapping = json.load(f)

            insights_path = self.comcosys_path / "integration" / "case_insights.json"
            if insights_path.exists():
                with open(insights_path) as f:
                    self._case_insights = json.load(f)

            if self.revstream1_path:
                events_path = self.revstream1_path / "data_models" / "events.json"
                if events_path.exists():
                    with open(events_path) as f:
                        data = json.load(f)
                        self._events = data.get("events", data) if isinstance(data, dict) else data

            self._loaded = True
            return True
        except Exception as e:
            print(f"[ComcosysBridge] Error loading data: {e}")
            return False

    def correlate_communications_with_events(
        self, window_days: int = 7
    ) -> List[Dict[str, Any]]:
        """
        Find communications that occur within ±window_days of case events.

        Returns list of temporal correlations linking emails to events,
        which can serve as evidence of foreknowledge or coordination.
        """
        if not self._loaded:
            self.load()

        correlations = []
        flagged = self._case_insights.get("keyword_flagged_communications", {})
        records = flagged.get("records", [])

        for event in self._events:
            event_date_str = event.get("date", "")
            if not event_date_str:
                continue
            try:
                event_date = datetime.strptime(event_date_str[:10], "%Y-%m-%d")
            except (ValueError, TypeError):
                continue

            event_id = event.get("event_id", "")
            event_title = event.get("title", event.get("description", ""))

            for comm in records:
                comm_date_str = comm.get("received_date", "")
                if not comm_date_str:
                    continue
                try:
                    comm_date = datetime.strptime(comm_date_str[:10], "%Y-%m-%d")
                except (ValueError, TypeError):
                    continue

                delta = abs((comm_date - event_date).days)
                if delta <= window_days:
                    from_entity = comm.get("from_entity")
                    correlation = {
                        "event_id": event_id,
                        "event_title": event_title,
                        "event_date": event_date_str,
                        "communication": {
                            "date": comm_date_str,
                            "subject": comm.get("subject", ""),
                            "from": comm.get("from", ""),
                            "from_entity": from_entity,
                            "keywords": comm.get("keywords", []),
                            "platform": comm.get("platform", ""),
                        },
                        "temporal_delta_days": delta,
                        "direction": "before" if comm_date < event_date else (
                            "same_day" if delta == 0 else "after"
                        ),
                        "evidence_type": "temporal_correlation",
                        "foreknowledge_indicator": (
                            comm_date < event_date and from_entity in (
                                "PERSON_001", "PERSON_002", "PERSON_007"
                            )
                        ),
                    }
                    correlations.append(correlation)

        correlations.sort(key=lambda c: (c["event_id"], c["temporal_delta_days"]))
        return correlations

    def extract_entity_pair_evidence(self) -> List[Dict[str, Any]]:
        """
        Extract communication patterns between entity pairs as evidence
        of coordination/conspiracy for revstream1 relation model.
        """
        if not self._loaded:
            self.load()

        patterns = self._case_insights.get("communication_patterns", {})
        top_pairs = patterns.get("top_entity_pairs", [])

        relations = []
        for pair in top_pairs:
            entity_a = pair.get("entity_a", pair.get("entity_1", ""))
            entity_b = pair.get("entity_b", pair.get("entity_2", ""))
            count = pair.get("message_count", pair.get("count", 0))
            subjects = pair.get("sample_subjects", pair.get("subjects", []))

            # Determine if this pair involves Tier A conspirators
            tier_a = {"PERSON_001", "PERSON_002", "PERSON_007"}
            involves_conspirator = entity_a in tier_a or entity_b in tier_a
            both_conspirators = entity_a in tier_a and entity_b in tier_a

            relation = {
                "relation_id": f"COMM_PAIR_{entity_a}_{entity_b}",
                "relation_type": "communication_pattern",
                "source_entity": entity_a,
                "target_entity": entity_b,
                "evidence": {
                    "source": "comcosys_forensic_archive",
                    "message_count": count,
                    "sample_subjects": subjects[:5] if subjects else [],
                },
                "conspiracy_indicator": both_conspirators,
                "foreknowledge_relevance": involves_conspirator,
                "confidence": min(1.0, count / 50),  # normalize to 0-1
            }
            relations.append(relation)

        return relations

    def map_emails_to_annexures(self) -> Dict[str, List[str]]:
        """
        Map comcosys email evidence to ad-res-j7 annexure references.

        Returns dict mapping email subjects/senders to potential annexure matches.
        """
        annexure_keywords = {
            "JF01": ["shopify", "plus", "email"],
            "JF04": ["cipc", "company", "registration"],
            "JF07": ["financial", "transaction", "bank", "statement"],
            "JF08": ["email", "correspondence", "fraud"],
            "JF09": ["court", "order", "timeline"],
            "JF10": ["director", "loan", "account"],
            "SF1": ["bantjies", "debt", "loan"],
            "SF2": ["sage", "screenshot", "rynette"],
            "SF4": ["sars", "audit", "tax"],
            "SF5": ["adderory", "registration"],
            "SF6": ["kayla", "estate"],
            "SF10": ["fnb", "fraud", "letter"],
        }

        flagged = self._case_insights.get("keyword_flagged_communications", {})
        records = flagged.get("records", [])

        email_annexure_map = {}
        for comm in records:
            subject = (comm.get("subject", "") or "").lower()
            keywords = comm.get("keywords", [])
            all_terms = subject.split() + keywords

            matched_annexures = []
            for annexure, terms in annexure_keywords.items():
                if any(t in all_terms for t in terms):
                    matched_annexures.append(annexure)

            if matched_annexures:
                key = f"{comm.get('received_date', '')}|{comm.get('from', '')}|{comm.get('subject', '')}"
                email_annexure_map[key] = matched_annexures

        return email_annexure_map

    def classify_communications_by_phase(self) -> Dict[str, List[Dict[str, Any]]]:
        """Classify keyword-flagged communications into case phases."""
        if not self._loaded:
            self.load()

        phase_comms: Dict[str, List[Dict[str, Any]]] = {
            phase: [] for phase in CASE_PHASES
        }
        phase_comms["pre_case"] = []
        phase_comms["post_case"] = []

        flagged = self._case_insights.get("keyword_flagged_communications", {})
        records = flagged.get("records", [])

        for comm in records:
            comm_date_str = comm.get("received_date", "")
            if not comm_date_str:
                continue
            try:
                comm_date = datetime.strptime(comm_date_str[:10], "%Y-%m-%d")
            except (ValueError, TypeError):
                continue

            placed = False
            for phase_name, (start_str, end_str) in CASE_PHASES.items():
                start = datetime.strptime(start_str, "%Y-%m-%d")
                end = datetime.strptime(end_str, "%Y-%m-%d")
                if start <= comm_date <= end:
                    phase_comms[phase_name].append(comm)
                    placed = True
                    break

            if not placed:
                if comm_date < datetime.strptime("2025-03-01", "%Y-%m-%d"):
                    phase_comms["pre_case"].append(comm)
                else:
                    phase_comms["post_case"].append(comm)

        return phase_comms

    def generate_evidence_export(self) -> Dict[str, Any]:
        """
        Generate a complete evidence export for revstream1 integration.

        Returns structured data compatible with revstream1's data model:
        - events: temporal correlations as evidence events
        - relations: communication patterns as entity relations
        - evidence_map: email-to-annexure cross-references
        """
        if not self._loaded:
            self.load()

        correlations = self.correlate_communications_with_events()
        pair_evidence = self.extract_entity_pair_evidence()
        annexure_map = self.map_emails_to_annexures()
        phase_classification = self.classify_communications_by_phase()

        # Convert correlations to revstream1-compatible events
        correlation_events = []
        for corr in correlations:
            if corr.get("foreknowledge_indicator"):
                event = {
                    "event_id": f"COMM_CORR_{corr['event_id']}_{corr['communication']['date']}",
                    "date": corr["communication"]["date"],
                    "event_type": "communication_correlation",
                    "description": (
                        f"Communication from {corr['communication']['from_entity']} "
                        f"({corr['communication']['subject']}) occurred "
                        f"{corr['temporal_delta_days']} days {corr['direction']} "
                        f"event {corr['event_id']}: {corr['event_title']}"
                    ),
                    "entities_involved": [
                        {"entity_id": corr["communication"]["from_entity"], "role": "sender"},
                    ],
                    "evidence": {
                        "source": "comcosys_temporal_correlation",
                        "correlated_event": corr["event_id"],
                        "keywords": corr["communication"]["keywords"],
                        "platform": corr["communication"]["platform"],
                    },
                    "foreknowledge_indicator": True,
                    "burden_of_proof": "preponderance_of_evidence",
                }
                correlation_events.append(event)

        phase_stats = {
            phase: len(comms) for phase, comms in phase_classification.items()
        }

        return {
            "metadata": {
                "generated_at": datetime.utcnow().isoformat() + "Z",
                "source": "comcosys_communication_evidence_bridge",
                "case_number": "2025-137857",
                "total_correlations": len(correlations),
                "foreknowledge_indicators": len(correlation_events),
                "entity_pair_relations": len(pair_evidence),
                "annexure_cross_references": len(annexure_map),
            },
            "temporal_correlations": correlations,
            "foreknowledge_events": correlation_events,
            "entity_pair_relations": pair_evidence,
            "email_annexure_map": annexure_map,
            "phase_statistics": phase_stats,
        }


def main():
    """CLI entry point for comcosys evidence bridge."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Bridge comcosys forensic email data to revstream1 case evidence"
    )
    parser.add_argument(
        "--comcosys-path",
        default=os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "comcosys"),
        help="Path to comcosys repository",
    )
    parser.add_argument(
        "--revstream1-path",
        default=os.path.join(os.path.dirname(__file__), "..", ".."),
        help="Path to revstream1 repository",
    )
    parser.add_argument(
        "--output",
        default=os.path.join(os.path.dirname(__file__), "communication_evidence_export.json"),
        help="Output JSON file path",
    )
    args = parser.parse_args()

    bridge = CommunicationEvidenceBridge(args.comcosys_path, args.revstream1_path)
    if not bridge.load():
        print("[ComcosysBridge] Failed to load data")
        return 1

    export = bridge.generate_evidence_export()

    with open(args.output, "w") as f:
        json.dump(export, f, indent=2, default=str)

    meta = export["metadata"]
    print(f"[ComcosysBridge] Evidence export written to {args.output}")
    print(f"  Temporal correlations: {meta['total_correlations']}")
    print(f"  Foreknowledge indicators: {meta['foreknowledge_indicators']}")
    print(f"  Entity pair relations: {meta['entity_pair_relations']}")
    print(f"  Annexure cross-references: {meta['annexure_cross_references']}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
