import random

from .stats import Stats


class Combat:
    """Combat System"""

    @staticmethod
    def physical_attack(attacker: Stats, defender: Stats) -> dict:
        """
        Physischer Angriff.
        
        Args:
            attacker: Angreifer (mit Stats)
            defender: Verteidiger (mit Stats)
        
        Returns:
            dict {
                'damage': int,      # Finaler Schaden
                'is_crit': bool,    # War es ein Crit?
                'defender_alive': bool  # Lebt Defender noch?
            }
        """
        defender_defense = max(1, defender.get_defense())
        base_damage = (attacker.get_attack() ** 2) / defender_defense
        is_crit = Combat._check_crit(attacker.get_luck())
        if is_crit:
            base_damage = base_damage * 1.5
        final_damage = Combat._calculate_variance(base_damage, (0.9, 1.1))
        defender.take_damage(final_damage)
        return {
            'damage': final_damage,
            'is_crit': is_crit,
            'defender_alive': defender.is_alive()
        }
    
    @staticmethod
    def magic_attack(attacker: Stats, defender: Stats, spell_power: int, mp_cost: int) -> dict:
        """
        Zauber-Angriff.
        
        Args:
            attacker: Angreifer (mit Stats)
            defender: Verteidiger (mit Stats)
            spell_power: Stärke des Zaubers (z.B. 30)
            mp_cost: MP-Kosten (z.B. 10)
        
        Returns:
            dict {
                'damage': int,       # Finaler Schaden (0 wenn kein MP)
                'mp_used': bool,     # Wurde MP verbraucht?
                'defender_alive': bool
            }
        """

        if not attacker.use_mp(mp_cost):
            return {
                'damage': 0,
                'mp_used': False,
                'defender_alive': defender.is_alive()
            }

        defender_magic_defense = max(1, defender.get_defense())
        base_damage = (attacker.get_magic_attack() * spell_power) / defender_magic_defense
        final_damage = Combat._calculate_variance(base_damage, (0.95, 1.05))
        defender.take_damage(final_damage)
        return {
            'damage': final_damage,
            'mp_used': True,
            'defender_alive': defender.is_alive()
        }
    
    @staticmethod
    def _calculate_variance(base_damage: float, variance_range: tuple) -> int:
        """
        Helper: Varianz auf Base Damage anwenden.
        
        Args:
            base_damage: Basis-Schaden
            variance_range: Tuple (min, max), z.B. (0.9, 1.1)
        
        Returns:
            Final Damage (int)
        """
        # PSEUDOCODE:
        variance = random.uniform(variance_range[0], variance_range[1])
        return max(1, int(base_damage * variance))

    @staticmethod
    def _check_crit(luck: int) -> bool:
        """
        Helper: Crit-Check.
        
        Args:
            luck: Luck-Stat des Angreifers
        
        Returns:
            True wenn Crit, sonst False
        """
        # PSEUDOCODE:
        return random.randint(1, 100) <= luck
