import pygame

from const.const import *


class Projectile:

    def __init__(self, playerPosition: (int, int)):
        self.image = pygame.image.load('assets/fire.png')

        self.rect = self.image.get_rect()

        self.rect.center = playerPosition

    def display(self, screen: pygame.Surface):
        self.move()
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.x += FIRE_SPEED

    def getX(self) -> int:
        return self.rect.x

    def getRect(self) -> pygame.Rect:
        return self.rect