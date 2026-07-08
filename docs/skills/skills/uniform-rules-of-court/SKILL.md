---
name: uniform-rules-of-court
description: Provides access to the Uniform Rules of Court for South African High Court proceedings. Use for legal research, case analysis, and drafting legal documents that require citation or understanding of specific court rules (e.g., applications, ex parte orders, discovery, contempt of court). Integrates with sa-entity-intel for entity-specific legal context.
---

# Uniform Rules of Court (South Africa)

This skill provides a comprehensive, searchable, and structured interface to the Uniform Rules of Court, which govern the conduct of proceedings in the Provincial and Local Divisions of the High Court of South Africa. It is an essential tool for legal research, drafting court documents, and understanding procedural requirements in litigation.

This skill is based on the SAFLII consolidated version of the rules, updated to **30 January 2026**.

## Key Capabilities

- **Full-Text Search**: Search the complete text of all 92 rules and associated forms.
- **Structured Access**: Directly access specific rules by number.
- **Key Rule Extraction**: Provides quick access to the most commonly used rules in commercial and civil litigation.
- **Integration with Entity Intelligence**: Can be used in conjunction with `sa-entity-intel` to apply procedural knowledge in the context of specific companies or individuals.

## Bundled Resources

- **`references/key_rules.md`**: A Markdown file containing the full, cleaned text of 12 key rules most relevant to the case context, including Rule 6 (Applications), Rule 30 (Irregular Proceedings), and Rule 42 (Rescission of Orders).
- **`references/all_rules.json`**: A JSON file containing the extracted text of all 92 rules, indexed by rule number.
- **`scripts/search_rules.py`**: A Python script to search and retrieve rule text programmatically.

## Workflow: How to Use

### 1. Read Key Rules

For the most common procedural questions (applications, discovery, contempt), start by reading the curated key rules file. This is the most efficient way to get context on core procedures.

```bash
# Read the curated list of key rules
cat /home/ubuntu/skills/uniform-rules-of-court/references/key_rules.md
```

### 2. Search All Rules

For more specific queries or to find rules related to a particular topic, use the `search_rules.py` script. It can search by keyword or retrieve a specific rule by number.

```bash
# Usage: python scripts/search_rules.py <command> <query>

# Search for rules containing a keyword (e.g., "ex parte")
python /home/ubuntu/skills/uniform-rules-of-court/scripts/search_rules.py search "ex parte"

# Get the full text of a specific rule (e.g., Rule 6)
python /home/ubuntu/skills/uniform-rules-of-court/scripts/search_rules.py get 6

# Get multiple rules at once
python /home/ubuntu/skills/uniform-rules-of-court/scripts/search_rules.py get 6 30 42
```

### 3. Integration with `sa-entity-intel` and Case Analysis

This skill is designed to be used alongside `sa-entity-intel` and other legal analysis skills. When analyzing a case, you can use this skill to ground your analysis in specific procedural rules.

**Example Workflow:**

1.  **Analyze Evidence**: Use `lex-case-analysis` or `super-sleuth` to identify key events, such as the filing of an *ex parte* application.
2.  **Retrieve Entity Data**: Use `sa-entity-intel` to get the full details of the applicant and respondent entities.
3.  **Consult the Rules**: Use `uniform-rules-of-court` to retrieve the full text of Rule 6 (Applications).
4.  **Assess Compliance**: Compare the facts of the case with the procedural requirements outlined in Rule 6(4) and 6(12) for urgency and *ex parte* matters.
5.  **Draft Filings**: When using `lex-case-analysis` to generate a legal filing (e.g., an application to set aside an irregular proceeding), cite the specific sub-rules from Rule 30 that have been violated.

This workflow ensures that all legal arguments and analyses are firmly rooted in the correct procedural framework, significantly strengthening the quality and accuracy of the output.
