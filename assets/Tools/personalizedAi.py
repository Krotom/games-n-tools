import matplotlib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import CategoricalNB
from os import system as sys
from time import sleep as sl
plt.switch_backend("WebAgg")


def anim(text, t):
    o = 0
    while o < t:
        print("\r" + text + "-", end="")
        sl(0.07)
        print("\r" + text + "\\", end="")
        sl(0.07)
        print("\r" + text + "|", end="")
        sl(0.07)
        print("\r" + text + "/", end="")
        sl(0.07)
        o += 1
    print("\r" + text + "OK")


enc = LabelEncoder()
helpm = """
-------How To Use-------

1 - Enter the name of the dataset without '.csv' part.
The dataset needs to be in the assets directory and must be '.csv' file.

2 - Enter the number of columns in your csv file.
If you enter this wrong, the program is gonna crash.

3 - Enter name of the given column in the csv file.
Don't Forget: It must be the exact same with the csv file! This is important!

4 - Choose your AI model.

5 - Enter test size percentage.
It works like this:
If you enter 30, %70 of the dataset will be used to train the AI and the left %30 will be used to test the AI

6 - Enter random state.
Just enter a number between 1 and 10000.

7 - Let the code do its work!

---- Example Use ----

1 - Dataset Name: ed(included in assets)
2 - Number of columns: 4
3 - 1. Column name: country_or_area
    2. Column name: year
    3. Column name: category
    4. Column name: value
4 - AI Model: 1(DecisionTreeClassifier)
5 - Test percentage: 50
6 - Random state: 19
7 - Done!"""
mainm = """
-------Main Menu-------

R - Run the code
? - How to use
Q - Quit"""
aim = """
Choose Your AI Model

1 - DecisionTreeClassifier(Recommended, Default)
2 - KNeighborsClassifier
3 - RandomForestClassifier
4 - CategoricalNB"""


def ph():
    return "Sorry, this tool is currently indev"


def pinput(x, y):
    print(x)
    z = input(y)
    return z


def maincode():
    sys("cls")
    ting = "mt"
    try:
        dataset = input("Enter dataset name: ")
        try:
            pd.read_csv("assets\\" + dataset + ".csv", encoding='unicode_escape')
        except FileNotFoundError:
            print("Sorry this file does not exist! Please make sure your .csv file is in the assets folder!")
            anim("Directing you back, make sure to read the error...", 20)

        data = pd.read_csv("assets\\" + dataset + ".csv", encoding='unicode_escape')
        dt = data.copy()
        colnum = int(input("Enter number of columns in the dataset: "))
        for i in range(colnum):
            name = input("Enter the name of the {}. column: ".format(i + 1))
            dt[name] = enc.fit_transform(dt[name])
            if i == 0:
                ting = name
        for column in dt.columns:
            if dt[column].dtype == 'O':
                dt[column] = pd.to_numeric(dt[column], errors='coerce')
                dt = dt.dropna(subset=[column])
        msel = pinput(aim, "Select your AI model: ")
        if msel == "2":
            model = KNeighborsClassifier()
        elif msel == "3":
            model = RandomForestClassifier()
        elif msel == "4":
            model = CategoricalNB()
        else:
            model = DecisionTreeClassifier()
        testp = input("Enter test percantage: ")
        try:
            p = int(testp)
            print("Selected test percantage:", p)
        except TypeError:
            print("Please enter a number!")
            anim("Directing you back...", 20)
            maincode()
        testp = int(testp)
        testp /= 100
        rands = input("Enter random state: ")
        try:
            h = int(rands)
            print("Selected random state:", h)
        except TypeError:
            print("Please enter a number!")
            anim("Directing you back...", 20)
            maincode()
        rands = int(rands)
        sys("cls")
        print("Setting up things...")
        anim("Please wait a minute...", 10)
        anim("Checking dataset size...", 10)
        if len(dt) <= 1 or (testp * len(dt)) >= len(dt):
            print("Not enough data for train and test split. Please choose a smaller test percentage.")
            anim("Directing you back...", 20)
            maincode()
        anim("Splitting dataset...", 15)
        x_train, x_test, y_train, y_test = train_test_split(
            dt.drop([ting], axis=1),
            dt[ting],
            test_size=testp,
            random_state=rands)
        anim("Training model...", 10)
        model.fit(x_train, y_train)
        anim("Testing model...", 10)
        pred = model.predict(x_test)
        anim("Calculting things...", 15)
        conf = confusion_matrix(y_test, pred)
        acc = accuracy_score(y_test, pred)
        anim("Finalizing...", 30)
        sl(1)
        sys("cls")
        print("Model accuracy: ", acc)
        print("Confusion Matrix: ", conf)
        plt.figure(figsize=(8, 6))
        sns.heatmap(conf, annot=True, fmt="d")
        plt.xlabel('Predicted Label')
        plt.ylabel('True Label')
        plt.title('Confusion Matrix')
        plt.show()
    except Exception as en:
        print("Sorry, an error happened!")
        a = input("Press enter to continue...")
        if a == "1235789":
            print("Hello dev!")
            print("Here is the error code: ", en)
            input("Press enter to continue...")


def main():
    sys("cls")
    hl = 0
    while True:
        c = pinput(mainm, "Your choice: ")
        if c == "R" or c == "r":
            if hl:
                maincode()
            else:
                sys("cls")
                print("Please open the 'How To Use' menu at least once before running")
        elif c == "?":
            sys("cls")
            print(helpm)
            hl = 1
        elif c == "q" or c == "Q":
            break
        else:
            print("Unknown choice, try again!")
