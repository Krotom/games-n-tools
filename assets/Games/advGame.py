import time
from os import system as sys
def clear(): sys("cls")


def ph():
    return "Sorry, this game is currently indev"


class Player:
    def __init__(self):
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"You picked up {item}.")

    def use_item(self, item):
        if item in self.inventory:
            print(f"You used {item}.")
            self.inventory.remove(item)
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False


def introduction():
    clear()
    print("You find yourself in a mysterious land with multiple paths ahead.")
    time.sleep(1)
    print("Your goal is to reach the treasure at the end of the journey.")
    time.sleep(1)


def choose_path():
    print("Choose your path:")
    print("1. The Dark Forest")
    print("2. The Rocky Mountains")
    print("3. The Enchanted Caves")
    return input("Enter 1, 2, or 3: ")


def dark_forest(player):
    print("You enter the dark and eerie forest.")
    time.sleep(1)
    print("You hear strange noises around you.")
    time.sleep(1)
    print("Do you:")
    print("1. Keep walking deeper into the forest")
    print("2. Try to find another way around")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("As you walk deeper, you encounter a friendly guide.")
        time.sleep(1)
        print("The guide leads you safely to the other side.")
        return True
    else:
        print("You get lost in the dense forest and encounter a hostile creature.")
        time.sleep(1)
        print("You can use an item to distract the creature.")
        use_item_choice = input("Do you want to use an item? (yes/no): ").lower()
        if use_item_choice == "yes":
            if player.use_item("Distracting Charm"):
                print("The creature is distracted, allowing you to escape.")
                time.sleep(1)
                print("You successfully navigate the forest.")
                return True
            else:
                print("Unfortunately, you don't have the required item to distract the creature.")
                time.sleep(1)
                print("Your adventure ends here.")
                return False
        else:
            print("You choose not to use an item and are unable to escape the creature.")
            time.sleep(1)
            print("Your adventure ends here.")
            return False


def rocky_mountains(player):
    print("You climb the steep and treacherous rocky mountains.")
    time.sleep(1)
    print("It's a challenging journey, but you press on.")
    time.sleep(1)
    print("Do you:")
    print("1. Take a risky shortcut")
    print("2. Stick to the safer path")
    choice = input("Enter 1 or 2: ")
    if choice == "2":
        print("You choose the safer path and successfully navigate the mountains.")
        time.sleep(1)
        print("You reach the other side and continue your adventure.")
        return True
    else:
        print("The risky shortcut leads to a dangerous cliff.")
        time.sleep(1)
        print("You can use an item to create a makeshift bridge.")
        use_item_choice = input("Do you want to use an item? (yes/no): ").lower()
        if use_item_choice == "yes":
            if player.use_item("Makeshift Bridge"):
                print("You successfully create a bridge and cross the dangerous cliff.")
                time.sleep(1)
                print("You reach the other side and continue your adventure.")
                return True
            else:
                print("Unfortunately, you don't have the required item to create a bridge.")
                time.sleep(1)
                print("Your adventure ends here.")
                return False
        else:
            print("You choose not to use an item and are unable to cross the cliff.")
            time.sleep(1)
            print("Your adventure ends here.")
            return False


def enchanted_caves(player):
    print("You enter the mysterious and enchanting caves.")
    time.sleep(1)
    print("There are multiple paths within the caves.")
    time.sleep(1)
    print("Do you:")
    print("1. Explore the glowing crystal cavern")
    print("2. Navigate through the dark tunnels")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("The crystal cavern is beautiful, but you encounter a magical barrier.")
        time.sleep(1)
        print("You can use an item to dispel the barrier.")
        use_item_choice = input("Do you want to use an item? (yes/no): ").lower()
        if use_item_choice == "yes":
            if player.use_item("Magic Crystal"):
                print("The barrier is dispelled, and you continue exploring the cavern.")
                time.sleep(1)
                print("You find a shortcut to the treasure.")
                return True
            else:
                print("Unfortunately, you don't have the required item to dispel the barrier.")
                time.sleep(1)
                print("Your adventure ends here.")
                return False
        else:
            print("You choose not to use an item and are unable to proceed through the barrier.")
            time.sleep(1)
            print("Your adventure ends here.")
            return False
    else:
        print("Navigating through the dark tunnels is challenging.")
        time.sleep(1)
        print("You can use an item to light your way.")
        use_item_choice = input("Do you want to use an item? (yes/no): ").lower()
        if use_item_choice == "yes":
            if player.use_item("Glowing Mushroom"):
                print("The glowing mushroom lights your way, and you successfully navigate the tunnels.")
                time.sleep(1)
                print("You find a hidden passage to the treasure.")
                return True
            else:
                print("Unfortunately, you don't have the required item to light your way.")
                time.sleep(1)
                print("Your adventure ends here.")
                return False
        else:
            print("You choose not to use an item and get lost in the dark tunnels.")
            time.sleep(1)
            print("Your adventure ends here.")
            return False


def maingame():
    while True:
        global success
        player = Player()
        player.add_to_inventory("Distracting Charm")
        player.add_to_inventory("Makeshift Bridge")
        player.add_to_inventory("Magic Crystal")
        player.add_to_inventory("Glowing Mushroom")

        introduction()

        path_choice = choose_path()
        if path_choice == "1":
            success = dark_forest(player)
        elif path_choice == "2":
            success = rocky_mountains(player)
        elif path_choice == "3":
            success = enchanted_caves(player)
        else:
            print("Invalid choice. Please choose again.")

        if success:
            print("Congratulations! You reach the treasure and complete your adventure.")
            print("Rerun?")
            cs = input("+/-:")
            if cs == "-":
                break
        else:
            print("Sorry, you lost!")


def main():
    while True:
        clear()
        print("""Welcome to the adventure game!
        
        1 - Start Game
        Q - Quit""")
        c = input("1/Q:")
        if c == "1":
            maingame()
        elif c == "q" or c == "Q":
            break
        else:
            print("Unknown choice, please try again...")
