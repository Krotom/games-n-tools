import os
from os import system as sys
from Tools import resistorCalc, brakeCalc, passwordGen, noteSys, personalizedAi, netScanner, refIndexCalc

toolResistorIndev = 0
toolBrakeCalcIndev = 0
toolPasswordGenIndev = 0
toolNoteSysIndev = 0
toolAIIndev = 0
toolnetScannerIndev = 1
toolRefIndexCalcIndev = 0


def placeholder():
    return "Sorry, tools section is currently indev"


menu = """Select the tool you want to use

1- Resistor Ohm Calculator
2- Brakes Pressure Calculator
3- Password Generator
4- Note System
5- Personalizable AI
6- Net Scanner
7- Refractive Index Calculator
q- Quit"""


def mainloop(devm):
    while True:
        os.system("cls")
        if devm:
            print("Welcome back developer!")
        print(menu)
        c = input("Select 1/2/3/4/5/6/7/q: ")
        if c == "1":
            if toolResistorIndev:
                print(resistorCalc.placeholder())
                input("Press enter to continue")
                sys("cls")
            else:
                resistorCalc.resistor_color_code_calculator()
        elif c == "2":
            if toolBrakeCalcIndev:
                print(brakeCalc.placeholder())
                input("Press enter to continue")
                sys("cls")
            else:
                brakeCalc.main()
        elif c == "3":
            if toolPasswordGenIndev:
                print(passwordGen.placeholder())
                input("Press enter to continue")
                sys("cls")
            else:
                passwordGen.main()
        elif c == "4":
            if toolNoteSysIndev:
                print(noteSys.placeholder())
                input("Press enter to continue")
                sys("cls")
            else:
                noteSys.main()
        elif c == "5":
            if toolAIIndev:
                print(personalizedAi.ph())
                input("Press enter to continue")
                sys("cls")
            else:
                personalizedAi.main()
        elif c == "6":
            if toolnetScannerIndev:
                print(netScanner.ph())
                input("Press enter to continue")
                sys("cls")
            else:
                netScanner.main()
        elif c == "7":
            if toolRefIndexCalcIndev:
                print(refIndexCalc.ph())
                input("Press enter to continue")
                sys("cls")
        elif c.lower() == "q":
            break
        else:
            print("Unknown choice. Please retry!")
