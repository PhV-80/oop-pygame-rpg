from .dice import DiceRoller


class CombatSystem:

    @staticmethod
    def attack(attacker, defender):
        """
        Führt Angriffswurf gegen Verteidigung durch.

        Args:
            attacker: Attributes-Objekt des Angreifers
            defender: Attributes-Objekt des Verteidigers

        Returns:
            Tuple (hit: bool, detail: str)
            Beispiel: (True, "Attack 18 vs Defense 12 → HIT!")
        """

        # Angriffswurf W20 + Stärke-Mod
        attack_mod = attacker.get_modifier('strength')
        attack_roll, attack_detail = DiceRoller.roll_d20(modifier=attack_mod)

        # Verteidigungswurf W20 + Geschick-Mod
        defense_mod = defender.get_modifier('dexterity')
        defense_roll, defense_detail = DiceRoller.roll_d20(modifier=defense_mod)

        # Vergleich
        hit = attack_roll > defense_roll

        # Detail-String
        if hit:
            detail = f"Attack {attack_roll} vs Defense {defense_roll} -> HIT!"
        else:
            detail = f"Attack {attack_roll} vs Defense {defense_roll} -> MISS!"

        return (hit, detail)

    @staticmethod
    def calculate_damage(attacker):
        """
        Berechnet Schaden bei Treffer.

        Args:
            attacker: Attributes-Objekt

        Returns:
            Tuple (damage: int, detail: str)
        """

        strength_mod = attacker.get_modifier('strength')
        damage, damage_detail = DiceRoller.roll_d6(count=1, modifier=strength_mod)

        return (damage, damage_detail)
