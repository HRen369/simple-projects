import os, random
import msvcrt as kb
from chessPieces import createBlackPawn,createBlackRook,createBlackBishop,createBlackKnight,createBlackQueen,createBlackKing
from chessPieces import Empty

BG = "\033[47m"
ENDC = '\033[0m'
clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')


def createChessBoard():
    blackPieces = [createBlackRook(), createBlackKnight(), createBlackBishop(),createBlackQueen(),createBlackKing(),createBlackBishop(), createBlackKnight(),createBlackRook()]
    blackPiecesPawns = [createBlackPawn() for i in range(8)]
    return [blackPieces, blackPiecesPawns,[Empty() for i in range(8)],[Empty() for i in range(8)]]

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