import os
from time import sleep as sl

inp = input("SKIP PIP INSTALL SEQUENCE(Not Recommended For First Run) y/N: ")
if inp.lower() == "y":
    print("PIP SEQUENCE SKIPPED - NORMAL OPERATION CONTINUE")
    sl(0.2)
else:
    os.system("%cd%\\Python\\python.exe -m pip install --upgrade pip bcrypt pandas pyfiglet colorama requests")
import pyfiglet
import bcrypt
import pandas as pd
import random
import colorama
from colorama import Fore, Back
from chronicle_engine import chronicle_log, clean_slate
import requests
import zipfile

colorama.init(autoreset=True)


kaggle_addr = "https://storage.googleapis.com/kaggle-data-sets/1993529/3293885/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240511%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240511T192510Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=6f77cb8caf2b75d6d6f98ff95d29a13b63627379c0dd7fd1670f16c60b2b819f5d44bada416a10316fc695b4b4ef045d31737174b0dd77d1fafeb5ddbad4196e533b3afefc855861d684dc4a9ab81d462180fa577c813defb90a1a6953f37b5592fc90d524f2b024fc131d19698072ca1c952c75050e981db6dc7c4c5d26dc7016804b041916aac9ca0ae7e8342c5e24050289bdc3541b2f162119557ad93c5356b246920dbedb9b95c7a1d35dc59b423d036e344e586146cb4f0153cc84c3c2c34a33bee3a998613509687811f847de572779f7c81a2cbe9d126b510e13cef45c9a1f06a72d1a180a951aa4f17d4c5fb10c25e62155ef402c7763a7479372a8"


def progress(percent=0, width=30):
    symbol = width * percent // 100
    blanks = width - symbol
    print('\r[ ', Fore.GREEN + symbol * "█", blanks * ' ', ' ]',
          f' {percent:.0f}%', sep='', end='', flush=True)


for i in range(101):
    progress(i)
    sl(0.0001)


available_cmds = f"""Current available commands:
{Fore.CYAN}help{Fore.GREEN} - Displays this list
{Fore.CYAN}resetcred{Fore.GREEN} - Removes current username and password from database and exits
{Fore.CYAN}lockdown{Fore.GREEN} - Initiates the emergency lockout system on the current frontend
{Fore.CYAN}access <SCP-No.>{Fore.GREEN} - Access mentioned SCP. If entered 'random', a rondom file will be shown
{Fore.CYAN}logout{Fore.GREEN} - Logs out from current session, does not close the program
{Fore.CYAN}clean{Fore.GREEN} - Removes current activity logs
{Fore.CYAN}inco{Fore.GREEN} - Enables/Disables INCOGNITO mode
{Fore.CYAN}cls/clear{Fore.GREEN} - Clear terminal
{Fore.CYAN}quit/exit{Fore.GREEN} - Quits the terminal
"""

figlet = pyfiglet.figlet_format("SCP", font="doh") + Fore.LIGHTCYAN_EX + pyfiglet.figlet_format("Foundation", font="standard")


def check_dataset():
    if not os.path.exists("scp6999.csv"):
        with open("archive.zip", 'wb') as file:
            resp = requests.get(kaggle_addr)
            file.write(resp.content)
        with zipfile.ZipFile('archive.zip') as zipp:
            zipp.extractall()
        os.remove("archive.zip")


check_dataset()
dt = pd.read_csv("scp6999.csv")
data = dt.copy()


def anim(text, tx, t):
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
    print("\r" + text + tx)


def access(no):
    if no.startswith("SCP-") or no.startswith("scp-"):
        scp = no.upper()
    else:
        scp = "SCP-" + str(no)
    anim("Accessing Database...", f"{Fore.GREEN}ACCESS GRANTED{Fore.RESET}", 10)
    anim("Decoding file...", "COMPLETE", 10)
    anim("Loading file...", "LOADED", 20)
    try:
        print(f"\nSCP NO.: {data[data['code'] == scp]['code'].iloc[0]}")
        print(f"SCP Title: {data[data['code'] == scp]['title'].iloc[0]}")
        print(f"Current file state: {data[data['code'] == scp]['state'].iloc[0]}")
        print(f"\n\n{data[data['code'] == scp]['text'].iloc[0]}")
    except Exception as ex:
        print("\rError while trying to load file... Probably the SCP you are searching for does not exist")
        print(f"Error code: {ex}")


