import matplotlib.pyplot as plt

# TODO: remember, if paths intersect, only the "cheaper" path needs to stay

with open("input\\testinput.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput = list(map(lambda y:list(map(lambda x:int(x), y)), taskInput))  # make each stringlet into int

def printVisitedCoords(riskMap, highlightCoords=[]):
    for y, row in enumerate(riskMap):
        for x, risk in enumerate(row):
            if (y, x) in highlightCoords:
                print('\033[96m%s\033[0m' % risk, end="")
            else:
                print(risk, end="")
        print("")

def in_bounds(matrix, row, col):
    if row < 0 or col < 0:
        return False
    if row > len(matrix)-1 or col > len(matrix)-1:
        return False
    return True

targetX = len(taskInput[0]) - 1
targetY = len(taskInput) - 1

print("target size: %s" % (targetX + targetY + 1))
print("")

finishedPaths = []  # [[[(pathCoordY, pathCoordX), ...], risk], ...]
paths = [[[(0, 0)], 0]]  # [[[(pathCoordY, pathCoordX), ...], risk], ...]
anyPathFound = False
while not anyPathFound:
    for pathPack in list(paths):
        paths.remove(pathPack)
        headCoords = pathPack[0][-1]
        if headCoords == (targetY, targetX):
            anyPathFound = True
            finishedPaths.append(pathPack)
            continue
        headY = headCoords[0]
        headX = headCoords[1]

        neighbourCoords = []
        if in_bounds(taskInput, headY+1, headX):
            neighbourCoords.append((headY+1, headX))
        if in_bounds(taskInput, headY-1, headX):
            neighbourCoords.append((headY-1, headX))
        if in_bounds(taskInput, headY, headX+1):
            neighbourCoords.append((headY, headX+1))
        if in_bounds(taskInput, headY, headX-1):
            neighbourCoords.append((headY, headX-1))

        
        for neighbourCoord in neighbourCoords:
            if neighbourCoord not in pathPack[0]:
                newPath = pathPack[0] + [neighbourCoord]
                newRisk = pathPack[1] + taskInput[neighbourCoord[0]][neighbourCoord[1]]
                paths.append([newPath, newRisk])

    minRisk = None
    for pathPack in finishedPaths:
        if minRisk == None or minRisk > pathPack[1]:
            minRisk = pathPack[1]
    if len(paths) > 1:
        singlePathLength = len(paths[0][0])
    else:
        singlePathLength = "Err"
    print("considering paths: %s (pathlength %s)" % (len(paths), singlePathLength))

print("")
minRisk = None
minRiskPath = None
for pathPack in finishedPaths:
    if minRisk == None or minRisk > pathPack[1]:
        minRisk = pathPack[1]
        minRiskPath = pathPack[0]

printVisitedCoords(taskInput, minRiskPath)
print("\nminimum risk: %s" % minRisk)

plt.imshow(taskInput, cmap="coolwarm", interpolation='nearest')
plt.colorbar()

Xcoords = []
Ycoords = []
for y, x in minRiskPath:
    Ycoords.append(y)
    Xcoords.append(x)
plt.plot(Xcoords, Ycoords, color="g", linewidth=2)
plt.show()  