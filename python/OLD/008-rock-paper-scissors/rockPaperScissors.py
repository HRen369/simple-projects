import os, random
import msvcrt as kb

BACKGROUND_WHITE = "\033[47m"
ENDC = '\033[0m'


clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')


options = ["rock", "paper","scissors"]


def pickChoice():
    return random.choice(options)


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
    

def displayResults(userChoice):
    opponent = pickChoice()
    user = options[userChoice]

    rock = options[0]
    paper = options[1]
    scissors = options[2]

    clear()
    print("*-*-*-*-*-*-*-*-*-*-")    
    print(f"Y: {user.capitalize()}")
    print(f"O: {opponent.capitalize()}")

    if user == opponent:
        print("DRAW!!!")
    elif user == rock and opponent == paper:
        print("OPPONENT WON!!!") 
    elif user == scissors and opponent == rock:
        print("OPPONENT WON!!!") 
    elif user == paper and opponent == scissors:
        print("OPPONENT WON!!!") 
    elif user == paper and opponent == rock:
        print("YOU WON!!!") 
    elif user == rock and opponent == scissors:
        print("YOU WON!!!")
    elif user == scissors and opponent == paper:
        print("YOU WON!!!")
    print("*-*-*-*-*-*-*-*-*-*-")    
    input("[Enter] to Continue > ")



def game():
    menu = 0
    userChoice = -1

    while True:
        printMenu(menu)
        userInput = kb.getch().decode('utf-8')

        if userInput == "w" and menu > 0:
            menu -= 1
        elif userInput == "s" and menu < 2:
            menu += 1
        elif userInput == "\r":
            userChoice = menu
            break            
        if userInput == "q":
            break
    
    displayResults(userChoice)

    

def main():
    startGame = False
    while True:
        clear()
        print("Rock, Paper, Scissors!")
        print("*-*-*-*-*-*-*-*-*-*-")
        print("[Enter] to Start")
        print("[Q] to Quit")
        print("*-*-*-*-*-*-*-*-*-*-")


        userInput = kb.getch().decode('utf-8')

        if userInput == "q":
            break
        elif userInput == "\r":
            startGame = True
            break

    if startGame:
        game()


if __name__ == '__main__':
    main()