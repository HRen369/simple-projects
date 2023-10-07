board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

winningRow = [
    ["-","-","-"],
    ["X","X","X"],
    ["-","-","-"]
]

winningCol = [
    ["-","-","X"],
    ["-","-","X"],
    ["-","-","X"]
]


def checkWinning(userLabel):
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

    if board[0][0] == userLabel and board[1][1] == userLabel and board[2][2] == userLabel:
        return True

    return False


def printBoard(userLabel):

    if checkWinning(userLabel):
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(f"{board[row][col]}",end="")
        print()


def main():
    printBoard("X")

if __name__ == "__main__":
    main()