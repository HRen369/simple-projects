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
def WhiteKing():
    return King("♔")

def WhiteQueen():
    return Queen("♙")

def WhiteRook():
    return Rook("♖")

def WhiteBishop():
    return Bishop("♗")

def WhiteKnight():
    return Knight("♘")

def WhitePawn():
    return Pawn("♙")


# Black Pieces
def BlackKing():
    return King("♚")

def BlackQueen():
    return Queen("♚")

def BlackRook():
    return Rook("♜")

def BlackBishop():
    return Bishop("♝")

def BlackKnight():
    return Knight("♞")

def BlackPawn():
    return Pawn("♟︎")


