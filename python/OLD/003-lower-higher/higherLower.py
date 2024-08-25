import os, random

clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')

HIGHER = 100
LOWER = 1

def printResults(guessedNum, randomNum):
    print("You found the guessed number!")
    print("Number:",number)
   

def game():
    randomNum = int(random.random() * HIGHER) + 1
    lower = LOWER
    higher = HIGHER

    while True:        
        clear()
        print("Guess the Random Number.")
        print(f"Random Number is between {lower} -- {higher}")
        numString = input("> ")
        guessedNum = convertNumStr(numString)
                
        if guessedNum > randomNum:
            higher = guessedNum
        elif guessedNum < randomNum and guessedNum > 0:
            lower = guessedNum
        elif guessedNum == randomNum:
            break
        
    printResults(guessedNum,randomNum)


def convertNumStr(numString):
    try:
        return int(numString)
    except:
        return -1


def main():
    game()

if __name__ == "__main__":
    main()