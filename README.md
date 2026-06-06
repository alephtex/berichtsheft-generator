[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/steimerbyte)

> ⭐ If you find this useful, consider [supporting me on Ko-fi](https://ko-fi.com/steimerbyte)!

<img src="https://storage.ko-fi.com/cdn/generated/fhfuc7slzawvi/2026-04-23_rest-162bec27f642a562eb8401eb0ceb3940-onjpojl8.jpg" width="250" alt="steimerbyte" style="border-radius: 5%; margin: 16px 0; max-width: 100%;"/>

---

# Berichtsheft-Generator

Automatischer Berichtsheft-Generator für Auszubildende bei CANCOM.

## Usage

```bash
python3 fill_docx.py \
  --kw 16 \
  --jahr 2026 \
  --nr 136 \
  --abteilung Berufsschule \
  --montag "Montag Text..." \
  --dienstag "Dienstag Text..." \
  --mittwoch "Mittwoch Text..." \
  --donnerstag "Donnerstag Text..." \
  --freitag "Freitag Text..." \
  --thema "Wochen-Thema..."
```

## Parameter

| Parameter | Beschreibung | Beispiel |
|-----------|--------------|----------|
| `--kw` | Kalenderwoche | `16` |
| `--jahr` | Jahr | `2026` |
| `--nr` | Ausbildungsnachweis-Nr. | `136` |
| `--abteilung` | Abteilung | `Betrieb` oder `Berufsschule` |
| `--montag` bis `--freitag` | Tägliche Berichte | Freitext |
| `--thema` | Thema der Woche | Freitext |

## Platzhalter in Vorlage

```
{Nr}, {Ausbildungsjahr}, {KW}, {datums-range}
{Montag}, {Dienstag}, {Mittwoch}, {Donnerstag}, {Freitag}
{week_topic}, {Abteilung}, {day_of_signature}
```

## Features

- ✅ Platzhalter-Ersetzung in DOCX
- ✅ Checkboxen automatisch setzen (☐/☒)
- ✅ Abteilung-Spalte Font 8
- ✅ Automatische PDF-Konvertierung
- ✅ Auto-Shrink bei mehreren Seiten
- ✅ Auto-Open PDF mit xdg-open

---

## Hinweis zur KI-Unterstützung

Bei der Entwicklung dieses Projekts wurden teilweise oder vollständig KI-gestützte Tools und Technologien eingesetzt.