import os, random
from pynput import keyboard
import msvcrt as kb


BACKGROUND_WHITE = "\033[47m"
ENDC = '\033[0m'
SELECTED=  "\033[106m"
clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')

CHOSEN = (-1,-1)
STAY = (-2,-2)
EXIT = (-9,-9)


class Empty:
    def __init__(self):
        self.c = " "

    def valid():
        return True

class Pawn:
    def __init__(self, c):
        self.c = c
        self.loc = STAY
    
    def valid(self, board, pieceLoc, userMove):
        if loc == STAY:
            return False
        elif abs(pieceLoc[0] - userMove[0]) == 2 and type(board[userMove[0]][userMove[1]]) == Empty:
            return True 


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


def validateMove(piece):
    pass


def decodeChar(option, cursorLoc):
    if option == "w":
        return validateBounds(cursorLoc[0]-1,cursorLoc[1])
    elif option == "s":
        return validateBounds(cursorLoc[0]+1,cursorLoc[1])
    elif option == "a":
        return validateBounds(cursorLoc[0],cursorLoc[1]-1)
    elif option == "d":
        return validateBounds(cursorLoc[0],cursorLoc[1]+1)
    else:
        return STAY


def createBlackPieces():
    return [[Pawn("♟︎") for j in range(8)] for i in range(2)]


def createEmptyPieces():
    return [[Empty() for j in range(8)] for i in range(4)]
    

def createWhitePieces():
    return [[Pawn("♙") for j in range(8)] for i in range(2)]


def printSelecetedBoard(board,cursor,piece):
    even = 0
    clear()
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if cursor == (row,col):
                print(f'{SELECTED}', end="")
            elif validateMove(piece):
                pass
            elif even % 2 == 0:
                print(f'{BACKGROUND_WHITE}',end="")
            print(f"{board[row][col].c} {ENDC}",end="")
            even += 1
        print()
        even += 1


def printUnselectedBoard(board,cursor):
    even = 0
    clear()
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if cursor == (row,col):
                print(f'{SELECTED}', end="")
            elif even % 2 == 0:
                print(f'{BACKGROUND_WHITE}',end="")
            print(f"{board[row][col].c} {ENDC}",end="")
            even += 1
        print()
        even += 1


def selectPieceMove(board, piece, cursor):
    tempCu = cursor
    printSelecetedBoard(board,cursor,piece)
    print(f"PIECE: {piece}")
    while True:
        decodedMove = selectLocation(board, cursor)
        
        if decodedMove == EXIT:
            return tempCu
        elif decodedMove != STAY and decodedMove != CHOSEN: 
            cursor = decodedMove        
        elif decodedMove ==  CHOSEN and piece.valid(board, tempCu, cursor):
            board[tempCu[0]][tempCu[1]] = Empty()
            board[cursor[0]][cursor[1]] = piece
            return cursor        
        printSelecetedBoard(board,cursor,piece)
        print(f"PIECE: {piece}")
        print(f"PIECE_LOC: {tempCu}")
        print(f"NEW_LOC: {cursor}")
        print(f"{abs(tempCu[0] - cursor[0])}")
    while kb.kbhit(): kb.getch()


def selectLocation(board,cursorLoc):
    with keyboard.Events() as events:
        for event in events:
            if type(event) == keyboard.Events.Release and type(event.key) == keyboard._win32.KeyCode:
                return decodeChar(event.key.char, cursorLoc)
            elif type(event) == keyboard.Events.Release and event.key == keyboard.Key.enter: # and validPiece(board,cursorLoc):
                return CHOSEN
            elif event.key == keyboard.Key.esc:
                return EXIT
            
    while kb.kbhit(): kb.getch()


def main():
    clear()
    chessboard = createBlackPieces() + createEmptyPieces() + createWhitePieces()
    cursor = (0,0)
    turn = 0
    printUnselectedBoard(chessboard, cursor)

    while True:
        decodedMove = selectLocation(chessboard, cursor)
        while kb.kbhit(): kb.getch()

        if decodedMove == EXIT:
            break
        elif decodedMove != STAY and decodedMove != CHOSEN: 
            cursor = decodedMove        
        elif decodedMove ==  CHOSEN: # and validPiece(board, cursor,turn)
            chosenPiece = chessboard[cursor[0]][cursor[1]]
            cursor = selectPieceMove(chessboard, chosenPiece, cursor)
            while kb.kbhit(): kb.getch()

            turn += 1
        printUnselectedBoard(chessboard, cursor)
    

    # if turn == 0:
    #     print("***---***---***")   
    #     print("WHITE's TURN")
    #     print("***---***---***")   
    #     print("Piece Selected: ")
    #     print("Location: ")
    # elif turn == 1:
    #     print("***---***---***")   
    #     print("BLACK's TURN")
    #     print("***---***---***")   
    #     print("Piece Selected: ")
    #     print("Location: ")
    # turn += 1

if __name__ == '__main__':
    main()
