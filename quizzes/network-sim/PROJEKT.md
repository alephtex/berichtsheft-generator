# Network Simulator Pro - Projekt

> Browser-basierter Netzwerk-Simulator inspiriert von Cisco Packet Tracer

## 🎯 Ziel

Ein vollständiger, in HTML/CSS/JavaScript implementierter Netzwerk-Simulator für:
- **ITSE IHK AP2 Prüfungsvorbereitung**
- **CCNA Zertifizierungsvorbereitung**
- **Netzwerk-Grundlagen Training**

## 📁 Projektstruktur

```
network-sim/
├── index.html          # Hauptanwendung (Single Page App)
├── DOCUMENTATION.md    # Detaillierte Dokumentation
├── TODO.md            # Feature-Tracking
├── README.md          # Kurze Einführung
└── PROJEKT.md         # Dieses Dokument
```

## 🔗 Git Repository

**Remote:** `https://github.com/steimbyte/berichtsheft-generator.git`  
**Branch:** `feature/packet-tracer-parity`  
**Pfad:** `quizzes/network-sim/`

**Public URL:** https://github.com/steimbyte/berichtsheft-generator/tree/feature/packet-tracer-parity/quizzes/network-sim

## 🚀 Quick Start

```bash
# Öffnen im Browser
firefox /home/steimer/workspace/quizzes/network-sim/index.html

# Oder via Python Server
cd /home/steimer/workspace/quizzes/network-sim
python3 -m http.server 8080
# Dann: http://localhost:8080
```

## 📊 Feature Matrix (vs Cisco Packet Tracer)

| Feature | Packet Tracer | NetSim Pro | Status |
|---------|--------------|------------|--------|
| Geräte ziehen | ✅ | ✅ | Done |
| Port-Verbindung | ✅ | ✅ | Done |
| Kabeltypen | ✅ | ✅ | Done |
| IP Konfiguration | ✅ | ✅ | Done |
| Routing Protokolle | ✅ | ✅ | RIP/OSPF/EIGRP |
| VLAN | ✅ | ✅ | Done |
| STP | ✅ | ✅ | Done |
| Port Security | ✅ | ✅ | Done |
| DHCP | ✅ | ✅ | Done |
| NAT/ACL | ✅ | ✅ | Done |
| CLI | ✅ | ✅ | Basic |
| PDU Simulation | ✅ | ✅ | Done |
| Paket-Details | ✅ | ⚠️ | Hex Dump |
| Physical View | ✅ | ⚠️ | Basic Rack |
| Wireless | ✅ | ❌ | - |
| Multiuser | ✅ | ❌ | - |

## 🛠️ Technologie

- **Frontend:** Vanilla HTML5, CSS3, JavaScript ES6+
- **Icons:** Phosphor Icons (CDN)
- **Zoom/Pan:** Panzoom Library (CDN)
- **Fonts:** Google Fonts (Outfit, Space Grotesk, Fira Code)
- **Kein Build-Prozess** - läuft direkt im Browser

## 📈 Entwicklung

