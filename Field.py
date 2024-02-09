class Field:
    def __init__(self, x, y):
        self.field = [[0 for i in range(x)] for j in range(y)]
    
    def printField(self):
        for row in self.field:
            line = ""
            for i in row:
               line += "%4s" % str(i)  + " " 
            print(line)