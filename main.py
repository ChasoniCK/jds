import os
import getpass
from colorama import init, Fore, Style
from mainFiles.main_commands import *
import mainFiles.configs as configs
import mainFiles.global_var as gv
import inline


init()

magneta = Fore.MAGENTA
red = Fore.RED
green = Fore.GREEN
black = Fore.BLACK
reset = Style.RESET_ALL
inl_input = inline.input

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        commands = ["debug", "global_vars", "dir", "mkdir", "rmdir", "cd", "cls", "python", "pip", "jds"]
        current_dir = os.getcwd()
        username = getpass.getuser()

        print(f'\n@{username} ~ {current_dir}')
        if configs.is_debug:
            user_input = inl_input(f" {red}${reset}> ", )
        else:
            user_input = inl_input(f" $> ", command=commands)

        if not user_input:
            continue

        parts = user_input.split(' ', 1)
        command = parts[0].lower()
        arguments = parts[1] if len(parts) > 1 else ''

        if command == 'debug':
            password = inl_input('Enter passwrod: ', secret=True)
            if password == configs.password:
                if configs.is_debug == False:
                    configs.is_debug = True
                else:
                    configs.is_debug = False
            else:
                print(red + "Incorrect password" + reset)
        elif command == 'global_vars':
            for key, value in gv.global_vars.items():
                print(f'{key}: {value}')
        elif command == 'dir':
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
