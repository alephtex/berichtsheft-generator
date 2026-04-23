#!/usr/bin/env python3
"""
Berichtsheft LaTeX Generator
Füllt das Template und kompiliert zu PDF

Usage:
    python3 fill_and_compile.py --kw 10 --jahr 2026 --nr 130 \
        --montag "Text für Montag" --montag-abt "Betrieb" \
        --dienstag "Text für Dienstag" --dienstag-abt "Betrieb" \
        ... (alle Tage und Thema der Woche)
"""

import argparse
import os
import subprocess
import tempfile
from pathlib import Path

def fill_template(template_path, output_path, args):
    """Ersetzt @PLATZHALTER@ mit den übergebenen Werten."""
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    replacements = {
        '@NUMMER@': str(args.nr),
        '@JAHR@': str(args.jahr),
        '@KW@': f"KW {args.kw:02d}",
        '@DATUM@': args.datum,
        '@MONTAG@': args.montag,
        '@MONTAG_ABT@': args.montag_abt,
        '@DIENSTAG@': args.dienstag,
        '@DIENSTAG_ABT@': args.dienstag_abt,
        '@MITTWOCH@': args.mittwoch,
        '@MITTWOCH_ABT@': args.mittwoch_abt,
        '@DONNERSTAG@': args.donnerstag,
        '@DONNERSTAG_ABT@': args.donnerstag_abt,
        '@FREITAG@': args.freitag,
        '@FREITAG_ABT@': args.freitag_abt,
        '@THEMA@': args.thema,
        '@THEMA_ABT@': args.thema_abt,
    }
    
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Template gefüllt: {output_path}")

def compile_to_pdf(tex_path, output_dir):
    """Kompiliert LaTeX zu PDF mit pdflatex."""
    
    os.chdir(output_dir)
    
    # Zweimal kompilieren für korrekte Referenzen
    for _ in range(2):
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', tex_path],
            capture_output=True
        )
        if result.returncode != 0:
            print("Fehler bei Kompilierung:")
            print(result.stderr[-2000:])  # Letzte 2000 Zeichen
            return False
    
    # PDF finden und verschieben
    pdf_name = Path(tex_path).stem + '.pdf'
    pdf_path = Path(output_dir) / pdf_name
    
    if pdf_path.exists():
        print(f"PDF erstellt: {pdf_path}")
        return str(pdf_path)
    else:
        print("PDF nicht gefunden!")
        return None

def main():
    parser = argparse.ArgumentParser(description='Berichtsheft Generator')
    parser.add_argument('--kw', type=int, required=True, help='Kalenderwoche')
    parser.add_argument('--jahr', type=int, required=True, help='Jahr')
    parser.add_argument('--nr', type=int, required=True, help='Ausbildungsnachweis Nummer')
    parser.add_argument('--datum', type=str, required=True, help='Datumsbereich (z.B. "02.03.2026 - 08.03.2026")')
    
    # Tage
    parser.add_argument('--montag', type=str, default='')
    parser.add_argument('--montag-abt', type=str, default='Betrieb')
    parser.add_argument('--dienstag', type=str, default='')
    parser.add_argument('--dienstag-abt', type=str, default='Betrieb')
    parser.add_argument('--mittwoch', type=str, default='')
    parser.add_argument('--mittwoch-abt', type=str, default='Betrieb')
    parser.add_argument('--donnerstag', type=str, default='')
    parser.add_argument('--donnerstag-abt', type=str, default='Betrieb')
    parser.add_argument('--freitag', type=str, default='')
    parser.add_argument('--freitag-abt', type=str, default='Betrieb')
    
    # Thema der Woche
    parser.add_argument('--thema', type=str, default='')
    parser.add_argument('--thema-abt', type=str, default='Betrieb')
    
    # Ausgabe
    parser.add_argument('--output', type=str, help='Ausgabe-PDF Pfad (optional)')
    
    args = parser.parse_args()
    
    # Pfade
    vorlage_dir = Path(__file__).parent
    template_path = vorlage_dir / 'berichtsheft_template.tex'
    output_tex = vorlage_dir / f'berichtsheft_kw{args.kw:02d}.tex'
    
    # Template füllen
    fill_template(template_path, output_tex, args)
    
    # Kompilieren
    pdf_path = compile_to_pdf(output_tex, vorlage_dir)
    
    if pdf_path and args.output:
        import shutil
        shutil.move(pdf_path, args.output)
        print(f"PDF verschoben nach: {args.output}")

if __name__ == '__main__':
    main()
