import os

clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')

hangmanDict = {
    "head":" ",
    "leftArm":" ",
    "body":" ",
    "rightArm":" ",
    "leftLeg":" ",
    "rightLeg":" "
}

def printHangman():
    print(f"  - - - - -")
    print(f"  |       |")
    print(f"  {hangmanDict['head']}       |")
    print(f" {hangmanDict['leftArm']}{hangmanDict['body']}{hangmanDict['rightArm']}      |")
    print(f" {hangmanDict['leftLeg']} {hangmanDict['rightLeg']}      |")
    print(f"  ________|________")


def printGuessedWord(guessedWord):
    for letter in guessedWord:
        print(letter, end=" ")
    print()


def getWord():
    return "test"


def findLetterLoc(chosenWord, letter):
    loc = []

    for i in range(len(chosenWord)):
        if letter == chosenWord[i]:
            loc.append(i)
    return loc


def addLimb(chances):
    match chances:
        case 5:
            hangmanDict['head'] = "O"
        case 4:
            hangmanDict['leftArm'] = "/"
        case 3:
            hangmanDict['body'] = "|"
        case 2:
            hangmanDict['rightArm'] = "\\"
        case 1:
            hangmanDict['leftLeg'] = "/"
        case 0:
            hangmanDict['rightLeg'] = "\\"


def gameOverLoss(chosenWord):
    clear()
    print("You Lost")
    printHangman()
    priny("Word:",chosenWord)
    print("**--**--**--**--**--**")
    ans = input("> ")


def gameOverWon(chosenWord):
    clear()
    print("You Won")
    printHangman()
    priny("Word:",chosenWord)
    print("**--**--**--**--**--**")
    ans = input("> ")


def game():
    chances = 6
    chosenWord = getWord()
    guessedWord = ["_" for i in range(len(chosenWord))]
    guessedLetters = {}

    while True:
        clear()
        printHangman()
        printGuessedWord(guessedWord)
        print("**--**--**--**--**--**")
        ans = input("> ")

        if len(ans) == 1 and ans in chosenWord and ans not in guessedLetters:
            indexes = findLetterLoc(chosenWord, ans)
            for ind in indexes:
                guessedWord[ind] = ans

            if "".join(guessedWord) == chosenWord:
                break
        else:
            chances -= 1
            addLimb(chances)

            if chances == 0:
                break
    
        guessedLetters[ans] = True

    if chances == 0:
        gameOverLoss(chosenWord)
    else:
        gameOverWon(chosenWord)


def main():
    print("Python Hangman")
    print("[1] Start")

    print("______________")
    ans = input(">")

    if ans == "1":
        game()

if __name__ == "__main__":
    game()