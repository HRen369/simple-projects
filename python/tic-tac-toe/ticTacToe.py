import os, random
from pynput import keyboard
import msvcrt as kb

BACKGROUND_WHITE = "\033[47m"
ENDC = '\033[0m'

NO_MOVE = (-2,-2)

clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')


def createEmptyBoard():
    return [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
    ]


def printBoard(board,cursorLoc):
    clear()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (row, col) == cursorLoc:
                print(f"{BACKGROUND_WHITE}{board[row][col]}{ENDC} ",end="")
            else:
                print(f"{board[row][col]} ",end="")
        print()
    print("___________")


# Validation Functions
def validateMove(board,chosenLoc):
    if board[chosenLoc[0]][chosenLoc[1]] == "-" and chosenLoc != NO_MOVE:
        return True
    return False


def validateWin(board,userLabel):
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
            colNum = len(board) - num - 1
            if board[num][colNum] == userLabel:
                diagonalCheck += 1
        if diagonalCheck == 3:
            return True

    return False


def validateBounds(x,y):
    if x == 3:
        x -= 1
    elif x == -1:
        x += 1
    elif y == 3:
        y -= 1
    elif y == -1:
        y += 1

    return (x,y)


def moveCursor(option, cursorLoc):
    if option == "w":
        return validateBounds(cursorLoc[0]-1,cursorLoc[1])
    elif option == "s":
        return validateBounds(cursorLoc[0]+1,cursorLoc[1])
    elif option == "a":
        return validateBounds(cursorLoc[0],cursorLoc[1]-1)
    elif option == "d":
        return validateBounds(cursorLoc[0],cursorLoc[1]+1)
    else:
        return NO_MOVE


def gameOverScreen(haveWon, turn):
    if haveWon:
        if (turn-1) % 2 == 0:
            wonLabel = "Player 1"
        else:
            wonLabel = "Player 2"
        print(f"{wonLabel} Has Won!")
    else:
        print("Draw Between Both Players!")
    print("Press Enter to continue")

    with keyboard.Events() as events:
        for event in events:
            if type(event) == keyboard.Events.Release and event.key == keyboard.Key.enter:
                break

    # clears buffer
    while kb.kbhit(): kb.getch()


# Computer Opponent
def findCrucialMove(board,userLabel):
    for row in range(len(board)):
        rowCheck = 0
        unusedLoc = -1
        for col in range(len(board[row])):
            if board[row][col] == userLabel:
                rowCheck += 1
            elif board[row][col] == "-":
                unusedLoc = col
        if rowCheck == 2 and validateMove(board,(row,unusedLoc)):
            return (row,unusedLoc)
    
    # check columns
    for row in range(len(board)):
        colCheck = 0
        unusedCol = -2
        unusedRow = -2
        for col in range(len(board[row])):
            if board[col][row] == userLabel:
                colCheck += 1
            elif board[col][row] == "-":
                unusedRow = row
                unusedCol = col
        if colCheck == 2 and validateMove(board,(unusedCol,unusedRow)):
            return (unusedCol,unusedRow)
        

    # check both diagonals
    diagonalCheck = 0
    unusedRow = -1
    for num in range(len(board)):
        if board[num][num] == userLabel:
            diagonalCheck += 1
        elif board[num][num] == "-":
            unusedRow = num
    if diagonalCheck == 2  and validateMove(board,(unusedRow,unusedRow)):
        return (unusedRow,unusedRow)

    diagonalCheck = 0
    unusedRow = -1
    unusedCol = -1
    for num in range(len(board)):
        colNum = len(board) - num-1
        if board[num][colNum] == userLabel:
            diagonalCheck += 1
        elif board[num][colNum] == "-":
            unusedCol = colNum
            unusedRow = num
    if diagonalCheck == 2  and validateMove(board,(unusedRow,unusedCol)):
        return (unusedRow,unusedCol)

    return NO_MOVE


def randomMove(board,userLabel):
    lastCell = NO_MOVE
    foundInput = False

    for row in range(len(board)):
        for col in range(len(board[row])):
            if validateMove(board,(row,col)):
                lastCell = (row,col)
                if foundInput:
                    return (row,col)
            elif board[row][col] == userLabel:
                foundInput = True 

    return lastCell

