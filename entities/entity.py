import pygame

class Entity:
    """Basis-Klasse für alle Spiel-Objekte mit Position und Rendering."""

    def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
        """
        Erstellt Entity mit Position, Größe und Farbe.

        Args:
            x: Horizontal-Position (Pixel)
            y: Vertikal-Position (Pixel)
            width: Breite (Pixel)
            height: Höhe (Pixel)
            color: RGB-Tuple (r, g, b)
        """
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color

    # Getter
    def get_x(self) -> int:
        """Gibt Horizontal-Position zurück."""
        return self._x

    def get_y(self) -> int:
        """Gibt Vertikal-Position zurück."""
        return self._y

    def get_width(self) -> int:
        """Gibt Breite zurück."""
        return self._width

    def get_height(self) -> int:
        """Gibt Höhe zurück."""
        return self._height

    def get_color(self) -> tuple:
        """Gibt Farbe zurück."""
        return self._color

    # Setter
    def set_x(self, x: int):
        """Setzt Horizontal-Position."""
        self._x = x

    def set_y(self, y: int):
        """Setzt Vertikal-Position."""
        self._y = y

    def set_width(self, width: int):
        """Setzt Breite."""
        self._width = width

    def set_height(self, height: int):
        """Setzt Höhe."""
        self._height = height

    def set_color(self, color: tuple):
        """Setzt Farbe."""
        self._color = color

    def update(self):
        """Update-Logik. Override in Subklassen."""
        pass

    def draw(self, screen: pygame.Surface):
        """
        Zeichnet Entity auf Screen.

        Args:
            screen: Pygame Surface zum Zeichnen
        """
        pygame.draw.rect(screen, self.get_color(),
                         (self.get_x(), self.get_y(),
                          self.get_width(), self.get_height()))

    def check_collision(self, other: 'Entity') -> bool:
        """
        Prüft Kollision mit anderer Entity.

        Args:
            other: Andere Entity

        Returns:
            True bei Kollision, sonst False
        """
        return (self.get_x() < other.get_x() + other.get_width() and
                self.get_x() + self.get_width() > other.get_x() and
                self.get_y() < other.get_y() + other.get_height() and
                self.get_y() + self.get_height() > other.get_y())