import re

with open("inputs\\input1.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

instructionR = re.compile(r"[a-z]+")
valueR = re.compile(r"[0-9]+")

horizontalSum = 0
depthSum = 0
aim = 0
for i in taskInput:
    print(i)
    instruction = re.search(instructionR, i).group()
    value = int(re.search(valueR, i).group())
    if instruction == "down":
        aim += value
    elif instruction == "up":
        aim -= value
    elif instruction == "forward":
        horizontalSum += value
        depthSum += value * aim
    elif instruction == "backward":
        horizontalSum -= value
        depthSum -= value * aim

print("")
print("depth: %s" % depthSum)
print("horizontal: %s" % horizontalSum)
print("product: %s" % (depthSum * horizontalSum))
