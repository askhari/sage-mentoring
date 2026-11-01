# /// script
# requires-python = ">=3.11"
# dependencies = ["pypdf>=4", "fonttools>=4"]
# ///
"""Download a source PDF and extract its text, so a source-researcher can read it.

Researchers only have WebFetch, which cannot extract text from most PDFs and
rejects some TLS certificates. The main session runs this script and gives
the researcher the path to the text file.

Usage:
  uv run tools/pdf_to_text.py <url-or-local-pdf> <out-dir> [--name NAME]

Writes <out-dir>/<name>.pdf (when given a URL) and <out-dir>/<name>.txt, with a
"=== PAGE n ===" marker before each page so claims can be located by page.
Use a scratch folder as <out-dir>, never the topic folder: raw sources are not
kept in the repository.
"""
import argparse
import logging
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader


def main() -> int:
    logging.getLogger("pypdf").setLevel(logging.ERROR)  # font-encoding chatter
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("out_dir")
    ap.add_argument("--name")
    a = ap.parse_args()

    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    name = a.name or Path(a.src.split("?")[0]).stem
    if a.src.startswith(("http://", "https://")):
        pdf = out / f"{name}.pdf"
        # curl copes with servers and certificates that WebFetch rejects.
        r = subprocess.run(["curl", "-sSL", "-m", "60", "-A", "Mozilla/5.0", "-o", str(pdf), a.src])
        if r.returncode != 0:
            print(f"download failed (curl exit {r.returncode})", file=sys.stderr)
            return 1
    else:
        pdf = Path(a.src)

    if not pdf.read_bytes()[:5] == b"%PDF-":
        print(f"{pdf} is not a PDF (probably an HTML page or a block)", file=sys.stderr)
        return 1

    reader = PdfReader(pdf)
    txt = out / f"{name}.txt"
    chars = 0
    with txt.open("w") as f:
        for i, page in enumerate(reader.pages, 1):
            text = page.extract_text() or ""
            chars += len(text)
            f.write(f"\n\n=== PAGE {i} ===\n{text}")
    print(f"{txt}: {len(reader.pages)} pages, {chars} characters")
    if chars < 200 * len(reader.pages):
        print("warning: little text extracted; the PDF may be scanned images", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
