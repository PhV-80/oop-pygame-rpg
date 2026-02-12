import pygame

from config import config

class Entity:
    """Base class for all game objects with encapsulated attributes."""

    def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
        """
        Initialize an entity with position, size and color.

        Args:
            x: Horizontal position (pixels)
            y: Vertical position (pixels)
            width: Width of the entity (pixels)
            height: Height of the entity (pixels)
            color: RGB tuple (r, g, b)
        """
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color

    # Getter methods
    def get_x(self) -> int:
        """Get horizontal position."""
        return self._x

    def get_y(self) -> int:
        """Get vertical position."""
        return self._y

    def get_width(self) -> int:
        """Get entity width."""
        return self._width

    def get_height(self) -> int:
        """Get entity height."""
        return self._height

    def get_color(self) -> tuple:
        """Get entity color."""
        return self._color

    # Setter methods
    def set_x(self, x: int):
        """Set horizontal position."""
        self._x = x

    def set_y(self, y: int):
        """Set vertical position."""
        self._y = y

    def set_width(self, width: int):
        """Set entity width."""
        self._width = width

    def set_height(self, height: int):
        """Set entity height."""
        self._height = height

    def set_color(self, color: tuple):
        """Set entity color."""
        self._color = color

    def update(self):
        """Update entity state. Override in subclasses."""
        pass

    def draw(self, screen: pygame.Surface):
        """
        Draw entity on screen.

        Args:
            screen: Pygame surface to draw on
        """
        pygame.draw.rect(screen, self.get_color(),
                         (self.get_x(), self.get_y(),
                          self.get_width(), self.get_height()))

    def check_collision(self, other) -> bool:
        """
        Check collision with another entity.

        Args:
            other: Another Entity object

        Returns:
            True if entities collide, False otherwise
        """
        return (self.get_x() <= other.get_x() + other.get_width() and
                self.get_x() + self.get_width() > other.get_x() and
                self.get_y() <= other.get_y() + other.get_height() and
                self.get_y() + self.get_height() > other.get_y())

    def clamp_to_bounds(self):
        """Clamp entity to bounds."""
        self._x = min(self.get_x(), self.get_x() + self.get_width())
        self._y = min(self.get_y(), self.get_y() + self.get_height())