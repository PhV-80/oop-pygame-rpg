from core.attributes import Attributes

char = Attributes(strength=14, dexterity=8, intelligence=16)

print(char.get_modifier('strength'))
print(char.get_modifier('dexterity'))
print(char.get_modifier('intelligence'))
print(char.get_modifier('invalid'))
