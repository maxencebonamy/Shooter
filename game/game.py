import pygame

from const.const import *
from event.event import Event
from game.blast import Blast
from game.monster import Monster
from game.player import Player
from game.projectile import Projectile


class Game:

    def __init__(self):
        self.player = Player()
        self.projectiles = []
        self.monsters = []
        self.blasts = []

        self.over = False

    def display(self, screen: pygame.Surface, event: Event):

        while len(self.monsters) < MONSTER_COUNT:
            self.monsters.append(Monster())

        if event.keyboard.has(pygame.K_SPACE):
            if len(self.projectiles) == 0 or self.projectiles[-1].getX() - 35 >= self.player.getPosition()[0]:
                self.projectiles.append(Projectile(self.player.getPosition()))

        for projectile in self.projectiles:
            projectile.display(screen)
            if projectile.getX() > GAME_WIDTH:
                self.projectiles.remove(projectile)
            else:
                for monster in self.monsters:
                    if projectile.getRect().colliderect(monster.getRect()):
                        self.blasts.append(Blast(monster.getPosition()))
                        self.monsters.remove(monster)
                        self.projectiles.remove(projectile)
                        self.player.score.add()

        for monster in self.monsters:
            monster.display(screen)
            if monster.getPosition()[0] < 0:
                self.over = True
            if self.player.getRect().colliderect(monster.getRect()):
                self.player.kill()
                self.blasts.append(Blast(self.player.getPosition()))
                self.monsters.remove(monster)

        for blast in self.blasts:
            blast.display(screen)
            if blast.isFinished():
                self.blasts.remove(blast)

        if not self.player.isKilled():
            self.player.display(screen, event)

        if self.player.isKilled() and len(self.blasts) == 0:
            self.over = True

    def isOver(self) -> bool:
        return self.over