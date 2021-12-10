import statistics as stats

with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput = list(map(lambda x:list(x), taskInput))

OPENERS = ["(", "[", "{", "<"]
CLOSERS = [")", "]", "}", ">"]
GETOPPOSITE = {"(": ")", "[": "]", "{": "}", "<": ">",
               ")": "(", "]": "[", "}": "{", ">": "<"}

ILLEGALCHARPOINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETIONCHARPOINTS = {")": 1, "]": 2, "}": 3, ">": 4}

completionScores = []
for line in taskInput:
    print("".join(line) + "\t", end="")
    stillOpenList = []
    corrupted = False
    for char in line:
        if char in OPENERS:
            stillOpenList.append(char)
        elif char in CLOSERS:
            expectedChar = GETOPPOSITE[stillOpenList[-1]]
            if char == expectedChar:
                stillOpenList.pop()
            else:
                print("expected \"%s\", but found \"%s\"" % (expectedChar, char), end="")
                corrupted = True
                break
    if len(stillOpenList) > 0 and not corrupted:
        completionChars = []
        stillOpenList.reverse()
        for openBracket in stillOpenList:
            completionChars.append(GETOPPOSITE[openBracket])
        
        print("complete with \"%s\"" % "".join(completionChars), end="")

        completionScore = 0
        for char in completionChars:
            completionScore *= 5
            completionScore += COMPLETIONCHARPOINTS[char]
        print("\t score: %s" % completionScore)
        completionScores.append(completionScore)

    print("")

print("")
print("median completion score: %s" % stats.median(completionScores))
