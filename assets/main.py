import init
import menuGames
import menuTools
import optparse
from os import system as sys


parse = optparse.OptionParser()
parse.add_option("-d", action="store_true", dest="dev_mode", default=False)
opts = parse.parse_args()[0]
dev = opts.dev_mode


def check_dev(devm):
    devpass = "DeveloperPassForMe1235789"
    if devm:
        cc = input("Enter Dev Password: ")
        if cc == devpass:
            print("Welcome back developer!")
            return True
        else:
            print("Wrong password!")
            return False


menu = """
Hello, Welcome To Games n' Tools
Recode as you like(if you know what you're doing)!
---Open Source Games and Tools---

****MENU*****

1-Games
2-Tools
q-Quit
"""
gamesIndev = 0
toolsIndev = 0


while True:
    sys(init.ph())
    print(menu)
    c = input("Choice: ")
    if c == "1":
        if gamesIndev:
            print(menuGames.placeholder())
            input("Press enter to continue")
            sys("cls")
        else:
            menuGames.mainloop(check_dev(dev))
    elif c == "2":
        if toolsIndev:
            print(menuTools.placeholder())
            input("Press enter to continue")
            sys("cls")
        else:
            menuTools.mainloop(check_dev(dev))
    elif c.lower() == "q":
        quit()
    else:
        sys("cls")
        print("Unknown Choice. Please retry!")
