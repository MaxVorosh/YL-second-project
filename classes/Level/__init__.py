import pygame
from ..Floor import *


class Level:
    def __init__(self, level, screen):
        """
        Обрабатывает уровень файлов.
        :param level: название уровня. Папку уровней прописывать нет необходимости.
        :param screen: экран, на котором было открыто меню или другой уровень.
        """
        self.sprites = pygame.sprite.Group()
        self.data = [[i for i in l] for l in open(f"levels\\{level}.txt").read().split("\n")]
        self.screen = screen
        for line in range(len(self.data)):
            for elem in range(len(self.data[line])):
                if self.data[line][elem] == ".":
                    pass
                if self.data[line][elem] == "#":
                    pass  # TODO
                if self.data[line][elem] == "f":
                    self.sprites.add(Floor(elem, line))
                if self.data[line][elem] == "w":
                    self.sprites.add(None)  # Стена.
                    pass  # TODO
                if self.data[line][elem] == "@":
                    self.sprites.add(None)  # Турель.
                    pass  # TODO
        self.run()

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.screen.fill((0, 0, 0))
            self.sprites.draw(self.screen)
            pygame.display.flip()
        pygame.quit()
