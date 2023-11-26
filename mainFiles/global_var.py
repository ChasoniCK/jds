import os
import getpass

global_vars = {
    "$path": os.getcwd(),
    "$user": getpass.getuser()
}

#for key, value in global_vars.items():
#    print(f'{key}: {value}')
