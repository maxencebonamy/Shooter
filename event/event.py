import pygame

from event.inputDevice import InputDevice


class Event:

    def __init__(self):
        self.mouse = InputDevice()
        self.keyboard = InputDevice()
        self.mousePosition = 0, 0
        self.quit = False

    def update(self):
        for event in pygame.event.get():

            self.quit = event.type == pygame.QUIT

            if event.type == pygame.MOUSEMOTION:
                self.mousePosition = event.pos

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse.set(event.button)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse.remove(event.button)

            elif event.type == pygame.KEYDOWN:
                self.keyboard.set(event.key)
            elif event.type == pygame.KEYUP:
                self.keyboard.remove(event.key)

    def isQuit(self):
        return self.quit