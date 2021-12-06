with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

DAYSTOSIMULATE = 256

taskInput = list(map(lambda x:int(x), taskInput[0].split(",")))

lanternFishMap = {}

for i in range(9):
    lanternFishMap[i] = 0

for fish in taskInput:
    lanternFishMap[fish] += 1

for day in range(DAYSTOSIMULATE):
    fishRegen = int(lanternFishMap[0])
    for index in range(0,8):
        lanternFishMap[index] = int(lanternFishMap[index + 1])
    lanternFishMap[8] = 0
    lanternFishMap[6] += fishRegen
    lanternFishMap[8] += fishRegen

fishSum = 0
for fishCount in lanternFishMap.values():
    fishSum += fishCount

print("after %s days, there are %s fish" % (DAYSTOSIMULATE, fishSum))
