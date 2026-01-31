import pygame

from config import *
from entities.entity import Entity


class Character(Entity):
    """Player character controlled by keyboard input (WASD or Arrow keys)."""

    def __init__(self, x: int, y: int, width: int, height: int, color):
        super().__init__(x, y, width, height, color)
        self.speed = 5  # Movement speed in pixels per frame
        self.health = 100

    def update(self):
        """Handle player movement and enforce window boundaries."""
        keys = pygame.key.get_pressed()

        # Movement controls (WASD or Arrow keys)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.speed

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.speed

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed

        # Boundary checks (prevent player from leaving the window)
        if self.x < 0:
            self.x = 0

        if self.x > WINDOW_WIDTH - self.width:
            self.x = WINDOW_WIDTH - self.width

        if self.y < 0:
            self.y = 0

        if self.y > WINDOW_HEIGHT - self.height:
            self.y = WINDOW_HEIGHT - self.height