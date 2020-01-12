import pygame
from ..Button import *


class Window:
    def __init__(self):
        self.sprites = pygame.sprite.Group()
        self.width = 0
        self.height = 0

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
