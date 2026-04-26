# Network Simulator Pro - TODO

## ✅ Completed Features

### Core
- [x] Drag & Drop devices from panel to canvas
- [x] **Devices stay draggable after placement** - always works!
- [x] **Port dragging for connections** - click port, drag to target port
- [x] **Improved port UX** - larger ports, labels on hover
- [x] 4 Cable types: Copper Straight, Crossover, Fiber, Serial
- [x] Connection preview line while dragging
- [x] Quick connect labels showing target
- [x] **Device Inspector Panel** - detailed device info

### Devices (25+)
- [x] End devices: PC, Laptop, Tablet, Printer, Server, IP Phone
- [x] Switches: 2960-24TT, 2960-24GP, 3560-24PS, 3560-48PS, 3750-48P
- [x] Routers: 1941, 2901, 4321, 4331
- [x] PoE devices: IP Camera, PTZ Camera, WLAN AP
- [x] Servers: HTTP, DNS, DHCP, Mail, FTP, AAA
- [x] WAN: Cloud, DSL Modem, Cable Modem, ISDN NT

### Routing & Protocols
- [x] Static Routes
- [x] RIP (Routing Information Protocol)
- [x] OSPF (Open Shortest Path First)
- [x] EIGRP (Enhanced IGRP)
- [x] Route type badges (C, S, R, O, D)
- [x] Routing table display

### Switch Features
- [x] VLAN configuration (1, 10, 20, 30, 40, 99, 100)
- [x] Port modes: Access, Trunk, Dynamic
- [x] STP (Spanning Tree Protocol) with root bridge election
- [x] Port Security (max MAC, violation actions)
- [x] EtherChannel (LACP, PAgP modes)
- [x] Native VLAN for trunks
- [x] **VTP (VLAN Trunking Protocol)** - Server/Client/Transparent

### Network Services
- [x] DHCP Pool configuration
- [x] DHCP Relay (ip helper-address)
- [x] NAT configuration
- [x] ACL (Standard and Extended)
- [x] QoS settings
- [x] **HSRP (Hot Standby Router Protocol)** - Gateway redundancy
- [x] **Syslog Viewer** - Facility/Severity filtering
- [x] **SSH/Telnet** - Remote access simulation

### Simulation
- [x] PDU types: ICMP, ARP, DHCP, DNS, HTTP, TCP, UDP
- [x] OSI Layer selection (L3, L4, L7)
- [x] Packet capture list
- [x] Packet detail view with hex dump
- [x] Path animation
- [x] Realtime vs Simulation mode
- [x] **Traffic Generator** (continuous packet generation)
- [x] **Ping Results** with detailed statistics
- [x] **Repeat packets** with configurable interval

### Workspace
- [x] Logical view
- [x] Physical view with rack representation
- [x] Config view
- [x] Fit all devices in view
- [x] Zoom in/out with mouse wheel

### CLI
- [x] Cisco IOS-like commands
- [x] Show commands: ip, mac, arp, route, vlan, interfaces
- [x] Configuration: ip address, no shutdown
- [x] Routing protocol commands
- [x] **CDP (Cisco Discovery Protocol)** neighbor discovery

