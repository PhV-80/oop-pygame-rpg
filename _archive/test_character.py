from _archive.attributes import Attributes
from entities.character import Character

print("=== Character Tests ===\n")

# Test 1: Konstruktor + HP-Berechnung
attrs = Attributes(strength=14, dexterity=12, constitution=14)
character = Character(x=100, y=200, width=50, height=50, color=(255, 0, 0), attributes=attrs)

print(f"CON: {attrs.get_constitution()}, Mod: {attrs.get_modifier('constitution')}")
expected_max_hp = 10 + (attrs.get_modifier('constitution') * 2)
print(f"Expected max HP: {expected_max_hp}")
print(f"Actual max HP: {character.get_max_hp()}")
assert character.get_max_hp() == expected_max_hp, "max_hp falsch berechnet"
assert character.get_hp() == expected_max_hp, "current_hp sollte = max_hp sein"
print("✅ HP-Berechnung korrekt\n")

# Test 2: take_damage()
character.take_damage(5)
assert character.get_hp() == expected_max_hp - 5, "take_damage() funktioniert nicht"
print(f"✅ Nach 5 Schaden: HP = {character.get_hp()}/{character.get_max_hp()}\n")

# Test 3: heal()
character.heal(3)
assert character.get_hp() == expected_max_hp - 2, "heal() funktioniert nicht"
print(f"✅ Nach 3 Heilung: HP = {character.get_hp()}/{character.get_max_hp()}\n")

# Test 4: Overheal (darf nicht über max_hp)
character.heal(100)
assert character.get_hp() == expected_max_hp, "Overheal nicht geclampt"
print(f"✅ Nach Overheal: HP = {character.get_hp()}/{character.get_max_hp()} (geclampt)\n")

# Test 5: is_alive()
assert character.is_alive() == True, "is_alive() sollte True sein"
character.take_damage(1000)  # Overkill
assert character.get_hp() == 0, "HP sollte auf 0 geclampt sein"
assert character.is_alive() == False, "is_alive() sollte False sein"
print("✅ is_alive() funktioniert (Tod bei HP=0)\n")

# Test 6: Negative damage/heal sollte fehlen
try:
    character.heal(-5)
    assert False, "Negative Heilung sollte ValueError werfen"
except ValueError:
    print("✅ Negative Heilung wirft ValueError\n")

# Test 7: Vererbung (Entity-Methoden)
character2 = Character(x=50, y=50, width=50, height=50,
                       color=(0, 255, 0),
                       attributes=Attributes(strength=10))
assert character2.get_x() == 50, "Entity-Vererbung kaputt (get_x)"
character2.set_x(75)
assert character2.get_x() == 75, "Entity-Vererbung kaputt (set_x)"
print("✅ Entity-Vererbung funktioniert\n")

# Test 8: __str__()
print(f"Debug-String: {character2}")
print("✅ __str__() existiert\n")

print("🎉 ALLE CREATURE-TESTS GRÜN")
