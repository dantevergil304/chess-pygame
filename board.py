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
        if Type == pType.King:
            self.board[x][y] = King(color, (x, y))
        elif Type == pType.Knight:
            self.board[x][y] = Knight(color, (x, y))
        elif Type == pType.Rook:
            self.board[x][y] = Rook(color, (x, y))
        elif Type == pType.Bishop:
            self.board[x][y] = Bishop(color, (x, y))
        elif Type == pType.Queen:
            self.board[x][y] = Queen(color, (x, y))
        elif Type == pType.Pawn:
            self.board[x][y] = Pawn(color, (x, y))

    def initBoard(self):
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append('.')
        # Black Pieces
        self.setPiece(pType.Rook, pColor.Black, 0, 0)
        self.setPiece(pType.Knight, pColor.Black, 0, 1)
        self.setPiece(pType.Bishop, pColor.Black, 0, 2)
        self.setPiece(pType.Queen, pColor.Black, 0, 3)
        self.setPiece(pType.King, pColor.Black, 0, 4)
        self.setPiece(pType.Bishop, pColor.Black, 0, 5)
        self.setPiece(pType.Knight, pColor.Black, 0, 6)
        self.setPiece(pType.Rook, pColor.Black, 0, 7)
        for j in range(8):
            self.setPiece(pType.Pawn, pColor.Black, 1, j)
        # White Pieces
        self.setPiece(pType.Rook, pColor.White, 7, 0)
        self.setPiece(pType.Knight, pColor.White, 7, 1)
        self.setPiece(pType.Bishop, pColor.White, 7, 2)
        self.setPiece(pType.Queen, pColor.White, 7, 3)
        self.setPiece(pType.King, pColor.White, 7, 4)
        self.setPiece(pType.Bishop, pColor.White, 7, 5)
        self.setPiece(pType.Knight, pColor.White, 7, 6)
        self.setPiece(pType.Rook, pColor.White, 7, 7)
        for j in range(8):
            self.setPiece(pType.Pawn, pColor.White, 6, j)

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
                    c = 'black'
                    if self.board[i][j].color == pColor.White:
                        c = 'white'
                    if self.board[i][j].Type == pType.King:
                        displayImage(i, j, './' + c + '/King.png')
                    elif self.board[i][j].Type == pType.Knight:
                        displayImage(i, j, './' + c + '/Knight.png')
                    elif self.board[i][j].Type == pType.Rook:
                        displayImage(i, j, './' + c + '/Rook.png')
                    elif self.board[i][j].Type == pType.Bishop:
                        displayImage(i, j, './' + c + '/Bishop.png')
                    elif self.board[i][j].Type == pType.Queen:
                        displayImage(i, j, './' + c + '/Queen.png')
                    elif self.board[i][j].Type == pType.Pawn:
                        displayImage(i, j, './' + c + '/Pawn.png')

    def move(self, from_x, from_y, to_x, to_y):
        if (to_x, to_y) in self.board[from_x][from_y].validMoves():
            self.board[to_x][to_y] = self.board[from_x][from_y]
            self.board[to_x][to_y].pos = (to_x, to_y)
            self.board[from_x][from_y] = '.'
