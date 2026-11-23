import pygame

from const.const import *


class Score:

    def __init__(self):
        self.value = 0

        self.font = pygame.font.Font('assets/beware.ttf', 32)

    def display(self, screen: pygame.Surface):
        text = self.font.render(f'SCORE : {self.value}', True, (100, 100, 100))
        rect = text.get_rect()
        rect.x = GAME_WIDTH - 16 - rect.width
        rect.y = 16

        screen.blit(text, rect)

    def add(self):
        self.value += MONSTER_SCORE