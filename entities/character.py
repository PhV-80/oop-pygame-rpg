import pygame
from config import config
from entities.entity import Entity


class Character(Entity):
    """Player character controlled by keyboard input (WASD or Arrow keys)."""

    def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
        super().__init__(x, y, width, height, color)
        self.speed = 5  # Movement speed in pixels per frame
        self.health = 100  # Hit points

    # Getter methods (zusätzlich zu Entity)
    def get_speed(self) -> int:
        """Get movement speed."""
        return self.speed

    def get_health(self) -> int:
        """Get current health."""
        return self.health

    # Setter methods (zusätzlich zu Entity)
    def set_speed(self, speed: int):
        """Set movement speed."""
        if speed >= 0:
            self.speed = speed

    def set_health(self, health: int):
        """Set health (clamped to 0-100)."""
        self.health = max(0, min(100, health))

    def update(self):
        """Handle player movement and enforce window boundaries."""
        keys = pygame.key.get_pressed()

        # Movement controls (WASD or Arrow keys)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.set_y(self.get_y() - self.get_speed())
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.set_y(self.get_y() + self.get_speed())
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.set_x(self.get_x() - self.get_speed())
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.set_x(self.get_x() + self.get_speed())

        # Boundary checks (prevent player from leaving window)
        if self.get_x() < 0:
            self.set_x(0)
        if self.get_x() > config.get_window_width() - self.get_width():
            self.set_x(config.get_window_width() - self.get_width())
        if self.get_y() < 0:
            self.set_y(0)
        if self.get_y() > config.get_window_height() - self.get_height():
            self.set_y(config.get_window_height() - self.get_height())