def get_command(usr):
    return input(f"USER:{usr}::>").split()


def is_first_launch():
    return not os.path.exists("passwd.txt")


def restricted():
    print("")
    print("                                    ", Back.RED + " << ACCESS RESTRICTED >> ")
    print(Fore.RED + "--------------------------------------------------------------------------".center(100))
    print(Fore.RED + "THIS FILE HAS BEEN CLASSIFIED".center(100))
    print(Fore.RED + "<< TOP SECRET >>".center(100))
    print(Fore.RED + "BY ORDER OF THE ADMINISTRATOR".center(100))
    print("")
    print(Fore.RED + "ACCESS TO SCP-001 IS RESCRICTED TO O5 COUNCIL MEMBERS ONLY.".center(100))
    print(Fore.RED + "--------------------------------------------------------------------------".center(100))
    print("")

    print(Fore.YELLOW + "GENERAL NOTICE 001-ALPHA:".center(100))
    print(Fore.YELLOW + "IN ORDER TO PREVENT KNOWLEDGE OF SCP-001 FROM".center(100))
    print(Fore.YELLOW + "BEING LEAKED, SEVERAL/NO FALSE SCP-001 FILES".center(100))
    print(Fore.YELLOW + "HAVE BEEN CREATED ALONGSIDE THE TRUE FILE/FILES.".center(100))
    print(Fore.YELLOW + "ALL FILES CONCERNING THE NATURE OF SCP-001, INCLUDING".center(100))
    print(Fore.YELLOW + "THE DECOY/DECOYS, ARE PROTECTED".center(100))
    print(Fore.YELLOW + "BY A MEMETIC KILL AGENT DESIGNED TO IMMEDIATELY".center(100))
    print(Fore.YELLOW + "CAUSE CARDIAC ARREST IN ANY NONAUTHORIZED PERSONNEL".center(100))
    print(Fore.YELLOW + "ATTEMPTING TO ACCESS THE FILE. REVEALING THE TRUE NATURE/NATURES OF SCP-001".center(100))
    print(Fore.YELLOW + "TO THE GENERAL PUBLIC IS CAUSE FOR EXECUTION.".center(100))
    print(Fore.YELLOW + "EXCEPT AS REQUIRED UNDER ████-███-██████.".center(100))
    print("")

    print(Fore.RED + "--------------------------------------------------------------------------".center(100))
    print(Fore.RED + "ANY NON-AUTHORIZED PERSONNEL ACCESSING THESE DOCUMENTS WILL BE IMMEDIATELY".center(100))
    print(Fore.RED + "TERMINATED THROUGH THE BERRYMAN-LANGFORD MEMETIC KILL AGENT.".center(100))
    print(Fore.RED + "--------------------------------------------------------------------------".center(100))
    print("")

    sl(1)
    print("")


def lock_protocol():
    os.system('cls')
    print("\t" + figlet)
    print(Fore.RED + '''
                ▀▀█▀▀ █▀▀▀  █▀▀█  █▀▄▀█ ▀█▀  █▄  █  █▀▀█  █       █     █▀▀▀█  █▀▀█  █ ▄▀  █▀▀▀  █▀▀▄ 
                  █   █▀▀▀  █▄▄▀  █ █ █  █   █ █ █  █▄▄█  █       █     █   █  █     █▀▄   █▀▀▀  █  █ 
                  █   █▄▄▄  █  █  █   █ ▄█▄  █  ▀█  █  █  █▄▄█    █▄▄█  █▄▄▄█  █▄▄█  █  █  █▄▄▄  █▄▄▀''')
    print("")
    print("                                ", Back.RED + " << EMERGENCY LOCKOUT PROTOCOL INITIATED >> ")

    print("")
    while True:
        usr, pas, o5 = get_o5_credentials()
        if check_o5_credentials(usr, pas, o5):
            os.remove("lockout")
            print("")
            print(Fore.YELLOW + "\tLOCKOUT PROTOCOL OVERRIDDEN")
            for fi in range(101):
                progress(fi)
                sl(0.001)
            mainlogonloop(usr, pas, True)
            break

        else:
            print("")
            print("      ", Fore.BLACK + Back.RED + " INVALID LOCKOUT BACKUP CODE ")
            print(Fore.RED + "       << TERMINAL LOCKED >>")
            sl(7300)


