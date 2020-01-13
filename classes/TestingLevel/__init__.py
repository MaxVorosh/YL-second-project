from ..Level import *


class TestingLevel(Level):
    def __init__(self, screen):
        super().__init__(screen)
        self.world()
        self.run()

    def world(self):
        side = 40
        for x in range(20):
            for y in range(3):
                self.sprites.add(Platform(x * side, y * side, 0, side, "asphalt.jpg"))

    def run(self):
        pygame.init()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.screen.fill((0, 0, 0))
            self.sprites.update()
            self.sprites.draw(self.screen)
            pygame.display.flip()
        pygame.quit()
