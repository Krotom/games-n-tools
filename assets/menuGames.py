from Games import diceGame, numGame, rpsGame, wordGame, xoxGame, advGame
import os
from os import system as sys


def placeholder():
    return "Sorry, games section is currently indev"


numGameIndev = 0
wordGameIndev = 0
rpsGameIndev = 0
diceGameIndev = 0
xoxGameIndev = 0
advGameIndev = 0

menu = """Select the game you want to play:

            1- Number Guessing Game
            2- Word Guessing Game
            3- Rock / Paper / Scissors Game
            4- Dice Game
            5- XOX Game
            6- Adventure Game
            q- Quit
            """


def mainloop(devm):
    while True:
        os.system("cls")
        if devm:
            print("Welcome back developer!")
        else:
            print("Welcome back!")
        print(menu)
        c = input("Select 1/2/3/4/5/6/q: ")
        if c == "1":
            if numGameIndev:
                print(numGame.placeholder())
                input("Press enter to continue")
                sys("cls")
            else:
                numGame.main()

        elif c == "2":
            if wordGameIndev:
                print(wordGame.placeholder())
                input("Press enter to continue")
                sys("cls")
            else:
                wordGame.main()

        elif c == "3":
            if rpsGameIndev:
                print(rpsGame.placeholder())
                input("Press enter to continue")
                sys("cls")
            else:
                rpsGame.main()

        elif c == "4":
            if diceGameIndev:
                print(diceGame.placeholder())
                input("Press enter to continue")
                sys("cls")
            else:
                diceGame.main()

        elif c == "5":
            if xoxGameIndev:
                print(xoxGame.ph())
                input("Press enter to continue")
                sys("cls")
            else:
                xoxGame.main()

        elif c == "6":
            if advGameIndev:
                print(advGame.ph())
                input("Press enter to continue")
                sys("cls")
            else:
                advGame.main()

        elif c == "q":
            break

        else:
            print("Please enter a valid choice!")
