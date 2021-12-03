with open("inputs\\input1.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput = list(map(lambda x:list(x), taskInput))

oxygenGeneratorList = list(taskInput)  # copy of taskInput
CO2ScrubberList = list(taskInput)

gammaRate = []
epsilonRate = []
for index in range(len(taskInput[0])):
    zeroSum = 0
    oneSum  = 0
    for number in oxygenGeneratorList:
        if number[index] == "0":
            zeroSum += 1
        elif number[index] == "1":
            oneSum += 1
    if zeroSum > oneSum:  # remove 1 from Oxygen
        if len(oxygenGeneratorList) > 1:
            for number in list(oxygenGeneratorList):
                if number[index] == "1":
                    oxygenGeneratorList.remove(number)

    elif zeroSum <= oneSum:  # remove 0 from Oxygen
        if len(oxygenGeneratorList) > 1:
            for number in list(oxygenGeneratorList):
                if number[index] == "0":
                    oxygenGeneratorList.remove(number)
    
    zeroSum = 0
    oneSum  = 0
    for number in CO2ScrubberList:
        if number[index] == "0":
            zeroSum += 1
        elif number[index] == "1":
            oneSum += 1
    if zeroSum > oneSum:  # remove 0 from CO2
        if len(CO2ScrubberList) > 1:
            for number in list(CO2ScrubberList):
                if number[index] == "0":
                    CO2ScrubberList.remove(number)

    elif zeroSum <= oneSum:  # remove 1 from CO2
        if len(CO2ScrubberList) > 1:
            for number in list(CO2ScrubberList):
                if number[index] == "1":
                    CO2ScrubberList.remove(number)

    if len(CO2ScrubberList) == 1 and len(oxygenGeneratorList) == 1:
        break

oxygenGeneratorInt = int("".join(oxygenGeneratorList[0]), base=2)
CO2ScrubberList = int("".join(CO2ScrubberList[0]), base=2)

print("oxygen:  %s" % oxygenGeneratorInt)
print("CO2:     %s" % CO2ScrubberList)
print("product: %s" % (oxygenGeneratorInt * CO2ScrubberList))
