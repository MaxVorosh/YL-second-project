import pygame


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprites\\floor.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pass  # TODO Спрайт добавить.
