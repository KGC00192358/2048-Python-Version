#!/usr/bin/python
from GameBoard import GameBoard
b = GameBoard()
b.printMe()
#print b.checkWinLose()
while(b.checkWinLose() == 0):
 #   print b.checkWinLose()
    move = raw_input("make a move")
    print move
    if (move == "s"):
        b.moveNumbersDown()
        b.printMe()
        print
        :a
    if(move == "w"):
        b.moveNumbersUp()
        b.printMe()
        print
    if(move == "d"):
        b.moveNumbersRight()
        b.printMe()
        print
    if(move == "a"):
        b.moveNumbersLeft()
        b.printMe()
        print
