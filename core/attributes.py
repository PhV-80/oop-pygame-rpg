"""
KLASSE Attributes:

    KONSTRUKTOR (alle Attribute optional, Standard = 10):
        - Speichere strength, dexterity, intelligence, wisdom, charisma, constitution
        - Validiere: Werte zwischen 1 und 20, sonst Fehler

    GETTER für jedes Attribut:
        - get_strength() → gibt Stärke-Wert zurück
        - get_dexterity() → gibt Geschick-Wert zurück
        - ... (analog für alle 6)

    SETTER für jedes Attribut (mit Validierung):
        - set_strength(wert) → setzt Wert, prüft Range 1-20
        - ... (analog für alle 6)

    MODIFIKATOR-BERECHNUNG:
        - get_modifier(attribut_name) → berechnet (Wert - 10) / 2, abgerundet
        - Beispiel: get_modifier("strength") bei Stärke 15 → +2

    STRING-REPRÄSENTATION (für Debug):
        - __str__() → gibt lesbare Ausgabe zurück
        - Beispiel: "STR:14(+2), DEX:12(+1), INT:10(+0), ..."

"""
class Attributes:

    def __init__(self, strength: int = 10, dexterity : int = 10, intelligence: int = 10, wisdom: int =10, charisma: int = 10, constitution: int = 10):
        """
        Erstellt Attribut-Set mit Validierung.

        Args:
            strength: Stärke (1-20, Standard: 10)
            dexterity: Geschick (1-20, Standard: 10)
            intelligence: Intelligenz (1-20, Standard: 10)
            wisdom: Weisheit (1-20, Standard: 10)
            charisma: Charisma (1-20, Standard: 10)
            constitution: Konstitution (1-20, Standard: 10)

        Raises:
            ValueError: Wenn ein Attribut außerhalb 1-20 liegt
        """
        # Parameter in Dictionary ablegen
        attributes = {
            'strength': strength,
            'dexterity': dexterity,
            'intelligence': intelligence,
            'wisdom': wisdom,
            'charisma': charisma,
            'constitution': constitution
        }

        # Validierung aller Parameter als Schleife
        for name, value in attributes.items():
            if value < 1 or value > 20:
                raise ValueError(f"{name} muss zwischen 1 und 20 liegen, erhielt: {value}")

        self._strength = strength
        self._dexterity = dexterity
        self._intelligence = intelligence
        self._wisdom = wisdom
        self._charisma = charisma
        self._constitution = constitution

    def get_strength(self):
        """Gibt Stärke-Wert zurück"""
        return self._strength

    def get_dexterity(self):
        """Gibt Geschicklichkeit-Wert zurück"""
        return self._dexterity

    def get_intelligence(self):
        """Gibt Intelligenz-Wert zurück"""
        return self._intelligence

    def get_wisdom(self):
        """Gibt Weisheit-Wert zurück"""
        return self._wisdom

    def get_charisma(self):
        """Gibt Charisma-Wert zurück"""
        return self._charisma

    def get_constitution(self):
        """Gibt Konstitution-Wert zurück"""
        return self._constitution

    def set_strength(self, value: int):
        if value < 1 or value > 20:
            raise ValueError(f"Strength muss zwischen 1-20 liegen, erhielt: {value}")
        self._strength = value

    def set_dexterity(self, value: int):
        if value < 1 or value > 20:
            raise ValueError(f"Dexterity muss zwischen 1-20 liegen, erhielt: {value}")
        self._dexterity = value

    def set_intelligence(self, value: int):
        if value < 1 or value > 20:
            raise ValueError(f"Intelligence muss zwischen 1-20 liegen, erhielt: {value}")
        self._intelligence = value

    def set_wisdom(self, value: int):
        if value < 1 or value > 20:
            raise ValueError(f"Wisdom muss zwischen 1-20 liegen, erhielt: {value}")
        self._wisdom = value

    def set_charisma(self, value: int):
        if value < 1 or value > 20:
            raise ValueError(f"Charisma muss zwischen 1-20 liegen, erhielt: {value}")
        self._charisma = value

    def set_constitution(self, value: int):
        if value < 1 or value > 20:
            raise ValueError(f"Constitution muss zwischen 1-20 liegen, erhielt: {value}")
        self._constitution = value

    def get_modifier(self, attribute_name: str) -> int:
        """
        Berechnet Modifikator für ein Attribut.

        Args:
            attribute_name: Name des Attributs (z.B. "strength")

        Returns:
            Modifikator-Wert (z.B. +2 bei Stärke 14)

        Raises:
            ValueError: Bei unbekanntem Attribut-Namen
        """
        if attribute_name not in ["strength", "dexterity", "intelligence", "wisdom", "charisma", "constitution"]:
            raise ValueError(f"Unbekanntes Attribut: {attribute_name}")

        private_name = f"_{attribute_name}"
        attribute_value = getattr(self, private_name)

        modifier = (attribute_value - 10) // 2
        return modifier

