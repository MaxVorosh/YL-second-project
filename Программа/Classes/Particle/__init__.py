import pygame
from random import choice
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


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    # fire = [load_image("one_confetti.png", screen), load_image("second_confetti.png", screen)]
    # for scale in (5, 10, 20):
    #     fire.append(pygame.transform.scale(fire[choice((0, 1))], (scale, scale)))

    def __init__(self, pos, dx, dy, group, screen):
        super().__init__(group)

        self.fire = [load_image("one_confetti.png", screen, color_key=(255, 255, 255)),
                     load_image("second_confetti.png", screen, color_key=(255, 255, 255))]
        for scale in (30, 40, 50):
            self.fire.append(pygame.transform.scale(self.fire[1], (scale, scale)))
        for scale in (5, 10, 20):
            self.fire.append(pygame.transform.scale(self.fire[0], (scale, scale)))

        self.image = choice(self.fire[2:])
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость - это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой
        self.gravity = 0.25

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect((0, 0, 640, 480)):
            self.kill()