def get_new_creds():
    username = input("Enter new username: ")
    while True:
        password = input("Enter new password: ")
        conf_password = input("Confirm password: ")
        if password == conf_password:
            final_pass = password
            break
        else:
            print("Passwords aren't the same, try again!")
    while True:
        o5 = input("Enter new LockoutBackupCode: ")
        o5_conf = input("Confirm LockoutBackupCode: ")
        if o5 == o5_conf:
            final_o5 = o5
            break
        else:
            print("Codes aren't the same, try again!")
    return username, final_pass, final_o5


def get_credentials():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        return username, password


def get_o5_credentials():
    while True:
        usr = input(Fore.RED + "Enter Username: " + Fore.RESET)
        pas = input(Fore.RED + "Enter Password: " + Fore.RESET)
        o5 = input(Fore.RED + "Enter LBC: " + Fore.RESET)
        return usr, pas, o5


def save_credentials(username, password, o5):
    with open("passwd.txt", "wb") as file:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        hashed_username = bcrypt.hashpw(username.encode(), salt)
        hashed_o5 = bcrypt.hashpw(o5.encode(), salt)
        file.write(hashed_username + b'\n' + hashed_password + b'\n' + hashed_o5)


def check_credentials(username, password):
    with open("passwd.txt", "rb") as file:
        stored_username = file.readline().strip()
        stored_password = file.readline().strip()
        if bcrypt.checkpw(username.encode(), stored_username) and bcrypt.checkpw(password.encode(), stored_password):
            return True
        else:
            return False


def check_o5_credentials(user, pasw, o5pass):
    with (open("passwd.txt", "rb") as file):
        usr = file.readline().strip()
        pas = file.readline().strip()
        stored_o5 = file.readline()
        if bcrypt.checkpw(user.encode(), usr) and bcrypt.checkpw(pasw.encode(), pas) and bcrypt.checkpw(o5pass.encode(), stored_o5):
            return True
        else:
            return False


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(figlet)
        print(pyfiglet.figlet_format("Welcome Back", font="digital"))
        if not os.path.exists("lockout"):
            if is_first_launch():
                print("First launch detected!")
                print("Please enter new credentials!")
                username, password, o5 = get_new_creds()
                save_credentials(username, password, o5)
                print("Credentials saved successfully.")
                chronicle_log("<<NEW SYSTEM CREDS SET>>", False)
                mainlogonloop(username, password, False)
            else:
                attempts = 3
                while attempts > 0:
                    username, password = get_credentials()
                    if check_credentials(username, password):
                        mainlogonloop(username, password, False)
                        break
                    else:
                        attempts -= 1
                        print("Invalid credentials. Please try again. Attempts left:", attempts)
                        chronicle_log("<<INVALID CREDS ENTERED>>", False)
                else:
                    with open("lockout", 'w'):
                        pass
                    print("Lockout initiated")
                    chronicle_log("<<TERMINAL AUTOMATIC LOCKOUT INITIATED>>", False)
        else:
            lock_protocol()


