# OOP PyGame RPG - Vision

## Projekt-Ziel
Ein 2D-RPG mit dynamischer, emergenter Story basierend auf DSA/D&D-Regelwerk.

## Kern-Konzepte

### 1. Regelwerk-basiert (DSA/D&D)
- Attribute: Stärke, Geschick, Intelligenz, Weisheit, Charisma, Konstitution
- Skills: Kampf, Magie, Social, Handwerk
- Würfelwürfe bestimmen Erfolg/Misserfolg
- Kein Arcade-Gameplay, sondern Simulation

### 2. Dynamische Welt
- NPCs haben Ziele, Bedürfnisse, Zeitpläne
- Keine vorgeschriebenen Quests
- Events entstehen aus NPC-Interaktionen
- Spieler-Aktionen haben Konsequenzen

### 3. Emergente Story
- Story entsteht durch Spielmechanik
- Fraktionen reagieren auf Spieler
- NPCs erinnern sich an Spieler-Taten
- Jeder Playthrough ist anders

### 4. Soziale Simulation
- Fraktionen mit Beziehungen
- Reputation-System
- NPCs haben Meinungen über Spieler
- Dynamische Allianzen/Feindschaften

## Nicht-Ziele (Out of Scope)
- Keine 3D-Grafik
- Keine Multiplayer-Funktionen
- Kein Voice Acting
- Keine riesige Open World (erstmal 1 Stadt + Umgebung)

## Technische Basis
- Python + PyGame
- OOP-Architektur
- Turn-based oder Echtzeit-mit-Pause (noch zu entscheiden)
- 2D Sprite-Grafik (Placeholder: farbige Rechtecke)

## Inspiration
- Dwarf Fortress (Emergenz)
- Kenshi (Sandbox)
- Classic CRPGs (Baldur's Gate, Planescape)
- DSA/D&D Regelwerke

## Development Strategy

### Phase 1 (Completed): D&D Prototype

- **Regelwerk:** D&D 5e-inspired (Attributes, W20-System, Modifiers)
- **Zweck:** Rapid prototyping, bekannte Mechaniken
- **Status:** Functional, archived in `_archive/dnd_prototype/`

### Phase 2 (Current): JRPG System Refactoring

- **Ziel-Regelwerk:** JRPG-Style (Final Fantasy, Mystic Quest)
- **Features:**
    - Stats: HP, MP, Attack, Defense, Magic Attack, Magic Defense, Speed, Luck
    - Combat: Formula-based (no dice), Turn-Order-System
    - MP-System für Abilities/Magic
    - XP + Level-System mit Auto-Stat-Growth
    - Status Effects (Poison, Sleep, Paralysis)
- **Architektur:** Core-Module austauschbar (modular design)

### Begründung für D&D Prototype

D&D-Mechaniken wurden für Prototyp gewählt:

1. Gut dokumentiert, schnelle Implementierung
2. Zeigt Regelwerk-Architektur-Prinzipien
3. Funktioniert als Referenz-Implementation
4. **Erkenntniss:** Ziel ist JRPG-System → Refactoring gestartet
