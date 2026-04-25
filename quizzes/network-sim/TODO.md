# Network Simulator Pro - TODO

## ✅ Completed Features

### Core
- [x] Drag & Drop devices from panel to canvas
- [x] **Devices stay draggable after placement** - always works!
- [x] **Port dragging for connections** - click port, drag to target port
- [x] 4 Cable types: Copper Straight, Crossover, Fiber, Serial
- [x] Connection preview line while dragging
- [x] Quick connect labels showing target

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
- [x] Connection labels
- [x] Delete zone visual
- [x] **Keyboard shortcuts**: Ctrl+S (Save), Ctrl+O (Open), Ctrl+P (PDU), Ctrl+T (Traffic), Ctrl+V (VTP), Ctrl+H (HSRP), Ctrl+L (Syslog)
- [x] **Interface configuration** (bandwidth, delay, description)

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
