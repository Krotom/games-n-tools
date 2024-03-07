import random as r


def placeholder():
    return "Sorry, this game is currently indev!"


def main():
    gm = 0
    maxguess = 15
    num = r.randint(1, 1000)
    while True:
        print("Try to guess the number(Its between 1 and 1000)")
        guess = int(input("Your guess:"))
        if gm == maxguess:
            print("You lost! Replay?")
            c = input("+/-:")
            if c == "+":
                main()
            elif c == "-":
                break
        else:
            if guess == num:
                print("Congrats! You won with only ", gm+1, " guesses! Replay?")
                c = input("+/-:")
                if c == "+":
                    main()
                elif c == "-":
                    break

            elif guess < num:
                gm += 1
                print("Try again with a bigger number, ", maxguess-gm, " guesses remaining.")

            elif guess > num:
                gm += 1
                print("Try again with a smaller number, ", maxguess-gm, "guesses remaining.")
