#!/usr/bin/env python3
"""
Berichtsheft DOCX Updater
Ersetzt Platzhalter in der aktuellen KW-DOCX.

Usage:
    python3 fill_docx.py --kw 10 --jahr 2026 --nr 130 \
        --montag "Text für Montag" --dienstag "Text für Dienstag" \
        --mittwoch "Text für Mittwoch" --donnerstag "Text für Donnerstag" \
        --freitag "Text für Freitag" --thema "Text für Thema der Woche" \
        --abteilung "Betrieb"

Platzhalter:
    {Abteilung}           - Abteilung (Betrieb/Berufsschule)
    {Day-of-signature}.{JAHRESJAHR}  - Datum für Unterschrift
    {Montag}             - Text für Montag
    {Dienstag}           - Text für Dienstag
    {Mittwoch}           - Text für Mittwoch
    {Donnerstag}          - Text für Donnerstag
    {Freitag}            - Text für Freitag
    {week_topic}          - Text für Thema der Woche
"""

import argparse
import os
import sys
from pathlib import Path
from docx import Document
from docx.shared import Pt

def replace_in_paragraph(paragraph, replacements):
    """Ersetzt Platzhalter in einem Paragraph."""
    full_text = paragraph.text
    for placeholder, value in replacements.items():
        if placeholder in full_text:
            for run in paragraph.runs:
                run.text = ""
            if paragraph.runs:
                paragraph.runs[0].text = full_text.replace(placeholder, value)
            else:
                paragraph.add_run(full_text.replace(placeholder, value))

def replace_in_cell(cell, replacements):
    """Ersetzt Platzhalter in einer Tabellenzelle."""
    for para in cell.paragraphs:
        replace_in_paragraph(para, replacements)

def main():
    parser = argparse.ArgumentParser(description='Berichtsheft DOCX Updater')
    parser.add_argument('--kw', type=int, required=True, help='Kalenderwoche')
    parser.add_argument('--jahr', type=int, required=True, help='Jahr')
    parser.add_argument('--nr', type=int, required=True, help='Ausbildungsnachweis Nummer')
    parser.add_argument('--abteilung', type=str, required=True, choices=['Betrieb', 'Berufsschule'],
                        help='Abteilung')
    parser.add_argument('--montag', type=str, default='')
    parser.add_argument('--dienstag', type=str, default='')
    parser.add_argument('--mittwoch', type=str, default='')
    parser.add_argument('--donnerstag', type=str, default='')
    parser.add_argument('--freitag', type=str, default='')
    parser.add_argument('--thema', type=str, default='')
    parser.add_argument('--datum', type=str, default='', help='Datumsbereich z.B. "02.03.2026 - 08.03.2026"')
    
    args = parser.parse_args()
    
    # KW-Ordner Pfad
    kw_dir = Path.home() / 'Nextcloud' / 'Dokumente' / 'Ausbildung-Cancom' / 'Berichtsheft' / str(args.jahr) / f'KW{args.kw:02d}'
    kw_dir.mkdir(parents=True, exist_ok=True)
    
    # DOCX-Pfad
    docx_path = kw_dir / f'Berichtsheft Täglich KW {args.kw:02d}.docx'
    
    if not docx_path.exists():
        print(f"FEHLER: DOCX nicht gefunden: {docx_path}")
        print("Bitte zuerst eine DOCX in den Ordner kopieren.")
        sys.exit(1)
    
    # Datumsberechnung für Signaturdatum (letzter Tag der KW)
    # Vereinfacht: 08.03.2026 für KW 10
    if args.datum:
        # Extrahiere letztes Datum aus dem Bereich
        parts = args.datum.split(' - ')
        if len(parts) == 2:
            day_of_signature = parts[1].split('.')[0] + '.' + parts[1].split('.')[1]
        else:
            day_of_signature = "08.03"
    else:
        day_of_signature = "08.03"
    
    # Replacements
    replacements = {
        '{Abteilung}': args.abteilung,
        '{Day-of-signature}.{JAHRESJAHR}': f"{day_of_signature}.{args.jahr}",
        '{Montag}': args.montag,
        '{Dienstag}': args.dienstag,
        '{Mittwoch}': args.mittwoch,
        '{Donnerstag}': args.donnerstag,
        '{Freitag}': args.freitag,
        '{week_topic}': args.thema,
    }
    
    print(f"Öffne: {docx_path}")
    
    # Dokument öffnen
    doc = Document(str(docx_path))
    
    # In Tables ersetzen
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                replace_in_cell(cell, replacements)
    
    # In Paragraphs ersetzen
    for para in doc.paragraphs:
        replace_in_paragraph(para, replacements)
    
    # Nummer und Jahr in Header aktualisieren falls vorhanden
    for para in doc.paragraphs:
        if 'Ausbildungsnachweis Nr.' in para.text:
            for run in para.runs:
                if 'Nr.' in run.text:
                    run.text = f"Ausbildungsnachweis Nr. {args.nr}"
            break
    
    # Speichern (überschreibt existierende DOCX)
    doc.save(str(docx_path))
    print(f"✓ DOCX aktualisiert: {docx_path}")
    
    # Optional: PDF generieren
    latex_dir = Path.home() / 'Nextcloud' / 'Dokumente' / 'Ausbildung-Cancom' / 'Berichtsheft' / 'Vorlage'
    latex_template = latex_dir / 'berichtsheft_template.tex'
    
    if latex_template.exists():
        print("LaTeX Template gefunden - PDF könnte generiert werden mit fill_and_compile.py")

if __name__ == '__main__':
    main()
