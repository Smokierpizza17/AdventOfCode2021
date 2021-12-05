import re

with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

numbersR = re.compile(r"\d+")

def printVentMap(ventMap):
    ventStr = ""
    for row in ventMap:
        rowString = ""
        for value in row:
            if value == 0:
                character= "."
            else:
                character = str(value)
            rowString += character
        ventStr += rowString + "\n"
    print(ventStr)

parsedInput = []  # [[[x1, y1], [x2, y2]], [[x3, y3], [x4, y4]]]
for line in taskInput:
    numbers = re.findall(numbersR, line)
    x1 = int(numbers[0])
    y1 = int(numbers[1])
    x2 = int(numbers[2])
    y2 = int(numbers[3])
    parsedInput.append([[x1, y1], [x2, y2]])

maxX = 0
maxY = 0
for coordinatePair in parsedInput:
    x1 = coordinatePair[0][0]
    x2 = coordinatePair[1][0]
    y1 = coordinatePair[0][1]
    y2 = coordinatePair[1][1]
    if maxX < x1:
        maxX = x1
    if maxX < x2:
        maxX = x2
    if maxY < y1:
        maxY = y1
    if maxY < y2:
        maxY = y2

ventMapRow = [0] * (maxX + 1)
ventMap = []
for _ in range(maxY + 1):
    ventMap.append(list(ventMapRow))

for coordinatePair in parsedInput:
    x1 = coordinatePair[0][0]
    x2 = coordinatePair[1][0]
    y1 = coordinatePair[0][1]
    y2 = coordinatePair[1][1]

    # 2nd coordinate will always be bigger

    if x1 == x2:  # vertical line
        if y1 > y2:
            y1, y2 = y2, y1
        for yIndex in range(y1, y2+1):  # consider y2 as well
            ventMap[yIndex][x1] += 1
    elif y1 == y2:  # horizontal line
        if x1 > x2:
            x1, x2 = x2, x1
        for xIndex in range(x1, x2+1):  # consider x2 as well
            ventMap[y1][xIndex] += 1

overlapCount = 0
for row in ventMap:
    for value in row:
        if value > 1:
            overlapCount += 1

printVentMap(ventMap)
print("")
print("vent overlaps happen %s times" % overlapCount)
