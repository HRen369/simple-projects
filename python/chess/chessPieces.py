STAY = (-9,-9)

class Empty:
    def __init__(self):
        self.c = " "

    def valid():
        return True

class King:
    def __init__(self,c):
        self.c = c
        self.loc = STAY

    def valid():
        return False

class Queen:
    def __init__(self,c):
        self.c = c
        self.loc = STAY

    def valid():
        return False

class Rook:
    def __init__(self,c):
        self.c = c
        self.loc = STAY

    def valid():
        return False

class Bishop:
    def __init__(self,c):
        self.c = c
        self.loc = STAY

    def valid():
        return False

class Knight:
    def __init__(self,c):
        self.c = c
        self.loc = STAY

    def valid():
        return False

class Pawn:
    def __init__(self,c):
        self.c = c
        self.loc = STAY

    def valid():
        return False


# Creat Pieces Methods
def createWhiteKing():
    return King("♔")

def createWhiteQueen():
    return Queen("♙")

def createWhitePawn():
    return Rook("♖")

def createWhitePawn():
    return Bishop("♗")

def createWhitePawn():
    return Knight("♘")

def createWhitePawn():
    return Pawn("♙")


# Black Pieces
def createBlackKing():
    return King("♚")

def createBlackQueen():
    return Queen("♚")

def createBlackRook():
    return Rook("♜")

def createBlackBishop():
    return Bishop("♝")

def createBlackKnight():
    return Knight("♞")

def createBlackPawn():
    return Pawn("♟︎")


