import pygame

from const.const import *
from event.event import Event
from game.game import Game
from game.wallpaper import Wallpaper


class Display:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

        self.game = Game()
        self.wallpaper = Wallpaper()

    def update(self, event: Event):
        self.screen.fill((0, 0, 0))
        self.wallpaper.display(self.screen)
        self.game.display(self.screen, event)
        pygame.display.flip()