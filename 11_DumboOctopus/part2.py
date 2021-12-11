with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput = list(map(lambda y:list(map(lambda x:int(x), y)), taskInput))  # make each stringlet into int

STEPSTOSIMULATE = 100
ALLFLASHCOUNT = len(taskInput) * len(taskInput[0])

def printOctopi(octopusArray, highlightCoords=[]):
    for y, row in enumerate(octopusArray):
        for x, octo in enumerate(row):
            if (y,x) in highlightCoords:
                print('\033[1m' + str(octo) + '\033[0m', end="")
            else:
                print(octo, end="")
        print("")

def in_bounds(matrix, row, col):
    if row < 0 or col < 0:
        return False
    if row > len(matrix)-1 or col > len(matrix)-1:
        return False
    return True

def incrementArray(array):
    '''adds 1 to all values of 2D array'''
    for row in array:
        for item in row:
            item += 1
    return array

def flashOctopus(octopusArray, y, x, alreadyFlashed):
    '''returnss new octopusArray after all flashes have been processed, as well as how many flashed total'''
    alreadyFlashed.add((y,x))

    neighbourCoords = []
    for deltaY in range(-1,2):  # -1;0;1
        for deltaX in range(-1,2):  # -1;0;1
            if in_bounds(octopusArray, y+deltaY, x+deltaX):
                neighbourCoords.append((y+deltaY, x+deltaX))
    
    for neighbourCoord in neighbourCoords:
        neighbourY = neighbourCoord[0]
        neighbourX = neighbourCoord[1]
        octopusArray[neighbourY][neighbourX] += 1
    
    for y, row in enumerate(octopusArray):
        for x, value in enumerate(row):
            if value > 9 and not (y,x) in alreadyFlashed:
                octopusArray, alreadyFlashed = flashOctopus(octopusArray, y, x, alreadyFlashed)

        for flashedCoord in alreadyFlashed:
            resetY = flashedCoord[0]
            resetX = flashedCoord[1]
            octopusArray[resetY][resetX] = 0

    return octopusArray, alreadyFlashed

print("after 0:")
printOctopi(taskInput)
totalFlashes = 0
step = 0
while True:
    taskInput = incrementArray(taskInput)
    alreadyFlashed = set()
    for y, row in enumerate(taskInput):
        for x, value in enumerate(row):
                taskInput[y][x] += 1

    for y, row in enumerate(taskInput):
        for x, value in enumerate(row):
            if value > 9:
                taskInput, flashedCoords = flashOctopus(taskInput, y, x, alreadyFlashed)
                totalFlashes += len(flashedCoords)
    print("after %s:" % (step + 1))
    if 'flashedCoords' in locals():
        printOctopi(taskInput, flashedCoords)
        print("(%s)\n" % len(flashedCoords))
        if len(flashedCoords) >= ALLFLASHCOUNT:
            print("all octopi flased on step %s" % (step + 1))
            break
    else:
        printOctopi(taskInput)
        print("(0)\n")
    
    step += 1
