#!/usr/bin/env python3
"""
PDF → Markdown converter for SkyBeamFinance/RokBastlMainFolder.

Usage:
    python tools/pdf_to_md/convert.py [--repo-root REPO_ROOT] [--output-dir OUTPUT_DIR]

Outputs cleaned Markdown files in OUTPUT_DIR (default: md/) with YAML front-matter
and a conversion log at md/conversion_log.json.
"""

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: PyMuPDF is not installed. Run: pip install pymupdf", file=sys.stderr)
    sys.exit(1)

TOOL_NAME = "pdf_to_md/convert.py"
TOOL_VERSION = "1.0.0"
SOURCE_REPO = "SkyBeamFinance/RokBastlMainFolder"

# Minimum chars per page to consider text "present" (not needs_ocr)
OCR_MIN_CHARS_PER_PAGE = 50

# Directory names (relative to repo root) whose contents must never be
# converted to Markdown.  These folders contain personal / government
# identity documents that must not be re-published as readable text.
EXCLUDED_DIRS: set[str] = {
    "Presumed Personal Government Digital Database",
    "Personal Predicament",
}

# Common bullet markers
BULLET_RE = re.compile(r"^(\s*[-•·▪▸►*+]\s+|\s*\d+[.)]\s+)")


def clean_text(raw: str) -> str:
    """
    Apply cleaning heuristics to raw extracted PDF text:
    - Normalize line endings to \\n
    - De-hyphenate line breaks ("hy-\\nphen" → "hyphen")
    - Collapse multiple spaces to one
    - Join hard-wrapped lines into paragraphs while preserving blank lines
    - Preserve lines that look like bullet points as-is
    """
    # 1. Normalize line endings
    text = raw.replace("\r\n", "\n").replace("\r", "\n")

    # 2. De-hyphenate line breaks: word- \\n word → wordword
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)

    # 3. Collapse runs of spaces/tabs (but not newlines yet)
    text = re.sub(r"[ \t]+", " ", text)

    # 4. Normalize multiple blank lines to exactly two newlines (paragraph separator)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 5. Join hard-wrapped lines inside paragraphs.
    #    Strategy: process line-by-line; when a non-empty line is followed by
    #    another non-empty line (and neither looks like a bullet), join them with a space.
    lines = text.split("\n")
    result: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if not line:  # blank line → paragraph separator
            result.append("")
            i += 1
            continue

        # Accumulate continuation lines
        while i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if not next_line:
                break  # next is blank → end of paragraph
            # Don't merge if current or next line looks like a bullet
            if BULLET_RE.match(line) or BULLET_RE.match(next_line):
                break
            # Don't merge if current line ends with sentence-ending punctuation
            # (heuristic: period + optional quote/paren, then uppercase next word)
            if re.search(r'[.!?]["\')]?\s*$', line) and re.match(r"[A-Z]", next_line):
                break
            # Merge
            line = line.rstrip() + " " + next_line
            i += 1

        result.append(line)
        i += 1

    cleaned = "\n".join(result).strip()
    # Final collapse of multiple blank lines that may have crept in
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned


def make_front_matter(
    title: str,
    source_path: str,
    source_pdf_rel: str,
    conversion_date: str,
    pages: int,
    needs_ocr: bool,
) -> str:
    """Return YAML front-matter block."""
    # Escape double quotes in title
    safe_title = title.replace('"', '\\"')
    lines = [
        "---",
        f'title: "{safe_title}"',
        f"source_repo: {SOURCE_REPO}",
        f"source_path: {source_path}",
        f"source_pdf: {source_pdf_rel}",
        f"conversion_date: {conversion_date}",
        f"conversion_tool: {TOOL_NAME} v{TOOL_VERSION}",
        f"pages: {pages}",
        f"needs_ocr: {'true' if needs_ocr else 'false'}",
        "---",
        "",
    ]
    return "\n".join(lines)


def pdf_to_md(
    pdf_path: Path,
    repo_root: Path,
    output_dir: Path,
    conversion_date: str,
) -> dict:
    """
    Convert one PDF to Markdown.

    Returns a log entry dict with keys:
        pdf, md, pages, needs_ocr, warning (optional)
    """
    rel_pdf = pdf_path.relative_to(repo_root)
    # Preserve subdirectory structure under output_dir
    rel_dir = rel_pdf.parent
    md_name = pdf_path.stem + ".md"
    md_path = output_dir / rel_dir / md_name

    md_path.parent.mkdir(parents=True, exist_ok=True)

    # Relative link from the md file back to the PDF
    # e.g. if md is at  md/sub/foo.md  and pdf is at  sub/foo.pdf
    # then relative path is  ../../sub/foo.pdf
    md_to_repo_root = Path(os.path.relpath(repo_root, md_path.parent))
    source_pdf_rel = str(md_to_repo_root / rel_pdf).replace("\\", "/")

    title = pdf_path.stem
    log_entry: dict = {
        "pdf": str(rel_pdf).replace("\\", "/"),
        "md": str(md_path.relative_to(repo_root)).replace("\\", "/"),
        "pages": 0,
        "needs_ocr": False,
    }

    warnings: list[str] = []

    try:
        doc = fitz.open(str(pdf_path))
        pages = len(doc)
        log_entry["pages"] = pages

        page_texts: list[str] = []
        total_chars = 0
        for page in doc:
            raw = page.get_text("text")
            total_chars += len(raw.strip())
            page_texts.append(raw)
        doc.close()

        avg_chars = total_chars / pages if pages > 0 else 0
        needs_ocr = pages > 0 and avg_chars < OCR_MIN_CHARS_PER_PAGE
        log_entry["needs_ocr"] = needs_ocr

        if needs_ocr:
            warnings.append(
                f"Low text yield ({avg_chars:.0f} chars/page avg). "
                "Document may be scanned — OCR recommended."
            )

        # Build markdown body: one section per page
        md_body_parts: list[str] = []
        for idx, raw_page in enumerate(page_texts, start=1):
            cleaned = clean_text(raw_page)
            if cleaned:
                md_body_parts.append(f"## Page {idx}\n\n{cleaned}")
            else:
                md_body_parts.append(f"## Page {idx}\n\n*(no extractable text)*")

        body = "\n\n---\n\n".join(md_body_parts)

    except Exception as exc:  # noqa: BLE001
        warnings.append(f"Extraction error: {exc}")
        needs_ocr = True
        log_entry["needs_ocr"] = True
        body = "*(conversion error — see conversion_log.json)*"
        pages = 0
        log_entry["pages"] = 0

    front_matter = make_front_matter(
        title=title,
        source_path=str(rel_pdf).replace("\\", "/"),
        source_pdf_rel=source_pdf_rel,
        conversion_date=conversion_date,
        pages=log_entry["pages"],
        needs_ocr=log_entry["needs_ocr"],
    )

    md_content = front_matter + "\n# " + title + "\n\n" + body + "\n"

    md_path.write_text(md_content, encoding="utf-8")

    if warnings:
        log_entry["warnings"] = warnings

    return log_entry


