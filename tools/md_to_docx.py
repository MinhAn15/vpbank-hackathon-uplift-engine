"""Simple Markdown to DOCX converter for the UpliftEngine_Presentation_Summary.md

This script performs lightweight conversions: headings to Word headings, paragraphs,
and simple lists. It's intentionally small and deterministic for the hackathon.
"""
from docx import Document
from docx.shared import Pt
import re
from pathlib import Path


def add_heading(doc, text, level):
    doc.add_heading(text, level=level)


def add_paragraph(doc, text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(11)


def add_list(doc, lines):
    for line in lines:
        clean = line.lstrip('-').strip()
        p = doc.add_paragraph(clean, style='List Bullet')
        p.runs[0].font.size = Pt(11)


def md_to_docx(md_path: Path, docx_path: Path):
    doc = Document()
    doc.add_heading('Uplift Engine 2.1 — Project Summary', level=1)
    doc.add_paragraph()

    lines = md_path.read_text(encoding='utf-8').splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line:
            i += 1
            continue
        # Headings
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            add_heading(doc, text, level=min(level, 3))
            i += 1
            continue
        # Ordered or unordered lists
        if re.match(r'^\s*[-\*]\s+', line):
            buffer = []
            while i < len(lines) and re.match(r'^\s*[-\*]\s+', lines[i]):
                buffer.append(lines[i])
                i += 1
            add_list(doc, buffer)
            continue
        # Paragraph
        add_paragraph(doc, line)
        i += 1

    doc.save(docx_path)


if __name__ == '__main__':
    import sys
    root = Path(__file__).resolve().parents[1]
    md = root / 'docs' / 'UpliftEngine_Presentation_Summary.md'
    out = root / 'docs' / 'UpliftEngine_Presentation_Summary.docx'
    if len(sys.argv) > 1:
        md = Path(sys.argv[1])
    if len(sys.argv) > 2:
        out = Path(sys.argv[2])
    print(f'Converting {md} -> {out}')
    md_to_docx(md, out)
    print('Done')
