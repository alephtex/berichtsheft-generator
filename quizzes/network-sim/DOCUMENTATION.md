# Netzwerk-Simulator Pro

## Übersicht

Ein vollständiger, browserbasierter Netzwerk-Simulator inspiriert von Cisco Packet Tracer, entwickelt für ITSE IHK AP2 Prüfungsvorbereitung. Vollständig in HTML, CSS und JavaScript implementiert.

**Features:**
- 25+ Netzwerk-Geräte (PCs, Switches, Router, Server, PoE-Geräte, WAN)
- Drag & Drop Topologie-Erstellung
- **Port-basierte Verbindungen per Ziehen** (Draggable Ports!)
- **4 Kabeltypen**: Kupfer Straight, Crossover, Glasfaser, Seriell
- PDU-Simulation (ICMP, ARP, DHCP, DNS, HTTP, TCP, UDP)
- **Packet Capture & Detail View** mit Hex Dump
- STP (Spanning Tree Protocol)
- **EtherChannel** (LACP/PAgP) Konfiguration
- **Port Security** Konfiguration
- VLAN & Switchport Konfiguration
- **Routing Protokolle**: RIP, OSPF, EIGRP
- **DHCP Pool & Relay (ip helper-address)**
- **QoS** Konfiguration
- CLI Terminal mit IOS-Befehlen
- NAT und ACL Unterstützung
- **Geräte Vorlagen** (Basic LAN, Router LAN, Corporate, WAN, PoE)
- **Physical Workspace** mit Rack View
- **Auto-Connect** für ausgewählte Geräte
- Save/Load Topologien (JSON)
- **Realtime & Simulation Modus**

---

## Inhaltsverzeichnis

