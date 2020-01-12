from ..Window import *
from ..Button import *


class Menu(Window):
    def __init__(self):
        super().__init__()
        self.ui()
        self.run()

    def ui(self):
        self.resize(640, 480)
        self.button = Button(self, "res.png")
        self.button.resize(40, 40)
        self.button.move(600, 0)

    def run(self):
        pygame.init()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.screen.fill((0, 0, 0))
            self.sprites.draw(self.screen)
            pygame.display.flip()
        pygame.quit()
