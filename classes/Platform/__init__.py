import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, z, side, texture):
        super().__init__()
        self.image = pygame.image.load(f"sprites\\{texture}")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.z = z
        self.image = pygame.transform.scale(self.image, (side, side))
