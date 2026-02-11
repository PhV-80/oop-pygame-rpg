# OOP PyGame RPG - Roadmap

## Phase 0: Projekt-Restrukturierung ✅
**Status:** In Arbeit (11.02.2026)

- [x] Branch `refactor/core-architecture` anlegen
- [x] Ordnerstruktur erstellen
- [x] Alten Code archivieren
- [x] Vision + Roadmap dokumentieren
- [ ] Commit + Push

**Aufwand:** 1h

---

## Phase 1: Regelwerk-Fundament
**Ziel:** DSA-Light-System implementieren

**Milestones:**
- [ ] `core/attributes.py` - 6 Basis-Attribute
- [ ] `core/skills.py` - 10 Skills mit Attribute-Boni
- [ ] `core/dice.py` - W20, W6, Modifikatoren
- [ ] `core/combat.py` - Angriff/Verteidigung/Schaden
- [ ] Konsolen-Test: Zwei Creatures kämpfen

**Geschätzte Zeit:** 8-12h
**Start:** KW 7/2026
**Status:** Geplant

---

## Phase 2: Creature + Player
**Ziel:** Spieler-Charakter mit Stats

**Milestones:**
- [ ] `entities/creature.py` - Entity + Stats kombiniert
- [ ] `entities/player.py` - Input + Creature
- [ ] Stats-UI (HP, Stamina, Attribute anzeigen)
- [ ] Bewegung mit Stamina-Kosten

**Geschätzte Zeit:** 6-8h
**Start:** KW 8/2026
**Status:** Geplant

---

## Phase 3: NPC-Grundlagen
**Ziel:** Erster simulierter NPC

**Milestones:**
- [ ] `entities/npc/npc_base.py` - AI-Basis
- [ ] `entities/npc/needs.py` - Hunger, Energy
- [ ] `entities/npc/behavior.py` - Goal-System
- [ ] Test-NPC: Villager sucht Essen bei Hunger

**Geschätzte Zeit:** 10-12h
**Start:** KW 9/2026
**Status:** Geplant

---

## Phase 4: Factions + Reputation
**Ziel:** NPCs gehören zu Gruppen

**Milestones:**
- [ ] `world/faction.py` - Fraktionen mit Beziehungen
- [ ] `world/reputation.py` - Spieler-Ruf pro Faction
- [ ] NPCs reagieren auf Reputation
- [ ] Test: Bandit töten → Wache mag Spieler

**Geschätzte Zeit:** 8-10h
**Start:** KW 10-11/2026
**Status:** Geplant

---

## Phase 5: Combat-Integration
**Ziel:** Kämpfe im Spiel ✨ PORTFOLIO-MILESTONE

**Milestones:**
- [ ] Kampf-Interface (Taste drücken = Angriff)
- [ ] Gegner-AI (greift feindliche Creatures an)
- [ ] Tod-System (HP = 0 → Entity entfernen)
- [ ] Reputation-Effekt bei Tötungen

**Geschätzte Zeit:** 12-15h
**Start:** KW 12-13/2026
**Status:** Geplant

**Hinweis:** Ab hier ist das Projekt portfolio-tauglich!

---

## Phase 6: Time + Schedule (Optional)
**Ziel:** Tag/Nacht-Zyklus

**Milestones:**
- [ ] `world/time_system.py` - 24h-Zyklus
- [ ] `entities/npc/schedule.py` - Tagesabläufe
- [ ] NPCs folgen Zeitplan
- [ ] Tag/Nacht-Grafik

**Geschätzte Zeit:** 10-12h
**Start:** Nach Umschulung
**Status:** Post-Launch

---

## Phase 7: Emergente Events (Optional)
**Ziel:** Dynamische Ereignisse

**Milestones:**
- [ ] `world/events.py` - Event-System
- [ ] Beispiel-Event: Banditenüberfall
- [ ] Spieler-Einfluss auf Events
- [ ] Event-Konsequenzen

**Geschätzte Zeit:** 15-20h
**Start:** Nach Umschulung
**Status:** Post-Launch

---

## Aktuelle Priorität
**Fokus:** Phase 1 (Regelwerk)
**Nächster Schritt:** `core/attributes.py` implementieren
