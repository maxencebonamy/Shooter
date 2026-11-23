import pygame

from const.const import *
from event.event import Event
from game.score import Score


class Player:

    def __init__(self):
        self.image = pygame.image.load('assets/player_1.png')

        self.rect = self.image.get_rect()
        self.rect.center = (0, GAME_HEIGHT // 2)
        self.rect.x = 32

        self.score = Score()

        self.killed = False

    def display(self, screen: pygame.Surface, event: Event):
        self.score.display(screen)
        self.move(screen, event)
        screen.blit(self.image, self.rect)

    def move(self, screen: pygame.Surface, event: Event):
        rect = self.rect.copy()

        if event.keyboard.has(pygame.K_LEFT):
            rect.x -= PLAYER_SPEED
        if event.keyboard.has(pygame.K_RIGHT):
            rect.x += PLAYER_SPEED
        if event.keyboard.has(pygame.K_UP):
            rect.y -= PLAYER_SPEED
        if event.keyboard.has(pygame.K_DOWN):
            rect.y += PLAYER_SPEED

        if screen.get_rect().contains(rect):
            self.rect = rect

    def getPosition(self) -> (int, int):
        return self.rect.center

    def getRect(self) -> pygame.Rect:
        return self.rect

    def kill(self):
        self.killed = True

    def isKilled(self) -> bool:
        return self.killed