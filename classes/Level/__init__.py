import pygame
from ..Platform import *


class Level:
    def __init__(self, screen):
        self.sprites = pygame.sprite.Group()
        self.screen = screen
