import os, random
import msvcrt as kb
from chessPieces import BlackPawn,BlackRook,BlackBishop,BlackKnight,BlackQueen,BlackKing
from chessPieces import WhitePawn,WhiteRook,WhiteBishop,WhiteKnight,WhiteQueen,WhiteKing
from chessPieces import Empty

LENGTH = 8
EXIT = (-99,-99)

BG = "\033[47m"
SEL = "\033[106m"
ENDC = '\033[0m'
clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')


def createChessBoard():
    blackPieces = [BlackRook(), BlackKnight(), BlackBishop(),BlackQueen(),BlackKing(),BlackBishop(), BlackKnight(),BlackRook()]
    blackPiecesPawns = [BlackPawn() for i in range(LENGTH)]
    whitePieces = [WhiteRook(), WhiteKnight(), WhiteBishop(),WhiteQueen(),WhiteKing(),WhiteBishop(), WhiteKnight(),WhiteRook()]
    whitePiecesPawns = [WhitePawn() for i in range(LENGTH)]

    return [blackPieces, blackPiecesPawns,[Empty() for i in range(LENGTH)],[Empty() for i in range(LENGTH)],whitePiecesPawns,whitePieces]

def printChessboard(chessboard,currSquare):
    even = 0
    for i in range(len(chessboard)):
        for j in range(len(chessboard[i])):
            if currSquare == (i,j):
                print(f'{SEL}', end="")
            elif even % 2 == 0:
                print(f'{BG}',end="")
            print(f"{chessboard[i][j].c} {ENDC}",end="")
            even += 1
        print()
        even += 1


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


def decodeInput(userInput, currSquare):
    if userInput == "w":
        return validateBounds(currSquare[0]-1,currSquare[1])
    elif userInput == "s":
        return validateBounds(currSquare[0]+1,currSquare[1])
    elif userInput == "a":
        return validateBounds(currSquare[0],currSquare[1]-1)
    elif userInput == "d":
        return validateBounds(currSquare[0],currSquare[1]+1)
    elif userInput == "q":
        return EXIT
    else:
        return currSquare


def main():
    currSquare = (0,0)
    chessboard = createChessBoard()

    while True:
        clear()
        printChessboard(chessboard,currSquare)
        userInput = kb.getch().decode('utf-8')
        
        currSquare = decodeInput(userInput,currSquare)
        
        if currSquare == EXIT:
            break

if __name__ == "__main__":
    main()