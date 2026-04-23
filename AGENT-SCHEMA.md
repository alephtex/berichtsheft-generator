# Agent Naming Schema & Versioning Convention

## Schema

```
[domain]-[function]-[subtype]-v[M][m][p].md
```

### Components

| Component | Beschreibung | Beispiele |
|-----------|--------------|-----------|
| `[domain]` | Funktionsbereich | `research`, `build`, `write`, `scrape`, `util` |
| `[function]` | Hauptaufgabe | `deep`, `fast`, `lite`, `pro` |
| `[subtype]` | Optional: Spezialisierung | `news`, `academic`, `code`, `docs` |
| `v[M][m][p]` | Major.Minor.Patch | `v001`, `v010`, `v100` |

### Version-Semantik

| Version | Bedeutung | Beispiel |
|---------|-----------|----------|
| `v001` → `v002` | Breaking Changes, neue Major-Features | rewrite, new workflow |
| `v001` → `v010` | Neue Features, rückwärts-kompatibel | added gap-filling |
| `v001` → `v011` | Bug Fixes, kleine Improvements | fixed timeout |

---

## Vorschlag: Konsolidierte Agenten

### 🗑️ ZU LÖSCHEN (Redundant/Veraltet)

| Datei | Grund |
|-------|-------|
| `research.md` | ✅ Veraltet → `deep-research-v003` existiert |
| `deep-research-v003.md` | ✅ Veraltet → `deep-research-v004` existiert |
| `GroqV2.md` | ✅ Veraltet → `groq-v002.md` erstellen |
| `super-builder.md` | ✅ Redundant → `defensive-builder` nutzen |
| `Super-Agent-v3.md` | ✅ Redundant → `defensive-builder` nutzen |
| `memory.md` | ❌ Kein echter Agent, nur Notes |

### 📝 UMZUBENENNEN

| Alt | Neu | Änderung |
|-----|-----|----------|
| `groq.md` | `chat-groq-v001.md` | Besseres Schema |
| `konzept-agent-v003.md` | `write-konzept-v001.md` | Besseres Schema, interne Version 2.4 → neue Major |
| `deep-news-agent.md` | `research-news-v001.md` | Besseres Schema |

### ✅ BEIBEHALTEN (mit ggf. neuer Version)

| Agent | Neue Version | Notes |
|-------|--------------|-------|
| `deep-research-v004.md` | `research-deep-v001.md` | Neues Schema, aber erst bei Major-Rewrite |
| `fast-research-v002.md` | `research-fast-v001.md` | Neues Schema |
| `deep-worker-v001.md` | `research-deep-heavy-v001.md` | Neues Schema |
| `defensive-builder.md` | `build-code-defensive-v001.md` | Neues Schema |

---

## Vollständige konsolidierte Liste

### RESEARCH Family

```
research-fast-v001.md      (3 searches, ~2min)
research-deep-v001.md      (10-50 permutations, NEW)
research-deep-heavy-v001.md (100+ permutations, NEW)
research-news-v001.md      (News only, NEW)
```

### BUILD Family

```
build-code-defensive-v001.md  (Negative Space, Auto modes)
build-agent-v001.md           (Agent builder, NEW)
```

### WRITE Family

```
write-konzept-v001.md      (IT-Konzepte)
write-bericht-v001.md      (Ausbildungsnachweise)
write-transcript-v001.md   (Video transcripts)
write-wallpaper-v001.md    (Image prompts)
```

### SCRAPE Family

```
scrape-itdz-v001.md        (ITDZ Ausschreibungen)
```

### UTIL Family

```
util-aufgaben-v001.md      (Task decomposition)
util-solution-reviewer-v001.md (Review workflow)
util-browser-v001.md       (Browser automation)
util-network-v001.md       (Netzwerk products)
util-action-log-v001.md    (Session logging)
util-news-aggregator-v001.md (AI News)
```

### SPECIAL

```
special-auswandern-v001.md (Emigration planning)
```

---

## Umsetzungsplan

### Phase 1: Löschen (Sicher)
```bash
# Redundante Agenten löschen
rm research.md
rm deep-research-v003.md
rm GroqV2.md
rm super-builder.md
rm Super-Agent-v3.md
rm memory.md
```

### Phase 2: Umbenennen
```bash
# Bessere Namen
mv groq.md chat-groq-v001.md
mv konzept-agent-v003.md write-konzept-v001.md
mv deep-news-agent.md research-news-v001.md
```

### Phase 3: Neue Major-Versionen (optional)
```bash
# Bei nächstem Major-Rewrite:
mv deep-research-v004.md research-deep-v001.md
mv fast-research-v002.md research-fast-v001.md
mv deep-worker-v001.md research-deep-heavy-v001.md
mv defensive-builder.md build-code-defensive-v001.md
```

---

## Regeln für neue Agenten

1. **Immer Schema verwenden**: `[domain]-[function]-[subtype]-v[M][m][p].md`
2. **Version bei Breaking Changes**: `v001` → `v002`
3. **Version bei neuen Features**: `v001` → `v010`
4. **Version bei Bug Fixes**: `v001` → `v011`
5. **Dokumentation**: Jeder Agent braucht Changelog in Frontmatter
6. **KEINE** Agenten mit gleichem Namen + unterschiedliche Versionen nebeneinander
