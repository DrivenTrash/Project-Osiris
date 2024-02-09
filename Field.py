class Field:
    def __init__(self, x, y):
        self.field = [[0 for i in range(x)] for j in range(y)]
    
    def printField(self):
        for row in self.field:
            print("\t".join((map(str, row))))


