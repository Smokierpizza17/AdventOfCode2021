with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

def getCave(caveName):
    '''returns CaveObject from caveNetwork that matches caveName'''
    global caveNetwork
    for cave in caveNetwork:
        if cave.name == caveName:
            return cave

def findPaths(start, end):
    '''finds all paths from current to end through caves. Small caves can only be visited once'''
    possiblePaths = []
    possiblePaths.append([start.name])

    changed = True
    while changed:
        changed = False
        for path in list(possiblePaths):
            if path[-1] == "end":
                continue
            head = getCave(path[-1])
            neighbours = list(head.connections)
            for neighbour in list(neighbours):
                if not neighbour.isBigCave and neighbour.name in path:
                    neighbours.remove(neighbour)
            if len(neighbours) == 0:
                continue
            changed = True
            possiblePaths.remove(path)
            for neighbour in neighbours:
                possiblePaths.append(path + [neighbour.name])

    finalPaths = []
    for path in possiblePaths:
        if path[0] == start.name and path[-1] == end.name:
            finalPaths.append(path)
    
    return finalPaths


caveNetwork = []
class Cave():
    def __init__(self, name, connections=[]):
        caveNetwork.append(self)
        self.name = name
        if name[0].isupper():
            self.isBigCave = True
        else:
            self.isBigCave = False

        if self.name == "start":
            global startCave 
            startCave = self
        elif self.name == "end":
            global endCave 
            endCave = self

        self.connections = []
        for cave in connections:
            self.addConnection(cave)

    def addConnection(self, connectedCave):
        if self.name == "start":
            self.connections.append(connectedCave)
        elif self.name == "end":
            connectedCave.connections.append(self)
        else:
            self.connections.append(connectedCave)
            connectedCave.connections.append(self)

for line in taskInput:
    parsedcaveNetwork = line.split("-")
    firstCave = parsedcaveNetwork[0]
    secondCave = parsedcaveNetwork[1]

    if getCave(firstCave) == None:
        firstCave = Cave(firstCave)
    else:
        firstCave = getCave(firstCave)
    if getCave(secondCave) == None:
        secondCave = Cave(secondCave)
    else:
        secondCave = getCave(secondCave)

    firstCave.addConnection(secondCave)    

paths = findPaths(startCave, endCave)
for path in paths:
    print(path)

print("\n%s" % len(paths))
