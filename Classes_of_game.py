import pygame
import os


player_group, all_sprites, obstacles = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
close_doors, all_electricity  = pygame.sprite.Group(), pygame.sprite.Group()
tile_width, tile_height = 0, 0


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Player(pygame.sprite.Sprite):
    image = load_image('player.png')

    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.invent = []

    def update(self, add_x, add_y):
        self.rext.x += add_x
        self.rect.y += add_y
        if pygame.sprite.spritecollideany(self, obstacles):
            self.rect.x -= add_x
            self.rect.y -= add_y


class Item(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image_name, numb):
        super().__init__(all_sprites)
        self.image = load_image(image_name)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.numb = numb

    def update(self, player):
        if pygame.sprite.spritecollideany(self, player_group):
            player.invent.append(self.numb)


class Door(pygame.sprite.Sprite):
    current_image = image = load_image('door')
    open_image = load_image('open_door.png')

    def __init__(self, pos_x, pos_y, numb):
        super().__init__(player_group, all_sprites)
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.is_closed = True
        self.numb = numb

    def update(self):
        if self.is_closed:
            self.current_image = self.image
        else:
            self.current_image = self.open_image
        self.is_closed = not self.is_closed


class Electricity(pygame.sprite.Sprite):
    image = load_image('player.png')

    def __init__(self, pos_x, pos_y, doors):
        super().__init__(player_group, all_sprites)
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.doors = doors

    def update(self):
        for i in self.doors:
            i.update()