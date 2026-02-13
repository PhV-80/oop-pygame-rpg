"""
Stats-System (JRPG-inspired)

Unterstützt verschiedene Klassen/Archetypen:
- Kampfklassen (Krieger): Hoher Attack/Defense, niedrige INT, kein/wenig MP
- Magiekundige (Magier): Hohe INT, viel MP + Magic Attack
- Hybrid-Klassen: Mittlere Werte

Intelligenz-System:
- Pro 5 INT → +1 Max-MP
- Pro 10 INT → +1 Magic Attack
"""


class Stats:
    """Stats für Characters (Player, NPC, Enemy)."""

    def __init__(self, level: int = 1, base_stats: dict = None):
        """
        Erstellt Stats basierend auf Level.

        Args:
            level: Charakter-Level (1-99)
            base_stats: Dict mit Basis-Werten für Klassen-Archetypen
                {
                    'hp': 50,
                    'mp': 30,
                    'attack': 50,
                    'defense': 50,
                    'magic_attack': 50,
                    'magic_defense': 50,
                    'intelligence': 50,  # Beeinflusst MP + Magic Attack
                    'speed': 10,
                    'luck': 5
                }

        Beispiele:
            # Krieger (niedrige INT, kein MP)
            warrior_stats = {
                'hp': 60, 'mp': 0,
                'attack': 80, 'defense': 120,
                'magic_attack': 20, 'magic_defense': 80,
                'intelligence': 30,  # Niedrig
                'speed': 8, 'luck': 5
            }

            # Magier (hohe INT → Bonus MP + Magic Attack)
            mage_stats = {
                'hp': 40, 'mp': 70,
                'attack': 20, 'defense': 80,
                'magic_attack': 80, 'magic_defense': 120,
                'intelligence': 100,  # Hoch → +20 MP, +10 Magic Attack
                'speed': 12, 'luck': 8
            }

            # Paladin (Hybrid)
            paladin_stats = {
                'hp': 55, 'mp': 40,
                'attack': 60, 'defense': 100,
                'magic_attack': 50, 'magic_defense': 100,
                'intelligence': 60,  # Mittel → +12 MP, +6 Magic Attack
                'speed': 10, 'luck': 6
            }
        """
        self._level = level

        # Standard-Werte wenn keine custom stats (Allrounder)
        if base_stats is None:
            base_stats = {
                'hp': 50,
                'mp': 30,
                'attack': 50,
                'defense': 50,
                'magic_attack': 50,
                'magic_defense': 50,
                'intelligence': 50,
                'speed': 10,
                'luck': 5
            }

        # Intelligenz berechnen (wächst mit Level)
        base_int = base_stats.get('intelligence', 50)
        self._intelligence = base_int + (level - 1) * 2

        # INT-Boni berechnen
        mp_bonus = self._intelligence // 5  # Pro 5 INT → +1 MP
        magic_bonus = self._intelligence // 10  # Pro 10 INT → +1 Magic Attack

        # HP (keine INT-Abhängigkeit)
        self._max_hp = base_stats['hp'] + (level - 1) * 15
        self._current_hp = self._max_hp

        # MP (mit INT-Bonus)
        base_mp = base_stats['mp']
        self._max_mp = base_mp + (level - 1) * 5 + mp_bonus
        self._current_mp = self._max_mp

        # Kampf-Stats (keine INT-Abhängigkeit)
        self._attack = base_stats['attack'] + (level - 1) * 2
        self._defense = base_stats['defense'] + (level - 1) * 1

        # Magie-Stats (mit INT-Bonus)
        self._magic_attack = base_stats['magic_attack'] + (level - 1) * 3 + magic_bonus
        self._magic_defense = base_stats['magic_defense'] + (level - 1) * 2

        # Utility-Stats
        self._speed = base_stats['speed'] + (level - 1) * 1
        self._luck = base_stats['luck']  # Luck steigt nicht mit Level

    # ===== GETTER =====
    def get_level(self) -> int:
        """Gibt Level zurück."""
        return self._level

    def get_hp(self) -> int:
        """Gibt aktuelle HP zurück."""
        return self._current_hp

    def get_max_hp(self) -> int:
        """Gibt maximale HP zurück."""
        return self._max_hp

    def get_mp(self) -> int:
        """Gibt aktuelles MP zurück."""
        return self._current_mp

    def get_max_mp(self) -> int:
        """Gibt maximales MP zurück."""
        return self._max_mp

    def get_attack(self) -> int:
        """Gibt Attack-Stat zurück (physischer Schaden)."""
        return self._attack

    def get_defense(self) -> int:
        """Gibt Defense-Stat zurück (physische Resistenz)."""
        return self._defense

    def get_magic_attack(self) -> int:
        """Gibt Magic Attack-Stat zurück (Zauber-Schaden, INT-geboosted)."""
        return self._magic_attack

    def get_magic_defense(self) -> int:
        """Gibt Magic Defense-Stat zurück (Zauber-Resistenz)."""
        return self._magic_defense

    def get_intelligence(self) -> int:
        """Gibt Intelligenz-Stat zurück (beeinflusst MP + Magic Attack)."""
        return self._intelligence

    def get_speed(self) -> int:
        """Gibt Speed-Stat zurück (Turn-Order)."""
        return self._speed

    def get_luck(self) -> int:
        """Gibt Luck-Stat zurück (Crit-Chance, Item-Drops)."""
        return self._luck

    def is_magic_user(self) -> bool:
        """Prüft, ob Charakter magiekundig ist (max_mp > 0)."""
        return self._max_mp > 0

    # ===== HP-MANAGEMENT =====
    def take_damage(self, amount: int):
        """
        Nimmt Schaden.

        Args:
            amount: Schadensmenge (>= 0)

        Raises:
            ValueError: Bei negativem amount
        """
        if amount < 0:
            raise ValueError(f"Schaden muss >= 0 sein, erhielt: {amount}")

        self._current_hp -= amount
        self._current_hp = max(0, self._current_hp)  # Clamp zu 0

    def heal(self, amount: int):
        """
        Heilt HP.

        Args:
            amount: Heilungsmenge (>= 0)

        Raises:
            ValueError: Bei negativem amount
        """
        if amount < 0:
            raise ValueError(f"Heilung muss >= 0 sein, erhielt: {amount}")

        self._current_hp += amount
        self._current_hp = min(self._max_hp, self._current_hp)  # Clamp zu max

    def is_alive(self) -> bool:
        """Prüft, ob Charakter noch lebt (HP > 0)."""
        return self._current_hp > 0

    # ===== MP-MANAGEMENT =====
    def use_mp(self, amount: int) -> bool:
        """
        Versucht MP zu verbrauchen.

        Args:
            amount: MP-Kosten (>= 0)

        Returns:
            True wenn genug MP vorhanden, sonst False

        Raises:
            ValueError: Bei negativem amount
        """
        if amount < 0:
            raise ValueError(f"MP-Kosten müssen >= 0 sein, erhielt: {amount}")

        # Nicht-Magier können kein MP nutzen
        if not self.is_magic_user():
            return False

        if self._current_mp >= amount:
            self._current_mp -= amount
            return True
        return False

    def restore_mp(self, amount: int):
        """
        Regeneriert MP.

        Args:
            amount: MP-Menge (>= 0)

        Raises:
            ValueError: Bei negativem amount
        """
        if amount < 0:
            raise ValueError(f"MP-Regeneration muss >= 0 sein, erhielt: {amount}")

        # Nicht-Magier haben kein MP zum Regenerieren
        if not self.is_magic_user():
            return

        self._current_mp += amount
        self._current_mp = min(self._max_mp, self._current_mp)  # Clamp zu max

    # ===== DEBUG =====
    def __str__(self) -> str:
        """Debug-String."""
        magic_status = "Magiekundig" if self.is_magic_user() else "Nicht-magisch"

        return f"""Stats(Level {self._level}, {magic_status}):
  HP: {self._current_hp}/{self._max_hp}
  MP: {self._current_mp}/{self._max_mp}
  Attack: {self._attack}, Defense: {self._defense}
  Magic Attack: {self._magic_attack}, Magic Defense: {self._magic_defense}
  Intelligence: {self._intelligence}
  Speed: {self._speed}, Luck: {self._luck}"""
