from GameBoard import GameBoard
'''
This is the player class that will eventually do all the learning, right now it just picks the highest board value move and picks it, ignoring ties and things. Baically, this is worthless because it always picks down or right depeneding on which one it higher, it will never go left. Currently, this can not even reach and end state, win or lose. The java one reaches a lose state but I didn't feel like porting all the placeholder logic in. The next step is to make it so that it can pick a target number for the board and then make the moves to create that number. Most likely this will initially just pick 2048, and then since it cant make it it moves down to 1024 until it finds a number it can make, or in the case of no combinations just makes a move.


The final goal is to have a file with weights representing  each of the numbers, as well as moves when there is no combination possible, the the program will pick move lists based on those weights;

'''
class Player:
    def __init__(self, b):
        self.B = b
        self.DOWN = 0
        self.RIGHT = 1
        self.UP = 2
        self.LEFT =3
        self.log = open("gameLog.log", "w")
        self.log.write("starting game on board:")
        self.log.write(self.B.toString())
        self.log.write("\n")
        print self.B.toString()


    def play(self):
        maxVal = 0
        maxMove = -1
        for i in range(4):
            if (self.getExpVal(i) > maxVal ):
                maxVal = self.getExpVal(i)
                maxMove = i
        if (maxMove == self.DOWN):
            print "DOWN"
            self.log.write("moving down")
            self.B.moveNumbersDown()
            self.log.write(self.B.toString())
        if (maxMove == self.RIGHT):
            print "RIGHT"
            self.log.write("moving Right")
            self.B.moveNumbersRight()
            self.log.write(self.B.toString())
        if (maxMove == self.UP):
            print "Up"
            self.log.write("moving Up")
            self.B.moveNumbersUp()
            self.log.write(self.B.toString())
        if (maxMove == self.LEFT):
            print "left"
            self.log.write("moving Left")
            self.B.moveNumbersLeft()
            self.log.write(self.B.toString())


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
        c = self.B.copyMe()
        val = 0
        if(dire == self.DOWN):
            self.B.moveNumbersDown()
            val = self.getBoardVal()
            self.B.restoreMe(c)
            return val
        if(dire == self.RIGHT):
            self.B.moveNumbersRight()
            val = self.getBoardVal()
            self.B.restoreMe(c)
            return val
        if(dire == self.UP):
            self.B.moveNumbersUp()
            val = self.getBoardVal()
            self.B.restoreMe(c)
            return val
        if(dire == self.LEFT):
            self.B.moveNumbersLeft()
            val = self.getBoardVal()
            self.B.restoreMe(c)
            return val
        return val

    def writeLog(self, message):
        self.log.write(message)

    '''
    This is where the  move list function should go, i have tried A* and dikstra's algorithm but they do not really get the job done, I need some way to pathfind on a moving field and reach a given end number, if it is reachable.
    '''
    def pickMoveList(self, targNum):
        placeHold = 0


