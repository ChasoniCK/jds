import os, getpass
import json
import subprocess
from colorama import init, Fore, Style
import mainFiles.configs as configs

init()

magneta = Fore.MAGENTA 
red = Fore.RED
green = Fore.GREEN
black = Fore.BLACK
reset = Style.RESET_ALL


def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def dir(arguments):
    run_command(f"dir {arguments}")

def mkdir(arguments):
    run_command(f"mkdir {arguments}")

def rmdir(arguments):
    run_command(f"rmdir {arguments}")

def cd(arguments):
    os.chdir(arguments)

def cls(arguments):
    os.system('cls' if os.name == 'nt' else 'clear')

def execute_python(arguments):
    run_command(f"python {arguments}")

def execute_custom_command(command_name, arguments, show_all_prefixes=False):
    command_path = os.path.join("jdsCommands", f"{command_name}.py")
    if os.path.exists(command_path):
        if show_all_prefixes:
            with open(command_path, 'r') as file:
                script_content = file.read()
                prefixes_start = script_content.find('prefixes = [')
                if prefixes_start != -1:
                    prefixes_end = script_content.find(']', prefixes_start)
                    prefixes_list = script_content[prefixes_start + len('prefixes = ['):prefixes_end]
                    prefixes = [p.strip().strip('"') for p in prefixes_list.split(',')]
                    print("Command prefixes:", ', '.join(prefixes))
                else:
                    print("Command has no prefixes.")
        else:
            if configs.is_debug:
                print(f' ╰─{black} $path{reset} {command_path}\n')

            run_command(f"python {command_path} {arguments}")
    else:
        print(f"Command '{command_name}' not found.")
