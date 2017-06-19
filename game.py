from board import *
import time


class Game:

    def __init__(self):
        self.board = Board()
        self.picked = False
        self.promote = False
        self.now = 1
        self.previous = 2

    def checkClickButton(self, button, eventPos, Type, x, y):
        if button.collidepoint(eventPos):
            self.promote = False
            self.board.promote(x, y, Type)

    def run(self):
        pygame.init()
        pygame.display.set_caption('Chess Game Against AI')

        self.board.initBoard()
        self.board.draw()
        pygame.display.update()
        while True:
            checkForQuit()
            self.now = 3 - self.previous
            if self.now == 2 and self.promote is False:
                nextMove = self.board.ALPHA_BETA_SEARCH(-1000000, 1000000)
                self.board.copyBoard(nextMove.getBoard())
                self.previous = 3 - self.previous
                continue
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    spotx, spoty = getSpotClicked(event.pos[0], event.pos[1])
                    if self.promote is True:
                        self.checkClickButton(
                            button[0], event.pos, pType.Queen, toX, toY)
                        self.checkClickButton(
                            button[1], event.pos, pType.Knight, toX, toY)
                        self.checkClickButton(
                            button[2], event.pos, pType.Rook, toX, toY)
                        self.checkClickButton(
                            button[3], event.pos, pType.Bishop, toX, toY)
                    elif (spotx, spoty) != (None, None):
                        if self.board.isNotBlank(spotx, spoty) and not self.picked:
                            fromX = spotx
                            fromY = spoty
                            Type, color = self.board.getTypeAndColor(
                                fromX, fromY)
                            if self.now == 1 and color == pColor.Black\
                               or self.now == 2 and color == pColor.White:
                                continue
                            self.picked = True
                        elif self.picked:
                            toX = spotx
                            toY = spoty
                            success = self.board.move(fromX, fromY, toX, toY)
                            if Type == pType.Pawn:
                                if (color == pColor.White and toX == 0)\
                                   or (color == pColor.Black and toX == 7):
                                    self.promote = True
                            if success:
                                self.previous = 3 - self.previous
                                self.picked = False

                            """if success:
                                if color == pColor.White:
                                    c = pColor.Black
                                if color == pColor.Black:
                                    c = pColor.White
                                for successor in self.board.getSuccessors(c):
                                    successor.draw()
                                    pygame.display.update()
                                    time.sleep(0.3)"""

            self.board.draw()
            if self.promote is True:
                button = makePopup(169, 240)
            pygame.display.update()
            FPSCLOCK.tick(FPS)

game = Game()
game.run()
