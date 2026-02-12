from core.attributes import Attributes
from entities.creature import Creature

print("=== Creature Tests ===\n")

# Test 1: Konstruktor + HP-Berechnung
attrs = Attributes(strength=14, dexterity=12, constitution=14)
creature = Creature(x=100, y=200, width=50, height=50,
                    color=(255, 0, 0), attributes=attrs)

print(f"CON: {attrs.get_constitution()}, Mod: {attrs.get_modifier('constitution')}")
expected_max_hp = 10 + (attrs.get_modifier('constitution') * 2)
print(f"Expected max HP: {expected_max_hp}")
print(f"Actual max HP: {creature.get_max_hp()}")
assert creature.get_max_hp() == expected_max_hp, "max_hp falsch berechnet"
assert creature.get_hp() == expected_max_hp, "current_hp sollte = max_hp sein"
print("✅ HP-Berechnung korrekt\n")

# Test 2: take_damage()
creature.take_damage(5)
assert creature.get_hp() == expected_max_hp - 5, "take_damage() funktioniert nicht"
print(f"✅ Nach 5 Schaden: HP = {creature.get_hp()}/{creature.get_max_hp()}\n")

# Test 3: heal()
creature.heal(3)
assert creature.get_hp() == expected_max_hp - 2, "heal() funktioniert nicht"
print(f"✅ Nach 3 Heilung: HP = {creature.get_hp()}/{creature.get_max_hp()}\n")

# Test 4: Overheal (darf nicht über max_hp)
creature.heal(100)
assert creature.get_hp() == expected_max_hp, "Overheal nicht geclampt"
print(f"✅ Nach Overheal: HP = {creature.get_hp()}/{creature.get_max_hp()} (geclampt)\n")

# Test 5: is_alive()
assert creature.is_alive() == True, "is_alive() sollte True sein"
creature.take_damage(1000)  # Overkill
assert creature.get_hp() == 0, "HP sollte auf 0 geclampt sein"
assert creature.is_alive() == False, "is_alive() sollte False sein"
print("✅ is_alive() funktioniert (Tod bei HP=0)\n")

# Test 6: Negative damage/heal sollte fehlen
try:
    creature.heal(-5)
    assert False, "Negative Heilung sollte ValueError werfen"
except ValueError:
    print("✅ Negative Heilung wirft ValueError\n")

# Test 7: Vererbung (Entity-Methoden)
creature2 = Creature(x=50, y=50, width=50, height=50,
                     color=(0, 255, 0),
                     attributes=Attributes(strength=10))
assert creature2.get_x() == 50, "Entity-Vererbung kaputt (get_x)"
creature2.set_x(75)
assert creature2.get_x() == 75, "Entity-Vererbung kaputt (set_x)"
print("✅ Entity-Vererbung funktioniert\n")

# Test 8: __str__()
print(f"Debug-String: {creature2}")
print("✅ __str__() existiert\n")

print("🎉 ALLE CREATURE-TESTS GRÜN")
