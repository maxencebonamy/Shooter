import pygame

from const.const import *
from display.display import Display
from event.event import Event


class Main:

    def __init__(self):
        self.display = Display()
        self.event = Event()

        self.running = True

    def mainloop(self):
        self.event.update()
        self.display.update(self.event)

        if self.event.isQuit() or self.event.keyboard.has(pygame.K_a) or self.display.game.isOver():
            self.running = False
            pygame.quit()

        pygame.time.wait(1000 // GAME_FPS)


if __name__ == '__main__':
    main = Main()
    while main.running:
        main.mainloop()