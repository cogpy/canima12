#!/usr/bin/env python3
"""
Data Contract Validator

Validates revstream1 data model files against the shared JSON Schema contracts.
Can also be used by other repos to validate their data against these schemas.

Usage:
    python validate_contracts.py                    # Validate revstream1 data
    python validate_contracts.py --data-dir /path   # Validate data from another repo
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    from jsonschema import validate, ValidationError, Draft202012Validator
except ImportError:
    print("jsonschema not installed. Install with: pip install jsonschema")
    print("Falling back to basic structure validation...")
    Draft202012Validator = None


CONTRACTS_DIR = Path(__file__).parent
DEFAULT_DATA_DIR = CONTRACTS_DIR.parent / "data_models"

SCHEMA_FILE_MAP = {
    "entities": ("entities/entities.json", "entity_schema.json"),
    "events": ("events/events.json", "event_schema.json"),
    "relations": ("relations/relations.json", "relation_schema.json"),
    "timelines": ("timelines/timeline.json", "timeline_schema.json"),
}


def load_json(path: Path) -> dict:
    """Load and parse a JSON file."""
    with open(path, "r") as f:
        return json.load(f)


def validate_basic(data: dict, model_name: str) -> List[str]:
    """Basic structure validation when jsonschema is not available."""
    errors = []

    if model_name == "entities":
        if "metadata" not in data:
            errors.append("Missing 'metadata' key")
        if "entities" not in data:
            errors.append("Missing 'entities' key")
        else:
            entities = data["entities"]
            for person in entities.get("persons", []):
                if "entity_id" not in person:
                    errors.append(f"Person missing entity_id: {person.get('name', '?')}")
                if "name" not in person:
                    errors.append(f"Person missing name: {person.get('entity_id', '?')}")

            for org in entities.get("organizations", []):
                if "entity_id" not in org:
                    errors.append(f"Organization missing entity_id: {org.get('name', '?')}")
                if "name" not in org:
                    errors.append(f"Organization missing name: {org.get('entity_id', '?')}")

    elif model_name == "events":
        if "metadata" not in data:
            errors.append("Missing 'metadata' key")
        if "events" not in data:
            errors.append("Missing 'events' key")
        else:
            for event in data["events"]:
                if "event_id" not in event:
                    errors.append(f"Event missing event_id")
                if "date" not in event:
                    errors.append(f"Event missing date: {event.get('event_id', '?')}")
                if "entities_involved" not in event:
                    errors.append(f"Event missing entities_involved: {event.get('event_id', '?')}")

    elif model_name == "relations":
        if "metadata" not in data:
            errors.append("Missing 'metadata' key")
        if "relations" not in data:
            errors.append("Missing 'relations' key")
        else:
            for rel_type, rel_list in data["relations"].items():
                if isinstance(rel_list, list):
                    for rel in rel_list:
                        if "relation_id" not in rel:
                            errors.append(f"Relation missing relation_id in {rel_type}")
                        has_source = "source_entity" in rel or "from_entity" in rel
                        has_target = "target_entity" in rel or "to_entity" in rel
                        if not has_source or not has_target:
                            errors.append(
                                f"Relation {rel.get('relation_id', '?')} missing source/target entities"
                            )

    elif model_name == "timelines":
        if "metadata" not in data:
            errors.append("Missing 'metadata' key")
        if "timeline" not in data:
            errors.append("Missing 'timeline' key")
        else:
            for entry in data["timeline"]:
                if "date" not in entry:
                    errors.append("Timeline entry missing date")
                if "event" not in entry:
                    errors.append("Timeline entry missing event")

    return errors


def validate_with_schema(data: dict, schema: dict) -> List[str]:
    """Validate data against JSON Schema."""
    errors = []
    validator = Draft202012Validator(schema)
    for error in validator.iter_errors(data):
        path = " -> ".join(str(p) for p in error.absolute_path) if error.absolute_path else "root"
        errors.append(f"[{path}] {error.message}")
    return errors


def validate_all(data_dir: Path) -> Tuple[int, int]:
    """Validate all data models. Returns (passed, failed) counts."""
    passed = 0
    failed = 0

    for model_name, (data_rel_path, schema_filename) in SCHEMA_FILE_MAP.items():
        data_path = data_dir / data_rel_path
        schema_path = CONTRACTS_DIR / schema_filename

        if not data_path.exists():
            print(f"  SKIP  {model_name}: data file not found at {data_path}")
            continue

        data = load_json(data_path)

        if Draft202012Validator and schema_path.exists():
            schema = load_json(schema_path)
            errors = validate_with_schema(data, schema)
        else:
            errors = validate_basic(data, model_name)

        if errors:
            print(f"  FAIL  {model_name} ({len(errors)} errors)")
            for err in errors[:10]:
                print(f"         - {err}")
            if len(errors) > 10:
                print(f"         ... and {len(errors) - 10} more errors")
            failed += 1
        else:
            print(f"  PASS  {model_name}")
            passed += 1

    return passed, failed


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Validate data models against contracts")
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=DEFAULT_DATA_DIR,
        help="Directory containing data model files",
    )
    args = parser.parse_args()

    print(f"Validating data contracts...")
    print(f"Data directory: {args.data_dir}")
    print(f"Contracts directory: {CONTRACTS_DIR}")
    print()

    passed, failed = validate_all(args.data_dir)

    print()
    print(f"Results: {passed} passed, {failed} failed")

    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
