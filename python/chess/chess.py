import os, random
from pynput import keyboard
import msvcrt as kb

BACKGROUND_WHITE = "\033[47m"
ENDC = '\033[0m'

NO_MOVE = (-2,-2)
PICKED = (-1,-1)

clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')


def createEmptyBoard():
    return [
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"]
    ]


def main():
    clear()
    print("Chess Game")
    print(len(createEmptyBoard()))
    print(len(createEmptyBoard()[0]))

if __name__ == '__main__':
    main()