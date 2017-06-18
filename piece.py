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


class Piece:

    def __init__(self, Type, color, pos):
        self.Type = Type
        self.color = color
        self.pos = pos
        self.moved = False

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


class Rook(Piece):

    def __init__(self, color, pos):
        Piece.__init__(self, pType.Rook, color, pos)
        self.moves = []
        for i in range(7):
            self.moves.append((0, i + 1))
            self.moves.append((0, -(i + 1)))
            self.moves.append((i + 1, 0))
            self.moves.append((-(i + 1), 0))


class Bishop(Piece):

    def __init__(self, color, pos):
        Piece.__init__(self, pType.Bishop, color, pos)
        self.moves = []
        for i in range(7):
            self.moves.append((-(i + 1), -(i + 1)))
            self.moves.append((i + 1, i + 1))
            self.moves.append((-(i + 1), i + 1))
            self.moves.append((i + 1, -(i + 1)))


class Queen(Piece):

    def __init__(self, color, pos):
        Piece.__init__(self, pType.Queen, color, pos)
        self.moves = []
        for i in range(7):
            self.moves.append((0, i + 1))
            self.moves.append((0, -(i + 1)))
            self.moves.append((i + 1, 0))
            self.moves.append((-(i + 1), 0))
            self.moves.append((-(i + 1), -(i + 1)))
            self.moves.append((i + 1, i + 1))
            self.moves.append((-(i + 1), i + 1))
            self.moves.append((i + 1, -(i + 1)))


class Pawn(Piece):

    def __init__(self, color, pos):
        Piece.__init__(self, pType.Pawn, color, pos)
        if color == pColor.Black:
            self.moves = [(1, 0)]
            self.captures = [(1, -1), (1, 1)]
        else:
            self.moves = [(-1, 0)]
            self.captures = [(-1, -1), (-1, 1)]

    def validCaptures(self):
        moves = []
        for choice in self.captures:
            x = self.pos[0] + choice[0]
            y = self.pos[1] + choice[1]
            if x >= 0 and x < 8 and y >= 0 and y < 8:
                moves.append((x, y))
        return moves
