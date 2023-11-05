import os
from pynput import keyboard
import msvcrt as kb


def writeToFile():
    with open("keylogged.txt","a") as file:
        file.write("a")


def main():
    writeToFile()


if __name__ == "__main__":
    main()