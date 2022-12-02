# https://adventofcode.com/2022/day/1

inputfile = open("input.txt", "r")
inputlines = inputfile.read().split("\n")
totals = []
totalsofar = 0
for inputline in inputlines:
    if inputline == "":
        totals.append(totalsofar)
        totalsofar = 0
    else:
        totalsofar = totalsofar + int(inputline)
biggestsofar = 0
for value in totals:
    if value > biggestsofar:
        biggestsofar = value
    
print(biggestsofar)