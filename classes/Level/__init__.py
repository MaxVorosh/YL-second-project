import pygame
import sys
from ..Floor import *
from ..Hero import *
from ..Door import *
from ..Turret import *
from ..Wall import *
from ..Border import *


flags = {(0, -1): False, # up
        (0, 1): False, # down
        (-1, 0): False, # left
        (0, 1): False} # right


def update_flags(event, val):
    if event.key == pygame.K_UP:
        flags[(0, -1)] = val
    if event.key == pygame.K_DOWN:
        flags[(0, 1)] = val
    if event.key == pygame.K_LEFT:
        flags[(-1, 0)] = val
    if event.key == pygame.K_RIGHT:
        flags[(1, 0)] = val


class Level:
    def __init__(self, level, screen):
        """
        Обрабатывает уровень файлов.
        :param level: название уровня. Папку уровней прописывать нет необходимости.
        :param screen: экран, на котором было открыто меню или другой уровень.
        """
        self.sprites, self.obstacles, self.Hero = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
        self.borders = pygame.sprite.Group()
        self.data = [[i for i in l] for l in open(f"levels\\{level}.txt").read().split("\n")]
        self.screen = screen
        for i in [(0, 0, 640, 0), (0, 0, 0, 480), (0, 480, 640, 480), (640, 0, 640, 480)]:
            self.borders.add(Border(*i, self.borders))
        for line in range(len(self.data)):
            for elem in range(len(self.data[line])):
                # if self.data[line][elem] == ".":
                #     pass
                # Зачем нам просто пустое пространство? Можно всё замостить полом
                if self.data[line][elem] == "#":
                    self.hero = Hero(elem, line)
                    self.sprites.add(Floor(elem, line))
                    self.Hero.add(self.hero)
                if self.data[line][elem] == "f":
                    self.sprites.add(Floor(elem, line))
                if self.data[line][elem] == "w":
                    w = Wall(elem, line)
                    self.sprites.add(w)
                    self.obstacles.add(w)
                if self.data[line][elem] == "@":
                    t = Turret(elem, line)  # Турель.
                    self.sprites.add(t)
                    self.obstacles.add(t)
                if self.data[line][elem] == "d":
                    d = Door(elem, line)
                    self.sprites.add(d)
                    self.obstacles.add(d)
        self.run()

    def exit_Func(self):
        pygame.quit()
        sys.exit()

    def run(self):
        """
        Начало дейсвтия.
        :return: ничего
        """
        run = True
        fps = 120
        clock = pygame.time.Clock()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    update_flags(event, True)
                if event.type == pygame.KEYUP:
                    update_flags(event, False)
            self.screen.fill((0, 0, 0))
            for i in flags.keys():
                if flags[i]:
                    self.hero.update(i[0], i[1], self.obstacles, self.borders)
            self.sprites.draw(self.screen)
            self.Hero.draw(self.screen)
            clock.tick(fps)
            pygame.display.flip()
        self.exit_Func()