def find_pdfs(repo_root: Path, output_dir: Path) -> list[Path]:
    """Recursively find all PDF files, excluding the output directory and
    any directories listed in EXCLUDED_DIRS (privacy/PII protection)."""
    output_dir_resolved = output_dir.resolve()
    repo_root_resolved = repo_root.resolve()
    pdfs: list[Path] = []
    for p in sorted(repo_root.rglob("*")):
        if p.suffix.lower() == ".pdf" and p.is_file():
            # Exclude anything inside the output directory
            try:
                p.resolve().relative_to(output_dir_resolved)
                continue  # it's inside output_dir, skip
            except ValueError:
                pass
            # Exclude directories that contain personal/sensitive documents
            rel_parts = p.resolve().relative_to(repo_root_resolved).parts
            if any(part in EXCLUDED_DIRS for part in rel_parts):
                print(f"  [skipped – excluded dir] {p.relative_to(repo_root)}")
                continue
            pdfs.append(p)
    return pdfs


def generate_index(log_entries: list[dict], output_dir: Path, repo_root: Path) -> None:
    """Write md/INDEX.md listing all converted files."""
    index_path = output_dir / "INDEX.md"
    lines = [
        "# Converted PDF Index",
        "",
        f"Generated by `{TOOL_NAME}` on {date.today().isoformat()}.",
        f"Source repository: `{SOURCE_REPO}`",
        "",
        "| Markdown | Source PDF | Pages | Needs OCR |",
        "|----------|-----------|-------|-----------|",
    ]
    for entry in log_entries:
        md_rel = entry["md"]
        pdf_rel = entry["pdf"]
        pages = entry.get("pages", "?")
        needs_ocr = "⚠️ yes" if entry.get("needs_ocr") else "no"
        # Link is relative from INDEX.md (which is in md/) to the md file
        md_link_path = Path(md_rel)
        md_link = str(md_link_path.relative_to(output_dir.relative_to(repo_root))) if str(md_link_path).startswith(str(output_dir.relative_to(repo_root))) else md_rel
        lines.append(f"| [{md_rel}]({md_link}) | `{pdf_rel}` | {pages} | {needs_ocr} |")

    lines.append("")
    index_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert all PDFs in a repository to Markdown."
    )
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Path to repository root (default: two levels up from this script)",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory for .md files (default: <repo_root>/md)",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).parent.resolve()

    if args.repo_root:
        repo_root = Path(args.repo_root).resolve()
    else:
        # tools/pdf_to_md/convert.py → repo root is two levels up
        repo_root = script_dir.parent.parent

    if args.output_dir:
        output_dir = Path(args.output_dir).resolve()
    else:
        output_dir = repo_root / "md"

    output_dir.mkdir(parents=True, exist_ok=True)

    conversion_date = date.today().isoformat()
    pdfs = find_pdfs(repo_root, output_dir)

    print(f"Found {len(pdfs)} PDF(s). Converting to {output_dir} …")

    log_entries: list[dict] = []
    for pdf_path in pdfs:
        rel = pdf_path.relative_to(repo_root)
        print(f"  → {rel}", end=" ", flush=True)
        entry = pdf_to_md(pdf_path, repo_root, output_dir, conversion_date)
        status = "⚠️  needs_ocr" if entry.get("needs_ocr") else "✓"
        print(status)
        log_entries.append(entry)

    # Write conversion log
    log_path = output_dir / "conversion_log.json"
    log_data = {
        "conversion_date": conversion_date,
        "tool": f"{TOOL_NAME} v{TOOL_VERSION}",
        "source_repo": SOURCE_REPO,
        "total_pdfs": len(log_entries),
        "needs_ocr_count": sum(1 for e in log_entries if e.get("needs_ocr")),
        "entries": log_entries,
    }
    log_path.write_text(json.dumps(log_data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nConversion log written to {log_path}")

    # Write index
    generate_index(log_entries, output_dir, repo_root)
    print(f"Index written to {output_dir / 'INDEX.md'}")

    needs_ocr_count = log_data["needs_ocr_count"]
    if needs_ocr_count:
        print(f"\n⚠️  {needs_ocr_count} file(s) flagged as needs_ocr.")

    print("\nDone.")


if __name__ == "__main__":
    main()
