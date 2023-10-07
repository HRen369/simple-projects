import os, math

BACKGROUND_WHITE = "\033[47m"
ENDC = '\033[0m'
currentLoc = (0,0)

board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

winningRow = [
    ["-","-","-"],
    ["X","X","X"],
    ["-","-","-"]
]

winningCol = [
    ["-","-","X"],
    ["-","-","X"],
    ["-","-","X"]
]

clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')

def checkValidMove(userLabel):
    global currentLoc
    if board[currentLoc[0]][currentLoc[1]] == "-":
        return True
    return False

def checkWinning(userLabel):
    # check rows
    for row in range(len(board)):
        rowCheck = 0
        for col in range(len(board[row])):
            if board[row][col] == userLabel:
                rowCheck += 1
        if rowCheck == 3:
            return True
    
    # check columns
    for row in range(len(board)):
        colCheck = 0
        for col in range(len(board[col])):
            if board[col][row] == userLabel:
                colCheck += 1
        if colCheck == 3:
            return True

    if board[0][0] == userLabel and board[1][1] == userLabel and board[2][2] == userLabel:
        return True

    return False


def printBoard():
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (row, col) == currentLoc:
                print(f"{BACKGROUND_WHITE}{board[row][col]}{ENDC} ",end="")
            else:
                print(f"{board[row][col]} ",end="")
        print()


def checkLoc(x,y):
    if x == 3:
        x -= 1
    elif x == -1:
        x += 1
    elif y == 3:
        y -= 1
    elif y == -1:
        y += 1

    return (x,y)

def main():
    haveWon = False
    player1Label = "X"
    player2Label = "O"

    turn = 0

    while haveWon == False:
        if turn > 8:
            break
        elif turn % 2 == 0:
            currentLabel = player1Label
        else:
            currentLabel = player2Label
    
        clear()
        printBoard()
        print("_______")
        ans = input("> ")

        global currentLoc
        if ans == "w":
            currentLoc = checkLoc(currentLoc[0]-1,currentLoc[1])
        elif ans == "s":
            currentLoc = checkLoc(currentLoc[0]+1,currentLoc[1])
        elif ans == "a":
            currentLoc = checkLoc(currentLoc[0],currentLoc[1]-1)
        elif ans == "d":
            currentLoc = checkLoc(currentLoc[0],currentLoc[1]+1)
        elif ans == "" or ans == "m":
            if checkValidMove(currentLabel):
                board[currentLoc[0]][currentLoc[1]] = currentLabel
                turn += 1

        haveWon = checkWinning(currentLabel)

    clear()
    printBoard()
    print("___________")
    if haveWon:
        if (turn-1) % 2 == 0:
            wonLabel = "Player 1"
        else:
            wonLabel = "Player 2"
        print(f"{wonLabel} Has Won!")
    else:
        print("Draw Between Both Players!")
    print("Press Enter to continue")
    input(">")

if __name__ == "__main__":
    main()