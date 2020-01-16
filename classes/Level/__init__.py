import pygame


class Level:
    def __init__(self):
        data = [[int(i) for i in line] for line in open("1.txt").read().split("\n")]
        data = []
