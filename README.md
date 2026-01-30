# OOP PyGame RPG

A learning project demonstrating Object-Oriented Programming (OOP) principles in Python using PyGame. Created as part of a vocational training program (Fachinformatiker Anwendungsentwicklung).

## Project Goal

Build a simple top-down RPG to showcase:
- Class inheritance and polymorphism
- Game loop architecture
- Entity-based game design

## Current Features

### Phase 1.1: Core Architecture ✅
- Base `Entity` class for all game objects
- PyGame window and game loop setup
- Configuration system for constants

### Phase 1.2: Player Movement ✅
- `Character` class inheriting from `Entity`
- WASD/Arrow key movement
- Boundary collision (player cannot leave the window)

### Phase 1.3: NPC System (Part 1) ✅
- `NPC` base class inheriting from `Entity`
- Multiple NPC instances rendered on screen
- Attributes: speed, health

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
