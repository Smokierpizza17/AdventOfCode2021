with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput = taskInput[0].split(",")
taskInput = list(map(lambda x:int(x), taskInput))

taskInput.sort()

median = taskInput[len(taskInput)//2]

fuelUsed = 0
for i in taskInput:
    fuelUsed += abs(median - i)
print("movement to %s uses %s fuel" % (median, fuelUsed))
