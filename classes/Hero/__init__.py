import pygame
from ..Border import *
import os


def load(name, colorkey=None):
    fullname = os.path.join('sprites', 'hero', f"{name}.png")
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.count = 0
        self.right = [load(f"r_{num}", -1) for num in range(1, 5)]
        self.left = [load(f"l_{num}", -1) for num in range(1, 5)]
        self.cur_right = 0
        self.cur_left = 0
        self.image = pygame.transform.scale(load("r_1", -1), (20, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x * 40
        self.rect.y = y * 40

    def update(self, add_x, add_y, *groups):
        self.count = (self.count + 1) % 4
        self.rect.x += add_x
        self.rect.y += add_y
        if self.count == 3:
            if add_x <= 0 and add_y <= 0:
                self.cur_right = 0
            if add_x >= 0 and add_y >= 0:
                self.cur_left = 0
            if add_x == 0 and add_y == 0:
                x = self.rect.x
                y = self.rect.y
                self.image = pygame.transform.scale(self.right[0], (20, 40))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
            if add_x > 0 or add_y > 0:
                x = self.rect.x
                y = self.rect.y
                self.image = pygame.transform.scale(self.right[self.cur_right], (20, 40))
                self.cur_right = (self.cur_right + 1) % len(self.right)
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
            if add_y < 0 or add_x < 0:
                x = self.rect.x
                y = self.rect.y
                self.image = pygame.transform.scale(self.left[self.cur_left], (20, 40))
                self.cur_left = (self.cur_left + 1) % len(self.left)
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
        for group in groups:
            if pygame.sprite.spritecollideany(self, group):
                self.rect.x -= add_x
                self.rect.y -= add_y
                break
