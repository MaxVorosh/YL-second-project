import pygame
from ..Floor import *


class Level:
    def __init__(self, level, screen):
        self.data = [[int(i) for i in l] for l in open(f"levels\\{level}.txt").read().split("\n")]
        self.screen = screen
        for line in range(len(self.data)):
            for elem in range(len(self.data[line])):
                if self.data[line][elem] == "#":
                    pass  # TODO
                if self.data[line][elem] == "f":
                    self.data[line][elem] = Floor(elem, line)
                if self.data[line][elem] == "w":
                    self.data[line][elem] = None  # Стена.
                    pass  # TODO
                if self.data[line][elem] == "@":
                    self.data[line][elem] = None  # Турель.
                    pass  # TODO