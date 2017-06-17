from board import *


class Game:

    def __init__(self):
        self.board = Board()


def main():
    pygame.init()
    pygame.display.set_caption('Slide Puzzle')
    game = Game()
    game.board.initBoard()
    game.board.draw()
    pygame.display.update()
    picked = False
    promote = False
    while True:
        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(event.pos[0], event.pos[1])
                if promote is True:
                    print('promoting...')
                    if button[0].collidepoint(event.pos):
                        promote = False
                        game.board.promote(toX, toY, pType.Queen)
                        deletePopup(515, 10)
                    if button[1].collidepoint(event.pos):
                        promote = False
                        game.board.promote(toX, toY, pType.Knight)
                        deletePopup(515, 10)
                    if button[2].collidepoint(event.pos):
                        promote = False
                        game.board.promote(toX, toY, pType.Rook)
                        deletePopup(515, 10)
                    if button[3].collidepoint(event.pos):
                        promote = False
                        game.board.promote(toX, toY, pType.Bishop)
                        deletePopup(515, 10)

                elif (spotx, spoty) != (None, None):
                    if game.board.isNotBlank(spotx, spoty) and not picked:
                        fromX = spotx
                        fromY = spoty
                        Type, color = game.board.getTypeAndColor(fromX, fromY)
                        picked = True
                    elif picked:
                        toX = spotx
                        toY = spoty
                        game.board.move(fromX, fromY, toX, toY)
                        if Type == pType.Pawn:
                            if (color == pColor.White and toX == 0)\
                                    or (color == pColor.Black and toX == 7):
                                promote = True
                                button = makePopup(522, 15)
                        picked = False
        game.board.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

main()
