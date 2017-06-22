from enum import Enum


class pType(Enum):
    King = 1
    Queen = 2
    Rook = 3
    Knight = 4
    Bishop = 5
    Pawn = 6


class pColor(Enum):
    White = 1
    Black = 2

SQUARETABLE = [
    # King end game
    [[-50, -30, -30, -30, -30, -30, -30, -50],
    [-30, -30,  0,  0,  0,  0, -30, -30],
    [-30, -10, 20, 30, 30, 20, -10, -30],
    [-30, -10, 30, 40, 40, 30, -10, -30],
    [-30, -10, 30, 40, 40, 30, -10, -30],
    [-30, -10, 20, 30, 30, 20, -10, -30],
    [-30, -20, -10,  0,  0, -10, -20, -30],
    [-50, -40, -30, -20, -20, -30, -40, -50]],
    # King early game
    [[20, 30, 10,  0,  0, 10, 30, 20],
     [20, 20,  0,  0,  0,  0, 20, 20],
     [-10, -20, -20, -20, -20, -20, -20, -10],
     [-20, -30, -30, -40, -40, -30, -30, -20],
     [-30, -40, -40, -50, -50, -40, -40, -30],
     [-30, -40, -40, -50, -50, -40, -40, -30],
     [-30, -40, -40, -50, -50, -40, -40, -30],
     [-30, -40, -40, -50, -50, -40, -40, -30]],
    # Queen
    [[-20, -10, -10, -5, -5, -10, -10, -20],
     [-10,  0,  5,  0,  0,  0,  0, -10],
     [-10,  5,  5,  5,  5,  5,  0, -10],
     [0,  0,  5,  5,  5,  5,  0, -5],
     [-5,  0,  5,  5,  5,  5,  0, -5],
     [-10,  0,  5,  5,  5,  5,  0, -10],
     [-10,  0,  0,  0,  0,  0,  0, -10],
     [-20, -10, -10, -5, -5, -10, -10, -20]],
    # Rook
    [[0,  0,  0,  5,  5,  0,  0,  0],
     [-5,  0,  0,  0,  0,  0,  0, -5],
     [-5,  0,  0,  0,  0,  0,  0, -5],
     [-5,  0,  0,  0,  0,  0,  0, -5],
     [-5,  0,  0,  0,  0,  0,  0, -5],
     [-5,  0,  0,  0,  0,  0,  0, -5],
     [5, 10, 10, 10, 10, 10, 10,  5],
     [0,  0,  0,  0,  0,  0,  0,  0]],
    # Knight
    [[-50, -40, -30, -30, -30, -30, -40, -50],
    [-40, -20,  0,  5,  5,  0, -20, -40],
    [-30,  5, 10, 15, 15, 10,  5, -30],
    [-30,  0, 15, 20, 20, 15,  0, -30],
    [-30,  5, 15, 20, 20, 15,  5, -30],
    [-30,  0, 10, 15, 15, 10,  0, -30],
    [-40, -20,  0,  0,  0,  0, -20, -40],
    [-50, -40, -30, -30, -30, -30, -40, -50]],
    # Bishop
    [[-20, -10, -10, -10, -10, -10, -10, -20],
    [-10,  5,  0,  0,  0,  0,  5, -10],
    [-10, 10, 10, 10, 10, 10, 10, -10],
    [-10,  0, 10, 10, 10, 10,  0, -10],
    [-10,  5,  5, 10, 10,  5,  5, -10],
    [-10,  0,  5, 10, 10,  5,  0, -10],
    [-10,  0,  0,  0,  0,  0,  0, -10],
    [-20, -10, -10, -10, -10, -10, -10, -20]],
    # Pawn
    [[0,  0,  0,  0,  0,  0,  0,  0],
    [5, 10, 10, -20, -20, 10, 10,  5],
    [5, -5, -10,  0,  0, -10, -5,  5],
    [0,  0,  0, 20, 20,  0,  0,  0],
    [5,  5, 10, 25, 25, 10,  5,  5],
    [10, 10, 20, 30, 30, 20, 10, 10],
    [50, 50, 50, 50, 50, 50, 50, 50],
    [0,  0,  0,  0,  0,  0,  0,  0]]
]

class Piece:

    def __init__(self, Type, color, pos):
        self.Type = Type
        self.color = color
        self.pos = pos
        self.moved = False
        self.value = 0

    def validMoves(self):
        moves = []
        for choice in self.moves:
            x = self.pos[0] + choice[0]
            y = self.pos[1] + choice[1]
            if x >= 0 and x < 8 and y >= 0 and y < 8:
                moves.append((x, y))
        return moves


class King(Piece):

    def __init__(self, color, pos):
        Piece.__init__(self, pType.King, color, pos)
        self.moves = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                      (1, 0), (-1, 1), (0, 1), (1, 1)]
        self.castling = [(0, -2), (0, 2)]
        self.value = 20000

    def validCastling(self):
        moves = []
        for choice in self.castling:
            x = self.pos[0] + choice[0]
            y = self.pos[1] + choice[1]
            if x >= 0 and x < 8 and y >= 0 and y < 8:
                moves.append((x, y))
        return moves


class Knight(Piece):

    def __init__(self, color, pos):
        Piece.__init__(self, pType.Knight, color, pos)
        self.moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
                      (1, 2), (2, 1), (2, -1), (1, -2)]
        self.value = 320


class Rook(Piece):

    def __init__(self, color, pos):
        Piece.__init__(self, pType.Rook, color, pos)
        self.moves = []
        for i in range(7):
            self.moves.append((0, i + 1))
            self.moves.append((0, -(i + 1)))
            self.moves.append((i + 1, 0))
            self.moves.append((-(i + 1), 0))
        self.value = 500


class Bishop(Piece):

    def __init__(self, color, pos):
        Piece.__init__(self, pType.Bishop, color, pos)
        self.moves = []
        for i in range(7):
            self.moves.append((-(i + 1), -(i + 1)))
            self.moves.append((i + 1, i + 1))
            self.moves.append((-(i + 1), i + 1))
            self.moves.append((i + 1, -(i + 1)))
        self.value = 330


class Queen(Piece):

    def __init__(self, color, pos):
        Piece.__init__(self, pType.Queen, color, pos)
        self.moves = []
        for i in range(6, -1, -1):
            self.moves.append((0, i + 1))
            self.moves.append((0, -(i + 1)))
            self.moves.append((i + 1, 0))
            self.moves.append((-(i + 1), 0))
            self.moves.append((-(i + 1), -(i + 1)))
            self.moves.append((i + 1, i + 1))
            self.moves.append((-(i + 1), i + 1))
            self.moves.append((i + 1, -(i + 1)))
        self.value = 900


class Pawn(Piece):

    def __init__(self, color, pos):
        Piece.__init__(self, pType.Pawn, color, pos)
        if color == pColor.Black:
            self.moves = [(1, 0)]
            self.captures = [(1, -1), (1, 1)]
        else:
            self.moves = [(-1, 0)]
            self.captures = [(-1, -1), (-1, 1)]
        self.value = 100

    def validCaptures(self):
        moves = []
        for choice in self.captures:
            x = self.pos[0] + choice[0]
            y = self.pos[1] + choice[1]
            if x >= 0 and x < 8 and y >= 0 and y < 8:
                moves.append((x, y))
        return moves

