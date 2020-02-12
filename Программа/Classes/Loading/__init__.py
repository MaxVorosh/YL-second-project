import pygame


class Loading:
    def __init__(self, screen, length):
        self.screen = screen
        self.count = 0
        self.cell_width = screen.get_width() // 2 // length
        self.cell_height = screen.get_height() // 5
        pygame.draw.rect(screen, (69, 42, 12), (screen.get_width() // 4, screen.get_width() // 5 * 2,
                                                screen.get_width() // 2, screen.get_height() // 5), 3)

    def update(self):
        pygame.draw.rect(self.screen, (0, 100, 0),
                         (self.screen.get_width() // 4 + self.cell_width * self.count,
                          self.screen.get_width() // 5 * 2, self.cell_width, self.cell_height))
        self.count += 1
