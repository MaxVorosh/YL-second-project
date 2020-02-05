import pygame
from ..Border import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        sheet = pygame.image.load("sprites\\hero.png")  # TODO указать расширение
        self.frames = []
        # columns, rows = None, None  # TODO указать количество фреймов
        columns, rows = 1, 1
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x * 40 + 1, y * 40 + 1)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, add_x, add_y, *groups):
        self.rect.x += add_x
        self.rect.y += add_y
        for group in groups:
            if pygame.sprite.spritecollideany(self, group):
                self.rect.x -= add_x
                self.rect.y -= add_y
                break
