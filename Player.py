from GameBoard import GameBoard

class Player:
    def __inti__(self, b):
        self.B = b

    def play(self):
        free = 0



    def getBoardVal(self):
        free = 0
        sumNums = 0
        for i in range(16):
            if(self.B.getVal(i) > 0):
                sumNums = sumNums + self.B.getVal(i)
            else:
                free = free + 1
        return free * sumNums


    def getExpVal(self, dire):
        placeHold = 0


    def pickMoveList(self, targNum):
        placeHold = 0


