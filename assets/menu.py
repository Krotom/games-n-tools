import numGame
import wordGame
import rpsGame
import diceGame
import os

numGameIndev = 0
wordGameIndev = 0
rpsGameIndev = 0
diceGameIndev = 0


menu = """Select the game you want to play:

            1- Number Guessing Game
            2- Word Guessing Game
            3- Rock / Paper / Scissors Game
            4- Dice Game
            q- Quit
            """


def mainloop():
    while True:
        os.system("cls")
        print(menu)
        c = input("Select 1/2/3/4/q: ")
        if c == "1":
            if numGameIndev:
                print(numGame.placeholder())
            else:
                numGame.main()

        elif c == "2":
            if wordGameIndev:
                print(wordGame.placeholder())
            else:
                wordGame.main()

        elif c == "3":
            if rpsGameIndev:
                print(rpsGame.placeholder())
            else:
                rpsGame.main()

        elif c == "4":
            if diceGameIndev:
                print(diceGame.placeholder())
            else:
                diceGame.main()

        elif c == "q":
            quit()

        else:
            print("Please enter a valid choice!")
