from field import Field
from creature import Creature
from random import randint

test = Field(5, 5)
while test.creatureCounter < 5:
    test.add_creature()
test.display()
print("-------------------")
print(test.population)
for i in range(3):
    for c in test.population:
        test.move_creature(c)
        test.display()
        print("-------------------")   