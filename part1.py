with open("inputs\\input1.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

for index in range(len(taskInput)):
    taskInput[index] = int(taskInput[index])

increaseCount = 0
print(str(taskInput[0]) + " (N/A)")

for index in range(1,len(taskInput)):  # skips first value
    if taskInput[index-1] < taskInput[index]:
        increaseCount += 1
        print(str(taskInput[index]) + " (+)")
    else:
        print(str(taskInput[index]))

print("")
print("total number of increases: %s" % increaseCount)
