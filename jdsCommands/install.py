from colorama import Fore, Style
import subprocess
from sys import argv

red = Fore.RED
reset = Style.RESET_ALL

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def install_deanon():
    user_input = input("You definitely want to install JDS_anon}? (Y/n): ")
    if user_input == "Y":
        run_command(f"git clone https://github.com/ChasoniCK/JDS_anon")
    else:
        pass

if "Deanon" in argv:
    install_deanon()

elif "popa" in argv:
    print('popas')

else:
    print(red + "No installation program is specified" + reset)