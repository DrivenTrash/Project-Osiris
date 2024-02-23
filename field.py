from random import randint
from creature import Creature   

class Field:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.field = [[0 for i in range(x)] for j in range(y)]
        self.generation = 0
        self.creatureCounter = 0
        self.population = [] ##stores pointers to  all creatures in the field

    ##spawns a new creature and adds it to the field
    def add_creature(self, x=None, y=None): 
        if x is None:
            x = randint(0, self.x-1)
        if y is None:
            y = randint(0, self.y-1)
        if self.field[y][x] == 0:
            newCreature = Creature(self.generation, self.creatureCounter, x, y) 
            self.field[y][x] = newCreature
            self.population.append(newCreature)
            self.creatureCounter += 1
    
    ##lets a creature perform a move
    def move_creature(self, creature): 
        ## first it gets the creatures current position
        x_old = creature.x
        y_old = creature.y
        ## then it gets the creatures move
        move = creature.move()
        ## then it calculates the creatures new position
        x_new = x_old
        y_new = y_old
        if move%3 == 0:
            x_new -= 1
        elif move%3 == 2:
            x_new += 1
        if move//3 == 0:
            y_new -= 1
        elif move//3 == 2:
            y_new += 1
        ## last it checks if the new position is valid (not outside the grid and free) and if it is, it moves the creature
        if x_new >= 0 and x_new < self.x and y_new >= 0 and y_new < self.y and self.field[x_new][y_new] == 0:
            self.field[y_old][x_old] = 0
            self.field[y_new][x_new] = creature
            creature.x = x_new
            creature.y = y_new

    ##prints the current state of the field
    def display(self): 
        for row in self.field:
            line = ""
            for i in row:
               line += "%4s" % str(i)  + " " 
            print(line)