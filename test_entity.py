from entities.entity import Entity

# Test 1: Konstruktor
e = Entity(x=100, y=200, width=50, height=50, color=(255, 0, 0))
print(f"✅ Konstruktor: x={e.get_x()}, y={e.get_y()}, w={e.get_width()}, h={e.get_height()}")

# Test 2: Setter
e.set_x(150)
e.set_y(250)
assert e.get_x() == 150, "set_x() funktioniert nicht"
assert e.get_y() == 250, "set_y() funktioniert nicht"
print("✅ Setter funktionieren")

# Test 3: Collision (überlappend)
e2 = Entity(x=120, y=220, width=50, height=50, color=(0, 255, 0))
assert e.check_collision(e2) == True, "Collision-Detection falsch (sollte True sein)"
print("✅ Collision-Detection (überlappend): True")

# Test 4: Collision (getrennt)
e3 = Entity(x=300, y=300, width=50, height=50, color=(0, 0, 255))
assert e.check_collision(e3) == False, "Collision-Detection falsch (sollte False sein)"
print("✅ Collision-Detection (getrennt): False")

print("\n🎉 ALLE TESTS GRÜN")