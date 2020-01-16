import pygame


class Level:
    def __init__(self, name, screen):
        data = [line for line in open(f"levels\\{name}")]
        for line in range(len(data)):
            for x in range(len(data[line])):
                self.draw(data[line][x])
        self.sprites = pygame.sprite.Group()
        self.screen = screen
        self.run()

    def draw(self, elem):
        pass

    def render(self):
        self.sprites.draw(self.screen)

    def run(self):
        pygame.init()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.render()
            pygame.display.flip()
        pygame.quit()
