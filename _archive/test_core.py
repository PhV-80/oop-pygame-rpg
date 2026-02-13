from _archive.attributes import Attributes
from _archive.combat import CombatSystem
from _archive.dice import DiceRoller

print("=== Attributes Test ===")
char = Attributes(strength=14, dexterity=8)
print(f"Strength: {char.get_strength()}, Mod: {char.get_modifier('strength')}")
print(f"Dexterity: {char.get_dexterity()}, Mod: {char.get_modifier('dexterity')}")

print("\n=== W20 Test ===")
for i in range(5):
    result, detail = DiceRoller.roll_d20(modifier=3)
    print(detail)

print("\n=== W20 mit Advantage ===")
result, detail = DiceRoller.roll_d20(modifier=2, advantage=True)
print(detail)

print("\n=== W6 Schaden ===")
for i in range(3):
    result, detail = DiceRoller.roll_d6(count=2, modifier=3)
    print(detail)

print("\n=== Combat Test ===")
attacker = Attributes(strength=14, dexterity=10)
defender = Attributes(strength=10, dexterity=12)

for i in range(5):
    hit, attack_detail = CombatSystem.attack(attacker, defender)
    print(attack_detail)

    if hit:
        damage, dmg_detail = CombatSystem.calculate_damage(attacker)
        print(f" -> {dmg_detail}")