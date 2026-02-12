from core.attributes import Attributes
from .entity import Entity


class Creature(Entity):
    """Lebewesen mit Attributen und HP-System."""

    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, attributes: Attributes):
        """
        Erstellt Creature mit Position und Stats.

        Args:
            x: Horizontal-Position
            y: Vertikal-Position
            width: Breite
            height: Höhe
            color: RGB-Farbe
            attributes: Attributes-Objekt (STR, DEX, etc.)
        """
        super().__init__(x, y, width, height, color)
        self._attributes = attributes

        con_mod = attributes.get_modifier('constitution')
        self._max_hp = 10 + (con_mod * 2)
        self._current_hp = self._max_hp

    def get_hp(self) -> int:
        """Gibt aktuelle HP zurück."""
        return self._current_hp

    def get_max_hp(self) -> int:
        """Gibt maximale HP zurück."""
        return self._max_hp

    def get_attributes(self) -> Attributes:
        """Gibt Attributes-Objekt zurück."""
        # TODO
        return self._attributes

    def take_damage(self, amount: int):
        """
        Nimmt Schaden.

        Args:
            amount: Schadensmenge (muss >= 0 sein)

        Raises:
            ValueError: Bei negativem amount
        """
        # Validierung
        if amount < 0:
            raise ValueError(f"Schaden muss >= 0 sein, erhielt: {amount}")
        # HP reduzieren
        self._current_hp -= amount
        # Clamp zu 0
        self._current_hp = max(0, self._current_hp)

    def heal(self, amount: int):
        """
        Heilt HP.

        Args:
            amount: Heilungsmenge (muss >= 0 sein)

        Raises:
            ValueError: Bei negativem amount
        """
        # Validierung
        if amount < 0:
            raise ValueError(f"Heilung muss >= 0 sein, erhielt: {amount}")
        # HP erhöhen
        self._current_hp += amount
        # Clamp zu max_hp
        self._current_hp = min(self._max_hp, self._current_hp)

    def is_alive(self) -> bool:
        """Prüft, ob Creature noch lebt."""
        if self._current_hp <= 0:
            return False
        return True

    def __str__(self) -> str:
        """Debug-String."""
        # TODO: "Creature at (x,y): HP current/max, STR:X(+Y), DEX:X(+Y)"
        return f"""
        empty
        """
        pass
