import pygame


class Turret(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('sprites\\turret.jpg'), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x * 40
        self.rect.y = y * 40
