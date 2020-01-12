import pygame
import os


class Button(pygame.sprite.Sprite):
    def __init__(self, window, path):
        super().__init__(window.sprites)
        self.set_image(path)
        self.rect = self.image.get_rect()
        self.func = None

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_image(self, path):
        path = os.path.join("sprites", path)
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

    def set_func(self, func):
        self.func = func

    def check_clicked(self, mouse_pos):
        if mouse_pos[0] >= self.rect.x and mouse_pos[0] <= self.rect.x + self.rect.width and mouse_pos[1] > self.rect.y and mouse_pos[1] < self.rect.y + self.rect.height:
            return True
        else:
            return False

    def clicked(self):
        self.func()
