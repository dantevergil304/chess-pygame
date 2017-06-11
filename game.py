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
    while True:
        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(event.pos[0], event.pos[1])
                if game.board.isNotBlank(spotx, spoty):
                    fromX = spotx
                    fromY = spoty
                    picked = True
                elif picked:
                    toX = spotx
                    toY = spoty
                    game.board.move(fromX, fromY, toX, toY)
                    picked = False
        game.board.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

main()
