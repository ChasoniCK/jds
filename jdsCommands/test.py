from sys import argv
def main():
    print('pisya')

def a():
    print('a?')

def b():
    print('b?')

if __name__ == "__main__":
    if "-a" in argv:
        a()
    elif "-b" in argv: 
        b()
    else:
        main()

prefixes = ["-a", "-b"]