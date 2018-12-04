#!/usr/bin/env python3 
from GameBoard import GameBoard
from Player import Player
b = GameBoard()


select = input("Hello, press 1 to enter manual mode, 2 to enter learning mode")
if (select == "1"):
    b.printMe()
    #print b.checkWinLose()
    while(b.checkWinLose() == 0):
    #   print b.checkWinLose()
        move = input("make a move")
        print(move)
        if (move == "s"):
            b.moveNumbersDown()
            b.printMe()
            print()
        if(move == "w"):
            b.moveNumbersUp()
            b.printMe()
            print()
        if(move == "d"):
            b.moveNumbersRight()
            b.printMe()
            print()
        if(move == "a"):
            b.moveNumbersLeft()
            b.printMe()
            print()
    if(b.checkWinLose() == 1):
        print("win")
    if(b.checkWinLose() == -1):
        print("lose")
if(select == "2"):
    p = Player(b)
    while(b.checkWinLose() == 0):
        p.play()

    if(b.checkWinLose() == 1):
        player.writeLog("win")
    if(b.checkWinLose() == -1):
        player.writeLog("lose")

