with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")
taskInput = list(map(lambda x:list(x), taskInput))
OPENERS = ["(", "[", "{", "<"]
CLOSERS = [")", "]", "}", ">"]
GETOPPOSITE = {"(": ")", "[": "]", "{": "}", "<": ">",
               ")": "(", "]": "[", "}": "{", ">": "<"}
ILLEGALCHARPOINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
syntaxErrorScore = 0
for line in taskInput:
    stillOpenList = []
    for char in line:
        if char in OPENERS:
            stillOpenList.append(char)
        elif char in CLOSERS:
            expectedChar = GETOPPOSITE[stillOpenList[-1]]
            if char == expectedChar:
                stillOpenList.pop()
            else:
                syntaxErrorScore += ILLEGALCHARPOINTS[char]
                break
print("total syntax error score: %s" % syntaxErrorScore)