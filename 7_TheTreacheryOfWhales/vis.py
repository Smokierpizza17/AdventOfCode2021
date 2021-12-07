import matplotlib.pyplot as plt

with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

def computeFuel(targetPosition, origPosition):
    delta = abs(targetPosition - origPosition)
    return delta * (delta + 1) // 2  # mathematical magic, (= 1 + 2 + ... + delta)

taskInput = taskInput[0].split(",")
taskInput = list(map(lambda x:int(x), taskInput))

taskInput.sort()
maximum = taskInput[-1]
minimum = taskInput[0]

fuelX = list(range(minimum, maximum+1))

fuelY1 = []
for target in fuelX:
    totalFuel = 0
    for crabPos in taskInput:
        totalFuel += abs(crabPos - target)
    fuelY1.append(totalFuel)

fuelY2 = []
for target in fuelX:
    totalFuel = 0
    for crabPos in taskInput:
        totalFuel += computeFuel(target, crabPos)
    fuelY2.append(totalFuel)


plt.title("fuelCons y, targetPos x, part1 green, part2 blue, crabPos red")
plt.plot(fuelX, fuelY1, "-g")
plt.plot(fuelX, fuelY2, "-b")
plt.plot(taskInput, [1] * len(taskInput), ".r")
plt.show()
