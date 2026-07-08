# F012 Rule 6(12)(c) Transcription QA Report

## Source selection

The primary transcription source selected is `F012-notice-motion-affidavit-rule6-12c-reconsideration.pdf` because it is the direct Rule 6(12)(c) reconsideration application file and contains the complete 49-page sequence used for the transcription. The reference file, `F-urgent-notice-motion-founding-affidavit.pdf`, has been retained alongside the transcription because it contains the related Court Online copy and useful corroborating page-image context, but it includes filing footers/stamps that make it less optimal as the primary transcription source.

| Item | Primary PDF | Reference PDF |
|---|---:|---:|
| Page count | 49 | 53 |
| Embedded text quality | Pages 1-7 strong; pages 8-49 scanned | Pages 1 and 5-11 contain text; later pages mostly scanned with Court Online footer text |
| Transcription role | Primary | Cross-reference copy retained |

## Transcription method

Pages 1–7 were extracted from the embedded text layer with layout-preserving `pdftotext -layout`. Pages 8–49 were rendered at 300 dpi and OCR-processed with Tesseract using page segmentation mode 4, then visually checked on representative scanned pages and corrected at the final commissioner/signature page.

The resulting deliverable is page-separated Markdown with the original PDF page order preserved. Code blocks are used to retain line breaks and spacing as far as practicable in Markdown.

## Important sequence observation

Both source copies show an internal affidavit page-order anomaly near the end. In PDF page order, internal affidavit page 41 appears before internal affidavit page 40, and internal page 42 follows thereafter. The transcription preserves the PDF source order rather than reordering the document.

| PDF page | Internal affidavit page | Paragraph range observed |
|---:|---:|---|
| 47 | 41 | 185.2–190 |
| 48 | 40 | 182–185.1 |
| 49 | 42 | 190.1–192 and commissioner block |

## Outputs

The working transcription package contains the Markdown transcription, metadata JSON, this QA report, and both PDF source copies for reference.
