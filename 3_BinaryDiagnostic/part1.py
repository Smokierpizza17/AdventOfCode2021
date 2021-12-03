with open("inputs\\input1.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput = list(map(lambda x:list(x), taskInput))

gammaRate = []
epsilonRate = []
for index in range(len(taskInput[0])):
    zeroSum = 0
    oneSum  = 0
    for number in taskInput:
        if number[index] == "0":
            zeroSum += 1
        elif number[index] == "1":
            oneSum += 1
    if zeroSum > oneSum:
        gammaRate.append("0")
        epsilonRate.append("1")
    else:
        gammaRate.append("1")
        epsilonRate.append("0")

gammaInt = int("".join(gammaRate), base=2)
epsilonInt = int("".join(epsilonRate), base=2)

print("gamma:   %s" % gammaInt)
print("epsilon: %s" % epsilonInt)
print("product: %s" % (gammaInt * epsilonInt))
