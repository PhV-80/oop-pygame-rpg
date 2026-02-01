import pygame
from entities.entity import Entity


class NPC(Entity):
    """Non-player character (enemy). AI: Chase player."""

    def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
        super().__init__(x, y, width, height, color)
        self.speed = 3  # Movement speed (slower than player)
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

    def update(self, player_x: int, player_y: int):
        """
        Update NPC state: Chase the player.

        Args:
            player_x: Player's x position
            player_y: Player's y position
        """
        # Horizontal movement (chase player on X axis)
        if self.get_x() < player_x:
            self.set_x(self.get_x() + self.get_speed())
        elif self.get_x() > player_x:
            self.set_x(self.get_x() - self.get_speed())

        # Vertical movement (chase player on Y axis)
        if self.get_y() < player_y:
            self.set_y(self.get_y() + self.get_speed())
        elif self.get_y() > player_y:
            self.set_y(self.get_y() - self.get_speed())