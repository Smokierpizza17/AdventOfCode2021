import re
import math as maths

STEPSTOSIMULATE = 40

with open("inputs\\input.txt", "r") as inputFile:
    JoinedInput = inputFile.read().split("\n\n")

chainString = JoinedInput[0]
insertInstructions = JoinedInput[1].split("\n")

def getPolymerMap(chainString):
    chainList = list(chainString)
    polymerMap = {}
    for index in range(len(chainList) - 1):  # looks ahead, so must stop one before
        firstAtom = chainList[index]
        secondAtom = chainList[index + 1]
        pairKey = firstAtom + secondAtom
        if pairKey in polymerMap.keys():
            polymerMap[pairKey] += 1
        else:
            polymerMap[pairKey] = 1
    return polymerMap

inserteeR = re.compile(r"(?<= -> ).+")
insertNeighboursR = re.compile(r".+(?= -> )")

insertionMap = {}
for instr in insertInstructions:
    insertee = re.search(inserteeR, instr).group()
    neighbours = re.search(insertNeighboursR, instr).group()
    insertionPairs = [neighbours[0] + insertee, insertee + neighbours[1], insertee]
    insertionMap[neighbours] = insertionPairs

polymerMap = getPolymerMap(chainString)

for step in range(1, STEPSTOSIMULATE+1):
    workingCopy = dict(polymerMap)
    for pairKey, pairCount in workingCopy.items():
        if pairKey in insertionMap.keys():
            newPairs = insertionMap[pairKey]
            polymerMap[pairKey] -= pairCount
            if newPairs[0] in polymerMap.keys():
                polymerMap[newPairs[0]] += pairCount
            else:
                polymerMap[newPairs[0]] = pairCount
            if newPairs[1] in polymerMap.keys():
                polymerMap[newPairs[1]] += pairCount
            else:
                polymerMap[newPairs[1]] = pairCount

atomCount = {}
for pair, frequency in polymerMap.items():
    firstAtom = pair[0]
    secondAtom = pair[1]

    if firstAtom in atomCount.keys():
        atomCount[firstAtom] += frequency
    else:
        atomCount[firstAtom] = frequency

    if secondAtom in atomCount.keys():
        atomCount[secondAtom] += frequency
    else:
        atomCount[secondAtom] = frequency

for atom, frequency in dict(atomCount).items():
    atomCount[atom] = maths.ceil(frequency / 2)

print("")
print(atomCount)

lowestFrequency = None
highestFrequency = None
for frequency in atomCount.values():
    if lowestFrequency == None or frequency < lowestFrequency:
        lowestFrequency = frequency
    if highestFrequency == None or frequency > highestFrequency:
        highestFrequency = frequency

freqDiff = highestFrequency - lowestFrequency
print("frequency difference is %s" % freqDiff)