### UI/UX
- [x] Glassmorphism design
- [x] Golden accent theme
- [x] Event log
- [x] Status bar
- [x] Device info on hover
- [x] Connection labels with bandwidth
- [x] Delete zone visual
- [x] **Keyboard shortcuts**: Ctrl+S/O/P/T/V/H/L/Z/Y/D
- [x] **Interface configuration** (bandwidth, delay, duplex, speed, MTU)
- [x] **Undo/Redo** system (50 states)
- [x] **Snap to Grid** toggle
- [x] **Mini-map** overview
- [x] **Right-click context menu**
- [x] **Lasso multi-selection** (Shift+Drag)
- [x] **Topology tree** panel
- [x] **OSI layer visualization** during simulation
- [x] **Device power toggle**
- [x] **Port LED status** indicators
- [x] **VLAN tags** on connections
- [x] **Device Inspector panel** - full device details
- [x] **Packet History panel** - detailed packet list
- [x] **Port tooltips** - connection info
- [x] **Auto-naming** devices (PC0, Switch0, Router0...)
- [x] **Interface Statistics** - In/Out bytes tracking
- [x] **VLAN Table** - all VLANs with status
- [x] **Network Health Dashboard** - uptime, links, delivery
- [x] **ARP Table** - IP/MAC, auto-populated
- [x] **Device search/filter** in panel
- [x] **Quick Templates** - 6 pre-made topologies
- [x] **Traffic animation** on connections
- [x] **Device status badges** (online/offline)
- [x] **MAC Address Table** - dynamic learning, VLAN filter
- [x] **Routing Table** - protocol badges (C/S/O/L), metrics
- [x] **NAT Translations** panel - Inside/Outside IP, protocols
- [x] **Enhanced packet animation** - type colors, trail effects, burst arrival
- [x] **Packet labels** - shows type during animation
- [x] **Device labels** - shows hop names during animation
- [x] **Realistic front panels** - hardware-style device views
- [x] **Port LED indicators** - green=up, dark=down
- [x] **System LEDs** - power, PoE, activity, speed
- [x] **Panel labels** - device type identification
- [x] **Auto-Save** to localStorage (every 30s)
- [x] **Export as PNG** image
- [x] **Center selected** (C key)
- [x] **Extended shortcuts**: F, C, R, G, N, L keys
- [x] **Auto-Forward simulation** - automatic packet generation
- [x] **Simulation controls** - Play/Pause/Step/Speed
- [x] **Enhanced status bar** - Geräte/Links/PKTs counters
- [x] **QoS Policy panel** - traffic prioritization queues
- [x] **Wireless Networks** - SSID, channel, security config
- [x] **Connection Details panel** - click to view/edit/delete connections
- [x] **STP Panel** - spanning tree protocol visualization
- [x] **Root bridge selection** - auto or manual
- [x] **Port states** - FWD/BLK with role display
- [x] **DNS Panel** - domain resolution, static records
- [x] **Device Labels** - IP/name below devices (toggle)
- [x] **Network Clock** - simulation time with sync
- [x] **Topology Notes** - document topologies, save/export notes
- [x] **Help Tutorial** - quick start guide modal
- [x] **Improved port UX** - highlighting, animations, ESC to cancel
- [x] **8 Quick Templates** - including Full Network, Data Center
- [x] **Welcome modal** for first-time users
- [x] **Device hover tooltip** - quick info on mouseover
- [x] **Network Summary panel** - device/cable breakdown statistics
- [x] **Selection glow animation** - pulsing glow on selected devices
- [x] **Smart port highlighting** - available ports glow green
- [x] **Quick actions bar** - Connect/Config/Delete buttons
- [x] **Improved port LEDs** - larger, better styling, blink animation
- [x] **Color-coded bandwidth** - gigabit/fast/slow indicators
- [x] **Spark effect** on successful connections
- [x] **Tips banner** - quick reference on startup
- [x] **Interface Statistics with traffic graphs** - detailed in/out monitoring
- [x] **Duplicate device** - right-click to copy
- [x] **Quick VLAN assignment** - popup with presets
- [x] **Keyboard shortcuts** - Ctrl+D, +/-, Home, etc.
- [x] **Favorites bar** - quick access to common devices
- [x] **Zoom slider** with +/- buttons in toolbar
- [x] **Enhanced status bar** - devices, connections, online count
- [x] **Improved drag UX** - scale, shadow, landing animations
- [x] **Target port highlighting** - pulsing green when connecting
- [x] **Snap guides** - grid alignment lines while dragging
- [x] **Alignment helpers** - snap to other devices
- [x] **Animated connection preview** - dashed moving line
- [x] **Align selected devices** - left, distribute horizontally/vertically
- [x] **Improved connection tooltip** - shows cable type, valid indicator
- [x] **Connection distance indicator** - shows pixel distance on cables
- [x] **Connection quality indicator** - shows signal quality %
- [x] **Port labels on cables** - shows F0/0 etc on endpoints
- [x] **Cable type button** - shows current type with color coding
- [x] **Improved connection hover** - thicker line, glow effect
- [x] **Keyboard shortcuts modal** - shows all shortcuts
- [x] **Space = Play/Pause** - toggle auto-forward
- [x] **Auto-Configure** - automatic IP assignment
- [x] **Network health check** - periodic diagnostics
- [x] **Playwright tests** - 6 tests for basic functionality
- [x] **Enhanced Simulation Panel** - filterable by type/layer, PDU info, hex dump
- [x] **Activity Mode** - Guided exercises with checklist
- [x] **CDP Neighbors Panel** - Show neighbor devices
- [x] **ACL Panel** - Access Control List viewer
- [x] **Path Trace Panel** - Route visualization with hops, latency, bandwidth
- [x] **QoS Queue Visualization** - Priority/High/Normal/Low queue status
- [x] **Interface Status Grid** - Auto-negotiation, speed, duplex, CRC stats
- [x] **Running Config View** - CLI show running-config command with full config
- [x] **Extended Cable Types** - Console (RJ45), Coaxial (BNC) cable options
- [x] **Improved Drag UX** - Drop zone indicators, snap guides enhancement, ghost elements
- [x] **SSH/Telnet Status** - Connection indicator with animation, session status
- [x] **IoT Devices** - Smart TV, Smart Light, Thermostat, Smart Speaker
- [x] **Device Search & Filters** - Quick filter buttons, search box
- [x] **Enhanced Context Menu** - VLAN submenu, power toggle, SSH access
- [x] **Enhanced Mini-map** - Clickable navigation, device type colors, connections
- [x] **Enhanced Health Dashboard** - Score display, stats grid (devices/links/online)
- [x] **Keyboard Shortcuts Panel** - Categorized shortcuts, better UI
- [x] **Connection Quality Indicators** - Bandwidth display, quality dots, packet flow animation
- [x] **Enhanced Port Status Panel** - Summary stats, port status LEDs, bandwidth display
- [x] **Improved Drag UX** - Scale/shadow during drag, enhanced landing animation, guide pulse
- [x] **Selection Box** - Click and drag to select multiple devices
- [x] **Enhanced Network Templates** - 11 templates, auto-connect, device count display
- [x] **Enhanced Undo/Redo** - State labels, history count, better tooltips
- [x] **Enhanced Port Security** - Sticky MAC, aging time, static MAC, live config preview
- [x] **Enhanced Traffic Generator** - Protocol options, packet size, bandwidth, preview
- [x] **Enhanced Network Summary** - Health score, device breakdown, IP/services, export report
- [x] **Quick Config Wizard** - Step-by-step IP configuration, subnet selection, router config
- [x] **Enhanced Device Tooltip** - Detailed info (IP, MAC, Gateway, Subnet, Status)
- [x] **JSON Export/Import** - Full topology save/load, settings preservation
- [x] **Device Grouping** - Group selected devices, visual grouping, toolbar buttons
- [x] **Auto-Layout** - Layer-based layout, tree layout algorithms, toolbar buttons
- [x] **Zoom to Selection** - Zoom controls, breadcrumb navigation, device zoom
- [x] **Layer Visualization** - Core/Distribution/Access layers, layer indicators, toggle button
- [x] **Packet Tracer Port Interface** - Enhanced port display, status indicators, hover effects
- [x] **IP Address Planning Panel** - Subnet overview, host list, IP range display
- [x] **Enhanced Wireless AP** - SSID, Security (WPA2/WPA3/WEP), Channel, Bandwidth settings
- [x] **Enhanced Cable Panel** - Bandwidth specs, connection recommendations, visual improvements
- [x] **Real-time Statistics** - Traffic in/out, CPU load, error counter in status bar
- [x] **Enhanced Device Inspector** - Detailed device info, connections list, quick actions
- [x] **Auto-Save History** - Version history, load/delete previous saves, toolbar button
- [x] **Enhanced Templates** - 14 templates with categories (Basic/Enterprise/WAN/Special)
- [x] **Enhanced CLI** - Tab completion, command history (↑↓), suggestions, hostname display
- [x] **Connection Quality Simulation** - Latency, bandwidth, packet loss, quality metrics
- [x] **Device Customization** - Icon color, label type, port visibility
- [x] **Diagram Annotations** - Draggable notes, editable text, add/delete annotations
- [x] **Packet Capture Modal** - Wireshark-style capture, filters, export CSV
- [x] **Interface Status Dashboard** - Per-device port status, speed, latency, refresh
- [x] **Config Diff Tool** - Compare running configs between devices, side-by-side view
- [x] **Topology Map View** - Hierarchical topology display, layer visualization, SVG export
- [x] **Event Log Panel** - Real-time event logging, filter, export CSV, clear
- [x] **Security Audit Panel** - Security score, checks (SSH/VLAN/ACL/PortSec), export report
- [x] **Device Comparison Tool** - Side-by-side device comparison, property highlighting
- [x] **Bandwidth Monitor** - Real-time bandwidth usage, utilization %, chart, link stats
- [x] **Documentation Generator** - Markdown/HTML export, topology, devices, IP schema, VLANs
- [x] **Network Calculator** - Subnet mask, CIDR, broadcast, host range calculation
- [x] **VLAN Manager** - Create/delete VLANs, assign devices, view by VLAN, status
- [x] **Route Table Viewer** - View/add/delete routes, static/RIP/OSPF/EIGRP types
- [x] **Ping/Traceroute Tool** - Network diagnostics, hop tracking, latency display
- [x] **MAC Address Table** - View/clear MAC table, VLAN/Interface/Type columns
- [x] **DHCP Pool Viewer** - Create pools, view leases, simulate DHCP
- [x] **Spanning Tree Panel** - STP status, port states (Forwarding/Blocking), roles, cost
- [x] **CDP/LLDP Neighbors** - View neighbors, CDP/LLDP toggle, capability/platform info
- [x] **ARP Table** - View/clear ARP cache, IP/MAC/Interface/Type columns
- [x] **Interface Configuration** - Port settings, speed/duplex, bandwidth, enable/disable
- [x] **ACL Manager** - Standard/Extended ACLs, add/delete entries, apply to router
- [x] **NAT Configuration** - Static/dynamic NAT, translations, enable/disable
- [x] **Quick Commands** - One-click CLI commands for router/switch/server
- [x] **Network Testing** - Connectivity, DHCP, DNS, VLAN tests
- [x] **Device Status Overview** - Network statistics, device types, online/offline status
- [x] **QoS Configuration** - Priority queuing, bandwidth allocation, queue management
- [x] **Syslog Viewer** - System logs, level filtering, export, clear
- [x] **Favorite Templates** - Save/load topologies, localStorage persistence
- [x] **Device Template Editor** - Save/load device configs, apply to devices
- [x] **Port Mirroring** - SPAN sessions, source/destination ports, traffic monitoring

