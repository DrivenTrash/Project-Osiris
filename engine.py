from Field import Field
from Creature import Creature
from random import randint

test = Field(5, 5)
test.field[3][2] = 15
test.printField()   

c1 = Creature()
print (c1.moves)
print (c1.move())
print (c1.move())