1. [Schnellstart](#schnellstart)
2. [Gerätebibliothek](#gerätebibliothek)
3. [Topologie erstellen](#topologie-erstellen)
4. [Verbindungen](#verbindungen)
5. [Konfiguration](#konfiguration)
6. [Simulation](#simulation)
7. [Protokolle](#protokolle)
8. [CLI Terminal](#cli-terminal)
9. [Erweiterte Features](#erweiterte-features)
10. [Tastenkürzel](#tastenkürzel)
11. [Technische Details](#technische-details)

---

## Schnellstart

### Öffnen
```bash
firefox /home/steimer/workspace/quizzes/network-sim/index.html
```

### Erste Topologie erstellen

1. **Gerät auf Canvas ziehen** - Von der linken Geräteleiste auf den Arbeitsbereich ziehen
2. **Geräte verbinden** - Orange Punkte (Ports) anklicken und zu anderem Gerät ziehen
3. **IP-Adressen konfigurieren** - Gerät auswählen und IP eingeben
4. **PDU senden** - Toolbar "PDU" klicken, Quelle/Ziel wählen, Senden

---

## Gerätebibliothek

### Endgeräte

| Gerät | Ports | Beschreibung |
|-------|-------|--------------|
| PC | 1 | Desktop-Computer |
| Laptop | 1 | Tragbarer Computer |
| Tablet | 0 (WLAN) | Drahtloses Gerät |
| Drucker | 1 | Netzwerkdrucker |
| IP-Phone | 1 | VoIP Telefon (PoE) |

### Switches

| Gerät | Ports | PoE Budget | Beschreibung |
|-------|-------|------------|--------------|
| 2960-24 | 24 + 2 Uplink | - | Basis 24-Port Switch |
| 3560-24PS | 24 + 2 Uplink | 370W | PoE+ Switch |
| 3750-48P | 48 + 4 Uplink | 740W | High-PoE Switch |

### Router

| Gerät | Ports | Beschreibung |
|-------|-------|--------------|
| 1941 | 2 + 2 Uplink | Kompakt-Router |
| 2901 | 2 + 2 Uplink | Mid-Range Router |
| 4321 | 4 + 2 Uplink | Modular Router |

### PoE Geräte

| Gerät | Leistung | Beschreibung |
|-------|----------|--------------|
| IP-Kamera | 13W | Standard PoE Kamera |
| PTZ-Kamera | 60W | High-Power PTZ |
| WLAN-AP | 25W | Access Point |

### Server

| Gerät | Services | Beschreibung |
|-------|----------|--------------|
| Webserver | HTTP, HTTPS | Apache/NGINX Simulation |
| DNS Server | DNS | Nameserver |
| DHCP Server | DHCP | IP-Adressvergabe |
| Mailserver | SMTP, POP3 | E-Mail Dienste |

---

## Topologie erstellen

### Geräte platzieren

1. **Auswählen** - Gerät in linker Leiste anklicken
2. **Ziehen** - Auf Canvas im Arbeitsbereich ziehen
3. **Loslassen** - Gerät wird platziert

```
┌─────────────────────────────────────┐
│  Geräteleiste  │    Canvas         │
│  ┌──────────┐  │                   │
│  │  PC      │──┼──► ┌─────┐       │
│  └──────────┘  │    │ PC  │       │
│  ┌──────────┐  │    └──┬──┘       │
│  │ Switch   │──┼───────┤           │
│  └──────────┘  │       │           │
└─────────────────────────────────────┘
```

### Geräte bewegen

- **Klicken und Ziehen** - Funktioniert jederzeit, auch nach Verbinden
- Geräte sind frei positionierbar
- Verbindungslinien folgen automatisch

### Geräte löschen

- Gerät auswählen → "Gerät löschen" Button
- Oder Delete-Taste im Config-Tab

---

## Verbindungen

### Ports verbinden

1. **Port anklicken** - Orange Punkt am Gerät
2. **Ziehen** - Linie zum Ziel-Port
3. **Loslassen** - Verbindung wird hergestellt

```
    Gerät A                    Gerät B
   ┌─────┐                   ┌─────┐
   │  ●  │──────────────────│  ●  │  ← Ports verbinden
   │  ●  │                   │  ●  │
   │  ●  │                   │  ●  │
   └─────┘                   └─────┘
     Port 1  ──────────────►  Port 1
```

### Port-Typen

| Symbol | Typ | Farbe |
|--------|-----|-------|
| ● | Normal Port | Orange |
| ● | Uplink Port | Lila |
| ● | Verbunden | Grün |

### Verbindungsregeln

- Ports müssen kompatibel sein (kein Kupfer ↔ Glasfaser direkt)
- Max. Ports pro Gerät beachten
- Verbindungen können gelöscht werden (Gerät löschen)

---

## Konfiguration

### IP-Konfiguration

1. Gerät auswählen
2. Config-Tab öffnen
3. IP-Adresse eingeben

```
IP Adresse:     192.168.1.10
Subnetzmaske:    255.255.255.0 (/24)
Gateway:         192.168.1.1
DNS Server:      8.8.8.8
```

### Subnetzmasken

| Notation | Maske | Hosts |
|----------|-------|-------|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /16 | 255.255.0.0 | 65.534 |

### VLAN Konfiguration

Nur für Switches und Router verfügbar:

1. Config-Tab → VLAN ID wählen
2. Mode: Access oder Trunk

```
VLAN 1  - Default (alle Ports)
VLAN 10 - Verwaltung
VLAN 20 - Produktion
VLAN 30 - Gast
VLAN 99 - Management
```

---

## Simulation

### Simulation Panel

**Öffnen:** Toolbar → "Simulation" Button

Das Simulation Panel bietet erweiterte Kontrolle über Paket-Simulationen:

- **Filter nach Typ**: ICMP, ARP, DHCP, DNS, TCP, UDP
- **Filter nach Layer**: L3, L4, L7
- **PDU Information**: Detaillierte Paket-Info mit Hex-Dump
- **OSI Layer Visualisierung**: Zeigt aktive Schichten
- **Simulation Controls**: Play/Pause, Step, Reset, Burst
- **Speed Control**: Geschwindigkeit der Animation anpassen

### PDU senden

1. **Toolbar** → "PDU" Button
2. **Quelle wählen** - Absender-Gerät
3. **Ziel wählen** - Empfänger-Gerät
4. **Typ wählen** - ICMP, ARP, DHCP, etc.
5. **Layer wählen** - L3, L4, oder L7
6. **Senden** - Paket wird simuliert

### PDU-Typen

| Typ | Layer | Farbe | Beschreibung |
|-----|-------|-------|-------------|
| ICMP | L3 | 🟢 | Ping-Anfrage |
| ARP | L2 | 🟠 | MAC-Auflösung |
| DHCP | L7 | 🟡 | IP-Adressanfrage |
| DNS | L7 | 🟣 | Namensauflösung |
| HTTP | L7 | 🟠 | Web-Anfrage |
| TCP | L4 | 🔵 | Verbindungsaufbau |
| UDP | L4 | 🟡 | Datagramme |

### Packet Detail View

Klicke auf ein Paket in der Liste für detaillierte Informationen:

- **Source/Dest MAC**: Hardware-Adressen
- **Source/Dest IP**: Netzwerk-Adressen
- **Protocol**: PDU-Typ
- **Size**: Paketgröße in Bytes
- **Hex Dump**: Hexadezimale Darstellung
- **OSI Layers**: Visualisierung der aktiven Schichten

### Paketfluss beobachten

- Animierte Pakete zeigen Datenverkehr
- Farben zeigen Layer:
  - 🟡 Gelb = Layer 3 (L3)
  - 🟢 Grün = Layer 4 (L4)
  - 🔵 Blau = Layer 7 (L7)

---

## Protokolle

### STP (Spanning Tree Protocol)

**Aktivierung:** Toolbar → "STP" Button

**Funktion:**
- Verhindert Schleifen im Netzwerk
- Automatische Root-Switch Wahl (niedrigste MAC)
- Blockiert redundante Pfade

**Port-Zustände:**
```
Root Switch (★)    Designated    Alternate
     │                  │            │
     ▼                  ▼            ▼
  Forwarding  ◄──►  Forwarding    Blocking
```

### VLAN

**Konfiguration pro Gerät:**
- VLAN ID zuweisen
- Access Port = ein VLAN
- Trunk Port = mehrere VLANs

### NAT (Network Address Translation)

**Konfiguration:**
1. Router auswählen
2. NAT aktivieren
3. NAT-Tabelle zeigt Übersetzung

---

## CLI Terminal

### Öffnen

1. Gerät auswählen
2. Toolbar → "CLI" Button

### Verfügbare Befehle

| Befehl | Beschreibung |
|--------|--------------|
| `help` | Hilfe anzeigen |
| `show ip` | IP-Konfiguration |
| `show mac` | MAC-Adress-Tabelle |
| `show arp` | ARP-Tabelle |
| `show route` | Routing-Tabelle |
| `show vlan` | VLAN-Status |
| `show running-config` | Komplette Config |
| `exit` | Terminal schließen |

### CLI-Beispiel

```
> show ip
IP Address: 192.168.1.10
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.1.1

> show mac
0011.2233.4455  VLAN 1  Port 1
0066.7788.9900  VLAN 1  Port 2

> show route
0.0.0.0/0       *               Gi0/0
192.168.1.0/24  directly connected Gi0/1
```

---

## Erweiterte Features

### DHCP Server

1. **DHCP-Server platzieren**
2. **Server konfigurieren:**
   - IP: 192.168.1.100
   - Pool: LAN_POOL
   - Start: 192.168.1.100
   - Max: 50 Clients

### DHCP Request simulieren

```
1. PC ohne IP platzieren
2. PDU senden: Typ = DHCP Discover
3. Server vergibt IP automatisch
```

### Routing

**Statische Routen hinzufügen:**
1. Router auswählen
2. Route-Tab → "Route hinzufügen"
3. Netzwerk, Maske, Gateway eingeben

### Save/Load

**Speichern:**
1. Toolbar → Download-Icon
2. JSON-Datei wird heruntergeladen

**Laden:**
1. Toolbar → Upload-Icon
2. JSON-Datei auswählen
3. Topologie wird restauriert

---

## Tastenkürzel

| Taste | Funktion |
|-------|----------|
| Mittelklick + Ziehen | Canvas verschieben |
| Mausrad | Zoom |
| Delete | Gerät löschen |
| Escape | Auswahl aufheben |

---

## Technische Details

### Dateistruktur

```
network-sim/
├── index.html          # Hauptanwendung
├── DOCUMENTATION.md    # Diese Dokumentation
└── (Browser-Cache)    # Lokale Speicherung
```

### Berechnungen

**Dämpfung (Kupfer):**
```
Dämpfung = (22 dB / 100m) × Kabellänge
```

**PoE Budget:**
```
Verfügbar = Budget - Verwendet
```

### Browser-Anforderungen

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

**Benötigte Features:**
- ES6+ JavaScript
- CSS Grid & Flexbox
- SVG
- Drag & Drop API
- CSS Animations

### Performance

- Max. Geräte: ~100 (Browser-abhängig)
- Max. Verbindungen: ~500
- Empfohlen: < 50 Geräte für flüssige Animation

---

## Troubleshooting

### Problem: Gerät lässt sich nicht verbinden

**Lösung:**
- Freie Ports prüfen (grün = belegt)
- Gerät hat möglicherweise keine Ports frei

### Problem: PDU erreicht Ziel nicht

**Lösung:**
- Pfad vorhanden? (Verbindungen prüfen)
- IP-Adressen im gleichen Subnetz?
- STP blockiert Pfad? → STP ausführen

### Problem: Keine IP vom DHCP

**Lösung:**
- DHCP-Server muss konfiguriert sein
- Server und Client im gleichen Netzwerksegment

---

## Lizenz & Credits

**Entwickelt für:** ITSE IHK AP2 Prüfungsvorbereitung

**Verwendete Libraries:**
- Phosphor Icons (Icons)
- Panzoom (Canvas Zoom/Pan)

**Design:** Glassmorphism mit Gold-Akzent (#c9a227)

---

## Changelog

### v1.0 - Initial
- Gerätebibliothek
- Drag & Drop
- Port-Verbindungen
- IP-Konfiguration

### v1.1 - Erweitert
- PDU-Simulation
- STP
- VLAN
- CLI Terminal
- Save/Load

### v1.2 - Current
- Verbesserte Port-UX
- Quick-Connect Labels
- NAT/ACL Support
- Erweiterte CLI-Befehle
