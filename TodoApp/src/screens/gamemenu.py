"""This file contains all methods for the start menu"""

import pygame
from buttons.gamemenubuttons import MyButton


class GameMenu():
    """Defines gamemenu (the menu that opens when you start a game)"""

    def __init__(self):
        """Initializes needed variables for pygame"""
        pygame.init() # pylint: disable=no-member
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = False
        self.start_button = None
        self.create_start_button = False

    def event_loop(self,events):
        """event loop for start menu"""
        for event in events:
            if event.type == pygame.QUIT: # pylint: disable=no-member
                self.running = False

    def start_menu(self):
        """Defines gamemenu (the menu that opens when you start a game)"""
        # used code from pygame.org website as a layout
        self.running = True
        self.screen.fill("gray")
        self.create_start_button = True
        while self.running:
            events = pygame.event.get()
            self.event_loop(events)

            start = MyButton(self.screen, "Aloita").draw()
            if start:
                return True
            pygame.display.update()

            pygame.display.flip()
            self.clock.tick(60)  # limits FPS to 60
        pygame.quit() # pylint: disable=no-member
        print("Game closed")
        return False
