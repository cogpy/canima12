# lexicog-ecosystem

Unified integration hub for the legal-cognitive ecosystem spanning five repositories.

## Repositories

| Repo | Role | Description |
|------|------|-------------|
| [cogpy/revstream1](https://github.com/cogpy/revstream1) | Data Truth | Canonical data models, schemas, and contracts |
| [cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7) | Evidence DB | Legal attention transformer and evidence repository |
| [cogpy/chainlex](https://github.com/cogpy/chainlex) | Legal Knowledge | Principles, rules, and inference chains |
| [cogpy/fincosys](https://github.com/cogpy/fincosys) | Financial Analysis | Reconciliation, cash flow, and legal evidence export |
| [o9-org/LexRexHGNN](https://github.com/o9-org/LexRexHGNN) | Integration Hub | Hypergraph neural network and pipeline orchestration |

## Structure

```
lexicog-ecosystem/
├── config/                  # Ecosystem configuration
│   ├── ecosystem.json       # Repository paths and roles
│   └── repositories.json    # Registry with cross-references
├── ../contracts/             # Shared data contracts (sibling dir in revstream1)
│   ├── entity_schema.json   # Entity JSON Schema
│   ├── relation_schema.json # Relation JSON Schema
│   ├── event_schema.json    # Event JSON Schema
│   ├── timeline_schema.json # Timeline JSON Schema
│   └── validate_contracts.py
├── bridges/                 # Cross-repo integration bridges
│   ├── chainlex/            # ChainLex export layer
│   ├── ad_res_j7/           # ChainLex-to-attention-head bridge
│   └── fincosys/            # Financial evidence exporter
└── pipeline/                # Orchestration
    ├── pipeline.py          # 5-stage LegalCasePipeline
    └── sync.py              # Multi-repo synchronizer
```

## Pipeline Stages

1. **Validate Data Contracts** — runs revstream1 schema validation
2. **Load ChainLex Knowledge** — exports principles, rules, inference chains
3. **Load Financial Evidence** — imports fincosys reconciliation and cash flow data
4. **Construct Hypergraph** — builds multi-repo hypergraph via LexRexHGNN
5. **Neuro-Symbolic Analysis** — runs LexiCog framework for case summary

## Usage

```bash
# Full pipeline
python pipeline/pipeline.py --workspace /home/user --output results.json

# Incremental (only changed repos)
python pipeline/pipeline.py --incremental chainlex fincosys

# Validate contracts
python contracts/validate_contracts.py --data-dir /path/to/data_models

# Sync data across repos
python -c "from pipeline.sync import RepositorySynchronizer; s = RepositorySynchronizer('/home/user'); s.sync_data_targeted()"
```

## Case Reference

- **Case**: 2025-137857 — Revenue Stream Hijacking
- **Total Losses**: R10,269,727.90
- **Entities**: 86 | **Events**: 130 | **Relations**: 123
