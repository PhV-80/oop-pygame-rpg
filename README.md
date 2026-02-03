# OOP PyGame RPG

A learning project demonstrating Object-Oriented Programming (OOP) principles in Python using PyGame. Created as part of a vocational training program (Fachinformatiker Anwendungsentwicklung).

## Project Goal

Build a simple top-down RPG to showcase:
- Class inheritance and polymorphism
- Game loop architecture
- Entity-based game design

## Current Features

### Phase 1.1: Core Architecture
- Base `Entity` class for all game objects
- PyGame window and game loop setup
- Configuration system for constants

### Phase 1.2: Player Movement
- `Character` class inheriting from `Entity`
- WASD/Arrow key movement
- Boundary collision (player cannot leave the window)

### Phase 1.3: NPC System (Part 1)
- `NPC` base class inheriting from `Entity`
- Multiple NPC instances rendered on screen
- Attributes: speed, health

### Phase 1.3.1 - Encapsulation Refactoring
**Branch:** `refactors/encapsulation`

Applied strict OOP encapsulation principles:
- **Getter/Setter Pattern**: All class attributes accessed via methods (`get_x()`, `set_x()`)
- **Config Class**: Game constants wrapped in configuration class with getters
- **Validation**: Health clamped to 0-100, speed validated >= 0
- **Consistency**: Umschulung-style encapsulation (no `_` prefix) applied project-wide

**Modified Files:**
- `config.py` - Converted to Config class with singleton pattern
- `entities/entity.py` - Added getter/setter methods for all attributes
- `entities/character.py` - Refactored movement and boundaries with getters/setters
- `entities/npc.py` - Chase AI uses encapsulation pattern
- `main.py` - All direct attribute access replaced with method calls

## Installation

### Requirements
- Python 3.10+
- PyGame

### Setup
```bash
# Clone repository
git clone https://github.com/PhV-80/oop-pygame-rpg.git
cd oop-pygame-rpg

# Install dependencies
pip install pygame

# Run the game
python main.py
```

## Project Structure
```text
oop-pygame-rpg/
├── entities/
│   ├── __init__.py
│   ├── entity.py       # Base class for all game objects
│   ├── character.py    # Player character (controllable)
│   └── npc.py          # Non-player characters
├── config.py           # Game constants (window size, colors, FPS)
└── main.py             # Entry point, game loop
```

## Class Hierarchy
```text
Entity (Base)
├── Character (Player)
└── NPC (Enemies)
```

## Roadmap
### Phase 1.3 Part 2: NPC AI
* NPCs follow the player
* Simple pathfinding logic

### Phase 1.4: Collision System
* Detect collision between player and NPCs
* Game over state on collision

### Phase 1.5: Basic UI
* Display health/score
* Simple HUD

### Phase 2: Game Mechanics (Future)
* Damage system
* Items and inventory
* Multiple enemy types (Goblin, Orc)
* Level/map system

### Phase 3: Persistence (Future)
* Save/load game state (JSON)
* Player progress tracking

## Controls
* WASD or Arrow Keys: Move player
* ESC: Quit game (not yet implemented)

## Learning Resources
This project follows standard PyGame patterns:
* [PyGame Documentation](https://www.pygame.org/docs/)
* [Game Loop Pattern](https://gameprogrammingpatterns.com/game-loop.html)

## License
Educational project - free to use and modify.

## Author
PhaseV80
