def ph():
    return 'cls'


def init(available):
    import subprocess
    from time import sleep
    import os

    print("Getting ready to run...")
    sleep(1)
    print("Checking program availability...")
    sleep(1)
    if available:
        print("Checking modules... Current dir: ", os.getcwd())
        try:
            import os.matplotlib
            import os.numpy
            import os.skfuzzy
            import os.pandas
            import os.sklearn
            import os.seaborn
            import os.scapy
            import os.optparse
            import os.tornado

        except ModuleNotFoundError:
            print("Installing modules, this will happen once...")
            subprocess.run([os.path.join(os.getcwd(), 'assets', 'Python', 'python.exe'), '-m', 'pip', 'uninstall', '-y', 'pip'])
            subprocess.run([os.path.join(os.getcwd(), 'assets', 'Python', 'python.exe'), '-m', 'ensurepip'])
            print("Updating pip...")
            subprocess.run([os.path.join(os.getcwd(), 'assets', 'Python', 'python.exe'), '-m', 'pip', 'install', '--upgrade', 'pip'])
            print("Pip update finished.")
            try:
                print("Installing missing modules...")
                subprocess.run([os.path.join(os.getcwd(), 'assets', 'Python', 'Scripts', 'pip.exe'), 'install', 'matplotlib'])
                subprocess.run([os.path.join(os.getcwd(), 'assets', 'Python', 'Scripts', 'pip.exe'), 'install', 'numpy'])
                subprocess.run([os.path.join(os.getcwd(), 'assets', 'Python', 'Scripts', 'pip.exe'), 'install', 'scikit-fuzzy'])
                subprocess.run([os.path.join(os.getcwd(), 'assets', 'Python', 'Scripts', 'pip.exe'), 'install', 'pandas'])
                subprocess.run([os.path.join(os.getcwd(), 'assets', 'Python', 'Scripts', 'pip.exe'), 'install', 'scikit-learn'])
                subprocess.run([os.path.join(os.getcwd(), 'assets', 'Python', 'Scripts', 'pip.exe'), 'install', 'seaborn'])
                subprocess.run([os.path.join(os.getcwd(), 'assets', 'Python', 'Scripts', 'pip.exe'), 'install', 'scapy'])
                subprocess.run([os.path.join(os.getcwd(), 'assets', 'Python', 'Scripts', 'pip.exe'), 'install', 'tornado'])
                print("Complete")
            except Exception as e:
                print("Error occurred during installation:", e)

        print("Check...")
        print("Redirecting...")
        sleep(2)
    else:
        print("Sorry, the program is currently non-available")
        input("Press enter to close...")
        quit()


init(1)
