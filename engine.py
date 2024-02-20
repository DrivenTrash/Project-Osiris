from field import Field
from creature import Creature
from random import randint

test = Field(5, 5)
test.add_creature()
test.add_creature()
test.display()
print(test.population)   