def mainlogonloop(username, password, fromlc):
    global incognito
    incognito = False
    os.system('cls' if os.name == 'nt' else 'clear')
    chronicle_log("<<LOGIN CONFIRMED>>", incognito)
    print(figlet)
    if fromlc:
        print(Fore.BLACK + Back.GREEN + "\t~~~~MANUAL LOCKOUT OVERRIDE CONFIRMED~~~~")
        chronicle_log("<<LOCKOUT OVERRIDDEN>>", incognito)
    print(pyfiglet.figlet_format(f"Welcome Back {username}", font="contessa"))
    print("Login successful!")
    print(f"Type help to see all available commands")
    while True:
        cmmd = get_command(username)
        if not cmmd:
            continue
        cmd = cmmd[0].lower()
        chronicle_log(f"USER:{username} Ran command: {''.join(cn for cn in cmmd)}", incognito)
        if cmd == "quit" or cmd == "exit":
            chronicle_log("<<TERMINAL EXIT>>", incognito)
            quit("Exiting...")
        elif cmd == "logout":
            break
        elif cmd == "clean":
            clean_slate()
            incognito = True
            print(f"{Back.GREEN}Activity logs deleted succesfully{Back.RESET}")
        elif cmd == "resetcred":
            usure = input("""Are you sure that you want to reset your credentials and exit?
            You will be prompted to enter a new username and password afterwards, requires for the password to be entered again.
            Are you sure? Y/N: """)
            if usure.lower() == "y":
                pasw = input("Please enter your password(Enter EXIT to exit): ")
                if pasw == password:
                    os.remove("passwd.txt")
                    print("Credentials reset")
                    chronicle_log("<<LOGIN CREDS RESET>>", incognito)
                    break
                elif pasw == "EXIT":
                    print("Command terminated")
                    break
                else:
                    print("Wrong password!")
            else:
                print("Command terminated")
        elif cmd == "help":
            print(available_cmds)
        elif cmd == "inco":
            incognito = not incognito
            print(f"Current INCOGNITO state: {incognito}")
        elif cmd == "lockdown":
            rusure = input("""This will initiate an immediate lockout procedure on your current frontend!
            And it will not be able to disabled without the password!
            Are you sure? This will require your password to be entered. Y/N: """)
            if rusure.lower() == "y":
                paswd = input("Please enter your password(Enter EXIT to exit): ")
                if paswd == password:
                    with open("lockout", 'w'):
                        pass
                    print("Lockout initiated")
                    chronicle_log("<<TERMINAL MANUAL LOCKOUT INITIATED>>", False)
                    break
                elif paswd == "EXIT":
                    print("Command terminated")
                    break
                else:
                    print("Wrong password!")
            else:
                print("Command terminated")
        elif cmd == "access":
            if len(cmmd) == 1:
                print("Please use the command with an SCP No or enter 'random' to access a random SCP")
            elif len(cmmd) >= 3:
                print("This command only accepts one argument")
            elif len(cmmd) == 2:
                if cmmd[1].lower() == "random":
                    rand = random.randint(1, 6999)
                    frand = f"{rand:04d}" if rand >= 1000 else f"{rand:03d}"
                    chronicle_log(f"Random SCP -> SCP-{frand} accessed", incognito)
                    access(frand)
                elif cmmd[1] == "001" or cmmd[1].lower() == "scp-001":
                    anim("Accessing Database...", f"{Fore.RED}ACCESS DENIED{Fore.RESET}", 10)
                    chronicle_log("<<ACCESS TO SCP-001 IS RESTRICTED TO O5 COUNCIL MEMBERS>>", incognito)
                    restricted()
                else:
                    try:
                        cmmmd = int(cmmd)
                        acc = f"{cmmmd:04d}" if cmmmd >= 1000 else f"{cmmmd:03d}"
                        chronicle_log(f"SCP-{acc} accessed", incognito)
                        access(acc)
                    except TypeError:
                        chronicle_log(f"{cmmd[1]} accessed", incognito)
                        access(cmmd[1])
        elif cmd == "cls" or cmd == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            chronicle_log("<<TERMINAL CLEARED>>", incognito)
        else:
            print(f"{cmd} is not an internal or external command | Error: Command Not Found")
            chronicle_log(f"{cmd} is an unknown command", incognito)


if __name__ == '__main__':
    main()
