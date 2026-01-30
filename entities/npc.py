import pygame

from config import *
from entities.entity import Entity


class NPC(Entity):
    """Non-player character (enemy). AI behavior not yet implemented."""

    def __init__(self, x: int, y: int, width: int, height: int, color):
        super().__init__(x, y, width, height, color)
        self.speed = 3  # Movement speed (slower than player)
        self.health = 100  # Hit points

    def update(self):
        """Update NPC state. AI logic will be added in Phase 1.3 Part 2."""
        pass  # Placeholder for future AI implementation