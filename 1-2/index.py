# https://adventofcode.com/2022/day/1#part2
debug = False

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

# I know this part would have been cleaner with arrays, but this is probably quicker and simpler.
biggest1 = 0
biggest2 = 0
biggest3 = 0

for value in totals:
    if value > biggest1:
        biggest3 = biggest2
        biggest2 = biggest1
        biggest1 = value
    elif value > biggest2:
        biggest3 = biggest2
        biggest2 = value
    elif value > biggest3:
        biggest3 = value
    
if debug == True:
    print(biggest1)
    print(biggest2)
    print(biggest3)

finalanswer = biggest1 + biggest2 + biggest3

print(finalanswer)