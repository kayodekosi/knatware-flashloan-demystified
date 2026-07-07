#!/usr/bin/env python3
"""
Build script for "Flash Loans, Demystified".

Renders the single-file HTML/CSS source (src/guide.html) to the
distributable PDF (dist/Flash-Loans-Instadapp-Pro-Cartoon-Guide.pdf)
using WeasyPrint.

Usage:
    pip install weasyprint
    python scripts/build.py
"""

from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "guide.html"
OUT = ROOT / "dist" / "Flash-Loans-Instadapp-Pro-Cartoon-Guide.pdf"


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    print(f"Rendering {SRC} -> {OUT} ...")
    HTML(str(SRC)).write_pdf(str(OUT))
    print("Done.")


if __name__ == "__main__":
    main()
