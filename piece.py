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

    def validMoves(self):
        moves = []
        for choice in self.choices:
            x = self.pos[0] + choice[0]
            y = self.pos[1] + choice[1]
            if x >= 0 and x < 8 and y >= 0 and y < 8:
                moves.append((x, y))
        return moves


class King(Piece):

    def __init__(self, color, pos):
        Piece.__init__(self, pType.King, color, pos)
        self.choices = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                        (1, 0), (-1, 1), (0, 1), (1, 1)]


class Knight(Piece):

    def __init__(self, color, pos):
        Piece.__init__(self, pType.Knight, color, pos)
        self.choices = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
                        (1, 2), (2, 1), (2, -1), (1, -2)]