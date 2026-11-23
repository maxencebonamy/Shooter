import pygame
import random

from const.const import *


class Monster:

    def __init__(self):
        self.image = pygame.image.load('assets/monster_1.png')

        self.rect = self.image.get_rect()
        self.rect.center = random.randint(GAME_WIDTH, GAME_WIDTH + 100), random.randint(20, GAME_HEIGHT - 20)

    def display(self, screen: pygame.Surface):
        self.move()
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.x -= MONSTER_SPEED

    def getRect(self) -> pygame.Rect:
        return self.rect

    def getPosition(self) -> (int, int):
        return self.rect.center