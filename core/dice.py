"""
KLASSE DiceRoller:

    STATISCHE METHODE roll_d20(modifier=0, advantage=False, disadvantage=False):
        - Würfle Zufallszahl 1-20
        - WENN advantage: Würfle 2x, nimm Maximum
        - WENN disadvantage: Würfle 2x, nimm Minimum
        - Addiere modifier
        - Gib Ergebnis + Detail-String zurück
        - Beispiel-Return: (18, "Roll: 15 + 3 = 18")

    STATISCHE METHODE roll_d6(count=1, modifier=0):
        - Würfle count-mal W6
        - Summiere alle Würfe
        - Addiere modifier
        - Gib Ergebnis + Detail-String zurück
        - Beispiel-Return: (11, "2d6: [4, 5] + 2 = 11")

    STATISCHE METHODE roll_multiple(dice_type, count, modifier=0):
        - Allgemeine Würfel-Funktion
        - dice_type: 6, 20, etc.
        - Würfle count-mal, summiere, addiere modifier
        - Return wie oben

"""
import random

class DiceRoller:
    """Würfel-System für Regelwerk (statische Methoden)."""
    @staticmethod
    def roll_d20(modifier: int = 0, advantage: bool = False, disadvantage: bool = False):
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
        roll2 = None

        # Advantage/Disadvantage
        if advantage and disadvantage:
            pass # Heben sich auf
        elif advantage:
            roll2 = random.randint(1, 20)
            roll = max(roll, roll2)
        elif disadvantage:
            roll2 = random.randint(1, 20)
            roll = min(roll, roll2)

        # Modifikator addieren
        total = roll + modifier

        #Detail-String generieren
        if roll2 is not None:
            detail = f"Roll: [{roll}, {roll2}] -> best/worst: {roll} + {modifier} = {total}"
        else:
            if modifier == 0:
                detail = f"Roll: {roll} = {total}"
            else:
                detail = f"Roll: {roll} + {modifier} = {total}"

        return (total, detail)

    @staticmethod
    def roll_d6(count: int = 1, modifier: int = 0) :
        """Würfelt W6 für Schaden"""

        roll = 0
        rolls = []
        for i in range(count):
            if range == 1:
                roll = random.randint(1, 6)
            else:
                rolls.append(random.randint(1, 6))

        roll_sum = sum(rolls)
        total = roll_sum + modifier

        if modifier == 0:
            if roll == 1:
                detail = f"{count}d6: {roll} = {roll_sum}"
            else:
                detail = f"{count}d6: {rolls} = {roll_sum}"
        else:
            if roll == 1:
                detail = f"{count}d6: {roll} + {modifier} = {total}"
            else:
                detail = f"{count}d6: {rolls} + {modifier} = {total}"

        return (total, detail)