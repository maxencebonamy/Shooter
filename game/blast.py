import pygame


class Blast:

    def __init__(self, position):
        self.image = pygame.image.load('assets/blast.png')

        self.sprite = self.image.subsurface(0, 0, 64, 64)

        self.rect = self.sprite.get_rect()
        self.rect.center = position

        self.stage = 7

        self.finished = False

    def display(self, screen: pygame.Surface):
        self.sprite = self.image.subsurface(self.stage * 64, 0, 64, 64)

        screen.blit(self.sprite, self.rect)
        self.stage -= 1
        if self.stage < 0:
            self.finished = True

    def isFinished(self) -> bool:
        return self.finished