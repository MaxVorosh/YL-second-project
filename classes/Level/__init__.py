import pygame
import sys
from ..Floor import *
from ..Hero import *
from ..Door import *
from ..Turret import *
from ..Wall import *
from ..Border import *
from ..Bullet import *
from ..Congratulations import *


flags = {(0, -1): False, # up
        (0, 1): False, # down
        (-1, 0): False, # left
        (0, 1): False} # right


def update_flags(event, val):
    if event.key == pygame.K_UP:
        flags[(0, -2)] = val
    if event.key == pygame.K_DOWN:
        flags[(0, 2)] = val
    if event.key == pygame.K_LEFT:
        flags[(-2, 0)] = val
    if event.key == pygame.K_RIGHT:
        flags[(2, 0)] = val


class Level:
    def __init__(self, level, screen):
        """
        Обрабатывает уровень файлов.
        :param level: название уровня. Папку уровней прописывать нет необходимости.
        :param screen: экран, на котором было открыто меню или другой уровень.
        """
        self.sprites, self.walls, self.Hero = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
        self.borders, self.door, self.danger = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
        self.turrets, self.bullets = pygame.sprite.Group(), pygame.sprite.Group()
        self.data = [[i for i in l] for l in open(f"levels\\{level}.txt").read().split("\n")]
        self.screen = screen
        self.level = int(level)
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
                if self.data[line][elem] == ".":
                    self.sprites.add(Floor(elem, line))
                if self.data[line][elem] == "w":
                    w = Wall(elem, line)
                    self.sprites.add(w)
                    self.walls.add(w)
                if self.data[line][elem] == "@":
                    t = Turret(elem, line)  # Турель.
                    self.sprites.add(t)
                    self.danger.add(t)
                    self.turrets.add(t)
                if self.data[line][elem] == "d":
                    d = Door(elem, line, self.door)
                    self.sprites.add(d)
                    self.door.add(d)
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
        fps = 60
        timer = 27
        vb = 3
        pygame.time.set_timer(timer, 1000)
        clock = pygame.time.Clock()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    update_flags(event, True)
                if event.type == pygame.KEYUP:
                    update_flags(event, False)
                if event.type == timer:
                    for turret in self.turrets:
                        x, y = turret.rect.x, turret.rect.y
                        b_up, b_left, b_down, b_right = (Bullet(x + 15, y - 5, 0, -vb), Bullet(x - 5, y + 15, -vb, 0),
                                                         Bullet(x + 15, y + 45, 0, vb), Bullet(x + 45, y + 15, vb, 0))
                        for bul in [b_up, b_left, b_right, b_down]:
                            self.sprites.add(bul)
                            self.danger.add(bul)
                            self.bullets.add(bul)
            self.screen.fill((0, 0, 0))
            for i in flags.keys():
                if flags[i]:
                    self.hero.update(i[0], i[1], self.walls, self.borders)
            for bul in self.bullets:
                bul.update(self.walls, self.borders, self.turrets)
            if pygame.sprite.spritecollideany(self.hero, self.door):
                if self.level < 5:
                    Level(str(self.level + 1), self.screen)
                else:
                    cong = Congratulations()
                    run = False
            if pygame.sprite.spritecollideany(self.hero, self.danger):
                Level(str(self.level), self.screen)
            self.sprites.draw(self.screen)
            self.Hero.draw(self.screen)
            clock.tick(fps)
            pygame.display.flip()
        self.exit_Func()
