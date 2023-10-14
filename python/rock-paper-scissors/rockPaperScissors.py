import os, random
from pynput import keyboard

BACKGROUND_WHITE = "\033[47m"
ENDC = '\033[0m'


clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')

def printMenu(menu):
    clear()
    print("Take your pick")
    print("*-*-*-*-*-*-*-*-*-*-")

    if menu == 0:
        print(f"{BACKGROUND_WHITE}[1]{ENDC} Rock")
        print("[2] Paper")
        print("[3] Scissors")
        print("----")
        print("[Esc] Quit")
    elif menu == 1:
        print("[1] Rock")
        print(f"{BACKGROUND_WHITE}[2]{ENDC} Paper")
        print("[3] Scissors")
        print("----")
        print("[Esc] Quit")
    elif menu == 2:
        print("[1] Rock")
        print("[2] Paper")
        print(f"{BACKGROUND_WHITE}[3]{ENDC} Scissors")
        print("----")
        print("[Esc] Quit")

    print("*-*-*-*-*-*-*-*-*-*-")
    
    

def game():
    running = True
    menu = 0
    userChoice = -1

    while running:
        printMenu(menu)

        with keyboard.Events() as events:
            for event in events:
                if type(event) == keyboard.Events.Release:
                    if event.key == keyboard.Key.up and menu > 0:
                        menu -= 1
                    elif event.key == keyboard.Key.down and menu < 2:
                        menu += 1                    
                    elif event.key == keyboard.Key.esc:
                        running = False
                    elif event.key == keyboard.Key.enter:
                        userChoice = menu                
                        running = False
                    break

def main():
    clear()
    print("Rock, Paper, Scissors!")
    print("*-*-*-*-*-*-*-*-*-*-")
    print("[Enter] to Start")
    print("[ESC] to Quit")
    print("*-*-*-*-*-*-*-*-*-*-")

    startGame = False
    with keyboard.Events() as events:
        for event in events:
            if type(event) == keyboard.Events.Release:        
                if event.key == keyboard.Key.enter:
                    startGame = True
                    break    
                elif event.key == keyboard.Key.esc:
                    startGame = False
                    break
    if startGame:
        game()

if __name__ == '__main__':
    game()