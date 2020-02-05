import pygame
import os


def load_image(name, screen, color_key=None):
    fullname = os.path.join('sprites', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Turret(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.image = pygame.transform.scale(load_image('Turret.jpg', screen, color_key=(255, 255, 255)),
                                            (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x * 40
        self.rect.y = y * 40
