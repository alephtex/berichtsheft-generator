# Berichtsheft-Generator

CLI-Tool zum automatischen Ausfüllen von Berichtsheft-DOCX-Vorlagen für AI Agents.

## Für Agent-Nutzung

Dieses Tool ist primär als **Tool-Call** für AI Agents konzipiert (OpenCode, Pi, Hermes, etc.).

### Tool-Definition (JSON)

```json
{
  "name": "berichtsheft_generator",
  "description": "Füllt eine Berichtsheft-DOCX-Vorlage mit den übergebenen Daten und exportiert sie zu PDF via LibreOffice",
  "parameters": {
    "type": "object",
    "properties": {
      "kw": {"type": "integer", "description": "Kalenderwoche (z.B. 10)"},
      "jahr": {"type": "integer", "description": "Jahr (z.B. 2026)"},
      "nr": {"type": "integer", "description": "Ausbildungsnachweis-Nummer"},
      "abteilung": {"type": "string", "enum": ["Betrieb", "Berufsschule"]},
      "montag": {"type": "string", "description": "Text für Montag"},
      "dienstag": {"type": "string", "description": "Text für Dienstag"},
      "mittwoch": {"type": "string", "description": "Text für Mittwoch"},
      "donnerstag": {"type": "string", "description": "Text für Donnerstag"},
      "freitag": {"type": "string", "description": "Text für Freitag"},
      "thema": {"type": "string", "description": "Thema der Woche"},
      "datum": {"type": "string", "description": "Datumsbereich (z.B. '02.03.2026 - 08.03.2026')"}
    },
    "required": ["kw", "jahr", "nr", "abteilung"]
  }
}
```

### Agent-Integration (Pi/OpenCode)

```bash
# Direkter Aufruf
python3 fill_docx.py --kw 10 --jahr 2026 --nr 130 \
  --montag "Montag-Text" --dienstag "Dienstag-Text" \
  --mittwoch "Mittwoch-Text" --donnerstag "Donnerstag-Text" \
  --freitag "Freitag-Text" --thema "Thema der Woche" \
  --abteilung "Betrieb" --datum "02.03.2026 - 08.03.2026"

# PDF-Export via LibreOffice
libreoffice --headless --convert-to pdf --outdir . "Berichtsheft Täglich KW 10.docx"
```

## Manueller Workflow

1. **DOCX-Vorlage** in KW-Ordner kopieren:
   ```
   [Cloud]/[Dokumente]/Berichtsheft/[JAHR]/KW[XX]/Berichtsheft Täglich KW [XX].docx
   ```

2. **Füllen:** `python3 fill_docx.py --kw 10 ...`

3. **PDF exportieren:** `libreoffice --headless --convert-to pdf ...`

## DOCX-Vorlage Platzhalter

| Platzhalter | Beschreibung |
|-------------|--------------|
| `{Montag}` | Text für Montag |
| `{Dienstag}` | Text für Dienstag |
| `{Mittwoch}` | Text für Mittwoch |
| `{Donnerstag}` | Text für Donnerstag |
| `{Freitag}` | Text für Freitag |
| `{week_topic}` | Thema der Woche |
| `{Abteilung}` | Abteilung (Betrieb/Berufsschule) |
| `{Day-of-signature}.{JAHRESJAHR}` | Datum für Unterschrift |

## Anforderungen

- Python 3.8+
- `python-docx`: `pip install python-docx`
- LibreOffice (für PDF-Export)

## Lizenz

Privatprojekt — Alle Rechte vorbehalten