### Templates
- [x] Basic LAN (2 PCs, 1 Switch)
- [x] Router LAN (2 PCs, 1 Switch, 1 Router)
- [x] Corporate Network (4 PCs, 2 Switches, 1 Router, 1 Server)
- [x] WAN Link (2 Routers, Cloud)
- [x] PoE Network (PC, PoE Switch, Camera, AP)

### Save/Load
- [x] Export topology as JSON
- [x] Import topology from JSON

---

## 🔄 In Progress

### Potential Enhancements
- [ ] VLAN trunking protocol (VTP)
- [ ] Inter-VLAN routing simulation
- [ ] Dynamic routing protocol convergence visualization
- [ ] More realistic packet headers
- [ ] Traffic generator/simulator
- [ ] Bandwidth/delay simulation on links

---

## 🎯 Future Ideas

### Advanced
- [ ] Wireless association simulation
- [ ] MPLS labels visualization
- [ ] BGP routing support
- [ ] VPN tunnel simulation
- [ ] Multi-area OSPF visualization

### Education
- [ ] Quiz mode with questions
- [ ] Packet tracer activity compatibility
- [ ] Step-by-step tutorials
- [ ] Protocol packet structure viewer
- [ ] CCNA exam practice mode

### UI
- [ ] Mini-map for navigation
- [ ] Undo/Redo support
- [ ] Layer visibility toggles
- [ ] Custom device icons
- [ ] Dark/Light theme toggle

### Integration
- [ ] Export to Packet Tracer format
- [ ] Import from real network data
- [ ] Packet capture file export (PCAP)
- [ ] Topology diagram export (PNG/SVG)

---

## 🐛 Known Issues

- [ ] Large topologies may have performance issues
- [ ] Some Safari compatibility issues with drag-drop

---

**Last Updated:** 2026-04-26
**Version:** 1.2
