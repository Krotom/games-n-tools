import random
import string


def placeholder():
    return "Sorry, this tool is currently indev!"


def generate_password(length, include_uppercase=True, include_digits=True, include_symbols=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    while True:
        leng = int(input("Enter the length of the password: "))
        inc_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        inc_digits = input("Include digits? (y/n): ").lower() == 'y'
        inc_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        generated_password = generate_password(leng, inc_uppercase, inc_digits, inc_symbols)

        print("Generated Password: ", generated_password)

        print("Rerun?")
        c = input("+/-:")
        if c == "-":
            break
