class Round:
    def __init__(self, line):
        self.opponentValue = line.split(" ")[0]
        self.result = line.split(" ")[1]
    
    def getTotalScore(self):
        return self.getItemScore() + self.getGameScore()

    def getItemScore(self):
        if self.opponentValue == "A":
            if self.result == "X":
                return 3
            elif self.result == "Y":
                return 1
            elif self.result == "Z":
                return 2

        elif self.opponentValue == "B":
            if self.result == "X":
                return 1
            elif self.result == "Y":
                return 2
            elif self.result == "Z":
                return 3
        elif self.opponentValue == "C":
            if self.result == "X":
                return 2
            elif self.result == "Y":
                return 3
            elif self.result == "Z":
                return 1
    
    def getGameScore(self):
        if self.result == "X":
            return 0
        elif self.result == "Y":
            return 3
        elif self.result == "Z":
            return 6



inputfile = open("input.txt", 'r')
inputlines = inputfile.read().split("\n")
pointssofar = 0
for inputline in inputlines:
    round = Round(inputline)
    pointssofar = pointssofar + round.getTotalScore()

print(pointssofar)