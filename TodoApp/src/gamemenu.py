import pygame
from gamemenubuttons import MyButton
# import pygame_widgets
# from pygame_widgets.button import Button


class GameMenu():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = False
        self.start_button = None
        self.create_start_button = False

    def start_menu(self):
        # used code from pygame.org website as a layout
        self.running = True
        self.screen.fill("gray")
        self.create_start_button = True
        start_game = False
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frameif

            # Pygame functions
            # RENDER YOUR GAME HERE
            start_button = MyButton(self.screen, "Aloita", 10, 10, True)
            pygame.display.update()

            # flip() the display to put your work on screen

            pygame.display.flip()
            self.clock.tick(60)  # limits FPS to 60
        pygame.quit()

        return print("Program closed")

    def IsGameRunning(self):
        return self.running

    def CloseGame(self):
        self.running = False
        return self.running
