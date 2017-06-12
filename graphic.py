import pygame
import sys
from pygame.locals import *

TILESIZE = 64

WINDOWWIDTH = 512
WINDOWHEIGHT = 512

FPS = 15

FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


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
