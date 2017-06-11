from piece import *
from graphic import *

WHITE = (255, 255, 255)
GREY = (119, 136, 153)


class Board:

    def __init__(self):
        self.board = []

    """def initBoard(self):
        self.board.append(['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'])
        self.board.append(['p'] * 8)
        for i in range(4):
            self.board.append(['.'] * 8)
        self.board.append(['P'] * 8)
        self.board.append(['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'])"""

    def setPiece(self, Type, color, x, y):
        if Type == Type.King:
            self.board[x][y] = King(color, (x, y))
        elif Type == Type.Knight:
            self.board[x][y] = Knight(color, (x, y))

    def initBoard(self):
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append('.')
        self.setPiece(pType.King, pColor.White, 0, 4)
        self.setPiece(pType.Knight, pColor.White, 0, 6)

    def isNotBlank(self, x, y):
        return self.board[x][y] != '.'

    def draw(self):
        for i in range(8):
            for j in range(8):
                color = GREY
                if (i + j) % 2 == 0:
                    color = WHITE
                drawTile(i, j, color)
                if self.board[i][j] != '.':
                    if self.board[i][j].Type == pType.King:
                        displayImage(i, j, './white/king.png')
                    elif self.board[i][j].Type == pType.Knight:
                        displayImage(i, j, './white/knight.png')

    def move(self, from_x, from_y, to_x, to_y):
        if (to_x, to_y) in self.board[from_x][from_y].validMoves():
            self.board[to_x][to_y] = self.board[from_x][from_y]
            self.board[to_x][to_y].pos = (to_x, to_y)
            self.board[from_x][from_y] = '.'
