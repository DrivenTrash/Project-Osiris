from random import randint

class Creature:
    def __init__(self, generation, number, x, y):
        self.generation = generation
        self.number = number
        self.x = x
        self.y = y
        self.genome = [randint(0, 8) for i in range(100)]

    def __str__(self):
        return "c" + str(self.number)
    
    def move(self):        return self.genome[randint(0, 99)]
    