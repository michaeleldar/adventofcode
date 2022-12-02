class Round:
    def __init__(self, line):
        self.opponentValue = line.split(" ")[0]
        self.myValue = line.split(" ")[1]
    
    def getTotalScore(self):
        return self.getItemScore() + self.getGameScore()

    def getItemScore(self):
        if self.myValue == "X":
            return 1
        elif self.myValue == "Y":
            return 2
        elif self.myValue == "Z":
            return 3
    
    def getGameScore(self):
        if self.myValue == "X":
            if self.opponentValue == "A":
                return 3
            elif self.opponentValue == "B":
                return 0
            elif self.opponentValue == "C":
                return 6

        elif self.myValue == "Y":
            if self.opponentValue == "A":
                return 6
            elif self.opponentValue == "B":
                return 3
            elif self.opponentValue == "C":
                return 0
        
        elif self.myValue == "Z":
            if self.opponentValue == "A":
                return 0
            elif self.opponentValue == "B":
                return 6
            elif self.opponentValue == "C":
                return 3



inputfile = open("input.txt", 'r')
inputlines = inputfile.read().split("\n")
pointssofar = 0
for inputline in inputlines:
    round = Round(inputline)
    pointssofar = pointssofar + round.getTotalScore()

print(pointssofar)