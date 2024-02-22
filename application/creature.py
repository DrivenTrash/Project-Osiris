from random import randint

class Creature:
    def __init__(self, generation, number, x, y):
        self.generation = generation
        self.number = number
        self.x = x
        self.y = y
        self.genome = [randint(0, 8) for i in range(100)] ##stores all possible moves for the creature, each number indicates to a direction, 0 = up left, 1 = up, ..., 8 = down right

    def __str__(self):
        return "c" + str(self.number)
    
    def move(self): ##returns a random number/direction from the genome
        return self.genome[randint(0, 99)]
    