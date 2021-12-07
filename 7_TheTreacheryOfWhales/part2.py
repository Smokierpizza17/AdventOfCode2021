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

currentLowestFuel = None
for target in range(minimum, maximum+1):
    totalFuel = 0
    for crabPos in taskInput:
        totalFuel += computeFuel(target, crabPos)
    if currentLowestFuel == None or totalFuel < currentLowestFuel:
        currentLowestFuel = totalFuel

print(currentLowestFuel)
