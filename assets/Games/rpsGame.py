import random as r


def placeholder():
    return "Sorry, this game is currently indev"


def main():
    actions = ["rock", "paper", "scissors"]
    cpuchoice = r.choice(actions)
    print("""!!!Welcome to Rock, Paper, Scissors!!!
            Please choose one of:
            Rock / Paper / Scissors
            (No typo allowed)
            CPU made his choice...""")
    while True:
        playerchoice = input("Your choice(Please don't enter a number): ").lower()

        print("CPU has chose", cpuchoice)
        print("You chose", playerchoice)

        if cpuchoice == playerchoice:
            print("Draw! Replay?")
            choice = input("+/-: ")
            if choice == "+":
                main()
            else:
                break
        elif cpuchoice == "rock" and playerchoice == "paper":
            print("You won! Replay?")
            choice = input("+/-: ")
            if choice == "+":
                main()
            else:
                break
        elif cpuchoice == "paper" and playerchoice == "scissors":
            print("You won! Replay?")
            choice = input("+/-: ")
            if choice == "+":
                main()
            else:
                break
        elif cpuchoice == "scissors" and playerchoice == "rock":
            print("You won! Replay?")
            choice = input("+/-: ")
            if choice == "+":
                main()
            else:
                break
        elif cpuchoice == "rock" and playerchoice == "scissors":
            print("You lost! Replay?")
            choice = input("+/-: ")
            if choice == "+":
                main()
            else:
                break
        elif cpuchoice == "paper" and playerchoice == "rock":
            print("You lost! Replay?")
            choice = input("+/-: ")
            if choice == "+":
                main()
            else:
                break
        elif cpuchoice == "scissors" and playerchoice == "paper":
            print("You lost! Replay?")
            choice = input("+/-: ")
            if choice == "+":
                main()
            else:
                break
        else:
            print("Unknown choice please try again!")
