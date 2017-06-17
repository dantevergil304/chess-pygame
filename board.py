from piece import *
from graphic import *

WHITE = (255, 255, 255)
GREY = (119, 136, 153)


class Board:

    def __init__(self):
        self.board = []
        self.previousMove = None

    """def initBoard(self):
        self.board.append(['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'])
        self.board.append(['p'] * 8)
        for i in range(4):
            self.board.append(['.'] * 8)
        self.board.append(['P'] * 8)
        self.board.append(['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'])"""

    def getTypeAndColor(self, x, y):
        return (self.board[x][y].Type, self.board[x][y].color)

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

    def isCollide(self, from_x, from_y, to_x, to_y):
        if self.board[from_x][from_y].Type != pType.Knight:
            dx = to_x - from_x
            dy = to_y - from_y
            if dx != 0:
                dx = dx / abs(dx)
            if dy != 0:
                dy = dy / abs(dy)
            x = int(from_x + dx)
            y = int(from_y + dy)
            while x != to_x or y != to_y:
                if self.board[x][y] != '.':
                    print(True)
                    return True
                x += int(dx)
                y += int(dy)
        print(False)
        return False

    def moveToAlly(self, from_x, from_y, to_x, to_y):
        if self.board[to_x][to_y] != '.':
            if self.board[to_x][to_y].color == self.board[from_x][from_y].color:
                return True
        return False

    def promote(self, x, y, Type):
        self.setPiece(Type, self.board[x][y].color, x, y)

    def makeMove(self, from_x, from_y, to_x, to_y):
        self.board[to_x][to_y] = self.board[from_x][from_y]
        self.board[to_x][to_y].pos = (to_x, to_y)
        self.board[to_x][to_y].moved = True
        self.board[from_x][from_y] = '.'
        self.previousMove = (
            self.board[to_x][to_y].Type, from_x, from_y, to_x, to_y)

    def move(self, from_x, from_y, to_x, to_y):
        if self.isCollide(from_x, from_y, to_x, to_y):
            return
        if self.moveToAlly(from_x, from_y, to_x, to_y):
            return

        cellFrom = self.board[from_x][from_y]
        cellTo = self.board[to_x][to_y]
        validMoves = cellFrom.validMoves()
        # Pawn pieces
        if cellFrom.Type == pType.Pawn:
            # first move
            validCaptures = cellFrom.validCaptures()
            if from_x == 1:
                validMoves.append((from_x + 2, from_y))
            if from_x == 6:
                validMoves.append((from_x - 2, from_y))
            # move
            if cellTo == '.' and (to_x, to_y) in validMoves:
                self.makeMove(from_x, from_y, to_x, to_y)
            # capture and en passant capture
            elif (to_x, to_y) in validCaptures:
                if cellTo != '.':
                    self.makeMove(from_x, from_y, to_x, to_y)
                elif cellFrom.color == pColor.White and from_x == 3:
                    if self.previousMove == (pType.Pawn, to_x - 1, to_y, to_x + 1, to_y):
                        self.makeMove(from_x, from_y, to_x, to_y)
                        self.board[to_x + 1][to_y] = '.'
                elif cellFrom.color == pColor.Black and from_x == 4:
                    if self.previousMove == (pType.Pawn, to_x + 1, to_y, to_x - 1, to_y):
                        self.makeMove(from_x, from_y, to_x, to_y)
                        self.board[to_x - 1][to_y] = '.'
        # King pieces
        elif cellFrom.Type == pType.King:
            validCastling = cellFrom.validCastling()
            # Castling
            if (to_x, to_y) in validCastling and cellFrom.moved is False:
                if to_y == from_y + 2 and self.board[to_x][to_y + 1].moved is False:
                    self.makeMove(from_x, from_y, to_x, to_y)
                    self.makeMove(to_x, to_y + 1, from_x, from_y + 1)
                if to_y == from_y - 2 and self.board[to_x][to_y - 2].moved is False:
                    self.makeMove(from_x, from_y, to_x, to_y)
                    self.makeMove(to_x, to_y - 2, from_x, from_y - 1)
            elif (to_x, to_y) in validMoves:
                self.makeMove(from_x, from_y, to_x, to_y)
        # Other pieces
        elif (to_x, to_y) in validMoves:
            self.makeMove(from_x, from_y, to_x, to_y)
