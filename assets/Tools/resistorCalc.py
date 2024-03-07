def placeholder():
    return "Sorry, this tool is currently indev!"


def resistor_color_code_calculator():
    color_codes = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "gray": 8,
        "white": 9
    }
    band1 = input("Enter the color of the first band: ").lower()
    band2 = input("Enter the color of the second band: ").lower()
    band3 = input("Enter the color of the third band: ").lower()
    resistance = (color_codes[band1] * 10 + color_codes[band2]) * (10 ** color_codes[band3])
    print("The resistance value is ", resistance, "ohms.")
