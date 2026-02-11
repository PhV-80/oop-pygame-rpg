import random

class DiceRoller:
    """Würfel-System für Regelwerk (statische Methoden)."""
    @staticmethod
    def roll_d20(self, modifier: int = 0, advantage: bool = False, disadvantage: bool = False):
        """
        Würfelt W20 für Skill-Checks.

        Args:
            modifier: Bonus/Malus (z.B. +3 für Attribut-Mod)
            advantage: Würfle 2x, nimm höheren Wert
            disadvantage: Würfle 2x, nimm niedrigeren Wert

        Returns:
            Tuple (Gesamt-Ergebnis, Detail-String)
            Beispiel: (18, "Roll: 15 + 3 = 18")
        """

        # Würfle W20
        roll = random.randint(1, 20)

        # Advantage/Disadvantage
        if advantage and disadvantage:
            pass
        elif advantage:
            roll2 = random.randint(1, 20)
            roll = max(roll, roll2)
            return
        elif disadvantage:
            roll2 = random.randint(1, 20)
            roll = min(roll, roll2)

