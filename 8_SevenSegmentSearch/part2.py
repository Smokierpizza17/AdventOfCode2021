with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

def intersect(list1, list2):
    return list(set(list1) & set(list2))

def difference(list1, list2):
    return list(set(list1) - set(list2)) + list(set(list2) - set(list1))

def getInversePossibilities(possMap):
    '''for a map like {"a": [1,2], "b": [2,3]}
       returns map like {1: ["a"], 2: ["a", "b"], 3: ["b"]}'''
    allKeys = possMap.keys()
    allValues = []
    for valueString in possMap.values():
        for value in valueString:
            if not value in allValues:
                allValues.append(value)
    inverseMap = {}
    for value in allValues:
        keysWithValue = []
        for key in allKeys:
            if value in possMap[key]:
                keysWithValue.append(key)
        inverseMap[value] = keysWithValue
    return inverseMap

def decodeSegments(segments):
    '''returns integer that segments represent. e.g. [topRight, bottomRight] -> 1'''
    segments = set(segments)
    if segments == {"top", "bottom", "topLeft", "topRight", "bottomLeft", "bottomRight"}:  # 0
        return 0
    elif segments == {"topRight", "bottomRight"}:  # 1
        return 1
    elif segments == {"top", "middle", "bottom", "topRight", "bottomLeft"}:  # 2
        return 2
    elif segments == {"top", "middle", "bottom", "topRight", "bottomRight"}:  # 3
        return 3
    elif segments == {"middle", "topLeft", "topRight", "bottomRight"}:  # 4
        return 4
    elif segments == {"top", "middle", "bottom", "topLeft", "bottomRight"}:  # 5
        return 5
    elif segments == {"top", "middle", "bottom", "topLeft", "bottomLeft", "bottomRight"}:  # 6
        return 6
    elif segments == {"top", "topRight", "bottomRight"}:  # 7
        return 7
    elif segments == {"top", "middle", "bottom", "topLeft", "topRight", "bottomLeft", "bottomRight"}:  # 8
        return 8
    elif segments == {"top", "middle", "bottom", "topLeft", "topRight", "bottomRight"}:  # 9
        return 9
    else:
        return "Err"

def getAllPossibleShapes(possMap, segments):
    '''for all the possibilities, return list of all shapes (list of segments) given segmentList could be'''
    inverseMap = getInversePossibilities(possMap)
    positionsList = []
    for segment in segments:
        positionsList.append(inverseMap[segment])
    

combedInput = []
ALLPOSSIBILITIES = {"top":         ["a", "b", "c", "d", "e", "f", "g"],
                    "middle":      ["a", "b", "c", "d", "e", "f", "g"],
                    "bottom":      ["a", "b", "c", "d", "e", "f", "g"],
                    "bottomLeft":  ["a", "b", "c", "d", "e", "f", "g"],
                    "bottomRight": ["a", "b", "c", "d", "e", "f", "g"],
                    "topLeft":     ["a", "b", "c", "d", "e", "f", "g"],
                    "topRight":    ["a", "b", "c", "d", "e", "f", "g"]}

for line in taskInput:
    twoParts = line.split(" | ")
    uniquePatterns = twoParts[0].split(" ")
    fourDigits = twoParts[1].split(" ")
    combedInput.append([uniquePatterns, fourDigits])

