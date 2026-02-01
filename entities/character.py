import pygame

from config import *
from entities.entity import Entity


class Character(Entity):
    """Player character controlled by keyboard input (WASD or Arrow keys)."""

    def __init__(self, x: int, y: int, width: int, height: int, color: tuple[int, int, int], damage: int):
        super().__init__(x, y, width, height, color, damage)
        self.speed = 5  # Movement speed in pixels per frame

    def update(self):
        """Handle player movement and enforce window boundaries."""
        keys = pygame.key.get_pressed()

        # Movement controls (WASD or Arrow keys)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.set_y(self.get_y() - self.speed)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.set_y(self.get_y() + self.speed)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.set_x(self.get_x() - self.speed)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.set_x(self.get_x() + self.speed)

        # Boundary checks (prevent player from leaving the window)
        if self.get_x() < 0:
            self.set_x(0)

        if self.get_x() > WINDOW_WIDTH:
            self.set_x(WINDOW_WIDTH)

        if self.get_y() < 0:
            self.set_y(0)

        if self.get_y() > WINDOW_HEIGHT:
            self.set_y(WINDOW_HEIGHT)