'''
This is the class the represents the board,
and contains the move functions as well as a print function


@author Kevin Conyers
@version 0.0.1
'''
import random
class GameBoard:

    def __init__(self):
        self.DOWN = 0
        self.UP = 2
        self.RIGHT = 1
        self.LEFT = 3
        w, h = 4,4
        self.Board = [[0 for x in range(w)] for y in range(h)]
        for i in range(16):

            self.Board[int(i/4)][int(i%4)] = self.Cell(0, i)
        self.addTwo()


    def toString(self):
        out = ""
        for i in range(4):
            out = out +  "\n"
            for j in range(4):
               # out = out +"-----"
                if (self.Board[i][j].getValue() < 10):
                    out = out + "[  " + str(self.Board[i][j].getValue()) + "  ]"
                elif(self.Board[i][j].getValue() < 100):
                    out = out + "[  " +  str(self.Board[i][j].getValue()) + " ]"
                elif(self.Board[i][j].getValue() < 1000):
                    out = out + "[ " + str(self.Board[i][j].getValue()) + " ]"
                elif(self.Board[i][j].getValue() > 1000):
                    out = out + "[" +  str(self.Board[i][j].getValue()) + "]"
            out = out + "-----\n"
           # out = out + "\n"

        return out

    def printMe(self):
        for i in range(4):
           # print()
           # for j in range(4):
           #     if (self.Board[i][j].getValue() < 10):
           #         print("|  ", self.Board[i][j].getValue(), "  |",)
           #     elif(self.Board[i][j].getValue() < 100):
           #         print ("|  ", self.Board[i][j].getValue(), " |",)
           #     elif(self.Board[i][j].getValue() < 1000):
           #         print ("| ", self.Board[i][j].getValue(), " |",)
           #     elif(self.Board[i][j].getValue() > 1000):
           #         print ("|", self.Board[i][j].getValue(), "|",)
           # print()
           print(self.toString())
        return 0


    def setSpot(self, x, y, val):
        self.Board[x][y].setValue(val)

    def clearMe(self):
        for i in range(16):
            self.setByRowMaj(i, 0)

    def getVal(self, rowMajor):
        return  self.Board[int(rowMajor/4)][int(rowMajor%4)].getValue()

    def getBoard(self):
        return self.Board

    def setByRowMaj(self, rowMajor, val):
        self.Board[int(rowMajor/4)][int(rowMajor%4)].setValue(val)

        '''
        This adds a two by scanning the board for empty cells
        and then picking a random rowmajor value from a list
        and placing a two in the cell in that corresponds to
        that spot
        '''
    def addTwo(self):
        for i in range(16):
            if(self.getVal(i) == 0):
                randRowMaj = random.randint(0, 15)
                while (self.getVal(randRowMaj) != 0):
                    randRowMaj = random.randint(0, 15)
                self.setByRowMaj(int(randRowMaj), 2)
                return 1

    '''
    Each of these functions work in the same, they loop from 0 to 3 and call moveLine and fixMult on those lines
    moveLine and fixMult are explained in greater detail where there defined, but the gist is, they squash the board, remove any pairs, and squash again then the movement function calls addTwo to continue the game
    '''
    def moveNumbersLeft(self):
        for i in range(4):
            self.moveLine(i, self.LEFT)
            self.fixMult(i, self.LEFT)
        self.addTwo()


    def moveNumbersRight(self):
         for i in range(4):
            self.moveLine(i, self.RIGHT)
            self.fixMult(i, self.RIGHT)
         self.addTwo()

    def moveNumbersUp(self):
         for i in range(4):
            self.moveLine(i, self.UP)
            self.fixMult(i, self.UP)
         self.addTwo()

    def moveNumbersDown(self):
         for i in range(4):
            self.moveLine(i, self.DOWN)
            self.fixMult(i, self.DOWN)
         self.addTwo()




    '''
    yeah this has a high time complexity and is not extensible

    Basically, for each cell in a line along the given direction, starting at the extreme most end of that direction
    we iterate up by the difference in the rowMajor order (4, -4 for up and down columns and 1, -1 for across rows) and slot the numbers into each zero
    we find.
    line stands for the row or collumn from 0-3 we are on, so there is some math vodoo to make sure wer start at the right point in our array.

all this method does is collapse the line into adjacent numbers that touch the edge its moving too, it doesnt care about combing like numbers, which helps in the ong run becase now it wont combine numbers that get made that turn ie 4220 doesnt become 0008 it becomes 0044
    '''
    def moveLine(self, line, dire):
        if(dire == self.RIGHT):
            line = line*4 + 3
            #print line
            for rowMaj in range(line, line - 4, -1):
              #  print "rowMaj",  rowMaj
               # print
               # self.printMe()
               # print
                if(self.getVal(rowMaj) == 0):
                    for i in range(rowMaj - 1, line - 4, -1):
                        if(self.getVal(i) != 0):
                            self.setByRowMaj(rowMaj, self.getVal(i))
                            self.setByRowMaj(i,0)
                            break


        if (dire ==  self.LEFT):
            #print "runing move on line:", line
            if (line > 0):
                line = line*4
             #   print "line is now:", line
            for rowMaj in range(line, line + 4, 1):
              #  print "rowMAj:", rowMaj
                if(self.getVal(rowMaj) == 0):
                    for i in range(rowMaj + 1, line + 4, 1):
               #         print "i:", i
                        if(self.getVal(i) != 0):
                            self.setByRowMaj(rowMaj, self.getVal(i))
                            self.setByRowMaj(i,0)
                            break

        if (dire == self.UP):
            for rowMaj in range(line, 16, 4):
                if(self.getVal(rowMaj) == 0):
                    for i in range(rowMaj + 4, 16, 4):
                        if (self.getVal(i) != 0):
                            self.setByRowMaj(rowMaj, self.getVal(i))
                            self.setByRowMaj(i,0)
                            break



        if (dire == self.DOWN):
            line = line + 12
            for rowMaj in range(line, -1, -4):
                if(self.getVal(rowMaj) == 0):
                    for i in range(rowMaj - 4, -1, -4):
                        if (self.getVal(i) > 0):
                            self.setByRowMaj(rowMaj, self.getVal(i))
                            self.setByRowMaj(i,0)
                            break
    '''
    this method is the second and third step in the movement procedure, it takes a board that is full of adjacent numbers
    and multiplies the pairs by 2.
    its starts at whatever edge our moveLine function moved to and works backwards, since all it does is check for pairs, and then leave a zero where the second number was, it leaves holes on the board, so we run a final moveLine command in the same direction, for complete the movement.
    '''

    def fixMult(self, line, dire): #whish i had a switch statemnet lol
        if(dire == self.RIGHT):
            line = line*4 + 3
            for rowMaj in range(line, line - 4, -1):
                if(self.getVal(rowMaj - 1) == self.getVal(rowMaj)):
                    self.setByRowMaj(rowMaj, 2*self.getVal(rowMaj))
                    self.setByRowMaj(rowMaj - 1, 0)
            self.moveLine((line - 3)/4, self.RIGHT)

        if(dire ==self.LEFT):
            if (line > 0):
                line = line*4
            for rowMaj in range(line, line + 3, 1):
                if(self.getVal(rowMaj + 1) == self.getVal(rowMaj)):
                    self.setByRowMaj(rowMaj, 2*self.getVal(rowMaj))
                    self.setByRowMaj(rowMaj + 1, 0)
                self.moveLine(line/4, self.LEFT)
        if(dire == self.DOWN):
           line = line + 12
           for rowMaj in range(line, -1, -4):
            if(self.getVal(rowMaj - 4) == self.getVal(rowMaj)):
                self.setByRowMaj(rowMaj, 2*self.getVal(rowMaj))
                self.setByRowMaj(rowMaj - 4, 0)
            self.moveLine(line - 12, self.DOWN)
        if(dire == self.UP):
             for rowMaj in range(line, 12, 4):
                if(self.getVal(rowMaj + 4) == self.getVal(rowMaj)):
                    self.setByRowMaj(rowMaj, 2*self.getVal(rowMaj))
                    self.setByRowMaj(rowMaj + 4, 0)
                    self.moveLine(line, self.UP)

    '''
    copies the board to a temporary one and returns the temporary one
    '''
    def copyMe(self):
        c = GameBoard()
        c.clearMe()
        for i in range(16):
            c.setByRowMaj(i, self.getVal(i))
        return c

    '''
    restores the board from a copy that is passed in
    '''
    def restoreMe(self, b):
        for i in range(16):
            self.setByRowMaj(i, b.getVal(i))

    '''
    Checks the board for a win state or a loss state
    '''
    def checkWinLose(self):
        freeSpace = -1
        for i in range(16):
            if (self.getVal(i) == 0 and freeSpace == -1):
                freeSpace = 0
            if (self.getVal(i) == 2048):
                return 1
        for i in range(15):
            if(i < 12):
                if (self.getVal(i) == self.getVal(i + 1) or self.getVal(i) == self.getVal(i + 4)):
                    return 0
            elif(i >= 12):
                if (self.getVal(i) == self.getVal(i + 1)):
                    return 0
        return freeSpace







    class Cell:
        def __init__(self, val, rowMajor): #important note: rowMajor order simplifies loops
            self._value = val
            self._col = rowMajor%4 #always True
            self._row = rowMajor/4
        def setValue(self, val):
            self._value = val
        def getValue(self):
            return self._value
        def getRow(self):
            return self._row
        def getCol(self):
            return self._col
