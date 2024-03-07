ls = 299792458


def calculate(speed_of_light_in_vacuum, speed_of_light_in_material):
    refractive_index = speed_of_light_in_vacuum / speed_of_light_in_material
    return refractive_index


def ph():
    return "Sorry, this tool is currently indev"


def main():
    while True:
        speed_of_light_in_material = float(input("Enter the speed of light in the material (m/s): "))

        refractive_index = calculate(ls, speed_of_light_in_material)

        print(f"Refractive Index: {refractive_index}")
        print("Rerun?")
        c = input("+/-:")
        if c == "-":
            break
