import os, random
import msvcrt as kb
from chessPieces import BlackPawn,BlackRook,BlackBishop,BlackKnight,BlackQueen,BlackKing
from chessPieces import WhitePawn,WhiteRook,WhiteBishop,WhiteKnight,WhiteQueen,WhiteKing
from chessPieces import Empty

LENGTH = 8
BG = "\033[47m"
ENDC = '\033[0m'
clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')


def createChessBoard():
    blackPieces = [BlackRook(), BlackKnight(), BlackBishop(),BlackQueen(),BlackKing(),BlackBishop(), BlackKnight(),BlackRook()]
    blackPiecesPawns = [BlackPawn() for i in range(LENGTH)]
    whitePieces = [WhiteRook(), WhiteKnight(), WhiteBishop(),WhiteQueen(),WhiteKing(),WhiteBishop(), WhiteKnight(),WhiteRook()]
    whitePiecesPawns = [WhitePawn() for i in range(LENGTH)]

    return [blackPieces, blackPiecesPawns,[Empty() for i in range(LENGTH)],[Empty() for i in range(LENGTH)],whitePiecesPawns,whitePieces]

def printChessboard(chessboard):
    even = 0
    for i in range(len(chessboard)):
        for j in range(len(chessboard[i])):
            if even % 2 == 0:
                print(f'{BG}',end="")
            print(f"{chessboard[i][j].c} {ENDC}",end="")
            even += 1
        print()
        even += 1

def main():
    chessboard = createChessBoard()
    clear()
    printChessboard(chessboard)
    # userInput = kb.getch().decode('utf-8')
    # print(userInput)


if __name__ == "__main__":
    main()