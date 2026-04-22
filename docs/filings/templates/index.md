# High Court Templates Index

**Last Updated:** 2026-04-22  
**Purpose:** Provide a dedicated home for reusable template documents, separate them from live filing analyses, and map the current template inventory against the missing High Court procedural templates that still need to be generated.[1] [2] [3]

## Purpose

This folder now serves as the **canonical template surface** for reusable documents. The objective is to separate three different document classes that had started to mix together in `docs/filings`:

| Document class | What belongs here | What does not |
|---|---|---|
| **Reusable templates** | Notices, motions, affidavits, pleadings, mandates, resolution templates, and adaptable precedent skeletons | Case-specific red-team critiques, evidence reports, or narrative memoranda |
| **Template indexes and reference maps** | Taxonomies, template inventories, warning matrices, and folder navigation | Final live filing versions for actual submission |
| **Supporting precedent packs** | Rule-family libraries and case-priority skeletons | Historical versions kept only for record or audit purposes |

## Proposed Folder Structure

The template library is best organized by **procedural function** rather than by the date a template was created.[2] [3]

| Folder | Function | Status |
|---|---|---|
| [templates/administrative/](./administrative/index.md) | CourtOnline access, attorney appointment, mandates, service/admin forms | Active |
| [templates/motion_proceedings/](./motion_proceedings/index.md) | Rule 6 motion notices and affidavit sequence | Active |
| [templates/action_proceedings/](./action_proceedings/index.md) | Summons, declaration, plea, exception, reconvention, bar, amendment | Active |
| [templates/irregularity_and_compliance/](./irregularity_and_compliance/index.md) | Rules 7, 27, 30, 30A, 42 and related corrective process | Active |
| [templates/discovery_and_trial/](./discovery_and_trial/index.md) | Rules 31, 32, 33, 34, 35, 36, 37, 38 and trial-preparation templates | Active |
| [templates/settlement_and_mediation/](./settlement_and_mediation/index.md) | Rule 41 / 41A templates | Active |
| [templates/appeals_and_review/](./appeals_and_review/index.md) | Rule 49 / 53 / leave-to-appeal / review templates | Active |
| [templates/execution_and_costs/](./execution_and_costs/index.md) | Rules 45A, 47, 48 templates | Active |
| [templates/special_proceedings/](./special_proceedings/index.md) | Rule 58 interpleader and other specialist forms | Active |
| [templates/corporate_and_evidence/](./corporate_and_evidence/index.md) | Board resolutions, POPIA release schedules, governance invitations, limited mandates | Active |
| [templates/reference/](./reference/index.md) | Taxonomies, master libraries, gap analyses, usage notes | Active |

## Existing Template Assets Identified

The following files already exist and should either remain in this folder or be moved into subfolders beneath it.

| Current file | Recommended destination | Reason |
|---|---|---|
| `templates/BOARD_RESOLUTION_TEMPLATE.md` | `templates/corporate_and_evidence/` | Existing reusable corporate template |
| `templates/CORRESPONDENT_MANDATE_TEMPLATE.md` | `templates/administrative/` | Existing mandate / appointment template |
| `templates/EMAIL_RADEMEYER_INQUIRY.md` | `templates/administrative/` | Existing correspondence / engagement template |
| `templates/POPIA_EVIDENCE_RELEASE_SCHEDULE.md` | `templates/corporate_and_evidence/` | Existing evidence-release template |
| `../TEMPLATE_ANSWERING_AFFIDAVIT_LIP.md` | `templates/motion_proceedings/` | Existing affidavit template asset |
| `../TEMPLATE_CORPORATE_GOVERNANCE_INVITATION.md` | `templates/corporate_and_evidence/` | Existing governance-affidavit template asset |
| `../COURTONLINE_APPEAL_RESPONSE_TEMPLATE_2026-04-22.md` | `templates/appeals_and_review/` | Existing case-specific appellate wrapper |
| `../UNIFORM_RULES_TEMPLATE_LIBRARY_2026-04-22.md` | `templates/reference/` | Master precedent pack for rule families |
| `../UNIFORM_RULES_TEMPLATE_TAXONOMY_2026-04-22.md` | `templates/reference/` | Gap analysis and structure guide |
| `../CASE_PRIORITY_MISSING_TEMPLATES_2026-04-22.md` | `templates/reference/` | Case-priority pack feeding individual template files |

## Missing Template Families to Generate as Individual Files

The current gap is not analytical anymore; it is structural. The master library exists, but most template families still need to be materialized as **individual files** inside the folder hierarchy.[2] [3]

| Category | Missing individual files to generate |
|---|---|
| Administrative | Request to access a case; notice of appointment as attorney of record; notice to abide |
| Motion proceedings | general notice of motion; founding affidavit skeleton; answering affidavit skeleton; replying affidavit skeleton |
| Action proceedings | combined summons; simple summons; notice of intention to defend; declaration; plea; exception / strike-out; claim in reconvention; notice of bar; notice of amendment |
| Irregularity and compliance | Rule 7 notice; Rule 27 condonation / removal of bar; Rule 30 notice; Rule 30 application; Rule 30A notice; Rule 30A application; Rule 42 rescission / variation |
| Discovery and trial | discovery affidavit; Rule 35(3) further discovery notice; expert notice and summary; Rule 37 pre-trial notice; Rule 38 affidavit-evidence application |
| Settlement and mediation | withdrawal / discontinuance notice; Rule 41A mediation notice |
| Appeals and review | leave-to-appeal notice; opposition to leave to appeal; Rule 53 review notice; amicus curiae application; joinder application |
| Execution and costs | Rule 45A stay / suspension application; Rule 47 security notice; Rule 47 security application; Rule 48 review of taxation |
| Special proceedings | Rule 58 interpleader |

## Migration Logic

The migration should follow three rules.

| Rule | Practical meaning |
|---|---|
| **Keep live filings visible** | Existing filing indexes should still point to important template resources even after the move. |
| **Prefer one template per file** | The master library should remain as a consolidated reference, but practical drafting works best when each template has its own file. |
| **Preserve historical source files where useful** | If a root-level template has value as provenance, it may be retained or replaced by a forwarding note after migration. |

## Next Build Step

The next implementation step is therefore to create the subfolders above, move the existing template assets into their category folders, and generate the missing individual template files from the master library and case-priority pack.[2] [3]

## References

[1]: file:///home/ubuntu/revstream1/docs/filings/index.md "Legal Filings Index"
[2]: file:///home/ubuntu/revstream1/docs/filings/UNIFORM_RULES_TEMPLATE_LIBRARY_2026-04-22.md "Uniform Rules Template Library (2026-04-22)"
[3]: file:///home/ubuntu/revstream1/docs/filings/UNIFORM_RULES_TEMPLATE_TAXONOMY_2026-04-22.md "Uniform Rules Template Taxonomy (2026-04-22)"
