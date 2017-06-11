import pygame
import sys
import random
from pygame.locals import *
from enum import Enum
import time

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

FPS = 15

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (119, 136, 153)


class Type(Enum):
    King = 1
    Queen = 2
    Rook = 3
    Knight = 4
    Bishop = 5
    Pawn = 6


class Color(Enum):
    White = 1
    Black = 2


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
            self.board[x][y] = King((x, y), color)

    def setBlank(self, x, y):
        self.board[x][y] = '.'

    def initBoard(self):
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append('.')
        self.setPiece(Type.King, Color.White, 0, 4)

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
                    if self.board[i][j].Type == Type.King:
                        displayImage(i, j, './black/king.png')

    def move(self, from_x, from_y, to_x, to_y):
        print('Valid Moves: ', self.board[from_x][from_y].validMoves())
        if (to_x, to_y) in self.board[from_x][from_y].validMoves():
            self.board[to_x][to_y] = self.board[from_x][from_y]
            self.board[to_x][to_y].pos = (to_x, to_y)
            self.board[from_x][from_y] = '.'


class King:

    def __init__(self, pos, color):
        self.Type = Type.King
        self.color = color
        self.pos = pos

    def validMoves(self):
        moves = []
        choices = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                   (1, 0), (-1, 1), (0, 1), (1, 1)]
        for choice in choices:
            x = self.pos[0] + choice[0]
            y = self.pos[1] + choice[1]
            if x >= 0 and x < 8 and y >= 0 and y < 8:
                moves.append((x, y))
        return moves


class Game:

    def __init__(self):
        self.board = Board()


TILESIZE = 50


def getLeftTopOfTile(tileX, tileY):
    left = tileY * TILESIZE
    top = tileX * TILESIZE
    return (left, top)


def drawTile(tilex, tiley, color):
    left, top = getLeftTopOfTile(tilex, tiley)
    pygame.draw.rect(DISPLAYSURF, color, (left, top, TILESIZE, TILESIZE))


def displayImage(tilex, tiley, path):
    left, top = getLeftTopOfTile(tilex, tiley)
    image = pygame.image.load(path)
    rect = image.get_rect()
    rect.topleft = (left, top)
    DISPLAYSURF.blit(image, rect)


def getSpotClicked(x, y):
    for tileX in range(8):
        for tileY in range(8):
            left, top = getLeftTopOfTile(tileX, tileY)
            tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()


def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Slide Puzzle')
    game = Game()
    game.board.initBoard()
    game.board.draw()
    pygame.display.update()
    picked = False
    while True:
        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(event.pos[0], event.pos[1])
                if game.board.isNotBlank(spotx, spoty):
                    fromX = spotx
                    fromY = spoty
                    print('From x: ', fromX)
                    print('From y: ', fromY)
                    picked = True
                elif picked:
                    toX = spotx
                    toY = spoty
                    print('To x: ', toX)
                    print('To y: ', toY)
                    game.board.move(fromX, fromY, toX, toY)
                    picked = False
        game.board.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

main()
