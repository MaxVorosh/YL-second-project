import pygame
import os


class Button(pygame.sprite.Sprite):
    def __init__(self, window, path):
        super().__init__(window.sprites)
        self.set_image(path)
        self.rect = self.image.get_rect()
        self.enabled = True
        self.window = window
        self.width = 0
        self.height = 0

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_image(self, path):
        path = os.path.join("sprites", path)
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
