with open("inputs\\testinput.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

def getCave(caveName):
    '''returns CaveObject from caveNetwork that matches caveName'''
    global caveNetwork
    for cave in caveNetwork:
        if cave.name == caveName:
            return cave

def containsSmallCaveTwice(path):
    '''returns true if a small cave has been visited twice'''
    alreadyVisitedSmall = []
    for cave in path:
        if cave[0].islower():
            if cave in alreadyVisitedSmall:
                return True
            alreadyVisitedSmall.append(cave)
    return False

def findPaths(start, end):
    '''finds all paths from current to end through caves. Small caves can only
    be visited once, except one small cave, which can be visited twice'''
    possiblePaths = []
    possiblePaths.append([[start.name], False])  # condition is "hasVisitedTwice"

    changed = True
    while changed:
        changed = False
        for pathPair in list(possiblePaths):
            path = pathPair[0]
            hasVisitedTwice = pathPair[1]
            if path[-1] == "end":
                continue
            head = getCave(path[-1])
            neighbours = list(head.connections)
            for neighbour in list(neighbours):
                if not neighbour.isBigCave and neighbour.name in path:
                    if hasVisitedTwice:
                        neighbours.remove(neighbour)

            possiblePaths.remove(pathPair)
            if len(neighbours) == 0:
                continue
            changed = True
            for neighbour in neighbours:
                newPath = path + [neighbour.name]
                if not hasVisitedTwice:  # if old path doesn't have visitedTwice set
                    newVisitedTwice = containsSmallCaveTwice(newPath)
                else:
                    newVisitedTwice = hasVisitedTwice
                possiblePaths.append([newPath, newVisitedTwice])

    finalPaths = []
    for pathPair in possiblePaths:
        path = pathPair[0]
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
        elif self.name == "end" or connectedCave.name == "start":
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
print("there are %s paths" % len(paths))

rawString = '''start,A,b,A,b,A,c,A,end
start,A,b,A,b,A,end
start,A,b,A,b,end
start,A,b,A,c,A,b,A,end
start,A,b,A,c,A,b,end
start,A,b,A,c,A,c,A,end
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,d,b,A,c,A,end
start,A,b,d,b,A,end
start,A,b,d,b,end
start,A,b,end
start,A,c,A,b,A,b,A,end
start,A,c,A,b,A,b,end
start,A,c,A,b,A,c,A,end
start,A,c,A,b,A,end
start,A,c,A,b,d,b,A,end
start,A,c,A,b,d,b,end
start,A,c,A,b,end
start,A,c,A,c,A,b,A,end
start,A,c,A,c,A,b,end
start,A,c,A,c,A,end
start,A,c,A,end
start,A,end
start,b,A,b,A,c,A,end
start,b,A,b,A,end
start,b,A,b,end
start,b,A,c,A,b,A,end
start,b,A,c,A,b,end
start,b,A,c,A,c,A,end
start,b,A,c,A,end
start,b,A,end
start,b,d,b,A,c,A,end
start,b,d,b,A,end
start,b,d,b,end
start,b,end'''

expectedOutput = list(map(lambda x:x.split(","), rawString.split("\n")))

#for i in paths:
#    if i not in expectedOutput:
#        print(i)
