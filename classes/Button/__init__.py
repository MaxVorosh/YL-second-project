import pygame
import os


class Button(pygame.sprite.Sprite):
    """
    Класс кнопки в меню.
    """
    def __init__(self, window, path):
        """
        Принимает на вход окно, в котором располагается и путь к своему спрайту.
        :param window: объект окна, в котором располагается
        :param path: путь к спрайту кнопки, не включает папку спрайтов
        """
        super().__init__(window.sprites)
        self.set_image(path)
        self.rect = self.image.get_rect()
        self.func = None

    def resize(self, width, height):
        """
        Изменяет размер кнопки.
        :param width: нужная ширина
        :param height: нужная высота
        :return: ничего
        """
        self.image = pygame.transform.scale(self.image, (width, height))

    def move(self, x, y):
        """
        Перемещает кнопку в окне.
        :param x: нужная х
        :param y: нужная у
        :return: ничео
        """
        self.rect.x = x
        self.rect.y = y

    def set_image(self, path):
        """
        Изменяет картинку.
        :param path: путь до спрайта.
        :return: ничего
        """
        path = os.path.join("sprites", path)
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

    def set_func(self, func):
        """
        Устанавливает необходимую функцию.
        :param func: нужная функция.
        :return:
        """
        self.func = func

    def check_clicked(self, mouse_pos):
        """
        Проверяет, если кнопка нажата.
        :param mouse_pos: координаты щелчка.
        :return: ничего
        """
        if self.rect.x <= mouse_pos[0] <= self.rect.x + self.rect.width and \
                self.rect.y < mouse_pos[1] < self.rect.y + self.rect.height:
            return True
        else:
            return False

    def clicked(self):
        """
        Если нажата.
        :return: ничего
        """
        self.func()