"""
Rule 1: If I have a winning move, take it. 
Rule 2: If the opponent has a winning move, block it. 
Rule 3: If I can create a fork (two winning ways) after this move, do it.
"""
def aiFindCell(board,turn,userLabel,opponentLabel):
    # Find winning move
    compWinMove = findCrucialMove(board,userLabel)
    if compWinMove != NO_MOVE:
        return compWinMove

    # Find Losing move
    compBlockMove = findCrucialMove(board,opponentLabel)
    if compBlockMove != NO_MOVE:
        return compBlockMove

    # Starting move
    if turn in [0,1]:
        if validateMove(board,(1,1)) and random.randint(0,1) == 0:
            return (1,1)
        else:
            cornerLoc = random.randint(0,3)
            if cornerLoc in [0,2] and validateMove(board,(cornerLoc,cornerLoc)):
                return(cornerLoc,cornerLoc)
            elif cornerLoc == 1 and validateMove(board,(0,2)):
                return (0,2)
            elif cornerLoc == 3 and validateMove(board,(2,0)):
                return (2,0)

    return randomMove(board,userLabel)


def vsComputer():
    cursorLoc = (0,0)
    board = createEmptyBoard()
    printBoard(board,cursorLoc)

    haveWon = False
    player1Label = "X"
    player2Label = "O"
    turn = 0

    with keyboard.Events() as events:
        for event in events:
            if turn > 8:
                break
            elif turn % 2 == 0:
                currentLabel = player1Label

                if type(event) == keyboard.Events.Release and type(event.key) == keyboard._win32.KeyCode:
                    newCurrLoc = moveCursor(event.key.char, cursorLoc)
                    cursorLoc = cursorLoc if newCurrLoc == NO_MOVE else newCurrLoc
                elif event.key == keyboard.Key.enter and validateMove(board,cursorLoc):
                    board[cursorLoc[0]][cursorLoc[1]] = currentLabel
                    turn += 1
                elif event.key == keyboard.Key.esc:
                    break
            else:
                currentLabel = player2Label
                compCell = aiFindCell(board,turn,currentLabel,player1Label)
                board[compCell[0]][compCell[1]] = player2Label
                turn += 1
            
            haveWon = validateWin(board,currentLabel)
            printBoard(board,cursorLoc)
            if haveWon == True:
                break

    # clears buffer
    while kb.kbhit(): kb.getch()

    printBoard(board,cursorLoc)
    gameOverScreen(haveWon,turn)


def vsHuman():
    cursorLoc = (0,0)
    board = createEmptyBoard()
    printBoard(board,cursorLoc)

    haveWon = False
    player1Label = "X"
    player2Label = "O"
    turn = 0


    with keyboard.Events() as events:
        for event in events:
            if turn > 8:
                break
            elif turn % 2 == 0:
                currentLabel = player1Label
            else:
                currentLabel = player2Label

            if type(event) == keyboard.Events.Release and type(event.key) == keyboard._win32.KeyCode:
                newCurrLoc = moveCursor(event.key.char, cursorLoc)
                cursorLoc = cursorLoc if newCurrLoc == NO_MOVE else newCurrLoc
            elif event.key == keyboard.Key.enter and validateMove(board,cursorLoc):
                board[cursorLoc[0]][cursorLoc[1]] = currentLabel
                turn += 1
            elif event.key == keyboard.Key.esc:
                break
            

            printBoard(board,cursorLoc)
            haveWon = validateWin(board,currentLabel)
            if haveWon == True:
                break

    # clears buffer
    while kb.kbhit(): kb.getch()

    printBoard(board,cursorLoc)
    gameOverScreen(haveWon,turn)


def main():
    menuChoice = -1
    print("Python Tic Tac Toe")
    print("  [1] Human Vs Human")
    print("  [2] Human Vs Computer")
    print("___________")

    with keyboard.Events() as events:
        for event in events:
            if type(event) == keyboard.Events.Release:
                if event.key == keyboard.Key.esc:
                    menuChoice = 0
                elif type(event.key) == keyboard._win32.KeyCode and event.key.char == "1":
                    menuChoice = 1
                elif type(event.key) == keyboard._win32.KeyCode and event.key.char == "2":
                    menuChoice = 2


            if menuChoice > -1:
                break
    # clears buffer
    while kb.kbhit(): kb.getch()

    if menuChoice == 1:
        vsHuman()
    elif menuChoice == 2:
        vsComputer()


if __name__ == "__main__":
    main()