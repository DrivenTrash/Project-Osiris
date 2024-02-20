from random import randint

class Creature:
    def __init__(self, generation, number):
        self.generation = generation
        self.number = number
        self.genome = [randint(1, 9) for i in range(100)]

    def __str__(self):
        return "c" + str(self.number)
    
    def move(self):
        return self.genome[randint(0, 99)]