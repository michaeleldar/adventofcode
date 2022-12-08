class Group:
    def __init__(self, lines):
        self.backpacks = lines


    def getBadge(self):
        for letter in self.backpacks[0]:
            if letter in self.backpacks[1]:
                if letter in self.backpacks[2]:
                    return letter

def getPriority(letter):
    prioritys = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return prioritys.index(letter)


def main():
    inputfile = open("input.txt", 'r')
    lineno = 0
    totpriority = 0
    lines = []

    for line in inputfile.read().split("\n"):
        lines.append(line)
        lineno = lineno + 1
        if lineno == 3:
            group = Group(lines)
            badge = group.getBadge()
            totpriority = totpriority + getPriority(badge)
            lineno = 0
            lines = []


    print(totpriority)



main()