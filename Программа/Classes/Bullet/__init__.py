import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("sprites\\bullet.jpg"), (5, 5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy

    def update(self, *groups):
        self.rect.x += self.vx
        self.rect.y += self.vy
        for group in groups:
            if pygame.sprite.spritecollideany(self, group):
                self.kill()
                break
