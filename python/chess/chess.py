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


class Square:
    def __init__(self,loc):
        self.loc = loc
    
    def valid():
        pass

class Empty:
    def __init__(self):
        pass

    def valid():
        return True

class Pawn:
    def __init__(self, loc, color):
        self.loc = loc
        self.color = color
    
    def valid(self, board, userMove):
        move = abs(self.loc[0] - cursor[0])
        if abs(self.loc[0] - cursor[0]) == 2 and type(board[userMove[0]][userMove[1]]) == Empty:
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


def selectPieceMove(board, piece, cursor):
    tempCu = cursor
    printChessBoard(board,cursor)
    print(f"PIECE: {piece}")
    while True:
        decodedMove = selectLocation(board, cursor)
        
        if decodedMove == EXIT:
            break
        elif decodedMove != STAY and decodedMove != CHOSEN: 
            cursor = decodedMove        
        elif decodedMove ==  CHOSEN:
            chosenMove = board[cursor[0]][cursor[1]]
            if chosenMove == " ":
                board[tempCu[0]][tempCu[1]] = " "
                board[cursor[0]][cursor[1]] = piece
                break
            else:
                print("INVALID_MOVE")
        
        printChessBoard(board,cursor)
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
    printChessBoard(chessboard, cursor)

    while True:
        decodedMove = selectLocation(chessboard, cursor)
        while kb.kbhit(): kb.getch()

        if decodedMove == EXIT:
            break
        elif decodedMove != STAY and decodedMove != CHOSEN: 
            cursor = decodedMove        
        elif decodedMove ==  CHOSEN: # and validPiece(board, cursor,turn)
            chosenPiece = chessboard[cursor[0]][cursor[1]]
            selectPieceMove(chessboard, chosenPiece, cursor)
        printChessBoard(chessboard, cursor)
    
    turn += 1

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
