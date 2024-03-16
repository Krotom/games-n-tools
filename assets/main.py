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
        cc = input("Enter dev password: ")
        if cc == devpass:
            print("Welcome back developer!")
        else:
            print("Wrong password!")
            input("Press enter to continue")
            quit()


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
    check_dev(dev)
    print(menu)
    c = input("Choice: ")
    if c == "1":
        if gamesIndev:
            print(menuGames.placeholder())
            input("Press enter to continue")
            sys("cls")
        else:
            menuGames.mainloop()
    elif c == "2":
        if toolsIndev:
            print(menuTools.placeholder())
            input("Press enter to continue")
            sys("cls")
        else:
            menuTools.mainloop()
    elif c.lower() == "q":
        quit()
    else:
        sys("cls")
        print("Unknown Choice. Please retry!")
