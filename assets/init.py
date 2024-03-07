from time import sleep
from os import system as sys


def ph():
    return 'cls'


def init(available):
    print("Getting ready to run...")
    sleep(1)
    print("Checking program availability...")
    sleep(1)
    if available:
        print("Checking modules...")
        try:
            import matplotlib
            import numpy
            import skfuzzy
            import pandas
            import sklearn
            import seaborn
            import scapy

        except ModuleNotFoundError:
            print("Installing modules, this will happen once...")
            sys('echo %cd% && %cd%\\assets\\Python\\python.exe -m pip install --upgrade pip && %cd%\\assets\\Python\\Scripts\\pip.exe install matplotlib numpy scikit-fuzzy pandas scikit-learn seaborn scapy')
            print("Complete")

        print("Check...")
        print("Redirecting...")
        sleep(2)
    else:
        print("Sorry, the program is currently non-available")
        input("Press enter to close...")
        quit()


init(1)
