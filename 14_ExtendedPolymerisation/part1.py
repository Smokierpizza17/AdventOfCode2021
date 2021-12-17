import re

STEPSTOSIMULATE = 3

with open("inputs\\testinput.txt", "r") as inputFile:
    JoinedInput = inputFile.read().split("\n\n")

chainList = list(JoinedInput[0])
insertInstructions = JoinedInput[1].split("\n")

inserteeR = re.compile(r"(?<= -> ).+")
insertNeighboursR = re.compile(r".+(?= -> )")

insertionMap = {}
for instr in insertInstructions:
    insertee = re.search(inserteeR, instr).group()
    neighbours = re.search(insertNeighboursR, instr).group()
    insertionMap[neighbours] = insertee

print("0: %s" % "".join(chainList))

for step in range(1, STEPSTOSIMULATE + 1):
    insertPairs = []
    for index in range(len(chainList) - 1):  # looks ahead, so must stop one before
        leftAtom = chainList[index]
        rightAtom = chainList[index + 1]
        insertKey = leftAtom + rightAtom
        if insertKey in insertionMap.keys():
            insertPairs.append((index + 1, insertionMap[insertKey]))

    indexCompensation = 0  # so that previous insertions don't eff up later ones
    for index, insertee in insertPairs:
        chainList.insert(index + indexCompensation, insertee)
        indexCompensation += 1
    if len(chainList) < 100:
        print("%s: %s (%s)" % (step, "".join(chainList), len(chainList)))
    else:
        print("%s: [...] (%s)" % (step, len(chainList)))

print("")

frequencyMap = {}
for element in chainList:
    if element in frequencyMap.keys():
        frequencyMap[element] += 1
    else:
        frequencyMap[element] = 1

print(frequencyMap)

lowestFrequency = None
highestFrequency = None
for frequency in frequencyMap.values():
    if lowestFrequency == None or frequency < lowestFrequency:
        lowestFrequency = frequency
    if highestFrequency == None or frequency > highestFrequency:
        highestFrequency = frequency

freqDiff = highestFrequency - lowestFrequency
print("frequency difference is %s" % freqDiff)
