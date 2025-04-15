"""This file contains all methods for the start menu"""

import pygame
from gamemenubuttons import MyButton


class GameMenu():
    """Defines gamemenu (the menu that opens when you start a game)"""
    def __init__(self):
        """Initializes needed variables for pygame"""
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = False
        self.start_button = None
        self.create_start_button = False

    def start_menu(self):
        """Defines gamemenu (the menu that opens when you start a game)"""
        # used code from pygame.org website as a layout
        self.running = True
        self.screen.fill("gray")
        self.create_start_button = True
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            MyButton(self.screen, "Aloita", 10, 10, True)
            pygame.display.update()

            pygame.display.flip()
            self.clock.tick(60)  # limits FPS to 60
        pygame.quit()

        return print("Program closed")

    def IsGameRunning(self):
        """Meant for testing, tells if the game is running or not"""
        return self.running
