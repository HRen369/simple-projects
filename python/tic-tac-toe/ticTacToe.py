import os, random

BACKGROUND_WHITE = "\033[47m"
ENDC = '\033[0m'
currentLoc = (0,0)

board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')


def checkMove(userLabel):
    global currentLoc
    if board[currentLoc[0]][currentLoc[1]] == "-":
        return True
    return False

def checkIfWon(userLabel):
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

        diagonalCheck = 0
        for num in range(len(board)):
            if board[num][num] == userLabel:
                diagonalCheck += 1
        if diagonalCheck == 3:
            return True

        diagonalCheck = 0
        for num in range(len(board)):
            colNum = len(board) - num-1
            if board[num][colNum] == userLabel:
                diagonalCheck += 1
        if diagonalCheck == 3:
            return True

    return False


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


def printBoard():
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (row, col) == currentLoc:
                print(f"{BACKGROUND_WHITE}{board[row][col]}{ENDC} ",end="")
            else:
                print(f"{board[row][col]} ",end="")
        print()

"""
Rule 1: If I have a winning move, take it. 
Rule 2: If the opponent has a winning move, block it. 
Rule 3: If I can create a fork (two winning ways) after this move, do it.
"""

def aiCrucialLoc(userLabel):
    for row in range(len(board)):
        rowCheck = 0
        unusedLoc = -1
        for col in range(len(board[row])):
            if board[row][col] == userLabel:
                rowCheck += 1
            elif board[row][col] == "-":
                unusedLoc = col
        if rowCheck == 2:
            return (row,unusedLoc)
    
    # check columns
    for row in range(len(board)):
        colCheck = 0
        unusedLoc = -1
        for col in range(len(board[col])):
            if board[col][row] == userLabel:
                colCheck += 1
            elif board[col][row] == "-":
                unusedLoc = row
        if colCheck == 2:
            return (col,unusedLoc)
        
        diagonalCheck = 0
        for num in range(len(board)):
            if board[num][num] == userLabel:
                diagonalCheck += 1
            elif board[num][num] == "-":
                unusedLoc = num
        if diagonalCheck == 2:
            return (num,num)

        # check both diagonals
        diagonalCheck = 0
        for num in range(len(board)):
            unusedLoc = -1
            colNum = len(board) - num-1
            if board[num][colNum] == userLabel:
                diagonalCheck += 1
            elif board[num][colNum] == "-":
                unusedLoc = colNum
        if diagonalCheck == 2:
            return (num,colNum)

    return (-1,-1)


def aiFindCell(userLabel,opponentLabel):
    # Find winning move
    compWinMove = aiCrucialLoc(userLabel)
    if compWinMove != (-1,-1):
        return compWinMove

    # Find opponent winning move and block it
    compBlockMove = aiCrucialLoc(opponentLabel)
    if compBlockMove != (-1,-1):
        return compBlockMove
    

    #starting move
    # if board[1][1] == "-":
    #     pickCenter = random.randint(0,1)
    #     if pickCenter == 0:
    #         return (1,1)
    #     else:
    #         pass
    
    
    # random move; might remove later
    # while True:
    #     x = random.randint(0, len(board)-1)
    #     y = random.randint(0, len(board)-1)

    #     if board[x][y] == "-":
    #         return (x,y)
    #     elif board[y][x] == "-":
    #         return (y,x)
    return (1,1)


def vsComputer():
    clear()

    haveWon = False
    player1Label = "X"
    player2Label = "O"
    turn = 0
    totalCells = 8

    while haveWon == False:
        if turn > totalCells:
            break
        elif turn % 2 == 0:
            currentLabel = player1Label

            # markCell(playerLabel, currentLoc)
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
                if checkMove(currentLabel):
                    board[currentLoc[0]][currentLoc[1]] = currentLabel
                    turn += 1

            haveWon = checkIfWon(currentLabel)
        else:
            currentLabel = player2Label
            compCell = aiFindCell(currentLabel,player1Label)
            board[compCell[0]][compCell[1]] = player2Label
            haveWon = checkIfWon(currentLabel)

            turn += 1

    
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


def vsHuman():
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
            if checkMove(currentLabel):
                board[currentLoc[0]][currentLoc[1]] = currentLabel
                turn += 1

        haveWon = checkIfWon(currentLabel)

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


def main():
    running = True
    while running:
        clear()
        print("Python Tic Tac Toe")
        print("  [1] Human Vs Human")
        print("  [2] Human Vs Computer")
        print("  [q] Quit")
        print("___________")
        ans = input("> ")

        if ans == "1":
            vsHuman()
        elif ans == "2":
            vsComputer()
        elif ans == "q" or ans == "Q":
            running = False

if __name__ == "__main__":
    main()