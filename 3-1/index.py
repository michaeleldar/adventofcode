class Backpack:
    def __init__(self, string):
        self.compartment1String = string[slice(0, len(string)//2)]
        self.compartment2String = string[slice(len(string)//2, len(string))]

    def getMatch(self):
        for letter in self.compartment1String:
            if letter in self.compartment2String:
                return letter


def getPriority(letter):
    prioritys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return prioritys.index(letter) + 1


def main():
    totalpriority = 0
    inputfile = open("input.txt", 'r')
    for line in inputfile.read().split("\n"):
        backpack = Backpack(line)
        match = backpack.getMatch()
        totalpriority = totalpriority + getPriority(match)

    print(totalpriority)

main()