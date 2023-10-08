import os, random

BACKGROUND_WHITE = "\033[47m"
ENDC = '\033[0m'

clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')

def emptyBoard():
    return [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
    ]


def printBoard(board,currentLoc):
    clear()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (row, col) == currentLoc:
                print(f"{BACKGROUND_WHITE}{board[row][col]}{ENDC} ",end="")
            else:
                print(f"{board[row][col]} ",end="")
        print()
    print("___________")


# Validation Functions
def checkMove(board,currentLoc):
    if board[currentLoc[0]][currentLoc[1]] == "-":
        return True
    return False


def checkIfWon(board,userLabel):
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


def userOption(ans, currentLoc):
    if ans == "w":
        return checkLoc(currentLoc[0]-1,currentLoc[1])
    elif ans == "s":
        return checkLoc(currentLoc[0]+1,currentLoc[1])
    elif ans == "a":
        return checkLoc(currentLoc[0],currentLoc[1]-1)
    elif ans == "d":
        return checkLoc(currentLoc[0],currentLoc[1]+1)
    elif ans == "" or ans == "m":
        return (-1,-1)
    else:
        return (-2,-2)


def gameOver(haveWon, turn):
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


"""
Rule 1: If I have a winning move, take it. 
Rule 2: If the opponent has a winning move, block it. 
Rule 3: If I can create a fork (two winning ways) after this move, do it.
"""
# # Computer Opponent
# def aiCrucialLoc(userLabel):
#     for row in range(len(board)):
#         rowCheck = 0
#         unusedLoc = -1
#         for col in range(len(board[row])):
#             if board[row][col] == userLabel:
#                 rowCheck += 1
#             elif board[row][col] == "-":
#                 unusedLoc = col
#         if rowCheck == 2:
#             return (row,unusedLoc)
    
#     # check columns
#     for row in range(len(board)):
#         colCheck = 0
#         unusedLoc = -1
#         for col in range(len(board[col])):
#             if board[col][row] == userLabel:
#                 colCheck += 1
#             elif board[col][row] == "-":
#                 unusedLoc = row
#         if colCheck == 2:
#             return (col,unusedLoc)
        
#         diagonalCheck = 0
#         for num in range(len(board)):
#             if board[num][num] == userLabel:
#                 diagonalCheck += 1
#             elif board[num][num] == "-":
#                 unusedLoc = num
#         if diagonalCheck == 2:
#             return (num,num)

#         # check both diagonals
#         diagonalCheck = 0
#         for num in range(len(board)):
#             unusedLoc = -1
#             colNum = len(board) - num-1
#             if board[num][colNum] == userLabel:
#                 diagonalCheck += 1
#             elif board[num][colNum] == "-":
#                 unusedLoc = colNum
#         if diagonalCheck == 2:
#             return (num,colNum)

#     return (-1,-1)


# def aiFindCell(userLabel,opponentLabel):
#     # Find winning move
#     compWinMove = aiCrucialLoc(userLabel)
#     if compWinMove != (-1,-1):
#         return compWinMove

#     # Find opponent winning move and block it
#     compBlockMove = aiCrucialLoc(opponentLabel)
#     if compBlockMove != (-1,-1):
#         return compBlockMove

#     # Starting move
#     if board[1][1] == "-" and random.randint(0,1) == 0:
#         return (1,1)
#     else:
#         pickCorner = random.randint(0,3)
#         if (pickCorner == 0 or pickCorner == 2 ) and board[pickCorner][pickCorner] != "-":
#             return(pickCorner,pickCorner)
#         elif pickCorner == 1 and board[0][2] != "-":
#             return (0,2)
#         elif pickCorner == 3 and board[2][0] != "-":
#             return (2,0)

#     return (-1,-1)


# def vsComputer():
#     currentLoc = (0,0)
#     board = emptyBoard()

#     haveWon = False
#     player1Label = "X"
#     player2Label = "O"
#     turn = 0

#     while haveWon == False:
#         if turn > 8:
#             break
#         elif turn % 2 == 0:
#             currentLabel = player1Label

#             printBoard()
#             print("_______")
#             ans = input("> ")

#             global currentLoc
#             if ans == "w":
#                 currentLoc = checkLoc(currentLoc[0]-1,currentLoc[1])
#             elif ans == "s":
#                 currentLoc = checkLoc(currentLoc[0]+1,currentLoc[1])
#             elif ans == "a":
#                 currentLoc = checkLoc(currentLoc[0],currentLoc[1]-1)
#             elif ans == "d":
#                 currentLoc = checkLoc(currentLoc[0],currentLoc[1]+1)
#             elif ans == "" or ans == "m":
#                 if checkMove(currentLabel):
#                     board[currentLoc[0]][currentLoc[1]] = currentLabel
#                     turn += 1

#             haveWon = checkIfWon(currentLabel)
#         else:
#             currentLabel = player2Label
#             compCell = aiFindCell(currentLabel,player1Label)
#             board[compCell[0]][compCell[1]] = player2Label
#             haveWon = checkIfWon(currentLabel)

#             turn += 1
#     gameOver(turn)


def vsHuman():
    currentLoc = (0,0)
    board = emptyBoard()

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
    
        printBoard(board,currentLoc)
        ans = input("> ")

        newCurrLoc = userOption(ans, currentLoc)
        print(newCurrLoc,currentLoc,checkMove(board,currentLoc))
        if newCurrLoc == (-1,-1) and checkMove(board,currentLoc):
            board[currentLoc[0]][currentLoc[1]] = currentLabel
            turn += 1
        elif newCurrLoc != (-2,-2) and board[currentLoc[0]][currentLoc[1]] == "-":
            currentLoc = newCurrLoc

        haveWon = checkIfWon(board,currentLabel)
    
    printBoard(board,currentLoc)
    gameOver(haveWon,turn)


def main():
    while True:
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
            #vsComputer()
            pass
        elif ans == "q" or ans == "Q":
            break

if __name__ == "__main__":
    main()