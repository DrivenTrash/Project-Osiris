from random import randint
from creature import Creature   

class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.field = [[0 for i in range(x)] for j in range(y)]
        self.generation = 0
        self.creatureCounter = 0
        self.population = []

    def add_creature(self):
        newCreature = Creature(self.generation, self.creatureCounter)   
        self.field[randint(0, self.x-1)][randint(0, self.y-1)] = newCreature
        self.population.append(newCreature)
        self.creatureCounter += 1
    
    def display(self):
        for row in self.field:
            line = ""
            for i in row:
               line += "%4s" % str(i)  + " " 
            print(line)