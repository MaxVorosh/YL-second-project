import pygame


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("sprites\\floor.jpg"), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x * 30
        self.rect.y = y * 30
