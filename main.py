import os
import subprocess
from colorama import init, Fore, Style
from mainFiles.main_commands import *

init()

magneta = Fore.MAGENTA
red = Fore.RED
green = Fore.GREEN
black = Fore.BLACK
reset = Style.RESET_ALL



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        user_input = input("$> ")
        if not user_input:
            continue

        parts = user_input.split(' ', 1)
        command = parts[0].lower()
        arguments = parts[1] if len(parts) > 1 else ''

        if command == 'dir':
            dir(arguments)
        elif command == 'mkdir':
            mkdir(arguments)
        elif command == 'rmdir':
            rmdir(arguments)
        elif command == 'cd':
            cd(arguments)
        elif command == 'cls':
            cls(arguments)
        elif command == 'python':
            execute_python(arguments)
        elif command == 'pip':
            run_command(f"pip {arguments}")
        elif command == 'jds':
            command_parts = arguments.split(' ', 1)
            command_name = command_parts[0]
            command_arguments = command_parts[1] if len(command_parts) > 1 else ''
            show_all_prefixes = '-all_prefixes' in command_arguments
            execute_custom_command(command_name, command_arguments, show_all_prefixes)
        else:
            print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
