# SA Entity Intelligence (`sa-entity-intel`)

This skill provides a comprehensive pipeline for gathering, resolving, and analyzing intelligence on South African juristic entities. It orchestrates multiple data sources to build a unified, cross-referenced master record for any given company, close corporation, or trust.

The pipeline is designed for deep forensic analysis, due diligence, and building a complete picture of an entity's structure, history, tax status, and relationships. It is a core component of the `regima-cognitive-ai` framework, feeding structured data into the organizational memory systems.

## Key Capabilities

- **Multi-Source Aggregation**: Chains together five key data sources for maximum coverage.
- **Entity Resolution**: Matches records across sources using registration numbers and fuzzy name matching.
- **VAT & CIPC Cross-Referencing**: Links SARS VAT trading names to official CIPC registered legal names.
- **Director & Officer Mapping**: Identifies directors, members, and officers and maps their relationships across other entities.
- **Anomaly Detection**: Automatically flags discrepancies between data sources (e.g., name mismatches, status changes).
- **Database Integration**: Syncs the consolidated master data to Neon (PostgreSQL) and Supabase for persistent storage and further analysis.
- **Portable Credentials**: Includes necessary credentials for database sync operations, making the skill self-contained and portable.

## Data Sources

The pipeline integrates the following sources in a specific sequence to build up the entity profile:

| Order | Source | Website | Scope | Method |
|---|---|---|---|---|
| 1 | **SA Company** | `sacompany.co.za` | Current CIPC registration data (name, reg number, type, status) | Scraper (Python `requests`) |
| 2 | **Companies SA** | `companies-southafrica.com` | Historical CIPC records (pre-2013), status history, SIC codes | Scraper (Python `requests`) |
| 3 | **VAT Search** | `vatsearch.co.za` | SARS VAT registration data (trading name, VAT number, office) | Scraper (Python `requests`) |
| 4 | **B2BHint** | `b2bhint.com` | Directors, officers, related entities (by address/officer) | Browser Automation (Playwright MCP) |
| 5 | **BizPortal** | `bizportal.gov.za` | Official CIPC portal for deep verification (100/day limit) | Browser Automation (Future) |

## Core Workflow (`entity_intel_pipeline.py`)

The primary entry point is the `entity_intel_pipeline.py` script, which orchestrates the entire process.

```bash
# Run the full pipeline for a given keyword and save results
python scripts/entity_intel_pipeline.py search "Regima" --output /tmp/regima_intel.json

# Run the pipeline and sync results to all configured databases
python scripts/entity_intel_pipeline.py search "Regima" --sync

# Initialize the database schema in Neon
python scripts/entity_intel_pipeline.py init-db --target neon

# Sync a local JSON file to Supabase
python scripts/entity_intel_pipeline.py sync --input /tmp/regima_intel.json --target supabase
```

### Pipeline Stages

1.  **Stage 1: `sacompany_search`**: Fetches a baseline list of current CIPC-registered entities matching the keyword.
2.  **Stage 2: `historical_search`**: Augments the list with historical data, matching by registration number.
3.  **Stage 3: `vat_search`**: Gathers all related VAT registrations and uses fuzzy matching to link them to the CIPC entities.
4.  **Stage 4: `b2bhint_urls`**: Generates the specific URLs needed to scrape director and related-party information from b2bhint.com. The actual scraping requires browser automation and is handled by the `workflow-creator` generated workflow.
5.  **Stage 5: `detect_anomalies`**: Compares data across all sources for each entity and flags inconsistencies, such as a VAT trading name that doesn't match the legal name.

## Database Schema

The skill uses a comprehensive relational schema to store the aggregated data. The full schema is defined in `references/schema.md`. Key tables include:

- `juristic_entities`: The master table for all companies.
- `natural_persons`: Directors, members, and other related individuals.
- `entity_person_roles`: Links persons to entities with their specific role and tenure.
- `entity_relationships`: Defines inter-company relationships (e.g., parent-subsidiary).
- `entity_events`: A timeline of all significant events for an entity.
- `source_records`: Stores the raw data from each source for auditability.

## Integration with `regima-cognitive-ai`

This skill is a foundational data ingestion module for the `regima-cognitive-ai` and `regimai-orgself-fabric` systems. The structured entity data populates the AtomSpace cognitive graph, providing the ground truth for organizational self-awareness, knowledge construction, and pattern mining (MOSES).

The `juristic_entities` table includes fields for `atomspace_handle` and `attention_sti`/`attention_lti` to directly integrate with the ECAN attention mechanism.

## Usage in Workflows

When used with `/workflow-creator`, this skill can be chained to perform end-to-end investigations. A typical workflow would be:

1.  **Input**: A partial company name or keyword.
2.  **Execute**: `entity_intel_pipeline.py search "{{keyword}}"` to get a JSON output of resolved entities.
3.  **Iterate**: For each entity in the JSON with a `b2bhint_url`:
    a. Use a browser automation tool (e.g., Playwright MCP) to navigate to the URL and save the HTML.
    b. Execute `b2bhint_search.py parse "{{html_file_path}}"` to extract director and relationship data.
    c. Merge the new data back into the main JSON record.
4.  **Sync**: Execute `entity_intel_pipeline.py sync --input "{{final_json_path}}" --target all` to push the complete, enriched data to all databases.

This creates a powerful, automated due diligence and corporate intelligence gathering system.
