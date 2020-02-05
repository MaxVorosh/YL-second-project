from ..Button import *
from ..Window import *
from ..Particle import *
import sys
import pygame
from random import choice


Particles = pygame.sprite.Group()


def make_fon(screen, intro_text):
    fon = pygame.transform.scale(load_image('bg.jpg', screen), (750, 500))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 190
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 320
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


class Congratulations(Window):
    def __init__(self):
        super().__init__()
        self.fl = False
        self.run()

    def run(self):
        pygame.init()
        pygame.mixer.music.load("sprites\\Music\\menu.mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()

        screen = pygame.display.set_mode((750, 500))
        intro_text = ["Congratulations", "You are the winner",
                      "Press esc to exit",
                      "Press R to restart"]
        make_fon(screen, intro_text)
        run = True
        self.create_particles((320, 240), screen)
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.fl = True
                        run = False
                    if event.key == pygame.K_ESCAPE:
                        self.exitFunc()
            screen.fill((0, 0, 0))
            make_fon(screen, intro_text)
            Particles.draw(screen)
            Particles.update()
            pygame.display.flip()

    def create_particles(self, position, screen):
        # количество создаваемых частиц
        particle_count = 20
        # возможные скорости
        numbers = range(-5, 6)
        for _ in range(particle_count):
            Particle(position, choice(numbers), choice(numbers), Particles, screen)

    def exitFunc(self):
        pygame.quit()
        sys.exit()
