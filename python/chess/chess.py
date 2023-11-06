import os, random
from pynput import keyboard
import msvcrt as kb


BACKGROUND_WHITE = "\033[47m"
ENDC = '\033[0m'
SELECTED=  "\033[106m"
clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')

NO_MOVE = (-2,-2)

class Piece:
    def __init__(self,color):
        pass
 

def validateBounds(x,y):
    if x == 8:
        x -= 1
    elif x == -1:
        x += 1
    elif y == 8:
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


def createBlackPieces():
    return [["♜","♞","♝","♛","♚","♝","♞","♜"],
    ["♟︎","♟︎","♟︎","♟︎","♟︎","♟︎","♟︎","♟︎"]]


def createEmptyPieces():
    return [[" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "]]
    

def createWhitePieces():
    return [["♙","♙","♙","♙","♙","♙","♙","♙"],
    ["♖","♘","♗","♕","♔","♗","♘","♖"]]


def printChessBoard(board,cursor):
    even = 0
    clear()
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if cursor == (row,col):
                print(f'{SELECTED}', end="")
            elif even % 2 == 0:
                print(f'{BACKGROUND_WHITE}',end="")
            print(f"{board[row][col]} {ENDC}",end="")
            even += 1
        print()
        even += 1


def main():
    clear()
    chessBoard = createBlackPieces() + createEmptyPieces() + createWhitePieces()
    cursorLoc = (0,0)
    turn = 0

    printChessBoard(chessBoard,cursorLoc)
    with keyboard.Events() as events:
        for event in events:
            if type(event) == keyboard.Events.Release and type(event.key) == keyboard._win32.KeyCode:
                newCurrLoc = moveCursor(event.key.char, cursorLoc)
                cursorLoc = cursorLoc if newCurrLoc == NO_MOVE else newCurrLoc
            elif event.key == keyboard.Key.enter and validateMove(board,cursorLoc):
                board[cursorLoc[0]][cursorLoc[1]] = currentLabel
                turn += 1
            elif event.key == keyboard.Key.esc:
                break
            
            printChessBoard(chessBoard,cursorLoc)

    # clears buffer
    while kb.kbhit(): kb.getch()

    # printChessBoard(board,cursorLoc)
    # gameOverScreen(haveWon,turn)
    

    # printChessBoard(chessBoard,currentCursor)
    
    if turn == 0:
        print("***---***---***")   
        print("WHITE's TURN")
        print("***---***---***")   
        print("Piece Selected: ")
        print("Location: ")
    elif turn == 1:
        print("***---***---***")   
        print("BLACK's TURN")
        print("***---***---***")   
        print("Piece Selected: ")
        print("Location: ")
    turn += 1

    

if __name__ == '__main__':
    main()