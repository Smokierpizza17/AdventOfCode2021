import re

with open("inputs\\testinput.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput = int(taskInput[0], 16)
print(format(taskInput, "b"))

def interpretPacket(packInt, lengthType=None, maxParseLength=None):
    bits = list(format(packInt, "b"))
    if maxParseLength != None:
        if lengthType == 0:  # bitlength given
            bits = bits[0:maxParseLength]
        elif lengthType == 1: # packetcount given
            pass
    version = int("".join(bits[0:3]), 2)
    type = int("".join(bits[3:6]), 2)
    if type == 4:  # literal value
        numberBits = []
        groupBits = bits[6:]
        for group in re.findall(".....", "".join(groupBits)):
            numberBits += group[1:]
            flowBit = group[0]
            if flowBit == "1":  # not last group
                continue
            elif flowBit == "0":  # last group, stop parsing
                break
        print("LITERAL: %s" % int("".join(numberBits), 2))
    else:
        lengthID = int(bits[6], 2)
        if lengthID == 0:  # next 15 bits are length
            length = int("".join(bits[7:22]), 2)
            result = interpretPacket(int("".join(bits[23:]), 2), lengthID, length)
        elif lengthID == 1:  # next 11 bits are number of subpackets
            length = int("".join(bits[7:18]), 2)#
            result = interpretPacket(int("".join(bits[19:]), 2), lengthID, length)
        
# EFFIN PACKETS ARE COMPLICATED AND I DONT WANNA

interpretPacket(taskInput)
