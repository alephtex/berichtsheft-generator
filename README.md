# Berichtsheft-Generator

Python-Tool zur automatischen Generierung von Berichtsheft-Ausbildungsnachweisen für die OSZ IMT Berlin.

## Programme

### 1. `fill_docx.py` - DOCX-Updater
Aktualisiert eine bestehende DOCX-Vorlage mit den eingegebenen Berichtsheft-Daten.

```bash
python3 fill_docx.py --kw 10 --jahr 2026 --nr 130 \
    --montag "Montag-Text" --dienstag "Dienstag-Text" \
    --mittwoch "Mittwoch-Text" --donnerstag "Donnerstag-Text" \
    --freitag "Freitag-Text" --thema "Thema der Woche" \
    --abteilung "Betrieb"
```

### 2. `fill_and_compile.py` - LaTeX zu PDF
Füllt ein LaTeX-Template und kompiliert direkt zu PDF (benötigt `pdflatex`).

```bash
python3 fill_and_compile.py --kw 10 --jahr 2026 --nr 130 \
    --datum "02.03.2026 - 08.03.2026" \
    --montag "Montag-Text" --montag-abt "Betrieb" \
    --dienstag "Dienstag-Text" --dienstag-abt "Betrieb" \
    --mittwoch "Mittwoch-Text" --mittwoch-abt "Betrieb" \
    --donnerstag "Donnerstag-Text" --donnerstag-abt "Berufsschule" \
    --freitag "Freitag-Text" --freitag-abt "Betrieb" \
    --thema "Thema der Woche" --thema-abt "Betrieb"
```

## Vorlagen-Syntax

### DOCX-Platzhalter (`fill_docx.py`)
Die DOCX-Vorlage muss folgende Platzhalter enthalten:

| Platzhalter | Beschreibung |
|-------------|--------------|
| `{Montag}` | Text für Montag |
| `{Dienstag}` | Text für Dienstag |
| `{Mittwoch}` | Text für Mittwoch |
| `{Donnerstag}` | Text für Donnerstag |
| `{Freitag}` | Text für Freitag |
| `{week_topic}` | Thema der Woche |
| `{Abteilung}` | Abteilung (Betrieb/Berufsschule) |
| `{Day-of-signature}.{JAHRESJAHR}` | Datum für Unterschriftsfeld |

### LaTeX-Platzhalter (`fill_and_compile.py`)
Das LaTeX-Template muss folgende Platzhalter enthalten:

| Platzhalter | Beschreibung |
|-------------|--------------|
| `@NUMMER@` | Ausbildungsnachweis-Nummer |
| `@JAHR@` | Ausbildungsjahr |
| `@KW@` | Kalenderwoche (z.B. "KW 10") |
| `@DATUM@` | Datumsbereich |
| `@MONTAG@` / `@MONTAG_ABT@` | Montag-Text + Abteilung |
| `@DIENSTAG@` / `@DIENSTAG_ABT@` | Dienstag-Text + Abteilung |
| `@MITTWOCH@` / `@MITTWOCH_ABT@` | Mittwoch-Text + Abteilung |
| `@DONNERSTAG@` / `@DONNERSTAG_ABT@` | Donnerstag-Text + Abteilung |
| `@FREITAG@` / `@FREITAG_ABT@` | Freitag-Text + Abteilung |
| `@THEMA@` / `@THEMA_ABT@` | Thema der Woche + Abteilung |

## Anforderungen

- Python 3.8+
- `python-docx` für DOCX-Updates: `pip install python-docx`
- `pdflatex` für PDF-Generierung (LaTeX)

## Lizenz

Privatprojekt - Alle Rechte vorbehalten
