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
        pass

    def get_max_hp(self) -> int:
        """Gibt maximale HP zurück."""
        # TODO
        pass

    def take_damage(self, amount: int):
        """
        Nimmt Schaden.

        Args:
            amount: Schadensmenge (muss >= 0 sein)

        Raises:
            ValueError: Bei negativem amount
        """
        # TODO: Validierung
        # TODO: HP reduzieren
        # TODO: Clamp zu 0
        pass

    def heal(self, amount: int):
        """
        Heilt HP.

        Args:
            amount: Heilungsmenge (muss >= 0 sein)

        Raises:
            ValueError: Bei negativem amount
        """
        # TODO: Validierung
        # TODO: HP erhöhen
        # TODO: Clamp zu max_hp
        pass

    def is_alive(self) -> bool:
        """Prüft, ob Creature noch lebt."""
        # TODO
        pass

    def get_attributes(self) -> Attributes:
        """Gibt Attributes-Objekt zurück."""
        # TODO
        pass

    def __str__(self) -> str:
        """Debug-String."""
        # TODO: "Creature at (x,y): HP current/max, STR:X(+Y), DEX:X(+Y)"
        pass
