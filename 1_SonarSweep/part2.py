with open("inputs\\input2.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

for index in range(len(taskInput)):
    taskInput[index] = int(taskInput[index])

increaseCount = 0
prevWindowSum = None
windowSum = taskInput[0] + taskInput[1] + taskInput[2]
for index in range(3,len(taskInput)):  # ignoring first three numbers and first window
    prevWindowSum = windowSum
    windowSum = taskInput[index-2] + taskInput[index-1] + taskInput[index]
    if prevWindowSum < windowSum:
        increaseCount += 1

print("total number of window increases: %s" % increaseCount)
