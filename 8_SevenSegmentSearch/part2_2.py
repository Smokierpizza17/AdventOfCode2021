with open("inputs\\testinput.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

def intersect(list1, list2):
    return list(set(list1) & set(list2))

def difference(list1, list2):
    return list(set(list1) - set(list2)) + list(set(list2) - set(list1))  

combedInput = []

for line in taskInput:
    twoParts = line.split(" | ")
    uniquePatterns = twoParts[0].split(" ")
    fourDigits = twoParts[1].split(" ")
    combedInput.append([uniquePatterns, fourDigits])

identifiableDigits = 0
for series in combedInput:
    pass