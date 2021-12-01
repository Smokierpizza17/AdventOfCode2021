with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

increaseCount = 0
print(taskInput[0] + " (N/A)")

for index in range(1,len(taskInput)):  # skips first value
    if taskInput[index-1] <= taskInput[index]:
        increaseCount += 1
        print(taskInput[index] + " (+)")
    else:
        print(taskInput[index])

print("")
print("total number of increases: %s" % increaseCount)
