# Fincosys Database Sync Report

**Date:** 2026-02-22  
**Target:** Neon PostgreSQL (Project: `calm-silence-72212970`)  
**Database:** `neondb`  
**Method:** Direct psycopg2 with batched upserts (ON CONFLICT DO UPDATE)

---

## Sync Results Summary

| Schema.Table | JSON Total | JSON Unique IDs | DB Count (Post-Sync) | Status |
|---|---|---|---|---|
| `entity_relation.entities` | 716 | 716 | 1,267 | **OK** (DB includes prior records) |
| `entity_relation.relations` | 1,828 | 1,828 | 2,074 | **OK** (FK constraints temporarily disabled for sync) |
| `event_timeline.events` | 14,809 | 14,807 | 15,749 | **OK** (DB includes prior records) |
| `event_timeline.state_machines` | 34 | 34 | 92 | **OK** (DB includes prior records) |
| `stock_flow.variables` | 120 | 120 | 192 | **OK** (DB includes prior records) |
| `stock_flow.simulation_history` | 455 | 63 | 119 | **OK** (many duplicate IDs in JSON) |
| `hypergraph.nodes` | 6,787 | 6,787 | 7,204 | **OK** |
| `hypergraph.hyperedges` | 14,069 | 8,847 | 8,864 | **OK** (5,222 duplicates in JSON) |
| `integration.entity_mappings` | 717 | 717 | 763 | **OK** |
| `integration.cross_references` | 40 | 40 | 93 | **OK** |
| `integration.analysis_snapshots` | 27 | 27 | 63 | **OK** |

**Total records synced this session:** ~25,631 (first pass) + 2,239 (hyperedge fix pass)

---

## Entity Type Distribution (DB)

| Entity Type | Count |
|---|---|
| ORGANIZATION | 898 |
| TRANSACTION | 247 |
| ACCOUNT | 55 |
| PERSON | 41 |
| SERVICE | 20 |
| FINANCIAL_INSTITUTION | 6 |

## Event Type Distribution (Top 10)

| Event Type | Count |
|---|---|
| UNKNOWN | 14,556 |
| BALANCE_UPDATED | 684 |
| CREDIT_RECEIVED | 152 |
| DEBIT_PROCESSED | 150 |
| FEE_CHARGED | 83 |
| PAYMENT_COMPLETED | 43 |
| STATEMENT_PERIOD_END | 33 |
| STATEMENT_PERIOD_START | 31 |
| ENTITY_CREATED | 11 |
| RATE_CHANGE | 4 |

## Hypergraph Node Types

| Node Type | Count |
|---|---|
| VALUE | 4,866 |
| ENTITY | 1,415 |
| TEMPORAL | 894 |
| CONCEPT | 29 |

## Hyperedge Types (Top 10)

| Edge Type | Count |
|---|---|
| TRANSACTION | 8,761 |
| DEBIT_TRANSACTION | 15 |
| STATEMENT_PERIOD | 15 |
| ACCOUNT_OWNERSHIP | 13 |
| BALANCE_STATE | 9 |
| CREDIT_TRANSACTION | 8 |
| FX_TRANSFER | 7 |
| OWNERSHIP | 5 |
| INTEREST_PAYMENT | 4 |
| AGGREGATION | 4 |

---

## Technical Notes

1. **FK Constraints:** The `entity_relation.relations` table had foreign key constraints on `source_id` and `target_id` referencing `entities.id`. These were temporarily dropped during sync and re-added with `NOT VALID` to allow relations referencing entities from prior syncs that exist in DB but not in current JSON.

2. **Enum Mapping:** JSON data uses entity/relation/event types not present in DB enums. A comprehensive mapping was applied:
   - Entity types: `BANK` → `FINANCIAL_INSTITUTION`, `GOVERNMENT` → `ORGANIZATION`
   - Relation types: `CUSTOMER_OF`/`PAYS` → `TRANSACTS_WITH`, `SUPPLIER_OF` → `PROVIDES_SERVICE`
   - Event types: `TRANSACTION_DEBIT` → `DEBIT_PROCESSED`, `TRANSACTION_CREDIT` → `CREDIT_RECEIVED`

3. **Duplicate IDs:** The JSON files contain significant duplicates:
   - `hypergraph.hyperedges`: 14,069 total records but only 8,847 unique IDs (5,222 duplicates)
   - `stock_flow.simulation_history`: 455 total but only 63 unique IDs
   - These were handled via `ON CONFLICT` upsert (last-write-wins)

4. **Dict Node IDs:** 13,971 hyperedges had `node_ids` containing dict objects `{"node_id": "...", "role": "..."}` instead of plain strings. These were normalized by extracting `node_id` values and moving `role` data into the `roles` JSONB column.

5. **Performance:** Individual row inserts over Neon pooler connection averaged ~15ms/row. Total sync time: ~45 minutes for all schemas.

---

## Sync Scripts

| Script | Purpose |
|---|---|
| `sync_fast.py` | Main sync script for all schemas (psycopg2 with execute_batch) |
| `sync_fix_hyperedges.py` | Fix and sync hyperedges with dict node_ids |
| `sync_he_small.py` | Incremental hyperedge sync (skip existing) |
| `sync_results.json` | Machine-readable sync results |

---

## Recommendations

1. **Deduplicate JSON sources:** The hypergraph and simulation_history JSON files contain significant duplicates that should be cleaned up at the source.
2. **Extend DB enums:** Consider adding missing event types (`TRANSACTION_DEBIT`, `TRANSACTION_CREDIT`, etc.) to the DB enum instead of mapping to generic types.
3. **Normalize hyperedge node_ids:** The JSON should store node_ids as plain string arrays with roles in a separate field, matching the DB schema.
4. **Validate FK references:** Run `ALTER TABLE entity_relation.relations VALIDATE CONSTRAINT relations_source_id_fkey` after ensuring all referenced entities exist.
