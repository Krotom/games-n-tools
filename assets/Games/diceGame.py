import random as r


def placeholder():
    return "Sorry, this game is currently indev"


def main():
    cpudice1 = r.randint(1, 6)
    cpudice2 = r.randint(1, 6)
    cpudice3 = r.randint(1, 6)
    diceall = 0
    diceallcpu = cpudice1 + cpudice2 + cpudice3
    tournum = 1
    while True:
        if tournum == 4:
            print("CPU total:", diceallcpu)
            print("Your total:", diceall)
            if diceall == diceallcpu:
                print("Draw! Replay?")
                choice = input("+/-: ")
                if choice == "+":
                    main()
                else:
                    break
            elif diceall < diceallcpu:
                print("You lost! Replay?")
                choice = input("+/-: ")
                if choice == "+":
                    main()
                else:
                    break
            elif diceall > diceallcpu:
                print("You won! Replay?")
                choice = input("+/-: ")
                if choice == "+":
                    main()
                else:
                    break
        print("Welcome To The Dice Game")
        print("Tour:", tournum)
        print("""
        R- Roll dice
        Q- quit
        """)
        c = input("Enter a letter: ").lower()
        if c == "r":
            dice = r.randint(1, 6)
            diceall += dice
            print("You rolled", dice)
            if tournum == 1:
                print("CPU rolled", cpudice1)
            elif tournum == 2:
                print("CPU rolled", cpudice2)
            elif tournum == 3:
                print("CPU rolled", cpudice3)
                print("---------------")
            tournum += 1
