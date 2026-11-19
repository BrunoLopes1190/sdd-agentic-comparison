"""Builds doc/reference.docx (Pandoc styles) from the ISEP TMDEI dissertation template.

Usage: python doc/make_reference_docx.py

Changes to the official .dotx: saved as .docx; body reduced to one section with a
right-aligned page number footer (the template's cover and front-matter sections
leaked into the build); chapters start on a new page; a "Table" style with grid
borders added (Pandoc's table style, absent from the template); line spacing 1.5
instead of the template's 1.15 (course guideline; tables stay single). Everything else
(fonts, headings, numbering, captions, margins) is the template's.
"""
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'course-materials/general/tmdei-2425-dissertation-template.dotx'
DST = ROOT / 'doc/reference.docx'

SECT = ('<w:sectPr><w:footerReference w:type="default" r:id="rId12"/>'  # footer2: PAGE, right
        '<w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1985" w:right="1474" w:bottom="1418" w:left="1985" '
        'w:header="709" w:footer="709" w:gutter="0"/>'
        '<w:pgNumType w:start="1"/><w:cols w:space="708"/></w:sectPr>')

TABLE = ('<w:style w:type="table" w:customStyle="1" w:styleId="Table"><w:name w:val="Table"/>'
         '<w:basedOn w:val="TableGrid"/><w:qFormat/>'
         '<w:pPr><w:spacing w:before="40" w:after="40" w:line="240" w:lineRule="auto"/></w:pPr>'
         '</w:style>')


def fix(name, data):
    if name == '[Content_Types].xml':
        return data.replace(b'wordprocessingml.template.main+xml', b'wordprocessingml.document.main+xml')
    if name == 'word/document.xml':
        x = data.decode()
        x = re.sub(r'<w:body>.*</w:body>', '<w:body><w:p/>' + SECT + '</w:body>', x, flags=re.S)
        return x.encode()
    if name == 'word/styles.xml':
        x = data.decode()
        # Chapters (Heading 1) start on a new page.
        x = re.sub(r'(<w:style [^>]*w:styleId="Heading1">.*?<w:pPr>)', r'\1<w:pageBreakBefore/>', x, count=1, flags=re.S)
        x = x.replace('</w:styles>', TABLE + '</w:styles>')
        # Line spacing 1.5 (course: Calibri 11, 1.5); the template's default is 1.15 (276).
        x = re.sub(r'(<w:pPrDefault>.*?w:line=")276(")', r'\g<1>360\2', x, count=1, flags=re.S)
        return x.encode()
    return data


with zipfile.ZipFile(SRC) as zi, zipfile.ZipFile(DST, 'w', zipfile.ZIP_DEFLATED) as zo:
    for item in zi.infolist():
        zo.writestr(item, fix(item.filename, zi.read(item.filename)))

with zipfile.ZipFile(DST) as z:  # self-check
    assert b'document.main+xml' in z.read('[Content_Types].xml')
    assert z.read('word/document.xml').count(b'<w:sectPr>') == 1
    assert b'w:styleId="Table"' in z.read('word/styles.xml')
    assert b'w:line="360"' in z.read('word/styles.xml')
print(f'Wrote {DST}')
