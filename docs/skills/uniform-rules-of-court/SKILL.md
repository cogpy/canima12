---
name: uniform-rules-of-court
description: Provides access to the Uniform Rules of Court for South African High Court proceedings. Use for legal research, case analysis, and drafting legal documents. Triggers on any mention of SA court proceedings, applications, interdicts, affidavits, discovery, contempt, rescission, or specific rule numbers.
---

# Uniform Rules of Court (South Africa)

This skill provides a comprehensive, searchable, and structured interface to the Uniform Rules of Court, which govern the conduct of proceedings in the Provincial and Local Divisions of the High Court of South Africa. It is an essential tool for legal research, drafting court documents, and understanding procedural requirements in litigation.

This skill is based on the SAFLII consolidated version of the rules, updated to **30 January 2026**.

## Quick Reference: Critical Sub-Rules

For immediate context, here are the most critical sub-rules for case analysis:

| Rule | Description | Key Text |
|---|---|---|
| **6(12)(a)** | **Urgent Applications** | "In urgent applications the court or a judge may dispense with the forms and service provided for in these Rules..." |
| **6(12)(b)** | **Urgency Justification** | "...the applicant shall set forth explicitly the circumstances which he avers render the matter urgent and the reasons why he claims that he could not be afforded substantial redress at a hearing in due course." |
| **7(1)** | **Power of Attorney** | "No person other than a party to any cause or matter shall be entitled to act on behalf of such party unless he is an attorney or unless he has been authorized thereto by such party by a power of attorney." |
| **7(2)** | **Authority to Act** | "A power of attorney to act shall be filed with the registrar by the person so authorized before he takes any step in the proceedings." |
| **30(1)** | **Irregular Proceedings** | "A party to a cause in which an irregular step has been taken by any other party may apply to court to set it aside." |
| **42(1)(a)** | **Rescission of Orders** | The court may rescind an order "erroneously sought or erroneously granted in the absence of any party affected thereby." |
| **42(1)(c)** | **Rescission for Mistake** | The court may rescind an order "granted as the result of a mistake common to the parties." |
| **45A** | **Contempt of Court** | "A court may, on application, declare a person to be in contempt of court and make an appropriate order." |

## Key Capabilities

- **Full-Text Search**: Search the complete text of all 92 rules and associated forms.
- **Structured Access**: Directly access specific rules by number.
- **Integration with Entity Intelligence**: Can be used in conjunction with `sa-entity-intel` to apply procedural knowledge in the context of specific companies or individuals.

## Bundled Resources

- **`references/key_rules.md`**: A Markdown file containing the full, cleaned text of 13 key rules (including Rule 7 — Power of Attorney).
- **`references/all_rules.json`**: A JSON file containing the extracted text of all 92 rules, indexed by rule number.
- **`scripts/search_rules.py`**: A Python script to search and retrieve rule text programmatically.

## Workflow: How to Use

### 1. Search All Rules

For specific queries or to find rules related to a particular topic, use the `search_rules.py` script. It can search by keyword or retrieve a specific rule by number.

```bash
# Usage: python scripts/search_rules.py <command> <query>

# Search for rules containing a keyword (e.g., "ex parte")
python /home/ubuntu/skills/uniform-rules-of-court/scripts/search_rules.py search "ex parte"

# Get the full text of a specific rule (e.g., Rule 6)
python /home/ubuntu/skills/uniform-rules-of-court/scripts/search_rules.py get 6
```

### 2. Integration with `sa-entity-intel` and Case Analysis

This skill is designed to be used alongside `sa-entity-intel` and other legal analysis skills. When analyzing a case, you can use this skill to ground your analysis in specific procedural rules.

**Example Workflow:**

1.  **Analyze Evidence**: Use `lex-case-analysis` or `super-sleuth` to identify key events, such as the filing of an *ex parte* application.
2.  **Retrieve Entity Data**: Use `sa-entity-intel` to get the full details of the applicant and respondent entities.
3.  **Consult the Rules**: Use `uniform-rules-of-court` to retrieve the full text of Rule 6 (Applications).
4.  **Assess Compliance**: Compare the facts of the case with the procedural requirements outlined in Rule 6(4) and 6(12) for urgency and *ex parte* matters.
5.  **Draft Filings**: When using `lex-case-analysis` to generate a legal filing (e.g., an application to set aside an irregular proceeding), cite the specific sub-rules from Rule 30 that have been violated.

This workflow ensures that all legal arguments and analyses are firmly rooted in the correct procedural framework, significantly strengthening the quality and accuracy of the output.
