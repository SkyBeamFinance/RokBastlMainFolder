# PDF → Markdown Converter

Converts every `.pdf` / `.PDF` file in the repository into a cleaned Markdown file optimised for AI ingestion.

## Quick Start (local)

```bash
# 1. Install dependencies
pip install -r tools/pdf_to_md/requirements.txt

# 2. Run from the repository root
python tools/pdf_to_md/convert.py
```

Generated files are written to the `md/` directory (never to the repo root).

### Options

| Flag | Default | Description |
|---|---|---|
| `--repo-root PATH` | repo root (auto-detected) | Where to search for PDFs |
| `--output-dir PATH` | `<repo-root>/md` | Where to write `.md` files |

## Output Structure

```
md/
├── INDEX.md                          # auto-generated listing of all converted files
├── conversion_log.json               # machine-readable log (dates, page counts, warnings)
├── 0 - INDEX.md                      # converted from 0 - INDEX.pdf
├── 1 - Introduction.md               # …
├── …
└── False Info Fed Via Chatbot, .../  # subdirectory mirrors PDF subdirectory
    └── The Dark Triad - ….md
```

- Every PDF maps 1-to-1 to a `.md` file: same base filename, same relative path, `.md` extension.
- Subdirectory structure is preserved so provenance is always unambiguous.

## Front-Matter Fields

Each `.md` file begins with a YAML block, e.g.:

```yaml
---
title: "1 - Introduction"
source_repo: SkyBeamFinance/RokBastlMainFolder
source_path: 1 - Introduction.pdf
source_pdf: ../1 - Introduction.pdf
conversion_date: 2026-03-19
conversion_tool: pdf_to_md/convert.py v1.0.0
pages: 12
needs_ocr: false
---
```

## What `needs_ocr: true` Means

`needs_ocr: true` is set when the average extracted text per page is below **50 characters**.  
This typically means the PDF is a **scanned image** rather than a digitally-generated document.  
PyMuPDF can extract *selectable* text only; scanned pages require an OCR step (e.g. `ocrmypdf` + Tesseract) to become readable.  
The `.md` stub is still generated so the file is indexed and its absence is not silently ignored.

## Idempotency

Running the converter twice without changing any PDFs produces identical output (same content, same timestamps in front-matter because `conversion_date` is the run date — re-running on the same day produces no diff; re-running on a different day updates `conversion_date` and `conversion_log.json`).

## GitHub Actions

A workflow is provided at `.github/workflows/pdf-to-md.yml`.  
It can be triggered:
- **Manually** via the *Actions → Run workflow* button (with an optional `commit_back` toggle).
- **Automatically** on any push that touches a `.pdf` file or the converter script.

When `commit_back` is enabled (the default in CI), generated `md/` files are committed back to the same branch automatically.
