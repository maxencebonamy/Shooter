import pygame

from const.const import *


class Wallpaper:

    def __init__(self):
        self.image = pygame.image.load('assets/level_1.png')

        self.rect = self.image.get_rect()
        self.width, self.height = self.rect.width, self.rect.height

        self.x = 0

    def display(self, screen: pygame.Surface):
        self.move()
        x, y = self.x, 0
        while x <= GAME_WIDTH:
            while y <= GAME_HEIGHT:
                screen.blit(self.image, (x, y))
                y += self.height
            x += self.width
            y = 0

    def move(self):
        self.x -= BACKGROUND_SPEED
        if self.x // self.width > 1:
            self.x += self.width