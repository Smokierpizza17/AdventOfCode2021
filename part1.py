import re

with open("inputs\\input1.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

instructionR = re.compile(r"[a-z]+")
valueR = re.compile(r"[0-9]+")

horizontalSum = 0
depthSum = 0
for i in taskInput:
    print(i)
    instruction = re.search(instructionR, i).group()
    value = int(re.search(valueR, i).group())
    if instruction == "down":
        depthSum += value
    elif instruction == "up":
        depthSum -= value
    elif instruction == "forward":
        horizontalSum += value
    elif instruction == "backward":
        horizontalSum -= value

print("")
print("depth: %s" % depthSum)
print("horizontal: %s" % horizontalSum)
print("product: %s" % (depthSum * horizontalSum))
