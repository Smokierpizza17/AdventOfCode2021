import enum
import re

with open("inputs\\input.txt", "r") as inputFile:
    joinedInput = inputFile.read().split("\n\n")

def printDotMap(dotMap):
    '''prints . for False, and X for True'''
    for row in dotMap:
        for value in row:
            if value:
                print("█", end="")
            else:
                print(" ", end="")
        print("")

axisR = re.compile(r".(?==)")
coordR = re.compile(r"(?<==)\d+")

coordInput = joinedInput[0].split("\n")
instrInput = joinedInput[1].split("\n")

coordInput = list(map(lambda x:x.split(","), coordInput))

maxX = 0
maxY = 0
for coordPair in coordInput:
    x = int(coordPair[0])
    y = int(coordPair[1])
    if x > maxX:
        maxX = x
    if y > maxY:
        maxY = y

dotMapRow = [False] * (maxX + 1)
dotMap = []
for _ in range(maxY + 1):
    dotMap.append(list(dotMapRow))

for coordPair in coordInput:
    dotMap[int(coordPair[1])][int(coordPair[0])] = True

# printDotMap(dotMap)
# print("\n")

for instruction in instrInput:
    axis = re.search(axisR, instruction).group()
    symCoord = int(re.search(coordR, instruction).group())
    if axis == "y":  # vertical fold, modify x coordinates
        for y, row in enumerate(list(dotMap)):
            for x, dotValue in enumerate(list(row)):
                if y > symCoord:
                    delta = y - symCoord
                    dotMap[symCoord - delta][x] = dotMap[symCoord - delta][x] or dotValue
        dotMap = dotMap[:symCoord]  # purge now empty lines
    elif axis == "x":
        for y, row in enumerate(list(dotMap)):
            for x, dotValue in enumerate(list(row)):
                if x > symCoord:
                    delta = x - symCoord
                    dotMap[y][symCoord - delta] = dotMap[y][symCoord - delta] or dotValue
            dotMap[y] = row[:symCoord]  # purge now empty lines
    # printDotMap(dotMap)
    # print("\n")

printDotMap(dotMap)
print("\n\n")

totalVisible = 0
for row in dotMap:
    for value in row:
        if value:
            totalVisible += 1

print("after %s fold(s), %s dots are visible" % (len(instrInput), totalVisible))
