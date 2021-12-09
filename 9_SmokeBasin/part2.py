with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput = list(map(lambda x:list(x), taskInput))

intTaskInput = []
for line in taskInput:
    intRow = []
    for digit in line:
        intRow.append(int(digit))
    intTaskInput.append(intRow)

def getPointAndSurroundings(array, y, x):
    '''returns point and four surrounding points, up down, left, right, or None if on edge'''
    if 0 < y < len(array) - 1:
        upOf = (y-1, x, array[y-1][x])
        downOf = (y+1, x, array[y+1][x])
    elif y == 0:
        upOf = (y-1, x, None)
        downOf = (y+1, x, array[y+1][x])
    elif y == len(array) - 1:
        upOf = (y-1, x, array[y-1][x])
        downOf = (y+1, x, None)

    if 0 < x < len(row) - 1:
        leftOf = (y, x-1, array[y][x-1])
        rightOf = (y, x+1, array[y][x+1])
    elif x == 0:
        leftOf = (y, x-1, None)
        rightOf = (y, x+1, array[y][x+1])
    elif x == len(row) - 1:
        leftOf = (y, x-1, array[y][x-1])
        rightOf = (y, x+1, None)
    
    return (y, x, array[y][x]), [upOf, downOf, leftOf, rightOf]

def getBasinSize(array, y, x, presetCoords):
    '''returns number of points before wall of 9s is reached'''
    point, neighbours = getPointAndSurroundings(array, y, x)
    if point[2] == 9:
        return presetCoords
    presetCoords.add(point)
    for neighbour in neighbours:
        if neighbour[2] != 9 and neighbour[2] != None and not neighbour in presetCoords:
            presetCoords.add(neighbour)
            presetCoords = getBasinSize(array, neighbour[0], neighbour[1], presetCoords)
    return presetCoords

def checkIfLowPoint(point, surrounding):
    '''returns true if all surrounding points are greater than (or None) point'''
    for nextPoint in surrounding:
        if nextPoint[2] == None:
            continue
        if nextPoint[2] - point <= 0:
            return False
    return True

def printArray(array):
    for row in array:
        for item in row:
            print(item, end="")
        print("")
    print("")

# printArray(intTaskInput)

basinSizes = []
for y, row in enumerate(intTaskInput):
    for x, digit in enumerate(row):
        point, surroundings = getPointAndSurroundings(intTaskInput, y, x)
        isLowPoint = checkIfLowPoint(digit, surroundings)

        if isLowPoint:
            basinSizes.append(len(getBasinSize(intTaskInput, y, x, set())))

basinSizes.sort()

product = 1
for size in basinSizes[-3:]:  # biggest three sizes
    product *= size

print("product of three biggest basins is %s" % product)
