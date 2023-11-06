import os, random
from pynput import keyboard
import msvcrt as kb


BACKGROUND_WHITE = "\033[47m"
ENDC = '\033[0m'


clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')


class Piece:
    def __init__(self,color):
        pass
 

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
            if even % 2 == 0:
                print(f'{BACKGROUND_WHITE}{board[row][col]} {ENDC}',end="")
            else:
                print(f'{board[row][col]} ',end="")
            even += 1
        even += 1
        print()



def main():
    clear()
    chessBoard = createBlackPieces() + createEmptyPieces() + createWhitePieces()
    currentCursor = (0,0)
    turn = 0
    
    printChessBoard(chessBoard,currentCursor)
    
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