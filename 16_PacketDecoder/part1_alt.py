import re

with open("inputs\\testinput.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput = int(taskInput[0], 16)
print(format(taskInput, "b"))

class Packet():
    def __init__(self, packetString):
        self.packetList = list(packetString)
        self.version = int("".join(self.packetList[0:3]), 2)
        self.type = int("".join(self.packetList[3:6]), 2)

        if self.type == 4:  # literal
            self.value = self.getLiteralValue()
        else:
            self.lengthID = int(self.packetList[6], 2)
            if self.lengthID == 0:  # next 15 bits are length
                self.length = int("".join(self.packetList[7:22]), 2)
                self.containedBits = self.packetList[23:]
            elif self.lengthID == 1:  # next 11 bits are number of subpackets
                self.length = int("".join(self.packetList[7:18]), 2)
                self.containedBits = self.packetList[19:]

            self.subPackets = []

    def getLiteralValue(self):
        '''finds and sets self.value to literal value stored in list'''
        if self.type != 4:
            raise TypeError
        numberBits = []
        groupBits = self.packetList[6:]
        for group in re.findall(".....", "".join(groupBits)):
            numberBits += group[1:]
            flowBit = group[0]
            if flowBit == "1":  # not last group
                continue
            elif flowBit == "0":  # last group, stop parsing
                break
        return int("".join(numberBits), 2)

    def getSubpackets(self):
        '''finds subpackets and adds them to self.subPackets'''
        if self.lengthID == 0: # bitlength given
            bitsToConsider = self.containedBits[:self.length-1]
            self.subPackets.append(Packet(bitsToConsider))
        elif self.lengthID == 1:  # subpacket count given
            pass
