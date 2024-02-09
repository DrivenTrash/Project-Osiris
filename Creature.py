from random import randint

class Creature:
    def __init__(self):
        self.moves = []
        for i in range(100):
            self.moves.append(randint(1, 9))
    def move(self):
        return self.moves[randint(0, 99)]