totalSum = 0
for series in combedInput:
    finalAssignments = {}
    uniquePatterns = series[0]
    possibilitiesMap = ALLPOSSIBILITIES.copy()

    # identify 1s, 4s, 7s, and 8s and rule out segments accordingly
    for pattern in uniquePatterns:
        segments = list(pattern)
        if len(pattern) == 2:  # 1
            possibilitiesMap["topRight"] = intersect(possibilitiesMap["topRight"], segments)
            possibilitiesMap["bottomRight"] = intersect(possibilitiesMap["bottomRight"], segments)
            oneSegments = segments
        elif len(pattern) == 3:  # 7
            possibilitiesMap["top"] = intersect(possibilitiesMap["top"], segments)
            possibilitiesMap["topRight"] = intersect(possibilitiesMap["topRight"], segments)
            possibilitiesMap["bottomRight"] = intersect(possibilitiesMap["bottomRight"], segments)
        elif len(pattern) == 4:  # 4
            possibilitiesMap["middle"] = intersect(possibilitiesMap["middle"], segments)
            possibilitiesMap["topLeft"] = intersect(possibilitiesMap["topLeft"], segments)
            possibilitiesMap["topRight"] = intersect(possibilitiesMap["topRight"], segments)
            possibilitiesMap["bottomRight"] = intersect(possibilitiesMap["bottomRight"], segments)
            fourSegments = segments
        elif len(pattern) == 7:  # 8
            possibilitiesMap["top"] = intersect(possibilitiesMap["top"], segments)
            possibilitiesMap["middle"] = intersect(possibilitiesMap["middle"], segments)
            possibilitiesMap["bottom"] = intersect(possibilitiesMap["bottom"], segments)
            possibilitiesMap["topLeft"] = intersect(possibilitiesMap["topLeft"], segments)
            possibilitiesMap["topRight"] = intersect(possibilitiesMap["topRight"], segments)
            possibilitiesMap["bottomLeft"] = intersect(possibilitiesMap["bottomLeft"], segments)
            possibilitiesMap["bottomRight"] = intersect(possibilitiesMap["bottomRight"], segments)
        elif len(pattern) == 5:  # 2, 3, 5
            pass
        elif len(pattern) == 6:  # 0, 9
            pass
    
    Lsegments = difference(oneSegments, fourSegments)  # difference of two lists

    # use the intersect of the remaining digits with oneSegments and Lsegments to figure them out
    for pattern in uniquePatterns:
        segments = list(pattern)
        if len(pattern) == 5:  # 2, 3, 5
            if len(intersect(segments, oneSegments)) == 1 and len(intersect(segments, Lsegments)) == 1:  # 2
                possibilitiesMap["top"] = intersect(possibilitiesMap["top"], segments)
                possibilitiesMap["middle"] = intersect(possibilitiesMap["middle"], segments)
                possibilitiesMap["bottom"] = intersect(possibilitiesMap["bottom"], segments)
                possibilitiesMap["topRight"] = intersect(possibilitiesMap["topRight"], segments)
                possibilitiesMap["bottomLeft"] = intersect(possibilitiesMap["bottomLeft"], segments)
            elif len(intersect(segments, oneSegments)) == 2 and len(intersect(segments, Lsegments)) == 1:  # 3
                possibilitiesMap["top"] = intersect(possibilitiesMap["top"], segments)
                possibilitiesMap["middle"] = intersect(possibilitiesMap["middle"], segments)
                possibilitiesMap["bottom"] = intersect(possibilitiesMap["bottom"], segments)
                possibilitiesMap["topRight"] = intersect(possibilitiesMap["topRight"], segments)
                possibilitiesMap["bottomRight"] = intersect(possibilitiesMap["bottomRight"], segments)
            elif len(intersect(segments, oneSegments)) == 1 and len(intersect(segments, Lsegments)) == 2:  # 5
                possibilitiesMap["top"] = intersect(possibilitiesMap["top"], segments)
                possibilitiesMap["middle"] = intersect(possibilitiesMap["middle"], segments)
                possibilitiesMap["bottom"] = intersect(possibilitiesMap["bottom"], segments)
                possibilitiesMap["topLeft"] = intersect(possibilitiesMap["topLeft"], segments)
                possibilitiesMap["bottomRight"] = intersect(possibilitiesMap["bottomRight"], segments)
        elif len(pattern) == 6:  # 0, 9
            if len(intersect(segments, oneSegments)) == 2 and len(intersect(segments, Lsegments)) == 2:  # 9
                possibilitiesMap["top"] = intersect(possibilitiesMap["top"], segments)
                possibilitiesMap["middle"] = intersect(possibilitiesMap["middle"], segments)
                possibilitiesMap["bottom"] = intersect(possibilitiesMap["bottom"], segments)
                possibilitiesMap["topLeft"] = intersect(possibilitiesMap["topLeft"], segments)
                possibilitiesMap["topRight"] = intersect(possibilitiesMap["topRight"], segments)
                possibilitiesMap["bottomRight"] = intersect(possibilitiesMap["bottomRight"], segments)
            elif len(intersect(segments, oneSegments)) == 2 and len(intersect(segments, Lsegments)) == 1:  # 0
                possibilitiesMap["top"] = intersect(possibilitiesMap["top"], segments)
                possibilitiesMap["bottom"] = intersect(possibilitiesMap["bottom"], segments)
                possibilitiesMap["topLeft"] = intersect(possibilitiesMap["topLeft"], segments)
                possibilitiesMap["topRight"] = intersect(possibilitiesMap["topRight"], segments)
                possibilitiesMap["bottomLeft"] = intersect(possibilitiesMap["bottomLeft"], segments)
                possibilitiesMap["bottomRight"] = intersect(possibilitiesMap["bottomRight"], segments)

    # keep removing segment possibilities when they're already uniquely assigned to another segment
    while len(finalAssignments) < 7:
        for segment, possibilities in possibilitiesMap.items():
            if len(possibilities) == 1:
                finalAssignments[possibilities[0]] = segment
            else:
                for removableSegment in finalAssignments.keys():
                    try:
                        if removableSegment in possibilities:
                            possibilitiesMap[segment].remove(removableSegment)
                    except KeyError:
                        pass

    # decode the numbers after | 
    numberString = ""
    for encodedDigit in series[1]:
            segmentStrings = []
            for encodedSegment in encodedDigit:
                segmentStrings.append(finalAssignments[encodedSegment])
            digit = decodeSegments(segmentStrings)
            numberString += str(digit)
    print("%s: %s" % (" ".join(series[1]), numberString))
    totalSum += int(numberString)

print("")
print("SUM: %s" % totalSum)
