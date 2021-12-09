with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput = list(map(lambda x:list(x), taskInput))

intTaskInput = []
for line in taskInput:
    intRow = []
    for digit in line:
        intRow.append(int(digit))
    intTaskInput.append(intRow)

def checkIfLowPoint(point, surrounding):
    '''returns true if all surrounding points are greater than (or None) point'''
    for nextPoint in surrounding:
        if nextPoint == None:
            continue
        if nextPoint - point <= 0:
            return False
    return True

totalRisk = 0
for y, row in enumerate(intTaskInput):
    for x, digit in enumerate(row):
        if 0 < y < len(intTaskInput) - 1:
            upOf = intTaskInput[y-1][x]
            downOf = intTaskInput[y+1][x]
        elif y == 0:
            upOf = None
            downOf = intTaskInput[y+1][x]
        elif y == len(intTaskInput) - 1:
            upOf = intTaskInput[y-1][x]
            downOf = None

        if 0 < x < len(row) - 1:
            leftOf = intTaskInput[y][x-1]
            rightOf = intTaskInput[y][x+1]
        elif x == 0:
            leftOf = None
            rightOf = intTaskInput[y][x+1]
        elif x == len(row) - 1:
            leftOf = intTaskInput[y][x-1]
            rightOf = None
        
        isLowPoint = checkIfLowPoint(digit, [upOf, downOf, leftOf, rightOf])
        if isLowPoint:
            totalRisk += digit + 1

print("total risk is %s" % totalRisk)