### Commit History
```
c9b4769 feat: v5.5 Interface Status + Auto-Negotiation
9560dde feat: v5.4 QoS Queue Visualization
58c6b46 feat: v5.3 Path Trace Panel + Physical Rack View
1eda4ad feat: v5.2 ACL Panel + Interface Security
5017039 feat: v5.1 CDP Neighbors Panel + VTP Configuration
b29e511 feat: v5.0 Activity Mode + Network Clock
6ae6147 feat: Enhanced Simulation Panel v4.9
29b2a19 docs: Update version to 4.8, add test info
c2d114b test: Add Playwright tests for NetSim Pro
906c3ae feat: Add auto-configure network, health check
be8145c feat: Add keyboard shortcuts modal, fit to selection, more shortcuts
7384c84 feat: Add cable type selector, improved connection styling
cc78094 feat: Add connection distance/quality indicators, alignment shortcuts
4602ae1 feat: Add align selected devices, improved connection tooltip
908328b feat: Add snap guides, alignment helpers, improved connection preview
62aa9ca feat: Improve drag UX, target port highlighting, better animations
caf5fe1 feat: Add zoom slider, enhanced status bar, device/connection counts
a21aae7 feat: Add keyboard shortcuts, favorites section, zoom controls
5f47028 feat: Add duplicate device, Quick VLAN assignment, improved power button
9914515 feat: Enhanced interface statistics with traffic graphs
587fc9f feat: Add spark effect on connection, tips banner
a32be84 feat: Improve port LED styling, add LED animation
02088e9 feat: Smart port highlighting, quick actions bar, connection animations
c51985a feat: Add Network Summary panel, selection glow animation
701e67c feat: Add device hover tooltip with quick info
d19da60 feat: Add more templates, welcome modal for new users
7972b48 feat: Improved port connection UX, visual guides
4ca732b feat: Add topology notes panel, help tutorial modal
a9adaac feat: Add network clock panel with time synchronization
523271d feat: Add DNS panel, device labels toggle
db34837 feat: Add STP panel with spanning tree visualization
70b5dbd feat: Connection details panel, enhanced connection visualization
83c2ecc feat: Add QoS policy, wireless network, STP, DNS
42e0a31 feat: Auto-forward simulation, simulation controls, enhanced status bar
72a2e86 feat: Add auto-save, export image, center view, keyboard shortcuts
e89c122 feat: Realistic device front panels, port LEDs, system LEDs
be36294 feat: Enhanced packet animation, NAT table, trail effects
0ee51ee feat: Add MAC address table, routing table, VLAN filter
a9d9284 feat: Add device search, quick templates, traffic animation, status badges
da55ba6 feat: Add interface stats, VLAN table, health dashboard, ARP table
cdafc89 feat: Add packet history, port tooltips, auto-naming
8e438da feat: Improved port UX, device inspector panel
c92e19d feat: Add topology tree, OSI layers, interface duplex/speed
199e9fa feat: Major UI/UX improvements
a805861 feat: Add Traffic Generator, CDP, Ping results, Interface config
7554f1e docs: Update documentation with all new features
3969139 feat: Add DHCP relay, EtherChannel, QoS, Port Security
395dc6e feat: Add routing protocols, physical workspace, DHCP pools
8bde292 feat: Major UI/UX improvements
b095704 Initial network simulator state
```

### Branches
- `master` - Stable releases
- `feature/packet-tracer-parity` - Active development

### Workflow
1. Feature entwickeln
2. Lokal testen
3. Commit mit aussagekräftiger Nachricht
4. Push zum Remote
5. PR erstellen (optional)

## 🎨 Design System

### Farben
```css
--accent: #c9a227       /* Gold - Primary */
--bg-deep: #0a0a0f      /* Dark Background */
--copper: #e07020       /* Copper Cable */
--fiber: #4080c0        /* Fiber Cable */
--ok: #5a8a6a          /* Success/Connected */
--error: #c04040        /* Error/Blocked */
```

### Icons (Phosphor)
- `ph-desktop` - PC
- `ph-laptop` - Laptop
- `ph-globe` - Router
- `ph-git-branch` - Switch
- `ph-hard-drives` - Server
- `ph-video-camera` - IP Camera
- `ph-wifi-high` - WLAN AP

## 📚 Lernressourcen

### Für ITSE AP2
- OSI Schichten verstehen
- IP-Adressierung (Subnetting)
- VLAN Konzepte
- Routing Grundlagen

### Für CCNA
- Spanning Tree Protocol
- Router Konfiguration
- Access Control Lists
- NAT/VLAN

## 🔧 Debugging

### Console öffnen
`F12` → Console Tab

### Häufige Probleme
1. **Gerät lässt sich nicht platzieren** → Browser Console prüfen
2. **Verbindung funktioniert nicht** → IP-Adressen prüfen
3. **Ports nicht sichtbar** → Zoom prüfen

### Logs
Event Log im rechten Panel zeigt alle Aktionen

## 📄 Lizenz

Entwickelt für Bildungszwecke.

## 👤 Autor

Benjamin Steimer  
ITSE IHK AP2 Projekt

---

**Version:** 5.45  
**Letzte Änderung:** 2026-04-26  
**Status:** 🟢 Aktiv
