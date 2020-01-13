from ..Window import *
from ..Button import *
from ..TestingLevel import *
import sys


class Menu(Window):
    def __init__(self):
        super().__init__()
        self.ui()
        self.run()

    def ui(self):
        self.resize(640, 480)
        self.exit = Button(self, "PNG\\White\\2x\\exit.png")
        self.exit.resize(80, 80)
        self.exit.move(560, 0)
        self.exit.set_func(self.exitFunc)
        self.start = Button(self, "PNG\\White\\2x\\buttonStart.png")
        self.start.resize(100, 100)
        self.start.move(270, 190)
        self.start.set_func(self.startFunc)
        self.set_background("bg.jpg")

    def startFunc(self):
        TestingLevel(self.screen)
        self.exitFunc()

    def exitFunc(self):
        pygame.quit()
        sys.exit()

    def run(self):
        pygame.init()
        pygame.mixer.music.load("sprites\\Music\\menu.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click(event.pos)
            self.screen.fill((0, 0, 0))
            if self.background:
                self.screen.blit(self.background, (0, 0))
            self.sprites.draw(self.screen)
            pygame.display.flip()
        pygame.quit()
