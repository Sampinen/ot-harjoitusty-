import pygame
from screen1buttons import MyButton
class Screen1():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = False

    def run(self):
        #used code from pygame.org website as a layout
        self.running = True
        self.screen.fill("blue")
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frameif
            

            #Pygame functions
            FUNCS = {}
            # RENDER YOUR GAME HERE
            yes_button = MyButton(self.screen,"Kyllä",10,10,True)
            no_button = MyButton(self.screen,"Ei",10,10,True)
            pygame.display.update()

            # flip() the display to put your work on screen

            pygame.display.flip()
            self.clock.tick(60)  # limits FPS to 60
        pygame.quit()
        return print("Program closed")
