import random as r
from os import system, getcwd


def placeholder():
    return "Sorry, this game is currently indev!"


def getfile(file):
    wordlist = []
    with open(file, encoding="utf-8") as file_in:
        for line in file_in:
            line = line[:-1].lower()
            wordlist.append(line)
    return wordlist


def displayword(word, guessed_letters):
    displayed_word = ''.join(letter if letter in guessed_letters else '_' for letter in word)
    return displayed_word


def main():
    print("Running in: ", getcwd())
    words = getfile("assets\\words_alpha.txt")
    word = r.choice(words)
    guessed_letters = []
    max_attempts = 10

    global currentdisplay

    while max_attempts > 0:
        print("Welcome to the Word Guessing Game!")
        print("Try to guess the name of the programming language.")
        print(displayword(word, guessed_letters))
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or guess == "-" or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            max_attempts -= 1
            print("Incorrect! You have ", max_attempts, " attempts left.")
        else:
            print("Correct!")

        currentdisplay = displayword(word, guessed_letters)
        print(currentdisplay)

        if "_" not in currentdisplay:
            system("cls")
            print("Congratulations! You guessed the word!")
            print("Play again?")
            choice = input("+/-: ")
            if choice == "+":
                main()
            else:
                break

    if "_" in currentdisplay:
        system("cls")
        print("Sorry, you ran out of attempts. The word was: ", word)
        print("Play again?")
        choice = input("+/-: ")
        if choice == "+":
            main()
