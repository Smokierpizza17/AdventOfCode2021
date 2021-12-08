with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

combedInput = []
for line in taskInput:
    twoParts = line.split(" | ")
    observedFlashes = twoParts[0].split(" ")
    fourDigits = twoParts[1].split(" ")
    combedInput.append([observedFlashes, fourDigits])

identifiableDigits = 0
for series in combedInput:
    digits = series[1]
    for number in digits:
        if len(number) in [2, 3, 4, 7]:
            identifiableDigits += 1

print("1, 4, 7 or 9 show up %s times" % identifiableDigits)
