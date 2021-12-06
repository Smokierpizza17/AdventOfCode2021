with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

DAYSTOSIMULATE = 80

taskInput = list(map(lambda x:int(x), taskInput[0].split(",")))

LanternfishList = []
class Lanternfish():
    def __init__(self, daysRem):
        LanternfishList.append(self)
        self.daysRem = daysRem
    
    def tick(self):
        if self.daysRem == 0:
            self.daysRem = 6
            # Lanternfish(8)
        else:
            self.daysRem -= 1

for fishAge in taskInput:
    Lanternfish(fishAge)

for day in range(DAYSTOSIMULATE):
    fishString = str(day+1) + ": "
    for fish in list(LanternfishList):
        fish.tick()
        fishString += str(fish.daysRem)
    # print(fishString)

print("")
print("after %s days, there are %s fish" % (DAYSTOSIMULATE, len(LanternfishList)))
