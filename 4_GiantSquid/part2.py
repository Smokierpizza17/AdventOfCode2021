import re

with open("inputs\\input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

numbersR = re.compile(r"[0-9]+")

#  taskInput = list(map(lambda x:list(x), taskInput))

numberSeries = taskInput[0].split(",")
numberSeries = list(map(lambda x:int(x), numberSeries))

taskInput = taskInput[2:]  # remove numberSeries and newline

def findWinningBoards(numbers, boards):
    '''returns list of scores in order of first to win to last'''
    winnerList = []
    boardsRemaining = list(boards)
    for newNumber in numbers:
        for board in list(boardsRemaining):
            board.checkNumber(newNumber)
            winner = board.isWinner(newNumber)
            if winner != False:
                winnerList.append(winner)
                boardsRemaining.remove(board)
    return winnerList


bingoBoards = []
class bingoBoard():
    def __init__(self, numbers):
        bingoBoards.append(self)
        self.numbers = numbers
        for yIndex in range(len(self.numbers)):
            for xIndex in range(len(self.numbers[yIndex])):
                actualNumber = self.numbers[yIndex][xIndex]
                self.numbers[yIndex][xIndex] = [actualNumber, False]

    def positionIsChecked(self, y, x):
        return self.numbers[y][x][1]

    def checkNumber(self, numberToCheck):
        '''sets isChecked of number to True, if number equals number given'''
        for row in self.numbers:
            for number in row:
                if number[0] == int(numberToCheck):
                    number[1] = True

    def isWinner(self, lastNumber=False):
        '''False if not, else ScoreInt if all numbers in a row or column are checked'''
        anyWinner = False
        for row in self.numbers:
            allWinnersInSeries = True
            for number in row:
                allWinnersInSeries = allWinnersInSeries and number[1]
            anyWinner = anyWinner or allWinnersInSeries
        for columnIndex in range(len(self.numbers[0])):
            columnSeries = []
            for row in self.numbers:
                columnSeries.append(row[columnIndex])
            allWinnersInSeries = True
            for number in columnSeries:
                allWinnersInSeries = allWinnersInSeries and number[1]
            anyWinner = anyWinner or allWinnersInSeries
        if anyWinner:
            if lastNumber != False:
                uncheckedSum = 0
                for row in self.numbers:
                    for number in row:
                        if number[1] == False:
                            uncheckedSum += number[0]
                return uncheckedSum * lastNumber
            else:
                return True
        else:
            return False



for board in "\n".join(taskInput).split("\n\n"):
    boardArray = []
    for row in board.split("\n"):
        rowSeries = []
        for number in re.finditer(numbersR, row):
            rowSeries.append(int(number.group()))
        boardArray.append(rowSeries)
    bingoBoard(boardArray)

winnerSeries = findWinningBoards(numberSeries, bingoBoards)
print("last board of %s to win has score %s" % (len(winnerSeries), winnerSeries[-1]))
