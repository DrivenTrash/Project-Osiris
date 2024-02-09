from random import randint

class Creature:
    def __init__(self, name):
        self.name = name
        self.moves = []
        for i in range(100):
            self.moves.append(randint(1, 9))

    def __str___(self):
        return self.name
    
    def move(self):
        return self.moves[randint(0, 99)]