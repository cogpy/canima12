---
name: sa-vat-search
description: Search and retrieve South African company VAT registration information from the vatsearch.co.za website. Use for finding VAT numbers by trading name, or verifying existing VAT numbers. Triggers on requests for SA VAT search, SARS VAT lookup, or scraping vatsearch.co.za.
---

# South African VAT Search

This skill provides tools to search and retrieve company VAT registration data from the `vatsearch.co.za` website. It is useful for verifying a company's VAT status with the South African Revenue Service (SARS) or finding a VAT number when only a trading name is known.

## Key Capabilities

- **Search by Name**: Find VAT-registered companies using a trading name (minimum 5 characters).
- **Verify by Number**: Confirm the details of a specific 10-digit VAT number.

**Note**: This skill scrapes the public `vatsearch.co.za` website. It does not provide CIPC company registration details directly, but results include a link to an external CIPC search for convenience.

## Bundled Resources

- **`scripts/vat_search.py`**: The core Python script for scraping the website.
- **`references/data_model.md`**: Documentation on the `VATResult` data model and integration with other skills like `sa-company-lookup` and `cipchub`.

## Workflow: How to Use

All operations are performed using the `vat_search.py` script. The script has two main commands: `search` and `verify`.

### 1. Search by Trading Name

To find a company's VAT details using its trading name, use the `search` command. The name must be at least 5 characters long.

```bash
# Usage: python scripts/vat_search.py search "<trading_name>"

# Example
python /home/ubuntu/skills/sa-vat-search/scripts/vat_search.py search "Regima"
```

Example output:
```
Found 4 VAT result(s) for 'Regima':
──────────────────────────────────────────────────────────────────────
  Trading Name                             VAT Number     Office
──────────────────────────────────────────────────────────────────────
  REGIMA                                   4260223906     JOHANNESBURG
  REGIMA SKIN TREATMENTS                   4590131043     GERMISTON
  REGIMA SKIN TREATMENTS CAPE TOWN         4540228550     CAPE TOWN
  REGIMA WORLDWIDE DISTRIBUTION            4320262621     JOHANNESBURG
──────────────────────────────────────────────────────────────────────
```

### 2. Verify a VAT Number

To confirm the details of a specific VAT number, use the `verify` command. The number must be 10 digits and start with "4".

```bash
# Usage: python scripts/vat_search.py verify "<vat_number>"

# Example
python /home/ubuntu/skills/sa-vat-search/scripts/vat_search.py verify "4260223906"
```

Example output:
```
Found 1 VAT result(s) for '4260223906':
──────────────────────────────────────────────────────────────────────
  Trading Name                             VAT Number     Office
──────────────────────────────────────────────────────────────────────
  REGIMA                                   4260223906     JOHANNESBURG
──────────────────────────────────────────────────────────────────────
```

### Outputting as JSON

Both commands support a `--json` flag to output the results in structured JSON format, which is useful for programmatic use. You can also save the output directly to a file with the `--output` flag.

```bash
# Example: Save search results to a JSON file
python /home/ubuntu/skills/sa-vat-search/scripts/vat_search.py search "Shoprite" --json --output /home/ubuntu/shoprite_vat.json
```

## Data Model and Integration

The data scraped from the website is returned in a structured format. For details on the data model and how to integrate these results with other skills like `sa-company-lookup` and `cipchub`, consult the reference file.

To view the data model documentation, read the following file:

```bash
cat /home/ubuntu/skills/sa-vat-search/references/data_model.md
```
