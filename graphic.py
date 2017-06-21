import pygame
import sys
from pygame.locals import *

TILESIZE = 64
PROMOTESIZE = 32
PROMOTEDISTANCE = 47
RADIUS = 23

WINDOWWIDTH = 512
WINDOWHEIGHT = 512

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
IVORY = (176, 196, 222)

FPS = 15

FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
DISPLAYSURF.fill(BLACK)


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


def makeText(text, color, bgcolor, top, left):
    font = pygame.font.Font('freesansbold.ttf', 20)
    textSurf = font.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (left, top)
    return (textSurf, textRect)


def makeImage(image, top, left):
    image = pygame.image.load(image)
    rect = image.get_rect()
    rect.topleft = (left, top)
    return (image, rect)


def drawButton(image, x, y):
    circleImg, circleRect = makeImage('./promote/circle.png', y - 5, x - 6)
    image, rect = makeImage(image, y, x)
    DISPLAYSURF.blit(circleImg, circleRect)
    DISPLAYSURF.blit(image, rect)
    return rect


def makePopup(x, y):
    paths = ['./texture/promote/queen.png',
             './texture/promote/knight.png',
             './texture/promote/rook.png',
             './texture/promote/bishop.png']
    button = []
    for path in paths:
        button.append(drawButton(path, x, y))
        x += PROMOTEDISTANCE
    return button


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
